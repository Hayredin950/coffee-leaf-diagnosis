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
> is what gets archived with the submission package. **One person (Yohannes) pastes the sheet
> content here each week — but each member writes their own row, never someone else's.**

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

| Field | Entry |
|---|---|
| **Member(s)** | H (Hayredin), B (Bemnet), Y (Yohannes), N (Nahom) |
| **Objective addressed** | Pre-SO — project setup and proposal preparation (SO1, SO7 planning) |
| **Planned activity** | H: download JMuBEN/JMuBEN2 and BRACOL; record class counts and licences; begin the duplicate-grouping script. B: install Flutter; scaffold the app; run it on a physical Android device; sketch the four screens. Y: create the GitHub repository with README, branch protection, PR and issue templates; draft the architecture v0.1. N: read the three anchor papers; start the comparison table; contact EIAR/JARC about the knowledge base. **All:** read the Guideline; send the ELD the phone number and group number; create the AI-use log; meet the advisor and obtain the first initials. |
| **Completed activity** | *(to be completed on Friday 23 Oct)* |
| **Problems and risks** | The JMuBEN author has not replied to the dataset request (R1). The JMuBEN paper's "respectively" mapping is inverted relative to the Mendeley record titles — corrected in the group's notes to avoid mislabelling (R13). |
| **Advisor feedback** | *(at the meeting)* |
| **Agreed actions and next milestone** | *(at the meeting)* |
| **Advisor initials** | ________ |

### Week 1 — per-member breakdown

| Member | Specific contribution |
|---|---|
| **Hayredin** | Dataset acquisition and inventory for JMuBEN, JMuBEN2 and BRACOL; documented the exact Mendeley record → class mapping and the count discrepancy (58,549 vs 58,555); began `scripts/prepare_data.py` |
| **Bemnet** | Verified the Flutter + Android toolchain end to end on a physical device; produced the four screen sketches |
| **Yohannes** | Created the repository, set up branch protection, PR/issue templates and the milestone labels; wrote architecture v0.1 |
| **Nahom** | Read the JMuBEN, PeerJ cs-3172 and PeerJ cs-3386 papers and verified every citation against Crossref; began the comparison table; sent the JARC contact email; completed the Appendix M ethics screening |

---

## Week 2 — Oct 26 – Nov 1, 2026

| Field | Entry |
|---|---|
| **Member(s)** | H, B, Y, N |
| **Objective addressed** | SO1, SO7 (proposal preparation) |
| **Planned activity** | H: download the five external datasets (Uganda, RoCoLE, Saposoa, CoffeeLeaf-CO, Silva); write the perceptual-hash duplicate-grouping function. B: build the four mock screens with a fake result and capture the screenshots that become the wireframes. Y: draft the API contract and the database schema; write the Dockerfile skeleton. N: draft the proposal §1–§8; finalise Appendix M; begin the High-complexity justification. **All:** complete logbook rows for weeks 1 and 2; book and hold the second advisor meeting. |
| **Completed activity** | |
| **Problems and risks** | |
| **Advisor feedback** | |
| **Agreed actions and next milestone** | |
| **Advisor initials** | ________ |

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
