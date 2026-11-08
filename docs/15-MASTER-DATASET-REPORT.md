# Coffee-leaf corpus — master verification report

**8 November 2026 · Hayredin Mohammed · BunaDoctor FYP**

One document, every dataset. It separates four things the field normally mixes together:

1. what a publisher **claims**,
2. what the archive **contains** (files),
3. how many **distinct images** are actually in it,
4. whether we are **allowed to ship** a model trained on it.

Everything below is reproducible from the URLs, hashes and commands in §7.

---

## 0. Post-ready summary (5 lines)

> We did not take any dataset's word for its size. **Six archives were downloaded and every image hashed; two more were verified from publisher manifests; two remain unopened; one is claimed only.**
>
> The headline corpus is **58,550 files but only 3,757 distinct images** — 93.6 % of JMuBEN is byte-identical duplication, and its Healthy class is 18,984 files but **63 distinct files — 62 decodable**.
>
> BRACOL's official archive is **truncated at the publisher** (1,402 of 1,747). We detected it by checksum and repaired it from a verified mirror.
>
> Uganda has **102 zero-byte files** and is 1,810 distinct, not 3,322.
>
> Full tables, the rejected datasets, and the reproduction commands are below.

### 0.1 Paste-ready table (monospace — renders on any phone)

```text
DATASET            COUNTRY    FILES      DISTINCT  TIER  ROLE
JMuBEN             Kenya     22,588         2,055  T1    training
JMuBEN2            Kenya     35,962         1,702  T1    training
  combined                   58,550         3,757  T1    training
BRACOL             Brazil     1,747         1,746  T1    training
RoCoLe             Ecuador    1,560         1,493  T1    external
Silva              Brazil       542           542  T2    external
Uganda             Uganda     3,322         1,810  T1    external
Ethiopian          Ethiopia  12,000       unknown  T2    external test
Uganda augmented   Uganda    26,335     not dedup  T2    ablation (NC)
Saposoa            Peru       1,500    not opened  T3    external
CoffeeLeaf-CO v2   Colombia   2,315    not opened  T3    external
CerradoCoffeeLeaf  Brazil     1,476  not released  T4    cite only
```

**Downloaded subtotal: 65,721 files → 9,348 distinct images.** Everything else is a claim we have not
yet counted, and is labelled as such.

---

## 1. The master table — every dataset, one view

**Tier** — T1: verified against two independent releases or counted from the publisher's bytes · T2: verified from one publisher manifest · T3: publisher's figure only, archive not opened · T4: claimed, nothing to check.

### 1.1 One table — all eleven datasets

| # | Dataset | Country | Species | Classes | Files | **Distinct** | Licence | Tier | How it was checked | Role |
|---|---|---|---|---:|---:|---:|---|---|---|---|
| 1 | **JMuBEN** | Kenya | Arabica | Rust, Cercospora, Phoma | 22,588 | **2,055** | CC BY 4.0 | T1 | downloaded + hashed | training |
| 2 | **JMuBEN2** | Kenya | Arabica | Miner, Healthy | 35,962 | **1,702** | CC BY 4.0 | T1 | downloaded + hashed | training |
| 3 | **BRACOL** | Brazil | Arabica | All five (+ mixed) | 1,747 | **1,746** | CC BY 4.0 | T1 | downloaded + hashed, repaired | training |
| 4 | **RoCoLe** | Ecuador | **Robusta** | Rust, Healthy (+ mite) | 1,560 | **1,493** | CC BY 4.0 | T1 | downloaded + hashed | external |
| 5 | **Silva 2020** | Brazil | Arabica | Rust, Miner | 542 | **542** | CC BY 4.0 | T2 | downloaded + hashed | external |
| 6 | **Uganda 2025** | Uganda | Arabica | Rust, Phoma, Healthy | 3,322 | **1,810** | CC BY 4.0 | T1 | downloaded + hashed | external |
| 7 | **Ethiopian** (Kaggle `biniyamyoseph`) | **Ethiopia** | Arabica | Cercospora, Rust, Phoma, Healthy | 12,000 | unknown | CC0 (claim) | T2 | publisher manifest | external test |
| 8 | **Uganda augmented** (Kaggle) | Uganda | Arabica | Rust, Phoma, Healthy | 26,335 | not deduplicated | **CC BY-NC-SA 4.0** | T2 | publisher manifest | ablation only |
| 9 | **Saposoa** (Mendeley `mfpxg4y65r`) | Peru | Arabica | Rust, Healthy (+ *Mycena*) | 1,500 | not opened | CC BY 4.0 | T3 | publisher figure only | external |
| 10 | **CoffeeLeaf-CO v2** (Zenodo 22756170) | Colombia | Arabica | Rust, Miner (+ weevil) | 2,315 | not opened | CC BY 4.0 | T3 | publisher figure only | external |
| 11 | **CerradoCoffeeLeaf** | Brazil | — | 7 classes | 1,476 | not released | unknown | T4 | claimed only | cite only |

**Read the table this way:** rows 1–6 were **downloaded and counted**, rows 7–8 were **verified from a
publisher's own file listing**, rows 9–10 are **figures we have not opened**, and row 11 has **nothing
to open**. Only the "Distinct" column of rows 1–6 is a measured number.

### 1.2 Grand totals — read the footnote

| | Files | Distinct |
|---|---:|---:|
| Downloaded and hashed | 65,721 | **9,348** |
| Manifest-verified (7, 8) | 38,335 | unknown |
| Unopened (9, 10) | 3,815 | unknown |
| **All candidates** | **107,871** | **≥ 9,348** |

**Footnote:** Uganda appears twice (rows 6 and 8) because the augmented release is a different
artifact of the same farms — do not add them as independent data. The 107,871 figure is the size of
the *search space*, not the corpus.

The corpus is **9,348 distinct downloaded files**, of which **9,347 decode** — `JMuBEN2/Healthy/2
(691).jpg` is corrupt in the publisher's archive. Of the 9,348, **5,503** belong to the three
training sources (JMuBEN, JMuBEN2, BRACOL); **5,441** are usable for 5-class training after removing
BRACOL's 62 mixed-infection images and the one corrupt file.

---

## 2. Per-class breakdown of the two big sources

### 2.1 JMuBEN + JMuBEN2 — 58,550 files, 3,757 distinct

| Class | Files | **Distinct** | Duplicate share | Copies per image |
|---|---:|---:|---:|---:|
| Leaf rust | 8,336 | **1,042** | 87.5 % | 8 |
| Cercospora | 7,681 | **322** | 95.8 % | 24 |
| Phoma | 6,571 | **691** | 89.5 % | 10 |
| Miner | 16,978 | **1,639** | 90.3 % | 8–16 |
| **Healthy** | **18,984** | **63** (62 usable) | **99.7 %** | **~300** |
| **Total** | **58,550** | **3,757** (3,756 usable) | **93.6 %** | — |

Three independent proofs:

1. `1 (1).jpg`, `2 (1).jpg`, `10 (1).jpg` are byte-identical (MD5 + SHA-256).
2. The same holds when read **straight from the publisher's inner zip**, so it is not an extraction artefact.
3. `data/figures/jmuben-healthy-63.png` shows all 63 distinct "Healthy" images — visually frames of **one leaf**, differing only in white balance.

The other four classes are genuinely varied (`data/figures/jmuben-unique-sample.png`); their
duplication is a copy artefact, not a single scene.

### 2.2 Uganda — 3,322 files, 1,810 distinct, 102 broken

| Class | Files | **Distinct** | Zero-byte | Duplicate share |
|---|---:|---:|---:|---:|
| Healthy | 1,179 | **739** | 100 | 37.3 % |
| Leaf rust | 1,033 | **617** | 2 | 40.3 % |
| Phoma | 1,110 | **454** | 0 | 59.1 % |
| **Total** | **3,322** | **1,810** | **102** | **45.5 %** |

The 102 zero-byte files are a **publisher defect** — the archive passes CRC, so it is not a bad
download. The "duplicates removed" claim in the dataset description is false.

### 2.3 BRACOL — 1,747 files, 1,746 distinct, and a repair

The Mendeley archive is **truncated at the publisher**: it stops at image `688.jpg`, giving 1,402 of
1,747 images and no zip central directory. Two independent downloads are byte-identical, and the
SHA-256 matches Mendeley's own manifest (`25a2fc97…`) — the file is broken at the source, not in
transit. The missing 345 images were restored from the Hugging Face mirror `luisangelico/bracol`,
after verifying that `dataset.csv` and `images/1.jpg` are byte-identical to the Mendeley release.

Class encoding found in `dataset.csv`:

| Code | Class | Images |
|---|---|---:|
| 0 | Healthy | 272 |
| 1 | Leaf miner | 387 |
| 2 | Leaf rust | 531 |
| 3 | Phoma | 348 |
| 4 | Cercospora | 147 |
| 5 | **Mixed infection** | 62 |
| | **Single-label usable** | **1,685** |

### 2.4 RoCoLe — 1,560 files, 1,493 distinct, and a leakage trap

67 images are byte-identical **across different plant IDs**:

```
C11P19E1.jpg == C12P28E1.jpg
C12P34E1.jpg == C11P24E1.jpg
C11P24H1.jpg == C12P34H1.jpg
C12P36E1.jpg == C11P23E1.jpg
```

A plant-level split still puts one copy in train and the other in test. Deduplicate by MD5 **before**
assigning plants to folds.

### 2.5 Silva — clean

542 files, 542 distinct, 0 unreadable, 542 XML annotations. The only fully clean archive in the set.

---

## 3. The five findings that change the project

1. **The primary benchmark is 93.6 % duplicate.** 58,550 files → 3,757 distinct. Any random split
   trains and tests on the same image 8–300 times. This is the mechanism behind 99 % in-dataset
   accuracy sitting next to 1.9 % external rust recall.
2. **The Healthy class is one leaf.** 18,984 files → 63 distinct files (62 decodable), visually a
   single leaf.
   Healthy must come from BRACOL (272), Uganda (739) and RoCoLe (780), not from JMuBEN.
3. **BRACOL's official archive is truncated.** Detected by SHA-256 against the publisher's own
   manifest; repaired from a verified mirror. 1,747/1,747 now, all decodable.
4. **Uganda has 102 zero-byte files and 45.5 % duplicates.** Usable count is 1,810, not 3,322.
5. **RoCoLe's duplicates cross plant boundaries.** 67 pairs; MD5 dedup must precede the plant split.

---

## 4. Licence map — what we can ship

| Licence | Datasets | Shippable in a product? |
|---|---|---|
| **CC BY 4.0** | JMuBEN, JMuBEN2, BRACOL, RoCoLe, Silva, Uganda | ✅ Yes, with attribution |
| **CC0** | Ethiopian (uploader's claim, unverifiable) | ⚠️ Probably; treat as research-only until provenance is confirmed |
| **CC BY-NC-SA 4.0** | **Uganda augmented (Kaggle)** | ❌ **No — non-commercial** |
| Unknown / unverified | Saposoa, CoffeeLeaf-CO, Cerrado | ❓ Check before shipping |

**Rule:** the headline model trains on **CC BY 4.0 data only**. The augmented Uganda mirror is a
research ablation, labelled as such, never a shipped model.

---

## 5. What the corpus actually is

| Purpose | Sources | Distinct images |
|---|---|---:|
| **Training** (headline) | JMuBEN + JMuBEN2 (3,757) + BRACOL (1,685 single-label) | **~5,440** |
| **Training** (ablation B) | + Uganda original (1,810) | ~7,250 |
| **External — African** | Uganda (1,810) + Ethiopian test (1,200) | ~3,010 |
| **External — other** | RoCoLe (1,493) + Silva (542) + Saposoa (1,500) + CoffeeLeaf-CO (2,315) | ~5,850 |
| **Research ablation** | Uganda augmented (26,335 files) | NC licence |

**Class balance on distinct images:** Cercospora 322 · Healthy 63 · Rust 1,042 · Miner 1,639 ·
Phoma 691 (JMuBEN only). Healthy is the bottleneck; Miner is 26× larger. Macro-averaged metrics are
the primary metric, and per-class recall is reported for every class on every dataset.

---

## 6. What was downloaded vs what was only checked

| Check | How | Datasets |
|---|---|---|
| **Downloaded + hashed** | 6 archives, 5.7 GB, MD5 per file, SHA-256 per archive | JMuBEN, JMuBEN2, BRACOL, RoCoLe, Silva, Uganda |
| **Manifest-verified** | Kaggle / Hugging Face / Zenodo file listing, every filename enumerated | Ethiopian, Uganda augmented |
| **Publisher figure only** | Dataset page + file-manifest API, archive not opened | Saposoa, CoffeeLeaf-CO v2 |
| **Claimed only** | Paper / README, no downloadable artifact | CerradoCoffeeLeaf |
| **Checked and rejected** | See §6.1 | 20+ records |

### 6.1 Checked and rejected (the report must show we looked)

| Record | Why rejected |
|---|---|
| **PlantVillage** | Contains **no coffee classes** — verified via the GitHub contents API |
| **AI-Lab-Makerere/beans** | Common bean, not coffee |
| **Rwandan dataset** (Hitimana et al.) | 37,939 images, but "available on request" and partly downloaded from the internet |
| **CoLeaf-DB** | 1,006 images of **nutritional deficiency**, not disease |
| **Coffee & cashew UAV (Makerere)** | 3,000 images of **fruit**, not leaves |
| **Roboflow "Coffee leaf disease"** | 7,134 images, no source, no methodology, no healthy class |
| **Kaggle Metadata-Enhanced Benchmark** | 90,780 images, but a **superset** of JMuBEN + BRACOL + RoCoLe + others → guaranteed leakage |
| **JMuBEN3** | Sweet-potato leaf rust; file API returns `[]` |
| **IP102** | Insect pests, not coffee leaf disease |
| **BRACOT** | 300 segmentation images, uncertain provenance |
| **iCog Labs (Addis Ababa)** | Repository is **empty (0 bytes)** |
| **dvelaren/clr-dataset** | 4,398 images, **rust severity only** — no healthy, no other disease |
| **Zenodo 14628690** | 810.8 MB, no description, no class statement, no paper |
| **brainer-fp66 (HF)** | 1,511 images, includes out-of-taxonomy red spider mite |
| **Laksh619 (HF)** | 4,000 images, **half are cocoa** |
| **minayahhh liberica/robusta** | 1.49 GB / 790 MB, no description, licence "Unknown" |
| **johnandrewborabo** | Binary healthy/unhealthy — collapses the taxonomy |
| **trongtri04042004** | 25 MB, one class of the Uganda set; **not Saposoa despite the name** |
| **tuannguyenhoang merged 5-class** | Contains re-annotated BRACOL → training/testing leak |
| **tuannguyenhoang/coffee-leaves** | 11 GB, unknown provenance |
| **humpreyocay liberica/robusta** | 2.12 GB, undocumented species mix |
| **gihozopatrick, mohas8, izzaiqbal, badasstechie** | No description, no licence, no provenance |
| **jorgearoca/coffee-rust** | 6,726 **multispectral** images — remote sensing, not a phone |
| **Ethiopian Coffee & Tea Authority site** | Serves gambling SEO spam; do not cite |

---

## 7. Reproduce it

```bash
# 1. count every image, per class, and deduplicate
python scripts/audit_duplicates.py --raw data/raw --out data/audit

# 2. verify the downloaded archives themselves (originals kept in ~/Downloads)
unzip -t ~/Downloads/t2r6rszp5c-1.zip \
        ~/Downloads/tgv3zb82nd-1.zip \
        ~/Downloads/"RoCoLe A robusta coffee leaf images dataset.zip" \
        ~/Downloads/vfxf4trtcg-5.zip \
        ~/Downloads/"A Machine  Learning Dataset for Classification of Common Coffee Leaf Diseases in Uganda.zip"

# 3. check the publisher's manifest against the bytes (BRACOL)
curl -s "https://data.mendeley.com/public-api/datasets/yy2k5y8mxg/files?folder_id=root&version=1"
sha256sum "data/raw/bracol/BRACOL_coffee_leaf_ images_datasets.zip"
# expected 25a2fc973137f92caa6700b95e645a0eceeb041c3cfc1eaba853f3e1b5fdfc1f
```

Machine-readable output: `data/audit/duplication-report.json`.
Narrative audit: `docs/14-DUPLICATION-AUDIT.md`.
Evidence tiers: `docs/12-DATASET-VERIFICATION.md`.
Provenance registry: `data/dataset-sources.md`.

---

## 8. Open items

1. **Saposoa** and **CoffeeLeaf-CO v2** — archives not opened (T3). They are the last two external sets.
2. **Ethiopian** — 12,000 files, but the distinct count is unknown: `train aug/` is 10,800 augmented
   files derived from an unpublished original set. Only the 1,200-image `test/` split is clean.
3. **CerradoCoffeeLeaf** — not released; cite as prior work only.
4. **Healthy class** — 62 usable distinct images from JMuBEN. The corpus needs BRACOL/Uganda/RoCoLe
   healthy data, and the report must say so.
5. **Dedup for training, group for splitting** — `prepare_data.py` already keeps duplicate hashes in
   one split (T-03); the training loader should additionally keep one file per MD5 so a single image
   is not weighted 300× in the loss.
