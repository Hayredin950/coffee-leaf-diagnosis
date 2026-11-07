# Dataset Verification — the grounded count

**Question asked:** *"Gather all available datasets and report the count before any preprocessing."*
**Answer date:** Sat 7 November 2026 (W3) · **Owner:** Hayredin Mohammed · **Status:** research complete, Colab confirmation pending
**Rule this document follows:** a number is only written down if it came from a **server response we
can reproduce**, and every number carries a **tier** saying how strong the evidence is.

---

## 0. Why this file exists

The internet is full of coffee-leaf dataset counts, and most of them are copied from a paper table
that was never checked against the files that were actually uploaded. If we repeat one of those
numbers and a panel member opens the dataset, the project loses credibility in ten seconds.

So this file separates four different things that everybody else conflates:

| Tier | Meaning | How we got it |
|---|---|---|
| **T1 — verified twice** | The count was read from the files of **two independent releases** and they agree | Mendeley file manifest **and** a Kaggle/HF mirror manifest |
| **T2 — verified once** | The count was read directly from the publisher's own file manifest | Mendeley or Kaggle listing API |
| **T3 — reported by publisher** | The publisher *says* this in the description, but the files are inside a zip/RAR we did not open | Dataset description text |
| **T4 — claimed only** | A paper or README says it, and we could not find the files at all | Paper table / README |

**Nothing below is T4 unless it is labelled T4.** The numbers the group quotes in the proposal and
the report will be **T1 or T2 only**, with T3/T4 shown in a footnote as "published, not observed".

---

## 1. The headline table

This is the table to paste into the proposal, the datasheet, and the message to John.

| # | Dataset | Record | Claimed by publisher | **Observed in the release** | Tier | Class coverage |
|---|---|---|---|---|---|---|
| 1 | **JMuBEN** | Mendeley `t2r6rszp5c` v1 | 22,591 | 3 zips, 549.1 MB — internals not opened | T3 (zip) | Rust, Cercospora, Phoma |
| 2 | **JMuBEN2** | Mendeley `tgv3zb82nd` v1 | 35,964 | 2 zips, 1,291.7 MB — internals not opened | T3 (zip) | Healthy, Miner |
| 1+2 | **JMuBEN combined** | — | **58,555** (paper Table 1) | **58,549** | **T1** | all five |
| 3 | **BRACOL** | Mendeley `yy2k5y8mxg` v1 | 1,747 leaves + 2,147 crops | 1 zip, 164.5 MB — **contents not verified** | T3 (zip) | all five |
| 4 | **RoCoLe** | Mendeley `c5yvn32dzg` v2 | 1,560 | **1,560 JPG**, 2.27 GB, **390 plants × 4 views** | **T1** | Rust, Healthy, red spider mite |
| 5 | **Uganda (Mendeley)** | Mendeley `k36wnd6knb` v1 | 3,312 | **3,322 JPG**, 256×256, **already augmented** | **T2** | Rust, Phoma, Healthy |
| 5a | **Uganda — original** | Kaggle `chelangatspecioza/coffeedataset34` | **12,480** (4,200 / 4,050 / 4,230) | originals **not uploaded** | T3 | Rust, Phoma, Healthy |
| 5b | **Uganda — augmented** | same Kaggle record | 26,315 (9,025 / 8,330 / 8,960) | **26,335** (9,045 / 8,330 / 8,960) | **T2** | Rust, Phoma, Healthy |
| 6 | **Saposoa, Peru** | Mendeley `mfpxg4y65r` v2 | 1,500 (500 × 3) | 1 RAR, 3.45 GB — contents not opened | T3 (RAR) | Rust, Healthy, *Mycena* |
| 7 | **Silva 2020** | Mendeley `vfxf4trtcg` v5 | 542 | **542 JPG + 542 XML** (285 rust + 257 miner) | **T1** | Rust, Miner |
| 8 | **CoffeeLeaf-CO v2** | Zenodo `22756170` | 2,315 images, 12,794 instances | 1 zip, 167.5 MB | T3 (zip) | Rust, Miner, weevil |
| 9 | **Ethiopian (NEW)** | Kaggle `biniyamyoseph/ethiopian-coffee-leaf-disease` | — | **12,000 JPG** (10,800 train-aug + 1,200 test) | **T2** | **Cercospora**, Rust, Phoma, Healthy |
| 10 | **CerradoCoffeeLeaf (NEW)** | GitHub `joaofmari/…` | 1,476 (7 classes) | **not released — download link is a placeholder** | T4 | 7 classes |
| 11 | **Zenodo 14628690 (NEW)** | Zenodo `14628690` | — | 1 zip, 810.8 MB | T3 | rust / not-rust |
| 12 | **brainer-fp66 HF (NEW)** | HF `brainer-fp66/coffee-leaf-diseases` | — | **1,511** (Healthy 362 / Miner 336 / Phoma 338 / **Red Spider Mite 116** / Rust 359) | **T2** | 4 + pest |
| 13 | **Laksh619 HF (NEW)** | HF `Laksh619/Coffee-Cocoa-Diseases` | — | **4,000** (8 classes × 500) | **T2** | coffee + cocoa |
| 14 | **dvelaren CLR (NEW)** | GitHub `dvelaren/clr-dataset` | — | **4,398 JPG**, 5 rust-severity stages, 3-month time series | **T2** | rust severity only |
| 15 | **iCog 2019 (checked)** | GitHub `iCogLabs/Coffee-Disease-Dataset` | — | **repository is empty (0 bytes)** | **T2** | none |

**The usable total for the project is not one number.** It is:
- **58,549** for the five-class training corpus (JMuBEN + JMuBEN2),
- **+12,000** Ethiopian field images that we did not know existed (four of our five classes, and —
  as far as we can verify — the only Cercospora set we can use as an independent external test),
- **+1,560** RoCoLe, **+542** Silva, **+3,322** Uganda, **+1,500** Saposoa, **+2,315** CoffeeLeaf-CO
  as external sets.

---

## 2. The five discrepancies that matter

These are the findings no other group will have, because no other group counted the files.

### 2.1 JMuBEN: the paper says 58,555; the release contains 58,549

| Class | Paper Table 1 | HF mirror | Kaggle mirror | Difference |
|---|---|---|---|---|
| Cercospora | 7,682 | 7,681 | 7,681 | −1 |
| Healthy | 18,985 | 18,983 | 18,983 | −2 |
| Leaf rust | 8,337 | 8,336 | 8,336 | −1 |
| Leaf miner | 16,979 | 16,978 | 16,978 | −1 |
| Phoma | 6,572 | 6,571 | 6,571 | −1 |
| **Total** | **58,555** | **58,549** | **58,549** | **−6** |

**Two independent mirrors agree to the image.** That upgrades this from "a mirror says" to T1. The
paper's total is not wrong by accident — six images were dropped between the paper and the upload.

**What we write:** *"The published total is 58,555; the released corpus contains 58,549 (verified
against two independent mirrors on 7 November 2026). We report 58,549."*

**Bonus finding:** the paper's Table 1 also mislabels its fifth row as "Rust 6572" where it means
"Phoma 6572". The mirrors have it right.

### 2.2 Uganda on Mendeley: 3,312 claimed, 3,322 present

| Class | Description says | Files present | Difference |
|---|---|---|---|
| Healthy (`1_*.jpg`) | 1,179 | **1,179** | 0 |
| Coffee Leaf Rust (`1200_*.jpg`) | 1,023 | **1,033** | **+10** |
| Phoma (`2300_*.jpg`) | 1,110 | **1,110** | 0 |
| **Total** | **3,312** | **3,322** | **+10** |

**The rust class is ten images larger than the description claims.** This matters because rust is the
headline class: any per-class recall computed on the "published" denominator would be slightly wrong.

**And the description admits the images are already augmented** (rotation, flipping, brightness). So
this is **not** a clean 3,312-image field set; it is an augmented derivative. That makes duplicate
clustering mandatory before it is used for anything but external testing.

### 2.3 Uganda has a bigger parent dataset that nobody cites

The Ugandan authors uploaded a **second, larger** Kaggle release. Its own description states:

> "The original coffee leaf dataset consisted of **12,480 images**, comprising 4,200 Healthy,
> 4,050 Coffee Leaf Rust (CLR), and 4,230 Phoma Leaf Spot images. Data augmentation … resulted in a
> final dataset of **26,315 images**, comprising 9,025 Healthy, 8,330 CLR, and 8,960 Phoma."

We counted the augmented release: **26,335 files** — Healthy **9,045**, CLR **8,330**, Phoma **8,960**.
So the description is again off, this time by **+20 in Healthy**.

| Release | Claimed | Observed | Tier |
|---|---|---|---|
| Original (before augmentation) | 12,480 | **not uploaded** | T3 |
| Augmented | 26,315 | **26,335** | T2 |
| Mendeley v1 | 3,312 | **3,322** | T2 |

**This is the single most useful discovery in the whole crawl.** It means:
1. The "3,312-image Uganda dataset" that appears in the literature is a **small slice** of a 12,480-image
   original. If we can get the originals, our external African test set triples in size.
2. The 26,335-file augmented release is **larger than RoCoLe, Silva, Saposoa and CoffeeLeaf-CO combined**
   and it is African field data — the closest domain to Ethiopia that exists.
3. Because both public releases are augmented, **we must request the 12,480 originals from the authors**
   (they are at Soroti University; the Mendeley record lists Specioza Chelangat and three co-authors).

### 2.4 An Ethiopian dataset exists and we did not have it

`biniyamyoseph/ethiopian-coffee-leaf-disease` (Kaggle, CC0, 2.12 GB, 1,606 downloads, updated
2024-06-08). We counted every file:

| Split | Cercospora | Healthy | Leaf rust | Phoma | Total |
|---|---|---|---|---|---|
| `train aug/` | 2,700 | 2,700 | 2,700 | 2,700 | **10,800** |
| `test/` | 300 | 300 | 300 | 300 | **1,200** |
| **Total** | **3,000** | **3,000** | **3,000** | **3,000** | **12,000** |

**Why this is important:**
- It is **Ethiopian** — the only Ethiopian coffee-leaf dataset we have found.
- It is **perfectly balanced** at 3,000 per class, and the **test split is clean and balanced** (300 each).
- It contains **Cercospora**, which is exactly the class for which our registry currently says
  *"no independent external test exists"*. This dataset is the only Cercospora set we have found
  that we can hold out, verify and use as a test.
- It has **four of our five classes** — only Leaf Miner is missing.

**Why we still handle it carefully:**
- It is a **self-uploaded Kaggle dataset with no paper, no methodology statement and no named
  annotator**. The CC0 licence is the uploader's claim, not an institution's.
- The `train aug/` folder is **explicitly augmented**, so it is not 10,800 independent samples.
- The `test/` folder is balanced by construction, which is a sign of **curation**, not of a random
  field sample — so its accuracy will be optimistic relative to a real farm.

**Decision:** use the **1,200-image test split as an external test set**, report its provenance
limitation in the same sentence as its result, and **never train on it** (T-05). It is the only way
to report Cercospora recall on non-Kenyan data.

### 2.5 BRACOL and Saposoa cannot be counted without opening the archive

Both are single compressed archives (BRACOL 164.5 MB zip; Saposoa 3.45 GB RAR) whose download
requires a Mendeley account. The file *listing* gives the archive, not its contents.

- **BRACOL:** the YOLO re-annotation on Kaggle (`jonatanfragoso/bracol-for-yolov8-detection`) contains
  only **2,885** images across two subsets — **fewer** than the 1,747 + 2,147 = 3,894 the record claims.
  So the mirror is **incomplete** and must not be used as the count. **BRACOL stays T3 until we open
  the zip on Colab.**
- **Saposoa:** one RAR named `Coffe Leaf.rar` (note the typo), 3.45 GB. A second-party audit reports
  1,500 published → 1,499 downloaded → 1,498 usable. **T3 until we open it.**

This is exactly what the Colab notebook in §6 is for.

---

## 3. The datasets we checked and rejected (and why the rejection is evidence)

The report has to show that we looked, so the rejection is part of the result.

| Dataset | What it is | Why rejected |
|---|---|---|
| **CerradoCoffeeLeaf** (`joaofmari/cerradocoffeeleaf-cross-dataset-analysis`) | 1,476 in-the-wild Brazilian field images, **7 classes**, predefined 64/16/20 splits, designed for **cross-dataset generalisation** | **The Zenodo download link in its own README is literally `[LINK]`** — the dataset is announced but not released (checked 7 Nov 2026). Its *method* is directly relevant: it independently confirms our claim that JMuBEN is pre-augmented ("preliminary inspection suggests the presence of augmented samples, which may inflate within-dataset performance"). Cite the repo as prior work; do not wait for the data. |
| **iCog Labs Coffee Disease Dataset** | 2019 iCog Makers challenge, Addis Ababa | **The GitHub repository is empty** (created and last pushed 2019-04-11, 0 bytes). Dead end. |
| **dvelaren/clr-dataset** | 4,398 JPG, 5 rust-severity stages, 3-month time series, EAFIT Colombia | Rust **severity only** — no healthy, no other disease. Useless for five-class training, but **potentially useful for ★4** (the farm-over-time history) because it is a genuine longitudinal series. Keep as a reference, not a corpus. |
| **Zenodo 14628690** (`Saif-aljumaili`) | `dataset.zip`, 810.8 MB, CC BY 4.0 | No description, no class statement, no paper. Cannot be characterised from the metadata; would need to be opened to be used. Low priority. |
| **brainer-fp66/coffee-leaf-diseases** (HF) | 1,511 images, 5 labels incl. **Red Spider Mite 116** | Smaller than JMuBEN and duplicates its classes; the mite class is out-of-taxonomy. Useful only as a sanity-check set. |
| **Laksh619/Coffee-Cocoa-Diseases** (HF) | 4,000 = 8 classes × 500, **coffee + cocoa** | Half the classes are cocoa. Merging them would teach the model cocoa diseases. Reject as a corpus; note as an example of why "coffee leaf" search results must be inspected. |
| **minayahhh/liberica & robusta** (Kaggle) | 1.49 GB / 790 MB, **no description, licence "Unknown"** | Cannot characterise classes or provenance. Reject. |
| **johnandrewborabo/coffee-leaf-binary** | 3.1 GB, Healthy vs Unhealthy | Binary — collapses the taxonomy we are trying to build. Reject. |
| **CoLeaf** (`hyeiin/coleaf-dataset`) | 1,006 images, nutritional deficiency | Not a disease. Already rejected in the registry. |
| **Roboflow "Coffee leaf disease"** | 7,134, CC BY 4.0, no healthy class | Already rejected — no published methodology. |
| **Kaggle "Metadata-Enhanced Benchmark"** | 90,780, CC0 | Superset of everything ⇒ guaranteed leakage. Already rejected. |

---

## 4. The licence trap — this is a real finding, not a footnote

Every large mirror **relabels the licence**, and the relabelling is wrong:

| Dataset | Upstream (authoritative) | Kaggle / HF mirror says | Verdict |
|---|---|---|---|
| JMuBEN | **CC BY 4.0** (Mendeley) | "Unknown" (Kaggle) | Mirror label unusable |
| JMuBEN mirror | CC BY 4.0 | **CC BY 4.0** (HF `Project-AgML`) | ✅ correct |
| RoCoLe | **CC BY 4.0** (Mendeley) | **MIT** (Kaggle) · **CC BY-SA 4.0** (Kaggle) | Mirror label wrong |
| BRACOL | **CC BY 4.0** | CC BY 4.0 (YOLO mirror) | ✅ correct |
| Silva | **CC BY 4.0** | "Data files © Original Authors" | Vague |
| Uganda | **CC BY 4.0** (Mendeley) | **CC BY-NC-SA 4.0** and **CC BY-SA 4.0** on two mirrors | Mirror labels contradict each other |
| Ethiopian | **CC0** (uploader's claim only) | CC0 | Unverifiable — no institution |
| CoffeeLeaf-CO | **CC BY 4.0** (Zenodo) | — | ✅ |

**Rule for the report:** cite the **Mendeley DOI or the Zenodo DOI**, never the mirror, and state the
licence from the DOI record. If a reviewer asks "why does Kaggle say MIT?", the answer is in this table.

**One more trap:** the PeerJ cs-3386 paper cites BRACOL with the **RoCoLe DOI** (`c5yvn32dzg`).
Do not propagate it. BRACOL is `10.17632/yy2k5y8mxg.1`.

---

## 5. What this changes in the project

### 5.1 Corpus plan, revised

| Purpose | Datasets | Classes | Change from the old plan |
|---|---|---|---|
| **Training — headline** | JMuBEN + JMuBEN2 (58,549) | all 5 | unchanged |
| **Training — ablation B** | + Uganda augmented (26,335) | all 5, African field | **much stronger**: 26k African images, not 3k |
| **External — African** | Uganda Mendeley (3,322) · **Ethiopian test split (1,200)** | Rust, Phoma, Healthy, **Cercospora** | **Cercospora external recall is now possible** |
| **External — other** | RoCoLe (1,560) · Silva (542) · Saposoa (1,500) · CoffeeLeaf-CO (2,315) | Rust, Miner, Healthy | unchanged |
| **Ablation — severity** | dvelaren (4,398) | rust severity | optional, ★4 only |

### 5.2 The two claims we can now make that nobody else can

1. **"The published Uganda dataset is a 3,322-image augmented slice of a 12,480-image original."**
   We can show the arithmetic from the authors' own two releases.
2. **"The only Ethiopian coffee-leaf dataset we can find has 12,000 images, and its held-out test
   split is the only external Cercospora set we can verify and will not train on."**
   That sentence belongs in the proposal's data section and in the defense.

### 5.3 What to request from the authors (this week)

| Who | What | Why |
|---|---|---|
| Specioza Chelangat (Soroti Univ.) | The **12,480 un-augmented originals** | Triples the African external set and removes the augmentation confound |
| Biniyam Yoseph (Ethiopian Kaggle uploader) | **Provenance**: where were the images taken, who labelled them, is the CC0 claim correct? | Without it the Ethiopian set is usable but not citable as ground truth |
| Bayile Getu Taye (JMuBEN) | The **un-augmented originals** | Still open (R1) |

---

## 6. How the Colab notebook confirms this

`notebooks/00-dataset-verification.ipynb` does, in order:

1. **Probe** every URL and print HTTP status + `Content-Length` + `ETag`. No download if the probe fails.
2. **Download** the open archives (Mendeley needs a session cookie; the notebook documents the manual step).
3. **Count before preprocessing** — walk the extracted tree and count files per class, per split,
   per extension. **No resizing, no dedup, no cleaning.** This is the number the instructor asked for.
4. **Hash** every archive (SHA-256) and every image (first 64 KB) and write `dataset_counts.json`.
5. **Measure** image dimensions (min / median / max) with Pillow — this is how we catch the
   "HF mirror is downscaled to 128 px" problem.
6. **Optional:** perceptual-hash clustering to estimate the duplicate rate, which is the input to the
   leakage-safe split.
7. **Emit** a markdown table identical in shape to §1 of this file, so the report and the notebook
   cannot drift apart.

The notebook's output file, `data/verified/dataset_counts.json`, is the artefact SO1 points at.

---

## 7. What we still cannot verify, stated honestly

| # | Cannot verify | Why | Consequence |
|---|---|---|---|
| 1 | BRACOL's 1,747 + 2,147 | archive needs a Mendeley login; mirror is incomplete | quote as "published, not observed" until Colab |
| 2 | Saposoa's 1,500 | 3.45 GB RAR; needs `unrar` on Colab | quote as "published, not observed" |
| 3 | JMuBEN/JMuBEN2 zip internals | 1.84 GB total; counted via two mirrors instead | the 58,549 figure is T1 *by mirror agreement*, not by opening the zip |
| 4 | CoffeeLeaf-CO's 2,315 | zip not opened | T3 |
| 5 | The Ethiopian dataset's true provenance | self-uploaded, no paper | use, but state the limitation |
| 6 | Uganda's 12,480 originals | not uploaded | request from the authors |
| 7 | CerradoCoffeeLeaf's 1,476 | not released | cite as prior work only |

**The honest sentence for the report:** *"Counts marked observed were read from the publishers' file
manifests or from two independent mirrors; four archives could not be opened without an authenticated
download and are reported as published, not observed. The Colab notebook reproduces every observed
count and is the artefact of record."*

---

## 8. The grounded truth, in one page

If the group reads nothing else, this is what is actually true on 7 November 2026:

1. **The five-class training corpus is 58,549 images, not 58,555.** Two independent mirrors agree.
2. **JMuBEN is pre-augmented** and the originals were never published. Any random split leaks. This is
   now corroborated by an independent 2026 paper (CerradoCoffeeLeaf) that says the same thing.
3. **BRACOL's 2,147 "images" are crops of its 1,747 leaves.** Group them or leak.
4. **RoCoLe is 1,560 images from 390 plants** — four views each. Split by plant, not by image.
5. **Uganda is three releases, not one:** 12,480 original (not uploaded), 26,335 augmented (counted),
   3,322 on Mendeley (counted). The published 3,312 is wrong by ten.
6. **An Ethiopian dataset exists:** 12,000 images, four classes, 1,200-image clean test split, CC0,
   no paper. It is the only Cercospora set we can verify and hold out. (Two other sources mention
   Cercospora: BRACOL is a planned training source, so it cannot be external; `Laksh619/Coffee-Cocoa-
   Diseases` has 500 `coffee_browneye` images but is an unverified coffee+cocoa aggregation.)
7. **Saposoa's third class is *Mycena citricolor*, not Cercospora.** Mapping it would corrupt the labels.
8. **Every Kaggle mirror relabels the licence, and most get it wrong.** Cite the DOI, not the mirror.
9. **Four archives cannot be counted without an authenticated download.** The Colab notebook opens them.
10. **Nobody else has done this count.** That is the point: the contribution starts before the model.

---

## 9. Reproduction

Every number in §1 and §2 was obtained from one of these endpoints. Anyone can re-run them.

```text
Mendeley dataset metadata   GET https://data.mendeley.com/public-api/datasets/{id}
Mendeley file manifest      GET https://data.mendeley.com/public-api/datasets/{id}/files?folder_id=root&version={v}
Zenodo record               GET https://zenodo.org/api/records/{id}
Kaggle metadata             GET https://www.kaggle.com/api/v1/datasets/view/{owner}/{slug}
Kaggle file manifest        GET https://www.kaggle.com/api/v1/datasets/list/{owner}/{slug}?pageSize=200[&pageToken=…]
Hugging Face dataset list   GET https://huggingface.co/api/datasets?search=coffee&limit=100
Hugging Face file tree      GET https://huggingface.co/api/datasets/{id}/tree/main?recursive=true
Hugging Face row statistics GET https://datasets-server.huggingface.co/statistics?dataset={id}&config=default&split=train
GitHub repository tree      GET https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1
```

Record IDs used:

```text
JMuBEN          Mendeley t2r6rszp5c v1
JMuBEN2         Mendeley tgv3zb82nd v1
BRACOL          Mendeley yy2k5y8mxg v1
RoCoLe          Mendeley c5yvn32dzg v2
Uganda          Mendeley k36wnd6knb v1
Saposoa         Mendeley mfpxg4y65r v2
Silva           Mendeley vfxf4trtcg v5
CoffeeLeaf-CO   Zenodo 22756170
Zenodo extra    Zenodo 14628690
Ethiopian       Kaggle biniyamyoseph/ethiopian-coffee-leaf-disease
Uganda orig.    Kaggle chelangatspecioza/coffeedataset34 (and …45)
JMuBEN mirror   Kaggle noamaanabdulazeem/jmuben-coffee-dataset · HF Project-AgML/arabica_coffee_leaf_disease_classification
RoCoLe mirror   Kaggle nirmalsankalana/rocole-a-robusta-coffee-leaf-images-dataset
Silva mirror    Kaggle alvarole/coffee-leaves-disease
```
