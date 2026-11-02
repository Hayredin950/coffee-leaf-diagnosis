# Chapter 1 — Introduction

> **Formatting (Guideline §11):** Times New Roman 12 pt, 1.5 line spacing, justified, A4, with
> 1.25 in left / 1.00 in other margins. Chapter titles are centred major headings in 14 pt
> bold capitals. Section headings 13 pt bold; sub-headings 12 pt bold. No heading deeper than
> the third order. Tables and figures are numbered per chapter — Table 1.1, Figure 1.1 — with
> the caption below a figure and above a table, and every one is referred to in the text.
> **Figures must be drawn by the group or credited at the end of the caption.**
>
> **Owner:** Nahom Solomon · **Estimated length:** 4–5 pages

---

## 1.1 Background

Coffee is the primary source of export revenue for Ethiopia and underpins the livelihoods of a
large rural population. Production is, however, constrained by a small number of foliar
diseases. Coffee leaf rust (*Hemileia vastatrix*), Cercospora leaf spot (brown eye spot,
*Cercospora coffeicola*), coffee leaf miner (*Leucoptera coffeella*) and Phoma leaf spot (brown
leaf spot, *Phoma costarricensis*) are among the most economically significant [1]–[4]. Field
surveys across south-western Ethiopia recorded a mean leaf rust incidence of 35.3 % and a
severity of 9.09 %, with altitude identified as the dominant driver of epidemics [58]. The
consequence is that **detection, rather than treatment, is the binding constraint** on yield
loss: by the time a farmer recognises the problem, the window for inexpensive early
intervention has closed [2], [3].

Two features of the diagnosis problem are worth stating precisely, because they determine the
design of any system intended to address it. The first is that the agronomic services able to
provide a diagnosis are concentrated in district and regional offices, so a farmer in a remote
coffee-producing kebelle may wait days or weeks for a visit. The second is that the four target
conditions are distinguished less by colour than by *pattern* — rust's powdery yellow-orange
pustules on the leaf underside, Cercospora's concentric brown "eye" lesions, Phoma's pale
circular necrotic patches and leaf miner's serpentine mines [4], [5]. Informal diagnosis is
error-prone even where a knowledgeable person is available.

Computer-vision models for coffee leaf disease have advanced rapidly. Convolutional models
trained on the JMuBEN and BRACOL corpora report in-domain accuracies in the mid- to high-90 %
range [6]–[10]. Two structural limitations of this literature motivate the present work.

The first is **deployment**. Most published coffee leaf disease classifiers exist as research
artefacts: a notebook, a Streamlit or Gradio page, or an application that calls a remote
inference server. The two published mobile applications identify only two diseases and require
network connectivity to reach a server-hosted model [11], [12]; the five-class web
applications run on cloud-hosted Streamlit or Gradio infrastructure [13]. None operates
offline, which is exactly the condition under which a farmer in a remote kebelle most needs
it.

The second limitation is **generalisation**, and it is more consequential. When models trained
on curated datasets are tested on field photographs, performance can collapse. A published
coffee-leaf EfficientNet-B2 model reports 94.09 % internal accuracy while correctly accepting a
rust diagnosis on only **16 of 847 (1.9 %)** external field rust images [14]. Independently, a
2026 benchmarking study of plant-disease classifiers reported a **67.7 percentage-point**
accuracy drop when moving from PlantVillage to PlantDoc field imagery, while the model's mean
confidence stayed at 79.76 % [15] — the model remained confidently wrong. The canonical
analysis of why plant-disease deep learning underperforms in the field identified background
clutter, uncontrolled illumination and the co-occurrence of multiple symptoms on a single leaf
as the dominant causes [16]. The conclusion across this evidence is that a coffee leaf disease
classifier validated only on curated imagery cannot yet be trusted by a farmer.

This project therefore targets a complete, offline, farmer-facing system whose central research
contribution is a rigorous answer to the question: *how accurately does a resource-constrained
coffee leaf disease classifier perform on real field photographs, and can that gap be narrowed
by methods that fit a low-end phone?*

### 1.1.1 Figure 1.1 — the three-stage response of the system

> **Figure 1.1** — The diagnosis flow: an image is acquired, classified on-device with a
> confidence check, and only then resolved against a knowledge base to produce an actionable
> result. The confidence check (the amber node) is what allows the system to decline to
> diagnose rather than to guess. Original work by the group.

---

## 1.2 Problem statement and gap

### 1.2.1 The existing condition and the affected stakeholders

Smallholder coffee farmers in Ethiopia's major producing regions — Jimma, Illubabor, Kaffa,
Bench, Shebelle and Welega, and the Sidama and Guji highlands — depend on early detection to
avoid crop loss and unnecessary chemical expenditure [2], [3]. Extension officers and the
plant pathologists of the Ethiopian Institute of Agricultural Research's Jimma Agricultural
Research Center (JARC) provide diagnosis, but their coverage falls far short of the number of
producing households.

Three stakeholder groups are affected differently. **Farmers** need an immediate diagnosis at
the point of the plant and guidance on what to do about it. **Extension officers** covering
many sites need a triage and record-keeping tool that works across a district, including where
there is no connectivity. **Plant pathologists at JARC** need field observations aggregated for
surveillance — a data type that does not currently exist at field scale, because a paper record
in an office is all that is currently produced.

### 1.2.2 Evidence that the problem exists

The group assembled four independent lines of evidence, three from the literature and one from
its own investigation.

1. **Agricultural evidence.** Rust epidemics in Ethiopia are well documented as severe and
   altitude-driven [5], with a dedicated review literature on Ethiopian rust status and
   management [2], [3].
2. **Deployment evidence.** Both published mobile applications delegate inference to a remote
   server [11], [12]; the five-class applications are cloud-hosted web applications [13]. A
   system requiring connectivity cannot serve its stated population.
3. **Generalisation evidence.** A published coffee-leaf model with 94.09 % internal accuracy
   achieves 1.9 % correct acceptance on external field rust images [14], and a
   controlled-to-field benchmark reports a 67.7-point accuracy collapse with uncalibrated
   confidence [15].
4. **The group's own investigation.** The group obtained direct access to the JMuBEN dataset
   from its originating author and independently confirmed that the released images are
   already cropped, resized and rotation/flip-augmented, with the original uncropped field
   photographs **not published**. The consequence is structural: a naive random split of this
   dataset leaks near-duplicate images between the training and test partitions and inflates
   the reported accuracy. The group further established that BRACOL's 2,147 symptom images are
   crops of its 1,747 whole-leaf photographs, and that RoCoLE provides four views of each of
   390 plants — so three of the four principal datasets contain duplication that a naive split
   would leak.

### 1.2.3 Shortcomings of current approaches

**Table 1.1** — The shortcomings of current approaches and their consequences for the
stakeholders named above.

| Shortcoming | Consequence for the farmer | Consequence for the extension officer | Consequence for JARC |
|---|---|---|---|
| Cloud and API dependence | The tool is unavailable in exactly the low-connectivity areas that need it | Offline visits produce no record | No field data reaches the institute |
| Heavy models (ConvNeXt-S ≈ 99 MB) | Impractical on a low-end phone; heavy data use | Cannot be distributed to officers | — |
| No agronomic guidance layer | A label is not an action; the farmer still does not know what to do | Must repeat the same advice at each site | — |
| No longitudinal record | Disease progression cannot be tracked | Progress between visits is unmeasured | No surveillance data |
| Validation on curated imagery only | The reported accuracy does not reflect the field | False confidence in the tool's output | Cannot judge field reliability |
| No uncertainty handling | A confident misclassification is presented as a diagnosis | The officer cannot tell a guess from a finding | Misdiagnosis is attributed to the system |

### 1.2.4 The gap

> No published system provides a **five-class coffee leaf disease classifier** (Coffee Leaf
> Rust, Cercospora Leaf Spot, Leaf Miner, Phoma Leaf Spot, Healthy) that **(a)** runs fully
> offline on a low-cost mobile device, **(b)** delivers actionable agronomic guidance and a
> persistent diagnosis history, and **(c)** is evaluated against external field photographs
> with per-class recall, calibration error and an explicit abstention mechanism.

---

## 1.3 Motivation

The motivation reduces to one sentence: **coffee leaf disease in Ethiopia is detected late
because the diagnostician is far away, and the software that could close that distance
currently requires the connectivity that is missing.**

Three further motivations shape the design. First, the four target diseases have genuinely
different management, so a classifier that emits only a label leaves the farmer no better off
than the informal diagnosis they could already attempt. Second, smallholders operate low-cost
Android devices on metered data, which makes model size a design constraint rather than an
optimisation detail. Third, an offline system generates longitudinal field data that a cloud
system never sees — data the group can use to advance the generalisation research question.

---

## 1.4 Objectives

### 1.4.1 General objective

To design, implement and evaluate a lightweight, fully offline deep-learning system that
diagnoses five coffee leaf conditions from a photograph on a low-cost mobile device, delivers
agronomic treatment guidance, and maintains a local diagnosis history, and to quantify and
mitigate the generalisation gap of such a classifier on external field photographs.

### 1.4.2 Specific objectives

**Table 1.2** — The specific objectives, their measurable targets and the evidence that will
be produced for each. The "achieved" column is completed in Chapter 6, as Guideline §10.5
requires.

| ID | Specific objective | Measurable target | Evidence |
|---|---|---|---|
| SO1 | Curate and document a multi-source, leakage-safe coffee leaf image corpus covering Rust, Cercospora, Leaf Miner, Phoma and Healthy, with a published datasheet and split manifest | ≥ 58,000 labelled images across ≥ 4 independently licensed sources; 100 % of images assigned to a split by a documented duplicate-grouping rule; the datasheet and manifest published | Datasheet; `split_manifest.csv`; audit results E-01 |
| SO2 | Train and compare lightweight CNN architectures against at least one naive baseline under identical conditions | ≥ 3 models plus the majority-class baseline, mean ± sd over ≥ 3 seeded runs, macro-F1 on the internal test split | E-02; Chapter 6.2 |
| SO3 | Quantify the generalisation gap on ≥ 3 external field datasets and mitigate it with an acceptance threshold | External macro-F1 per dataset with the gap stated; a threshold such that ≥ 95 % of accepted diagnoses are correct, with the coverage reported alongside | E-03…E-07; Chapter 6.3–6.6 |
| SO4 | Implement on-device inference in a mobile application supporting camera capture and gallery upload | TFLite model ≤ 10 MB; median latency ≤ 500 ms, p95 ≤ 1,000 ms on a low-end device; all core features functional in airplane mode | E-08…E-11; Chapter 6.7–6.8 |
| SO5 | Implement the results and guidance experience: per-class confidence plus a structured agronomic knowledge base | 100 % of the five classes have a reviewed, sourced KB entry; the KB ships as an offline asset; the guidance renders within one tap | E-12…E-14; Chapter 5.4 |
| SO6 | Implement a persistent local diagnosis history with search, filtering and export | History survives restart; query by class and date range; CSV export; 100 % of diagnoses logged with the seven required fields | E-15…E-17; Chapter 5.5 |
| SO7 | Test and evaluate the complete system — functionally, for performance, for security and for usability — and report the result against every objective | ≥ 40 executed test cases with actual results and evidence; a SUS score from ≥ 10 participants; a traceability matrix with an achievement status per objective | Appendix F; Appendix E; Chapter 6 |

### 1.4.3 Research questions and hypotheses

Each research question links to an objective and has a defined method of answer.

**RQ1** (→ SO3). How large is the drop in macro-F1 when a coffee leaf classifier trained on
curated imagery is evaluated on external field photographs, and how does it vary by disease
class and by source dataset? *Method: the identical model, preprocessing and inference code
applied to five datasets; a per-class and per-dataset breakdown; bootstrap confidence
intervals.* **H1:** the drop is at least 20 macro-F1 points.

**RQ2** (→ SO3). Among augmentation strategy, calibration with abstention, and the inclusion of
an African-sourced field dataset in training, which improves external macro-F1 most per unit
of deployed model size? *Method: a controlled ablation, each variant trained with ≥ 3 seeds; a
McNemar test on paired predictions for the decisive comparison.* **H2:** adding the Uganda
field dataset together with field-realistic augmentation gains at least 5 external macro-F1
points at a deployed-size cost below 1 MB.

**RQ3** (→ SO3). How much does calibration reduce the miscalibration of the classifier on
external data, and what coverage does the resulting acceptance threshold retain? *Method:
temperature scaling fitted on the validation split; ECE and NLL before and after; the
acceptance-coverage and selective-risk curves on the external sets.* **H3:** the relative ECE
reduction is at least 30 % at a coverage of at least 60 %.

**RQ4** (→ SO4). What classification performance is achievable under a 10 MB model budget and a
1 s latency budget on a low-cost Android device? *Method: MobileNetV3-Small and
EfficientNet-Lite0 in float32, float16 and int8 post-training quantisation, measured on three
reference devices.*

**RQ5** (→ SO5). Can treatment guidance be delivered in a form that is both agronomically
defensible and comprehensible to a user without formal training? *Method: KB entries sourced
from FAO and peer-reviewed Ethiopian literature, reviewed by a JARC plant pathologist, then
checked during the usability session by a comprehension question.*

---

## 1.5 Scope and limitations

### 1.5.1 Scope

The system identifies **five** coffee leaf conditions — Coffee Leaf Rust, Cercospora Leaf Spot,
Leaf Miner, Phoma Leaf Spot and Healthy — from RGB smartphone photographs acquired by camera
capture or gallery selection. It classifies entirely on the device, presents the predicted
class with per-class confidence and a confidence-based recommendation to retake the photo,
resolves the prediction against an embedded agronomic knowledge base, and records the
diagnosis in a local, searchable database. A REST API and a web client expose the same model
and the same knowledge base for extension officers and for demonstration. The data are nine
independently licensed public corpora from six countries, all under CC BY 4.0.

### 1.5.2 Limitations

**Table 1.3** — The limitations of the project, stated explicitly.

| # | Limitation | Effect |
|---|---|---|
| L1 | The diagnostic scope is restricted to five classes and to coffee leaves | No nutrient deficiencies, pests (other than as an explicit `unsupported` label), root, stem, cherry or soil diagnosis, and no other crops |
| L2 | The model classifies visible symptoms only | It cannot measure severity, cannot see the whole plant, and cannot detect pathogens below the visible-symptom threshold |
| L3 | Accuracy degrades under direct glare, deep shadow, motion blur, occlusion and non-typical backgrounds | Mitigated by a photo-quality gate and by confidence abstention, not eliminated |
| L4 | The training corpus contains no Ethiopian field imagery | The reported field performance is measured on African, South American and Ecuadorian data; Ethiopian performance may differ |
| L5 | No public field corpus contains Cercospora | Field performance for that class is essentially unmeasured and is reported as such |
| L6 | The evaluation quantifies a generalisation gap that this project does not fully close | The external macro-F1 in Chapter 6 is the honest measure of likely real-world usefulness |
| L7 | The diagnosis history is stored on the device and is not automatically synchronised | Synchronisation is a user-initiated export in this version |
| L8 | The guidance is decision support, not a prescription | It summarises published recommendations and directs the user to a qualified extension officer; it names active-ingredient classes rather than products or dosages |
| L9 | Labels in six of the eight sources carry no annotator-agreement statistic, and the strongest source uses a single expert | Ground-truth uncertainty is unquantified, which is an additional reason for reporting per-class metrics and an error analysis |

---

## 1.6 Significance

**For farmers.** A farmer in a remote kebelle can photograph an affected leaf and receive, in
seconds and without signal or data cost, a probable diagnosis with guidance on what to observe
and what action to take. Early identification shortens the window between infection and
response, the decisive factor in rust management [2], [3], [5].

**For extension officers.** The system produces structured, timestamped observation records —
a surveillance input that does not currently exist at field scale. Because it works offline, an
officer can work through a district without connectivity and synchronise later.

**For JARC and the research community.** The project publishes a leakage-safe split protocol and
an external-evaluation methodology for coffee leaf disease, together with an honest,
quantified account of the curated-to-field generalisation gap. Given the documented 1.9 %
external rust recall of an existing published model [14] and the 67.7-point collapse reported
in the wider plant-disease literature [15], an independent, reproducible measurement is of
clear value.

**For the Department.** Coffee is a national priority sector and JARC is a local institution.
A validated, open-source, offline diagnostic tool is a deliverable that outlives the project.

---

## 1.7 Organisation of the report

**Chapter 2** presents the literature review: a thematic synthesis of the coffee leaf disease
datasets, model-accuracy literature, deployed applications, on-device modelling, generalisation
evidence and agronomic treatment sources, together with a comparison table and an explicit gap
statement. **Chapter 3** sets out the methodology, the tools, the data, the work plan and the
risk management. **Chapter 4** presents the requirements analysis and the system design,
including the architecture, the models, the database and the user interface. **Chapter 5**
describes the implementation. **Chapter 6** presents the testing, the evaluation against each
objective, the traceability matrix and the limitations. **Chapter 7** concludes the report with
a summary against the objectives, the contributions, the limitations and the recommendations
for future work.

---

*Figures and tables to produce: Figure 1.1 (the diagnosis flow); Table 1.1 (the shortcomings);
Table 1.2 (the objectives); Table 1.3 (the limitations).*
