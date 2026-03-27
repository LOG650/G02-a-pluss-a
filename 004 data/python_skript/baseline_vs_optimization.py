import pandas as pd
import numpy as np

# Konfigurasjon og låste parametere
KATEGORI = 'Norsk krim'
LAGERKOSTNAD = 8
STOCKOUT_KOSTNAD = 95
FAST_BESTILLINGSKOSTNAD = 250  # Fra train_data.csv for Norsk krim

# Stier til data
TRAIN_DATA_PATH = r'004 data\splittet_data\train\train_data.csv'
TEST_DATA_PATH = r'004 data\splittet_data\test\test_data.csv'

def last_og_filtrer_data(path, kategori):
    df = pd.read_csv(path)
    return df[df['Kategori'] == kategori].copy()

def beregn_baseline_parametere(train_df):
    # Enkel baseline: s = snitt etterspørsel i ledetid + 10%, Q = snitt månedsbehov
    snitt_ettersporsel = train_df['Etterspørsel'].mean()
    snitt_ledetid = train_df['Supp_Ledetid (dager)'].mean() / 30  # Konverter til måneder
    
    s_baseline = (snitt_ettersporsel * snitt_ledetid) * 1.10
    Q_baseline = snitt_ettersporsel
    
    return s_baseline, Q_baseline

def simuler_politikk(test_df, s, Q, navn="Baseline"):
    lager = test_df.iloc[0]['Startlager']
    totale_kostnader = 0
    mangel_enheter = 0
    ordre_i_gang = [] # (ankomst_måned, kvantum)
    
    resultater = []
    
    for i, row in test_df.iterrows():
        mnd = row['Måned']
        ettersporsel = row['Etterspørsel']
        ledetid_dager = row['Supp_Ledetid (dager)']
        
        # 1. Motta varer som ankommer denne måneden
        for ankomst, kvantum in ordre_i_gang[:]:
            if i >= ankomst:
                lager += kvantum
                ordre_i_gang.remove((ankomst, kvantum))
        
        # 2. Dekk etterspørsel
        salg = min(lager, ettersporsel)
        stockout = max(0, ettersporsel - lager)
        lager -= salg
        mangel_enheter += stockout
        
        # 3. Kostnadsberegning
        lagerkost = lager * LAGERKOSTNAD
        stockout_kost = stockout * STOCKOUT_KOSTNAD
        bestillings_kost = 0
        
        # 4. Sjekk om vi må bestille
        if lager <= s and not ordre_i_gang:
            bestillings_kost = FAST_BESTILLINGSKOSTNAD
            ankomst_mnd = i + 1 # Forenkling: ankommer neste måned
            ordre_i_gang.append((ankomst_mnd, Q))
            
        totale_kostnader += (lagerkost + stockout_kost + bestillings_kost)
        
        resultater.append({
            'Måned': mnd,
            'Lager': lager,
            'Salg': salg,
            'Stockout': stockout,
            'Totalkost': lagerkost + stockout_kost + bestillings_kost
        })
        
    return pd.DataFrame(resultater), totale_kostnader

# Hovedkjøring
print(f"--- Analyse for {KATEGORI} ---")

train_norsk_krim = last_og_filtrer_data(TRAIN_DATA_PATH, KATEGORI)
test_norsk_krim = last_og_filtrer_data(TEST_DATA_PATH, KATEGORI)

s_base, Q_base = beregn_baseline_parametere(train_norsk_krim)
print(f"Baseline Parametere: s={s_base:.2f}, Q={Q_base:.2f}")

res_base, kost_base = simuler_politikk(test_norsk_krim, s_base, Q_base, "Baseline")
print(f"Totale kostnader Baseline: {kost_base:,.2f} NOK")
print(f"Gjennomsnittlig servicegrad Baseline: {(res_base['Salg'].sum() / test_norsk_krim['Etterspørsel'].sum())*100:.2f}%")

# Enkel Optimalisering (M5 Start)
# EOQ for Q
D = train_norsk_krim['Etterspørsel'].mean() * 12 # Årlig etterspørsel
S = FAST_BESTILLINGSKOSTNAD
H = LAGERKOSTNAD * 12 # Årlig lagerkostnad
Q_opt = np.sqrt((2 * D * S) / H)

# Optimalt s (basert på marginalanalyse)
# P(Demand in LT > s) = H / (H + Stockout_Cost)
P_stockout = LAGERKOSTNAD / (LAGERKOSTNAD + STOCKOUT_KOSTNAD)
# Forenklet: bruker normalfordeling for etterspørsel i ledetid
std_d = train_norsk_krim['Etterspørsel'].std()
mean_lt_d = (D/12) * (train_norsk_krim['Supp_Ledetid (dager)'].mean() / 30)
std_lt_d = std_d * np.sqrt(train_norsk_krim['Supp_Ledetid (dager)'].mean() / 30)

from scipy.stats import norm
z = norm.ppf(1 - P_stockout)
s_opt = mean_lt_d + (z * std_lt_d)

print(f"\nOptimaliserte Parametere: s={s_opt:.2f}, Q={Q_opt:.2f}")

res_opt, kost_opt = simuler_politikk(test_norsk_krim, s_opt, Q_opt, "Optimalisert")
print(f"Totale kostnader Optimalisert: {kost_opt:,.2f} NOK")
print(f"Gjennomsnittlig servicegrad Optimalisert: {(res_opt['Salg'].sum() / test_norsk_krim['Etterspørsel'].sum())*100:.2f}%")

print(f"\nPotensiell besparelse: {((kost_base - kost_opt) / kost_base)*100:.2f}%")
