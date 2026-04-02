import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Last inn data
df = pd.read_csv('004 data/vasket data/master_data_vasket.csv')

# Konverter dato_sortering til datetime
df['Dato_Sortering'] = pd.to_datetime(df['Dato_Sortering'])

def identify_campaigns(df_cat, category_name):
    # Beregn gjennomsnitt og standardavvik for hver måned over alle år
    monthly_stats = df_cat.groupby(df_cat['Dato_Sortering'].dt.month)['Etterspørsel'].agg(['mean', 'std']).reset_index()
    monthly_stats.columns = ['month', 'monthly_mean', 'monthly_std']
    
    # Slå sammen med hoveddata
    df_cat = df_cat.copy()
    df_cat['month'] = df_cat['Dato_Sortering'].dt.month
    df_cat = df_cat.merge(monthly_stats, on='month')
    
    # Beregn Z-score (avvik fra normalen for den aktuelle måneden)
    # Dette hjelper oss å skille mellom "normal sesong" (f.eks. jul) og "kampanje"
    df_cat['z_score'] = (df_cat['Etterspørsel'] - df_cat['monthly_mean']) / df_cat['monthly_std']
    
    # Identifiser kampanjer (Z-score > 1.5 - altså betydelig høyere enn normalt for den måneden)
    df_cat['Er_Kampanje'] = df_cat['z_score'] > 1.5
    
    return df_cat

# Analyser alle kategorier
categories = df['Kategori'].unique()
results = []

for cat in categories:
    cat_df = df[df['Kategori'] == cat]
    analyzed_cat = identify_campaigns(cat_df, cat)
    results.append(analyzed_cat)

final_df = pd.concat(results)

# Lagre resultatene for videre bruk i 3.8
final_df.to_csv('006 analysis/milestones/M5 - Kvantitativ analyse/3.8 utvidet feature engineering/kampanje_analyse.csv', index=False)

# Lag en enkel oppsummering av funnene
summary = []
summary.append("# Funn fra 3.8 Utvidet Feature Engineering\n")
summary.append("## Identifiserte Kampanjer (Salgstopper utover sesong)")

for cat in categories:
    campaigns = final_df[(final_df['Kategori'] == cat) & (final_df['Er_Kampanje'] == True)]
    summary.append(f"\n### {cat}")
    if campaigns.empty:
        summary.append("- Ingen tydelige enkeltstående kampanjer funnet utover normal sesong.")
    else:
        for idx, row in campaigns.iterrows():
            summary.append(f"- {row['År']} {row['Måned']}: Etterspørsel {row['Etterspørsel']} (Z-score: {row['z_score']:.2f})")

with open('006 analysis/milestones/M5 - Kvantitativ analyse/3.8 utvidet feature engineering/3.8_oppsummering_kampanjer.md', 'w') as f:
    f.write('\n'.join(summary))

print("Analyse av kampanjer og salgstoppe fullført.")
