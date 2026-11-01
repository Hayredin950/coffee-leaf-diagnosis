# Roadmap and Work Plan

**Project:** Design and Development of a Coffee Leaf Disease Diagnosis System Using Deep Learning
**Duration:** 32 weeks — FYP I (weeks 1–16), FYP II (weeks 17–32)
**Week 1 begins:** Monday 19 October 2026

> **Numbering is continuous across the year, and this file is the 32-week view.** FYP I occupies
> **W1–W16** (defense W14, corrections and final submission W15–W16). The week-by-week, one-task-per-person
> plan for FYP I is `docs/02-WEEKLY-PLAN.md`, and that file is authoritative for FYP I detail.

---

## 1. Product goal (one sentence)

> A farmer or extension officer photographs a coffee leaf on a phone with no network, gets a
> five-class diagnosis with confidence and actionable treatment guidance in under one second,
> and keeps a searchable local history of every diagnosis.

## 2. System scope (what "the system" is)

| Layer | Component | Technology |
|---|---|---|
| L1 | **Model** | MobileNetV3-Small (ImageNet) → fine-tuned → int8 post-training quantised → TFLite (`.tflite` + metadata + labels) |
| L2 | **Mobile client** | Flutter (Android-first, iOS-compatible), `tflite_flutter`, `image_picker`/`camera`, `sqflite` (or Drift) |
| L3 | **Knowledge base** | Versioned JSON of symptoms, severity bands and treatment (organic + chemical) per class, embedded in the app asset — fully offline |
| L4 | **API** | Python FastAPI + Pydantic + SQLAlchemy; REST; deployed on a free-tier container host |
| L5 | **Web client** | Lightweight HTML/JS client (or Gradio) calling the API — for extension officers and for the defense demo on a laptop |
| L6 | **Data layer** | Local SQLite on device; optional Postgres on the server; sync of history via REST with last-write-wins on `(diagnosis_id)` |
| L7 | **Training pipeline** | Python + TensorFlow/Keras + `tflite-model-maker` + Albumentations; DVC-style manifest of splits and seeds |

**Explicit non-goals (put these in the proposal — scope control earns marks):** no soil/root/cherry
diagnosis, no nutrient-deficiency detection, no cloud model training, no user accounts in v1,
no real-time video diagnosis in v1.

## 3. Milestone plan

### Phase 0 — Orientation and title selection (Weeks 1–2, Oct 19 – Nov 1)
**Goal:** Proposal, ethics screen, logbook, repository.

| # | Task | Owner | Output |
|---|---|---|---|
| 0.1 | Read the Guideline; extract all deliverable obligations into a tracker | Nahom | `docs/00-STATUS.md` |
| 0.2 | Send ELD: name, phone, title, group number | Hayredin | DM sent |
| 0.3 | Download and inventory all 6 datasets; record exact counts + licenses | Hayredin | `data/dataset-sources.md` |
| 0.4 | Duplicate-grouping + leakage-safe split script | Hayredin | `scripts/prepare_data.py` |
| 0.5 | Repo, branches, PR template, issue board, CI skeleton | Yohannes | GitHub repo live |
| 0.6 | Architecture + API contract + DB schema (v0.1) | Bemnet | `docs/design/*` |
| 0.7 | Flutter scaffold running on a real device with a mock model | Yohannes | APK installs, screen navigable |
| 0.8 | Read 6 anchor papers; fill comparison table; draft gap statement | Nahom | `docs/literature/*` |
| 0.9 | Appendix M ethical screening; draft proposal (all 14 sections) | Nahom + all | `docs/proposal/Appendix-A-Proposal.md` |
| 0.10 | Contact EIAR/JARC for knowledge-base review | Nahom | Email sent |
| 0.11 | Fill logbook W1–W2; advisor meeting + initials | All | Sheet rows 1–2 complete |

**Gate 1 (end W2):** Proposal submitted, ethics screen done, repo live, logbook current, advisor meeting held.

### Phase 1 — Proposal and approval (Weeks 3–4, Nov 2 – Nov 15)
**Goal:** Committee approval.

| # | Task | Owner | Output |
|---|---|---|---|
| 1.1 | Incorporate advisor feedback into the proposal | Nahom | Proposal v2 |
| 1.2 | Build the **High-complexity justification** (external data + real stakeholder + OOD research question) | All, led by Hayredin | Proposal §2, §5, §9 |
| 1.3 | Baseline experiment: majority-class + small MobileNetV3 on the leakage-safe split | Hayredin | Baseline metrics table |
| 1.4 | Prepare the 10-minute proposal presentation (≤10 slides) | All | Slides |
| 1.5 | Proposal defense rehearsal ×2; role-split the speaking | All | Dry run notes |
| 1.6 | Update risk register with advisor feedback; confirm roles in the proposal | Yohannes | `docs/04-RISK-REGISTER.md` |

**Gate 2 (end W4):** Committee approval recorded in the Appendix A approval block.

### Phase 2 — Extended literature review and requirements (Weeks 5–7, Nov 16 – Dec 6)
**Goal:** Requirements baseline approved by the advisor (§7.3).

| # | Task | Owner | Output |
|---|---|---|---|
| 2.1 | Thematic literature synthesis (not source-by-source), ≥15 sources read | Nahom | `docs/literature/ch2-literature-review.md` |
| 2.2 | Comparison table, ≥3 directly comparable systems on identical criteria | Nahom | `docs/literature/comparison-table.md` |
| 2.3 | Gap statement: what exists does not do, why it matters, how we respond | Nahom | Chapter 2 |
| 2.4 | Write FR/NFR specification with IDs and priorities | Nahom + Bemnet | `docs/requirements/requirements-spec.md` |
| 2.5 | Verify every reference against the publisher page; complete the IEEE reference list | Nahom | `docs/literature/references.md` |
| 2.6 | Literature-informed architecture decisions (cite where each choice came from) | Bemnet | Architecture v1.0 |
| 2.7 | Test plan + test-case templates + levels justified | Nahom + Bemnet | `docs/requirements/test-plan.md` |
| 2.8 | Traceability matrix v0.1 (SO → FR/NFR → design → test) | All | `docs/requirements/traceability-matrix.md` |
| 2.9 | Advisor meeting; obtain **requirements baseline approval** | All | Signed spec |

**Gate 3 (end W7):** Signed requirements baseline. *No design work starts before this.*

### Phase 3 — Design and feasibility prototype (Weeks 8–13, Dec 7 – Jan 17)
**Goal:** Design review + a trained model that proves the approach works.

| # | Task | Owner | Output |
|---|---|---|---|
| 3.1 | System architecture, component, deployment and data-flow diagrams | Bemnet | `docs/design/architecture.md` |
| 3.2 | Database schema, data dictionary, migrations, seed script | Bemnet | `docs/design/database-schema.md` |
| 3.3 | Use-case, activity, sequence and state diagrams | Yohannes | `docs/design/ui-wireframes.md` |
| 3.4 | UI wireframes for the 4 screens + clickable prototype | Yohannes | Wireframes |
| 3.5 | **Train the first real model** on the leakage-safe split; report metrics | Hayredin | Trained model + metrics |
| 3.6 | External test-set evaluation v0 (Uganda, ROCoLE, Saposoa) | Hayredin | External metrics |
| 3.7 | Convert to TFLite, quantise int8, measure size/latency | Hayredin | `.tflite` artefact |
| 3.8 | Build the agronomic knowledge base with JARC/FAO/peer-reviewed sources | Nahom | `data/knowledge-base.md` |
| 3.9 | API implemented + Dockerised + deployed to staging | Bemnet | Staging URL |
| 3.10 | Flutter app wired to the real `.tflite` model | Yohannes | Working APK |
| 3.11 | Write Chapters 1–4 of the report | All (Nahom integrating) | `docs/report/ch1..ch4` |
| 3.12 | Traceability matrix v0.5; risk register review with advisor | Yohannes | Updated matrix |

**Gate 4 (end W13):** Design review passed; model prototype proven; Chapters 1–4 drafted.

### Phase 4 — FYP I defense, corrections and submission (Weeks 14–16, Jan 18 – Feb 7)
**Goal:** Pass FYP I, close every panel condition, submit the corrected document.
Week 14 is the defense; W15–W16 are corrections and final submission — see `docs/02-WEEKLY-PLAN.md`.

| # | Task | Owner | Output |
|---|---|---|---|
| 4.1 | Finalise Chapters 1–4; format to the guideline spec (Times New Roman 12, 1.5 spacing, margins) | Nahom | `FYP I document.pdf` + `.docx` |
| 4.2 | Build the ≤22-slide deck | All | `docs/defense/slides-outline.md` |
| 4.3 | Speaker allocation + rehearsal ×3 | All | Rehearsal notes |
| 4.4 | Appendix D checklist self-audit | All | `docs/appendices/Appendix-D-Defense-Checklist.md` |
| 4.5 | Submit slides to the Coordinator ≥48 h before | Yohannes | Email confirmation |

### Phase 5 — FYP II core prototype (Weeks 17–20, Feb 8 – Mar 7)
**Goal:** Progress review passed.

| # | Task | Owner | Output |
|---|---|---|---|
| 5.1 | Mobile app: camera capture, gallery upload, quality gate, result screen | Yohannes | Screens work end-to-end |
| 5.2 | Mobile app: local SQLite history, search, filter, delete, export | Yohannes | History works |
| 5.3 | Knowledge-base rendering from the embedded JSON | Yohannes | Guidance screen works |
| 5.4 | Confidence threshold + "retake photo" path | Yohannes | UX matches design |
| 5.5 | API: `/predict`, `/diagnoses`, `/diagnoses/{id}`, `/health`, `/kb` | Bemnet | API live |
| 5.6 | Optimise: model size, latency, memory on a low-end phone | Hayredin + Yohannes | Perf table |
| 5.7 | Unit tests for inference wrapper, history DAO and API | Bemnet + Hayredin | Test suite |
| 5.8 | Weekly logbook + advisor meeting | All | Logbook current |

**Gate 5 (end W20):** Core prototype demonstrated to advisor.

### Phase 6 — FYP II integrated system (Weeks 21–22, Mar 8 – Mar 21)
**Goal:** Prototype review passed.

| # | Task | Owner | Output |
|---|---|---|---|
| 6.1 | Web client: upload → diagnosis → guidance → history | Bemnet + Yohannes | Live web app |
| 6.2 | Optional history sync (device → server), conflict rule documented | Bemnet | Sync working |
| 6.3 | Model v2: retrain with the best augmentation recipe, recalibrate confidence | Hayredin | Model v2 |
| 6.4 | Calibration: temperature scaling; report ECE + selective risk | Hayredin | Calibration results |
| 6.5 | Retrain/refresh the external evaluation on all 5 external sets | Hayredin | Final metrics |
| 6.6 | Security pass: input validation, file-size/type limits, auth on the API, dependency scan | Bemnet | Security checklist |
| 6.7 | Offline verification: airplane-mode test of every core feature | Yohannes | Offline test evidence |
| 6.8 | Write Chapter 5 | All (Nahom integrating) | Chapter 5 draft |

**Gate 6 (end W22):** Integrated system demoed; Chapter 5 drafted.

### Phase 7 — Testing and evaluation (Weeks 23–24, Mar 22 – Apr 4)
**Goal:** Evaluation review passed.

| # | Task | Owner | Output |
|---|---|---|---|
| 7.1 | Execute the full test plan; fill Appendix F test cases with actual results | All | `docs/appendices/Appendix-F-Test-Cases.md` |
| 7.2 | Performance test on 3 reference phones (low/mid/high) | Hayredin | Latency/memory/battery table |
| 7.3 | Usability study with ≥10 participants, SUS questionnaire + task success | Nahom | SUS score, task success |
| 7.4 | Error analysis: representative failures, confusion matrix, per-class recall | Hayredin | Chapter 6 error analysis |
| 7.5 | Statistical test (McNemar / bootstrap CI) for model comparison claims | Hayredin | Significance results |
| 7.6 | Final traceability matrix with achievement status per objective | All | Appendix E complete |
| 7.7 | Write Chapter 6; state limitations honestly | All | Chapter 6 draft |

**Gate 7 (end W24):** Evaluation review; every objective has evidence and an achievement status.

### Phase 8 — Final report (Weeks 25–29, Apr 5 – May 9)
**Goal:** Advisor approves the draft.

| # | Task | Owner | Output |
|---|---|---|---|
| 8.1 | Write Chapter 7 (conclusion, contributions, limitations, future work) | Nahom | Chapter 7 |
| 8.2 | Front matter, title page, declaration, approval sheet, abstract (200–300 words) | Nahom | Front matter |
| 8.3 | Format the whole document to the guideline spec | Nahom | `.docx` |
| 8.4 | Appendix L AI-use declaration — final and complete | All | Appendix L |
| 8.5 | Appendix G individual contribution statement | Each member | Appendix G |
| 8.6 | Appendix J technical documentation + install guide + user guide | Yohannes + Bemnet | Docs |
| 8.7 | Reproducibility package: env file, seeds, scripts, results-to-script table | Hayredin | Reproducibility package |
| 8.8 | Similarity check (self-run, <20 %) | Nahom | Similarity report |
| 8.9 | Appendix I final submission checklist audit | All | Checklist |
| 8.10 | Defense deck (≤22 slides) + demo script + recorded backup video | All | Deck + video |

### Phase 9 — FYP II defense (Week 30, May 10 – May 16)

| # | Task | Owner | Output |
|---|---|---|---|
| 9.1 | Submit slides to the Coordinator ≥48 h before | Yohannes | Email |
| 9.2 | Rehearsal ×3; question-drill each other against Appendix D | All | Notes |
| 9.3 | **Live demonstration**: phone offline demo + web demo + failure case | Yohannes | Demo passes |
| 9.4 | All members present; each explains their own module **and** the whole system | All | — |

### Phase 10 — Corrections and final submission (Weeks 31–32, May 17 – May 30)

| # | Task | Owner | Output |
|---|---|---|---|
| 10.1 | Implement the panel's required corrections | All | Corrected report |
| 10.2 | Re-run any test affected by the corrections; update Appendix E and F | Hayredin + Bemnet | Updated evidence |
| 10.3 | Final submission package assembled per Appendix I | Yohannes | Package |
| 10.4 | Advisor verification sign-off | All | Verified report |
| 10.5 | Archive the repo snapshot; final logbook completion | Yohannes | Archived |

---

## 4. Critical path

```
Week 1 ─ datasets downloaded ─┐
                              ├─► split script ─► baseline ─► Model v1 ─► TFLite ─► App wired ─►
Week 1 ─ Flutter toolchain ───┘                                                     │
                                                                                     ▼
Week 5 ─ literature ─► requirements baseline ─► design ───────────────────► integrated system
                                                                                     │
                                                                                     ▼
                                              external eval ─► Chapter 6 ─► report ─► defense
```

**The critical path is Hayredin's data → model → TFLite chain feeding Yohannes's app.**
If that slips, everything slips. Mitigation: a placeholder model must exist in the app by
**Week 13** even if it is the 2-class baseline, so integration is never the blocker.

## 5. Recurring weekly rhythm (every week, no exceptions)

| When | What | Who |
|---|---|---|
| Monday | Read the plan for the week; pick tasks; update the logbook "Planned activity" | All |
| Daily | Commit under your own identity with a meaningful message; open/close an issue | All |
| Thursday | Update the logbook row: completed activity, problems, risks | All |
| Friday | **Logbook row completed and sent to the advisor** | All |
| Every 2 weeks | Advisor meeting with agenda + minutes; advisor initials the logbook | All + advisor |
| Every 4 weeks | Risk register review with the advisor (§6.3 requires monthly) | Yohannes + advisor |
| End of month | Appendix L AI-use log updated | All |
