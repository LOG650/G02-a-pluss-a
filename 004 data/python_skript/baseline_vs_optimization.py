import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm

# Konfigurasjon
TRAIN_DATA_PATH = r'004 data/splittet_data/train/train_data.csv'
TEST_DATA_PATH = r'004 data/splittet_data/test/test_data.csv'
FIGURES_DIR = r'006 analysis/figures'

KATEGORI_INFO = {
    'Engelsk fiksjon': {'lagerkost': 10, 'stockout_kost': 120, 'bestillingskost': 600},
    'Norske barnebøker': {'lagerkost': 6, 'stockout_kost': 75, 'bestillingskost': 250},
    'Norsk krim': {'lagerkost': 8, 'stockout_kost': 95, 'bestillingskost': 250},
}


def last_og_filtrer_data(path, kategori):
    df = pd.read_csv(path)
    return df[df['Kategori'] == kategori].copy().reset_index(drop=True)


def beregn_baseline_parametere(train_df):
    snitt_ettersporsel = train_df['Etterspørsel'].mean()
    snitt_ledetid_mnd = train_df['Supp_Ledetid (dager)'].mean() / 30
    s_baseline = (snitt_ettersporsel * snitt_ledetid_mnd) * 1.10
    Q_baseline = snitt_ettersporsel
    return s_baseline, Q_baseline, snitt_ettersporsel, snitt_ledetid_mnd


def beregn_optimaliserte_parametere(train_df, kost_params):
    D = train_df['Etterspørsel'].mean() * 12
    S = kost_params['bestillingskost']
    H = kost_params['lagerkost']
    Q_opt = np.sqrt((2 * D * S) / H)

    P_stockout = H / (H + kost_params['stockout_kost'])
    std_d = train_df['Etterspørsel'].std()
    lt_mnd = train_df['Supp_Ledetid (dager)'].mean() / 30
    mean_lt_d = (D / 12) * lt_mnd
    std_lt_d = std_d * np.sqrt(lt_mnd)

    z = norm.ppf(1 - P_stockout)
    s_opt = mean_lt_d + (z * std_lt_d)
    return s_opt, Q_opt


def simuler_politikk(test_df, s, Q, kost_params):
    lager = test_df.iloc[0]['Startlager']
    totale_kostnader = 0
    mangel_enheter = 0
    ordre_i_gang = []
    resultater = []

    for i, row in test_df.iterrows():
        mnd = row['Måned']
        ettersporsel = row['Etterspørsel']

        for ankomst, kvantum in ordre_i_gang[:]:
            if i >= ankomst:
                lager += kvantum
                ordre_i_gang.remove((ankomst, kvantum))

        salg = min(lager, ettersporsel)
        stockout = max(0, ettersporsel - lager)
        lager -= salg
        mangel_enheter += stockout

        lagerkost = lager * kost_params['lagerkost']
        stockout_kost = stockout * kost_params['stockout_kost']
        bestillings_kost = 0
        ordre_lagt = False

        if lager <= s and not ordre_i_gang:
            bestillings_kost = kost_params['bestillingskost']
            ankomst_mnd = i + 1
            ordre_i_gang.append((ankomst_mnd, Q))
            ordre_lagt = True

        totale_kostnader += (lagerkost + stockout_kost + bestillings_kost)

        resultater.append({
            'Måned': mnd,
            'Etterspørsel': ettersporsel,
            'Lager': lager,
            'Salg': salg,
            'Stockout': stockout,
            'Ordre_lagt': ordre_lagt,
            'Totalkost': lagerkost + stockout_kost + bestillings_kost,
        })

    return pd.DataFrame(resultater), totale_kostnader, mangel_enheter


def plott_sq_sykel(resultater_df, kategori, s, Q, figures_dir):
    """Visualiserer (s, Q)-sykler: lagerbeholdning, etterspørsel og bestillingstidspunkter."""
    fig, ax1 = plt.subplots(figsize=(11, 5))

    x = np.arange(len(resultater_df))
    ax1.plot(x, resultater_df['Lager'], color='#1f77b4', marker='o', label='Lagerbeholdning (etter salg)')
    ax1.bar(x, resultater_df['Etterspørsel'], color='#ff7f0e', alpha=0.25, label='Etterspørsel')

    ax1.axhline(s, color='#d62728', linestyle='--', linewidth=1.4, label=f'Bestillingspunkt s = {s:.0f}')

    ordre_idx = resultater_df.index[resultater_df['Ordre_lagt']].tolist()
    if ordre_idx:
        ax1.scatter(ordre_idx, resultater_df.loc[ordre_idx, 'Lager'],
                    s=120, color='#2ca02c', zorder=5, marker='^',
                    label=f'Bestilling lagt (Q = {Q:.0f})')

    ax1.set_xticks(x)
    ax1.set_xticklabels(resultater_df['Måned'], rotation=45, ha='right')
    ax1.set_ylabel('Enheter')
    ax1.set_xlabel('Testperiode (2025)')
    ax1.set_title(f'Baseline (s, Q)-sykel – {kategori}')
    ax1.grid(alpha=0.3)
    ax1.legend(loc='upper right')

    fig.tight_layout()
    filnavn = f"15_baseline_sq_sykel_{kategori.replace(' ', '_')}.png"
    sti = os.path.join(figures_dir, filnavn)
    fig.savefig(sti, dpi=150)
    plt.close(fig)
    return sti


def kjor_analyse(kategori, kost_params, train_path, test_path, figures_dir):
    print(f"\n--- Analyse for {kategori} ---")
    train_df = last_og_filtrer_data(train_path, kategori)
    test_df = last_og_filtrer_data(test_path, kategori)

    s_base, Q_base, snitt_d, snitt_lt = beregn_baseline_parametere(train_df)
    print(f"Baseline:       s={s_base:.2f}, Q={Q_base:.2f} (D̄={snitt_d:.1f}, L̄={snitt_lt*30:.1f} dager)")

    res_base, kost_base, mangel_base = simuler_politikk(test_df, s_base, Q_base, kost_params)
    sl_base = (res_base['Salg'].sum() / test_df['Etterspørsel'].sum()) * 100
    print(f"  Total kost: {kost_base:,.2f} NOK | Servicegrad: {sl_base:.2f}% | Mangel: {mangel_base:.0f} enheter")

    s_opt, Q_opt = beregn_optimaliserte_parametere(train_df, kost_params)
    print(f"Optimalisert:   s={s_opt:.2f}, Q={Q_opt:.2f}")
    res_opt, kost_opt, mangel_opt = simuler_politikk(test_df, s_opt, Q_opt, kost_params)
    sl_opt = (res_opt['Salg'].sum() / test_df['Etterspørsel'].sum()) * 100
    print(f"  Total kost: {kost_opt:,.2f} NOK | Servicegrad: {sl_opt:.2f}% | Mangel: {mangel_opt:.0f} enheter")

    besparelse = ((kost_base - kost_opt) / kost_base) * 100
    print(f"Potensiell besparelse: {besparelse:.2f}%")

    figur_sti = plott_sq_sykel(res_base, kategori, s_base, Q_base, figures_dir)
    print(f"Figur lagret: {figur_sti}")

    return {
        'Kategori': kategori,
        's_baseline': round(s_base, 2),
        'Q_baseline': round(Q_base, 2),
        'Kost_baseline': round(kost_base, 2),
        'SL_baseline (%)': round(sl_base, 2),
        's_opt': round(s_opt, 2),
        'Q_opt': round(Q_opt, 2),
        'Kost_opt': round(kost_opt, 2),
        'SL_opt (%)': round(sl_opt, 2),
        'Besparelse (%)': round(besparelse, 2),
    }


def main():
    os.makedirs(FIGURES_DIR, exist_ok=True)
    oppsummering = []
    for kategori, kost_params in KATEGORI_INFO.items():
        oppsummering.append(kjor_analyse(kategori, kost_params, TRAIN_DATA_PATH, TEST_DATA_PATH, FIGURES_DIR))

    print("\n=== Samlet oppsummering ===")
    print(pd.DataFrame(oppsummering).to_string(index=False))


if __name__ == '__main__':
    main()
