# Appendix I — Final Submission Checklist
# Appendix J — Technical Documentation Checklist

> **Guideline §16.4:** *"The final submission package consists of the final report; source
> code; database and scripts where applicable; the executable or deployed system where
> applicable; the dataset where permitted; the installation guide; the user guide; testing
> evidence; the presentation slides; the logbook; the individual contribution statement; the
> AI-use declaration; the similarity report; the reproducibility package for AI and data
> projects; and the required declarations and approvals."*

---

# Appendix I — Final Submission Checklist

**Owner:** Yohannes Berhanu (assembly) · **Audit:** Nahom Solomon · **Sign-off:** all four
**Target date:** end of FYP II week 29 (9 May 2027), with the corrections in weeks 31–32.

## I.1 Documents

- [ ] **Approved final report** — searchable PDF **and** the editable source (DOCX or LaTeX) (§11.12)
- [ ] The file is named with the group identifier, the course and the year (§11.12)
- [ ] The report contains the complete structure of Table 11.1: front matter, Chapters 1–7, back matter
- [ ] Title page follows the Appendix K template, in the specified order and sizes
- [ ] Declaration page signed by all four members, including the AI-disclosure sentence (§15.3)
- [ ] Approval sheet signed by the advisor; the examiners' names added after the defense
- [ ] Abstract of 200–300 words with keywords
- [ ] Table of contents, list of tables, list of figures, list of abbreviations
- [ ] The document uses Times New Roman 12 pt, 1.5 line spacing, and the margins of Table 11.3
- [ ] Page numbering: no number on the title page; lower-case Roman before Chapter 1; Arabic from Chapter 1, aligned right
- [ ] Headers: the project title on odd pages, the chapter title on even pages, none on the first page of a chapter
- [ ] Every table and figure is numbered per chapter, captioned, and referred to in the text
- [ ] Every figure is legible in print; every borrowed figure is credited in its caption (§11.7)
- [ ] Equations are numbered at the right margin with every symbol defined
- [ ] Code listings use Courier New 10 pt, single-spaced
- [ ] References are in IEEE format, numbered in order of first citation (§11.11)
- [ ] No AI tool appears in the reference list (§11.11)

## I.2 Code and repository

- [ ] **Source code** in the group repository, with the full history preserved
- [ ] The repository is accessible to the advisor and to the examiners (§8.4)
- [ ] Every member's commits are under their own identity (§8.4)
- [ ] Branches, pull requests, issue tracking and milestone tags are used (§8.4)
- [ ] `README.md` explains how to build and run the system (§8.1)
- [ ] No secrets, keys or credentials are committed (§8.3)
- [ ] `.env.example` exists; `.env` is gitignored (§8.5)
- [ ] Configuration is separated from code (§8.5)
- [ ] A coding standard is stated and enforced by linting (§8.1)
- [ ] The repository size is < 50 MB — the datasets are not committed (NFR-32)
- [ ] `THIRD_PARTY_LICENSES.md` lists every third-party library, dataset and media item with its licence (§15.5)
- [ ] The release is tagged and a snapshot is archived (§16.5)

## I.3 The system

- [ ] **The executable or deployed system** — the Android APK, installed and demonstrable
- [ ] The web client is deployed and reachable
- [ ] The API's OpenAPI schema is committed at `api/openapi.json`
- [ ] **Database scripts** — the migrations, the seed script and the schema documentation
- [ ] The seed data contains no real personal data (§8.2)
- [ ] The system is demonstrable in an environment available at the defense (§8.5)
- [ ] A **recorded demonstration** is kept as a backup (§17.2)

## I.4 Data and models

- [ ] **The dataset**, where permitted — otherwise the download procedure with URLs and a split manifest
- [ ] `data/datasheet.md` — the data description (§9.2, §9.6)
- [ ] `data/model-card.md` — the model description (§9.6)
- [ ] `data/knowledge_base.json` with its version and the checksum
- [ ] The licence and attribution for every dataset, with the record IDs cited explicitly

## I.5 Documentation

- [ ] **Installation guide** (§8.6, Appendix J)
- [ ] **User guide** (§8.6, Appendix J)
- [ ] **Testing evidence** — Appendix F with the actual results, plus the evidence files
- [ ] **Evaluation results** — Chapter 6 and the `results/` folder
- [ ] **Presentation slides** (§12.4)
- [ ] **Logbook** — 32 weekly entries with the advisor's initials (Appendix B)
- [ ] **Individual contribution statement** — Appendix G, one signed page per member
- [ ] **Generative-AI use declaration** — Appendix L, complete and signed (§15.3)
- [ ] **Similarity report** — from the tool the Committee specifies, with the overall score < 20 % and no single source above 5 % (§15.2)
- [ ] **Reproducibility package** (§9.7) — the code, the configuration, the environment file, the instructions for obtaining the data, the trained model or the training script, and the table linking each result to its script
- [ ] **Ethical approval documents** where applicable — Appendix M, signed (§15.4)
- [ ] **The required declarations and approvals** — the declaration page, the approval sheet, the advisor's progress assessment (Appendix C) for each member
- [ ] The traceability matrix is complete, with an achievement status for every objective (§10.5, Appendix E)

## I.6 Assembly

- [ ] The package is assembled as a single archive plus a repository link
- [ ] The archive's file names follow the convention `<group>_<course>_<year>_<item>`
- [ ] Every item in this checklist is present in the archive, not only in the repository
- [ ] A copy of the checklist, with the items ticked, is included in the archive as evidence of completeness

## I.7 Sign-off

| Item | Verified by | Date |
|---|---|---|
| I.1 Documents | Nahom Solomon | |
| I.2 Code and repository | Yohannes Berhanu | |
| I.3 The system | Yohannes Berhanu | |
| I.4 Data and models | Hayredin Mohammed | |
| I.5 Documentation | Nahom Solomon | |
| I.6 Assembly | Yohannes Berhanu | |
| Final review | All four + advisor | |

---

# Appendix J — Technical Documentation Checklist

> **Guideline §8.6:** *"The submission must include the technical documentation described in
> Appendix J, together with an installation guide and a user guide."*
> **Owner:** Yohannes Berhanu, with Bemnet Tesfaye for the technical documentation.

| # | Item | Where it lives | Status |
|---|---|---|---|
| 1 | **System overview and architecture** | `docs/design/architecture.md`; Chapter 4 | ☐ |
| 2 | **Installation prerequisites and dependencies** | `INSTALLATION.md` — the list of prerequisites (Git, Python 3.11, Flutter 3.x, the Android SDK, Docker) and the versions used | ☐ |
| 3 | **Configuration and environment variables** | `.env.example` per service; a table of every variable, its purpose, whether it is required and its default | ☐ |
| 4 | **Database setup and migration instructions** | `api/README.md` — how to run the migrations against a fresh database; `mobile/README.md` — the schema version and the migration behaviour | ☐ |
| 5 | **API documentation** | The generated OpenAPI at `/docs`, plus the committed `api/openapi.json`, plus `docs/design/database-and-api.md` §B | ☐ |
| 6 | **Authentication and authorisation model** | JWT bearer tokens; the scopes; how a token is obtained and rotated | ☐ |
| 7 | **Testing instructions** | `docs/requirements/test-plan.md`; `scripts/run_tests.sh` for the unit and integration suites; how to run the model evaluation | ☐ |
| 8 | **Known limitations and defects** | Chapter 6 and §7; the unresolved defect list from Appendix F | ☐ |
| 9 | **Deployment instructions** | `docker/`; `docs/deployment.md` — how to build the image, push it, run the migrations and deploy; how to roll back | ☐ |
| 10 | **Backup and recovery considerations** | `docs/design/database-and-api.md` §A.7 | ☐ |
| 11 | **Third-party libraries and licences** | `THIRD_PARTY_LICENSES.md` | ☐ |
| 12 | **Data description** | `data/datasheet.md` | ☐ |
| 13 | **Model description** | `data/model-card.md` | ☐ |
| 14 | **Security considerations** | `docs/design/architecture.md` §12; the OWASP checklist; the secret-scanning result | ☐ |

## J.1 Installation guide — required sections

- [ ] The prerequisites, with exact versions and the operating system
- [ ] The clone-and-build steps for the model pipeline, the API and the mobile client
- [ ] How to obtain the datasets (the URLs, the licences, the expected sizes and the checksums) and how to produce the split with one command
- [ ] How to train the model and how long it takes on the reference hardware
- [ ] How to run the tests
- [ ] How to run the API locally, including the database container
- [ ] How to build and install the APK on a device
- [ ] A troubleshooting section covering the most common failures: the TFLite delegate failing to load, the Flutter Gradle version mismatch, the camera permission being denied, and the API refusing the local database connection
- [ ] The expected run time and the disk space required

## J.2 User guide — required sections

- [ ] What the app does, in one paragraph, aimed at a farmer or an extension officer
- [ ] The installation and the permissions (camera, storage)
- [ ] The four-step usage guide: photograph → diagnosis → guidance → history
- [ ] **What the colours and icons mean**
- [ ] What to do when the app says it is not confident enough (this is the most important section of the guide)
- [ ] How to search, filter, delete and export the history
- [ ] How the app works offline, and what does not work offline
- [ ] The disclaimer, quoted exactly as it appears in the app
- [ ] A FAQ covering the questions the usability study actually surfaced
- [ ] A one-page quick reference card, printable

## J.3 A note on the honesty of the user guide

The user guide must not overstate the system's capability. It must say plainly that the
app is decision support, that the guidance is advisory, and that an extension officer should
confirm a diagnosis before treatment is applied. A guide that oversells is a worse artefact
than no guide, and the examiner will notice.
