# Dataset verification — the real counts

**7 November 2026 · Hayredin**

Every dataset we plan to cite, opened and counted **before any preprocessing**.
Six of ten are verified. Three are still unopened. One cannot be used for the headline model, for licence reasons.

**PR #3:** https://github.com/jov1523/coffee_leaf_disease_diagnosis/pull/3

---

## 1. Verified counts

| Dataset | Count | Tier | Note |
|---|---|---|---|
| JMuBEN + JMuBEN2 | **58,549** | T1 | Two independent mirrors agree |
| RoCoLe | **1,560** | T1 | 390 plants × 4 views |
| Silva | **542** | T2 | 285 rust + 257 miner |
| Uganda (Mendeley) | **3,322** | T2 | Healthy 1,179 / Rust 1,033 / Phoma 1,110 |
| Uganda augmented (Kaggle) | **26,335** | T2 | ⚠ non-commercial licence |
| Ethiopian (Kaggle) | **12,000** | T2 | Only ~1,200 unique clean images |
| BRACOL | 1,747 leaves / 2,147 crops | T3 | Archive not opened |
| Saposoa | 1,500 | T3 | Archive not opened |
| CoffeeLeaf-CO v2 | 2,315 | T3 | Archive not opened |

**Tiers**
**T1** — two independent releases agree
**T2** — one publisher file manifest
**T3** — published figure only, archive not opened
**T4** — claimed, nothing to check

---

## 2. Five findings that change what we write

1. **JMuBEN** — the paper says 58,555. The files say **58,549** (−6). Use 58,549 and footnote the paper.
2. **RoCoLe** — 1,560 is 390 plants × 4 views, not 1,560 independent leaves. Split **by plant**, not by file, or the same leaf leaks into train and test.
3. **Uganda** — description says 3,312, files say **3,322** (+10). The augmented mirror claims 26,315, files say **26,335** (+20).
4. **Ethiopian set** — "12,000" is not 12,000 leaves. 10,800 sit in `train aug/` (2,700 × 4 classes); only 1,200 in `test/` are clean. It also has **4 classes — no Leaf Miner**. It can validate 4 of our 5 classes, not 5.
5. **BRACOL, Saposoa, CoffeeLeaf-CO** — still T3. Nothing is wrong with them; we just have not opened the archives. Until someone runs the download, the report says *reported*, not *verified*.

---

## 3. Licence warning — read before any training run

The augmented Uganda Kaggle mirror is **CC BY-NC-SA 4.0 — non-commercial**.
If the headline model trains on it, we cannot ship it as a product.

**Rule:** headline model trains on the **Mendeley original (CC BY 4.0)**. The augmented set is a research ablation only, and we say so in the report.

---

## 4. What I need from each of you

- **Yohannes** — nothing blocking. Class list stays 5. Counts come from the datasheet, not hardcoded.
- **Bemnet** — serving layer reads class order from `data/dataset-sources.md`. Do not hardcode it; the order will change.
- **Nahom** — T1/T2 numbers are *verified*, T3 are *reported*. Add the RoCoLe plant-level split to the test plan. Ethiopian set enters as a 4-class external check.
- **Everyone** — never quote a size from the Kaggle API. `datasets/view` and `datasets/list` disagree by more than 2×.

---

## 5. How to check my work

**Colab** — open and run all:
https://colab.research.google.com/github/Hayredin950/coffee-leaf-diagnosis/blob/main/notebooks/00-dataset-verification.ipynb

**Kaggle** — import `notebooks/00-dataset-verification.ipynb`, attach the dataset, set `DOWNLOAD = True` in the SETTINGS cell.

It prints the count table, writes JSON + CSV + MD, and gives a verdict per dataset.
If a number differs from mine, tell me. I would rather fix it now than at the defense.

---

## 6. Still open

- Mendeley archives need a logged-in session — this is why BRACOL, Saposoa and CoffeeLeaf-CO are still T3.
- Written to the JMuBEN author (Bayile Getu Taye); no reply yet.
- JARC has not replied.
