# ============================================================
# KATEGORI D — Histogram + KDE
# Distribusi luas tanah (area) untuk melihat kemencengan data
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load dataset ────────────────────────────────────────────
df = pd.read_csv("Kelas C_Housing.csv")

# ── Style ──────────────────────────────────────────────────
sns.set_theme(style="whitegrid", font_scale=1.1)
PURPLE = "#9B59B6"
RED    = "#E74C3C"
GREEN  = "#2ECC71"
ACCENT = "#2C3E50"

fig, ax = plt.subplots(figsize=(9, 6))
ax.set_facecolor('#FFFFFF')

sns.histplot(df['area'], bins=30, kde=True, ax=ax,
             color=PURPLE, edgecolor='white', linewidth=0.6,
             alpha=0.75, line_kws={'linewidth': 2.5, 'color': '#6C3483'})

mean_area   = df['area'].mean()
median_area = df['area'].median()
skew_val    = df['area'].skew()

ax.axvline(mean_area,   color=RED,   linestyle='--', linewidth=1.8,
           label=f'Mean: {mean_area:,.0f}')
ax.axvline(median_area, color=GREEN, linestyle='-.', linewidth=1.8,
           label=f'Median: {median_area:,.0f}')

ax.set_xlabel('Luas Tanah (ft²)', fontsize=12, color=ACCENT)
ax.set_ylabel('Frekuensi', fontsize=12, color=ACCENT)
ax.set_title('Kategori D : Distribusi Luas Tanah (Area)\nHistogram + KDE',
             fontsize=13, fontweight='bold', color=ACCENT, pad=10)
ax.legend(fontsize=10, framealpha=0.85)
ax.legend(fontsize=10, 
          framealpha=0.85, 
          loc='upper right', 
          bbox_to_anchor=(1, 0.82))

skew_dir = ("Right-Skewed (Positif)" if skew_val > 0.5 else
            "Left-Skewed (Negatif)" if skew_val < -0.5 else "Simetris")
ax.text(0.97, 0.93, f'Skewness (kemencengan)  {skew_val:.3f}\n({skew_dir})',
        transform=ax.transAxes, fontsize=9, ha='right', va='top',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#EBF5FB',
                  edgecolor=PURPLE, alpha=0.9))
ax.spines[['top', 'right']].set_visible(False)

plt.tight_layout()
plt.show()