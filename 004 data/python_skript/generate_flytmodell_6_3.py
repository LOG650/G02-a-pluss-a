"""
Genererer Figur 6.6 — flytmodell som viser hvordan Prophet-prognosen mates inn
i den kvantitative optimaliseringsmodellen i kapittel 6.3 av rapporten.

Output: 006 analysis/figures/16_flytmodell_prognose_optimalisering.png
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------
FIG_W, FIG_H = 11.0, 9.5
fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect("equal")
ax.axis("off")

# Fargepalett (matter, profesjonell — matcher rapportens øvrige figurer)
COL_DATA = "#E8F0F7"     # lys blå — input
COL_PROPHET = "#C8DCEC"  # blå — prognose
COL_BIAS = "#FFE6CC"     # lys oransje — korreksjon
COL_OPT = "#D5E8D4"      # lys grønn — optimering
COL_PARAM = "#F8E6FA"    # lys lilla — parametere
COL_OUT = "#FFF2CC"      # lys gul — output
EDGE = "#444444"
ARROW = "#222222"


def add_box(x, y, w, h, text, facecolor, fontsize=10, fontweight="normal"):
    """Tegn en avrundet boks med sentrert tekst."""
    box = FancyBboxPatch(
        (x - w / 2, y - h / 2),
        w,
        h,
        boxstyle="round,pad=0.08,rounding_size=0.15",
        linewidth=1.4,
        edgecolor=EDGE,
        facecolor=facecolor,
    )
    ax.add_patch(box)
    ax.text(
        x,
        y,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        fontweight=fontweight,
        linespacing=1.35,
    )


def add_arrow(x1, y1, x2, y2, label=None, label_offset=(0.15, 0.0)):
    """Tegn en pil mellom to punkter, med valgfri label."""
    arrow = FancyArrowPatch(
        (x1, y1),
        (x2, y2),
        arrowstyle="-|>",
        mutation_scale=18,
        linewidth=1.6,
        color=ARROW,
        shrinkA=2,
        shrinkB=2,
    )
    ax.add_patch(arrow)
    if label:
        mx, my = (x1 + x2) / 2 + label_offset[0], (y1 + y2) / 2 + label_offset[1]
        ax.text(
            mx,
            my,
            label,
            fontsize=10,
            fontstyle="italic",
            ha="left",
            va="center",
            color="#222222",
        )


# ---------------------------------------------------------------------------
# Bokser
# ---------------------------------------------------------------------------
# Hovedflyt (vertikal, sentrert på x = 5)
add_box(
    5.0, 9.2, 5.4, 0.9,
    "HISTORISK DATA (2021–2024)\nDaglig etterspørsel per kategori",
    COL_DATA, fontsize=10, fontweight="bold",
)

add_box(
    5.0, 7.6, 5.4, 1.2,
    "PROPHET-MODELL\n"
    r"$y(t) = g(t) + s(t) + h(t) + \varepsilon_t$"
    "\nTrend  ·  Sesong  ·  Helligdager/kampanjer",
    COL_PROPHET, fontsize=10, fontweight="bold",
)

add_box(
    5.0, 5.85, 5.4, 0.95,
    "BIAS-JUSTERING (backtesting på 2025)\n"
    "Korrigerer systematisk over-/underestimering per kategori",
    COL_BIAS, fontsize=10, fontweight="bold",
)

add_box(
    5.0, 3.6, 6.4, 1.85,
    "OPTIMALISERINGSMODELL  (kap. 6.3)\n"
    r"$\min\ Z = \sum_{t=1}^{T}\,(C_h \cdot I_t + C_s \cdot S_t)$"
    "\n"
    r"u.b.b.  $I_t = I_{t-1} + Q_{t-L} - D_t + S_t$,   $I_t,\,Q_t \geq 0$"
    "\n"
    r"$P(I_t > 0) \geq SL_{\mathrm{mål}}$",
    COL_OPT, fontsize=10, fontweight="bold",
)

add_box(
    5.0, 1.25, 6.4, 1.0,
    "BESLUTNINGSVARIABLER\n"
    r"Bestillingsmengde $Q_t$  ·  Bestillingspunkt $s_t$  ·  Sikkerhetslager",
    COL_OUT, fontsize=10, fontweight="bold",
)

# Sidekasse: parametere (kobles inn på optimeringssteget)
add_box(
    1.35, 3.6, 2.5, 1.85,
    "PARAMETERE\n"
    r"$C_h$ : lagerhold"
    "\n"
    r"$C_s$ : mangel"
    "\n"
    r"$L$    : ledetid"
    "\n"
    r"$SL_{\mathrm{mål}}$ : servicegrad",
    COL_PARAM, fontsize=9.5, fontweight="bold",
)

# ---------------------------------------------------------------------------
# Piler (hovedflyt)
# ---------------------------------------------------------------------------
add_arrow(5.0, 8.75, 5.0, 8.20)               # Data → Prophet
add_arrow(5.0, 7.00, 5.0, 6.33, label=r"$\hat{y}(t)$", label_offset=(0.2, 0.0))
add_arrow(5.0, 5.38, 5.0, 4.53, label=r"$D_t$ (prognose 2026)", label_offset=(0.2, 0.0))
add_arrow(5.0, 2.68, 5.0, 1.75)               # Optimering → beslutninger

# Pil fra parametere inn i optimering
add_arrow(2.65, 3.6, 3.80, 3.6)

# ---------------------------------------------------------------------------
# Tittel og forklaring
# ---------------------------------------------------------------------------
ax.text(
    5.0, 9.85,
    "Dataflyt: fra historisk etterspørsel til bestillingsbeslutning",
    ha="center", va="center", fontsize=12, fontweight="bold",
)

# ---------------------------------------------------------------------------
# Lagre
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "006 analysis" / "figures" / "16_flytmodell_prognose_optimalisering.png"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
plt.tight_layout()
plt.savefig(OUTPUT, dpi=180, bbox_inches="tight", facecolor="white")
plt.close(fig)
print(f"Skrev: {OUTPUT}")
