#!/usr/bin/env python3
"""Render the two figures used in docs/16-DATASET-CHEATSHEET.md.

Numbers are the measured audit counts (8 Nov 2026); this script does not read
the raw data, so it can run anywhere. Reproduce the numbers with
`python scripts/audit_duplicates.py --raw data/raw --out data/audit`.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

OUT = Path("data/figures")
OUT.mkdir(parents=True, exist_ok=True)

UNIQUE = "#1b5e20"
DUP = "#e57373"
TEXT = "#212121"
GRID = "#bdbdbd"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.edgecolor": GRID,
    "axes.labelcolor": TEXT,
    "text.color": TEXT,
    "xtick.color": TEXT,
    "ytick.color": TEXT,
})

# ---------------------------------------------------------------- figure 1
# dataset, files, distinct
DATA = [
    ("JMuBEN + JMuBEN2", 58_550, 3_757),
    ("Uganda", 3_322, 1_810),
    ("BRACOL", 1_747, 1_746),
    ("RoCoLe", 1_560, 1_493),
    ("Silva", 542, 542),
]

fig, ax = plt.subplots(figsize=(9, 3.6))
labels = [d[0] for d in DATA][::-1]
for i, (name, files, distinct) in enumerate(DATA[::-1]):
    uniq_pct = distinct / files * 100
    ax.barh(i, uniq_pct, color=UNIQUE, height=0.55, zorder=3)
    ax.barh(i, 100 - uniq_pct, left=uniq_pct, color=DUP, height=0.55,
            zorder=3, hatch="///", edgecolor="white", linewidth=0)
    ax.text(101, i, f"{files:,} files  →  {distinct:,} distinct",
            va="center", ha="left", fontsize=9)
    if uniq_pct >= 12:
        ax.text(uniq_pct / 2, i, f"{uniq_pct:.1f}%", va="center", ha="center",
                color="white", fontsize=8, fontweight="bold")
    else:
        ax.text(uniq_pct + 1.2, i, f"{uniq_pct:.1f}%", va="center", ha="left",
                color=UNIQUE, fontsize=8, fontweight="bold",
                bbox=dict(facecolor="white", edgecolor="none", pad=1.5))

ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels)
ax.set_xlim(0, 100)
ax.set_xlabel("share of the downloaded files")
ax.set_title("How much of each dataset is a byte-identical copy?",
             loc="left", fontsize=12, fontweight="bold", pad=10)
ax.grid(axis="x", color=GRID, linewidth=0.6, alpha=0.6, zorder=0)
ax.set_axisbelow(True)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.legend(handles=[Patch(color=UNIQUE, label="distinct image"),
                   Patch(facecolor=DUP, hatch="///", edgecolor="white",
                         label="duplicate copy")],
          loc="lower right", frameon=False, ncol=2, bbox_to_anchor=(1.0, -0.42))
fig.subplots_adjust(left=0.21, right=0.52, bottom=0.28)
fig.savefig(OUT / "dataset-duplication.png", dpi=200)
plt.close(fig)

# ---------------------------------------------------------------- figure 2
CLASSES = [  # class, files, distinct
    ("Healthy", 18_984, 63),
    ("Miner", 16_978, 1_639),
    ("Leaf rust", 8_336, 1_042),
    ("Cercospora", 7_681, 322),
    ("Phoma", 6_571, 691),
]

fig, ax = plt.subplots(figsize=(9, 3.8))
y = range(len(CLASSES))
h = 0.36
ax.barh([i + h / 2 for i in y], [c[1] for c in CLASSES], height=h,
        color=DUP, label="files", zorder=3)
ax.barh([i - h / 2 for i in y], [c[2] for c in CLASSES], height=h,
        color=UNIQUE, label="distinct images", zorder=3)
for i, (name, files, distinct) in enumerate(CLASSES):
    ax.text(files + 250, i + h / 2, f"{files:,}", va="center", fontsize=8)
    ax.text(distinct + 250, i - h / 2, f"{distinct:,}", va="center", fontsize=8,
            color=UNIQUE, fontweight="bold")

ax.set_yticks(list(y))
ax.set_yticklabels([c[0] for c in CLASSES])
ax.set_xlim(0, 21_500)
ax.set_xlabel("images in JMuBEN + JMuBEN2")
ax.set_title("JMuBEN: 18,984 'Healthy' files are 63 distinct images",
             loc="left", fontsize=12, fontweight="bold", pad=10)
ax.grid(axis="x", color=GRID, linewidth=0.6, alpha=0.6, zorder=0)
ax.set_axisbelow(True)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.legend(frameon=False, loc="upper right")
fig.tight_layout()
fig.savefig(OUT / "jmuben-files-vs-distinct.png", dpi=200)
plt.close(fig)

print("wrote", OUT / "dataset-duplication.png")
print("wrote", OUT / "jmuben-files-vs-distinct.png")
