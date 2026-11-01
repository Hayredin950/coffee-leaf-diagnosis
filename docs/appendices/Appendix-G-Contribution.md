# Appendix G — Individual Contribution Statement

> **Guideline §14.2:** *"Each member must hold primary technical responsibility for at least one
> major component or work package. The roles are declared in the proposal and recorded again in
> the Individual Contribution Statement (Appendix G)."*
> **§17.7:** the examiners assign an Individual Contribution Factor from the logbook, the
> repository history and this statement.
>
> **Template (Appendix G):** Student name and ID · Group project title · a table of
> *Area · Specific contribution · Evidence · Estimated effort (% of own time)* · a student
> declaration with a signature and a date · an advisor acknowledgement.
>
> **How to complete this.** Each member fills in **their own page**, in their own words, at the
> **end of FYP II (week 29)** — when the effort percentages are real rather than guesses. Keep
> the evidence column concrete: a repository path, a document, a PR number, a logbook week.
> Do not copy another member's page. The advisor acknowledges each page.

---

## Project header (repeated on each page)

| Field | Value |
|---|---|
| **Group project title** | Design and Development of a Coffee Leaf Disease Diagnosis System Using Deep Learning |
| **Group members** | Yohannes Berhanu (UGR/9440/16) · Hayredin Mohammed (UGR/2361/16) · Bemnet Tesfaye (UGR/3266/16) · Nahom Solomon (UGR/3155/16) |
| **Advisor** | Surafiel Habib Asefa |
| **Primary category** | Artificial intelligence and machine learning (Guideline §2.3) |
| **Complexity class** | High (Guideline §2.4) |

---

## Page 1 — Hayredin Mohammed (UGR/2361/16)

**Role:** Data and Model Lead · **Primary work package:** dataset curation, leakage-safe splits,
model training, quantisation, TFLite export, external evaluation and error analysis.

| Area | Specific contribution | Evidence | Estimated effort (% of own time) |
|---|---|---|---|
| **Requirements** | Drafted the data and model requirements (DR-01…DR-08) and the model-facing NFRs (NFR-01…NFR-03, NFR-27…NFR-29); co-authored the evaluation requirements for SO3 | `docs/requirements/requirements-spec.md` §4; traceability matrix §1 | 4 % |
| **Design** | Designed the training pipeline and the duplicate-grouping and split strategy; specified the artefact contract (`model.tflite` + `labels.txt` + `metadata.json` + `model-card.md`); defined the evaluation protocol for the five external datasets | `docs/design/architecture.md` §5, §6; `docs/literature/ch2-literature-review.md` §2.2 | 6 % |
| **Implementation** | Wrote `scripts/prepare_data.py` (grouping, stratified grouped split, manifest with checksums); wrote `training/train.py`, `training/evaluate_internal.py`, `training/evaluate_external.py`, `training/calibrate.py`, `training/ablate.py`, `training/significance.py`; wrote `model/export_tflite.py`; produced the float32, float16 and int8 artefacts | `scripts/prepare_data.py`; `training/`; `model/` — commit history under `hayredin` | 20 % |
| **Database or data** | Curated and documented nine datasets from six countries; produced `data/dataset-sources.md` and `data/datasheet.md`; recorded the exact observed class counts and the discrepancies against the published counts; preserved the out-of-taxonomy classes as a distinct `unsupported` label | `data/datasheet.md`; `data/split_manifest.csv`; `data/dataset-sources.md` | 12 % |
| **Testing** | Executed T-01…T-16 and E-01…E-07; wrote the split-integrity audit; ran the ablation, the calibration and the McNemar significance test; measured the latency on three devices | `docs/appendices/Appendix-F-Test-Cases.md` §F.2, §F.3; `results/E-*.csv` | 10 % |
| **Documentation** | Wrote the datasheet, the model card and the results-to-script table; wrote the reproducibility instructions | `data/datasheet.md`; `data/model-card.md`; `results.md`; Chapter 6 draft | 8 % |
| **Other** | Obtained the written data-access permission from the JMuBEN author; maintained the dataset risk register entries; ran the weekly cross-review of the app and the API packages | Email correspondence; `docs/04-RISK-REGISTER.md`; PR reviews in the repository history | 6 % |

**Total: ___ %** (must sum to 100)

**Student declaration:** I certify that the contribution described above accurately represents
my work, subject to the University's academic-integrity rules.

**Student signature:** ________________________  **Date:** ____________

**Advisor acknowledgement:** ________________________  **Date:** ____________

---

## Page 2 — Yohannes Berhanu (UGR/9440/16)

**Role:** Mobile App and UI/UX Lead, and Project Lead · **Primary work package:** the Flutter
client — capture and upload, on-device inference, the result and guidance screens, offline
operation and the local diagnosis history — plus repository governance.

| Area | Specific contribution | Evidence | Estimated effort (% of own time) |
|---|---|---|---|
| **Requirements** | Co-authored the functional requirements for acquisition, inference, the result screen and the history; specified the UI state model and the abstention user experience | `docs/requirements/requirements-spec.md` §2.1–§2.3; `docs/design/ui-wireframes.md` | 6 % |
| **Design** | Designed the four screens and the navigation model; wrote the wireframes and the accessibility checklist; designed the offline-first interaction model and the photo-quality gate | `docs/design/ui-wireframes.md` (Figures 4.10–4.14) | 8 % |
| **Implementation** | Built the Flutter application: camera and gallery acquisition, the image validator, the quality gate, the preprocessing pipeline, the TFLite interpreter integration, the calibrator, the abstention policy, the KB resolver, the SQLite/Drift repository with migrations, the history screen with search and filter, and the CSV exporter; implemented the localisation scaffolding | `mobile/lib/` — commit history under `yohannes` | 24 % |
| **Database or data** | Designed and implemented the on-device SQLite schema, the DAOs and the forward-only migration strategy | `mobile/lib/data/`; migration test T-40 | 5 % |
| **Testing** | Executed T-17…T-40 and T-65; wrote the golden-image preprocessing test that proves the Dart and Python pipelines agree; ran the airplane-mode and packet-capture verification; co-executed the web client cases | `docs/appendices/Appendix-F-Test-Cases.md` §F.4, §F.7; `evidence/` | 10 % |
| **Documentation** | Wrote the installation guide, the user guide, the on-device troubleshooting section and the model-card usage notes | `docs/appendices/Appendix-I-J-Checklists.md`; Chapter 5 draft | 7 % |
| **Other** | Maintained the APK build pipeline and the release signing for the defence build; produced the demo script and the recorded backup video; created and governed the repository — branch protection, PR templates, the issue board, the milestone tags; managed the advisor and examiner access; ran the weekly cross-review of the model and the deployment packages | `mobile/` release notes; `docs/defense/slides-and-demo.md`; repository settings history | 6 % |

**Total: ___ %**

**Student declaration:** I certify that the contribution described above accurately represents
my work, subject to the University's academic-integrity rules.

**Student signature:** ________________________  **Date:** ____________

**Advisor acknowledgement:** ________________________  **Date:** ____________

---

## Page 3 — Bemnet Tesfaye (UGR/3266/16)

**Role:** Backend and Platform Lead · **Primary work package:** the REST API, the server-side
database, the knowledge-base implementation, deployment, security, CI and the reproducibility
package.

| Area | Specific contribution | Evidence | Estimated effort (% of own time) |
|---|---|---|---|
| **Requirements** | Co-authored the API and web-client functional requirements and the security, availability, performance and reproducibility NFRs | `docs/requirements/requirements-spec.md` §2.4–§2.5, §3 | 5 % |
| **Design** | Designed the system architecture, the component and deployment diagrams, the API contract, the server-side relational schema, the data dictionary and the transaction and migration strategy | `docs/design/architecture.md` (Figures 4.1–4.8); `docs/design/database-and-api.md` | 10 % |
| **Implementation** | Built the FastAPI service with Pydantic v2 validation, JWT authentication, rate limiting, the SQLAlchemy models and the Alembic migrations; built the static web client; wrote the Dockerfile, the deployment pipeline and the health and metrics endpoints; implemented the versioned knowledge-base JSON asset with its checksum | `api/`; `web/`; `docker/` — commit history under `bemnet` | 20 % |
| **Database or data** | Implemented the PostgreSQL schema with its constraints and indexes, the migration scripts and the seed data; implemented the transaction and idempotency rules | `api/app/models.py`; `api/migrations/`; `scripts/seed.sql` | 6 % |
| **Testing** | Executed T-51…T-60 and T-63; set up CI with lint, unit tests, the container build, the model-artefact check, the KB audit and the secret scan; ran the OWASP ZAP baseline against the group's own staging deployment; wrote the security checklist | `docs/appendices/Appendix-F-Test-Cases.md` §F.5; `.github/workflows/` | 12 % |
| **Documentation** | Wrote the technical documentation and the installation guide; wrote the third-party licence list; assembled the final submission package; maintained the risk register | `docs/appendices/Appendix-I-J-Checklists.md`; `THIRD_PARTY_LICENSES.md` | 8 % |
| **Other** | Produced the reproducibility package and the deployment runbook; maintained the staging environment through the design review; ran the weekly cross-review of the app and the data packages | Repository settings history; `docs/05-DECISION-LOG.md` | 5 % |

**Total: ___ %**

**Student declaration:** I certify that the contribution described above accurately represents
my work, subject to the University's academic-integrity rules.

**Student signature:** ________________________  **Date:** ____________

**Advisor acknowledgement:** ________________________  **Date:** ____________

---

## Page 4 — Nahom Solomon (UGR/3155/16)

**Role:** Research, Requirements and Quality Lead · **Primary work package:** the literature
review and gap analysis, the requirements specification, the test plan, the agronomic knowledge
base, the ethics screening, the usability study, and the report integration.

| Area | Specific contribution | Evidence | Estimated effort (% of own time) |
|---|---|---|---|
| **Requirements** | Authored the requirements specification with unique IDs, priorities and measurable acceptance criteria; wrote the traceability matrix; authored the test plan and the test-case register; authored the risk register with the advisor | `docs/requirements/requirements-spec.md`; `docs/requirements/traceability-matrix.md`; `docs/requirements/test-plan.md`; `docs/04-RISK-REGISTER.md` | 14 % |
| **Design** | Designed the knowledge-base schema with its ten fields and its citation model; contributed the agricultural interpretation of the evaluation design; defined the evidence structure of the report | `data/knowledge-base.md`; `docs/design/architecture.md` §10 | 6 % |
| **Implementation** | Curated the agronomic knowledge base for all five classes from FAO, peer-reviewed Ethiopian literature and the APS taxonomy; ran the citation audit; built the literature-review evidence tables; assembled the report chapters and the presentation | `data/knowledge_base.json`; `docs/literature/`; `docs/report/` | 14 % |
| **Database or data** | Verified the provenance, licensing and citation of all nine datasets; compiled the datasheet content and the reference list; verified every DOI against the publisher record | `data/datasheet.md`; `docs/literature/references.md` | 6 % |
| **Testing** | Executed the usability study with the consent procedure, the SUS analysis and the comprehension check; compiled all the test evidence into Appendix F; performed the final consistency audit across the requirements, the design and the implementation | `docs/appendices/Appendix-F-Test-Cases.md` §F.9; `docs/requirements/test-plan.md` §8 | 8 % |
| **Documentation** | Wrote Chapters 1, 2, 6 and 7 and integrated Chapters 3–5; formatted the whole document to the Department standard; wrote the abstract, the front matter and the Appendix L AI-use declaration; maintained the logbook template | `docs/report/`; `docs/appendices/Appendix-L-AI-Disclosure.md`; `docs/appendices/Appendix-B-Logbook.md` | 14 % |
| **Other** | Completed the Appendix M ethical screening and the advisor/Committee approval workflow; coordinated the advisor meetings and the weekly logbook discipline; conducted the 15-source literature verification; ran the weekly cross-review of the data and the deployment packages | `docs/appendices/Appendix-M-Ethics.md`; `docs/appendices/Appendix-B-Logbook.md` | 4 % |

**Total: ___ %**

**Student declaration:** I certify that the contribution described above accurately represents
my work, subject to the University's academic-integrity rules.

**Student signature:** ________________________  **Date:** ____________

**Advisor acknowledgement:** ________________________  **Date:** ____________

---

## Group-level statement

The four work packages above cover every element of the delivered system: the data and the
model, the mobile client, the API and the platform, and the research and the documentation. Each
member holds primary technical responsibility for one major component, as §14.2 requires, and
each member has contributed across all seven Appendix G areas.

**Effort distribution check (must be roughly equal):**

| Member | Requirements | Design | Implementation | Data | Testing | Documentation | Other | Total |
|---|---|---|---|---|---|---|---|---|
| Hayredin | | | | | | | | |
| Bemnet | | | | | | | | |
| Yohannes | | | | | | | | |
| Nahom | | | | | | | | |
| **Mean** | | | | | | | | |

**If one member's total is more than 15 percentage points above another's, the group must
explain why in a note below and raise it with the advisor — §14.4 and §17.7 make individual
contribution a scored factor, and an unexplained imbalance is a risk.**

> Note: ____________________
> ____________________
> ____________________

---

## Advisor acknowledgement (group)

I confirm that the contributions described above are consistent with the repository history and
the weekly progress log, and that each member has demonstrated an understanding of the whole
system in addition to their own modules.

**Advisor name:** Surafiel Habib Asefa  **Signature:** ____________________  **Date:** ____________
