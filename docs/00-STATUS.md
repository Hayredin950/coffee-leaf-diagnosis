# Project Status Assessment

**Project:** Design and Development of a Coffee Leaf Disease Diagnosis System Using Deep Learning
**Institution:** Addis Ababa University, College of Natural and Computational Sciences, Department of Computer Science
**Advisor:** Surafiel Habib Asefa
**Assessment date:** 21 October 2026 (Week 1)
**Status:** 🟡 **Conditional approval — proposal revision pending**

---

## 1. Where the project actually stands

| Item | State | Evidence |
|---|---|---|
| Topic chosen | ✅ Done | Coffee leaf disease diagnosis |
| Title fixed by advisor | ✅ Done | "Design and Development of a Coffee Leaf Disease Diagnosis System Using Deep Learning" |
| Advisor conditional acceptance | ✅ Done | Advisor email of 10 Oct 2026 requiring a *complete working system*, revised scope, and a build+test plan |
| Revised proposal submitted | ❌ **Not done** | Blocking the approval gate (Guideline §4.5) |
| Group size justification | ❌ **Not done** | Group of 4 **requires High complexity** (Guideline §14.1, §2.4) |
| Ethical screening (Appendix M) | ❌ **Not done** | Required at the approval gate (§4.5, §15.4) |
| Weekly logbook | ❌ **Empty** | Sheet created, 32 rows, zero entries. Required weekly (§13.2) |
| Datasets identified | ✅ Done | JMuBEN/JMuBEN2, BRACOL, ROCoLE + 4 more verified |
| Author permission for full JMuBEN | 🟡 Requested, no reply | Email sent to Mr. Bayile Getu Taye |
| Literature review | ❌ **Not started** | Needs ≥15 sources + 3-system comparison table (§5.5) |
| Requirements baseline | ❌ Not started | Gate falls in FYP I weeks 5–7 (§7.3) |
| Design artifacts | ❌ Not started | FYP I weeks 8–13 |
| Repository / source code | ❌ Not started | Required by §8.4, and it is the main ICF evidence (§17.7) |
| AI-use disclosure (Appendix L) | ❌ **Not started** | Required with every report (§15.3). **Start today** — prior AI use is already substantial |

**Verdict:** The project is at the *topic concept* gate. Weeks 1–2 of the guideline's timeline
(Table 16.1: "Orientation and title selection, weeks 1 to 2") are exactly where you should be,
but the logbook and proposal must not slip past week 2.

---

## 2. Nine things that must be settled this week

### 2.1 Group size → you must argue **High complexity** (Guideline §14.1, Table 2.2)

> "A fourth member is allowed only for a project of high complexity that the Committee approves."

A group of three is the norm; four needs High complexity = *standard complexity + a substantial
research/data/algorithmic/systems challenge **or** a real external stakeholder with real data.*

**You have two real levers. Use both:**

1. **Real external data + real stakeholders.** Two stakeholders already exist in the record:
   - the JMuBEN author (Mr. Bayile Getu Taye) — you have an open data-sharing relationship;
   - the Ethiopian Coffee and Tea Administration / EIAR–Jimma Agricultural Research Center
     (JARC) Plant Pathology department — a real agronomy stakeholder for the treatment
     knowledge base.
2. **A genuine research challenge.** The field's own published model card shows a coffee-leaf
   EfficientNet-B2 model that scores **94.09 % internally but accepts a correct rust diagnosis
   on only 16 of 847 external field rust images (1.9 %)**. Separately, a 2026 benchmarking
   study found a **67.7 percentage-point accuracy collapse** on PlantVillage→PlantDoc field
   shift while mean model confidence stayed at 79.76 %. *Reproducing and explaining this
   collapse on coffee, then engineering a mitigation and measuring it, is a real research
   contribution.* Put that in the proposal as the primary research question.

### 2.2 Data leakage — the single largest threat to your mark

Three of your four datasets contain near-duplicate structure that a naive random split will leak:

| Dataset | Leakage mechanism | Correct split unit |
|---|---|---|
| JMuBEN / JMuBEN2 | Released images are **cropped, resized and rotation/flip-augmented** from a smaller original set | Group by original capture, or use perceptual-hash duplicate clustering |
| BRACOL | The 2,147 symptom crops are **crops of the 1,747 whole-leaf photos** | Group leaf ↔ its crops together |
| ROCoLE | 4 images per plant (`C##P##` filenames) | Group by plant ID |

Guideline §9.3: *"Split the data before any preprocessing that learns from it, and never tune on
the test set."* §9.3 also requires cross-validation on small datasets.

### 2.3 Correct your citation facts before they enter the report

These were verified against Crossref/Mendeley/Hugging Face APIs on 21 Oct 2026. Use these, not the
versions floating in your earlier notes:

| Item | Correct value |
|---|---|
| JMuBEN paper title | "Arabica coffee leaf images dataset for coffee leaf disease detection and classification" |
| JMuBEN paper | J. Jepkoech, D. M. Mugo, B. K. Kenduiywo, E. C. Too, *Data in Brief*, vol. 36, Art. 107142, 2021, doi:10.1016/j.dib.2021.107142 |
| JMuBEN (Rust/Cercospora/Phoma) | Mendeley `t2r6rszp5c` — https://data.mendeley.com/datasets/t2r6rszp5c/1 |
| JMuBEN2 (Miner/Healthy) | Mendeley `tgv3zb82nd` — https://data.mendeley.com/datasets/tgv3zb82nd/1 |
| ⚠️ The paper's "respectively" is **inverted** relative to the record titles | Cite the record IDs explicitly so a reviewer doesn't think you mislabelled |
| Image count | **58,549** (measured, Hugging Face mirror) vs 58,555 (paper). Record which one you used and why |
| BRACOL | https://data.mendeley.com/datasets/yy2k5y8mxg/1 (doi:10.17632/yy2k5y8mxg.1) — authors Krohling, Esgario, Ventura (UFES) |
| ⚠️ PeerJ cs-3386 cites BRACOL with the **RoCoLe** DOI | Do not propagate that error |
| BRACOL counts | 1,747 whole leaves + 2,147 symptom crops (Mendeley card) vs 2,722 (Omdena mirror). **Count the files yourself** and state which you used |
| The "edge" paper | *Smart Agricultural Technology*, vol. 4, Art. 100183, 2023, doi:10.1016/j.atech.2023.100183 — **not** Procedia Computer Science |
| PeerJ cs-3386 title | "Robust coffee plant disease classification using deep learning and **advanced feature engineering techniques**" |
| Ethiopian Coffee & Tea Authority site | `ethiocta.gov.et` is currently serving gambling spam. **Do not cite it.** Use EIAR / JARC instead |

### 2.4 Group of four → you need a **fourth** external test set, and you have four

Your best defence against the §2.1 "real data" claim is an evaluation that no prior system has.
Verified, downloadable, CC BY 4.0:

| Test set | Location | What it tests | Cannot test |
|---|---|---|---|
| **Uganda 2025** | Mendeley `k36wnd6knb` | Rust, Phoma, Healthy — **Africa**, different farms, smartphone | Cercospora, Miner |
| **RoCoLe** | Mendeley `c5yvn32dzg` v2 | Robusta (species shift), Ecuador, field | Cercospora, Phoma, Miner; has red spider mite → *unsupported class* |
| **Saposoa, Peru 2026** | Mendeley `mfpxg4y65r` v2 | Rust, Healthy + *Mycena citricolor* → *unsupported* | Cercospora, Phoma, Miner |
| **CoffeeLeaf-CO v2** | Zenodo `22756170` | Rust, Miner, healthy-as-background + weevil → *unsupported* | Cercospora, Phoma |
| **Silva 2020** (full-res 4000×2250) | Mendeley `vfxf4trtcg` v5 | Rust, Miner at full resolution | everything else |

**Do not use** the Kaggle "Metadata-Enhanced Coffee Disease Benchmark" (`itznolex`) as a test set —
it is a superset of JMuBEN+BRACOL+RoCoLE, so testing on it while training on those is
guaranteed leakage.

**Taxonomy warning:** *Mycena citricolor* ("ojo de gallo"), coffee weevil ("coco") and red spider
mite are **not** Cercospora, Phoma or Miner. Keep them as an explicit `unsupported` /
`out_of_taxonomy` label. Folding them into a disease class is the most common way this kind of
project produces silently wrong results.

### 2.5 AI-use disclosure — start the log **today**

Guideline §15.3 and Appendix L require a record of significant AI use: tool, version, date,
purpose, where used, and how the output was checked. The logbook + Appendix L are already
assessed for honesty, and §18.1 lists *"inability to explain substantial submitted work,
including AI-assisted work"* as a critical-failure condition.

A pre-filled starter log is at `docs/appendices/Appendix-L-AI-Disclosure.md`. Keep appending to it
every time you use an AI tool. The rule that keeps you safe: **never submit a single line of
AI-generated text or code that you cannot explain line-by-line.**

### 2.6 The novelty gap is real, and it is narrow

Verified prior art (GitHub API + Hugging Face model cards, 21 Oct 2026):

| System | Classes | Form | Offline? |
|---|---|---|---|
| Coffee Recognize (Lucs1590) | Rust + Miner | Ionic mobile app | **No** — needs `Coffee_Recognize_API` server |
| Manso et al. 2019 (arXiv:1904.00742) | Rust + Miner | Mobile app | Not stated |
| Hitimana et al. 2024 (MDPI) | 4 + GPS | Mobile app | Not stated |
| Brewguard / `FTsune/kape` | Rust, Cercospora, Algal, Sooty | Streamlit web | No |
| Omdena (dimitramuni) | **all 5** | Gradio/Streamlit | No |
| sleepypioneer | Rust vs other | Streamlit + AWS Lambda | No |
| `ixrbhii/coffee-disease-convnext` | 7 | HF model (99 MB ConvNeXt) | Yes | 
| `ConnorLee08/coffee-leaf-efficientnet-b2` | 8 | HF model + **8.57 MB TFLite** | Yes, but **1.9 % external rust recall** |

**Gap statement:** *No published system provides a five-class coffee leaf disease classifier
(Leaf Rust, Cercospora, Leaf Miner, Phoma, Healthy) that runs fully offline on a low-cost
mobile device and is evaluated on external field photographs. The offline models that exist
cover seven to eight classes and demonstrably collapse out-of-distribution; the two-class mobile
applications require network connectivity; the five-class web applications run on cloud
Streamlit/Gradio infrastructure.*

**But this gap statement is not enough on its own.** The instructor's point was that a *bunch of public
projects* already do the classifier half of this. That is true, and it is why the contribution cannot be
the classifier, the datasets, the split or the abstention. It has to be what the system does **after** it
produces a probability. That analysis — the public systems, the nine differentiators already in our own
repo, and the five ★ features we add on top, each with a pass condition — is `06-DIFFERENTIATION.md`.

### 2.7 Risk: the logbook is empty and the advisor has not signed anything

§13.1 requires a meeting with the advisor **at least once every two weeks**, with the advisor
initialing each logbook entry. Zero entries after one week is a red flag on the advisor's
progress assessment (Appendix C, "Regularity and preparedness" 10% + "Documentation and
logbook" 10%).

**Fix this week:** fill Week 1 and Week 2 rows, book the next advisor meeting, get initials.

### 2.8 Risk: the department needs a phone number and group number

From the department notice of 20 Oct 2026: one member per group must send the ELD their name,
phone number, final project name, **and group number**. Send this **today** — it is a
one-minute task with an obvious reputational cost if missed.

### 2.9 Risk: the syllabus-level scope mismatch

Your current `tilte.txt` describes a **mobile/edge app with offline inference**. The advisor's
email asks for "upload **or capture**", "display the results with relevant guidance", and
"maintain diagnosis history" — which the app covers. But note the advisor never said *mobile*
specifically. A **web** target would widen your audience and your evaluation options.

**Recommendation (see `docs/design/architecture.md`):** build **one model + one API + two
front-ends** (Flutter mobile app + a small web client). This is not scope creep — it is
*reuse*, and it is what makes the "real external stakeholder" claim credible (a web app can
be used by an extension officer on a laptop in a town, not only a farmer with a phone).
If time runs short, the mobile app is the deliverable and the web client is the bonus.

---

## 3. Gate timeline — what is due when

| Week | Dates | Gate (Guideline Table 16.1) | Must be complete |
|---|---|---|---|
| 1–2 | Oct 19 – Nov 1 | Advisor / Coordinator approval | Proposal, ethics screen, logbook W1–W2, repo created |
| 3–4 | Nov 2 – Nov 15 | **Proposal approval** | Approved proposal with approval block signed |
| 5–7 | Nov 16 – Dec 6 | **Requirements baseline** | ≥15 sources, comparison table, gap, FR/NFR spec signed by advisor |
| 8–13 | Dec 7 – Jan 17 | Design review | Architecture, schema, UI wireframes, traceability matrix started, **model prototype trained** |
| 14 | Jan 18 – Jan 24 | **FYP I defense** | Chapters 1–4 + ≤22 slides |
| 15–18 | Jan 25 – Feb 21 | Progress review | Core prototype |
| 19–22 | Feb 22 – Mar 21 | Prototype review | Integrated system |
| 23–24 | Mar 22 – Apr 4 | Evaluation review | Test results + evaluation |
| 25–29 | Apr 5 – May 9 | Advisor approval | Draft final report |
| 30 | May 10 – May 16 | **FYP II defense** | Report + live demo |
| 31–32 | May 17 – May 30 | Advisor verification | Corrected report + submission package |

---

## 4. This week's checklist (Week 1: Oct 19–25)

**Everyone**
- [ ] Send the ELD: name, phone number, project title, **group number** (pick one member — Hayredin)
- [ ] Read the full Guideline PDF (64 pages) — at minimum §2, §4, §5, §7, §9, §10, §13, §14, §15, §16, §17
- [ ] Fill logbook Week 1 row; book advisor meeting for Week 2
- [ ] Append to the AI-use log (`docs/appendices/Appendix-L-AI-Disclosure.md`)
- [ ] Create the GitHub repo, add all 4 members, create the branch/issue structure
- [ ] Agree the tech stack (Flutter vs React Native) — see `docs/design/architecture.md` §2

**Hayredin — data & model**
- [ ] Download JMuBEN + JMuBEN2 (Mendeley, CC BY 4.0) and BRACOL
- [ ] Download ROCoLE, Uganda 2025, Saposoa Peru, CoffeeLeaf-CO v2, Silva 2020
- [ ] Record exact class counts per dataset (files actually present) into `data/dataset-sources.md`
- [ ] Write the duplicate-grouping script (pHash clustering) — `scripts/prepare_data.py`
- [ ] Start the logbook row: which datasets, licenses, collection notes

**Bemnet — mobile app**
- [ ] Read the Flutter TFLite stack: `tflite_flutter`, `image_picker`, `camera`, `sqflite`
- [ ] Scaffold the Flutter app, run it on a real Android phone (or emulator) — prove the toolchain
- [ ] Draw the 4 screens on paper / Figma: Capture-Upload, Result, Guidance, History
- [ ] Get the app running with a **placeholder** model + mock result → this de-risks everything

**Yohannes — backend & platform**
- [ ] Create the GitHub org/repo: README, `main` protected, issue board, milestone tags, PR template
- [ ] Design the API contract (draft) → `docs/design/api-spec.md`
- [ ] Design the diagnosis-history schema → `docs/design/database-schema.md`
- [ ] Draft the architecture diagram → `docs/design/architecture.md`
- [ ] Write the Dockerfile + `docker-compose` skeleton for the API

**Nahom — research & quality**
- [ ] Read the 6 anchor papers in `docs/literature/references.md` (start with JMuBEN, PeerJ cs-3172, PeerJ cs-3386, the edge paper, the ConvNeXt and EfficientNet-B2 model cards)
- [ ] Fill the comparison table with ≥3 systems → `docs/literature/comparison-table.md`
- [ ] Draft the gap statement (use §2.6 above as the skeleton)
- [ ] Contact EIAR/JARC Plant Pathology for the treatment knowledge base (email template in `data/knowledge-base.md`)
- [ ] Complete Appendix M ethical screening

---

## 5. What "done" looks like

At the FYP II defense, the panel must be able to see:

1. A **working mobile app** that diagnoses a leaf offline in under 1 second and logs the result.
2. A **working web app** (same model) for extension officers.
3. A **model** trained on a leakage-safe split, with a **baseline** (majority class + a heavy
   reference model) evaluated under identical conditions.
4. An **external field-photo evaluation** — the thing no prior system has — with per-class
   recall, calibration, and an honest error analysis.
5. A **full evidence chain**: Problem → Gap → Objectives → Requirements → Design → Implementation
   → Tests → Evaluation → Conclusion, with a traceability matrix proving each objective is met.
6. A **logbook** with 32 weekly entries and advisor initials, and a git history where each of you
   can be seen working.
7. **Honest limitations.** The panel will ask what your model does on a bad photo. Answer: it
   rejects below a confidence threshold and tells the user to retake the photo.
