# Coffee Leaf Disease Diagnosis System — Final Year Project

**Title:** Design and Development of a Coffee Leaf Disease Diagnosis System Using Deep Learning
**Institution:** Addis Ababa University — College of Natural and Computational Sciences, Department of Computer Science
**Advisor:** Surafiel Habib Asefa
**Group:** Yohannes Berhanu (UGR/9440/16) · Hayredin Mohammed (UGR/2361/16) · Bemnet Tesfaye (UGR/3266/16) · Nahom Solomon (UGR/3155/16)
**Logbook starts:** Week 1, Monday 19 October 2026
**FYP I defense:** Week 14, 18–24 January 2027 · **FYP II defense:** Week 30, 10–16 May 2027

---

## Read this first

| If you have | 10 minutes | 1 hour | A whole afternoon |
|---|---|---|---|
| **10 minutes** | `docs/00-STATUS.md` | | |
| **An hour** | | `docs/01-ROADMAP.md` + `docs/03-ROLES.md` | |
| **A whole afternoon** | | | `docs/proposal/Appendix-A-Proposal.md` → `docs/literature/` → `docs/requirements/` → `docs/design/` → `docs/report/` |
| **Just want to know what to do today** | | `docs/02-WEEKLY-PLAN.md` — find your column (H / B / Y / N) | |
| **Want to know why this isn't an ordinary project** | | | `docs/06-DIFFERENTIATION.md` → `docs/07-IMPACT-AND-SCALE.md` |
| **Are preparing for the defense** | | | `docs/appendices/Appendix-D-N-Defense.md` + `docs/defense/slides-and-demo.md` |

---

## Project in one paragraph

Smallholder coffee farmers in Ethiopia detect disease late because the diagnostician is far
away, and the software that could close that distance currently requires the connectivity
that is missing. This project builds a **complete, fully offline mobile application** that
diagnoses five coffee leaf conditions on a low-cost Android phone, delivers sourced agronomic
treatment guidance, and keeps a searchable local diagnosis history — and it **measures
honestly** how well such a classifier performs on real field photographs, because the
published evidence says that in-domain accuracy does not survive the field. The research gap
is specific: *no published system provides a five-class coffee leaf disease classifier that
runs offline on a low-cost phone, with guidance and history, evaluated on external field
photographs.*

---

## Repository map

```
Final-Year-Project/
├── README.md                        ← you are here
├── tilte.txt                        ← the original synopsis
│
│   (chat.txt and Pasted image.png are advisor correspondence and are
│    git-ignored — kept locally, never published)
│
├── docs/
│   ├── 00-STATUS.md                 ← where the project stands + what to do THIS WEEK
│   ├── 01-ROADMAP.md                ← the 32-week view, phases and gates
│   ├── 02-WEEKLY-PLAN.md            ← THE plan: 16 weeks, one task per person per week
│   ├── 03-ROLES.md                  ← roles, RACI, ICF strategy (no duplicate weekly table)
│   ├── 04-RISK-REGISTER.md          ← Appendix H, with the fallbacks
│   ├── 05-DECISION-LOG.md           ← ADRs, scope changes, the weekly troubleshooting drill
│   ├── 06-DIFFERENTIATION.md        ← the five ★ features vs. the public GitHub projects
│   ├── 07-IMPACT-AND-SCALE.md       ← what this adds to Ethiopia and the world, and what "winning" requires
│   │
│   ├── proposal/
│   │   └── Appendix-A-Proposal.md   ← the full 14-section proposal
│   │
│   ├── literature/
│   │   ├── ch2-literature-review.md ← the thematic synthesis + the gap statement
│   │   ├── comparison-table.md      ← the §5.5 comparison table (3 systems + 2 model artefacts)
│   │   └── references.md            ← the IEEE reference list + the verification ledger
│   │
│   ├── requirements/
│   │   ├── requirements-spec.md     ← 37 FR + 35 NFR + 8 DR
│   │   ├── traceability-matrix.md   ← Appendix E
│   │   └── test-plan.md             ← the test levels, techniques and protocols
│   │
│   ├── design/
│   │   ├── architecture.md          ← Figures 4.1–4.14, the ADR, the security design
│   │   ├── database-and-api.md      ← the schema, the data dictionary, the API contract
│   │   └── ui-wireframes.md         ← the five screens and the accessibility rules
│   │
│   ├── report/
│   │   ├── ch1-introduction.md
│   │   ├── ch2-literature-review.md  (→ ../literature/ch2-literature-review.md)
│   │   ├── ch3-methodology.md
│   │   ├── ch4-requirements-and-design.md
│   │   ├── ch5-implementation.md
│   │   ├── ch6-testing-results.md
│   │   ├── ch7-conclusion.md
│   │   └── abstract.md
│   │
│   ├── defense/
│   │   └── slides-and-demo.md       ← the 22-slide plan + the 10-minute demo script
│   │
│   └── appendices/
│       ├── Appendix-B-Logbook.md     ← the 32-week logbook master
│       ├── Appendix-D-N-Defense.md   ← the defense checklist + the rubric self-audit
│       ├── Appendix-F-Test-Cases.md  ← the test register with the actual-result columns
│       ├── Appendix-G-Contribution.md← the individual contribution statements
│       ├── Appendix-I-J-Checklists.md← the submission and technical documentation checklists
│       ├── Appendix-L-AI-Disclosure.md ← the AI-use log and the declaration
│       └── Appendix-M-Ethics.md
│
├── data/
│   ├── dataset-sources.md            ← the 9 verified sources + the rejected ones
│   ├── datasheet.md                 ← the full datasheet (§9.2, §9.6)
│   ├── knowledge-base.md            ← the KB content plan and the source map
│   └── knowledge_base.json          ← (to be created in FYP I week 9)
│
└── scripts/
    └── prepare_data.py               ← the leakage-safe split pipeline with the audit gate
```

---

## The three things that will decide this project's grade

**1. The proposal has not been submitted yet.** The advisor asked for a revised scope and a
build-and-test plan. The full proposal is drafted at `docs/proposal/Appendix-A-Proposal.md` —
it needs the observed dataset numbers filled in, the novelty section rewritten around ★1–★5
(`docs/06-DIFFERENTIATION.md` §5), the advisor's name confirmed on the high-complexity
justification, and the approval block signed. **This is the Week 3 deliverable.**

**2. The logbook is still empty, and Weeks 1–2 are already gone.** Guideline §13.2 requires a
weekly entry and §13.1 requires the advisor to initial it every two weeks. The 32-week master
with every planned activity is at `docs/appendices/Appendix-B-Logbook.md`, and the exact
backfill rows for W1–W2 (with dates) are in `docs/02-WEEKLY-PLAN.md` §7. **Backfill by
Friday 6 November, then write in-week, never afterwards.**

**3. The AI-use disclosure must stay current.** Guideline §15.3 requires a record of
significant AI use with every report, and §18.1 treats an inability to explain AI-assisted
work as a critical failure. The log is at `docs/appendices/Appendix-L-AI-Disclosure.md`. The
rule is that every AI-assisted artefact must be reviewed, understood and tested by a named
member — which is also why `scripts/prepare_data.py` was executed and its audit gate verified
rather than merely generated.

---

## Role summary

| Person | Package | Also owns |
|---|---|---|
| **Hayredin Mohammed** | Data and model — corpus, splits, training, quantisation, TFLite export, external evaluation, error analysis | The JMuBEN data correspondence |
| **Bemnet Tesfaye** | The Flutter app — capture, on-device inference, the result and guidance screens, offline mode, the local history | The web client and the defense demo |
| **Yohannes Berhanu** | The API, the database, deployment, security, repository governance, CI, the reproducibility package | The risk register and the submission package |
| **Nahom Solomon** | The literature review, the requirements, the test plan, the knowledge base, the ethics screening, the usability study, the report | The logbook and the decision log |

Each member holds primary technical responsibility for one major component (Guideline §14.2)
and must be able to explain the whole system at the defense (Guideline §14.3). The weekly
cross-review rotation in `docs/03-ROLES.md` §5 and the troubleshooting drill in
`docs/05-DECISION-LOG.md` §C exist to make that automatic rather than a crisis.

---

## The technical approach, in one page

| Layer | Choice |
|---|---|
| Model | MobileNetV3-Small (compared against EfficientNet-Lite0 and MobileNetV2) → int8 post-training quantisation → TensorFlow Lite |
| Mobile client | Flutter; `tflite_flutter`; `sqflite`/Drift; a 10 MB budget and a 500 ms median latency budget |
| Knowledge base | A versioned JSON asset embedded in the application — ten fields per class, every practice cited, offline |
| API | FastAPI + Pydantic v2 + SQLAlchemy 2 + PostgreSQL; JWT; rate limiting; content-based upload validation |
| Web client | Static HTML/CSS/JS with no build step, against the same API |
| Data | Nine CC BY 4.0 corpora from six countries and two species; a **grouped, leakage-safe** split with four automated invariants |
| Evaluation | Macro-F1 and per-class recall on the internal split and on **five external field datasets**; temperature scaling; an acceptance-coverage curve; McNemar significance; an error analysis |

---

## What has been verified, and how

Every dataset URL, paper DOI and repository claim in these documents was checked against the
primary source on **21 October 2026** — the Mendeley public API, the Zenodo REST API, the
Hugging Face `datasets-server` API, the Kaggle datasets API, the Crossref REST API, the arXiv
API, PubMed, and the GitHub REST API. The verification ledger is in
`docs/literature/references.md` §Verification status, and the per-dataset ledger is in
`data/dataset-sources.md` §E.

Three corrections were made to the earlier working notes and are worth knowing:

1. The JMuBEN paper is *"Arabica coffee leaf images dataset for coffee leaf disease
   detection and classification"* (Data in Brief, vol. 36, Art. 107142, 2021) — not the title
   previously assumed.
2. The Mendeley record mapping is **inverted** relative to the paper's "respectively":
   `t2r6rszp5c` holds Rust/Cercospora/Phoma and `tgv3zb82nd` holds Miner/Healthy.
3. The BRACOL DOI is `10.17632/yy2k5y8mxg.1`; the PeerJ paper cites BRACOL with the RoCoLE
   DOI, and that error must not be propagated.

---

## Where we are, and what happens next

**Week 2 closes on Sunday 1 November 2026. Week 3 starts Monday 2 November.** Everything below
is dated in `docs/02-WEEKLY-PLAN.md`, which is the single authoritative plan.

**Close out Week 2 (by Friday 6 November):**

1. **Backfill the logbook** for Weeks 1–2, using the rows in `docs/02-WEEKLY-PLAN.md` §7.
2. **Send the ELD** the name, phone number, project title and **group number** — if this has
   not already been done, it is now two weeks late and needs a phone call, not an email.
3. **Add all four members to the repository** (`jov1523/coffee_leaf_disease_diagnosis`), with
   branch protection on `main`, and get every member's GitHub username on record.

**Week 3 (2–8 November) — the week the project becomes defensible:**

4. **Merge the two copies of this project** — this workspace and the group repository — by
   pull request, so that one plan, one logbook and one requirement register exist
   (`docs/06-DIFFERENTIATION.md` §8).
5. **Rewrite the proposal's novelty section** around ★1–★5, conceding in one sentence that
   five-class classification is already solved in public work.
6. **Merge `scripts/prepare_data.py`** and record the observed dataset counts — this is the one
   artefact no comparable public project ships.

Then follow `docs/02-WEEKLY-PLAN.md` week by week.

---

## Conventions used throughout

- **Guideline § references** point to the *Final Year Project Guideline, BSc in Computer
  Science*, Department of Computer Science, AAU, version 2.0, October 2026.
- **Appendix letters** (A, B, D, F, G, H, I, J, L, M, N) refer to the appendices of that
  guideline.
- **`[PENDING]`** marks a value that must be filled with a measured result before submission.
  Nothing marked `[PENDING]` may appear in a submitted document.
- **`[OBSERVE]`** marks a value that must be replaced by what is actually observed after
  downloading the data, not by the published figure.
- **ADR-##** is an architecture decision record; **R##** is a risk;
  **SO##** is a specific objective; **RQ##** a research question; **FR/NFR/DR##** a
  requirement; **T-##** a test case; **E-##** an evaluation experiment; **F-4.x** a figure;
  **Table 4.x** a table.

---

## Sources and licences

All datasets used are CC BY 4.0 and are attributed in `data/dataset-sources.md` and
`docs/literature/references.md`. **No dataset is redistributed by this project** — the
repository carries the download instructions, the preparation script and the split manifest
only. The group's own code, data manifest and documentation are the group's original work and
are to be released under a licence chosen with the advisor (Guideline §15.5).
