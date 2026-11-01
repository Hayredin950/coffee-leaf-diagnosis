# Chapter 4 — Requirements Analysis and Design

> **Owner:** Bemnet Tesfaye (architecture, database, API) with Yohannes Berhanu (the client
> and interface design), Hayredin Mohammed (the model design) and Nahom Solomon (the
> knowledge base and the requirements) · **Estimated length:** 8–10 pages
>
> **Cross-reference:** the complete requirements specification is
> `docs/requirements/requirements-spec.md`; the architecture, the sequence and state diagrams
> and the design-decision record are `docs/design/architecture.md`; the schema and the API
> contract are `docs/design/database-and-api.md`; the wireframes are
> `docs/design/ui-wireframes.md`.

---

## 4.1 Requirements analysis

### 4.1.1 Requirements elicitation

Requirements were elicited from five sources, and each requirement in the specification
carries the source that produced it.

**Table 4.1** — The requirement sources.

| Source | Technique | Requirements produced |
|---|---|---|
| The problem statement and the gap (Chapter 1) | Traceability from SO1–SO7 | The functional requirements FR-01…FR-37 |
| The literature review (Chapter 2) | The "how the review shaped the design" table in §2.7 | The abstention requirement FR-09; the per-class reporting requirement; the offline requirement FR-08 |
| The prior-art comparison (`docs/literature/comparison-table.md`) | Feature-by-feature gap analysis | FR-11 and FR-35…FR-37 (guidance), FR-14…FR-20 (history), FR-08 (offline) |
| The design of the deployed competitors | Deployment-boundary analysis | FR-21…FR-30 (the API), FR-31…FR-34 (the web client) |
| The guideline's non-functional categories (§7.2) | Checklist against each quality attribute | NFR-01…NFR-35 |

### 4.1.2 The requirement specification

The specification contains **37 functional requirements**, **35 non-functional requirements**
and **8 data requirements**, each with a unique identifier, a priority (Must / Should / May), a
measurable acceptance criterion and a traceability target.

**Table 4.2** — The functional requirements, summarised by area. The complete table, with
every acceptance criterion, is in `docs/requirements/requirements-spec.md`.

| Area | IDs | The essential requirements |
|---|---|---|
| Image acquisition | FR-01…FR-05 | Camera capture; gallery selection; a framing guide; input validation with specific error messages; a photo-quality check with named reasons |
| Inference and diagnosis | FR-06…FR-13 | Exactly five classes; a confidence value for each class summing to 1.0; inference entirely on-device; the acceptance threshold and the retake path; the ranked alternatives; the guidance entry; the advisory notice; the knowledge-base browser |
| Diagnosis history | FR-14…FR-20 | Seven mandatory logged fields; a reverse-chronological list; class and date-range filters; free-text search; deletion; CSV export; persistence across restart and upgrade |
| API service | FR-21…FR-30 | Prediction; history CRUD with filters and pagination; the knowledge base; health; the published metrics; a published OpenAPI schema; authentication on mutating endpoints; upload size and type limits |
| Web client | FR-31…FR-34 | Upload and diagnose; the guidance; the history browser and export; graceful degradation when the API is unreachable |
| Knowledge-base content | FR-35…FR-37 | Ten mandatory fields per class; a citation for every practice; a single versioned JSON shared by both clients |

**Table 4.3** — The non-functional requirements, grouped by the Guideline §7.2 categories.

| Category | IDs | Targets |
|---|---|---|
| Performance | NFR-01…NFR-07 | Median latency ≤ 500 ms and p95 ≤ 1,000 ms on the low-cost device; model ≤ 10 MB; peak memory ≤ 250 MB; shutter-to-result ≤ 2 s; API p95 ≤ 2 s; API availability ≥ 99 %; a history query over 10,000 records ≤ 500 ms |
| Offline operation | NFR-08…NFR-10 | 100 % of the core features pass in airplane mode; the knowledge base is an embedded asset; an explicit notice when a network-dependent feature is unavailable |
| Usability, accessibility, localisation | NFR-11…NFR-16 | SUS ≥ 70 from ≥ 10 participants; ≥ 90 % task success; ≤ 60 s median time on task; ≥ 48 dp touch targets; all strings externalised with English and Amharic resources; Android 8.0+ |
| Security and privacy | NFR-17…NFR-25 | No secrets in the repository; typed validation on every input; content-based upload validation; authentication; rate limiting; dependency scanning; no PII stored; no third-party transmission in the offline core; the advisory notice visible |
| Maintainability and reproducibility | NFR-26…NFR-35 | A README that a newcomer can follow; a single command that reproduces the split and the training; recorded seeds, versions and an environment file; a results-to-script table; ≥ 80 % unit-test coverage on the inference wrapper, the history layer and the API; a stated coding standard; the dataset not committed; configuration separated from code; a demonstrable deployment environment; a third-party licence list |

### 4.1.3 Requirements baseline

Following Guideline §7.3, the specification was presented to the advisor at the requirements
baseline gate in FYP I week 7 and approved before the design phase began. Any later change is
recorded in the change-control table of the specification with its rationale and its effect on
scope, schedule and testing.

**Table 4.4** — The requirement change-control record (to be completed as changes occur).

| Change | Date | Requirement | Rationale | Scope effect | Schedule effect | Testing effect | Approved by |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — |

### 4.1.4 Out-of-scope decisions

Eight features were deliberately excluded, and the reasons are recorded in the specification
§5: detection and bounding-box localisation; disease severity quantification; nutrient
deficiency classification; non-coffee crops; root, stem, berry and soil diagnosis; real-time
video diagnosis; user accounts with automatic cloud synchronisation; and adversarial domain
adaptation. The last deserves a note: the evidence shows DANN-style adversarial adaptation
*degraded* accuracy to 0.252 in a comparable setting [15], so excluding it is a
literature-informed design decision rather than an omission. Excluding it also reduced the
scope of the ablation to something the group could execute properly with three seeds.

---

## 4.2 Design principles

Seven principles governed the design, and each is traceable to a specific piece of evidence.

**Table 4.5** — The design principles and their evidential basis.

| # | Principle | Evidential basis |
|---|---|---|
| P1 | The offline core is the product | Both published mobile applications require a server [11], [12] |
| P2 | One model and one knowledge base, two front-ends | Guarantees that the app and the web client cannot disagree |
| P3 | The model is a data product, not a binary | The artefact ships with labels, metadata and a model card |
| P4 | Abstain rather than guess | Both published model cards advise asking for a better photo below a confidence threshold [14], [27]; the documented failure mode is confident error [15] |
| P5 | Offline data is first-class | The device store is the source of truth for the user's history |
| P6 | Version everything | Every diagnosis carries the model version and the knowledge-base version |
| P7 | Testability is a design constraint | Every module boundary is a seam with a unit test |

---

## 4.3 System architecture

### 4.3.1 Figure 4.1 — the system context

> **Figure 4.1** — System context diagram. The farmer's phone contains everything needed for
> the core flow; the API and the web client are optional and serve extension officers.
> Original work by the group.

### 4.3.2 Figure 4.2 — the component diagram

> **Figure 4.2** — Component diagram of the three deployable components. Within the mobile
> client, the acquisition → validation → quality → preprocessing → inference → calibration →
> abstention chain is the core; the knowledge-base resolver and the repository hang off it.
> Original work by the group.

### 4.3.3 The mobile client

The mobile client is a Flutter application, because one Dart codebase serves Android and iOS,
the TFLite plugin ecosystem is the best supported of the cross-platform options, and a single
language across the team reduces the coordination cost of a four-person project.

The core pipeline is:

```
acquire → validate → quality check → preprocess → TFLite inference
        → temperature scaling → abstention decision → resolve guidance → persist
```

Two design decisions within this pipeline are worth stating explicitly.

**The quality gate precedes inference.** A photograph that is undecodable, undersized,
blurred, badly exposed or shows too little of the leaf is rejected *before* any inference
cost is incurred, and the reason is named to the user ("the photo looks blurry", "please fill
the frame with a single leaf"). This mirrors the field failure modes identified by Barbedo
[16] and converts them into a specific, actionable instruction rather than a low-confidence
result.

**The abstention decision is a separate, explicit step.** It is not a property of the model
file but of the inference contract, and the threshold is read at runtime from the model's
`metadata.json` rather than being hard-coded. The pseudocode is given in
`docs/design/architecture.md` §7 and is reproduced in Chapter 5.

### 4.3.4 The API service and the web client

The API is a FastAPI service exposing ten endpoints under `/v1`, documented by an OpenAPI 3.1
schema that is committed to the repository and validated against the running application in
CI. The web client is deliberately a static HTML/CSS/JavaScript application with no build
step: the contract is guaranteed by the OpenAPI schema, and a build step is a schedule risk in
the final fortnight before the defense.

The API uses a JWT bearer token on all mutating endpoints, validates every input with Pydantic
v2 models, enforces a 20 MB upload limit, validates uploads by their magic bytes rather than
by their extension or their client-supplied MIME type, and rate-limits to 60 requests per
minute per client. The API never fetches a URL supplied by a client — a deliberate decision,
since the "predict by URL" pattern used by one prior-art system [28] is a server-side request
forgery vector.

### 4.3.5 The knowledge base

The knowledge base is a single versioned JSON asset embedded in the application binary and
served identically by the API. Each of the five classes has an entry with ten fields: the
display name, the scientific name, the local names, the distinguishing symptoms, the severity
cues and progression, the risk factors, the organic control, the chemical control, the
prevention, and the source list.

Two constraints govern the content. First, **every field that states a practice carries a
citation**, and a CI job fails the build if any practice is uncited. Second, the chemical
control section names **active-ingredient classes rather than products or dosages**, and
directs the user to a locally registered product and to its label. The app therefore cannot
become the source of an incorrect or illegal dosage recommendation.

### 4.3.6 The deployment

The application is offline-capable and has no startup dependency on the server. The API is
packaged as a single Docker container running as a non-root user behind a TLS-terminating
proxy, with a managed PostgreSQL instance. The model artefact is versioned in the repository
with a SHA-256 checksum that is verified when the model is loaded.

---

## 4.4 Data design

### 4.4.1 The on-device store

The device store is a SQLite database accessed through Drift, providing typed data objects and
a forward-only migration strategy. Two tables suffice: `diagnoses` and `diagnosis_images`. The
`diagnoses` table carries the seven fields required by FR-14 — the UTC timestamp, the image
reference, the predicted class, the top-1 confidence, the full five-class confidence vector,
the model version and the device note — plus the client-generated identifier and the
knowledge-base version.

Two decisions are notable. The identifier is **generated on the device**, which makes an
optional export idempotent: a retried export cannot create duplicates. And the confidence
vector is stored as a single JSON column rather than five scalar columns, because it is read
and written as a unit and its shape may change with the class count in a future model version
— while the top-1 class and confidence remain scalar columns because they are the fields that
are filtered and sorted.

### 4.4.2 The server store

The server store is PostgreSQL with four tables — `diagnosis`, `diagnosis_image`,
`model_version` and `kb_version` — with the same logical schema, the same field names and the
same semantics as the device store, so that an export is a lossless copy. Constraints enforce
the class list, the confidence range, the vector length and the foreign keys to the version
tables, so a diagnosis can never reference a model version that does not exist. The indexes
serve the default history query — a reverse-chronological list, optionally filtered by class —
and the date-range query.

### 4.4.3 Figure 4.3 — the entity-relationship diagram

> **Figure 4.3** — ER diagram. `diagnosis` references exactly one `model_version` and one
> `kb_version`, so that a historic record can always be re-interpreted with the artefact that
> produced it. Original work by the group.

### 4.4.4 Table 4.6 — the data dictionary for the principal table

| Column | Type | Null | Constraint | Meaning |
|---|---|---|---|---|
| `id` | uuid | no | PK | Client-generated UUID v4 |
| `timestamp_utc` | timestamptz | no | — | The moment the diagnosis was produced, in UTC |
| `image_path` | text | no | — | The URI of the stored leaf photograph |
| `label` | text | no | in the five classes | The predicted class key |
| `top1_confidence` | real | no | 0 ≤ x ≤ 1 | The calibrated top-1 probability |
| `confidence_vector` | jsonb | no | 5 elements | The calibrated probability for each class |
| `model_version` | text | no | FK → `model_version` | The artefact that produced the record |
| `kb_version` | text | no | FK → `kb_version` | The knowledge base that interprets it |
| `device_note` | text | yes | — | The user's optional free-text note |
| `notes` | text | yes | — | A second free-text field for the server's use |
| `created_at` | timestamptz | no | default now() | When the row was written |

The full data dictionary, covering all four tables and both implementations, is in
`docs/design/database-and-api.md` §A.3.

### 4.4.5 Transactions, migrations, backup and security

The specification of these is in `docs/design/database-and-api.md` §A.4–A.8. In summary: a
diagnosis write is a single transaction covering both tables; the export uses a
`REPEATABLE READ` snapshot so that a partially-written set cannot be exported; migrations are
forward-only, reviewed by a second member, and covered by test T-40; the seed script contains
no diagnosis records and no personal data; the device store relies on the operating system's
application sandbox; and the server store uses a least-privilege application role separate
from the migration role.

---

## 4.5 User interface design

The interface comprises five screens and a two-tab bottom navigation. The flow is
capture → result → guidance, with the history and the knowledge-base browser available from
every screen.

**Figure 4.4** — The navigation model.

Two interface decisions carry the most weight.

**The low-confidence state replaces the class name rather than greying it.** Showing
"Cercospora Leaf Spot — 38 %" invites the user to act on a guess; showing the *ranking*
without a label is informative and non-misleading. The screen states plainly that the system
could not identify the leaf with enough certainty, offers the best guesses, and asks for a
better photograph with specific suggestions. Both prior-art model cards independently
recommend exactly this behaviour below their confidence thresholds [14], [27].

**The advisory notice is on the result screen, not buried in an about page.** The result
carries a permanent notice that the output is decision support and does not replace an
extension officer, together with the knowledge base's own source attribution.

The wireframes for all five screens, the design tokens, the accessibility rules and the
localisation approach are in `docs/design/ui-wireframes.md`.

---

## 4.6 Technology selection

**Table 4.7** — The technology decision record. The full record, with the alternatives
considered and the reasons for rejection, is in `docs/design/architecture.md` §2.

| Layer | Choice | Principal reason |
|---|---|---|
| Mobile framework | Flutter | One codebase for Android and iOS; the best-supported TFLite plugin; one language for the team |
| On-device runtime | TFLite / LiteRT via `tflite_flutter` | The Model Maker produces the artefact directly; the MediaPipe image-classification task provides a validated pipeline with a score threshold |
| Model architecture | MobileNetV3-Small, compared against EfficientNet-Lite0 and MobileNetV2 | Phone-targeted by construction; the alternatives are the reasonable comparators |
| Quantisation | int8 post-training, with float16 and float32 retained | Demonstrated to shrink plant-disease models without accuracy loss [41] |
| Local database | SQLite via `sqflite`, wrapped in Drift | Typed DAOs, schema versioning and migrations, which FR-20 requires |
| Server database | PostgreSQL | Concurrent writes, indexed queries, `jsonb` for the confidence vector |
| API framework | FastAPI + Pydantic v2 | Automatic OpenAPI generation satisfies FR-28; typed validation satisfies NFR-18 directly |
| Web client | Vanilla HTML/CSS/JS | No build step; the OpenAPI schema guarantees the contract |
| Authentication | JWT bearer tokens | Stateless; works identically for both front-ends |
| CI | GitHub Actions | Free, zero setup, and the repository is already accessible to the advisor and the examiners |

**Rejected alternatives.** React Native was rejected in favour of Flutter because of the
TFLite plugin ecosystem and the team's language familiarity, and because a second language
would slow a four-person team. TensorFlow Lite Micro was rejected because it targets
microcontrollers rather than phones. A fully custom native Android application was rejected
for schedule risk. A cloud-only inference design was rejected because it directly contradicts
the offline requirement. ONNX Runtime Mobile is viable but offers weaker Flutter support and
a less well-documented export path. A microservices split, a message queue, a NoSQL store and
a federated-learning design were each considered and rejected as unjustified for a
single-service, transactional, non-personal-data system.

---

## 4.7 Design verification and traceability

Before the design review, the group ran a design-consistency check (Guideline §7.5), which
confirms that no diagram, requirement, schema, interface and implementation contradicts
another.

**Table 4.8** — The design-consistency checks and their results.

| Check | Result |
|---|---|
| Every endpoint in the API specification exists in the OpenAPI schema and is tested | ☐ |
| The seven FR-14 fields exist as columns in both the device and the server schemas, with matching names and types | ☐ |
| The five label strings are identical across `labels.txt`, the knowledge base, the API enum and the interface | ☐ |
| The acceptance threshold is read from `metadata.json`, and the value in the model card matches | ☐ |
| Every field in the knowledge-base JSON schema is rendered, and nothing is rendered that is not in the schema | ☐ |
| The measured deployed artefact satisfies NFR-02 (≤ 10 MB), not merely the claimed figure | ☐ |
| Every error condition in the architecture document has a test case in Appendix F | ☐ |

The objective-to-evidence traceability matrix (`docs/requirements/traceability-matrix.md`)
is started in this phase and completed in FYP II, as Guideline §10.6 requires.
