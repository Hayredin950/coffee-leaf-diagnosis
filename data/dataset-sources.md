# Dataset Sources — Verified Registry

> **Every row below was verified by a direct fetch on 21 October 2026.** The verification column
> records the HTTP status and the endpoint used. Nothing here is from memory.
>
> **Owner:** Hayredin Mohammed · **Reviewed by:** Nahom Solomon
>
> ---
>
> ### ⚠️ Read `docs/12-DATASET-VERIFICATION.md` first
>
> On **7 November 2026** every record was re-fetched and, where possible, **the files were counted**.
> That pass found: the true JMuBEN total is **58,549** (two independent mirrors agree); the Uganda
> Mendeley release contains **3,322** files, not the claimed 3,312; Uganda has a **12,480-image
> original** and a **26,335-image augmented** release that this registry did not know about; and an
> **Ethiopian dataset of 12,000 images** exists on Kaggle and is the only Cercospora set we can
> verify and hold out. The three-tier evidence scale (T1 verified twice … T4 claimed only) is defined
> in §0 of that file. **This registry keeps the provenance; that file keeps the count.**
>
> ### ⚠️ Then on 8 November 2026 the archives were opened
>
> Six archives were downloaded and every image hashed. **JMuBEN + JMuBEN2 contain 58,550 files but
> only 3,757 distinct images (93.6 % are byte-identical copies).** The Healthy class is 18,984 files
> and 63 distinct images. Uganda has 3,322 files, **1,810 distinct** and **102 zero-byte files**.
> RoCoLe has 67 images duplicated across different plant IDs. See
> **`docs/14-DUPLICATION-AUDIT.md`** for the table, the method and the proof. Any count below that is
> a **file** count must be read as such, and the split groups by MD5 before anything else.

## Download rules

1. **Cite the original, not the mirror.** The Kaggle and Hugging Face mirrors carry incorrect
   licence labels ("Unknown", "MIT", "CC BY-SA 4.0") that contradict the upstream CC BY 4.0
   record. Always attribute the Mendeley or Zenodo record.
2. **Do not commit the data.** The repository stays under 50 MB (NFR-32). This registry carries the
   URLs and `scripts/prepare_data.py` reproduces the split from them.
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

**Decision:** the group uses the **observed archive counts (58,550 files)** as the reference *file*
count, because they are the only ones counted from the publisher's own bytes. The mirrors report
58,549 (one file short) and the paper reports 58,555 (a rounded/estimated figure). All three are
recorded in the datasheet.

**But the number that goes in the report is the distinct-image count, not the file count:**

| Class | Files | Distinct images |
|---|---:|---:|
| Leaf rust | 8,336 | 1,042 |
| Cercospora | 7,681 | 322 |
| Phoma | 6,571 | 691 |
| Miner | 16,978 | 1,639 |
| Healthy | 18,984 | 63 |
| **Total** | **58,550** | **3,757** |

Counted 8 Nov 2026 from `t2r6rszp5c-1.zip` + `tgv3zb82nd-1.zip`, MD5 over every file. Proof and
caveats in `docs/14-DUPLICATION-AUDIT.md`.

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

#### A.4.1 Every Kaggle mirror, and the licence each one claims

Checked 7 November 2026 with the Kaggle view endpoint. **A mirror's licence field is not the
publisher's licence.** Three of these are wrong, and one is a genuine trap.

| Mirror | Record it copies | Size (unpacked) | Licence on the mirror | Verdict |
|---|---|---|---|---|
| `noamaanabdulazeem/jmuben-coffee-dataset` | JMuBEN + JMuBEN2 | 1.84 GB | "Unknown" | Wrong. Upstream is CC BY 4.0. Use for speed; cite Mendeley. |
| `anitagarg123/coffee-leaves` | RoCoLe | 2.27 GB | "Unknown" | Wrong. Upstream is CC BY 4.0. Includes `RoCoLE-csv.csv`, which the Mendeley record also has. |
| `diegopgonzlez/rocoleoriginal` | RoCoLe | 2.27 GB | **CC BY-SA 4.0** | A **share-alike** claim on a CC BY 4.0 record. Do not rely on it. |
| `alvarole/coffee-leaves-disease` | Silva 2020 | 1.50 GB | "Data files © Original Authors" | Same author as the Mendeley record, so this is a second *release*, not an independent source. |
| `chelangatspecioza/coffeedataset34` | Uganda 2025, **augmented** | 435 MB | **CC BY-NC-SA 4.0** | **Non-commercial.** See the warning below. |
| `biniyamyoseph/ethiopian-coffee-leaf-disease` | itself (no upstream) | 2.12 GB | **CC0 1.0** | The uploader's own record. No paper. |
| `jonatanfragoso/bracol-for-yolov8-detection` | BRACOL, re-annotated | 335 MB | CC BY 4.0 | **Incomplete** — 2,885 images, not the 3,894 of the original. Do not use it to verify a count. |

> **⚠️ The Uganda augmented mirror is CC BY-NC-SA 4.0.** The `NC` clause forbids commercial use.
> BunaDoctor is meant to be a product, so **the headline model must train on the Mendeley original
> (`k36wnd6knb`, CC BY 4.0), not on the Kaggle augmented re-upload**. The augmented set can be used
> for an ablation only if that ablation is not part of the shipped model, and the report must say
> which one was used. This is exactly the kind of trap that a "download the biggest coffee dataset"
> search walks into.

> **⚠️ The two Kaggle size fields disagree.** The `datasets/view` endpoint reports `totalBytes`
> (unpacked) while `datasets/list` reports the download size. On the JMuBEN mirror they differ by
> more than 2×. **Never quote a size from the API**; quote the archive size from the publisher.

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
| **⚠️ The publisher's file is truncated** | The Mendeley archive stops at image `688.jpg`: **1,402 of 1,747** images, no zip central directory. Two independent downloads are byte-identical, and the SHA-256 matches Mendeley's own manifest (`25a2fc97…`), so the file is broken **at the source**, not in transit. |
| **Repair** | The missing 345 images were restored from the Hugging Face mirror `luisangelico/bracol`, whose `dataset.csv` and `images/1.jpg` are byte-identical to the Mendeley release. **Now 1,747 files, 1,746 distinct, 0 unreadable.** Cite Mendeley; the mirror is a repair channel, not a separate source. |
| **Counts — observed (8 Nov 2026)** | **1,747 whole-leaf photographs**, 210.3 MB. `dataset.csv` has 1,747 rows. The 2,147 symptom crops are **not** in this archive — it ships the leaf images plus labels only. |
| **Class encoding in `dataset.csv`** | `predominant_stress`: **0 = healthy (272) · 1 = leaf miner (387) · 2 = leaf rust (531) · 3 = phoma (348) · 4 = cercospora (147) · 5 = mixed infection (62)**. Only the 1,685 single-label rows are usable for 5-class training; the 62 mixed rows need a separate label or exclusion. |
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
| **Counts** | **1,560** images = 4 views × 390 plants. **1,493 distinct** (67 byte-identical duplicates, counted 8 Nov 2026). |
| **Classes** | healthy 791 · red spider mite 167 · rust L1 344 / L2 166 / L3 62 / L4 30 |
| **Collection** | 5 MP smartphone, f/2.2 autofocus, working distance 200–300 mm, no zoom. Cloudy, sunny and windy days; backgrounds of other plants and weeds; upper and back leaf sides. CIIDEA, ESPAM MFL, Calceta, Manabí, Ecuador (−0.834206, −80.177159). Rust severity by the OIRSA/LANREF method. |
| **Annotations** | Labelbox web tool — object segmentation + classification; export to JSON, CSV, COCO, VOC, XLSX |
| **Verification** | ✅ Fetched 21 Oct 2026 |
| **⚠️ Leakage** | **Split by plant ID** (`C##P##`), never by image. Four near-duplicate views of one leaf otherwise land in both partitions. **⚠️ The 67 duplicates are cross-plant**: e.g. `C11P19E1.jpg` = `C12P28E1.jpg`. A plant-level split alone still leaks them — deduplicate by MD5 *before* assigning plants to folds. See `docs/14-DUPLICATION-AUDIT.md` §5. |
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
| **Counts — published** | **3,312** images, JPEG 256×256 — Healthy 1,179 / Coffee Leaf Rust 1,023 / Phoma 1,110 |
| **Counts — observed (8 Nov 2026)** | **3,322 files** — Healthy **1,179** / CLR **1,033** / Phoma **1,110**. **But only 1,810 are distinct images, and 102 files are zero bytes** (Healthy 100, CLR 2). Usable: Healthy **739** / CLR **617** / Phoma **454**. The CLR class has ten more files than the description claims; the "duplicates removed" claim in the description is **false**. |
| **Collection** | Smartphone on Ugandan farms; varying light (daylight and low light); leaves at early, medium and advanced growth stages. Duplicates removed; rotation, flipping and brightness augmentation applied. |
| **Verification** | ✅ Fetched 21 Oct 2026 · ✅ files counted and hashed 8 Nov 2026 |
| **Role in the project** | **The most valuable single dataset for the project.** It is African, from real farms, with a different camera and a different protocol — a genuine domain shift from Kenya's curated JMuBEN. It tests Rust, Phoma and Healthy. It cannot test Cercospora or Miner. **Use 1,810, not 3,322.** |
| **⚠️** | The augmentation was already applied by the publishers, and 45.5 % of the files are byte-identical copies. Drop the 102 zero-byte files first; then group by MD5. Proof in `docs/14-DUPLICATION-AUDIT.md` §4. |

#### A.7.1 The two larger Uganda releases — this registry missed them

The same authors uploaded a **larger Kaggle release**. Its description gives the pre-augmentation
counts, which is exactly what the project has been missing.

| Release | Record | Claimed | Observed | Tier |
|---|---|---|---|---|
| **Original, before augmentation** | Kaggle `chelangatspecioza/coffeedataset34` (description) | **12,480** = Healthy 4,200 / CLR 4,050 / Phoma 4,230 | **not uploaded** | T3 |
| **Augmented** | Kaggle `chelangatspecioza/coffeedataset34` | 26,315 = 9,025 / 8,330 / 8,960 | **26,335** = **9,045** / 8,330 / 8,960 | **T2** |
| **Mendeley v1** | Mendeley `k36wnd6knb` v1 | 3,312 = 1,179 / 1,023 / 1,110 | **3,322** = 1,179 / **1,033** / 1,110 | **T2** |

**Consequences:**
1. The "3,312-image Uganda dataset" in the literature is a **slice** of a 12,480-image original.
2. The augmented release (26,335) is the largest African field corpus available and is a far stronger
   ablation-B training set than the 3,322-image record.
3. Both public releases are augmented ⇒ **request the 12,480 originals** from the authors (Soroti
   University: Specioza Chelangat, Racheal Anirwoth, Kizito Najib Mayanja, Abubakhari Sserwadda).
4. The augmented release carries **CC BY-NC-SA 4.0** on one mirror and **CC BY-SA 4.0** on another;
   the Mendeley record is CC BY 4.0. Cite the Mendeley DOI and state the conflict.

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
| **Second-source check (7 Nov 2026)** | The Kaggle record `alvarole/coffee-leaves-disease` — uploaded by the **same author** — lists exactly **542 JPG + 542 XML**. It is a second release, not an independent one, so the count is **T2**, not T1. |

### A.11 Ethiopian coffee-leaf dataset — **new, and the only Ethiopian data in public**

Discovered 7 November 2026. This record was not in any earlier version of this registry and is the
most consequential find of the verification pass.

| Field | Value |
|---|---|
| **Record** | Kaggle `biniyamyoseph/ethiopian-coffee-leaf-disease` |
| **Uploader** | Biniyam Yoseph |
| **Updated** | 8 June 2024 · **2.12 GB** · 1,606 downloads |
| **Licence** | CC0 (the uploader's claim; **no institution, no paper, no methodology statement**) |
| **Classes** | Cercospora, Healthy, Leaf rust, Phoma — **four of our five; no Leaf Miner** |
| **Counts — observed (7 Nov 2026)** | **12,000 JPG** — `train aug/` **2,700 × 4 = 10,800**; `test/` **300 × 4 = 1,200** |
| **Tier** | **T2** (Kaggle file manifest, every file enumerated) |
| **Why it matters** | It is **Ethiopian**; it is **perfectly balanced**; and its **test split is the only Cercospora set we can verify and hold out**. Our registry previously said Cercospora had no independent external test. (BRACOL also contains Cercospora but is a planned training source, so it cannot be external; `Laksh619/Coffee-Cocoa-Diseases` has 500 `coffee_browneye` images but is an unverified coffee+cocoa aggregation.) |
| **How to use it** | **External test only** (T-05): the 1,200-image `test/` split. **Never train on it.** |
| **⚠️ Provenance** | Self-uploaded, no paper, no named annotator, licence unverifiable. The balanced `test/` split is a sign of **curation, not of a random field sample**, so its accuracy will be optimistic. State this in the same sentence as the result. |
| **⚠️ Augmentation** | `train aug/` is explicitly augmented ⇒ 10,800 files ≠ 10,800 independent samples. |

### A.12 CerradoCoffeeLeaf — announced, **not released** (cite as prior work)

| Field | Value |
|---|---|
| **Record** | GitHub `joaofmari/cerradocoffeeleaf-cross-dataset-analysis` |
| **What it claims** | 1,476 in-the-wild Brazilian field images, **7 classes**, predefined 64/16/20 splits, designed for cross-dataset generalisation |
| **Status (7 Nov 2026)** | **Not downloadable.** The README's Zenodo link is the literal placeholder `[LINK]`; the dataset repository returns 404. Tier **T4**. |
| **Why it is still valuable** | It **independently confirms our central data claim**: *"preliminary inspection suggests the presence of augmented samples, which may inflate within-dataset performance"* (JMuBEN). Cite it in §2 of the proposal as corroboration, and do not wait for the data. |

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
| **iCog Labs Coffee Disease Dataset** | https://github.com/iCogLabs/Coffee-Disease-Dataset | 2019 iCog Makers challenge, Addis Ababa. **The repository is empty** — created and last pushed 2019-04-11, 0 bytes. Checked 7 Nov 2026. Dead end. |
| **dvelaren/clr-dataset** | https://github.com/dvelaren/clr-dataset | **4,398 JPG**, 5 rust-severity stages, 3-month time series, EAFIT Colombia. **Severity only** — no healthy, no other disease. Useless for five-class training; keep as a reference for ★4 (longitudinal history). |
| **Zenodo 14628690** | https://zenodo.org/records/14628690 | `dataset.zip`, 810.8 MB, CC BY 4.0, but **no description, no class statement, no paper**. Cannot be characterised from metadata; low priority. |
| **brainer-fp66/coffee-leaf-diseases** (HF) | https://huggingface.co/datasets/brainer-fp66/coffee-leaf-diseases | 1,511 images — Healthy 362 / Miner 336 / Phoma 338 / **Red Spider Mite 116** / Rust 359. Smaller than JMuBEN, duplicates its classes, and the mite class is out-of-taxonomy. Sanity-check set only. |
| **Laksh619/Coffee-Cocoa-Diseases** (HF) | https://huggingface.co/datasets/Laksh619/Coffee-Cocoa-Diseases | 4,000 = 8 classes × 500, **coffee + cocoa**. Half the classes are cocoa; merging would teach the model cocoa diseases. Example of why a "coffee leaf" search result must be inspected. |
| **minayahhh liberica / robusta** (Kaggle) | `minayahhh/liberica-coffee-leaf-dataset`, `minayahhh/robusta-coffee-leaf-dataset` | 1.49 GB / 790 MB, **no description, licence "Unknown"**. Cannot characterise classes or provenance. |
| **johnandrewborabo binary** (Kaggle) | `johnandrewborabo/coffee-leaf-binary-classification-dataset` | 3.1 GB, Healthy vs Unhealthy. Binary — collapses the taxonomy we are building. |
| **trongtri04042004 partial Uganda** (Kaggle) | `trongtri04042004/coffee-dataset-mendeley` | 25 MB, **6 downloads**. Its entire manifest is `coffee dataset/Health leaves/1_*.jpg` — a single class of the Uganda set. **Not Saposoa, despite the name.** Checked 7 Nov 2026. |
| **tuannguyenhoang merged 5-class** (Kaggle) | `tuannguyenhoang/coffee-leaves-disease-5-classes-merged-dataset` | 2.09 GB, "Unknown". A YOLO merge whose files are named `BRACOL_REVIEWED_*` — i.e. **it contains a re-annotated BRACOL**, so training on it and testing on BRACOL leaks. Rejected. |
| **tuannguyenhoang/coffee-leaves** (Kaggle) | `tuannguyenhoang/coffee-leaves` | 11 GB, "Unknown", no description. Cannot be characterised; a merge of unknown provenance. |
| **humpreyocay liberica/robusta** (Kaggle) | `humpreyocay/self-captured-liberica-robusta-coffee-leaves` | 2.12 GB, "Unknown", no description. Self-captured, but the species mix (liberica + robusta) and the class list are undocumented. |
| **gihozopatrick coffee pests** (Kaggle) | `gihozopatrick/coffee-pests-and-diseases` | 1.53 GB, "Unknown", no description. Possibly Ugandan; **cannot be verified** from the manifest. |
| **mohas8/coffee-disease** (Kaggle) | `mohas8/coffee-disease` | 142 MB, "Unknown", no description, 6 downloads. Unverifiable. |
| **jorgearoca/coffee-rust multispectral** (Kaggle) | `jorgearoca/coffee-rust` | 6,726 **multispectral** images (RGB JPG + five TIF bands: blue, green, red, NIR, red-edge), CC0, 386 downloads. Real and well-formed, but it is a **remote-sensing** product, not a phone photograph — incompatible with the deployment target. |
| **izzaiqbal/capstone-project** (Kaggle) | `izzaiqbal/capstone-project` | Folder layout `Coffee Leaf Diseases/Coffee leaf Diseases/Healthy/…`. No description, no licence, no provenance. Unverifiable merge. |
| **badasstechie/coffee-leaf-diseases** (Kaggle) | `badasstechie/coffee-leaf-diseases` | Pre-split `test/` tree, no description, no licence. Unverifiable. |

---

## C. Final corpus plan

| Purpose | Datasets | Distinct images | Classes covered |
|---|---|---|---|
| **Training** (headline model) | JMuBEN + JMuBEN2 (**3,757 distinct / 58,550 files**) + BRACOL (1,747 leaves) | ~5,500 | All 5 — but Healthy is thin (62 distinct from JMuBEN), so healthy comes from BRACOL + Uganda |
| **Training** (ablation variant B) | The above **+ Uganda original (1,810 distinct / 3,322 files, CC BY 4.0)** | ~7,300 | All 5, with African field data added |
| **Research-only ablation** | Uganda augmented (26,335 files, **CC BY-NC-SA 4.0**) | not deduplicated | **Non-commercial.** Report it as an ablation, never ship a model trained on it. |
| **External evaluation — African** | Uganda Mendeley (**1,810**) · **Ethiopian `test/` split (1,200 files, ~1,200 unique)** | ~3,000 | Rust, Phoma, Healthy, **Cercospora** — the Ethiopian test split is the only Cercospora set we can verify and hold out |
| **External evaluation — other** | RoCoLe (**1,493 distinct** / 1,560) · Silva (542) · Saposoa (1,500) · CoffeeLeaf-CO (2,315) | ~5,850 | Rust, Miner, Healthy |
| **Optional — ★4 only** | dvelaren CLR (4,398) | rust severity, longitudinal |

**⚠️ Deduplicate before splitting.** 93.6 % of the JMuBEN files are byte-identical copies and
45.5 % of Uganda's are. The split groups by MD5 **first**; the manifest records the effective
sample size. See `docs/14-DUPLICATION-AUDIT.md`.

**⚠️ Licence rule for a product.** The headline model must be trainable on CC BY 4.0 / CC0 data
only. The augmented Uganda mirror is **CC BY-NC-SA 4.0**; it is excluded from the shipped model and
may appear only as a research ablation, labelled as such.

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
| 9 | **Ethiopian** (Kaggle `biniyamyoseph/…`) | ☐ | ☐ | ☐ | `data/raw/ethiopian/` |
| 10 | **Uganda augmented** (Kaggle `chelangatspecioza/coffeedataset34`) | ☐ | ☐ | ☐ | `data/raw/uganda_aug/` |

`data/raw/` is gitignored. The paths above are the only place the raw data lives. Run
`notebooks/00-dataset-verification.ipynb` after placing the archives; it fills every ☐ in this table.

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
