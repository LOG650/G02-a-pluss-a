import pandas as pd
import numpy as np
from prophet import Prophet
import matplotlib.pyplot as plt
import holidays
import os

# 1. Konfigurasjon og sti-oppsett
DATA_PATH = '004 data/vasket data/master_data_vasket.csv'
CAMPAIGN_PATH = '006 analysis/milestones/M5 - Kvantitativ analyse/3.8 utvidet feature engineering/kampanje_analyse.csv'
RULES_PATH = '006 analysis/milestones/M5 - Kvantitativ analyse/3.10 estimering av kampanjeløft/3.10_optimaliserte_regler.csv'
OUTPUT_DIR = '006 analysis/milestones/M5 - Kvantitativ analyse/3.11 prognoser'

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# 2. Last inn data
df = pd.read_csv(DATA_PATH)
campaigns_df = pd.read_csv(CAMPAIGN_PATH)
rules_df = pd.read_csv(RULES_PATH)

# Konverter til datetime
df['ds'] = pd.to_datetime(df['Dato_Sortering'])
campaigns_df['ds'] = pd.to_datetime(campaigns_df['Dato_Sortering'])

# 3. Definer Helligdager og Kampanjer (likt som i 3.8)
no_holidays = holidays.Norway(years=[2021, 2022, 2023, 2024, 2025, 2026])
christmas_dates = [pd.to_datetime(f"{year}-12-01") for year in range(2021, 2027)]
holidays_df = pd.DataFrame({
  'holiday': 'christmas',
  'ds': christmas_dates,
  'lower_window': 0,
  'upper_window': 0,
})

easter_dates = []
for h_date, name in no_holidays.items():
    if 'Påskedag' in name and 'Andre' not in name:
        easter_dates.append(pd.to_datetime(f"{h_date.year}-{h_date.month:02d}-01"))

easter_df = pd.DataFrame({
  'holiday': 'easter',
  'ds': list(set(easter_dates)),
  'lower_window': 0,
  'upper_window': 0,
})

detected_campaigns = campaigns_df[campaigns_df['Er_Kampanje'] == True][['ds', 'Kategori']].copy()
detected_campaigns['holiday'] = 'promo_' + detected_campaigns['Kategori'].str.replace(' ', '_')
detected_campaigns['lower_window'] = 0
detected_campaigns['upper_window'] = 0

all_holidays = pd.concat([holidays_df, easter_df, detected_campaigns[['holiday', 'ds', 'lower_window', 'upper_window']]])

# 4. Generer prognose for hver kategori
categories = df['Kategori'].unique()
all_forecasts = []

for cat in categories:
    print(f"Genererer 2026-prognose for: {cat}...")
    cat_df = df[df['Kategori'] == cat].copy()
    cat_df = cat_df.rename(columns={'Etterspørsel': 'y'})
    
    # Tren på ALL historikk (2021-2025)
    # interval_width=0.90 gir et 90% usikkerhetsintervall (z = 1.645), slik at
    # (yhat_upper - yhat) ≈ 1.645 * sigma. Dette gjør sikkerhetslager-formelen
    # nedenfor mattematisk konsistent med standard SS = k * sigma.
    model = Prophet(holidays=all_holidays,
                    yearly_seasonality=True,
                    weekly_seasonality=False,
                    daily_seasonality=False,
                    changepoint_prior_scale=0.05,
                    interval_width=0.90)
    model.fit(cat_df)
    
    # Lag fremtidig tidsramme (hele 2026)
    future = model.make_future_dataframe(periods=12, freq='MS')
    forecast = model.predict(future)
    
    # Filtrer ut kun 2026
    forecast_2026 = forecast[forecast['ds'].dt.year == 2026][['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
    forecast_2026['Kategori'] = cat
    
    # Hent optimaliserte regler for denne kategorien
    rule = rules_df[rules_df['Kategori'] == cat].iloc[0]
    bias_adj = rule['Bias_Justering']
    k = rule['Sikkerhetsfaktor_k']
    
    # Påfør bias-justering på yhat
    forecast_2026['yhat_adj'] = forecast_2026['yhat'] + bias_adj
    
    # Beregn sikkerhetslager (Safety Stock) basert på usikkerhetsintervallet fra Prophet og k-faktoren.
    # (yhat_upper - yhat) / 1.645 estimerer sigma fra Prophet's 90% intervall, og multipliseres med k.
    forecast_2026['Safety_Stock'] = (forecast_2026['yhat_upper'] - forecast_2026['yhat']) * (k / 1.645)
    
    # Beregn Bestillingspunkt (Order-up-to level)
    # Forenklet: s = (Forventet etterspørsel i ledetid) + Sikkerhetslager
    # Her antar vi 1 mnd ledetid for enkelthets skyld i denne visningen
    forecast_2026['Order_Up_To'] = forecast_2026['yhat_adj'] + forecast_2026['Safety_Stock']
    
    all_forecasts.append(forecast_2026)
    
    # Visualisering
    plt.figure(figsize=(10, 6))
    plt.plot(cat_df['ds'], cat_df['y'], label='Historisk Etterspørsel', color='black', alpha=0.5)
    plt.plot(forecast_2026['ds'], forecast_2026['yhat_adj'], label='Justert Prognose 2026', color='blue', linewidth=2)
    plt.fill_between(forecast_2026['ds'], 
                     forecast_2026['yhat_adj'] - forecast_2026['Safety_Stock'], 
                     forecast_2026['yhat_adj'] + forecast_2026['Safety_Stock'], 
                     color='blue', alpha=0.2, label='Sikkerhetslager-sone')
    
    plt.title(f'Etterspørselsprognose 2026: {cat}')
    plt.xlabel('Dato')
    plt.ylabel('Enheter')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plot_path = os.path.join(OUTPUT_DIR, f'prognose_2026_{cat.replace(" ", "_")}.png')
    plt.savefig(plot_path)
    plt.close()

# 5. Lagre samlede resultater
final_forecast_df = pd.concat(all_forecasts)
final_forecast_df.to_csv(os.path.join(OUTPUT_DIR, 'prognoser_2026_alle_kategorier.csv'), index=False)

# 6. Lag oppsummeringsrapport for 3.11
report = []
report.append("# Rapport: 3.11 Prognosegenerering 2026\n")
report.append("Dette dokumentet presenterer de endelige etterspørselsprognosene for 2026, basert på optimaliserte bestillingsregler.\n")

report.append("## Metodikk")
report.append("1. **Full historikk:** Modellen er trent på alle tilgjengelige data fra 2021 til desember 2025.")
report.append("2. **Bias-justering:** Prognosene er korrigert for systematiske skjevheter identifisert i backtestingen (steg 3.9).")
report.append("3. **Sikkerhetslager:** Dynamisk beregning av sikkerhetslager basert på modellens usikkerhetsintervall og de optimaliserte k-faktorene fra steg 3.10.\n")

report.append("## Prognoseoversikt 2026 (Snitt per måned)\n")
summary_table = final_forecast_df.groupby('Kategori')[['yhat_adj', 'Safety_Stock', 'Order_Up_To']].mean().round(2)
report.append(summary_table.to_markdown())

report.append("\n## Visualiseringer")
for cat in categories:
    img_name = f'prognose_2026_{cat.replace(" ", "_")}.png'
    report.append(f'<div align="center">')
    report.append(f'  <img src="{img_name}" style="width: 70%; height: auto;">')
    report.append(f'  <br>')
    report.append(f'  <em>Figur: Prognose og sikkerhetslager for {cat} i 2026</em>')
    report.append(f'</div>\n')

with open(os.path.join(OUTPUT_DIR, '3.11_prognose_oppsummering.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(report))

print(f"2026-prognoser er generert og lagret i {OUTPUT_DIR}")
