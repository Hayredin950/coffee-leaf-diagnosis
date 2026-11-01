# Chapter 2 — Literature Review and Related Work

> **Note on how to use this chapter.** Guideline §5.4 requires *critical synthesis organised by
> theme*, not a source-by-source summary, ending with an explicit gap statement. Each section
> below is a theme; within it, the sources are grouped, compared, and judged. Every claim carries
> an IEEE reference number matching `references.md`. **Nahom Solomon owns this chapter;
> Hayredin Mohammed co-owns §2.2 (model accuracy) and §2.5 (generalisation); Bemnet Tesfaye
> co-owns §2.4 (deployment).**

---

## 2.1 Datasets for coffee leaf disease recognition, and why the obvious split is wrong

### 2.1.1 The available corpora

Six open datasets dominate the coffee leaf disease literature, and this project uses all of them.

**JMuBEN and JMuBEN2** [1] are the field's primary resource: 58,549–58,555 Arabica (*Coffea
arabica*) leaf images across five classes — Cercospora, Rust, Phoma, Miner and Healthy —
collected at the Mutira coffee plantation in Kirinyaga County, Kenya, using a Fujifilm X-T4
camera, with labels assigned by a plant pathologist. The dataset is published as two Mendeley
records under CC BY 4.0: `t2r6rszp5c` (Rust, Cercospora, Phoma) and `tgv3zb82nd` (Miner,
Healthy). A machine-readable mirror on Hugging Face reports the per-class distribution as
Cercospora 7,681, Healthy 18,983, Leaf_rust 8,336, Miner 16,978, Phoma 6,571 — 58,549 in total,
six fewer than the paper's stated 58,555. The group will record the count it actually observes
and cite the discrepancy.

**BRACOL** [5] is the second pillar: 1,747 whole-leaf photographs plus 2,147 cropped symptom
images, captured with five different smartphones under partially controlled conditions in
Espírito Santo, Brazil, with expert labelling and severity bands computed from segmentation
masks.

**RoCoLe** [19] is the only *Robusta* corpus: 1,560 images from 390 plants (four views each),
smartphone-captured in Ecuadorian field conditions, with segmentation and severity
annotations and rust split into four severity levels.

Three further datasets have been verified as usable and are additional to the original plan:
a 2025 Ugandan corpus of 3,312 images covering Healthy, Rust and Phoma collected on Ugandan
farms [28]; a 2026 Peruvian corpus of 1,500 balanced images of Healthy, Rust and *Mycena
citricolor* with a uniform capture protocol and specialist diagnosis [29]; and CoffeeLeaf-CO
v2.0.0 from Colombia, a detection dataset of 2,315 field images with 12,794 annotated instances
of rust, coffee weevil and leaf miner, released with a SHA256-verified split [30]. A smaller
full-resolution Brazilian set of 542 smartphone images at 4000×2250 [31] is retained as a
high-resolution spot-check set.

### 2.1.2 The shared methodological flaw

All six corpora share a structural property that the literature rarely confronts: **the released
images are not independent samples.** JMuBEN's dataset card states that images were "cropped to
emphasize the region of interest", resized for uniformity, and "augmented" — the paper specifies
rotation through 180° in both planes plus horizontal and vertical flipping — with the original
uncropped field photographs **not published** [1]. BRACOL's symptom images are, by construction,
crops of the 1,747 whole-leaf photographs [5]. RoCoLe provides four views of each of 390
plants [19]. CoffeeLeaf-CO deliberately removed RoCoLe images from its own release specifically
to keep RoCoLe usable as an independent external set [30].

This has a direct, checkable consequence: a randomly shuffled split places images that are
rotations, flips or crops of the same physical leaf in both the training and the test partition.
The published accuracies on JMuBEN — 99 % [7], 97.37 % [8], 97.31 % [9], 99.72 % [10] — are
therefore upper bounds on field performance, not estimates of it.

### 2.1.3 What the evidence shows as a whole

Taken together, the datasets are adequate in volume and coverage but poorly matched to the
deployment target: only one corpus (RoCoLE) is from a species other than Arabica, one (Uganda)
is from a second African coffee-growing country, and none is Ethiopian. Two of the four target
diseases — Cercospora and Phoma — appear in *no* external field corpus, which means no
independent measurement of field performance for those two classes is currently possible from
public data alone. This is a limitation this project states explicitly rather than works around.

## 2.2 Model accuracy on curated imagery: high, consistent, and not comparable

### 2.2.1 The reported figures

The literature's headline results are strikingly consistent. Baht *et al.* [7] trained eleven
architectures on JMuBEN with balanced classes (6,572 per class), and every model landed between
93 % and 99 %; their from-scratch CNN1 reached 99 %. Ayikpa *et al.* [8] combined deep and
classical learning on JMuBEN for 97.37 %. Novtahaning *et al.* [9] ensembled VGG-16, ResNet-152
and EfficientNet-B0 for 97.31 %. Venkatraman *et al.* [10] reported 99.72 % with EfficientNet-B0.
Ardah *et al.* [6] reached 99.78 % on BRACOL through GoogLeNet–ResNet18 feature fusion, PCA to
99 % variance and an RBF-kernel SVM. Elezmazy *et al.* [32] reported 97 % with MobileNetV3 on
JMuBEN, and Binney and Ren [33] reported 99.36 % for a fine-tuned VGG19 on JMuBEN2.

### 2.2.2 Why these figures cannot be compared with each other

Critically, the studies do **not** share an evaluation protocol, and the differences are large
enough to make the numbers non-comparable:

- **Different splits and class balances.** Baht *et al.* [7] deliberately undersampled to
  6,572 per class, discarding roughly two-thirds of the data, while Elezmazy *et al.* [32] used
  the full distribution, in which Healthy is 2.9× more frequent than Phoma.
- **Different image sizes.** 100×100×3 in [7] against 128×128 in the JMuBEN release and 256×256
  in [6] and [13].
- **Different tasks.** Classification in [7]–[10] versus *detection* in the BRACOL-YOLO work
  [34] and CoffeeLeaf-CO [30], whose mAP figures are not comparable to accuracy.
- **Different augmentation.** [7] applies flips, 20° affine rotation, ×1.2 brightness and
  Gaussian blur σ=1.0; [6] applies none of these; [13] applies mirroring, rotation, colour
  jitter *and* Mixup.
- **Almost no external testing.** Only [7] reports an external test, and it is compromised:
  the fifth class of that external set was populated with training images to balance it.

**Judgement.** The gap between 93 % and 99.78 % in this literature is not a meaningful
scientific spread; it is mostly protocol variation. Treating any of these as a "state of the
art benchmark" to beat would be a methodological error. A defensible comparison requires an
identical pipeline, an identical split, and an identical evaluation set — which is precisely
what this project establishes, and what §2.6 of Chapter 6 will report.

### 2.2.3 What the evidence shows as a whole

Deep learning clearly works on curated coffee leaf imagery; every credible architecture
reaches the mid- to high-90s. But the literature's headline number is uninformative about the
question a farmer actually cares about, because it measures performance on data whose
collection process resembles the training data. The real question is not "can a CNN classify
coffee leaves?" but "does a CNN classify coffee leaves taken by a farmer, in a field, with a
₹2,000 phone?" — and this literature is not designed to answer it.

## 2.3 On-device deployment: a solved engineering problem that coffee disease has not used

### 2.3.1 The enabling technology

MobileNetV3 was produced by hardware-aware neural architecture search explicitly targeted at
phone CPUs [22], and EfficientNet-Lite is Google's mobile-oriented variant of EfficientNet,
documented in the EfficientDet paper [23] and released with the measured claim that the
integer-only quantised EfficientNet-Lite4 achieves 80.4 % ImageNet top-1 accuracy at 30 ms per
image on a Pixel 4 CPU. The plant-disease literature has already demonstrated the specific
translation this project needs: MobileNetV3-Small for edge plant-disease classification
reached 99.50 % on PlantVillage's 38 classes while post-training quantisation shrank the model
from 1.5 M to 0.93 M parameters with **no accuracy loss** [24]. A 2026 TinyMLOps pipeline
exported to LiteRT with mixed-precision float fallback and measured an F1 degradation of at
most 0.0073 on a single-threaded Raspberry Pi Zero 2 W [25]. A lightweight vision transformer
for mobile plant-disease identification reported 85.4 % on a coffee dataset [35].

### 2.3.2 The gap between capability and coffee-disease practice

The tooling is mature and the target is achievable. Yet none of the coffee leaf disease
publications reviewed here reports a deployed, quantized, phone-resident artefact together with
measured on-device latency and memory. The paper closest to the target — Waldamichael *et al.*
[4] — is explicitly "for use on smartphones" and uses HSV segmentation with transfer learning
for four classes, but reports no on-device measurements and no offline evaluation.

**What this shows.** The on-device engineering problem for coffee leaf disease is *unclaimed
rather than unsolved*. That is an opportunity, and it is a low-risk one: the tools exist, the
architecture is known, the risk is entirely in the group's own execution.

## 2.4 Existing coffee leaf disease applications: narrow, cloud-bound, and rarely measured

This section is the project's most important prior-art analysis, because it is where the
gap statement is earned.

### 2.4.1 The mobile applications

**Manso *et al.* [11]** built "a smartphone application to detection and classification of
coffee leaf miner and coffee leaf rust", with severity quantification, from the same Brazilian
research group that authored BRACOL. This is the closest published academic prior art and it
must be cited as such. Its successor, **Coffee Recognize** [12], is the most complete
deployment in the literature: an Ionic/Angular Android application performing TensorFlow Object
Detection with an 81.5 % average precision, with severity quantification at 38.9 % accuracy
under a 50 % IoU threshold [36]. Its backend is a Node.js REST API hosting a 54 MB frozen
TensorFlow graph [37]. The architecture is the point: **the phone is a thin client and the model
lives on a server**, so the system is unusable without connectivity.

**Hitimana *et al.* [21]** developed a Rwandan mobile application with GPS geo-tagging of
captured images, comparing Xception, ResNet50, Inception-v3, VGG16 and DenseNet, with DenseNet
scoring highest on the four leaf classes at 99.57 % training accuracy. **De Felipe Rendón
*et al.* [20]** at UNAM built a mobile module that detects rust, predicts the infection level
and delivers treatment and prevention recommendations — functionally close to this project's
proposal — but at 58 % accuracy, and published only in a student congress proceeding with no
DOI.

### 2.4.2 The web applications

**Brewguard** [38] is a Streamlit application using YOLO-v11 with leaf-species classification,
GPS tracking and a disease-tracking module; its public demo URL now redirects to an
authentication page. Its class set covers Leaf Rust, Cercospora, Algal Growth and Sooty Molds,
omitting Miner and Phoma. **The Omdena São Paulo chapter application** [13] is the only
five-class system located — healthy, miner, rust, phoma, cercospora — trained on the BRACOL
symptom subset with a custom CNN and Mixup augmentation, delivered as Gradio and Streamlit
notebooks. **The sleepypioneer predictor** [39] is a binary rust-versus-other Xception model
deployed as a TFLite Lambda behind API Gateway with a Streamlit front end. **Bharathlogs'**
application [40] adds pesticide recommendations to a YOLOv5 Streamlit app; its file layout is
identical to Brewguard's, indicating a re-upload rather than independent work.

### 2.4.3 A serious measurement problem in the applied literature

A finding that runs through this entire strand is that **most applied systems publish no
evaluation metrics at all**. Brewguard's repository contains no accuracy, precision, recall or
mAP figure. The Omdena notebook calls `classification_report` but the executed outputs saved in
the repository do not include the printed report. The sleepypioneer README contains no
accuracy number. Bharathlogs' README claims "high accuracy" with no figures and explicitly
leaves the dataset unspecified.

This is not a quibble. It means the applied literature cannot establish a baseline for this
project, because there is nothing to compare against. It also means that a project which *does*
measure honestly — external field-photo evaluation, per-class recall, calibration error, an
abstention threshold — is contributing something the applied literature has not.

### 2.4.4 The two offline model cards: the strongest available evidence

The two most relevant artefacts are Hugging Face model cards, and both are unusually candid.

**ConvNeXt-Small** [27] covers seven classes at 224×224 with a 99 MB F16 export, reporting
94.7 % test accuracy and macro-F1 0.809 over 506 held-out photos. Its own card warns that
"test photos come from the same datasets the model learned from, so real field photos score
lower", and its per-class table shows **Cercospora recall of 9.1 %** (1 of 11 test photos) and
F1 of 0.167 — the weakest class by a wide margin — while Leaf Miner reaches 100 % and Phoma
97.8 %. The card also carries an operational rule this project adopts: below about 45 %
confidence, ask for a better photo.

**EfficientNet-B2** [14] is the closest thing to a deployable artefact that exists: 8.57 MB
TFLite, 7.78 M parameters, eight classes including an explicit `Unsupported` label, with
accepted-accuracy and accepted-coverage as first-class metrics — an approach this project copies.
Its internal numbers are strong: 94.09 % raw accuracy, macro-F1 0.872, 95.14 % accepted
accuracy at 79.52 % coverage, 98.1 ms mean response. But its external evaluation is
catastrophic and the card says so plainly:

> "B2 correctly identified and accepted just **16 of 847 rust images (1.9 %)**. It accepted an
> incorrect supported diagnosis on 177 rust images and rejected 654."

Across four model variants on the same 847-image external rust collection, correct acceptances
ranged from 1.9 % to 16.9 %. On a 100-scan external set the same models achieved 12.0 % to
44.0 % raw accuracy. The card adds the caveat that these collections were inspected during
development and should be described as "development stress tests rather than newly blinded
field tests", and that "None of the four models is established as dependable for these external
imaging conditions."

### 2.4.5 What this shows as a whole

Across the applied literature there is a consistent, and uncomfortable, pattern: **in-domain
accuracy is high, external accuracy is unknown or catastrophic, and the deployed systems are
either cloud-bound or cover only a subset of the diseases.** The gap is not that nobody has
built a coffee leaf disease app. It is that no app simultaneously (a) covers the five-class
taxonomy, (b) runs offline, (c) carries agronomic guidance and history, and (d) is evaluated
against external field photographs with calibrated confidence.

## 2.5 Why curated-image accuracy does not survive the field

### 2.5.1 The mechanism

Barbedo's 2018 analysis [41] is the canonical explanation and remains the best account of why
plant-disease deep learning underperforms outside the laboratory: the presence of background
clutter, uncontrolled and varying illumination, the co-occurrence of multiple symptoms on a
single leaf, and the dominance of the leaf in frame are the dominant drivers of error, and
each of these is controlled or absent in curated datasets. Segmented-background datasets such
as PlantVillage do not represent the conditions in which a farmer's photograph is taken.

### 2.5.2 The measured size of the collapse

The magnitude is now quantified in three independent places.

**PlantVillage → PlantDoc.** Xiang *et al.* [42] measured a **67.7 percentage-point** accuracy
collapse with ResNet-50 while **mean confidence stayed at 79.76 %** — the model remained
confidently wrong, which is the worst possible failure mode for a farmer-facing tool. Their
temperature-scaling result was also unhelpful for deployment: ECE 0.3645, and at 80 %
coverage a selective risk of 64.30 %. Critically, they showed that the standard remedy
**backfires**: DANN-style adversarial adaptation *degraded* accuracy to 0.252, AdaBN to 0.321,
and feature moment matching to 0.366 — every one worse than the 32.3 % baseline. Their best
OOD detector was a DINOv2-S/14 linear-probe ensemble at AUROC 0.779.

**Laboratory → field, self-supervised.** Wu *et al.* [43] reported mean accuracy of 56.06 % for
a self-supervised MSUN model on PlantDoc against 42.87 % for the adversarial DSAN baseline.

**Coffee specifically.** The EfficientNet-B2 card's 1.9 % external rust acceptance [14] and the
ConvNeXt card's 9.1 % Cercospora recall [27] place coffee at the severe end of this spectrum.

### 2.5.3 What this means for system design

Three design consequences follow directly, and they shape this project's architecture:

1. **Abstention is a first-class feature, not a nicety.** A confidence threshold with a
   "retake the photo" path is not a UX detail; it is the mechanism that prevents the
   confidently-wrong failure mode from reaching a farmer who will act on it. Both prior model
   cards independently recommend it [14], [27].
2. **Calibration must be measured, not assumed.** A model that is 94 % accurate but
   overconfident is worse for decision support than a 90 %-accurate model whose confidence is
   meaningful. Hence ECE, selective risk and the acceptance-coverage curve are report metrics,
   not extras.
3. **Training data must be diversified deliberately, and domain adaptation applied with
   caution.** The evidence from [42] is that naive adversarial adaptation can make things
   dramatically worse. Field-realistic augmentation and adding field-sourced data to training
   are safer interventions and are what this project tests.

## 2.6 Agronomic knowledge for treatment guidance

The applied literature largely stops at the label. Of the systems reviewed, only the UNAM
module [20] and the sleepypioneer predictor's surrounding material attach any treatment
content, and the former's guidance is not sourced. For an Ethiopian deployment the usable
sources are agronomic rather than computational:

- **Berihun and Alemu [4]** review the status and management of coffee leaf rust in Ethiopia
  specifically — the primary source for rust management in the knowledge base.
- **Yirga [5]**, from Jimma Agricultural Research Center, reviews rust biology and management
  options in Ethiopian conditions.
- **The FAO Arabica coffee manual**, Chapter 9 [44], provides FAO-authored field guidance with
  symptom descriptions and preventive, chemical and traditional control measures for Cercospora
  leaf spot, coffee leaf rust, black sooty mould and anthracnose — an authoritative,
  citable, internationally recognised source.
- **Negesa *et al.* [45]** and **Belachew *et al.* [46]** provide Ethiopian field context on
  cultivar susceptibility and epidemic drivers.
- For disease *taxonomy*, the APS common-names list [47] provides the authoritative mapping
  between common names and pathogens.

Note for the record: the Ethiopian Coffee and Tea Authority website is currently unavailable
and serves unrelated content, and the Coffee and Tea Research Institute has no live site — the
relevant institutional expertise sits within EIAR and JARC. The knowledge base therefore cites
only sources that a marker can open, and the JARC review is the mechanism that grounds it in
Ethiopian practice.

## 2.7 Gap statement

Synthesising the five strands:

1. **The datasets are adequate but not split safely.** Six corpora with nine distinct sources
   provide ample data, yet all of them contain duplication structures that inflate a random
   split's apparent accuracy (§2.1).
2. **The reported accuracies are not comparable and are not field estimates.** Protocol
   variation dominates the 93–99.78 % spread (§2.2), and the field-performance evidence is
   unambiguously negative (§2.5).
3. **The deployment tooling is solved, but coffee disease has not used it.** Quantised
   MobileNetV3-scale models are established for plant disease generally (§2.3); the coffee
   literature has no measured on-device artefact (§2.3.2).
4. **The applied systems are narrow, cloud-bound and unmeasured.** Two-class mobile apps need a
   server; five-class web apps run on Streamlit; most publish no metrics at all (§2.4).
5. **The two models that ship offline models fail badly out of distribution** — 1.9 % external
   rust acceptance, 9.1 % Cercospora recall (§2.4.4) — and neither has been engineered for
   that failure.

> **Explicit gap.** No published system provides a **five-class coffee leaf disease classifier
> (Coffee Leaf Rust, Cercospora Leaf Spot, Leaf Miner, Phoma Leaf Spot, Healthy) that runs fully
> offline on a low-cost mobile device, delivers sourced agronomic treatment guidance and a
> persistent diagnosis history, and is evaluated on external field photographs with per-class
> recall, calibration error and an explicit abstention mechanism.**
>
> **Why this matters for the stakeholders.** Smallholder farmers and extension officers in
> coffee-producing regions of Ethiopia need diagnosis at the point of the plant, without signal
> and without data cost (§2.4.1 shows the only deployed mobile apps require a server). A
> classifier whose accuracy has never been measured in the field cannot safely be put in their
> hands, because the documented failure mode is a confidently wrong diagnosis, not a visible
> error (§2.5.2).
>
> **How this project responds.** (i) A **leakage-safe, source-diverse corpus** with a published
> datasheet and a reproducible split manifest (§2.1). (ii) **A quantified generalisation gap**
> across five external field datasets, reported per class and per dataset, with bootstrap
> confidence intervals and a significance test — converting the literature's observation into
> a measured result under a controlled protocol (§2.5). (iii) **An offline mobile application**
> with a quantised TFLite model, an embedded sourced knowledge base, and a local diagnosis
> history (§2.3, §2.6). (iv) **Calibration with abstention**, so that the system declines to
> answer when it does not know, and reports coverage alongside accuracy rather than hiding it
> (§2.4.4, §2.5.3). (v) **An honest evaluation**, in which a low external macro-F1 is reported
> as the central finding rather than concealed behind an in-domain number (§2.2.2).

---

### How this review shaped the design (Guideline §5.4, final requirement)

| Evidence | Design decision it produced |
|---|---|
| JMuBEN/BRACOL/RoCoLe duplication structures [1], [5], [19] | Duplicate-grouped splitting implemented *before* any preprocessing (NFR-09, `scripts/prepare_data.py`) |
| Protocol heterogeneity across accuracy studies [6]–[10], [32], [33] | All models evaluated under one identical pipeline; two external published baselines run on our splits (§9.1 of the proposal) |
| Efficiency-B2 card: accepted-accuracy + coverage as metrics [14] | Acceptance-threshold evaluation and the coverage curve become report metrics (SO3) |
| ConvNeXt card: 9.1 % Cercospora recall [27] | Per-class recall reported for every class on every dataset, not just macro averages (SO3) |
| Both cards: "below ~45 % confidence, ask for a better photo" [14], [27] | FR-09 abstention path, adopted directly from prior art |
| Xiang *et al.*: DANN degrades to 0.252; confidence stays 79.76 % [42] | No adversarial domain adaptation in this project; calibration and data diversification used instead, and calibration error is measured (SO3) |
| Barbedo: background, lighting, multi-symptom leaves [41] | Photo-quality gate in the app; field-realistic augmentation in training (SO4, SO3) |
| Mobile apps require a server [12], [37] | On-device inference is a hard architectural requirement, not an optimisation (SO4, NFR-04) |
| Omdena is the only 5-class system and it is cloud-hosted [13] | The five-class taxonomy is retained precisely because the applied literature leaves it open |
| Applied systems publish no metrics [38], [39], [40] | Evaluation rigour is positioned as a contribution (SO7) |
| FAO Ch. 9, Berihun & Alemu, Yirga [44], [4], [5] | Sourced, reviewed knowledge base; JARC review before inclusion (SO5) |

---

*Next: `comparison-table.md` (the §5.5 comparison table) and `references.md` (the IEEE list).*
