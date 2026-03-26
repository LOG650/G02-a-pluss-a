import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import os
import numpy as np

# Konfigurasjon
file_path = '004 data/processed/master_data_vasket.csv'
output_dir = '006 visualisation'
sns.set_theme(style="whitegrid")

# Les data
df = pd.read_csv(file_path)
df['Dato_Sortering'] = pd.to_datetime(df['Dato_Sortering'])
df = df.sort_values('Dato_Sortering')

# Funksjon for å formatere X-aksen (Måneder/År)
def format_x_axis(ax):
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3)) 
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.xticks(rotation=90)

# 1. Etterspørsel, Salg og Sluttlager over tid
plt.figure(figsize=(14, 7))
df_total = df.groupby('Dato_Sortering').agg({'Etterspørsel': 'sum', 'Salg': 'sum', 'Sluttlager': 'sum'}).reset_index()
plt.plot(df_total['Dato_Sortering'], df_total['Etterspørsel'], label='Etterspørsel', marker='o', color='blue', alpha=0.6)
plt.plot(df_total['Dato_Sortering'], df_total['Salg'], label='Salg', linestyle='--', color='green', alpha=0.6)
plt.fill_between(df_total['Dato_Sortering'], df_total['Sluttlager'], alpha=0.2, label='Lagerbeholdning', color='gray')
format_x_axis(plt.gca())
plt.title('Etterspørsel, Salg og Lagernivå Over Tid (2021-2025)', fontsize=15, fontweight='bold')
plt.ylabel('Antall enheter', fontsize=12)
plt.legend()
plt.tight_layout()
plt.savefig(f'{output_dir}/01_ettersporsel_salg_lager.png')
plt.close()

# 2. Restordre (Stockout) Utvikling - MED SEPARASJON
plt.figure(figsize=(20, 10))
stockout_months = df.groupby('Dato_Sortering')['Restordre (stockout)'].sum()
dates_to_keep = stockout_months[stockout_months > 0].index
df_filtered_02 = df[df['Dato_Sortering'].isin(dates_to_keep)].copy()
df_filtered_02['Måned_År'] = df_filtered_02['Dato_Sortering'].dt.strftime('%b %Y')

df_pivot_02 = df_filtered_02.pivot_table(index='Måned_År', columns='Kategori', values='Restordre (stockout)', aggfunc='sum', fill_value=0)
sorted_months_02 = df_filtered_02.sort_values('Dato_Sortering')['Måned_År'].unique()
df_pivot_02 = df_pivot_02.reindex(sorted_months_02)
df_full_02 = df_pivot_02.reset_index().melt(id_vars='Måned_År', value_name='Restordre (stockout)')

ax2 = sns.barplot(data=df_full_02, x='Måned_År', y='Restordre (stockout)', hue='Kategori', errorbar=None)

# --- Legg til separasjonshjelp ---
for i in range(len(sorted_months_02)):
    # Bakgrunnsfarge på annenhver måned (Sebra-striper)
    if i % 2 == 0:
        plt.axvspan(i - 0.5, i + 0.5, color='gray', alpha=0.07, zorder=0)
    # Vertikal skillelinje mellom måneder
    if i < len(sorted_months_02) - 1:
        plt.axvline(i + 0.5, color='gray', linestyle='--', alpha=0.2, linewidth=1)

# Legg til tallverdier
for p in ax2.patches:
    height = p.get_height()
    x_center = p.get_x() + p.get_width() / 2.
    if height <= 0:
        ax2.plot([p.get_x() + p.get_width()*0.1, p.get_x() + p.get_width()*0.9], [0.5, 0.5], color='lightgray', linewidth=1)
        ax2.annotate('0', (x_center, 1), ha='center', va='bottom', fontsize=7, color='gray', rotation=90)
    else:
        ax2.annotate(f'{int(height)}', (x_center, height), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points', fontsize=9, fontweight='bold', rotation=90)

plt.title('Restordre (Stockouts) per Kategori: Separert per måned (2021-2025)', fontsize=16, fontweight='bold')
plt.xticks(rotation=90)
plt.legend(title='Kategori', bbox_to_anchor=(1.01, 1), loc='upper left')
plt.ylim(0, df_full_02['Restordre (stockout)'].max() * 1.4)
plt.tight_layout()
plt.savefig(f'{output_dir}/02_stockouts_over_tid.png')
plt.close()

# 3. Kategori Fordeling
plt.figure(figsize=(10, 7))
category_demand = df.groupby('Kategori')['Etterspørsel'].sum().sort_values(ascending=False)
category_demand.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('pastel'), startangle=140)
plt.title('Fordeling av total etterspørsel per kategori (2021-2025)', fontsize=15, fontweight='bold')
plt.ylabel('')
plt.tight_layout()
plt.savefig(f'{output_dir}/03_kategori_fordeling_total.png')
plt.close()

# 4. Kostnads-Tradeoff
df['Lager_Kost'] = df['Sluttlager'] * df['Kostnad_Lagerkostnad']
df['Stockout_Kost'] = df['Restordre (stockout)'] * df['Kostnad_Stockout-kostnad']
df_costs = df.groupby('Dato_Sortering').agg({'Lager_Kost': 'sum', 'Stockout_Kost': 'sum'}).reset_index()
plt.figure(figsize=(14, 7))
plt.stackplot(df_costs['Dato_Sortering'], df_costs['Lager_Kost'], df_costs['Stockout_Kost'], 
              labels=['Lagerholdskostnad', 'Stockout-kostnad'], colors=['#95a5a6', '#e74c3c'], alpha=0.7)
format_x_axis(plt.gca())
plt.title('Kostnads-Tradeoff: Lagerhold vs Stockout (2021-2025)', fontsize=15, fontweight='bold')
plt.ylabel('Kostnad (NOK)', fontsize=12)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig(f'{output_dir}/04_kostnads_tradeoff.png')
plt.close()

# 5. Totalt Svinn
plt.figure(figsize=(10, 7))
svinn_total = df.groupby('Kategori')['Svinn'].sum().sort_values(ascending=False).reset_index()
ax5 = sns.barplot(data=svinn_total, x='Kategori', y='Svinn', palette='Reds_r', hue='Kategori', legend=False)
for p in ax5.patches:
    ax5.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                 ha='center', va='bottom', xytext=(0, 5), textcoords='offset points', fontsize=12, fontweight='bold')
plt.title('Totalt akkumulert svinn per kategori (2021-2025)', fontsize=15, fontweight='bold')
plt.ylabel('Enheter mistet/skadet', fontsize=12)
plt.ylim(0, svinn_total['Svinn'].max() * 1.15)
plt.tight_layout()
plt.savefig(f'{output_dir}/05_svinn_total_oversikt.png')
plt.close()

# 6. Bestillingsmønster - MED SEPARASJON
plt.figure(figsize=(24, 10))
all_orders = df[df['Bestilt_kvantum'] >= 0].copy()
all_orders['Måned_År'] = all_orders['Dato_Sortering'].dt.strftime('%b %Y')
df_pivot_06 = all_orders.pivot_table(index='Måned_År', columns='Leverandør_navn', values='Bestilt_kvantum', aggfunc='sum', fill_value=0)
sorted_months = all_orders.sort_values('Dato_Sortering')['Måned_År'].unique()
df_pivot_06 = df_pivot_06.reindex(sorted_months)
df_full_06 = df_pivot_06.reset_index().melt(id_vars='Måned_År', value_name='Bestilt_kvantum')

ax6 = sns.barplot(data=df_full_06, x='Måned_År', y='Bestilt_kvantum', hue='Leverandør_navn', palette='viridis')

# --- Legg til separasjonshjelp ---
for i in range(len(sorted_months)):
    if i % 2 == 0:
        plt.axvspan(i - 0.5, i + 0.5, color='gray', alpha=0.05, zorder=0)
    if i < len(sorted_months) - 1:
        plt.axvline(i + 0.5, color='gray', linestyle='--', alpha=0.15, linewidth=1)

for p in ax6.patches:
    height = p.get_height()
    x_center = p.get_x() + p.get_width() / 2.
    if height <= 0:
        ax6.plot([p.get_x() + p.get_width()*0.1, p.get_x() + p.get_width()*0.9], [2, 2], color='lightgray', linewidth=1)
        ax6.annotate('0', (x_center, 5), ha='center', va='bottom', fontsize=7, color='gray', rotation=90)
    else:
        ax6.annotate(f'{int(height)}', (x_center, height), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points', fontsize=9, fontweight='bold', rotation=90)

plt.title('Totalt månedlig innkjøpskvantum: Separert per måned (2021-2025)', fontsize=16, fontweight='bold')
plt.xticks(rotation=90)
plt.legend(title='Leverandør', bbox_to_anchor=(1.01, 1), loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.2)
plt.ylim(0, df_full_06['Bestilt_kvantum'].max() * 1.3)
plt.tight_layout()
plt.savefig(f'{output_dir}/06_bestillingsmonster_innkjop.png')
plt.close()

print(f"Endelige og polerte visualiseringer er klare i '{output_dir}/'")
