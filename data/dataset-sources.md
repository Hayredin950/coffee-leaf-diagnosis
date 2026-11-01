# Dataset Sources — Verified Registry

> **Every row below was verified by a direct fetch on 21 October 2026.** The verification column
> records the HTTP status and the endpoint used. Nothing here is from memory.
>
> **Owner:** Hayredin Mohammed · **Reviewed by:** Nahom Solomon

## Download rules

1. **Cite the original, not the mirror.** The Kaggle and Hugging Face mirrors carry incorrect
   licence labels ("Unknown", "MIT", "CC BY-SA 4.0") that contradict the upstream CC BY 4.0
   record. Always attribute the Mendeley or Zenodo record.
2. **Do not commit the data.** The repository stays under 50 MB (NFR-32). `data/README.md`
   carries these URLs and `scripts/prepare_data.py` reproduces the split from them.
3. **Record the checksum** of every archive in `data/dataset-sources.md` after downloading, so
   the corpus is verifiable later.
4. **Respect the terms of each platform.** Mendeley, Zenodo and Kaggle all require a free
   account for some downloads; that is acceptable. No scraping, no paywalled content.

---

## A. Primary training sources

### A.1 JMuBEN — the field's primary dataset

| Field | Value |
|---|---|
| **Record title** | "JMuBEN" |
| **Authors** | J. Jepkoech, D. M. Mugo, B. K. Kenduiywo, E. C. Too (Univ. of Embu, Chuka Univ., JKUAT) |
| **URL** | https://data.mendeley.com/datasets/t2r6rszp5c/1 |
| **DOI** | 10.17632/t2r6rszp5c.1 |
| **Version / date** | v1, 26 March 2021 |
| **Licence** | CC BY 4.0 |
| **Classes in this record** | **Coffee Rust, Cerscospora, Phoma** (the record's own filenames: `Cerscospora-20210326T085017Z-001.zip`, `Leaf rust-20210326T083416Z-001.zip`, `Phoma-20210326T082051Z-001.zip`) |
| **Stated size** | 22,591 images across 3 archives (252 MB + 69 MB + 227 MB) |
| **Collection** | Mutira coffee plantation, Kirinyaga County, Kenya (0°28′59″S, 37°19′59″E). Fujifilm X-T4. Sunny, windy and cloudy days; both leaf surfaces. Labels assigned by a plant pathologist (Dr. Felix Rotich); annotated with a data-labelling web tool. **Noise filtering + contrast stretching; centre-square crop; resized; rotation (180° horizontal and vertical, counter-clockwise) and horizontal/vertical flipping applied as augmentation to the smaller images.** |
| **Verification** | ✅ Fetched 21 Oct 2026 — the dataset page and the public file-listing API (`data.mendeley.com/public-api/datasets/t2r6rszp5c/files?folder_id=root&version=1`) |
| **⚠️** | The paper's abstract says the two records are "respectively" `tgv3zb82nd` and `t2r6rszp5c`. That is **inverted** relative to the record titles. Cite the record IDs explicitly in the methods so a reviewer does not think the group mislabelled the classes. |
| **⚠️** | The record's "Steps to reproduce" text mentions healthy and miner folders — copy-paste boilerplate that contradicts the three files actually uploaded. Trust the file list. |

### A.2 JMuBEN2

| Field | Value |
|---|---|
| **Record title** | "JMuBEN2" |
| **URL** | https://data.mendeley.com/datasets/tgv3zb82nd/1 |
| **DOI** | 10.17632/tgv3zb82nd.1 |
| **Version / date** | v1, 26 March 2021 |
| **Licence** | CC BY 4.0 |
| **Classes in this record** | **Healthy, Miner** (`Healthy-20210326T083815Z-001.zip` 567 MB, `Miner-20210326T082341Z-001.zip` 725 MB) |
| **Stated size** | 35,964 images across 2 archives |
| **Collection** | The same campaign, the same authors and institutions |
| **Verification** | ✅ Fetched 21 Oct 2026, including the file-listing API |

### A.3 Class counts — the three published figures and what to use

| Source | Cercospora | Rust | Phoma | Miner | Healthy | Total |
|---|---|---|---|---|---|---|
| The paper's Table 1 | 7,682 | 8,337 | 6,572 | 16,979 | 18,985 | **58,555** |
| The Kaggle mirror (Data Explorer) | 7,681 | 8,336 | 6,571 | ~17,000 | ~19,000 | ~58,500 |
| The Hugging Face mirror (machine-readable API) | **7,681** | **8,336** | **6,571** | **16,978** | **18,983** | **58,549** |

**Decision:** the group uses the **Hugging Face figures (58,549)** as the reference count,
because they are the only ones obtainable from a machine-readable API and can be independently
reproduced by anyone. The six-image discrepancy against the paper is recorded in the datasheet.
**Hayredin must re-count the files after download and record what is actually present** — the
datasheet reports the observed count, not the published one.

> The paper's Table 1 also contains a typo: the fifth row is labelled "Rust 6572" where it
> means "Phoma 6572". The abstract has it right.

### A.4 Mirrors (download convenience only — cite the original)

| Mirror | URL | Notes | Licence as stated on the mirror |
|---|---|---|---|
| Kaggle | https://www.kaggle.com/datasets/noamaanabdulazeem/jmuben-coffee-dataset | v2, 2022-07-22. 1.84 GB per the view endpoint; 810 MB per the list endpoint — **the two API fields disagree, so do not quote a size**. Folder layout `JMuBEN/<class>/`. | "Unknown" (Kaggle) — **incorrect**; the upstream is CC BY 4.0 |
| Kaggle | https://www.kaggle.com/datasets/nvanhoa74/jmuben | v1, 2025-11-09 | "Unknown" |
| Hugging Face | https://huggingface.co/datasets/Project-AgML/arabica_coffee_leaf_disease_classification | Parquet; `num_examples = 58,549`; one `train` split; `ClassLabel` names `["Cerscospora","Healthy","Leaf_rust","Miner","Phoma"]`; image width min 74 / max 256 / median 128 | `cc-by-4.0` ✅ |

**Note on the class-name spelling.** "Cerscospora" is a misspelling that appears in the Mendeley
filenames, the Kaggle folder names and the Hugging Face `ClassLabel` names. The group uses the
correct spelling **"Cercospora"** everywhere except where it must match a source's literal
identifier, in which case it records the mapping explicitly in `data/dataset-sources.md` and in
`scripts/prepare_data.py`.

### A.5 BRACOL — the second Arabica source

| Field | Value |
|---|---|
| **Full name** | BRACOL — A Brazilian Arabica Coffee Leaf images dataset to identification and quantification of coffee diseases and pests |
| **Authors** | R. A. Krohling, G. J. M. Esgario, J. A. Ventura (Universidade Federal do Espírito Santo) |
| **URL** | https://data.mendeley.com/datasets/yy2k5y8mxg/1 |
| **DOI** | 10.17632/yy2k5y8mxg.1 |
| **Version / date** | v1, 6 November 2019 |
| **Licence** | CC BY 4.0 |
| **Archive** | One file, `BRACOL_coffee_leaf_ images_datasets.zip` (note the stray double space in the name), 164,516,964 bytes |
| **Counts** | **1,747 whole-leaf photographs** and **2,147 cropped symptom images**. **⚠️ The Omdena mirror documents 2,722 symptom images.** The group counts the files after download and states which figure it used. |
| **Classes** | leaf miner, leaf rust, brown leaf spot (Phoma), cercospora leaf spot, healthy |
| **Collection** | Santa Maria de Marechal Floreano, Espírito Santo, Brazil, across different times of the year. **Exactly five phones:** ASUS Zenfone 2, Xiaomi Redmi 5A, Xiaomi S2, Galaxy S8, iPhone 6S. The **abaxial (lower) leaf side**, on a white background, partially controlled conditions. "The acquisition of the images was done without much criterion to make the dataset more heterogeneous." Labelling assisted by an expert. |
| **Severity bands** | On the leaf dataset, computed from segmentation masks: healthy < 0.1 %; very low 0.1–5 %; low 5–10 %; high 10–15 %; very high > 15 % |
| **Splits** | Both sub-datasets are pre-split into train / validation / test. **The group does not use these splits** — it re-splits by group to prevent leakage. |
| **Verification** | ✅ Fetched 21 Oct 2026, including the public file-listing API |
| **⚠️ Citation trap** | The PeerJ cs-3386 paper cites BRACOL with the **RoCoLe** DOI (`c5yvn32dzg`). The correct BRACOL DOI is `10.17632/yy2k5y8mxg.1`. Do not propagate that error. |
| **⚠️ Leakage** | The symptom crops are **crops of the 1,747 leaves**. Group them together or they leak across the split. |

### A.6 RoCoLe — the only Robusta source

| Field | Value |
|---|---|
| **Full name** | RoCoLe: A robusta coffee leaf images dataset |
| **Authors** | J. Parraga-Alava, K. Cusme, A. Loor, E. Santander (ESPAM MFL, Ecuador; Univ. de Santiago, Chile) |
| **URL** | https://data.mendeley.com/datasets/c5yvn32dzg/2 |
| **DOI** | 10.17632/c5yvn32dzg.2 |
| **Version / date** | v2, 17 May 2019 |
| **Licence** | CC BY 4.0 |
| **Counts** | **1,560** images = 4 views × 390 plants |
| **Classes** | healthy 791 · red spider mite 167 · rust L1 344 / L2 166 / L3 62 / L4 30 |
| **Collection** | 5 MP smartphone, f/2.2 autofocus, working distance 200–300 mm, no zoom. Cloudy, sunny and windy days; backgrounds of other plants and weeds; upper and back leaf sides. CIIDEA, ESPAM MFL, Calceta, Manabí, Ecuador (−0.834206, −80.177159). Rust severity by the OIRSA/LANREF method. |
| **Annotations** | Labelbox web tool — object segmentation + classification; export to JSON, CSV, COCO, VOC, XLSX |
| **Verification** | ✅ Fetched 21 Oct 2026 |
| **⚠️ Leakage** | **Split by plant ID** (`C##P##`), never by image. Four near-duplicate views of one leaf otherwise land in both partitions. |
| **⚠️ Taxonomy** | Has red spider mite (a pest) and four rust severity levels. Collapse L1–L4 → `rust`. **Red spider mite is NOT leaf miner** — it must be an `unsupported` class. |
| **⚠️ Note** | The Kaggle mirror `nirmalsankalana/rocole-a-robusta-coffee-leaf-images-dataset` lists the licence as MIT — **incorrect**; the source is CC BY 4.0. It is classification-only with **no annotations** and its folder names are not fully verifiable. Use the Mendeley record. |

### A.7 Uganda 2025 — the African field set

| Field | Value |
|---|---|
| **Full name** | A machine learning dataset for classification of common coffee leaf diseases in Uganda |
| **Authors** | S. chelangat, R. Anirwoth, K. N. Mayanja, A. sserwadda (Soroti University) |
| **URL** | https://data.mendeley.com/datasets/k36wnd6knb/1 |
| **DOI** | 10.17632/k36wnd6knb.1 |
| **Version / date** | v1, 7 February 2025 |
| **Licence** | CC BY 4.0 |
| **Counts** | **3,312** images, JPEG 256×256 — Healthy 1,179 / Coffee Leaf Rust 1,023 / Phoma 1,110 |
| **Collection** | Smartphone on Ugandan farms; varying light (daylight and low light); leaves at early, medium and advanced growth stages. Duplicates removed; rotation, flipping and brightness augmentation applied. |
| **Verification** | ✅ Fetched 21 Oct 2026 |
| **Role in the project** | **The most valuable single dataset for the project.** It is African, from real farms, with a different camera and a different protocol — a genuine domain shift from Kenya's curated JMuBEN. It tests Rust, Phoma and Healthy. It cannot test Cercospora or Miner. |
| **⚠️** | The augmentation was already applied by the publishers, so the "duplicates removed" claim must be verified independently by the group's own pHash clustering. |

### A.8 Saposoa, Peru 2026

| Field | Value |
|---|---|
| **Full name** | Coffee leaf dataset by phytosanitary class |
| **Author** | J. C. Santa Maria Pinedo (UNMSM, Lima) |
| **URL** | https://data.mendeley.com/datasets/mfpxg4y65r/2 (v2, 18 Sep 2026) · v1 at `/1` |
| **DOI** | 10.17632/mfpxg4y65r.2 |
| **Licence** | CC BY 4.0 |
| **Counts** | **1,500** — perfectly balanced 500 / 500 / 500 |
| **Classes** | healthy · coffee leaf rust (*Hemileia vastatrix*) · coffee leaf spot (***Mycena citricolor***) |
| **Collection** | Arabica, Saposoa, San Martín, Peru. Uniform protocol: fixed camera-to-leaf distance, homogeneous natural lighting, in focus. Diagnosed by plant-health specialists. Non-probability convenience sampling stratified by condition; blurred, occluded and ambiguous images excluded. |
| **Verification** | ✅ Fetched 21 Oct 2026 |
| **⚠️ Taxonomy trap** | ***Mycena citricolor* ("ojo de gallo", American leaf spot) is NOT Cercospora.** It must be an `unsupported` / out-of-taxonomy class. Mapping it to Cercospora is one of the most common silent errors in this literature. |
| **⚠️** | A second-party audit reports 1,500 published → 1,499 downloaded → 1,498 usable (one corrupt rust file). Verify after download. |

### A.9 CoffeeLeaf-CO v2.0.0 — the Colombian detection set

| Field | Value |
|---|---|
| **Full name** | DECAFIA / CoffeeLeaf-CO v2.0.0 |
| **Authors** | L. E. Rosas Ruiz, A. F. Salom Medina, J. G. Barrero Perez (Universidad Industrial de Santander) |
| **URL** | https://zenodo.org/records/22756170 |
| **DOI** | 10.5281/zenodo.22756170 (concept DOI 10.5281/zenodo.19931903) |
| **Published** | 14 September 2026 |
| **Licence** | CC BY 4.0 |
| **Counts** | **2,315** images · **12,794** annotated instances · **1,113** background/healthy images (empty label files) |
| **Classes** | `0` roya (rust, *H. vastatrix*) · `1` coco (Curculionidae weevil defoliation) · `2` minador (leaf miner) |
| **Collection** | 1,705 own Colombian field images (El Socorro, Santander, 6°28′N 73°19′W, ~1,500 m, consumer Android smartphones, natural light, 2022–2023) + 610 from Silva *et al.* 2020. Annotation via VIA + SAM, YOLO `.txt`, **Cohen's κ = 0.91**. Splits: train 1,618 / val 348 / test 349, stratified, seed 42, zero filename and zero SHA256 collisions. Baseline YOLOv8m: mAP50 0.9235, mAP50-95 0.7293. |
| **Verification** | ✅ Fetched 21 Oct 2026 via the Zenodo REST API (`https://zenodo.org/api/records/22756170`) — the HTML page serves a JavaScript challenge |
| **⚠️** | **Use v2, not v1.** The v2 card documents that the v1 numbers (2,786 images / 15,181 instances / 4 classes / mAP50 92.4 %) were wrong. |
| **⚠️** | RoCoLe was deliberately removed from v2 so that RoCoLe stays an independent external set. Using v1 would contaminate it. |
| **Taxonomy** | Weevil damage → `unsupported`. Healthy is a background class, not a detection class, so it must be handled carefully if used for classification. |

### A.10 Silva *et al.* 2020 — the full-resolution set

| Field | Value |
|---|---|
| **Full name** | Rust and leaf miner in coffee crop (*Coffea arabica*) |
| **Authors** | L. B. Silva, A. L. C. Carneiro, M. S. A. Renaud Faulin (Faculdade de Tecnologia de São Paulo) |
| **URL** | https://data.mendeley.com/datasets/vfxf4trtcg/5 (v5, 20 Nov 2020; v3 also exists) |
| **DOI** | 10.17632/vfxf4trtcg.5 |
| **Licence** | CC BY 4.0 |
| **Counts** | **542** — 285 rust + 257 miner |
| **Collection** | Original smartphone resolution **4000×2250 RGB**, mostly laboratory shots on a white background, manually collected and labelled on a Brazilian farm |
| **Verification** | ✅ Fetched 21 Oct 2026 |
| **Role** | Small, but **full-resolution, single-stress, expert-labelled** — an ideal high-resolution spot-check set, and a good demonstration of what the model does with a real 4K photo rather than a 128×128 crop |

---

## B. Datasets that were checked and rejected

Recording the rejections matters: the report must show the group evaluated its options (§9.2),
and a reviewer may otherwise ask "did you consider X?".

| Dataset | URL | Why rejected |
|---|---|---|
| **PlantVillage** | https://github.com/spMohanty/PlantVillage-Dataset | **Contains no coffee classes.** Verified via the GitHub contents API: the 38 class folders are Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach, Pepper, Potato, Raspberry, Soybean, Squash, Strawberry and Tomato — no Coffee. Usable only as a non-coffee out-of-distribution control. |
| **AI-Lab-Makerere/beans** | https://huggingface.co/datasets/AI-Lab-Makerere/beans | 1,295 images, 3 classes — but it is **common bean**, not coffee. Usable only as an explicit negative control. |
| **Rwandan dataset** (Hitimana *et al.*) | doi:10.3390/technologies11050116 | 37,939 images from Rwanda — highly relevant, but the data availability statement says *"available on request"* and it includes images "downloaded from the internet", so it is not openly downloadable and its provenance is partly unverifiable. |
| **CoLeaf-DB** | https://data.mendeley.com/datasets/brfgw46wzb/1 | 1,006 images of **nutritional deficiency**, not disease. A different task. |
| **Coffee & cashew nut (UAV, Makerere)** | https://data.mendeley.com/datasets/r46c6bpfpf/1 | 3,000 coffee images of **fruit**, not leaves. |
| **Roboflow "Coffee leaf disease"** | https://universe.roboflow.com/dame-23kub/coffee-leaf-disease-kc1ca | 7,134 images, CC BY 4.0, **but** no published source, no methodology, **no healthy class**, and multi-label semantics with overlapping labels. Not usable as ground truth and must not be merged into a single-label training set. |
| **Kaggle "Metadata-Enhanced Coffee Disease Benchmark"** | https://www.kaggle.com/datasets/itznolex/metadata-enhanced-coffee-disease-benchmark | 90,780 images, CC0 — **but it is a superset of JMuBEN + BRACOL + RoCoLe + CoLeaf + Roboflow + others.** Using it as a held-out test set while training on those is guaranteed leakage. Use only for its metadata. |
| **JMuBEN3** (`jjn4ht687d`) | Mendeley | Described in the literature as a **sweet potato** leaf-rust dataset. Irrelevant. The file-listing API returned `[]`. |
| **IP102** | — | A 102-class insect-pest dataset, not coffee leaf disease. |
| **BRACOT** | https://data.mendeley.com/datasets/pmkbyjpf6k/1 | 300 images of instance segmentation. Small and of uncertain provenance. |
| **Ethiopian Coffee & Tea Authority website** | https://ethiocta.gov.et/ | The domain resolves but **currently serves gambling SEO spam**; `/about` and `/services` return 404. **Do not cite it.** |
| **Coffee and Tea Research Institute** | `ctri.gov.et` | Does not resolve. The institute's functions now sit inside **EIAR / Jimma Agricultural Research Center**. Cite JARC. |

---

## C. Final corpus plan

| Purpose | Datasets | Classes covered |
|---|---|---|
| **Training** (headline model) | JMuBEN + JMuBEN2 (+ BRACOL as the second Arabica source) | All 5 |
| **Training** (ablation variant B) | The above **+ Uganda 2025** | All 5, with African field data added |
| **External evaluation** | Uganda 2025 · RoCoLe · Saposoa Peru · CoffeeLeaf-CO v2 · Silva 2020 | Rust, Phoma, Healthy, Miner across 5 sets; Cercospora has **no independent external test** — stated as a limitation |

**⚠️ The headline model must exclude every external set from training**, and the exclusion is
asserted by test T-05 and by a CI check that compares the training manifest's source IDs
against the external set IDs.

---

## D. Download checklist

| # | Dataset | Done | SHA-256 recorded | Observed counts recorded | Files extracted to |
|---|---|---|---|---|---|
| 1 | JMuBEN (`t2r6rszp5c`) | ☐ | ☐ | ☐ | `data/raw/jmuben/` |
| 2 | JMuBEN2 (`tgv3zb82nd`) | ☐ | ☐ | ☐ | `data/raw/jmuben2/` |
| 3 | BRACOL (`yy2k5y8mxg`) | ☐ | ☐ | ☐ | `data/raw/bracol/` |
| 4 | RoCoLE (`c5yvn32dzg` v2) | ☐ | ☐ | ☐ | `data/raw/rocole/` |
| 5 | Uganda (`k36wnd6knb`) | ☐ | ☐ | ☐ | `data/raw/uganda/` |
| 6 | Saposoa Peru (`mfpxg4y65r` v2) | ☐ | ☐ | ☐ | `data/raw/peru/` |
| 7 | CoffeeLeaf-CO v2 (`22756170`) | ☐ | ☐ | ☐ | `data/raw/coffeeleafco/` |
| 8 | Silva 2020 (`vfxf4trtcg` v5) | ☐ | ☐ | ☐ | `data/raw/silva/` |

`data/raw/` is gitignored. The paths above are the only place the raw data lives.

---

## E. Verification ledger

| Source | Method | Result |
|---|---|---|
| Mendeley JMuBEN, JMuBEN2, BRACOL, RoCoLE, Uganda, Saposoa, Silva | Direct dataset-page fetch + the public file-listing API | ✅ HTTP 200 |
| Zenodo CoffeeLeaf-CO v2 | The Zenodo REST API (`zenodo.org/api/records/22756170`) | ✅ HTTP 200 |
| Hugging Face AgML JMuBEN mirror | The `datasets-server` `info` and `statistics` endpoints | ✅ HTTP 200 — 58,549 confirmed |
| Kaggle JMuBEN, RoCoLE, BRACOL-for-YOLO | The Kaggle datasets API (`view` and `list`) | ✅ HTTP 200 |
| PlantVillage | The GitHub contents API on `raw/color` | ✅ HTTP 200 — confirmed no coffee classes |
| All 38 paper DOIs | The Crossref REST API | ✅ HTTP 200 |
| arXiv records | The arXiv API | ✅ HTTP 200 |
| PubMed records | The NCBI E-utilities | ✅ HTTP 200 |
| peerj.com, frontiersin.org, PMC | Full-text fetch | ✅ HTTP 200 |
| ScienceDirect, MDPI, Wiley, IEEE Xplore, Taylor & Francis | Attempted | ❌ HTTP 403 — **bibliographic metadata only; read via the university library before quoting any figure** |
