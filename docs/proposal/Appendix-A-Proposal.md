# Appendix A — Project Proposal

**College of Natural and Computational Sciences**
**Department of Computer Science**
**Addis Ababa University**

---

| Field | Value |
|---|---|
| **Title** | Design and Development of a Coffee Leaf Disease Diagnosis System Using Deep Learning |
| **Students and IDs** | Yohannes Berhanu (UGR/9440/16) · Hayredin Mohammed (UGR/2361/16) · Bemnet Tesfaye (UGR/3266/16) · Nahom Solomon (UGR/3155/16) |
| **Advisor** | Surafiel Habib Asefa |
| **Co-advisor / sponsor** | To be requested: Ethiopian Institute of Agricultural Research — Jimma Agricultural Research Center, Department of Plant Pathology (subject to approval) |
| **Primary project category** | Artificial intelligence and machine learning (Guideline §2.3) — with an interdisciplinary application component in agriculture |
| **Proposed complexity class** | **High** (Guideline §2.4) — justification in §2.4 below |
| **Submission date** | 21 October 2026 |

---

## 1. Background

Coffee is the primary source of foreign exchange and export revenue for Ethiopia, and the
crop supports a large rural population whose livelihoods depend directly on it. Production in
Ethiopia is, however, constrained by a small number of foliar diseases, of which coffee leaf
rust (*Hemileia vastatrix*), Cercospora leaf spot / brown eye spot (*Cercospora coffeicola*),
coffee leaf miner (*Leucoptera coffeella*) and brown leaf spot (*Phoma costarricensis*) are
among the most economically significant [1]–[4].

Two factors make disease identification a persistent problem for Ethiopian smallholders. First,
the agronomic services that provide diagnosis are concentrated in regional and district offices,
so a farmer in a remote coffee-producing kebelle may wait days or weeks for a visit, during
which an early rust infection can move from a few spots to whole-tree defoliation [2], [3].
Second, the visual symptoms of these four conditions overlap at the level of a farmer's eye
— rust's yellow-orange powdery pustules, Cercospora's concentric "brown eye spot" lesions,
Phoma's pale circular necrotic patches and leaf miner's serpentine mines are distinguished as
much by pattern and position on the leaf as by colour [4], [5]. This makes informal diagnosis
error-prone even when a knowledgeable person is available.

Computer-vision models for coffee leaf disease have advanced rapidly since 2018. Convolutional
models trained on the JMuBEN and BRACOL datasets report in-domain accuracies in the mid- to
high-90 % range on curated, laboratory-conditioned imagery [6]–[10]. This literature, however,
has two structural limitations that this project addresses.

The first is **deployment**. The overwhelming majority of published coffee leaf disease
classifiers exist as research artefacts: a notebook, a Streamlit or Gradio page, or an
application that calls a remote inference server. The two published mobile applications
identify only two diseases and require network connectivity to reach a server-hosted
model [11], [12]; the five-class web applications run on cloud-hosted Streamlit or Gradio
infrastructure [13]. None of the published systems operates offline, which is precisely the
condition under which a farmer in a remote kebelle most needs it.

The second limitation is **generalisation**, and it is more consequential. When models trained on
curated datasets are tested on field photographs, performance can collapse. A published
coffee-leaf EfficientNet-B2 model reports 94.09 % internal accuracy while correctly accepting a
rust diagnosis on only **16 of 847 (1.9 %)** external field rust images [14]. Independently, a
2026 benchmarking study of plant-disease classifiers reported a **67.7 percentage-point**
accuracy drop when moving from PlantVillage to PlantDoc field imagery, while the model's *mean
confidence stayed at 79.76 %* — meaning the model remained confidently wrong [15]. Furthermore,
the canonical analysis of why plant-disease deep learning underperforms in the field identified
background clutter, uncontrolled illumination and the presence of multiple symptoms on one leaf
as the dominant causes [16]. The conclusion across this evidence is that a coffee leaf disease
classifier which has only been validated on curated imagery cannot yet be trusted by a farmer.

This project therefore targets a **complete, offline, farmer-facing system** whose central
research contribution is a rigorous answer to the question: *how accurately does a
resource-constrained coffee leaf disease classifier perform on real field photographs, and can
that gap be narrowed with methods that fit a low-end phone?*

## 2. Problem statement and gap

### 2.1 The existing condition and affected stakeholders

Smallholder coffee farmers in Ethiopia's major producing regions — Jimma, Illubabor, Kaffa,
Bench, Shebelle, Welega and the Sidama and Guji highlands — depend on early detection of foliar
disease to avoid crop loss and unnecessary chemical expenditure [2], [3]. Extension officers
and Coffee and Tea Research Institute / Jimma Agricultural Research Center (JARC) staff provide
diagnosis, but their coverage is far below the number of producing households.

The consequence is measurable at the national level. Field surveys across south-western
Ethiopia recorded mean leaf rust incidence of **35.3 %** and severity of **9.09 %**, with
altitude identified as the dominant driver of epidemics [17]. Rust incidence of this magnitude
means detection, not treatment, is the binding constraint: by the time a farmer recognises a
problem, the window for inexpensive early intervention has closed.

The primary stakeholders are therefore (a) smallholder farmers who need immediate, actionable
diagnosis at the point of the plant; (b) extension officers who need a triage and record-keeping
tool across many sites; and (c) JARC/plant pathologists, who need field observations and
photographs aggregated for surveillance.

### 2.2 Evidence that the problem exists

1. **Agricultural evidence.** Rust epidemics in Ethiopia are well documented as severe and
   altitude-driven [17], with dedicated review literature on Ethiopian rust status and
   management [2], [3].
2. **Deployment evidence.** Both published mobile applications delegate inference to a remote
   server [11], [12]; the five-class applications are cloud-hosted web applications [13].
   A system requiring connectivity cannot serve its stated population.
3. **Generalisation evidence.** A published coffee-leaf model with 94.09 % internal accuracy
   achieves 1.9 % correct acceptance on external field rust images [14], and a controlled-to-field
   benchmark reports a 67.7-point accuracy collapse with uncalibrated confidence [15].
4. **Preliminary group investigation.** The group obtained direct access to the JMuBEN dataset
   from its originating author and independently confirmed that the released images are already
   cropped, resized and rotation/flip-augmented, with the original uncropped field photographs
   **not published** — meaning a naive random split of this dataset leaks near-duplicate
   images between training and test sets and inflates reported accuracy.

### 2.3 Shortcomings of current approaches

| Shortcoming | Consequence |
|---|---|
| Cloud/API dependence | The system is unavailable in exactly the low-connectivity areas that need it most |
| Heavy models (ConvNeXt-S ~99 MB) | Impractical for low-end Android devices and high data costs |
| No agronomic guidance layer | A label is not an action; farmers still need to know what to do |
| No longitudinal record | Disease progression cannot be tracked; repeated visits are unmeasured |
| Validation on curated imagery only | Reported accuracy does not reflect field performance |
| No uncertainty handling | Confident misclassification is presented to the user as a diagnosis |

### 2.4 The specific gap this project addresses

> **No published system provides a five-class coffee leaf disease classifier (Coffee Leaf Rust,
> Cercospora Leaf Spot, Leaf Miner, Phoma Leaf Spot, Healthy) that (a) runs fully offline on a
> low-cost mobile device, (b) delivers actionable agronomic guidance and a persistent diagnosis
> history, and (c) is evaluated against external field photographs with per-class recall,
> calibration error and selective-risk analysis rather than in-domain accuracy alone.**

### 2.5 Justification for High complexity (Guideline §2.4, §14.1)

A group of four requires the Committee to approve a High-complexity project. This project meets
the "substantial research, data or systems challenge **or** a real external stakeholder with
real data" criterion on all three counts:

1. **A real external stakeholder with real data.** The group has an open data-sharing
   relationship with the originating author of JMuBEN, and is seeking a written collaboration
   with JARC's Plant Pathology Department for agronomic validation of the treatment knowledge
   base and for field photographs for the external evaluation set.
2. **A substantial research challenge.** The central research question is a *measured,
   reproducible* generalisation gap: how far does a coffee leaf classifier trained on curated
   imagery fall on genuine field photographs, and which intervention (aggressive augmentation,
   domain-robust pretraining, confidence calibration with abstention) most reduces that gap
   under a hard memory and latency budget? The literature provides a documented failure
   phenomenon [14], [15], [16] but no offline, five-class, phone-deployed system that measures it.
3. **A substantial data and systems challenge.** Nine separately licensed datasets across four
   countries, each with different label taxonomies, species (Arabica and Robusta), capture
   conditions and duplication structures, must be harmonised into a leakage-safe evaluation
   protocol — a genuine data-engineering task, not a download-and-train exercise.

Additionally, the project satisfies well over five of the ten standard-complexity activities:
requirements analysis, architecture and design, database/data engineering, model development,
substantial programming in three languages (Python, Dart, TypeScript/JavaScript), systematic
testing, quantitative and user evaluation, security design, deployment, and practical research.

## 3. Motivation

The motivation is a single sentence: **coffee leaf disease in Ethiopia is detected late because
the diagnostician is far away, and the software that could close that distance currently
requires the connectivity that is missing.**

Three further motivations shape the design. First, the four target diseases have genuinely
different management, so a classifier that only emits a label leaves the farmer no better off.
Second, Ethiopian smallholders operate low-cost Android devices on metered data, so model size
is a design constraint, not an optimisation detail. Third, an offline system generates
longitudinal field data that a cloud system never sees — and the group can use that data to
advance the generalisation research question.

## 4. Objectives

### General Objective

> To design, implement and evaluate a lightweight, fully offline deep-learning system that
> diagnoses five coffee leaf conditions from a photograph on a low-cost mobile device, delivers
> agronomic treatment guidance, and maintains a local diagnosis history, and to quantify and
> mitigate the generalisation gap of such a classifier on external field photographs.

### Specific Objectives

| ID | Specific objective | Measurable target |
|---|---|---|
| **SO1** | **Curate and document** a multi-source, leakage-safe coffee leaf image corpus covering Coffee Leaf Rust, Cercospora, Leaf Miner, Phoma and Healthy leaves, with a published datasheet recording provenance, licensing, class distribution and the exact train/validation/test split | ≥58,000 labelled images across ≥4 independently licensed sources; 100 % of images assigned to a split by a documented duplicate-grouping rule; a datasheet and split manifest published in the repository |
| **SO2** | **Train and compare** lightweight CNN architectures against at least one naive baseline under identical conditions | ≥3 models (majority-class baseline, MobileNetV3-Small, and ≥1 further architecture such as EfficientNet-Lite0 or MobileNetV2) with mean and standard deviation over ≥3 seeded runs; macro-F1 on the internal test split reported |
| **SO3** | **Quantify the generalisation gap** by evaluating every trained model on ≥3 external field-photo datasets that share no source with training, and **mitigate** it | External macro-F1 reported per dataset, with the gap vs the internal split stated; a confidence-acceptance threshold implemented such that ≥95 % of *accepted* diagnoses on the external sets are correct (coverage reported alongside, not hidden) |
| **SO4** | **Implement on-device inference** in a mobile application supporting camera capture and gallery upload | Quantised TFLite model ≤10 MB; median inference latency ≤500 ms and p95 ≤1,000 ms on a low-end reference device; all core features functional in airplane mode |
| **SO5** | **Implement the results and guidance experience**: a diagnosis screen with per-class confidence and a structured agronomic knowledge base (symptoms, severity guidance, organic and chemical treatment) linked to each prediction | 100 % of the five classes have a reviewed KB entry with a named source; the KB ships as an embedded offline asset; the result screen renders it in ≤1 tap from the prediction |
| **SO6** | **Implement a persistent local diagnosis history** with search, filtering and export | History survives app restart; query by class and date range; export to CSV; 100 % of diagnoses are logged with timestamp, predicted class, confidence and image reference |
| **SO7** | **Test and evaluate the complete system** — functionally, for performance, for security and for usability — and report the result against every objective | ≥40 executed test cases with actual results and evidence (Appendix F); a SUS usability score from ≥10 participants; a completed objective-to-evidence traceability matrix stating achieved / partially achieved / not achieved per objective |

**Research questions (RQ)** — linked to objectives, each with a defined method of answer:

- **RQ1** (→ SO3): How large is the drop in macro-F1 when a coffee leaf classifier trained on
  curated imagery is evaluated on external field photographs, and how does that drop vary by
  disease class and by source dataset? *Method: identical model, identical preprocessing,
  identical inference code; five datasets; per-class and per-dataset breakdown; bootstrap
  confidence intervals.*
- **RQ2** (→ SO3): Among augmentation strategy, calibration with abstention, and inclusion of
  an African-sourced field dataset in training, which most improves external macro-F1 per unit
  of deployed model size? *Method: controlled ablation, each variant trained with ≥3 seeds;
  McNemar test on paired predictions for the winning comparison.*
- **RQ3** (→ SO4): What accuracy is achievable on a low-cost Android device under a 10 MB
  model budget and a 1 s latency budget? *Method: MobileNetV3-Small and EfficientNet-Lite0 with
  float32, float16 and int8 post-training quantisation; measured on three reference devices.*
- **RQ4** (→ SO5): Can treatment guidance be delivered in a form that is both agronomically
  defensible and comprehensible to a user without formal training, verified by review from a
  plant pathology specialist and a comprehension check with participants? *Method: KB entries
  sourced from FAO and peer-reviewed Ethiopian literature, reviewed by JARC, then checked
  during the usability session.*

**Hypotheses (H)** — stated so they can be falsified:
- **H1:** A model trained on JMuBEN/JMuBEN2 alone will achieve a macro-F1 at least 20 points
  lower on external field photographs than on its internal test split.
- **H2:** Adding the Uganda field dataset to training and applying field-realistic augmentation
  will increase external macro-F1 by at least 5 points over the JMuBEN-only baseline, at a
  deployed-size cost of less than 1 MB.
- **H3:** Temperature scaling plus a confidence-acceptance threshold will reduce the
  expected calibration error on the external sets by at least 30 % relative, while retaining
  at least 60 % coverage.

## 5. Scope and limitations

### 5.1 Scope

| Dimension | Included |
|---|---|
| **Diagnostic classes** | Coffee Leaf Rust (*Hemileia vastatrix*); Cercospora Leaf Spot / brown eye spot (*Cercospora coffeicola*); Coffee Leaf Miner (*Leucoptera coffeella*); Phoma Leaf Spot / brown leaf spot (*Phoma costarricensis*); Healthy |
| **Inputs** | RGB smartphone photographs — live camera capture or gallery selection. Single leaf, adaxial or abaxial surface |
| **Outputs** | Predicted class with per-class confidence, a confidence-based recommendation to retake the photo, and the linked agronomic guidance entry |
| **Application features** | Capture/upload, on-device offline inference, results screen, guidance screen, local diagnosis history with search and export |
| **Secondary interface** | A web client against the same REST API, for extension officers and for demonstration on a laptop |
| **Environment** | Android 8.0+ primary target; iOS-compatible Flutter codebase; server component on a standard container host |
| **Data** | Nine CC BY 4.0 public datasets from Kenya, Brazil, Ecuador, Uganda, Peru and Colombia |

### 5.2 Limitations

1. **Diagnostic scope.** Restricted to the five classes above. It does not cover nutrient
   deficiencies, red spider mite, coffee weevil damage, *Mycena citricolor* (ojo de gallo),
   anthracnose, root and stem disease, or coffee cherry diseases. Where the model encounters a
   symptom outside the supported taxonomy, it must report `unsupported`, not force a label.
2. **Appearance-only reasoning.** The model classifies visible symptoms; it cannot measure
   disease severity, cannot see the whole plant, and cannot detect pathogens below the
   visible-symptom threshold.
3. **Environmental sensitivity.** Accuracy degrades under direct glare, deep shadow, severe
   motion blur, heavy occlusion and non-typical backgrounds. The system mitigates this with
   photo-quality checks and confidence abstention rather than eliminating it.
4. **Field-performance ceiling.** The evaluation quantifies a generalisation gap that this
   project does not fully close. The external macro-F1 reported in Chapter 6 is the honest
   measure of likely real-world usefulness, not the internal test accuracy.
5. **Local-only history.** Diagnosis history is stored on the device. Synchronisation to the
   server is an optional, user-initiated export in v1, not an automatic sync.
6. **Guidance is advisory.** The KB summarises published recommendations for crop protection.
   It is decision support, not a substitute for a qualified extension officer, and the app must
   state this.
7. **Training-data geography.** The largest curated source is Kenyan; the Ugandan and
   Ethiopian contribution is a single field set. An Ethiopian-specific model would require
   substantially more Ethiopian field data than is currently openly available.

## 6. Significance

**For farmers.** A farmer in a remote kebelle can photograph an affected leaf and receive, in
seconds and without signal or data cost, a probable diagnosis with guidance on what to observe
and what action to take. Early identification shortens the window between infection and
response, which is the decisive factor in rust management [2], [3], [17].

**For extension officers and JARC.** The system produces structured, geotagged, timestamped
observation records — a surveillance input that currently does not exist at field scale.
Because the system works offline, an officer can work through a district without connectivity
and synchronise later.

**For the research community.** The project publishes a leakage-safe split protocol and an
external-evaluation methodology for coffee leaf disease, together with an honest, quantified
account of the curated-to-field generalisation gap. Given the documented 1.9 % external rust
recall of an existing published model [14] and the 67.7-point collapse reported in the wider
plant-disease literature [15], a reproducible measurement from an independent group has clear
value.

**For the Department.** Coffee is a national priority sector and JARC is a local institution.
A validated, open-source, offline diagnostic tool is a deliverable that outlives the project.

## 7. Literature review and related work

*(Full thematic synthesis: `docs/literature/ch2-literature-review.md`. Comparison table:
`docs/literature/comparison-table.md`. IEEE reference list: `docs/literature/references.md`.)*

The literature is organised thematically into five strands.

**Strand 1 — Dataset construction and leakage.** The field's dominant dataset is JMuBEN
[1], comprising 58,549–58,555 Arabica images across five classes collected at Mutira
plantation, Kirinyaga, Kenya, labelled by a plant pathologist. The dataset card and the
dataset's own paper both document that the released images are **cropped to the region of
interest, resized, and augmentation-augmented (rotation and flipping)** to equalise sizes —
and the original uncropped field photographs are not published. The consequence is structural:
a random split leaks near-duplicates. BRACOL [5] has the same property in a different form —
its 2,147 symptom images are **crops of the 1,747 whole-leaf photographs** — and ROCoLE [19]
provides four views per plant. The group's preliminary analysis therefore treats
*duplicate grouping before splitting* as a methodological precondition rather than an
optimisation.

**Strand 2 — Model accuracy on curated imagery.** Reported in-domain accuracies are high and
rising: 93–99 % across eleven architectures on JMuBEN with balanced classes [7]; 97.37 % on
JMuBEN with hybrid DL+ML [8]; 97.31 % with a VGG-16/ResNet-152/EfficientNet-B0 ensemble [9];
99.72 % with EfficientNet-B0 [10]; 99.78 % with a GoogLeNet–ResNet18 feature fusion and SVM
on BRACOL [6]. A review of this literature reveals a methodological weakness that runs
through it: with the single exception of the 2020 external test [7], these figures are
in-domain, and the "external" test in [7] was itself constructed by topping up the fifth class
with training images.

**Strand 3 — Deployment reality.** The published mobile applications are the crucial prior
art. Manso et al. [11] built a smartphone application detecting leaf miner and rust with
severity quantification, from the same Brazilian group that produced BRACOL; its commercial
successor, Coffee Recognize [12], is an Ionic/Android client that delegates inference to a
Node.js REST API hosting a 54 MB frozen TensorFlow Object Detection graph — it therefore
**requires connectivity**. A 2024 Rwanda-based application pairs DenseNet inference with GPS
geo-tagging of captured images [21]. A 2023 student-congress mobile module pairs rust
detection with treatment recommendations at 58 % accuracy [20]. All of these cover two to four
classes, and none is offline.

**Strand 4 — On-device and lightweight modelling.** MobileNetV3 was designed by hardware-aware
architecture search specifically for phone CPUs [22]; EfficientNet-Lite is Google's
mobile-oriented variant [23]; and lightweight plant-disease models using MobileNetV3 with
post-training quantisation have been demonstrated to lose no accuracy while shrinking
1.5 M parameters to 0.93 M [24]. A TinyMLOps pipeline for plant disease exported to LiteRT
with mixed-precision float fallback measured F1 degradation of at most 0.0073 on a Raspberry Pi
Zero 2 W [25]. This strand establishes that the ≤10 MB, sub-second target in SO4 is
achievable with standard tools.

**Strand 5 — Generalisation and responsible deployment.** This is where the literature turns
against itself. Barbedo's 2018 analysis identified uncontrolled background, illumination and
multiple concurrent symptoms as the dominant causes of plant-disease model failure in the
field [16]. A 2023 study of unsupervised domain adaptation from laboratory to field imagery
reported mean accuracy of 56.06 % for a self-supervised model versus 42.87 % for an
adversarial baseline [26]. A 2026 benchmarking study measured a **67.7 percentage-point
accuracy collapse** from PlantVillage to PlantDoc while **mean confidence remained 79.76 %**,
and found that DANN-style adversarial adaptation *degraded* accuracy to 0.252 — i.e. the
standard domain-adaptation remedy can make things worse [15]. The most directly relevant
single artefact is the published coffee-leaf EfficientNet-B2 model card: 94.09 % internal
accuracy, 8.57 MB TFLite export, and **16 of 847 (1.9 %) correct acceptances on an external
rust collection** [14]. A second model card, for a ConvNeXt-S covering seven classes, reports
Cercospora recall of just **9.1 %** [27].

**The gap.** Across all five strands, one thing is never found: a five-class coffee leaf
classifier that runs fully offline on a low-cost phone, delivers agronomic guidance and
diagnosis history, and is evaluated on external field photographs with per-class recall,
calibration and abstention. Strand 2's accuracies are high but unmeasured in the field. Strand
3's systems are deployed but cloud-bound and narrow in class coverage. Strand 5's evidence
that curated-image accuracy does not survive the field has never been operationalised into a
system design that a farmer can actually hold.

## 8. Methodology

### 8.1 Research and development method

An **iterative, prototype-driven** method is adopted, because the project has three components
whose feasibility is genuinely uncertain and must be de-risked early: (i) whether a leakage-safe
split materially changes the accuracy picture, (ii) whether a sub-10 MB model can retain
acceptable external accuracy, and (iii) whether Flutter + TFLite inference can be made reliable
on low-end Android hardware. Each uncertainty is converted into a prototype that is built,
measured and reviewed before the next component is built on top of it.

Within the model work specifically, an **experimental** method is used: a fixed protocol
(all data, splits, augmentation pipelines and training scripts are version-controlled; seeds are
fixed and recorded; ≥3 seeds per configuration; the test set is touched once per configuration
and never for tuning) supports the ablation and comparison that RQ1–RQ3 require.

### 8.2 How each objective is achieved and measured

| SO | Method | Success measure |
|---|---|---|
| SO1 | Curate 9 datasets; record provenance and licenses; perceptual-hash + source-group duplicate clustering; stratified grouped split by source and duplicate-closure | Datasheet published; every image in exactly one split; split manifest checksummed and committed |
| SO2 | Transfer learning on ≥3 architectures + majority-class baseline; identical pipeline; ≥3 seeds | Macro-F1, per-class F1, confusion matrix; mean ± sd across seeds |
| SO3 | Evaluate on Uganda, ROCoLE, Saposoa, CoffeeLeaf-CO and Silva; then ablate augmentation, calibration and training-data source | Per-dataset macro-F1 with bootstrap CI; gap vs internal; abstention curve; McNemar test for the key comparison |
| SO4 | MobileNetV3-Small / EfficientNet-Lite0; float32 → float16 → int8 PTQ; Flutter + `tflite_flutter` | Model ≤10 MB; median ≤500 ms, p95 ≤1,000 ms on a low-end device; airplane-mode feature test passes |
| SO5 | KB as versioned JSON embedded as an app asset; fields: scientific name, local name, symptoms, risk factors, severity cues, organic control, chemical control, prevention, references | 5/5 classes covered; every field sourced; reviewed by JARC; rendered in ≤1 tap |
| SO6 | SQLite (sqflite/Drift) with a versioned schema and migrations | Restart-persistence test; class and date-range queries; CSV export; 100 % logging rate |
| SO7 | Test plan across unit, integration, system, performance, security and usability levels; Appendix F as the evidence record | ≥40 test cases with actual results and evidence; SUS from ≥10 participants; Appendix E complete with achievement status |

### 8.3 Baseline justification (Guideline §9.1)

The project reports **three** baselines, all evaluated under conditions identical to the
proposed model: (i) a **majority-class predictor** (predicting the most frequent class always),
which establishes the floor and exposes class imbalance; (ii) a **transfer-learning MobileNetV3-
Small** on the leakage-safe split, which is the practical lightweight reference; and (iii) the
**published external baselines** — the ConvNeXt-S coffee model [27] and the EfficientNet-B2
TFLite model [14] — run on our splits so that our numbers are comparable to the field's.

**Why machine learning rather than a rule-based solution (Guideline §9.1):** a rule-based
classifier would require hand-crafted thresholds over lesion colour, size, count, position and
shape simultaneously. Because the diagnostic signal is the *pattern* of lesions across the leaf
rather than any single measurable feature, and because the four target diseases overlap in
colour and morphology, a rule system would encode the hand-crafted decisions of one expert and
would not generalise to the lighting, background and cultivar variation present in field
imagery. Learning the feature combination from data is the appropriate approach, provided the
evaluation measures field performance honestly.

## 9. Preliminary requirements

### 9.1 Functional requirements (abbreviated; the full specification is the requirements baseline)

| ID | Requirement | Priority |
|---|---|---|
| FR-01 | The system shall allow the user to capture an image of a coffee leaf using the device camera | Must |
| FR-02 | The system shall allow the user to select an existing image from the device gallery | Must |
| FR-03 | The system shall perform classification entirely on the device, without network access | Must |
| FR-04 | The system shall return the predicted class with a confidence value for each of the five classes | Must |
| FR-05 | The system shall display the agronomic guidance entry corresponding to the predicted class | Must |
| FR-06 | The system shall record every diagnosis with timestamp, image reference, predicted class and confidence in a local database | Must |
| FR-07 | The system shall allow the user to list, search and filter the diagnosis history by class and date | Must |
| FR-08 | The system shall allow the user to delete a history record and export the history to CSV | Should |
| FR-09 | The system shall warn the user to retake the photo when confidence is below a defined threshold | Must |
| FR-10 | The system shall provide a REST API offering prediction, history CRUD and knowledge-base retrieval | Should |
| FR-11 | The system shall provide a web interface against that API | Should |
| FR-12 | The system shall validate every uploaded image (type, size, decodability) and reject invalid input safely | Must |

### 9.2 Non-functional requirements (abbreviated)

| ID | Requirement | Target |
|---|---|---|
| NFR-01 | Inference latency on the low-cost reference device | Median ≤500 ms; p95 ≤1,000 ms |
| NFR-02 | Deployed model size | ≤10 MB |
| NFR-03 | Peak app memory | ≤250 MB |
| NFR-04 | Core-feature operation with no network | 100 % of FR-01…FR-09 pass in airplane mode |
| NFR-05 | API availability during the demo | ≥99 % over the evaluation window |
| NFR-06 | API response time for a 224×224 upload (p95) | ≤2 s |
| NFR-07 | Security | OWASP Top 10 for the API: input validation, file-type and size limits, no secrets in the repository, dependency scanning, rate limiting |
| NFR-08 | Usability | SUS score ≥70 from ≥10 participants; ≥90 % task success on capture→diagnosis→guidance |
| NFR-09 | Reproducibility | A single documented command reproduces the split and training from a pinned environment file |
| NFR-10 | Maintainability | Modular code, a stated coding standard, README with build/run instructions, ≥80 % unit-test coverage on the inference wrapper, history layer and API |
| NFR-11 | Portability | Android 8.0+; graceful message on unsupported device |
| NFR-12 | Localisation readiness | User-facing strings externalised, with English and Amharic string resources, so an Amharic UI is a configuration change rather than a code change |

## 10. Proposed design and technologies

### 10.1 Architecture

```
┌────────────────────────── Mobile client (Flutter, Android/iOS) ──────────────────────────┐
│  Capture / Gallery  →  Quality Gate  →  Preprocess (224×224, RGB, /255)  →  TFLite       │
│  Interpreter (int8)  →  Calibrator (temperature scaling)  →  Abstention check            │
│                                              │                                              │
│                                              ▼                                              │
│                          Result Screen ◄── KB Resolver (embedded JSON) ──► Guidance Screen  │
│                                              │                                              │
│                                              ▼                                              │
│                          Local Repository (SQLite) ──► History Screen (search/filter/export) │
└──────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                               │ optional, user-initiated export
                                               ▼
┌─────────────────────── Server (FastAPI + PostgreSQL) ───────────────────────┐
│  POST /v1/predict   POST/GET /v1/diagnoses   GET /v1/diagnoses/{id}       │
│  GET  /v1/kb/{class}   GET /v1/health   GET /v1/metrics                   │
│  TFLite (float32 server model)  ·  Model registry  ·  JWT auth  ·  CORS     │
└────────────────────────────────────────────────────────────────────────────┘
                                               ▲
┌────────────────────────────── Web client (static HTML/JS) ───────────────────────────────┐
│  Upload → Result → Guidance → History (extension-officer view)                          │
└──────────────────────────────────────────────────────────────────────────────────┘
```

### 10.2 Technology choices and justification

| Layer | Choice | Justification |
|---|---|---|
| Model | TensorFlow/Keras, MobileNetV3-Small + EfficientNet-Lite0 | Hardware-aware architectures designed for phone CPUs [22], [23]; both supported directly by TFLite Model Maker |
| Model export | TFLite with post-training int8 quantisation | Demonstrated to preserve accuracy while shrinking plant-disease models [24]; supported by Model Maker and MediaPipe |
| Mobile | Flutter + `tflite_flutter` + `sqflite`/Drift | One codebase for Android and iOS; mature TFLite plugin; strong camera and gallery support; single language across the team |
| Knowledge base | JSON asset embedded in the app | Zero network dependency, versionable with the build, diffable in review |
| API | Python 3.11 + FastAPI + Pydantic v2 + SQLAlchemy 2 + Alembic | Fast to build, automatic OpenAPI documentation, typed validation that directly satisfies NFR-07 |
| Server DB | PostgreSQL (SQLite for local dev) | Transactional, indexed history queries, standard for a defense demonstration |
| Web client | Vanilla HTML/CSS/JS + fetch | No build step to break the night before the defense; trivially hostable; the API's OpenAPI schema guarantees the contract |
| Experiment tracking | Versioned YAML configs + seeded runs + a results-to-script mapping table | Satisfies §9.3 and §9.7 reproducibility requirements |
| CI | GitHub Actions: lint, unit test, container build, model-artefact check | §8.4 and §8.5 |
| Deployment | Docker on a free-tier container host | Reproducible, cheap, demonstrable at the defense |

**Rejected alternatives, with reasons.** React Native: comparable capability, but the TFLite
plugin ecosystem and our familiarity are weaker, and a second language would slow a
four-person team. TensorFlow Lite Micro: target is microcontrollers, not phones; the model
runtime integration burden is not justified. A fully custom native Android app: maximum
control, minimum schedule risk. Full cloud-only inference: directly contradicts SO3 and the
offline requirement. ONNX Runtime Mobile: viable, but TFLite has the better Flutter support
and the better-documented Model Maker path.

### 10.3 Design artifacts to be produced in FYP I weeks 8–13

Use-case diagram; activity diagram; sequence diagram; class diagram; state diagram for the
diagnosis lifecycle; relational schema and data dictionary; architecture, component and
deployment diagrams; data-flow diagram; UI wireframes for all screens; algorithm pseudocode for
the inference and abstention pipeline; and a working prototype (§10.4).

### 10.4 Prototype

A prototype will exist in two forms: (a) a **model prototype** — a trained TFLite artefact with
reported metrics, proving the modelling feasibility; and (b) an **application prototype** — a
Flutter build with a placeholder model and a mocked API, proving the integration and offline
paths before the real components are ready. The second is what de-risks the schedule.

## 11. Resources, risks and ethical considerations

### 11.1 Resources

| Resource | Requirement | Source |
|---|---|---|
| Data | 9 open datasets, all CC BY 4.0 | Public Mendeley Data, Zenodo, Kaggle mirrors (see §12) |
| Compute — training | GPU with ≥8 GB VRAM; **Kaggle notebooks (free, Tesla P100) are the primary route** | Kaggle / Colab free tier |
| Compute — local | A development laptop; model conversion runs comfortably on CPU | Group member hardware |
| Compute — devices | ≥3 Android reference devices across low/mid/high tiers | Group members' own phones + department lab request |
| Software | Python 3.11, Flutter SDK, Android Studio, Docker, Git | All open source (Appendix §12) |
| Server | 1 container instance for the API and web client | Free-tier container host |
| Human | JARC plant pathology specialist (2–3 h review of the KB) | To be requested; in-kind |
| Budget | ≈ 0 ETB; ≈ 3,000 ETB at most if a mobile data bundle is needed for field testing | Group / student |

### 11.2 Risk register (full register: `docs/04-RISK-REGISTER.md`)

| ID | Risk | P | I | Mitigation | Owner |
|---|---|---|---|---|---|
| R1 | JMuBEN author does not share the original un-augmented images | M | M | The released dataset is sufficient if duplicate grouping is done properly; the group proceeds regardless and documents the limitation | Hayredin |
| R2 | External datasets prove unavailable or unlabelled | M | H | Five independent external sources are already verified; at least three are sufficient | Hayredin |
| R3 | No GPU available for training | M | M | Kaggle/Colab free-tier P100/T4 notebooks; the reference architectures train in under 2 h | Hayredin |
| R4 | Flutter/TFLite integration stalls | M | H | Fallback: TensorFlow Lite task library via platform channels; second fallback: a Kotlin camera app using the same `.tflite` artefact | Yohannes |
| R5 | Model too large or too slow for low-end devices | M | M | Progressive fallback: int8 quantisation → EfficientNet-Lite0 → MobileNetV2 → 160×160 input | Hayredin + Yohannes |
| R6 | External accuracy is too low to demonstrate usefulness | H | M | This is a *finding*, not a failure. The contribution is the quantified gap plus abstention; the report states it honestly | All |
| R7 | Scope expansion into detection, severity or other crops | M | H | Explicit non-goals in §5.1; change control per Guideline §4.6 | All |
| R8 | Schedule delay from an unavailable member or exam period | M | M | Weekly cross-review rotation keeps knowledge distributed; tasks have named backups | All |
| R9 | The system is deployed but cannot be demonstrated at the defense | L | H | A recorded demonstration is always kept as a backup; the app runs offline with no server dependency for the core flow | Yohannes + Bemnet |
| R10 | Agronomic guidance is challenged as inaccurate | M | M | Every KB field carries a citation; JARC reviews before inclusion; the app states that guidance is advisory | Nahom |
| R11 | AI-generated content in the report is treated as misconduct | M | H | Appendix L is maintained from day one; every AI-assisted artifact is reviewed, understood and tested by a named member | All |
| R12 | Personal data or photos of identifiable people enter the repository | L | M | No personal data is collected; photos are of leaves; `.gitignore` excludes raw uploads; the ethics screen (Appendix M) records this | Yohannes |

### 11.3 Ethical considerations

Completed in Appendix M. Summary: the project involves **no** human participants in the data
phase, **no** identifiable personal data, **no** health/biometric/financial/educational records,
**no** minors, and **no** confidential sponsor data. The usability study in SO7 does involve
participants and therefore requires informed consent, anonymised records and the safeguard
described in Appendix M. No confidential or personal data will be entered into any external AI
service. The app is classified as **decision support**: it displays an advisory notice and
recommends consulting an extension officer, and it is designed to abstain rather than to give a
confident answer it cannot support. All third-party data is used under CC BY 4.0 with
attribution in the datasheet, the report and the app's about screen.

## 12. Expected deliverables

1. Approved project proposal (this document).
2. A published **datasheet** and a reproducible **split manifest** for the curated corpus (SO1).
3. Trained model artefacts: float32, float16 and int8 TFLite, with a model card (SO2, SO4).
4. A **mobile application** (Flutter, Android/iOS) implementing capture, upload, offline
   inference, results, guidance and history (SO4, SO5, SO6).
5. A **REST API** service and a **web client** (SO5, SO6).
6. A **knowledge base** of five reviewed agronomic entries with citations (SO5).
7. **Test evidence**: ≥40 executed test cases, performance measurements on three devices,
   calibration and external-evaluation results, a SUS usability study (SO7).
8. **FYP I document** (Chapters 1–4), **FYP II report** (Chapters 1–7), **presentation slides**
   (≤22), and the **logbook** with weekly entries and advisor initials.
9. **Reproducibility package**: environment file, seeds, scripts, a results-to-script table, and
   a permitted dataset sample with download instructions (Guideline §9.7, Appendix I).
10. **Technical documentation**: installation guide, user guide, architecture, API documentation,
    third-party licence list (Appendix J), AI-use declaration (Appendix L), individual
    contribution statements (Appendix G).

## 13. Work plan

The full 32-week plan with per-member allocation is in `docs/01-ROADMAP.md` and
`docs/03-ROLES.md`. Summary against the guideline timeline (Table 16.1):

| Phase | Weeks | Dates | Deliverable | Gate |
|---|---|---|---|---|
| Orientation and title selection | 1–2 | Oct 19 – Nov 1 | Proposal, ethics screen, repository, logbook W1–W2 | Advisor / Coordinator approval |
| Proposal | 3–4 | Nov 2 – Nov 15 | Final proposal, baseline results, proposal presentation | **Proposal approval** |
| Extended literature review and requirements | 5–7 | Nov 16 – Dec 6 | Literature review, comparison table, gap, FR/NFR specification | **Requirements baseline** |
| Design | 8–13 | Dec 7 – Jan 17 | Models, architecture, database, UI design, model prototype | Design review |
| FYP I defense | 14 | Jan 18 – Jan 24 | FYP I document (Chapters 1–4) and presentation | Presentation and assessment |
| FYP II implementation I | 15–18 | Jan 25 – Feb 21 | Core prototype | Progress review |
| FYP II implementation II | 19–22 | Feb 22 – Mar 21 | Integrated system, web client, model v2 | Prototype review |
| Testing and evaluation | 23–24 | Mar 22 – Apr 4 | Test results, external evaluation, usability study, traceability | Evaluation review |
| Final report | 25–29 | Apr 5 – May 9 | Draft final report (Chapters 1–7) | Advisor approval |
| FYP II defense | 30 | May 10 – May 16 | Report, presentation and live demonstration | Final assessment |
| Corrections and final submission | 31–32 | May 17 – May 30 | Corrected report and submission package | Advisor verification |

**Critical path:** dataset download → duplicate grouping → leakage-safe split → model training →
TFLite export → app integration. The integration step is protected by a placeholder-model
prototype that must exist in the app by the end of FYP I week 13.

**Recurring controls.** The logbook is updated weekly and initialled by the advisor every two
weeks (Guideline §13). The risk register is reviewed with the advisor monthly (§6.3). The
AI-use declaration is updated monthly (§15.3). The traceability matrix is maintained from the
requirements baseline and completed during FYP II (§10.6).

## 14. References

The complete IEEE-formatted reference list is maintained at `docs/literature/references.md`
(≥20 sources). The principal sources cited in this proposal are:

[1] J. Jepkoech, D. M. Mugo, B. K. Kenduiywo, and E. C. Too, "Arabica coffee leaf images dataset for coffee leaf disease detection and classification," *Data in Brief*, vol. 36, Art. no. 107142, Jun. 2021, doi: 10.1016/j.dib.2021.107142.

[2] G. Berihun and K. Alemu, "Status of coffee leaf rust (*Hemileia vastatrix*) and its management in Ethiopia: a review," *Archives of Phytopathology and Plant Protection*, vol. 55, no. 20, pp. 2283–2300, Dec. 2022, doi: 10.1080/03235408.2023.2168173.

[3] M. Yirga, "Potential effects, biology and management options of coffee leaf rust (*Hemileia vastatrix*): a review," *International Journal of Forestry and Horticulture*, vol. 6, no. 1, pp. 19–31, 2020, doi: 10.20431/2454-9428.0601003.

[4] F. G. Waldamichael, T. G. Debelee, and M. Y. Ayano, "Coffee disease detection using a robust HSV color-based segmentation and transfer learning for use on smartphones," *Int. J. Intell. Syst.*, vol. 37, no. 8, pp. 4967–4993, Nov. 2021, doi: 10.1002/int.22747.

[5] R. A. Krohling, G. J. M. Esgario, and J. A. Ventura, "BRACOL — A Brazilian Arabica coffee leaf images dataset to identification and quantification of coffee diseases and pests," *Data in Brief*, vol. 23, Art. no. 001284, 2019, doi: 10.1016/j.dib.2019.01.284.

[6] H. Ardah, M. Alrahhal, W. M. Abd-Elhafiez, and D. Trabay, "Robust coffee plant disease classification using deep learning and advanced feature engineering techniques," *PeerJ Comput. Sci.*, vol. 11, Art. no. e3386, Dec. 2025, doi: 10.7717/peerj-cs.3386.

[7] N. Baht, E. Dominguez, and S. Aljumaili, "Detection of coffee leaf disease and identification using deep learning," *PeerJ Comput. Sci.*, vol. 11, Art. no. e3172, Oct. 2025, doi: 10.7717/peerj-cs.3172.

[8] K. J. Ayikpa, D. Mamadou, P. Gouton, and K. J. Adou, "Experimental evaluation of coffee leaf disease classification and recognition based on machine learning and deep learning algorithms," *J. Comput. Sci.*, vol. 18, no. 12, pp. 1201–1212, Dec. 2022, doi: 10.3844/jcssp.2022.1201.1212.

[9] D. Novtahaning, H. A. Shah, and J.-M. Kang, "Deep learning ensemble-based automated and high-performing recognition of coffee leaf disease," *Agriculture*, vol. 12, no. 11, Art. no. 1909, Nov. 2022, doi: 10.3390/agriculture12111909.

[10] S. Venkatraman, M. Mani, A. Balasundaram, and A. Shaik, "Automated coffee leaf disease classification via deep feature extraction with PhytoV2Net and InceptionV3 architectures," *Front. Agron.*, vol. 8, Art. no. 1767554, Mar. 2026, doi: 10.3389/fagro.2026.1767554.

[11] G. L. Manso, H. Knidel, R. A. Krohling, and J. A. Ventura, "A smartphone application to detection and classification of coffee leaf miner and coffee leaf rust," arXiv:1904.00742, Mar. 2019.

[12] A. L. C. Carneiro and L. B. Silva, "Coffee Recognize: coffee leaf disease recognition and severity quantification," GitHub, `Lucs1590/Coffee_Recognize` and `AlvaroCavalcante/Coffee_Recognize_API`.

[13] dimitramuni, "Coffee disease identification — Omdena São Paulo local chapter," GitHub, `dimitramuni/Coffee-Disease-Identification-Omdena`.

[14] ConnorLee08, "Coffee leaf EfficientNet-B2 — model card and TFLite export," Hugging Face, `ConnorLee08/coffee-leaf-efficientnet-b2`.

[15] K. Xiang, D. Shi, and X. Zhu, "Quantifying the reliability gap in cross-domain plant disease classification: benchmarking the limited efficacy of standard mitigation techniques under controlled-to-field shift," *Front. Plant Sci.*, vol. 17, Art. no. 1826962, May 2026, doi: 10.3389/fpls.2026.1826962.

[16] J. G. A. Barbedo, "Factors influencing the use of deep learning for plant disease recognition," *Biosyst. Eng.*, vol. 172, pp. 84–91, Aug. 2018, doi: 10.1016/j.biosystemseng.2018.05.013.

[17] K. Belachew, G. A. Senbeta, W. Garedew, R. W. Barreto, and E. M. Del Ponte, "Altitude is the main driver of coffee leaf rust epidemics: a large-scale survey in Ethiopia," *Trop. Plant Pathol.*, vol. 45, no. 5, pp. 511–521, Jul. 2020, doi: 10.1007/s40858-020-00383-4.

[18] J. V. Y. B. Yamashita and J. P. R. R. Leite, "Coffee disease classification at the edge using deep learning," *Smart Agric. Technol.*, vol. 4, Art. no. 100183, Aug. 2023, doi: 10.1016/j.atech.2023.100183.

[19] J. Parraga-Alava, K. Cusme, A. Loor, and E. Santander, "RoCoLe: A robusta coffee leaf images dataset for evaluation of machine learning based methods in plant diseases recognition," *Data in Brief*, vol. 25, Art. no. 104414, Aug. 2019, doi: 10.1016/j.dib.2019.104414.

[20] E. De Felipe Rendón *et al.*, "Coffee rust detection and recommendations module through deep learning algorithms," in *Proc.Congr. Estudiantil de Inteligência Artificial Aplicada a la Ingeniería y Tecnología*, UNAM, FESC, Estado de México, México, 2023.

[21] E. Hitimana *et al.*, "Revolutionizing coffee farming: a mobile app with GPS-enabled reporting for rapid and accurate on-site detection of coffee leaf diseases using integrated deep learning," *Software*, vol. 3, no. 2, pp. 146–168, Apr. 2024, doi: 10.3390/software3020007.

[22] A. Howard *et al.*, "Searching for MobileNetV3," in *Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV)*, 2019, pp. 1314–1324, doi: 10.1109/ICCV.2019.00140.

[23] M. Tan, R. Pang, and Q. V. Le, "EfficientDet: scalable and efficient object detection," in *Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR)*, 2020, pp. 10781–10790, doi: 10.1109/CVPR42600.2020.01079.

[24] A. T. Khan, S. M. Jensen, A. R. Khan, and S. Li, "Plant disease detection model for edge computing devices," *Front. Plant Sci.*, vol. 14, Art. no. 1308528, Dec. 2023, doi: 10.3389/fpls.2023.1308528.

[25] H. Aqasizade, M. Antonini, M. Vecchio, and F. Antonelli, "A TinyMLOps pipeline for coarse-grained plant disease classification in precision agriculture," *Sensors*, vol. 26, no. 16, Art. no. 5029, Aug. 2026, doi: 10.3390/s26165029.

[26] X. Wu, X. Fan, P. Luo, S. D. Choudhury, T. Tjahjadi, and C. Hu, "From laboratory to field: unsupervised domain adaptation for plant disease recognition in the wild," *Plant Phenomics*, vol. 5, Art. no. 0038, 2023, doi: 10.34133/plantphenomics.0038.

[27] ixrbhii, "Coffee disease ConvNeXt — model card," Hugging Face, `ixrbhii/coffee-disease-convnext`.

---

## Approval block

| Role | Decision | Signature | Date |
|---|---|---|---|
| Advisor (recommendation) | ☐ Recommend  ☐ Do not recommend | | |
| Coordinator / Committee | ☐ Approved  ☐ Approved with modifications  ☐ Rejected | | |

### Committee notes / modifications required

<br><br><br><br>

---

*Ethical screening checklist: Appendix M (attached).*
*Weekly progress log: Appendix B, maintained in the departmental Google Sheet.*
