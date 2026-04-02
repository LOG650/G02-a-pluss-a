import pandas as pd
import numpy as np
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import holidays
import os

# 1. Last inn data
df = pd.read_csv('004 data/vasket data/master_data_vasket.csv')
campaigns_df = pd.read_csv('006 analysis/milestones/M5 - Kvantitativ analyse/3.8 utvidet feature engineering/kampanje_analyse.csv')

# Konverter til datetime
df['ds'] = pd.to_datetime(df['Dato_Sortering'])
campaigns_df['ds'] = pd.to_datetime(campaigns_df['Dato_Sortering'])

# 2. Definer Helligdager (Jul og Påske)
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

# 3. Legg til de identifiserte kampanjene som egne "holidays"
detected_campaigns = campaigns_df[campaigns_df['Er_Kampanje'] == True][['ds', 'Kategori']].copy()
detected_campaigns['holiday'] = 'promo_' + detected_campaigns['Kategori'].str.replace(' ', '_')
detected_campaigns['lower_window'] = 0
detected_campaigns['upper_window'] = 0

all_holidays = pd.concat([holidays_df, easter_df, detected_campaigns[['holiday', 'ds', 'lower_window', 'upper_window']]])

def calculate_metrics(actual, forecast):
    mae = mean_absolute_error(actual, forecast)
    rmse = np.sqrt(mean_squared_error(actual, forecast))
    # Bruker MAPE (Mean Absolute Percentage Error) for relativ nøyaktighet
    # Legger til en liten epsilon for å unngå divisjon med null (selv om usannsynlig her)
    mape = np.mean(np.abs((actual - forecast) / (actual + 1e-10))) * 100
    bias = np.mean(forecast - actual)
    return mae, rmse, mape, bias

def run_validation(category_name):
    cat_df = df[df['Kategori'] == category_name].copy()
    cat_df = cat_df.rename(columns={'Etterspørsel': 'y'})
    
    # 12 måneder test (siste år: 2025)
    train = cat_df.iloc[:-12]
    test = cat_df.iloc[-12:]
    
    model = Prophet(holidays=all_holidays, 
                    yearly_seasonality=True, 
                    weekly_seasonality=False, 
                    daily_seasonality=False,
                    changepoint_prior_scale=0.05)
    
    model.fit(train)
    
    future = model.make_future_dataframe(periods=12, freq='MS')
    forecast = model.predict(future)
    
    # Hent prediksjoner for test-perioden
    pred = forecast.iloc[-12:]['yhat'].values
    actual = test['y'].values
    
    mae, rmse, mape, bias = calculate_metrics(actual, pred)
    
    # Generer plot: Faktisk vs. Prognose
    plt.figure(figsize=(10, 6))
    plt.plot(cat_df['ds'], cat_df['y'], label='Faktisk etterspørsel (Full historikk)', color='black', alpha=0.3)
    plt.plot(test['ds'], actual, label='Faktisk (Testperiode 2025)', color='blue', marker='o')
    plt.plot(test['ds'], pred, label='Prognose (Modell)', color='red', linestyle='--', marker='x')
    plt.title(f'Modellvalidering (Backtesting): {category_name}')
    plt.xlabel('Dato')
    plt.ylabel('Etterspørsel (Enheter)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    img_filename = f'validering_{category_name.replace(" ", "_")}.png'
    img_path = f'006 analysis/milestones/M5 - Kvantitativ analyse/3.9/{img_filename}'
    
    plt.savefig(img_path)
    plt.close()
    
    return {
        'Kategori': category_name,
        'MAE': round(mae, 2),
        'RMSE': round(rmse, 2),
        'MAPE (%)': round(mape, 2),
        'Bias': round(bias, 2),
        'Img': img_filename
    }

# Kjør validering
categories = df['Kategori'].unique()
results = []
for cat in categories:
    print(f"Validerer modell for: {cat}...")
    res = run_validation(cat)
    results.append(res)

results_df = pd.DataFrame(results)

# Generer rapport i 3.9-mappen
report_path = '006 analysis/milestones/M5 - Kvantitativ analyse/3.9/3.9_validering_resultater.md'
with open(report_path, 'w') as f:
    f.write("# Rapport: 3.9 Modellvalidering (Backtesting)\n\n")
    f.write("## Metodikk\n")
    f.write("I denne fasen har vi gjennomført en grundig modellvalidering ved bruk av 'backtesting'. Dette er et kritisk steg for å verifisere at den forbedrede Prophet-modellen (inkl. helligdager og kampanjer) fungerer stabilt over tid.\n\n")
    f.write("- **Testperiode:** Siste 12 måneder av historikken (januar-desember 2025).\n")
    f.write("- **Treningsperiode:** Fire år med historiske data (2021-2024).\n")
    f.write("- **Målsetting:** Bekrefte at MAPE er på et akseptabelt nivå for lagerstyring, og identifisere eventuelle systematiske bias (feilretning).\n\n")
    
    f.write("## Valideringsresultater (2025)\n\n")
    f.write(results_df[['Kategori', 'MAE', 'RMSE', 'MAPE (%)', 'Bias']].to_markdown(index=False))
    
    f.write("\n\n## Detaljert Analyse\n")
    for idx, row in results_df.iterrows():
        f.write(f"### {row['Kategori']}\n")
        f.write(f"- **MAPE på {row['MAPE (%)']}%:** Dette indikerer at modellen i gjennomsnitt treffer innenfor {row['MAPE (%)']}% av faktisk etterspørsel per måned.\n")
        bias_text = "svak overvurdering" if row['Bias'] > 0 else "svak undervurdering"
        f.write(f"- **Bias ({row['Bias']}):** Modellen viser en {bias_text} av etterspørselen, noe som er viktig informasjon ved fastsettelse av sikkerhetslager.\n\n")
        
        f.write(f'<div align="center">\n')
        f.write(f'  <img src="{row["Img"]}" style="width: 70%; height: auto;">\n')
        f.write(f'  <br>\n')
        f.write(f'  <em>Figur {idx+1}: Faktisk vs. Prognose for {row["Kategori"]} i teståret 2025</em>\n')
        f.write(f'</div>\n\n')

print(f"Modellvalidering fullført. Rapport lagret i {report_path}")
