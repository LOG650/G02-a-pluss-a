import pandas as pd
import numpy as np
from prophet import Prophet
import os

# Konfigurasjon
TRAIN_DATA_PATH = r'004 data/splittet_data/train/train_data.csv'
TEST_DATA_PATH = r'004 data/splittet_data/test/test_data.csv'

KATEGORI_INFO = {
    'Engelsk fiksjon': {'lagerkost': 10, 'stockout_kost': 120, 'bestillingskost': 600},
    'Norske barnebøker': {'lagerkost': 6, 'stockout_kost': 75, 'bestillingskost': 250},
    'Norsk krim': {'lagerkost': 8, 'stockout_kost': 95, 'bestillingskost': 250}
}

norsk_til_engelsk = {
    'Januar': 'January', 'Februar': 'February', 'Mars': 'March', 'April': 'April',
    'Mai': 'May', 'Juni': 'June', 'Juli': 'July', 'August': 'August',
    'September': 'September', 'Oktober': 'October', 'November': 'November', 'Desember': 'December'
}

def vask_dato_df(df):
    def vask_str(dato_str):
        for n, e in norsk_til_engelsk.items():
            if n in dato_str:
                dato_str = dato_str.replace(n, e)
        return dato_str
    df = df.copy()
    df['Måned_Vasket'] = df['Måned'].apply(vask_str)
    df['ds'] = pd.to_datetime(df['År'].astype(str) + ' ' + df['Måned_Vasket'], format='%Y %B')
    return df

train_df = vask_dato_df(pd.read_csv(TRAIN_DATA_PATH))
test_df = vask_dato_df(pd.read_csv(TEST_DATA_PATH))

def simuler_lager_detaljert(data, s_list, Q_list, kost_params):
    lager = data.iloc[0]['Startlager']
    tot_h_kost = 0
    tot_s_kost = 0
    ordre_i_gang = []
    for i in range(len(data)):
        row = data.iloc[i]
        d = row['Etterspørsel']
        for ankomst, kvantum in ordre_i_gang[:]:
            if i >= ankomst:
                lager += kvantum
                ordre_i_gang.remove((ankomst, kvantum))
        salg = min(lager, d)
        stockout = max(0, d - lager)
        lager -= salg
        h = kost_params['lagerkost'] / 12
        cs = kost_params['stockout_kost']
        s = s_list[i]
        Q = Q_list[i]
        if lager <= s and not ordre_i_gang:
            ledetid = int(row['Supp_Ledetid (dager)'] / 30) + 1
            ordre_i_gang.append((i + ledetid, Q))
        tot_h_kost += (lager * h)
        tot_s_kost += (stockout * cs)
    return tot_h_kost, tot_s_kost

print("--- DIAGNOSE RAPPORT ---")
for kat, params in KATEGORI_INFO.items():
    tr = train_df[train_df['Kategori'] == kat]
    te = test_df[test_df['Kategori'] == kat].sort_values('ds')
    
    m = Prophet(yearly_seasonality=True)
    m.fit(tr[['ds', 'Etterspørsel']].rename(columns={'ds': 'ds', 'Etterspørsel': 'y'}))
    forecast = m.predict(te[['ds']])
    
    residualer = forecast['yhat'].values - te['Etterspørsel'].values
    mae = np.mean(np.abs(residualer))
    bias = np.mean(residualer)
    std_err = np.std(residualer)
    
    # Baseline simulation
    snitt_ettersp = tr['Etterspørsel'].mean()
    snitt_lt = tr['Supp_Ledetid (dager)'].mean() / 30
    s_base = (snitt_ettersp * snitt_lt) * 1.10
    Q_base = snitt_ettersp
    h_b, s_b = simuler_lager_detaljert(te, [s_base]*len(te), [Q_base]*len(te), params)
    
    # Prophet simulation
    D_annual = tr['Etterspørsel'].mean() * 12
    Q_opt = np.sqrt((2 * D_annual * params['bestillingskost']) / params['lagerkost'])
    if kat == 'Norsk krim': Q_opt *= 1.5
    s_opt_list = [(row['yhat_upper'] * snitt_lt) for _, row in forecast.iterrows()]
    h_p, s_p = simuler_lager_detaljert(te, s_opt_list, [Q_opt]*len(te), params)

    print(f"\nKATEGORI: {kat}")
    print(f"  Prognose (Figur 10/11):")
    print(f"    - MAE (Gj.snittlig avvik): {mae:.2f} enheter")
    print(f"    - Bias (Systematisk feil): {bias:.2f} (Positiv betyr overestimering)")
    print(f"    - Std Dev (Usikkerhet): {std_err:.2f}")
    print(f"  Kostnad (Figur 12):")
    print(f"    - Baseline: Lagerhold={h_b:.0f}, Stockout={s_b:.0f}")
    print(f"    - Prophet : Lagerhold={h_p:.0f}, Stockout={s_p:.0f}")
    print(f"    - Effekt  : {'Redusert' if s_p < s_b else 'Økt'} stockout med {abs(s_b-s_p):.0f} NOK")
