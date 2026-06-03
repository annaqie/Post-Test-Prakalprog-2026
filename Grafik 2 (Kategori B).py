# ============================================================
# KATEGORI B — Bar Chart
# 5 rumah paling mahal dengan hanya 1 kamar mandi
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load dataset ────────────────────────────────────────────
df = pd.read_csv("Kelas C_Housing.csv")

# ── Style ──────────────────────────────────────────────────
sns.set_theme(style="whitegrid", font_scale=1.1)
ACCENT = "#2C3E50"

fig, ax = plt.subplots(figsize=(9, 6))
ax.set_facecolor('#FFFFFF')

top5 = (df[df['bathrooms'] == 1]
        .nlargest(5, 'price')
        .reset_index(drop=True))
top5['label'] = [f'Rumah #{i + 1}\n{row.bedrooms}BR | {row.stories}Lt\n{row.area:,} ft²'
                 for i, row in top5.iterrows()]
top5['price_jt'] = top5['price'] / 1e6

palette_b = sns.color_palette("Blues_d", n_colors=5)[::-1]
bars = ax.bar(top5['label'], top5['price_jt'],
               color=palette_b, edgecolor='white', linewidth=0.8)
for bar, val in zip(bars, top5['price_jt']):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
             f'{val:.2f} Jt', ha='center', va='bottom',
             fontsize=10, fontweight='bold', color=ACCENT)

ax.set_ylabel('Harga (Juta)', fontsize=12, color=ACCENT)
ax.set_title('Kategori B : 5 Rumah Paling Mahal\ndengan 1 Kamar Mandi',
             fontsize=13, fontweight='bold', color=ACCENT, pad=10)
ax.set_ylim(0, top5['price_jt'].max() * 1.18)
ax.tick_params(axis='x', labelsize=9)
ax.tick_params(axis='y', labelsize=10)
ax.spines[['top', 'right']].set_visible(False)

plt.tight_layout()
plt.show()