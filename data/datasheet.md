# Dataset Datasheet

> **Guideline §9.2:** *"Document the source, size, variables or features, target, collection
> method, licensing and permissions, preprocessing, and ethical considerations. For labeled
> data, also describe how labels were produced, who produced them, and how agreement between
> annotators was measured. Report the class distribution and describe how the train, validation
> and test sets were created."*
> **§9.6:** *"Document the intended use, the known limits and the data used in a short model
> description (model card) and a data description (datasheet)."*
>
> **Owner:** Hayredin Mohammed · **Reviewer:** Nahom Solomon
> **Status:** ☐ Template — ☐ Filled with observed counts — ☐ Final (FYP II week 25)
>
> ⚠️ **Every field marked `[OBSERVE]` must be replaced with the value Hayredin actually
> observes after downloading.** Do not copy the published figures into those fields. If the
> observed value differs from the published one, record both and explain the difference.

---

## 1. Motivation

The corpus exists to train and evaluate a five-class coffee leaf disease classifier that runs
offline on a low-cost phone, and — equally importantly — to produce an **honest measurement of
how such a classifier performs on field photographs** rather than on curated imagery. The
second purpose drives the source selection: the corpus deliberately spans six countries, two
*Coffea* species, and both laboratory-curated and field-collected capture conditions, so that
the internal-to-external shift can be measured rather than assumed.

## 2. Composition

### 2.1 Sources

| # | Source | Country | Species | Capture environment | Classes contributed | Images (published) | **Images observed (7 Nov 2026)** | Tier |
|---|---|---|---|---|---|---|---|---|
| S1 | JMuBEN (`t2r6rszp5c`) | Kenya | Arabica | Field plantation, both leaf surfaces, varied weather; cropped and augmented by the publishers | Rust, Cercospora, Phoma | 22,591 | **22,588 files → 2,055 distinct** | **T1** |
| S2 | JMuBEN2 (`tgv3zb82nd`) | Kenya | Arabica | Same campaign | Miner, Healthy | 35,964 | **35,962 files → 1,702 distinct** | **T1** |
| S1+2 | **JMuBEN combined** | Kenya | Arabica | — | All 5 | **58,555** (paper) | **58,550 files → 3,757 distinct** | **T1** |
| S3 | BRACOL (`yy2k5y8mxg`) | Brazil | Arabica | Field, abaxial side, white background, 5 smartphones | All 5 | 1,747 leaves + 2,147 crops | **1,747 files → 1,746 distinct** (Mendeley file truncated; 345 restored from HF mirror) | **T1** |
| S4 | Uganda (`k36wnd6knb`) | Uganda | Arabica | Real farms, smartphone, daylight and low light; **already augmented** | Rust, Phoma, Healthy | 3,312 | **3,322 files → 1,810 distinct, 102 zero-byte** | **T1** |
| S5 | Saposoa Peru (`mfpxg4y65r`) | Peru | Arabica | Uniform protocol, fixed distance, homogeneous light, specialist diagnosis | Rust, Healthy (+ *Mycena*) | 1,500 | 1 RAR, 3.45 GB — **not verified** | T3 |
| S6 | RoCoLE (`c5yvn32dzg` v2) | Ecuador | **Robusta** | Field, natural backgrounds, smartphone at 200–300 mm | Rust, Healthy (+ red spider mite) | 1,560 | **1,560 files → 1,493 distinct** | **T1** |
| S7 | CoffeeLeaf-CO v2 (`22756170`) | Colombia | Arabica | Field collection, consumer Android phones, natural light | Rust, Miner (+ weevil); healthy as background | 2,315 | 1 zip, 167.5 MB — **not verified** | T3 |
| S8 | Silva 2020 (`vfxf4trtcg` v5) | Brazil | Arabica | Mostly lab on white background, original 4000×2250 | Rust, Miner | 542 | **542** (285 rust + 257 miner) | **T2**¹ |
| **S9** | **Ethiopian** (Kaggle `biniyamyoseph/…`) | **Ethiopia** | Arabica | Field photographs; `train aug/` augmented, `test/` curated | **Cercospora**, Rust, Phoma, Healthy | — | **12,000** = 10,800 train-aug + 1,200 test | **T2** |
| **S10** | Uganda augmented (Kaggle `chelangatspecioza/…34`) | Uganda | Arabica | Same farms as S4, augmented | Rust, Phoma, Healthy | 26,315 | **26,335** (9,045 / 8,330 / 8,960) | **T2** |
| | **Total (distinct, file-verified sets)** | **7 countries** | **2 species** | | | | **≈ 9,350 distinct** + Ethiopian 12,000 files (not deduplicated) | |

¹ Silva's count is confirmed by the author's own Kaggle upload — a second release, not an independent
one.

**Tier definitions** (full explanation in `docs/12-DATASET-VERIFICATION.md` §0): **T1** verified
against two independent releases; **T2** verified from one publisher file manifest; **T3** published
figure, archive not opened; **T4** claimed only.

**Why there is no single "total".** Two numbers matter and they are not the same:
**files** (what the publishers count) and **distinct images** (what a model can learn from).
JMuBEN + JMuBEN2 is 58,550 files but **3,757 distinct images**; 93.6 % of the files are
byte-identical copies. Uganda is 3,322 files and 1,810 distinct. Any corpus total that adds file
counts is inflated by roughly the duplication rate of each source, so the datasheet reports
**distinct** counts wherever they have been measured and leaves the rest at their file count with a
tier label. The audit is `docs/14-DUPLICATION-AUDIT.md`; the raw output is
`data/audit/duplication-report.md`.

### 2.2 Class distribution

The per-class counts for JMuBEN and JMuBEN2 combined were **observed** on 7 November 2026 and agree
across two independent mirrors (Kaggle `noamaanabdulazeem/jmuben-coffee-dataset` and HF
`Project-AgML/arabica_coffee_leaf_disease_classification`). The paper's Table 1 is six images larger.
On **8 November 2026** the archives were opened and every file was hashed. The file count and the
distinct-image count are both shown, because they differ by a factor of fifteen.

| Class | Cercospora | Healthy | Leaf Rust | Leaf Miner | Phoma | **Total** |
|---|---|---|---|---|---|---|
| Paper Table 1 | 7,682 | 18,985 | 8,337 | 16,979 | 6,572 | 58,555 |
| **Observed files (T1)** | **7,681** | **18,984** | **8,336** | **16,978** | **6,571** | **58,550** |
| **Distinct images** | **322** | **63** | **1,042** | **1,639** | **691** | **3,757** |
| Duplicate share | 95.8 % | 99.7 % | 87.5 % | 90.3 % | 89.5 % | **93.6 %** |

The **Healthy class is the crisis**: 18,984 files resolve to 63 distinct images, and visually those
63 are frames of a single leaf (`data/figures/jmuben-healthy-63.png`). A model evaluated on a random
split of this class is measured on memorisation. The report states the distinct count, and the
healthy training signal must come from BRACOL, Uganda and RoCoLe, not from JMuBEN.

The Ethiopian external set (S9) is perfectly balanced by construction:
**3,000 Cercospora / 3,000 Healthy / 3,000 Rust / 3,000 Phoma** across its train-augmented and test
splits, of which the **clean test split is 300 per class (1,200 total)**.

**The corpus is imbalanced — and the effective imbalance is worse than the file counts suggest.**
On distinct images the five classes are 322 / 63 / 1,042 / 1,639 / 691, i.e. Miner is **26× larger
than Healthy**. Consequences the group must handle and report:
- a **majority-class baseline** (always Miner) scores ≈ 44 % on the distinct-image corpus and is the
  floor that any model must beat by a wide margin (§9.1 of the proposal);
- **macro-averaged metrics** are the primary reported metric, not accuracy, because accuracy
  is inflated by the two dominant classes;
- the two minority classes are the ones most likely to be missed on field photographs — which
  is exactly what the published model card for EfficientNet-B2 shows for Cercospora (9.1 %
  recall on a ConvNeXt model, 0.717 F1 on the EfficientNet-B2) — so **per-class recall is
  reported for every class on every dataset**, not just the averages;
- **Healthy cannot be learned from JMuBEN.** 62 usable distinct healthy images is below the
  threshold at which a 5-class model can generalise; healthy must be sourced from BRACOL (1,747
  leaves, all five classes), Uganda (739 distinct) and RoCoLe (759). This is a corpus-design
  decision, not a footnote.

[OBSERVE] the observed distribution after the union with BRACOL, and record the change.

### 2.3 Out-of-taxonomy classes

Three conditions appear in the sources but are **not** in the five-class target taxonomy. They
are retained under a separate `unsupported` label and are **never** mapped onto a disease
class (requirement DR-08, test T-16):

| Condition | Source | Pathogen / agent | Why it is not one of the five |
|---|---|---|---|
| Red spider mite | RoCoLE | *Oligonychus coffeae* | An arthropod pest, not a fungal or bacterial disease |
| Coffee weevil ("coco") | CoffeeLeaf-CO | Curculionidae (*Compsus*, *Epicaerus* sp.) | Insect defoliation, not a leaf disease |
| *Mycena citricolor* ("ojo de gallo") | Saposoa Peru | *Mycena citricola* | A different fungal genus; superficially resembles Cercospora but is taxonomically distinct |

**This is the single most important taxonomy decision in the project.** Folding *Mycena* into
Cercospora or red spider mite into leaf miner would silently corrupt both the training labels
and the external evaluation, and would produce a flattering but false result.

## 3. Collection process

### 3.1 How the labels were produced

| Source | Labelling method | Who labelled | Annotator agreement |
|---|---|---|---|
| JMuBEN / JMuBEN2 | Manual annotation with a data-labelling web tool, on the basis of a plant pathologist's field diagnosis during a tour of the plantation | **A plant pathologist** (acknowledged in the paper: Dr. Felix Rotich) | Not reported in the source; the single-expert design is stated here as a limitation |
| BRACOL | Expert labelling of the collected material | A domain expert, with severity computed from segmentation masks | Not reported in the source |
| Uganda 2025 | Manual labelling after duplicate removal | The dataset's authors (Soroti University) | Not reported in the source |
| Saposoa Peru | Diagnosis by plant-health specialists under a uniform protocol | Specialists | Not reported in the source |
| RoCoLE | Labelbox web tool — segmentation and classification | The dataset's authors, with rust severity by the OIRSA/LANREF method | Not reported in the source |
| CoffeeLeaf-CO v2 | **VIA + SAM**, with expert review | The dataset's authors | **Cohen's κ = 0.91** — the only source reporting agreement |
| Silva 2020 | Manual labelling on a Brazilian farm | The dataset's authors | Not reported in the source |

**Honest limitation:** six of the eight sources report no annotator-agreement statistic, and
the strongest source uses a **single expert** rather than multiple raters. This means the
ground-truth labels themselves carry unquantified uncertainty, which is an additional reason
the group reports per-class metrics and an error analysis rather than a single headline
number. It is also a limitation of the *labels*, not only of the *model*.

### 3.2 The publishers' preprocessing — and why it matters

| Source | Publisher preprocessing | Consequence for the group |
|---|---|---|
| JMuBEN / JMuBEN2 | Noise filtering and contrast stretching; centre-square crop of non-square images; resize to a uniform shape; **rotation (180° both axes, counter-clockwise) and horizontal/vertical flipping applied as augmentation to the smaller images** | The released images are **augmented and cropped derivatives** of a smaller original set, and **the originals are not published**. A random split leaks near-duplicates. The group must cluster by perceptual hash and group before splitting. |
| BRACOL | Symptom images cropped from the whole-leaf images | The crops and their parent leaf must be in the same partition. |
| RoCoLE | Four views per plant | Split by plant ID (`C##P##`), never by image. |
| Uganda 2025 | Duplicates removed; rotation, flipping and brightness augmentation applied | The "duplicates removed" claim must be verified independently. |
| Saposoa Peru | Fixed distance, homogeneous light; blurred and occluded images excluded | A low-noise source — arguably *too* clean, which makes it a useful but not representative test. |
| CoffeeLeaf-CO v2 | SHA256-clean split, verified; 454 RoCoLe images deliberately removed | The only source with a verified, reproducible split. |
| RoCoLE (Kaggle mirror) | Resized, sorted into class folders, **annotations excluded** | Use the Mendeley record, not the mirror. |

### 3.3 The group's own preprocessing

Applied **only after** the split, and only to the training partition:

1. Resize to 224×224 (bicubic), preserving aspect ratio with a centred crop.
2. Convert to RGB.
3. Scale to [0, 1]; the int8 quantisation uses the standard TFLite input/output scale and
   zero-point.
4. **Training-time augmentation** (train partition only): random rotation ±20°, random
   horizontal flip, random brightness/contrast jitter within ±20 %, random Gaussian blur
   with σ ≤ 1.0 at p = 0.2, and random resized crop at scale 0.8–1.0.
5. **Ablation variants** additionally add: random JPEG compression (quality 60–100),
   RandomGrayscale (p = 0.1), and a simulated low-light exposure (p = 0.2).

The augmentation recipe is chosen to mirror the failure modes documented for plant-disease
models in the field — background clutter, uncontrolled illumination, blur, and low resolution
— rather than to maximise in-domain accuracy.

## 4. Preprocessing, splits and their rationale

### 4.1 The split procedure

```
raw images
   │
   ├─ 1. assign a source id and a group id
   │     JMuBEN    → group = perceptual-hash cluster        (the originals are not published)
   │     BRACOL    → group = parent leaf id                 (a crop shares its leaf's group)
   │     RoCoLE    → group = plant id  (C##P##)
   │     others    → group = source id + filename stem
   │
   ├─ 2. cluster by perceptual hash within each source
   │     pHash (DCT-based, 64-bit), agglomerative with a Hamming distance ≤ 6
   │     → near-duplicate clusters become one group
   │
   ├─ 3. stratified grouped split
   │     groups assigned to train / validation / test with a fixed seed (42)
   │     stratified by class, so that the per-class proportions are preserved
   │     target: 70 % train / 15 % validation / 15 % test
   │
   ├─ 4. assert the invariants (tests T-03, T-04, T-05, T-06)
   │     no hash in two partitions
   │     no pHash cluster in two partitions
   │     no group id in two partitions
   │     the partition sizes sum to the corpus size
   │     the split is stratified: for each class, the number of groups in each
   │     partition is within one group of the target ratio
   │
   └─ 5. emit data/split_manifest.csv with: image_path, sha256, phash, source, group_id,
        class, split, and the seed
```

**The split is performed before any learned preprocessing**, as Guideline §9.3 requires. There
is no normalisation statistic, no augmentation and no preprocessing parameter that is fitted on
the data, because the preprocessing is entirely deterministic and label-free.

### 4.2 The split as it will be reported

| Split | Images [OBSERVE] | % | Cercospora | Healthy | Rust | Miner | Phoma |
|---|---|---|---|---|---|---|---|
| Train | | ~70 % | | | | | |
| Validation | | ~15 % | | | | | |
| Test | | ~15 % | | | | | |
| **Total** | | 100 % | | | | | |

The stratification is asserted at the **group** level rather than the image level, because
groups are the unit the split actually allocates: a perceptual-hash cluster may hold eight
images and its neighbour two, so the image-level proportion is not what the stratification
controls. The audit asserts that, for each class, the number of groups in each partition is
within one group of the target ratio, and it prints the image-level distribution for
information.

### 4.3 The external evaluation sets

These are **never** used for training in the headline model, and their exclusion is asserted
by test T-05 and by a CI check:

| Set | Role | Why it is a genuine shift |
|---|---|---|
| Uganda 2025 (3,322) | External test (and, in ablation variant B, a training source) | Different country, real farms, smartphone, uncontrolled light |
| **Ethiopian `test/` (1,200)** | **External test — the only Cercospora set we can verify and hold out** | **Same country as the target user**, different farms, curated 300-per-class test split |
| RoCoLE (1,560) | External test | Different **species** (Robusta), different country, natural backgrounds, a 390-plant grouping structure |
| Saposoa Peru (1,500) | External test | Uniform, specialist-labelled protocol — a "clean" shift that probes a different failure mode |
| CoffeeLeaf-CO v2 (2,315) | External test | Different country, detection-annotated field imagery with a verified split |
| Silva 2020 (542) | External test | Original 4000×2250 resolution — tests the pipeline on realistic file sizes and detail |

**The Ethiopian set's provenance caveat travels with every number computed on it:** it is a
self-uploaded Kaggle dataset (CC0) with no paper, no named annotator and no methodology statement.
Its balanced `test/` split is evidence of curation, not of a random field sample, so its accuracy is
an **upper bound**. It is used because it is the only way to report Cercospora recall outside Kenya,
and the caveat is printed beside the result.

### 4.4 A note on what the external sets can and cannot test

| Class | Uganda | **Ethiopian** | RoCoLE | Saposoa | CoffeeLeaf-CO | Silva |
|---|---|---|---|---|---|---|
| Rust | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Healthy | ✔ | ✔ | ✔ | ✔ | (background) | — |
| Phoma | ✔ | ✔ | — | — | — | — |
| Leaf Miner | — | — | — | — | ✔ | ✔ |
| **Cercospora** | — | **✔ (300)** | — | — | — | — |
| *unsupported* | — | — | red spider mite | *Mycena* | weevil | — |

**Cercospora now has one usable external test: the 300-image Ethiopian `test/` split.** Before
7 November 2026 the registry said no public field corpus contained it; that is no longer true. BRACOL
contains Cercospora but is a planned training source, so it cannot serve as external; the HF set
`Laksh619/Coffee-Cocoa-Diseases` has 500 `coffee_browneye` images but is an unverified coffee+cocoa
aggregation and is not used. The evaluation
must still state that (a) the set has no published provenance and (b) 300 images give a 95 % binomial
confidence interval of roughly ±5.7 points on a recall near 90 % — so it is a benchmark, not a
verdict. Phoma is now tested by two sets (Uganda and Ethiopian), which is a real improvement over one.

## 5. Licensing, permissions and ethics

| Source | Licence | Attribution required | Redistribution in the repo |
|---|---|---|---|
| JMuBEN, JMuBEN2 | CC BY 4.0 | Yes — Jepkoech *et al.*, *Data in Brief*, 36:107142 | **No** — the download URL and the split manifest only |
| BRACOL | CC BY 4.0 | Yes — Krohling, Esgario & Ventura | No |
| RoCoLE | CC BY 4.0 | Yes — Parraga-Alava *et al.* | No |
| Uganda 2025 | CC BY 4.0 | Yes — chelangat *et al.* | No |
| Saposoa Peru | CC BY 4.0 | Yes — Santa Maria Pinedo | No |
| CoffeeLeaf-CO v2 | CC BY 4.0 | Yes — Rosas Ruiz *et al.* | No |
| Silva 2020 | CC BY 4.0 | Yes — Silva *et al.* | No |

- All use is **non-commercial academic research**. All are used under CC BY 4.0, which permits
  it with attribution.
- **The dataset itself is never redistributed** by this project — only the download
  instructions, the split manifest (paths, hashes and labels, no image content) and the
  preparation script are published (NFR-32).
- **No personal data.** The images are of leaves; no person is identifiable in any of them.
  No face, no house, no vehicle. The group confirms this for every source it uses.
- **Third-party platform terms** were respected: no scraping, no paywalled content, no
  login-gated downloads beyond a free account where the platform requires one.
- **Ethical screening** is recorded in `docs/appendices/Appendix-M-Ethics.md`; question 6
  ("does it collect data from websites or third-party platforms") is answered **Yes** with the
  safeguards listed there.

## 6. Known limitations of the dataset

1. **Geographic imbalance.** Kenya (JMuBEN) and Brazil (BRACOL) dominate. Only 3,312 images come
   from an African dataset beyond Kenya. **No Ethiopian field imagery is included** — the
   dataset that matters most for the target population does not exist publicly, which is the
   single largest limitation of the corpus and the project.
2. **Pre-augmented training data.** JMuBEN's augmentation cannot be undone, so the group
   cannot recover the original field photographs, and cannot measure the effect of the
   publishers' augmentation separately from its own.
3. **Single-expert labels.** Six of eight sources report no annotator agreement, and JMuBEN's
   labels come from one pathologist. Label noise is unquantified.
4. **Two classes are untestable in the field.** No public field corpus contains Cercospora or
   Phoma beyond Uganda's Phoma. Field performance for Cercospora is essentially unknown.
5. **Taxonomic heterogeneity.** The sources use different common names for what may be related
   conditions; the five-class taxonomy is the JMuBEN taxonomy and it does not cover
   *Mycena*, weevil or red spider mite.
6. **Species mismatch.** Only RoCoLE is Robusta. A model trained on Arabica and tested on
   Robusta measures a harder shift than the deployment target, which is Arabica.
7. **Background and scale.** BRACOL and Saposoa place leaves on white backgrounds; JMuBEN
   crops to the region of interest. A model trained on these may be poorly calibrated for a
   leaf photographed in a bush. CoffeeLeaf-CO v2, with genuine field backgrounds, is the only
   source that addresses this, and it covers just two classes.
8. **Class imbalance.** Healthy and Miner are 61 % of the corpus; the minority classes are
   where the field failure will occur.
9. **The published counts disagree.** JMuBEN's total is 58,555 in the paper and 58,549 in the
   machine-readable mirror; BRACOL's symptom count is 2,147 in the Mendeley record and 2,722 in
   the Omdena mirror. The group records what it observes and states which figure it used.

## 7. Intended use

**Intended.** Training and evaluating a five-class coffee leaf disease classifier for
deployment on low-cost Android phones in coffee-growing regions, with an explicit abstention
mechanism and sourced agronomic guidance.

**Out of scope — the system must not be used for:** certifying a plant for export or
certification; automated fungicide application without human review; any commercial grading
decision; diagnosing coffee cherry, root, stem or soil problems; determining the presence of a
pest species not in the taxonomy; or any purpose requiring regulatory-grade accuracy.

**Out-of-scope inputs.** Non-leaf images, images of coffee cherry or stem, microscopic images,
and images of other crops. The system is expected to reject or mis-handle these, and the
report says so.

## 8. Maintenance

| Item | Owner | Frequency |
|---|---|---|
| The observed counts and the checksums in §2.1 | Hayredin | Once, at the first download; re-verified if a source is re-downloaded |
| The split manifest | Hayredin | Regenerated only when the corpus changes, and then the seed is bumped and the change is logged |
| The licence check | Nahom | At the start of each semester |
| The taxonomy mapping (`unsupported` handling) | Hayredin + Nahom | Whenever a new source is added |

## 9. Citation of this datasheet

If this datasheet or the corpus it describes is used in any publication, the original dataset
papers must be cited (the IEEE list is `docs/literature/references.md`, §A), and the split
protocol must be cited as this group's own work, with the repository URL and the version of
the split manifest.
