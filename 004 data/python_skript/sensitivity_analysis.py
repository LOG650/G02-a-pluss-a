import pandas as pd
import numpy as np
from prophet import Prophet
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasjon
TRAIN_DATA_PATH = r'004 data/splittet_data/train/train_data.csv'
TEST_DATA_PATH = r'004 data/splittet_data/test/test_data.csv'
OUTPUT_DIR = r'006 analysis/milestones/M5 - Kvantitativ analyse/3.7 sensitivitetsanalyse'
FIGURES_DIR = r'006 analysis/figures'

if not os.path.exists(FIGURES_DIR):
    os.makedirs(FIGURES_DIR)
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

def simuler_lager(data, s_list, Q_list, kost_params, lt_multiplier=1.0):
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
        h = kost_params['lagerkost'] / 12
        cs = kost_params['stockout_kost']
        k = kost_params['bestillingskost']
        
        best_kost = 0
        s = s_list[i]
        Q = Q_list[i]
        
        if lager <= s and not ordre_i_gang:
            best_kost = k
            ledetid = int((row['Supp_Ledetid (dager)'] * lt_multiplier) / 30) + 1
            ordre_i_gang.append((i + ledetid, Q))
            
        tot_kost += (lager * h + stockout * cs + best_kost)
        
    return tot_kost, (salg_tot / ettersp_tot) * 100

# Last data
train_df = vask_dato_df(pd.read_csv(TRAIN_DATA_PATH))
test_df = vask_dato_df(pd.read_csv(TEST_DATA_PATH))

results = []

for kat, base_params in KATEGORI_INFO.items():
    print(f"Analyserer sensitivitet for {kat}...")
    tr = train_df[train_df['Kategori'] == kat]
    te = test_df[test_df['Kategori'] == kat]
    
    # Tren Prophet
    m = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    m.fit(tr[['ds', 'Etterspørsel']].rename(columns={'ds': 'ds', 'Etterspørsel': 'y'}))
    future = te[['ds']].copy()
    forecast = m.predict(future)
    
    snitt_lt = tr['Supp_Ledetid (dager)'].mean() / 30
    D_annual = tr['Etterspørsel'].mean() * 12
    
    # Parametere som skal testes (norske navn — vises som legendetekst i figurene)
    test_configs = [
        ('Stockout-kostnad', [0.5, 0.75, 1.0, 1.25, 1.5], 'stockout_kost'),
        ('Lagerholdskostnad', [0.8, 1.0, 1.2], 'lagerkost'),
        ('Sikkerhetsmargin-faktor', [0.8, 1.0, 1.2, 1.5, 2.0], None)
    ]

    for param_name, factors, key in test_configs:
        for f in factors:
            if param_name == 'Sikkerhetsmargin-faktor' and f == 1.0 and any(r['Parameter'] == 'Stockout-kostnad' and r['Faktor'] == 1.0 and r['Kategori'] == kat for r in results):
                continue
            if param_name == 'Lagerholdskostnad' and f == 1.0: continue
            
            p = base_params.copy()
            if key:
                p[key] *= f
                
            # Oppdater Q_opt ved endring i kostnader
            Q_opt = np.sqrt((2 * D_annual * p['bestillingskost']) / p['lagerkost'])
            if kat == 'Norsk krim': Q_opt *= 1.5
            
            # Oppdater s_opt
            safety_factor = f if param_name == 'Sikkerhetsmargin-faktor' else 1.0
            s_opt_list = [(row['yhat_upper'] * snitt_lt * safety_factor) for _, row in forecast.iterrows()]
            
            kost, sl = simuler_lager(te, s_opt_list, [Q_opt]*len(te), p)
            results.append({'Kategori': kat, 'Parameter': param_name, 'Faktor': f, 'Kostnad': round(kost, 2), 'ServiceLevel': round(sl, 2)})

res_df = pd.DataFrame(results)

# Generer figurer
for kat in KATEGORI_INFO.keys():
    kat_df = res_df[res_df['Kategori'] == kat]
    
    # Kostnadssensitivitet (refereres i rapporten som Figur 8.5/8.7/8.9)
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=kat_df, x='Faktor', y='Kostnad', hue='Parameter', marker='o', linewidth=2)
    plt.title(f'Kostnadssensitivitet – {kat}', fontsize=14, fontweight='bold')
    plt.xlabel('Multiplikator på basisverdi', fontsize=12)
    plt.ylabel('Totalkostnad (NOK)', fontsize=12)
    plt.tick_params(axis='both', labelsize=11)
    plt.legend(title='Parameter', fontsize=11, title_fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, f'13_sensitivitet_kost_{kat.replace(" ", "_")}.png'), dpi=150)
    plt.close()

    # Servicenivå-sensitivitet (refereres i rapporten som Figur 8.6/8.8/8.10)
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=kat_df, x='Faktor', y='ServiceLevel', hue='Parameter', marker='s', linewidth=2)
    plt.title(f'Servicenivå-sensitivitet – {kat}', fontsize=14, fontweight='bold')
    plt.xlabel('Multiplikator på basisverdi', fontsize=12)
    plt.ylabel('Servicenivå (%)', fontsize=12)
    plt.tick_params(axis='both', labelsize=11)
    plt.legend(title='Parameter', fontsize=11, title_fontsize=11, loc='lower right')
    plt.ylim(0, 105)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, f'14_sensitivitet_service_{kat.replace(" ", "_")}.png'), dpi=150)
    plt.close()

# Lagre rådata til CSV for reproduserbarhet. Kuratert aktivitetsdokument
# (`3.7_Sensitivitetsanalyse.md`) oppdateres manuelt med disse tallene og
# tilhørende fortolkning, og overskrives derfor ikke av skriptet.
csv_path = os.path.join(OUTPUT_DIR, 'sensitivity_results.csv')
res_df.to_csv(csv_path, index=False, encoding='utf-8')

print("Sensitivitetsanalyse ferdig! Figurer lagret til %s og rådata til %s." % (FIGURES_DIR, csv_path))

