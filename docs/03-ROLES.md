# Roles, Task Allocation and Individual Contribution Strategy

**Group of four.** Each member holds primary technical responsibility for at least one major
work package (Guideline §14.2). Roles are declared in the proposal and repeated in Appendix G.

---

## 1. Role assignment

| Role | Owner | ID | Primary work package | Secondary |
|---|---|---|---|---|
| **A. Data & Model Lead** | **Hayredin Mohammed** | UGR/2361/16 | Dataset curation, leakage-safe splits, training, baselines, quantisation, TFLite export, evaluation and error analysis | Backend CI, model serving |
| **B. Mobile App Lead** | **Bemnet Tesfaye** | UGR/3266/16 | Flutter app: capture/upload, on-device inference, result screen, knowledge-base rendering, offline mode, local history | Web client, demo |
| **C. Backend & Platform Lead** | **Yohannes Berhanu** | UGR/9440/16 | FastAPI service, database schema, deployment, security, repository governance, CI, reproducibility package | Web client, logbook compilation |
| **D. Research, Requirements & Quality Lead** | **Nahom Solomon** | UGR/3155/16 | Literature review, gap analysis, requirements specification, test plan, knowledge-base content, ethics screening, usability study, report integration | Model evaluation, KB verification |

Swap freely if someone has a stronger prior skill — but write the swap into `docs/05-DECISION-LOG.md`
and tell the advisor. The *labels* matter less than the *coverage*.

## 2. Why these four packages give you full marks against the rubric

Guideline Table 17.3 weighs FYP I as: Problem definition 15, Literature review 15, Objectives
and requirements 20, Methodology 15, Analysis and design 25, Documentation 5, Presentation 5.
FYP II adds: Technical implementation 20, Testing and evaluation 10, Results/discussion 5.

| Package | Directly feeds | Owns which rubric rows |
|---|---|---|
| A. Data & Model | SO1, SO2, SO3 | Technical implementation (20), Testing & evaluation (10), Results (5) |
| B. App | SO4, SO5 | Technical implementation (20), Analysis & design (25), Presentation/demo (5) |
| C. Backend | SO4, SO6, SO7 | Technical implementation (20), Analysis & design (25), Documentation (5) |
| D. Research | SO1–SO7 | Problem definition (15), Literature review (15), Objectives & requirements (20), Methodology (15), Documentation (5), Presentation (5) |

Every rubric row has an owner. No row is orphaned.

## 3. RACI matrix

R = Responsible (does the work) · A = Accountable (one person, owns the outcome) · C = Consulted · I = Informed

| Deliverable | Hayredin | Bemnet | Yohannes | Nahom |
|---|---|---|---|---|
| Dataset curation & datasheet | **A/R** | I | C | C |
| Leakage-safe split script | **A/R** | I | C | C |
| Model training & baselines | **A/R** | C | C | C |
| TFLite quantisation & export | **A/R** | C | I | I |
| External evaluation & error analysis | **A/R** | C | I | C |
| Calibration (temperature scaling) | **A/R** | I | I | C |
| Flutter app — screens & navigation | C | **A/R** | C | I |
| On-device inference integration | C | **A/R** | C | I |
| Local SQLite history | C | **A/R** | C | I |
| Offline-mode verification | C | **A/R** | I | I |
| Knowledge base content | C | C | I | **A/R** |
| Knowledge base rendering | I | **A/R** | I | C |
| FastAPI service | C | I | **A/R** | I |
| Database schema & migrations | C | C | **A/R** | I |
| Deployment & CI | C | C | **A/R** | I |
| Security review & OWASP checklist | C | C | **A/R** | I |
| Web client | C | **A/R** | C | I |
| Repository governance & logbook compile | C | C | **A/R** | C |
| Literature review & gap | C | C | C | **A/R** |
| Requirements specification | C | C | C | **A/R** |
| Test plan & test cases | C | C | C | **A/R** |
| Usability study (SUS) | I | C | I | **A/R** |
| Ethics screening (Appendix M) | C | C | I | **A/R** |
| AI-use declaration upkeep | C | C | C | **A/R** |
| Traceability matrix | C | C | C | **A/R** |
| Report integration & formatting | C | C | C | **A/R** |
| Defense slides & rehearsal | C | C | C | **A/R** |
| Reproducibility package | **A/R** | C | C | I |

## 4. Weekly task allocation

Every task in `02-WEEKLY-PLAN.md` becomes one logbook entry (Appendix B format: *Week and date ·
Member(s) · Objective addressed · Planned activity · Completed activity · Problems and risks · Advisor
feedback · Agreed actions and next milestone · Advisor initials*). The plan supplies the "planned" and
"completed" columns; nothing is written twice.

### FYP I — the plan lives in one place

The week-by-week allocation for FYP I (W1–W16) is **not duplicated here**. It is
[`docs/02-WEEKLY-PLAN.md`](02-WEEKLY-PLAN.md): sixteen weeks, one task per person per week, and for
every task the artefact that proves it is finished.

This file defines **who owns which work package** (§1–§3) and **how we protect the individual
contribution factor** (§5–§6). It does not say what happens in week 9 — `02-WEEKLY-PLAN.md` does, and
if the two ever disagree, that file wins on tasks and this one wins on ownership.

### FYP II — not planned yet, deliberately

FYP II (W17–W32) is **not** broken into weeks here. Planning it now would be guessing: it depends on what
the FYP I panel asks for, on the final model, and on the FYP II calendar. The phase-level outline is in
[`01-ROADMAP.md`](../01-ROADMAP.md) §Phase 5–10, and the week-by-week plan is written at the **W13 design
review**, when there is evidence to plan against.

Anyone can add an item to the FYP II backlog at any time — put it in `05-DECISION-LOG.md`, not in a
week.

---

## 5. Cross-review rotation (protects your ICF)

The ICF (Guideline Table 17.4) drops to **0.80** if you "explain own modules but the
understanding of other parts is limited". You are a group of four on a system with four
subsystems. Rotate a **review task** every week — you read, test and comment on another
person's package. This is cheap insurance for the defense.

| Week | Hayredin reviews | Bemnet reviews | Yohannes reviews | Nahom reviews |
|---|---|---|---|---|
| Odd weeks | Bemnet's app | Yohannes's API | Nahom's requirements | Hayredin's data pipeline |
| Even weeks | Nahom's KB/literature | Hayredin's model | Bemnet's app | Yohannes's deployment |

**Rule:** the reviewer writes the comment in the PR and the author must respond. Both names land
in the git history — which the examiners read for the ICF.

## 6. ICF defence plan

| Guideline requirement | Your evidence | Where it lives |
|---|---|---|
| §14.3 "can explain the architecture and overall operation" | Every member writes a 1-page "how the whole system works" note, revised weekly | `docs/architecture-understanding.md` (create in W3) |
| §14.2 "primary technical responsibility for at least one major component" | The role table above, in the proposal and Appendix G | Proposal §11; Appendix G |
| §17.7 ICF 1.00: "records show an equal or larger share of the work" | Weekly logbook entries naming who did what + per-member commit counts | Logbook; `git shortlog -s` |
| §17.7 ICF 1.00: "answers troubleshooting questions without the report" | Weekly "troubleshooting drill": each member answers one question about another package | `docs/05-DECISION-LOG.md` drill log |
| §8.4 "each member must commit their own work under their own identity" | Enforce: no shared accounts, PRs reviewed by someone else | Repo settings + PR template |
| Appendix D "can explain any use of AI tools and the checks made" | Each member can describe their own AI-assisted work and the check they ran | Appendix L |

## 7. Rules that protect the group

1. **Never commit to `main` directly.** Branch → PR → one other member approves → merge.
2. **Never commit secrets.** `.env` stays in `.gitignore`; use `.env.example`. (§8.3)
3. **Never commit the datasets.** JMuBEN is 1.8 GB. Keep a `data/README.md` with the download
   URLs and a `scripts/prepare_data.py` that reproduces the split from a manifest. (§8.5, §9.7)
4. **Never mark a task done in the logbook that you cannot show a commit, a screenshot or a
   document for.** The logbook is evidence (§13.2).
5. **One person owns the logbook compilation** (Yohannes), but **every member writes their own
   row**. Do not let one person write all four rows — that is visible in the handwriting/style
   and it undermines the ICF.
6. **Update Appendix L the same day you use an AI tool**, not the night before submission.
