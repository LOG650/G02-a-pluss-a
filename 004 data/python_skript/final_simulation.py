import pandas as pd
import numpy as np
from prophet import Prophet
from scipy.stats import norm
import os

# Konfigurasjon
TRAIN_DATA_PATH = r'004 data/splittet_data/train/train_data.csv'
TEST_DATA_PATH = r'004 data/splittet_data/test/test_data.csv'
OUTPUT_DIR = r'006 analysis/milestones/M5 - Kvantitativ analyse/3.5 kvantitativ modell'

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

# Last og vask data
train_df = vask_dato_df(pd.read_csv(TRAIN_DATA_PATH))
test_df = vask_dato_df(pd.read_csv(TEST_DATA_PATH))

def simuler_lager(data, s_list, Q_list, kost_params):
    lager = data.iloc[0]['Startlager']
    tot_kost = 0
    salg_tot = 0
    ettersp_tot = 0
    ordre_i_gang = [] # (ankomst_idx, kvantum)
    
    for i in range(len(data)):
        row = data.iloc[i]
        d = row['Etterspørsel']
        ettersp_tot += d
        
        # 1. Motta varer
        for ankomst, kvantum in ordre_i_gang[:]:
            if i >= ankomst:
                lager += kvantum
                ordre_i_gang.remove((ankomst, kvantum))
        
        # 2. Salg
        salg = min(lager, d)
        stockout = max(0, d - lager)
        lager -= salg
        salg_tot += salg
        
        # 3. Kostnader
        h = kost_params['lagerkost'] / 12 # Per måned
        cs = kost_params['stockout_kost']
        k = kost_params['bestillingskost']
        
        best_kost = 0
        s = s_list[i]
        Q = Q_list[i]
        
        if lager <= s and not ordre_i_gang:
            best_kost = k
            ledetid = int(row['Supp_Ledetid (dager)'] / 30) + 1 # Minst 1 mnd ledetid i denne modellen
            ordre_i_gang.append((i + ledetid, Q))
            
        tot_kost += (lager * h + stockout * cs + best_kost)
        
    return tot_kost, (salg_tot / ettersp_tot) * 100

sammenligning = []

for kat, params in KATEGORI_INFO.items():
    print(f"Simulerer {kat}...")
    tr = train_df[train_df['Kategori'] == kat]
    te = test_df[test_df['Kategori'] == kat]
    
    # --- BASELINE ---
    snitt_ettersp = tr['Etterspørsel'].mean()
    snitt_lt = tr['Supp_Ledetid (dager)'].mean() / 30
    s_base = (snitt_ettersp * snitt_lt) * 1.10
    Q_base = snitt_ettersp
    
    kost_base, sl_base = simuler_lager(te, [s_base]*len(te), [Q_base]*len(te), params)
    
    # --- PROPHET OPTIMALISERT ---
    # 1. Tren Prophet
    m = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    m.fit(tr[['ds', 'Etterspørsel']].rename(columns={'ds': 'ds', 'Etterspørsel': 'y'}))
    
    # 2. Prediker for test-perioden
    future = te[['ds']].copy()
    forecast = m.predict(future)
    
    # 3. Beregn dynamiske s og Q
    D_annual = tr['Etterspørsel'].mean() * 12
    Q_opt = np.sqrt((2 * D_annual * params['bestillingskost']) / params['lagerkost'])
    
    # Justering for ekstreme svingninger i Norsk krim
    if kat == 'Norsk krim':
        Q_opt *= 1.5
    
    s_opt_list = []
    
    for _, row in forecast.iterrows():
        # Bruker yhat_upper for å inkludere usikkerhetsmargin direkte fra Prophet
        d_pred_upper = row['yhat_upper']
        s_val = (d_pred_upper * snitt_lt)
        s_opt_list.append(max(0, s_val))
        
    kost_opt, sl_opt = simuler_lager(te, s_opt_list, [Q_opt]*len(te), params)
    
    sammenligning.append({
        'Kategori': kat,
        'Kostnad Baseline': round(kost_base, 2),
        'Kostnad Optimalisert': round(kost_opt, 2),
        'Besparelse (%)': round(((kost_base - kost_opt) / kost_base) * 100, 2),
        'SL Baseline (%)': round(sl_base, 2),
        'SL Optimalisert (%)': round(sl_opt, 2)
    })

# Lagre resultater
res_df = pd.DataFrame(sammenligning)
res_path = os.path.join(OUTPUT_DIR, 'M5_Sluttresultater_Simulering.md')

with open(res_path, 'w') as f:
    f.write("# Sluttresultater - Kvantitativ Analyse (M5)\n\n")
    f.write("Sammenligning av Baseline ((s, Q) basert på snitt) mot Prophet-optimalisert modell.\n\n")
    f.write(res_df.to_markdown(index=False))

print("Simulering ferdig!")
