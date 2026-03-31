import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet
import os

# Konfigurasjon
TRAIN_DATA_PATH = r'004 data/splittet_data/train/train_data.csv'
TEST_DATA_PATH = r'004 data/splittet_data/test/test_data.csv'
OUTPUT_DIR = r'006 analysis/figures'

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

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

def simuler_lager_detaljert(data, s_list, Q_list, kost_params):
    lager = data.iloc[0]['Startlager']
    tot_h_kost = 0
    tot_s_kost = 0
    tot_k_kost = 0
    salg_tot = 0
    ettersp_tot = 0
    ordre_i_gang = []
    
    for i in range(len(data)):
        row = data.iloc[i]
        d = row['Etterspørsel']
        ettersp_tot += d
        
        for ankomst, kvantum in ordre_i_gang[:]:
            if i >= ankomst:
                lager += kvantum
                ordre_i_gang.remove((ankomst, kvantum))
        
        salg = min(lager, d)
        stockout = max(0, d - lager)
        lager -= salg
        salg_tot += salg
        
        h = kost_params['lagerkost'] / 12
        cs = kost_params['stockout_kost']
        k = kost_params['bestillingskost']
        
        best_kost = 0
        s = s_list[i]
        Q = Q_list[i]
        
        if lager <= s and not ordre_i_gang:
            best_kost = k
            ledetid = int(row['Supp_Ledetid (dager)'] / 30) + 1
            ordre_i_gang.append((i + ledetid, Q))
            
        tot_h_kost += (lager * h)
        tot_s_kost += (stockout * cs)
        tot_k_kost += best_kost
        
    return tot_h_kost, tot_s_kost, tot_k_kost

# Behandle hver kategori
for kat, params in KATEGORI_INFO.items():
    tr = train_df[train_df['Kategori'] == kat]
    te = test_df[test_df['Kategori'] == kat].sort_values('ds')
    
    # --- PROPHET FORECAST ---
    m = Prophet(yearly_seasonality=True)
    m.fit(tr[['ds', 'Etterspørsel']].rename(columns={'ds': 'ds', 'Etterspørsel': 'y'}))
    future = te[['ds']].copy()
    forecast = m.predict(future)
    
    # 1. FIGUR 10: Forecast vs Actual
    plt.figure(figsize=(12, 6))
    plt.plot(te['ds'], te['Etterspørsel'], label='Faktisk etterspørsel', color='black', marker='o')
    plt.plot(forecast['ds'], forecast['yhat'], label='Predikert (Prophet)', color='blue', linestyle='--')
    plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='blue', alpha=0.2, label='Usikkerhetsintervall')
    plt.title(f'Figur 10: Forecast vs Actual - {kat}', fontsize=14, fontweight='bold')
    plt.ylabel('Etterspørsel (enheter)')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f'10_forecast_vs_actual_{kat.replace(" ", "_")}.png'))
    plt.close()

    # 2. FIGUR 11: Residual Analysis
    residualer = forecast['yhat'].values - te['Etterspørsel'].values
    plt.figure(figsize=(10, 6))
    sns.histplot(residualer, kde=True, color='purple')
    plt.axvline(0, color='red', linestyle='--')
    plt.title(f'Figur 11: Distribusjon av residualer - {kat}', fontsize=14, fontweight='bold')
    plt.xlabel('Prognosefeil (Predikert - Faktisk)')
    plt.ylabel('Frekvens')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f'11_residualer_{kat.replace(" ", "_")}.png'))
    plt.close()

    # 3. FIGUR 12: Cost Breakdown
    # Baseline
    snitt_ettersp = tr['Etterspørsel'].mean()
    snitt_lt = tr['Supp_Ledetid (dager)'].mean() / 30
    s_base = (snitt_ettersp * snitt_lt) * 1.10
    Q_base = snitt_ettersp
    h_b, s_b, k_b = simuler_lager_detaljert(te, [s_base]*len(te), [Q_base]*len(te), params)
    
    # Prophet
    D_annual = tr['Etterspørsel'].mean() * 12
    Q_opt = np.sqrt((2 * D_annual * params['bestillingskost']) / params['lagerkost'])
    if kat == 'Norsk krim': Q_opt *= 1.5
    s_opt_list = [(row['yhat_upper'] * snitt_lt) for _, row in forecast.iterrows()]
    h_p, s_p, k_p = simuler_lager_detaljert(te, s_opt_list, [Q_opt]*len(te), params)

    cost_data = {
        'Modell': ['Baseline', 'Baseline', 'Prophet', 'Prophet'],
        'Type': ['Lagerhold', 'Stockout', 'Lagerhold', 'Stockout'],
        'Kostnad': [h_b, s_b, h_p, s_p]
    }
    cost_df = pd.DataFrame(cost_data)
    
    plt.figure(figsize=(10, 6))
    # Bruker bar_plot for stablede søyler manuelt for bedre kontroll
    bottom_val = [0, 0]
    plt.bar(['Baseline', 'Prophet'], [h_b, h_p], label='Lagerholdskostnad (Ch)', color='skyblue')
    plt.bar(['Baseline', 'Prophet'], [s_b, s_p], bottom=[h_b, h_p], label='Stockoutkostnad (Cs)', color='salmon')
    
    plt.title(f'Figur 12: Kostnadsfordeling (Ch vs Cs) - {kat}', fontsize=14, fontweight='bold')
    plt.ylabel('Totalkostnad (NOK)')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f'12_cost_breakdown_{kat.replace(" ", "_")}.png'))
    plt.close()

print("Nye visualiseringer for M6 er generert!")
