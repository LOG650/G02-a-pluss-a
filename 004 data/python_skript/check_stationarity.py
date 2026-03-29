import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss
import warnings
warnings.filterwarnings('ignore')

# Konfigurasjon
TRAIN_DATA_PATH = r'004 data/splittet_data/train/train_data.csv'
KATEGORIER = ['Engelsk fiksjon', 'Norske barnebøker', 'Norsk krim']

df = pd.read_csv(TRAIN_DATA_PATH)

results = []

for kat in KATEGORIER:
    df_kat = df[df['Kategori'] == kat].copy()
    series = df_kat['Etterspørsel']
    
    # ADF-test
    adf_res = adfuller(series)
    
    # KPSS-test
    kpss_res = kpss(series, regression='ct')
    
    results.append({
        'Kategori': kat,
        'ADF p-verdi': round(adf_res[1], 4),
        'KPSS p-verdi': round(kpss_res[1], 4),
        'ADF Konkl': 'Stasjonær' if adf_res[1] <= 0.05 else 'Ikke-stasjonær',
        'KPSS Konkl': 'Stasjonær' if kpss_res[1] > 0.05 else 'Ikke-stasjonær'
    })

res_df = pd.DataFrame(results)
print(res_df.to_markdown(index=False))
