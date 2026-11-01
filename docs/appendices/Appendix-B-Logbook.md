# Appendix B — Weekly Project Progress Log

> **Guideline §13.2:** *"The group keeps a logbook (Appendix B) and updates it every week. Each
> entry records the date, the objective addressed, progress, issues, advisor feedback, agreed
> actions and the next milestone, and the advisor initials the entries after each meeting. The
> logbook must show which member did what."*
>
> **§13.1:** *"The group must meet the advisor at least once every two weeks... the advisor signs
> or initials the logbook entry."*
>
> **How to use this file.** This is the working master. The **official** logbook is the
> departmental Google Sheet (the template the advisor circulated on 19 Oct 2026). Every Friday,
> each member updates **their own row** for the week in the sheet; on the meeting week, the row
> goes to the advisor for initials. This markdown file is the group's consolidated copy, and it
> is what gets archived with the submission package. **Nahom compiles it here each Friday
> (`02-WEEKLY-PLAN.md` §3) — but each member writes their own row, never someone else's.**

**Columns (Appendix B):** Week and date · Member(s) · Objective addressed · Planned activity ·
Completed activity · Problems and risks · Advisor feedback · Agreed actions and next milestone ·
Advisor initials.

---

## How to fill a row (the group's house style)

| Column | Rule |
|---|---|
| **Member(s)** | The actual contributors that week. Use initials so per-member counts can be derived. |
| **Objective addressed** | The SO number, e.g. "SO1, SO2". Use the traceability IDs consistently. |
| **Planned activity** | Written on Monday, before the work. |
| **Completed activity** | Written on Friday. Be specific: "merged PR #42 (split script v2), 3 files, 210 lines" — not "worked on the data". |
| **Problems and risks** | The real blocker, plus the risk ID from `docs/04-RISK-REGISTER.md` if it matches. If there was no problem, write "None" — do not leave it blank, because a blank cell is ambiguous. |
| **Advisor feedback** | Filled in at the meeting, in the advisor's own words where possible. |
| **Agreed actions and next milestone** | Who does what by when. Specific and dated. |
| **Advisor initials** | Only the advisor fills this. |

---

## Week 1 — Oct 19–25, 2026

> **Completed retrospectively on 1 November 2026, at the end of W2.** Every line below is traceable to
> a commit, a file, a dated message or a screenshot. The two gate tests that failed are recorded as
> failed rather than backdated, because a logbook that is right about everything is not believed about
> anything.

| Field | Entry |
|---|---|
| **Member(s)** | H (Hayredin), B (Bemnet), Y (Yohannes), N (Nahom) |
| **Objective addressed** | Pre-SO — orientation and inputs (SO1, SO7) |
| **Planned activity** | H: download JMuBEN and JMuBEN2; count images per class. Y: create the Flutter project and run it on a physical phone. B: create the repository, folder tree and `.gitignore`. N: extract the obligations from Guideline §1–§7; score four candidate titles. All: read the Guideline; send the ELD the group details; open the AI-use log. |
| **Completed activity** | **H** — catalogued JMuBEN (`t2r6rszp5c`) and JMuBEN2 (`tgv3zb82nd`) in the Mendeley registry with licences and class lists, and reconciled the count discrepancy between the paper (58,555) and the machine-readable record (58,549); the **download itself was not completed** (see Problems). **Y** — installed the Flutter toolchain and ran a first app on a physical Android device. **B** — wrote the `.gitignore` rule set for data, models and secrets that the repository later adopted, and settled the backend stack (FastAPI + PostgreSQL, ADR-008). **N** — extracted the submission obligations from Guideline §1–§7 and scored four candidate titles with the rejection reason for each (`title-selection.md`). **All** — read the Guideline; the synopsis had been revised and submitted on 12 Oct. |
| **Problems and risks** | **The repository was not created in W1**, so the gate test *("a commit from all four")* failed and is backfilled in W2 — B and N did not yet have GitHub accounts. **The dataset download was not completed** (R1): the JMuBEN author had not replied to the request and the Mendeley records would not resolve from the lab network. |
| **Advisor feedback** | *(at the meeting — to be written in the advisor's own words)* |
| **Agreed actions and next milestone** | Repository created by Y in W2, because the lead held the only group account. H to complete the per-class counts and the datasheet by **Wed 4 Nov**. Downloads to be retried off-campus. |
| **Advisor initials** | ________ |

### Week 1 — per-member breakdown

| Member | Specific contribution | Evidence |
|---|---|---|
| **Hayredin** | JMuBEN / JMuBEN2 record mapping, licences, and the 58,549 vs 58,555 reconciliation | `data/dataset-sources.md` §3 |
| **Bemnet** | `.gitignore` rule set for data, models and secrets; backend stack decision | `.gitignore`; ADR-008 |
| **Yohannes** | Flutter toolchain verified on a physical device | screenshot, filed with the meeting record |
| **Nahom** | Guideline obligations; four candidate titles scored with rejection reasons | `title-selection.md` |

---

## Week 2 — Oct 26 – Nov 1, 2026

> **Completed retrospectively on 1 November 2026.** The repository did not exist for most of this week,
> which is why so much of W2's planned activity landed on the last two days.

| Field | Entry |
|---|---|
| **Member(s)** | H, B, Y, N |
| **Objective addressed** | SO1, SO2, SO7 |
| **Planned activity** | H: datasheet — composition, licences, five external sets, limitations. Y: nine-screen inventory and navigation map; camera plugin spike. B: CI, security NFRs, branch protection. N: ethics screening (App. M), AI-use log (App. L), first three comparison-table rows. All: W1–W2 logbook rows; second advisor meeting. |
| **Completed activity** | **Y** — created `jov1523/coffee_leaf_disease_diagnosis` on **31 Oct**, 43 files and 8,428 lines: the proposal in Appendix A order, the reference registry, the comparison table, FR-01…FR-40 / NFR-01…NFR-40 / DR-01…DR-10, the use cases, test plan T-01…T-60, the traceability matrix, architecture, data model, ML pipeline, the nine-screen UI design, Chapters 1–4 and the starter set; the Guideline and the revised synopsis are carried as read-only sources. **H** — wrote `scripts/prepare_data.py` (grouping key, stratified grouped split, four invariants) and ran the `--audit` gate end to end, **AUDIT PASSED**; wrote the dataset registry and datasheet; rewrote the plan as **16 weeks, one task per person per week**, and opened PR #1 against the group repository (7 files, +2,012 / −292) on 1 Nov. **B** — drafted the API contract and the SQLite DDL for the KB JSON schema. **N** — Appendix M ethics screening and Appendix L AI-use log drafted; the first three comparison-table rows; the JARC contact email sent (no reply as of 1 Nov). |
| **Problems and risks** | **CI is not configured**, so the W2 gate test *("green CI run")* is not met — carried to W3. **B and N could not commit**: `nahoom-sh` was issued on 1 Nov and Bemnet's account is still outstanding, so the *"one commit each"* gate is still open. **Appendix M and L exist in the working set but not in the repository.** The logbook itself is late. |
| **Advisor feedback** | *(at the meeting)* |
| **Agreed actions and next milestone** | Every member commits something by **Tue 3 Nov**. H completes the counts and the datasheet by **Wed 4 Nov**; Y posts the phone screenshot by **Wed 4 Nov**; N lands Appendix M and L by **Wed 4 Nov**. Proposal approval gate **Sun 15 Nov** (W4). |
| **Advisor initials** | ________ |

### Week 2 — per-member breakdown

| Member | Specific contribution | Evidence |
|---|---|---|
| **Hayredin** | Split script with a passing audit; dataset registry and datasheet; 16-week plan; PR #1 | `scripts/prepare_data.py`; PR #1 |
| **Bemnet** | API contract, SQLite DDL, KB JSON schema | `design/data-model.md` |
| **Yohannes** | Group repository — 43 files, 8,428 lines; nine-screen inventory | commit `70b179e`, 31 Oct |
| **Nahom** | Appendix M, Appendix L, comparison table, JARC contact | `appendices/` |

---

## Weeks 3–4 — Nov 2–15, 2026 — Proposal approval gate

### Week 3

| Field | Entry |
|---|---|
| **Member(s)** | H, B, Y, N |
| **Objective addressed** | SO2 (baseline), proposal approval |
| **Planned activity** | H: run the majority-class and MobileNetV3-small baselines to obtain a number for the proposal. B: wire the mock result to real screen states and measure the navigation time. Y: write the High-complexity justification section and risk register v1. N: finish proposal §9–§14 and build the 10-slide proposal deck. |
| **Completed activity** | |
| **Problems and risks** | |
| **Advisor feedback** | |
| **Agreed actions and next milestone** | |
| **Advisor initials** | ________ |

### Week 4

| Field | Entry |
|---|---|
| **Member(s)** | H, B, Y, N |
| **Objective addressed** | Proposal approval |
| **Planned activity** | H: present the baseline results and the split methodology. B: prepare the proposal demonstration. Y: rehearse the proposal Q&A with the team and polish the README. N: finalise proposal v2 and submit it for approval. |
| **Completed activity** | |
| **Problems and risks** | |
| **Advisor feedback** | |
| **Agreed actions and next milestone** | |
| **Advisor initials** | ________ |

---

## Weeks 5–7 — Nov 16 – Dec 6, 2026 — Requirements baseline gate

### Week 5

| Field | Entry |
|---|---|
| **Member(s)** | H, B, Y, N |
| **Objective addressed** | SO1, SO2, SO7 |
| **Planned activity** | H: read both published model cards and write the "why models fail in the field" note. B: draft the wireframes and define the UI state model. Y: turn the literature findings into architecture decisions with citations. N: read five more papers and write the thematic synthesis §2.1–§2.3. |
| **Completed activity** | |
| **Problems and risks** | |
| **Advisor feedback** | |
| **Agreed actions and next milestone** | |
| **Advisor initials** | ________ |

### Week 6

| Field | Entry |
|---|---|
| **Member(s)** | H, B, Y, N |
| **Objective addressed** | SO1, SO5, SO6 |
| **Planned activity** | H: write the dataset datasheet — provenance, labels, licences, class balance, known limitations. B: define the functional requirements for the app with Nahom. Y: draft the API specification and the OpenAPI contract. N: write the full FR/NFR specification with IDs, priorities and measurable targets. |
| **Completed activity** | |
| **Problems and risks** | |
| **Advisor feedback** | |
| **Agreed actions and next milestone** | |
| **Advisor initials** | ________ |

### Week 7

| Field | Entry |
|---|---|
| **Member(s)** | H, B, Y, N |
| **Objective addressed** | SO1, SO7 — **requirements baseline gate** |
| **Planned activity** | H: implement the leakage-safe splitter and produce the split manifest. B: review the FR/NFR specification for testability. Y: add the security requirements to the NFRs and produce the deployment plan. N: complete the comparison table and the gap statement; obtain the advisor's requirements-baseline approval. |
| **Completed activity** | |
| **Problems and risks** | |
| **Advisor feedback** | |
| **Agreed actions and next milestone** | |
| **Advisor initials** | ________ |

---

## Weeks 8–13 — Dec 7, 2026 – Jan 17, 2027 — Design and prototype

### Week 8

| Field | Entry |
|---|---|
| **Member(s)** | H, B, Y, N |
| **Objective addressed** | SO2, SO5 |
| **Planned activity** | H: train model v1 by transfer learning. B: draw the use-case, activity and state diagrams. Y: draw the architecture, deployment and data-flow diagrams. N: write the KB schema — symptoms, severity, organic and chemical control. |
| **Completed activity** | |
| **Problems and risks** | |
| **Advisor feedback** | |
| **Agreed actions and next milestone** | |
| **Advisor initials** | ________ |

### Week 9

| Field | Entry |
|---|---|
| **Member(s)** | H, B, Y, N |
| **Objective addressed** | SO2, SO3, SO5, SO6 |
| **Planned activity** | H: evaluate model v1 on the internal test set and produce the confusion matrix. B: draw the inference sequence diagram. Y: write the database schema, data dictionary and the first migration. N: draft the KB content for all five classes from the FAO and peer-reviewed sources. |
| **Completed activity** | |
| **Problems and risks** | |
| **Advisor feedback** | |
| **Agreed actions and next milestone** | |
| **Advisor initials** | ________ |

### Week 10

| Field | Entry |
|---|---|
| **Member(s)** | H, B, Y, N |
| **Objective addressed** | SO3, SO4, SO5 |
| **Planned activity** | H: evaluate model v1 on Uganda, RoCoLE and Saposoa; record the generalisation gap. B: sign off the wireframes and build the Flutter result screen. Y: implement `POST /v1/predict` and `GET /v1/health`. N: review the KB content with the agronomy contact. |
| **Completed activity** | |
| **Problems and risks** | |
| **Advisor feedback** | |
| **Agreed actions and next milestone** | |
| **Advisor initials** | ________ |

### Week 11

| Field | Entry |
|---|---|
| **Member(s)** | H, B, Y, N |
| **Objective addressed** | SO4, SO5 |
| **Planned activity** | H: quantise to int8 and measure the size and the desktop latency. B: integrate the `.tflite` into the app and display a real prediction. Y: Dockerise the API and deploy it to staging. N: start the Chapter 1 and Chapter 3 drafts. |
| **Completed activity** | |
| **Problems and risks** | |
| **Advisor feedback** | |
| **Agreed actions and next milestone** | |
| **Advisor initials** | ________ |

### Week 12

| Field | Entry |
|---|---|
| **Member(s)** | H, B, Y, N |
| **Objective addressed** | SO4, SO6, SO7 |
| **Planned activity** | H: measure the latency on two reference phones. B: implement the local SQLite history schema and the repository layer. Y: set up CI — lint, test, container build, model-artefact check. N: start the Chapter 2 draft and update the traceability matrix to v0.5. |
| **Completed activity** | |
| **Problems and risks** | |
| **Advisor feedback** | |
| **Agreed actions and next milestone** | |
| **Advisor initials** | ________ |

### Week 13

| Field | Entry |
|---|---|
| **Member(s)** | H, B, Y, N |
| **Objective addressed** | All SOs — **design review gate** |
| **Planned activity** | H: package the final model v1 metrics for the report. B: make the full app flow work end to end on a phone. Y: finish the figures supporting Chapters 1–4 and freeze the architecture. N: assemble Chapters 1–4 and hold the advisor's pre-review of the FYP I document. |
| **Completed activity** | |
| **Problems and risks** | |
| **Advisor feedback** | |
| **Agreed actions and next milestone** | |
| **Advisor initials** | ________ |

---

## Week 14 — Jan 18–24, 2027 — FYP I defense

| Field | Entry |
|---|---|
| **Member(s)** | H, B, Y, N |
| **Objective addressed** | SO1–SO7 (Chapters 1–4) |
| **Planned activity** | H: present the methodology, dataset and model. B: present the system demonstration on the phone. Y: present the architecture, the repository and the CI. N: present the problem, the gap, the literature and the requirements; lead the session and keep time. |
| **Completed activity** | |
| **Problems and risks** | |
| **Advisor feedback** | |
| **Agreed actions and next milestone** | |
| **Advisor initials** | ________ |

---

## Weeks 15–18 — Jan 25 – Feb 21, 2027 — Core prototype

| Week | Member(s) | Objective | Planned activity | Completed | Problems/risks | Advisor feedback | Actions / milestone | Initials |
|---|---|---|---|---|---|---|---|---|
| 15 | H,B,Y,N | SO4, SO5 | H: inference wrapper and the precision–recall curves. B: camera capture, gallery upload, quality gate. Y: `POST /v1/predict` with validation and error codes. N: test plan v1 and the API test cases. | | | | | |
| 16 | H,B,Y,N | SO4, SO6 | H: latency benchmark harness (30 runs, mean and p95). B: the result screen with confidence, top-3 and guidance. Y: `/v1/diagnoses` CRUD and the server database. N: the usability protocol, the consent form and the ethics note. | | | | | |
| 17 | H,B,Y,N | SO6, SO7 | H: memory and model-size measurement on a low-end phone. B: the history screen with list, search, filter, delete and CSV export. Y: authentication, rate limiting, the dependency audit. N: run the usability study (≥10 participants) and compute the SUS. | | | | | |
| 18 | H,B,Y,N | SO4, SO7 | H: write the performance section. B: offline-mode verification in airplane mode. Y: deploy the API and the staging database. N: write the evaluation-plan section; hold the advisor's progress review. | | | | | |

---

## Weeks 19–22 — Feb 22 – Mar 21, 2027 — Integrated system

| Week | Member(s) | Objective | Planned activity | Completed | Problems/risks | Advisor feedback | Actions / milestone | Initials |
|---|---|---|---|---|---|---|---|---|
| 19 | H,B,Y,N | SO3, SO6 | H: train model v2 with the refined recipe. B: the web client — upload and result. Y: the history sync endpoint and the conflict rule. N: draft Chapter 5. | | | | | |
| 20 | H,B,Y,N | SO3, SO5 | H: temperature scaling; the ECE and selective-risk report. B: the web client's guidance and history views. Y: integrate the web client with the API. N: knowledge base v2 with the sources cited per field. | | | | | |
| 21 | H,B,Y,N | SO3, SO7 | H: the final external evaluation across all five external sets. B: export and share a diagnosis record. Y: the security hardening pass and the OWASP self-check. N: update the traceability matrix; outline Chapter 6. | | | | | |
| 22 | H,B,Y,N | All | H: the error analysis and the representative failure cases. B: the integrated end-to-end demo, phone and web. Y: the prototype review with the advisor. N: draft Chapter 6; the prototype review with the advisor. | | | | | |

---

## Weeks 23–24 — Mar 22 – Apr 4, 2027 — Testing and evaluation

| Week | Member(s) | Objective | Planned activity | Completed | Problems/risks | Advisor feedback | Actions / milestone | Initials |
|---|---|---|---|---|---|---|---|---|
| 23 | H,B,Y,N | SO7 | H: run the full evaluation suite, the bootstrap CIs and the McNemar test. B: execute the UI test cases and capture the evidence. Y: execute the API and security test cases. N: compile all the evidence into Appendix F. | | | | | |
| 24 | H,B,Y,N | SO3, SO7 | H: the final metrics table for Chapter 6. B: the performance test on three reference phones. Y: the deployment and the reproducibility package. N: the final traceability matrix with the achievement status; the evaluation review. | | | | | |

---

## Weeks 25–29 — Apr 5 – May 9, 2027 — Final report

| Week | Member(s) | Objective | Planned activity | Completed | Problems/risks | Advisor feedback | Actions / milestone | Initials |
|---|---|---|---|---|---|---|---|---|
| 25 | H,B,Y,N | SO7 | H: the results-to-script table and the reproduction instructions. B: the user guide and the installation guide. Y: the technical documentation (Appendix J). N: draft Chapter 7 and the abstract. | | | | | |
| 26 | H,B,Y,N | SO7 | H: proofread Chapters 5 and 6. B: the demo script and the recorded backup video. Y: assemble the submission package (Appendix I). N: the front matter; format the document. | | | | | |
| 27 | H,B,Y,N | SO7 | H: address the review comments on Chapters 5 and 6. B: the demo rehearsal 1 and 2. Y: fix the defects found in the rehearsal. N: the full-document formatting and the similarity check. | | | | | |
| 28 | H,B,Y,N | SO7 | H: freeze the metrics; no new claims after this point. B: the demo rehearsal 3 and the timing check. Y: the release tag, the repository snapshot and the archive. N: the final Appendix L and each member's Appendix G. | | | | | |
| 29 | H,B,Y,N | SO7 | H: the final code freeze. B: the final slides and the speaker notes. Y: submit the draft to the advisor; send the slides to the Coordinator. N: the submission of the draft and the slides. | | | | | |

---

## Week 30 — May 10–16, 2027 — FYP II defense

| Field | Entry |
|---|---|
| **Member(s)** | H, B, Y, N |
| **Objective addressed** | All SOs — final assessment |
| **Planned activity** | Full rehearsal ×3; a question drill against Appendix D; the live demonstration (phone offline, web, and a deliberate failure case); all members present. |
| **Completed activity** | |
| **Problems and risks** | |
| **Advisor feedback** | |
| **Agreed actions and next milestone** | |
| **Advisor initials** | ________ |

---

## Weeks 31–32 — May 17–30, 2027 — Corrections and final submission

| Field | Entry |
|---|---|
| **Member(s)** | H, B, Y, N |
| **Objective addressed** | All SOs — advisor verification |
| **Planned activity** | Implement the panel's required corrections; re-run any affected test and update Appendices E and F; assemble the final submission package; obtain the advisor's verification; archive the repository snapshot and complete the logbook. |
| **Completed activity** | |
| **Problems and risks** | |
| **Advisor feedback** | |
| **Agreed actions and next milestone** | |
| **Advisor initials** | ________ |

---

## Advisor meeting record

Every two weeks, per §13.1. An agenda before, minutes after.

| # | Date | Attendees | Agenda | Decisions | Actions (owner, date) | Advisor initials |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| 11 | | | | | | |
| 12 | | | | | | |
| 13 | | | | | | |
| 14 | | | | | | |
| 15 | | | | | | |
| 16 | | | | | | |

---

## End-of-project completion check

- [ ] 32 weekly entries, each naming the contributing members
- [ ] Advisor initials on every meeting week
- [ ] Every row has a "completed activity" that could be evidenced by a commit, a document or a screenshot
- [ ] Every "problems and risks" cell is filled (including "None")
- [ ] Every "agreed actions and next milestone" names an owner and a date
- [ ] The meeting record has 16 entries
- [ ] The advisor's progress assessment (Appendix C) is completed for each of the four members
