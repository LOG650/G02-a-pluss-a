import pandas as pd
import numpy as np
from prophet import Prophet
import matplotlib.pyplot as plt
import os

# Konfigurasjon
TRAIN_DATA_PATH = r'004 data/splittet_data/train/train_data.csv'
OUTPUT_DIR = r'006 analysis/milestones/M5 - Kvantitativ analyse/3.5 kvantitativ modell'
KATEGORIER = ['Engelsk fiksjon', 'Norske barnebøker', 'Norsk krim']

# Definer helligdager (Jul, Påske, Skolestart)
jul = pd.DataFrame({
    'holiday': 'jul',
    'ds': pd.to_datetime(['2021-12-24', '2022-12-24', '2023-12-24', '2024-12-24', '2025-12-24']),
    'lower_window': -15,
    'upper_window': 0,
})

paske = pd.DataFrame({
    'holiday': 'paske',
    'ds': pd.to_datetime(['2021-04-04', '2022-04-17', '2023-04-09', '2024-03-31', '2025-04-20']),
    'lower_window': -10,
    'upper_window': 0,
})

skolestart = pd.DataFrame({
    'holiday': 'skolestart',
    'ds': pd.to_datetime(['2021-08-16', '2022-08-15', '2023-08-21', '2024-08-19', '2025-08-18']),
    'lower_window': -7,
    'upper_window': 7,
})

holidays = pd.concat((jul, paske, skolestart))

# Last data
df = pd.read_csv(TRAIN_DATA_PATH)

# Håndter norske månedsnavn
norsk_til_engelsk = {
    'Januar': 'January', 'Februar': 'February', 'Mars': 'March', 'April': 'April',
    'Mai': 'May', 'Juni': 'June', 'Juli': 'July', 'August': 'August',
    'September': 'September', 'Oktober': 'October', 'November': 'November', 'Desember': 'December'
}

def vask_dato(dato_str):
    for n, e in norsk_til_engelsk.items():
        if n in dato_str:
            dato_str = dato_str.replace(n, e)
    return dato_str

df['Måned'] = df['Måned'].apply(vask_dato)
df['ds'] = pd.to_datetime(df['År'].astype(str) + ' ' + df['Måned'], format='%Y %B')

stats_summary = []

for kat in KATEGORIER:
    print(f"Analyserer {kat}...")
    kat_df = df[df['Kategori'] == kat].copy()
    
    # Prophet format: ds (date), y (value)
    prophet_df = kat_df[['ds', 'Etterspørsel']].rename(columns={'ds': 'ds', 'Etterspørsel': 'y'})
    
    # Tren modell
    m = Prophet(holidays=holidays, yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    m.fit(prophet_df)
    
    # Lag fremtidige datoer (12 måneder)
    future = m.make_future_dataframe(periods=12, freq='ME')
    forecast = m.predict(future)
    
    # Lagre plot av komponenter (forstørret skrift + norske etiketter)
    LABEL_MAP_NB = {
        'trend': 'Trend (enheter)',
        'ds': 'Dato',
        'holidays': 'Helligdager (enheter)',
        'yearly': 'Årlig sesong (enheter)',
        'Day of year': 'Dag i året',
    }
    fig = m.plot_components(forecast)
    fig.set_size_inches(13, 12)
    for ax in fig.axes:
        ax.tick_params(axis='both', labelsize=12)
        if ax.get_xlabel() in LABEL_MAP_NB:
            ax.set_xlabel(LABEL_MAP_NB[ax.get_xlabel()], fontsize=13)
        else:
            ax.xaxis.label.set_fontsize(13)
        if ax.get_ylabel() in LABEL_MAP_NB:
            ax.set_ylabel(LABEL_MAP_NB[ax.get_ylabel()], fontsize=13)
        else:
            ax.yaxis.label.set_fontsize(13)
        ax.grid(True, alpha=0.35)
    fig.suptitle(f'Sesong- og trendkomponenter: {kat}', fontsize=15, fontweight='bold', y=0.995)
    fig.tight_layout(rect=(0, 0, 1, 0.985))
    plot_path = os.path.join(OUTPUT_DIR, f'prophet_components_{kat.replace(" ", "_")}.png')
    fig.savefig(plot_path, dpi=160, bbox_inches='tight')
    plt.close(fig)
    
    # Trekk ut noen nøkkeltall
    trend_start = forecast['trend'].iloc[0]
    trend_end = forecast['trend'].iloc[-1]
    trend_change = ((trend_end - trend_start) / trend_start) * 100
    
    # Maksimal sesongeffekt (amplitude)
    yearly = forecast['yearly'].abs().max()
    
    stats_summary.append({
        'Kategori': kat,
        'Trend_Endring (%)': trend_change,
        'Sesong_Amplitude (enheter)': yearly,
        'Plot': f'prophet_components_{kat.replace(" ", "_")}.png'
    })

# Lagre en oppsummeringsfil for M5
summary_df = pd.DataFrame(stats_summary)
summary_path = os.path.join(OUTPUT_DIR, 'M5_Analyse_Oppsummering.md')

with open(summary_path, 'w') as f:
    f.write("# Oppsummering av Sesong- og Trendanalyse (M5)\n\n")
    f.write("Denne analysen er utført med Prophet-modellen og danner grunnlaget for de dynamiske bestillingsreglene.\n\n")
    f.write(summary_df.to_markdown(index=False))
    f.write("\n\n*Notat: Trend_Endring viser utviklingen over hele analyseperioden (2021-2026).*")

print("Ferdig!")
