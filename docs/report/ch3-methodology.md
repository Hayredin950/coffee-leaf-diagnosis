# Chapter 3 — Methodology

> **Owner:** Nahom Solomon (methodology, planning, risk) with Hayredin Mohammed (the
> experimental protocol) · **Estimated length:** 3–4 pages
>
> **Cross-reference:** the full literature review is `docs/literature/ch2-literature-review.md`;
> the design detail is `docs/design/architecture.md`; the requirements are
> `docs/requirements/requirements-spec.md`.

---

## 3.1 Development and research method

An **iterative, prototype-driven** method was adopted, with an **experimental** protocol
nested inside the model work.

The choice is driven by three genuine uncertainties, each of which must be de-risked before
the next component can be built on it:

1. Whether a leakage-safe split materially changes the accuracy picture. If it does, every
   number in the literature becomes suspect and the project's premise changes.
2. Whether a model under 10 MB can retain acceptable external accuracy. If it cannot, the
   offline requirement (the core of the project) is unaffordable.
3. Whether Flutter with on-device TFLite inference can be made reliable on low-end Android
   hardware. If it cannot, the entire delivery vehicle changes.

Each uncertainty was converted into a prototype that was built, measured and reviewed before
the next component was built on top of it. Concretely: a placeholder model was running in the
app before any feature code was written; the real model was exported and measured before the
API was implemented; and the API was deployed and contract-tested before the web client was
written.

Within the model work specifically, an experimental method was used, with the following
controls, all of which are reproducible:

- **Data.** The split manifest is committed with a SHA-256 checksum of every image. The split
  is produced by a single script, `scripts/prepare_data.py`, from a fixed seed.
- **Randomness.** Every run records its seed; the environment is pinned in `environment.yml`
  and `requirements.lock`.
- **Repetition.** Every configuration is trained with at least three seeds. Results are
  reported as the mean and the standard deviation across seeds, never as a single run.
- **Test-set discipline.** The internal test partition is used once per configuration and is
  never used to tune a hyperparameter. Model selection uses the validation partition. The
  external sets are used only for final evaluation.
- **Statistical testing.** Where the report claims one method is better than another, a
  McNemar test on paired predictions is reported with the p-value (§6.6).
- **Reproducibility.** A table maps every reported number to the script that produced it
  (`results.md`), as Guideline §9.7 requires.

### 3.1.1 Figure 3.1 — the methodology as a sequence of gated prototypes

> **Figure 3.1** — The prototype-driven method: each box is a prototype whose measurement
> determines whether the next box is built. A failed measurement changes the plan rather than
> being carried forward. Original work by the group.

---

## 3.2 Data

The corpus and the split protocol are documented in full in the **datasheet** (Appendix —
`data/datasheet.md`) and the **dataset registry** (`data/dataset-sources.md`). This section
summarises the methodological decisions that the datasheet records in detail.

### 3.2.1 Source selection

Nine corpora were selected, spanning six countries, two *Coffea* species, and both
laboratory-curated and field-collected capture conditions.

**Table 3.1** — The training corpus. The per-class counts are those published by the sources;
the observed counts are recorded in the datasheet after download.

| Source | Country | Species | Environment | Classes | Published images | Observed |
|---|---|---|---|---|---|---|
| JMuBEN | Kenya | Arabica | Plantation, both leaf surfaces, varied weather | Rust, Cercospora, Phoma | 22,591 | — |
| JMuBEN2 | Kenya | Arabica | Same campaign | Miner, Healthy | 35,964 | — |
| **JMuBEN + JMuBEN2** | Kenya | Arabica | — | All 5 | 58,555 | **58,549** (two mirrors agree) |
| BRACOL | Brazil | Arabica | Field, abaxial side, white background, 5 phones | All 5 | 1,747 leaves + 2,147 crops | — |
| Uganda 2025 | Uganda | Arabica | Real farms, smartphone, varied light; already augmented | Rust, Phoma, Healthy | 3,312 | **3,322** |
| Uganda augmented (Kaggle) | Uganda | Arabica | Same farms, augmented | Rust, Phoma, Healthy | 26,315 | **26,335** |

The observed counts are the ones the report quotes; the published figures are shown beside them so
that the six-image JMuBEN discrepancy and the ten-image Uganda discrepancy are visible rather than
silent. The full evidence table is `docs/12-DATASET-VERIFICATION.md`.

**Table 3.2** — The external evaluation sets. These are excluded from training in the
headline model; the exclusion is asserted by test T-05 and by a CI check.

| Source | Country | Species | Environment | Classes tested | n |
|---|---|---|---|---|---|
| Uganda 2025 | Uganda | Arabica | Real farms | Rust, Phoma, Healthy | 3,322 |
| **Ethiopian (Kaggle)** | **Ethiopia** | Arabica | Field; curated `test/` split | **Cercospora**, Rust, Phoma, Healthy | **1,200** |
| RoCoLE | Ecuador | **Robusta** | Field, natural backgrounds | Rust, Healthy (+ red spider mite as `unsupported`) | 1,560 |
| Saposoa Peru | Peru | Arabica | Uniform protocol, specialist diagnosis | Rust, Healthy (+ *Mycena* as `unsupported`) | 1,500 |
| CoffeeLeaf-CO v2 | Colombia | Arabica | Field, consumer phones | Rust, Leaf Miner (+ weevil as `unsupported`) | 2,315 |
| Silva 2020 | Brazil | Arabica | Lab, full resolution 4000×2250 | Rust, Leaf Miner | 542 |

**The Ethiopian set is the only external Cercospora benchmark in public.** It is used with a stated
provenance caveat: it is a self-uploaded CC0 Kaggle record with no paper and no named annotator, and
its balanced `test/` split reflects curation rather than random field sampling, so its accuracy is an
upper bound.

### 3.2.2 The leakage-safe split

This is the methodological core of SO1, and it is described in full in §4.1 of the datasheet.
In summary, each image is assigned a **group** before the split:

| Source | Grouping rule | Why |
|---|---|---|
| JMuBEN, JMuBEN2 | Perceptual-hash near-duplicate cluster (64-bit pHash, Hamming ≤ 6) | The published images are cropped, resized and rotation/flip-augmented derivatives of a smaller original set, and the originals are unpublished |
| BRACOL | The parent leaf identifier, recovered from the crop filename | The symptom images are crops of the 1,747 whole-leaf photographs |
| RoCoLE | The plant identifier parsed from the `C##P##` filename | Four views of each of 390 plants exist |
| Uganda 2025 | pHash cluster | The publisher applied augmentation and states that duplicates were removed; that claim is verified independently |
| Saposoa, CoffeeLeaf-CO, Silva | Source + filename stem | Each image is an independent photograph; CoffeeLeaf-CO additionally publishes a SHA256-verified split |

Groups are then assigned to train / validation / test (70 / 15 / 15) with a stratified,
seeded procedure, and four invariants are asserted by an automated audit:

- **T-03** — no SHA-256 hash appears in more than one partition;
- **T-04** — no pHash cluster appears in more than one partition;
- **T-05** — no group identifier appears in more than one partition, and no external-only
  source appears in the training partition;
- **T-06** — the partition sizes sum to the corpus size, and the split is stratified: for each
  class, the number of groups in each partition is within one group of the target ratio.

**Why this matters.** A random split of these corpora places images that are rotations, flips
or crops of the same physical leaf on both sides of the partition. The published accuracies of
93–99 % on JMuBEN [7]–[10] are therefore upper bounds on field performance rather than
estimates of it, and the group treats them as such.

### 3.2.3 Label taxonomy

Five target classes are supported. Three conditions present in the sources — red spider mite,
coffee weevil damage and *Mycena citricolor* — are **not** in the taxonomy and are retained
under an explicit `unsupported` label. They are never mapped onto a disease class
(requirement DR-08, test T-16). This is the single most important label decision in the
project: *Mycena citricolor* ("ojo de gallo") resembles Cercospora superficially but is a
different fungal genus, and red spider mite is an arthropod pest rather than the leaf miner
damage it can be mistaken for at low resolution. Mapping either onto a target class would
corrupt both the training labels and the external evaluation, and would produce a flattering
but false result.

### 3.2.4 Preprocessing

Preprocessing is deterministic and label-free, and is applied **after** the split. The
training-time augmentation was chosen to mirror the failure modes documented for
plant-disease models in the field — background clutter, uncontrolled illumination, blur and
low resolution [16] — rather than to maximise in-domain accuracy: random rotation ±20°, random
horizontal flip, brightness/contrast jitter within ±20 %, Gaussian blur with σ ≤ 1.0 at
p = 0.2, and random resized crop at scale 0.8–1.0. An ablation variant adds random JPEG
compression, random grayscale at p = 0.1 and a simulated low-light exposure at p = 0.2.

A **golden-image test** compares the Python and Dart implementations of the inference
preprocessing element by element, so the app cannot silently diverge from the training
pipeline.

---

## 3.3 Models and evaluation

### 3.3.1 Baseline selection (Guideline §9.1)

Three baselines are reported, all evaluated under conditions identical to the proposed model:

1. **Majority-class predictor.** Predicting the most frequent class always. This establishes
   the floor and quantifies the class imbalance (Healthy is 32 % of the corpus).
2. **Transfer-learning MobileNetV3-Small.** The practical lightweight reference.
3. **Two published external models.** The ConvNeXt-S coffee model and the EfficientNet-B2
   TFLite model are run on the group's own splits, so that the group's numbers are directly
   comparable with the published field rather than with a differently-protocolled number.

**Why machine learning rather than a rule-based classifier (§9.1).** A rule-based classifier
would require hand-crafted thresholds over lesion colour, size, count, position and shape
simultaneously. Because the diagnostic signal is the *pattern* of lesions across the leaf
rather than any single measurable feature, and because the four target diseases overlap in
colour and morphology, a rule system would encode one expert's hand-crafted decisions and
would not generalise to the lighting, background and cultivar variation present in field
imagery. Learning the feature combination from data is the appropriate approach — provided
that the evaluation measures field performance honestly, which is what Chapter 6 does.

### 3.3.2 Architectures

Three architectures are compared, all TFLite-supported and all designed for phone CPUs
[22], [40]:

| Architecture | Why included |
|---|---|
| MobileNetV3-Small | Hardware-aware architecture search targeted at phone CPUs [22]; the lightest option |
| EfficientNet-Lite0 | The mobile-optimised EfficientNet variant, supported directly by the TFLite Model Maker [40] |
| MobileNetV2 | A strong, widely reproduced reference that isolates the effect of the MobileNetV3 improvements [37] |

### 3.3.3 Evaluation protocol

| Protocol element | Choice |
|---|---|
| Primary metric | Macro-F1 — chosen because accuracy is inflated by the two dominant classes |
| Secondary metrics | Per-class precision, recall and F1; the confusion matrix; the top-1 accuracy |
| Calibration | Temperature scaling fitted on the validation partition; ECE and NLL before and after |
| Decision rule | An acceptance threshold on the calibrated top-1 probability. Below the threshold the system does not present a diagnosis |
| External reporting | Per-class and per-dataset results, with bootstrap confidence intervals |
| Significance | McNemar's test on paired predictions for the decisive model comparison |
| Error analysis | Representative failures examined individually and discussed by cause |
| Reporting discipline | Every result is linked to the script that produced it; the test partition is never used for tuning |

---

## 3.4 Tools and environment

| Stage | Tool | Version | Note |
|---|---|---|---|
| Data preparation | Python, Pillow, ImageHash, pandas, scikit-learn | pinned in `requirements.lock` | `scripts/prepare_data.py` |
| Model training | TensorFlow / Keras | pinned | Kaggle notebook, NVIDIA Tesla P100 16 GB, free tier |
| Quantisation and export | TensorFlow Lite Model Maker / LiteRT converter | pinned | `model/export_tflite.py` |
| Evaluation | scikit-learn, SciPy, matplotlib | pinned | `training/evaluate_*.py` |
| Mobile client | Flutter / Dart | 3.x | `tflite_flutter`, `image_picker`, `camera`, `sqflite`, `drift` |
| API | Python, FastAPI, Pydantic v2, SQLAlchemy 2, Alembic, PostgreSQL | pinned | `api/` |
| Web client | HTML / CSS / JavaScript | — | No build step; the OpenAPI schema guarantees the contract |
| Version control and CI | Git, GitHub Actions | — | Lint, unit tests, container build, artefact check, KB audit, secret scan |
| Deployment | Docker | — | One container for the API; the web client is static |
| Documentation | Markdown, Mermaid, LaTeX/DOCX | — | Figures rendered to PNG for the report |

**Compute.** Training runs on free-tier Kaggle notebooks (Tesla P100 16 GB); the reference
architectures complete within approximately two hours per run, and the ablation (three
architectures × three seeds × two data regimes) is scheduled across weeks 8–13. Inference
measurement is performed on three physical Android devices representing low, mid and high
tiers.

---

## 3.5 Work plan

The full 32-week plan with the per-member allocation, the dependencies and the milestone
gates is in `docs/01-ROADMAP.md` and `docs/03-ROLES.md`. It follows the departmental timeline
of Guideline Table 16.1.

**Table 3.3** — The work plan against the guideline's gates.

| Phase | Weeks | Dates | Principal deliverable | Gate |
|---|---|---|---|---|
| Orientation and title selection | 1–2 | Oct 19 – Nov 1, 2026 | Proposal, ethics screening, repository, logbook | Advisor / Coordinator approval |
| Proposal | 3–4 | Nov 2 – Nov 15, 2026 | Final proposal, baseline results, proposal presentation | **Proposal approval** |
| Extended literature review and requirements | 5–7 | Nov 16 – Dec 6, 2026 | Literature review, comparison table, gap, FR/NFR specification | **Requirements baseline** |
| Design | 8–13 | Dec 7, 2026 – Jan 17, 2027 | Models, architecture, database, UI design, model prototype | Design review |
| FYP I defense | 14 | Jan 18 – Jan 24, 2027 | Chapters 1–4 and the presentation | Presentation and assessment |
| Implementation I | 15–18 | Jan 25 – Feb 21, 2027 | Core prototype | Progress review |
| Implementation II | 19–22 | Feb 22 – Mar 21, 2027 | Integrated system, web client, model v2 | Prototype review |
| Testing and evaluation | 23–24 | Mar 22 – Apr 4, 2027 | Test results, external evaluation, usability study | Evaluation review |
| Final report | 25–29 | Apr 5 – May 9, 2027 | Draft final report | Advisor approval |
| FYP II defense | 30 | May 10 – May 16, 2027 | Report, presentation, live demonstration | Final assessment |
| Corrections and submission | 31–32 | May 17 – May 30, 2027 | Corrected report and the submission package | Advisor verification |

**Figure 3.2** — The Gantt chart of the 32-week plan, by member, with the five gates marked.
Produced from `docs/03-ROLES.md` and rendered as a PNG for the report. Original work.

**The critical path** is dataset download → duplicate grouping → leakage-safe split → model
training → TFLite export → application integration. The integration step is protected by a
placeholder-model prototype that must exist in the application by the end of FYP I week 13,
so that integration is never the blocking step.

---

## 3.6 Risk management

A risk register is maintained in `docs/04-RISK-REGISTER.md` and reviewed with the advisor at
least monthly, as Guideline §6.3 requires. Twenty risks are recorded, with a probability, an
impact, a preventive mitigation, a named fallback, an owner and a review date.

**Table 3.4** — The five risks with the highest impact, and their fallbacks.

| ID | Risk | Impact | Fallback |
|---|---|---|---|
| R2 | An external dataset proves unavailable or unlabelled | High | Three verified external sources are already sufficient for SO3; the substitution is reported |
| R4 | The Flutter + TFLite integration stalls | High | The TensorFlow Lite task library over a platform channel; failing that, a minimal Kotlin client loading the same artefact |
| R6 | External field accuracy is too low to be useful | Medium | **This is a finding, not a failure.** The contribution becomes the quantified gap plus the abstention mechanism, and SO3's achievement status is stated as partially achieved |
| R9 | The system cannot be demonstrated at the defense | High | The core flow is offline and needs no server; the APK is installed on two devices in advance; a recorded demonstration is kept as a backup |
| R15 | The High-complexity justification is rejected, so the fourth member is not approved | High | The scope is reduced to the three-member minimum and the web client is dropped. The advisor is consulted before the Committee sees the proposal, so the advisor's objection is the one that matters |

**R6 deserves particular attention.** The project has decided *in advance* how it will report a
poor external result: honestly, as the central finding, with the abstention mechanism as the
mitigation. Deciding this before the measurement is what prevents a poor result in week 26
from becoming a crisis rather than a contribution.

---

## 3.7 Ethical considerations

The ethical screening checklist (Appendix M) is completed and reviewed by the advisor and the
Committee as part of the approval gate. The project involves **no** personal data, **no**
health, biometric, financial or educational records, **no** minors and **no** confidential
sponsor data. It does involve **human participants** in the usability evaluation, which
triggers the written-approval requirement of Guideline §15.4; the safeguards are an
information sheet, an informed-consent form, pseudonymous participant codes, aggregate-only
reporting, a right to withdraw, and destruction of the data after the defense. All third-party
data is used under CC BY 4.0 with attribution, and no dataset is redistributed by the project.
The AI-use record required by §15.3 is maintained from the first week.

The full screening and the safeguards are in `docs/appendices/Appendix-M-Ethics.md`; the AI-use
record is in `docs/appendices/Appendix-L-AI-Disclosure.md`.
