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
OUTPUT_DIR = '006 analysis/milestones/M5 - Kvantitativ analyse/3.12 scenario-analyse'

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# 2. Last inn data
df = pd.read_csv(DATA_PATH)
campaigns_df = pd.read_csv(CAMPAIGN_PATH)
rules_df = pd.read_csv(RULES_PATH)

# Konverter til datetime
df['ds'] = pd.to_datetime(df['Dato_Sortering'])
campaigns_df['ds'] = pd.to_datetime(campaigns_df['Dato_Sortering'])

# 3. Definer Helligdager og Kampanjer (samme oppsett som 3.11 for at baseline skal være konsistent)
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

# 4. Scenario-simulering
categories = df['Kategori'].unique()
scenario_results = []

for cat in categories:
    print(f"Simulerer scenarier for: {cat}...")
    cat_df = df[df['Kategori'] == cat].copy()
    cat_df = cat_df.rename(columns={'Etterspørsel': 'y'})
    
    # Tren Baseline Modell (samme konfig som 3.11)
    model = Prophet(holidays=all_holidays,
                    yearly_seasonality=True,
                    weekly_seasonality=False,
                    daily_seasonality=False,
                    changepoint_prior_scale=0.05,
                    interval_width=0.90)
    model.fit(cat_df)
    
    future = model.make_future_dataframe(periods=12, freq='MS')
    forecast = model.predict(future)
    
    # Filtrer 2026
    f26 = forecast[forecast['ds'].dt.year == 2026][['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
    f26['Kategori'] = cat
    
    # Hent regler
    rule = rules_df[rules_df['Kategori'] == cat].iloc[0]
    bias = rule['Bias_Justering']
    k_base = rule['Sikkerhetsfaktor_k']
    lift_base = rule['Gjennomsnittlig_Kampanjeloft']
    
    # --- SCENARIO 0: Baseline ---
    # Sigma estimeres fra Prophets 90%-intervall: (yhat_upper - yhat) / 1.645.
    # Identisk med 3.11 slik at baseline-Order_Up_To er sammenfallende.
    f26['y_base'] = f26['yhat'] + bias
    f26['ss_base'] = (f26['yhat_upper'] - f26['yhat']) * (k_base / 1.645)
    f26['out_base'] = f26['y_base'] + f26['ss_base']
    
    # --- SCENARIO 1: Kampanje-sjokk (+50% ekstra løft i Des og Mai) ---
    f26['y_shock'] = f26['y_base'].copy()
    # Identifiser Mai (5) og Desember (12)
    f26.loc[f26['ds'].dt.month == 5, 'y_shock'] += (lift_base * 0.5)
    f26.loc[f26['ds'].dt.month == 12, 'y_shock'] += (lift_base * 0.5)
    # Sikkerhetslageret øker også ved usikkerhet rundt kampanjer
    f26['ss_shock'] = f26['ss_base'] * 1.2 
    f26['out_shock'] = f26['y_shock'] + f26['ss_shock']
    
    # --- SCENARIO 2: Kostnads-sjokk (Kutter sikkerhetslager med 20% pga økt lagerleie) ---
    f26['y_cost'] = f26['y_base']
    f26['ss_cost'] = f26['ss_base'] * 0.8 # Redusert k-faktor implisitt
    f26['out_cost'] = f26['y_cost'] + f26['ss_cost']
    
    scenario_results.append(f26)
    
    # Visualisering per kategori
    plt.figure(figsize=(12, 7))
    plt.plot(f26['ds'], f26['out_base'], 'k--', label='Baseline Order-up-to (M5)', alpha=0.7)
    plt.plot(f26['ds'], f26['out_shock'], 'r-', label='Scenario A: Kampanje-sjokk (+50% lift)', linewidth=2)
    plt.plot(f26['ds'], f26['out_cost'], 'g-', label='Scenario B: Kostnads-kutt (-20% Safety Stock)', linewidth=2)
    
    plt.fill_between(f26['ds'], f26['out_base'], f26['out_shock'], color='red', alpha=0.1)
    plt.fill_between(f26['ds'], f26['out_cost'], f26['out_base'], color='green', alpha=0.1)
    
    plt.title(f'Scenario-analyse 2026: {cat}\nEffekt på nødvendig lagernivå (Order-up-to)')
    plt.xlabel('Måned')
    plt.ylabel('Enheter på lager')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    plt.savefig(f"{OUTPUT_DIR}/scenario_plot_{cat.replace(' ', '_')}.png")
    plt.close()

# Samle og lagre
all_scenarios = pd.concat(scenario_results)
all_scenarios.to_csv(f"{OUTPUT_DIR}/3.12_scenario_resultater.csv", index=False)

# Oppsummeringsrapport
report = []
report.append("# Rapport: 3.12 Scenario-analyse 2026\n")
report.append("Dette dokumentet analyserer hvordan eksterne endringer i 2026 vil påvirke lagerbehovet.\n")

report.append("## Antagelser og datakvalitet")
report.append("- **Sykronisering:** Modellen antar at sesongmønsteret fra de siste 4 årene vil vedvare i 2026.")
report.append("- **Kampanjeløft:** Kampanjeløftet i scenario A er basert på historisk effekt pluss et estimert sjokk (50% økning av gjennomsnittlig løft).")
report.append("- **Prognosekvalitet:** Analysen tar høyde for volatilitet (sikkerhetslager), men ekstreme uforutsette hendelser (f.eks. ny pandemi) er ikke inkludert.\n")

report.append("## Scenariebeskrivelser")
report.append("1. **Baseline:** Basert på optimaliserte parametere fra Aktivitet 3.10.")
report.append("2. **Scenario A (Kampanje-sjokk):** Simulerer en situasjon der kampanjene i mai og desember gir 50% høyere løft enn historisk snitt. Vi øker også sikkerhetslageret med 20% for å håndtere økt volatilitet.")
report.append("3. **Scenario B (Kostnads-sjokk):** Simulerer en 30% økning i lagerkostnader, som tvinger oss til å redusere sikkerhetslageret med 20% for å minimere kapitalbinding.\n")

report.append("## Resultat-oppsummering (Gjennomsnittlig lagernivå 2026)\n")
summary = all_scenarios.groupby('Kategori')[['out_base', 'out_shock', 'out_cost']].mean().round(1)
summary.columns = ['Baseline (Units)', 'Kampanje-sjokk (Units)', 'Kostnads-sjokk (Units)']
report.append(summary.to_markdown())

report.append("\n## Prosentvis endring vs Baseline\n")
perc = (summary.div(summary['Baseline (Units)'], axis=0) - 1) * 100
report.append(perc.round(1).to_markdown())

report.append("\n## Visualiseringer")
for i, cat in enumerate(categories, 1):
    img = f"scenario_plot_{cat.replace(' ', '_')}.png"
    report.append(f'<div align="center">')
    report.append(f'  <img src="{img}" style="width: 70%; height: auto;">')
    report.append(f'  <br>')
    report.append(f'  <em>Figur {i}: Scenario-sammenligning for {cat} i 2026</em>')
    report.append(f'</div>\n')

with open(f"{OUTPUT_DIR}/3.12_scenario_oppsummering.md", "w", encoding="utf-8") as f:
    f.write("\n".join(report))

print(f"Scenario-analyse fullført. Resultater i {OUTPUT_DIR}")
