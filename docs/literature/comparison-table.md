# Comparison of Related Systems (Guideline §5.5)

> **Requirement:** *"A comparison table must compare at least three directly comparable systems
> or studies on the same stated criteria, for example the problem addressed, method or
> technology, data, evaluation measures, results, strengths and limitations. The table supports
> the synthesis and does not replace it."*
>
> **Owner:** Nahom Solomon. **Verification:** every cell was checked against the primary source
> (GitHub REST API, the Hugging Face model card, the paper's Crossref record, or the arXiv
> record) on **21 October 2026**. Where a source publishes no metric, the cell says
> **"not reported"** — it does not guess. **Verification date and method are stated for each
> row**, which is itself a required table column under §11.6 ("give units in the column
> headings").

---

## Table 2.1 — Directly comparable deployed systems

**Stated criteria (identical for every row):**
1. Problem addressed and target user
2. Diagnostic classes covered
3. Method / technology
4. Training and evaluation data
5. Reported evaluation measures and results
6. Form factor and delivery
7. Offline operation
8. Agronomic guidance included
9. Diagnosis history / longitudinal record
10. Licences and availability
11. Principal strengths
12. Principal limitations

| # | Criterion | **This project (proposed)** | **A.** Manso *et al.* (2019) [11] + **Coffee Recognize** [12] | **B.** Brewguard / `FTsune/kape` [38] | **C.** Omdena São Paulo [13] | **D.** Hitimana *et al.* (2024) [21] | **E.** De Felipe Rendón *et al.* (2023) [20] |
|---|---|---|---|---|---|---|---|
| 1 | **Problem / user** | Coffee leaf disease diagnosis for smallholder farmers and extension officers, with treatment guidance | Coffee leaf miner and rust detection and severity quantification for coffee producers | Leaf-species identification plus coffee disease detection and GPS tracking for field and estate managers | 5-class coffee disease classification for the Brazilian coffee value chain | On-site coffee leaf disease detection with GPS reporting for Rwandan smallholders | Rust detection, infection-level prediction and treatment recommendations for coffee growers |
| 2 | **Classes** | **5** — Rust, Cercospora, Leaf Miner, Phoma, Healthy | **2** — Rust, Leaf Miner (+ severity) | 4 in code (Abiotic Disorder, Cercospora, Leaf Rust, Sooty Mold); README adds Algal Growth; Miner and Phoma **absent** | **5** — health, miner, rust, phoma, cercospora (exact match to ours) | 4 + GPS geotag; dense layer reported over four leaf classes | Rust vs healthy |
| 3 | **Method / technology** | MobileNetV3-Small / EfficientNet-Lite0 → int8 TFLite; Flutter; FastAPI; SQLite | TensorFlow Object Detection (frozen graph) + OpenCV + k-means; Ionic/Angular/TypeScript client | YOLO-v11 (leaf species + disease models); Streamlit; SQLite; GPS | Custom from-scratch Keras CNN (5 max-pool blocks, 32→256 filters, Dense 64, Dropout 0.5); Gradio + Streamlit | Xception, ResNet50, Inception-v3, VGG16, **DenseNet (best)**; mobile app | Deep learning classifier + rules; mobile application module |
| 4 | **Data** | 9 sources, 6 countries (Kenya, Brazil, Ecuador, Uganda, Peru, Colombia, plus Ethiopia field set); ≥58k images; **leakage-safe grouped split** | Project-collected *Coffea arabica* images (Brazil) | Not named in the README; no dataset card or licence in repo | BRACOL "Symptoms" subset, 2,722 images, 70/15/15 | 37,939 images from 5 districts in Rwanda; **"available on request"** — not openly downloadable | Small diseased/healthy leaf set (unstated size) |
| 5 | **Reported measures** | *To be produced:* macro-F1 + per-class recall on internal **and 5 external** datasets, ECE, selective risk, coverage curve, latency, memory, model size, SUS | 81.5 % average precision; severity accuracy 38.9 % at IoU 0.50 (Tukey test, 5 %) | **NOT REPORTED** — no accuracy, precision, recall or mAP anywhere in the repo | **NOT VERIFIABLE** — the notebook calls `classification_report` but the saved executed outputs do not contain the printed report | DenseNet training accuracy 99.57 % on four classes (abstract only) | **58 %** accuracy on diseased leaves; student congress, no DOI, not peer-reviewed |
| 6 | **Form factor** | Android/iOS mobile app (offline) + REST API + web client | Mobile app (Android/iOS) | Web app (Streamlit, cloud-hosted); live demo now behind a login | Web app (Gradio + Streamlit notebooks) | Mobile app with GPS reporting | Mobile application module |
| 7 | **Offline operation** | **YES** — on-device TFLite; core flow needs no network | **NO** — the app delegates inference to `Coffee_Recognize_API` (54 MB frozen graph on a server) | **NO** | **NO** | Not stated; no artefact implies offline operation | Not stated |
| 8 | **Guidance** | Sourced KB per class: symptoms, severity cues, organic + chemical control, prevention — FAO Ch. 9, Berihun & Alemu, Yirga; **JARC-reviewed** | No treatment guidance | Disease information pages per disease | No treatment guidance | Not stated | **YES** — treatment and prevention recommendations (unsourced) |
| 9 | **History** | **YES** — local SQLite, searchable by class and date, CSV export | No | **YES** — disease-tracking module + SQLite | No | Not stated | No |
| 10 | **Licence / availability** | To be released under a licence chosen with the advisor; all data CC BY 4.0; source code in the group repository | App repo: GPL-2.0 per the GitHub API (**README badge says GPL-3 — internally inconsistent**); research repo: **no licence file**; API repo: MIT per the API, **`package.json` says ISC** — three-way inconsistency | **NO LICENCE FILE** — GitHub API `license: null` | MIT (code); **contains no images** | MDPI article CC BY 4.0; code not identified | No repository identified |
| 11 | **Strengths** | Only five-class offline phone system located; only one with sourced guidance + history; only one with external field-photo evaluation and calibration; complete end-to-end deliverable | Real field deployment; severity quantification; patents; longest-lived artefact (2019→2026) | Richest feature set (species + disease + GPS + tracking + batch); accessible UI | Correct five-class taxonomy; Mixup augmentation; documented notebook | GPS geo-tagging adds epidemiological value; five architectures compared | Closest prior art on *guidance*; honest low accuracy |
| 12 | **Limitations** | External performance is expected to be modest; must be reported honestly. Guidance is advisory, not a substitute for an extension officer. Trained largely on non-Ethiopian imagery | **2 classes only**; requires connectivity; server-side 54 MB graph; severity accuracy 38.9 %; licence ambiguity | **Miner and Phoma missing**; **no metrics at all**; no licence; demo gated | **Cloud-only**; no usable metrics; no image data in the repo; not a system | No offline claim; no open dataset; abstract-only reading; not peer-reviewed at source | 58 % accuracy; unpeer-reviewed; no dataset; no offline claim |

---

## Table 2.2 — Directly comparable published model artefacts (offline-capable)

**Purpose of this second table.** Rows A–F above are *systems*. These two are *deployable model
artefacts*, and they are the closest competitors to the technical heart of this project because
they are the only published coffee models that can actually run on a phone.

| # | Criterion | **`ixrbhii/coffee-disease-convnext`** [27] | **`ConnorLee08/coffee-leaf-efficientnet-b2`** [14] | **This project (proposed)** |
|---|---|---|---|---|
| 1 | Architecture | ConvNeXt-Small (`convnext_small.fb_in22k_ft_in1k`), timm | EfficientNet-B2 (`timm/efficientnet_b2.ra_in1k`) | MobileNetV3-Small **and** EfficientNet-Lite0 (compared) |
| 2 | Classes | **7** — Berry Blotch, Cercospora, Healthy, Leaf Miner, Phoma, Red Spider Mite, Rust | **8** — Cercospora, Healthy, Leaf miner, Phoma, Rust, Red spider mite, Weevil damage, **Unsupported** | **5** — Rust, Cercospora, Leaf Miner, Phoma, Healthy |
| 3 | Artefact | Safetensors F16, **99 MB**, 49.5 M params, 224×224 | Safetensors F32 **+ `model.tflite` 8.57 MB**, 7.78 M params, 224×224 | float32 / float16 / **int8 TFLite**, ≤10 MB target, 224×224 |
| 4 | Training data | LeafNet + the authors' own field photos | 9 sources, 20,311 prepared images + 5,294 validation | 9 sources (6 countries), leakage-safe grouped split |
| 5 | **Internal** results | 94.7 % test accuracy, macro-F1 0.809, 506 held-out photos | 94.09 % raw accuracy, macro-F1 0.8720, 95.14 % accepted accuracy @ 79.52 % coverage, 98.1 ms mean response, 5,868-image test set | To be reported: macro-F1 ± sd over ≥3 seeds, identical pipeline for all models |
| 6 | **Per-class** | Leaf Miner 100 % / F1 1.000 · Phoma 97.8 % / 0.978 · Rust 92.7 % / 0.949 · Healthy 99.3 % / 0.980 · Red Spider Mite 92.9 % / 0.812 · Berry Blotch 92.3 % / 0.774 · **Cercospora 9.1 % / 0.167** | Cercospora 0.717 (231) · Healthy 0.947 (318) · Leaf miner 0.955 (1,253) · Phoma 0.891 (677) · Rust 0.954 (2,267) · **Red spider mite 0.540 (26)** · Weevil 0.976 (894) · Unsupported 0.998 (202) | To be reported per class on internal **and every external** dataset |
| 7 | **External** results | "Test photos come from the same datasets the model learned from, so real field photos score lower" — **no external numbers published** | **16 of 847 external rust images correctly accepted (1.9 %)**; 177 wrong acceptances; 654 rejections. B0 16.9 %, B1 2.6 %, B3 6.1 %. External scan set (100 scans): B2 raw accuracy **12.0 %**, 11.2 % accuracy among accepted; B0 27.0 %/16.4 %, B1 44.0 %/34.5 %, B3 42.0 %/44.4 %. AUROC 0.778 for B2 | **5 external field datasets**, per-class and per-dataset, with bootstrap CIs, the abstention coverage curve, and a paired significance test |
| 8 | Offline | Yes (portable file) but no TFLite export and no app | **Yes** — 8.57 MB TFLite; "No credentials or network access are required" | Yes, plus guidance and history |
| 9 | Guidance / history | Neither | Neither | Both |
| 10 | Licence | CC BY-4.0 | Component-specific upstream licences (Apache-2.0 for B1–B3) | To be chosen with the advisor |

---

## Table 2.3 — Research-method comparison (the studies that set the evaluation standard)

| Study | Data | Split protocol | External test? | Metric emphasis | Key finding | Limitation of its evidence |
|---|---|---|---|---|---|---|
| Baht *et al.* [7] | JMuBEN + JMuBEN2, 58,555 | Undersampled to 6,572/class, random 80/20, 100×100 | **Yes, but compromised** — the external set's 5th class was filled with training images to balance it | Accuracy, per-class metrics, 11 architectures | Best model 99 %; external 98 % | The external test is not independent; the balancing step is undisclosed in the headline |
| Ardah *et al.* [6] | BRACOL | 70/30 stratified, MATLAB | No | Accuracy, precision, recall, F1, ROC | GoogLeNet+ResNet18 fusion + PCA + SVM = 99.78 % | **No split-leakage control** and BRACOL's symptom crops leak across a naive split; proprietary MATLAB; code has hard-coded Windows paths |
| Ayikpa *et al.* [8] | JMuBEN | Not fully specified in the abstract | No | Accuracy, precision, recall, F1 | 97.37 % hybrid DL+ML | Protocol not reproducible from the accessible record |
| Novtahaning *et al.* [9] | Arabica dataset (Esgario) | Not specified | No | Accuracy, F1 | 97.31 % with a 3-model ensemble | No external evaluation; no leakage control |
| Xiang *et al.* [42] | PlantVillage → PlantDoc | Standard splits | **Yes, rigorously** | Accuracy collapse, **ECE**, **selective risk**, AUROC, mitigation ablation | **67.7 pp collapse with confidence steady at 79.76 %**; DANN *degraded* accuracy to 0.252 | Not coffee-specific; no phone deployment |
| Wu *et al.* [43] | PlantVillage → PlantDoc/C-PD | Standard splits | Yes | Mean accuracy, self-supervision vs adversarial | MSUN 56.06 % vs DSAN 42.87 % | Not coffee; laboratory→field, not curated→field |
| Barbedo [41] | Review | — | — | Failure-mode taxonomy | Background, lighting and multi-symptom leaves dominate field error | Predates modern architectures |

---

## What the comparison establishes (synthesis, not summary)

1. **The class taxonomy is settled; the delivery is not.** The five classes match JMuBEN exactly
   and match the Omdena system exactly — yet Omdena is a cloud-hosted notebook with no usable
   metrics, while the two mobile apps cover two classes and require a server. The literature has
   settled *what* to classify and has not settled *how to deliver it offline*.
2. **The two artefacts that could compete technically are the two that fail in the field.**
   ConvNeXt-S has 99 MB and 9.1 % Cercospora recall; EfficientNet-B2 has 8.57 MB and 1.9 %
   external rust acceptance. Neither reports an abstention threshold or a coverage curve as a
   headline metric — though the B2 card does compute accepted-accuracy and coverage, which this
   project adopts.
3. **The applied literature cannot serve as a baseline because it publishes no baselines.**
   Rows B–F report "not reported" or "not verifiable" for their primary metric. Any claim of
   the form "our system improves on X" would be unfounded. The defensible comparisons are
   against (a) the majority-class and transfer-learning baselines this project trains itself,
   and (b) the two published model artefacts, both re-run on our splits.
4. **The evaluation standard exists and is not being met.** Xiang *et al.* [42] demonstrate the
   methodology this project adopts — external shift, calibration error, selective risk, and an
   explicit ablation including interventions that fail. Nobody has applied it to coffee.
5. **Therefore the contribution is measurable and specific:** offline operation across the full
   five-class taxonomy, with sourced guidance and history, evaluated with the field-shift
   methodology that the plant-disease literature has established but the coffee literature has
   not applied.

---

### Verification ledger

| Row | Primary source consulted | Verification method | Date | HTTP |
|---|---|---|---|---|
| A | `github.com/Lucs1590/Coffee_Recognize`, `github.com/Lucs1590/coffee-phytopathology-detection`, `github.com/AlvaroCavalcante/Coffee_Recognize_API`, arXiv:1904.00742 | GitHub REST API + raw README + arXiv API | 2026-10-21 | 200 |
| B | `github.com/FTsune/kape` (renamed from `Coffee-Leaf-Classification-Disease-Detection`) | GitHub REST API + raw `app.py`, `diseases.json`, `leaves.json` | 2026-10-21 | 200 (old path redirects) |
| C | `github.com/dimitramuni/Coffee-Disease-Identification-Omdena` | GitHub REST API + README + notebook outputs | 2026-10-21 | 200 |
| D | doi:10.3390/software3020007 | Crossref record + abstract field (publisher page returns 403) | 2026-10-21 | Crossref 200 |
| E | UNAM CEIAT 2023 proceedings PDF | Direct PDF fetch, text extracted | 2026-10-21 | 200 |
| ConvNeXt | `huggingface.co/ixrbhii/coffee-disease-convnext` | Model card fetch, per-class table read verbatim | 2026-10-21 | 200 |
| EfficientNet-B2 | `huggingface.co/ConnorLee08/coffee-leaf-efficientnet-b2` | Model card fetch, external tables read verbatim | 2026-10-21 | 200 |
| Studies | Crossref / arXiv / PubMed records; peerj.com and frontiersin.org full texts where reachable | 38 DOI lookups + 4 full texts | 2026-10-21 | mixed — see `references.md` for per-item status |
