import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Konfigurasjon
TRAIN_DATA_PATH = r'004 data/splittet_data/train/train_data.csv'
KATEGORI = 'Engelsk fiksjon'

# Last og vask data (gjenbruker vaskelogikk)
norsk_til_engelsk = {
    'Januar': 'January', 'Februar': 'February', 'Mars': 'March', 'April': 'April',
    'Mai': 'May', 'Juni': 'June', 'Juli': 'July', 'August': 'August',
    'September': 'September', 'Oktober': 'October', 'November': 'November', 'Desember': 'December'
}

df = pd.read_csv(TRAIN_DATA_PATH)
df_kat = df[df['Kategori'] == KATEGORI].copy()

# Enkel ADF-test på etterspørsel
print(f"--- ADF-test for {KATEGORI} ---")
result = adfuller(df_kat['Etterspørsel'])

print(f'ADF Statistikk: {result[0]:.4f}')
print(f'p-verdi: {result[1]:.4f}')
print('Kritiske verdier:')
for key, value in result[4].items():
    print(f'\t{key}: {value:.3f}')

if result[1] > 0.05:
    print("\nKonklusjon: Dataene er IKKE stasjonære (p > 0.05).")
else:
    print("\nKonklusjon: Dataene er stasjonære (p <= 0.05).")
