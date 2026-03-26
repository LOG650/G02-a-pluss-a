import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Konfigurasjon
file_path = '004 data/processed/master_data_vasket.csv'
output_dir = '006 visualisation'
sns.set_theme(style="whitegrid")

# Opprett output-mappe hvis den ikke finnes
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Les data
df = pd.read_csv(file_path)
df['Dato_Sortering'] = pd.to_datetime(df['Dato_Sortering'])

# Mapping for måneder for å sikre riktig sortering
month_map = {
    'Januar': 1, 'Februar': 2, 'Mars': 3, 'April': 4, 'Mai': 5, 'Juni': 6,
    'Juli': 7, 'August': 8, 'September': 9, 'Oktober': 10, 'November': 11, 'Desember': 12
}
df['Måned_Nr'] = df['Måned'].map(month_map)

# 07. Totalt salg pr år
plt.figure(figsize=(10, 6))
yearly_sales = df.groupby('År')['Salg'].sum().reset_index()
ax7 = sns.barplot(data=yearly_sales, x='År', y='Salg', palette='viridis', hue='År', legend=False)
for p in ax7.patches:
    ax7.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                 ha='center', va='bottom', xytext=(0, 5), textcoords='offset points', fontsize=11, fontweight='bold')
plt.title('Totalt salg per år (2021-2025)', fontsize=15, fontweight='bold')
plt.ylabel('Antall enheter solgt', fontsize=12)
plt.tight_layout()
plt.savefig(f'{output_dir}/07_totalt_salg_per_aar.png')
plt.close()

# 08. Gjennomsnittlig salg pr måned
plt.figure(figsize=(12, 6))
monthly_avg_sales = df.groupby(['Måned_Nr', 'Måned'])['Salg'].mean().reset_index().sort_values('Måned_Nr')
ax8 = sns.barplot(data=monthly_avg_sales, x='Måned', y='Salg', palette='magma', hue='Måned', legend=False)
for p in ax8.patches:
    ax8.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                 ha='center', va='bottom', xytext=(0, 5), textcoords='offset points', fontsize=10, fontweight='bold')
plt.title('Gjennomsnittlig salg per måned (2021-2025)', fontsize=15, fontweight='bold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f'{output_dir}/08_gjennomsnittlig_salg_per_maaned.png')
plt.close()

# 09. Graf for sesongvariasjoner - VARMEKART
plt.figure(figsize=(14, 8))
pivot_data = df.pivot_table(index='År', columns='Måned_Nr', values='Salg', aggfunc='sum')
month_names = [m for m, nr in sorted(month_map.items(), key=lambda x: x[1])]
pivot_data.columns = month_names
sns.heatmap(pivot_data, annot=True, fmt=".0f", cmap="YlGnBu", linewidths=.5, cbar_kws={'label': 'Totalt salg'})
plt.title('Varmekart: Salgsintensitet per måned og år (2021-2025)', fontsize=16, fontweight='bold', pad=20)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f'{output_dir}/09_sesongvariasjoner_salg.png')
plt.close()

print(f"Visualiseringene 07, 08 og 09 er oppdatert i '{output_dir}/'")
