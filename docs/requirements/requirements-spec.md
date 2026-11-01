# Software Requirements Specification

**Project:** Design and Development of a Coffee Leaf Disease Diagnosis System Using Deep Learning
**Version:** 1.0 (Requirements Baseline)
**Status:** ☐ Draft ☐ Advisor-reviewed ☐ **Approved as baseline** (Guideline §7.3 — gate falls in FYP I weeks 5–7)
**Owner:** Nahom Solomon · **Contributors:** Bemnet Tesfaye (app testability), Yohannes Berhanu (security/deployment NFRs), Hayredin Mohammed (model NFRs)

**Notation.** *Must* / *Should* / *May* follow Guideline §1.5. Every requirement has a unique ID,
a priority, a traceability target (objective → design → test), and a measurable acceptance
criterion. A requirement with no measurable acceptance criterion is not a requirement (§7.1, §7.2).

---

## 1. System context

**Coffee Leaf Disease Diagnosis System (CLDDS)** — a system with three components:

| Component | Name | Deployment | Network |
|---|---|---|---|
| C1 | **Mobile client** (Flutter, Android/iOS) | User's device | **Not required** |
| C2 | **API service** (FastAPI) | Container host | Required for C3 only |
| C3 | **Web client** (static) | Browser | Required |

The **offline core** (capture → inference → result → guidance → history) lives entirely in C1
and must function with the radio off. C2 and C3 are optional enhancements: they exist to serve
extension officers and to provide a laptop demonstrable at the defense.

### 1.1 Actors

| Actor | Description | Interaction |
|---|---|---|
| **Farmer** | Smallholder coffee farmer; may have limited literacy, limited connectivity, a low-end Android device | Capture → read result → read guidance → review history |
| **Extension officer** | Coffee and tea extension worker covering many sites; has a laptop and intermittent connectivity | Upload → diagnose → record → export |
| **Plant pathologist / JARC reviewer** | Reviews the agronomic knowledge base; may inspect the exported records | Reviews KB entries and CSV exports |
| **System administrator** | Group member deploying and maintaining the service | Deploys, monitors, rotates credentials |
| **Developer** | Group member | Builds, tests, maintains |

---

## 2. Functional requirements

### 2.1 Image acquisition (mobile)

| ID | Requirement | Priority | Acceptance criterion | Traces to |
|---|---|---|---|---|
| FR-01 | The mobile client shall capture a photograph of a coffee leaf using the device camera | Must | With the camera permission granted, a captured frame is delivered to the inference pipeline within 1 s of shutter, at ≥640×480 | SO4, FR-16 |
| FR-02 | The mobile client shall allow the user to select an image from the device gallery | Must | A selected image is delivered to the inference pipeline; the original file is not modified | SO4, FR-16 |
| FR-03 | The mobile client shall present a live camera preview with framing guidance (single leaf, in focus, no glare) | Should | The preview shows a visible guide overlay before capture | SO4, FR-15 |
| FR-04 | The mobile client shall validate the captured or selected image and reject it with a specific message if it is not a decodable image, is smaller than 64×64, or exceeds 20 MB | Must | Four invalid-input test cases each produce the specified error message; no crash in 100 attempts | SO4, NFR-07 |
| FR-05 | The mobile client shall perform a photo-quality check (resolution, mean luminance, sharpness proxy, dominant-colour ratio) before inference | Should | A low-quality photo triggers the "retake" path with the reason named (blurred / too dark / too bright / leaf too small) | SO3, SO4 |

### 2.2 Inference and diagnosis

| ID | Requirement | Priority | Acceptance criterion | Traces to |
|---|---|---|---|---|
| FR-06 | The mobile client shall classify the image into exactly one of five classes: Coffee Leaf Rust, Cercospora Leaf Spot, Leaf Miner, Phoma Leaf Spot, Healthy | Must | The predicted label is always one of the five; no other label can be emitted | SO2, SO4 |
| FR-07 | The mobile client shall return a confidence value for **each** of the five classes, summing to 1.0 | Must | The sum of the five confidences is 1.0 ± 1e-5 for 1,000 random inputs | SO3, SO4 |
| FR-08 | The mobile client shall run inference **entirely on the device**, without any network request | Must | Airplane-mode test: all of FR-01 → FR-13 pass with the radio off; verified by packet capture during the test | SO4, NFR-04 |
| FR-09 | The mobile client shall apply a confidence-acceptance threshold and, when the top-1 confidence is below the threshold, shall not present a diagnosis but shall ask the user to retake the photograph | Must | At the configured threshold, all below-threshold predictions produce the retake path; the threshold value is recorded in the model card | SO3, SO4 |
| FR-10 | The mobile client shall display, alongside the prediction, the confidence value and the ranked alternative classes | Should | The result screen shows the top-1 confidence and at least the top-3 classes | SO3, SO4 |
| FR-11 | The mobile client shall display, for the predicted class, the corresponding agronomic guidance entry | Must | Every one of the five classes has a KB entry and renders on the result screen | SO5 |
| FR-12 | The mobile client shall include an explicit advisory notice that the result is decision support and does not replace an extension officer | Must | The notice is visible on the result screen without scrolling for the default device size | SO5, §15.4 |
| FR-13 | The mobile client shall allow the user to view the full knowledge base for all five classes, not only the predicted one | Should | A KB list screen shows all five classes and opens any of them | SO5 |

### 2.3 Diagnosis history

| ID | Requirement | Priority | Acceptance criterion | Traces to |
|---|---|---|---|---|
| FR-14 | The mobile client shall record every completed diagnosis in a local database with: UTC timestamp, image reference, predicted class, top-1 confidence, full five-class confidence vector, model version, and device note | Must | 100 % of completed diagnoses appear in the history; the record contains all seven fields | SO6 |
| FR-15 | The mobile client shall display the diagnosis history as a reverse-chronological list | Must | The list is ordered newest-first and shows class, confidence and timestamp | SO6 |
| FR-16 | The mobile client shall allow the user to filter the history by class and by date range | Must | Filtering by each class returns only that class; an empty result shows an explicit empty state | SO6 |
| FR-17 | The mobile client shall allow the user to search the history by free text across class and notes | Should | A search for a class name returns matching records | SO6 |
| FR-18 | The mobile client shall allow the user to delete a history record, with confirmation | Should | After deletion the record is absent after an app restart | SO6 |
| FR-19 | The mobile client shall export the full diagnosis history to a CSV file | Must | The exported CSV has one row per record with a header, and opens in a spreadsheet | SO6 |
| FR-20 | The mobile client shall persist the diagnosis history across app restarts and app upgrades (schema migration) | Must | A record written at schema v1 is readable at schema v2 after an upgrade; the migration test passes | SO6, NFR-10 |

### 2.4 API service

| ID | Requirement | Priority | Acceptance criterion | Traces to |
|---|---|---|---|---|
| FR-21 | The API shall expose `POST /v1/predict`, accepting a multipart image upload and returning the predicted class, the five confidences, and the model version | Must | The endpoint returns HTTP 200 with the documented schema for a valid image, and HTTP 422 for a non-image | SO4, SO6 |
| FR-22 | The API shall expose `GET /v1/diagnoses` supporting class, date-range and pagination filters | Must | Filters are applied server-side; the response is paginated with a documented page size | SO6 |
| FR-23 | The API shall expose `GET /v1/diagnoses/{id}` returning a single diagnosis | Must | Returns 200 for a known id and 404 for an unknown id | SO6 |
| FR-24 | The API shall expose `DELETE /v1/diagnoses/{id}` | Should | Deletes the record and returns 204; returns 404 for an unknown id | SO6 |
| FR-25 | The API shall expose `GET /v1/kb` and `GET /v1/kb/{class}` returning the agronomic knowledge base | Must | All five classes are retrievable; each entry contains its sources | SO5 |
| FR-26 | The API shall expose `GET /v1/health` returning service status and the deployed model version | Must | Returns 200 with `status: "ok"` and a model version string | NFR-05 |
| FR-27 | The API shall expose `GET /v1/metrics` returning the server's aggregate evaluation metrics (macro-F1 per dataset) | Should | The metrics correspond exactly to the numbers in the report | SO3, SO7 |
| FR-28 | The API shall publish an OpenAPI schema describing every endpoint | Must | `/docs` renders and the schema validates all requests and responses in CI | NFR-10 |
| FR-29 | The API shall require authentication for all mutating endpoints | Must | An unauthenticated POST /v1/predict returns 401 | NFR-07 |
| FR-30 | The API shall enforce a maximum upload size and a restricted set of accepted content types | Must | A 25 MB upload returns 413; a `.txt` renamed to `.jpg` is rejected | NFR-07 |

### 2.5 Web client

| ID | Requirement | Priority | Acceptance criterion | Traces to |
|---|---|---|---|---|
| FR-31 | The web client shall allow the user to upload an image and receive a diagnosis | Must | Uploading a sample image returns a result within 5 s on the deployment network | SO4 |
| FR-32 | The web client shall display the agronomic guidance for the returned class | Must | Guidance renders identically to the mobile client | SO5 |
| FR-33 | The web client shall allow the user to browse, filter and export the diagnosis history | Must | The same filter semantics as FR-16 are honoured | SO6 |
| FR-34 | The web client shall degrade gracefully when the API is unreachable, showing a clear error rather than a blank screen | Must | Killing the API produces an explicit error message within 5 s | NFR-05 |

### 2.6 Knowledge base content (non-functional, but functional in effect)

| ID | Requirement | Priority | Acceptance criterion | Traces to |
|---|---|---|---|---|
| FR-35 | Each of the five class KB entries shall contain: scientific name, common/local names, distinguishing symptoms, severity cues and progression, risk factors, organic control, chemical control, prevention, and a source list | Must | A schema check confirms all 10 fields are present and non-empty for all 5 classes | SO5 |
| FR-36 | Every KB field that states a chemical or cultural practice shall cite at least one peer-reviewed or institutional source | Must | No uncited practice; the citation check is automated in CI | SO5, §15.5 |
| FR-37 | The KB shall be versioned and stored in a single JSON asset shared by the mobile and web clients | Should | One file, one version field, referenced by both clients | SO5, NFR-10 |

---

## 3. Non-functional requirements

### 3.1 Performance

| ID | Requirement | Target | Measurement method | Traces to |
|---|---|---|---|---|
| NFR-01 | Inference latency on the **low-cost reference device** | Median ≤ 500 ms; p95 ≤ 1,000 ms | 50 runs on an idle device, warm cache, timing inside the app | SO4, RQ3 |
| NFR-02 | Deployed model size (`.tflite`) | ≤ 10 MB | File size on disk | SO4, RQ3 |
| NFR-03 | Peak application memory | ≤ 250 MB | Android Studio profiler / `adb shell dumpsys meminfo` | SO4 |
| NFR-04 | Time from shutter to rendered result | ≤ 2,000 ms | End-to-end timing with a stopwatch over 20 captures | SO4 |
| NFR-05 | API response time, p95, for a 224×224 upload | ≤ 2,000 ms | `hey`/Locust against the staging deployment | SO4 |
| NFR-06 | API availability during the evaluation and defense window | ≥ 99 % | Uptime check every 5 min | NFR-05 |
| NFR-07 | History query latency for 10,000 records | ≤ 500 ms | Benchmarked against a seeded 10k-record database | SO6 |

### 3.2 Offline and connectivity

| ID | Requirement | Target | Traces to |
|---|---|---|---|
| NFR-08 | Every core mobile feature (FR-01…FR-13, FR-14…FR-20) shall operate with no network at all | 100 % pass in airplane mode | SO4, SO6 |
| NFR-09 | The knowledge base shall be embedded in the application binary as an asset | No network access, no runtime download | SO5 |
| NFR-10 | The application shall present an explicit, non-blocking notice when it detects that a network-dependent optional feature is unavailable | Notice shown; core flow unaffected | SO4 |

### 3.3 Usability, accessibility and localisation

| ID | Requirement | Target | Traces to |
|---|---|---|---|
| NFR-11 | System Usability Scale score | ≥ 70 from ≥10 participants | SO7, §10.4 |
| NFR-12 | Task success rate on "capture → diagnosis → read guidance" | ≥ 90 % of participants | SO7 |
| NFR-13 | Time on task for the core flow | ≤ 60 s median | SO7 |
| NFR-14 | Minimum touch target | ≥ 48×48 dp on all interactive elements | §7.2 |
| NFR-15 | All user-facing strings shall be externalised, with English and Amharic resources | 100 % of strings in the localisation files | §9.6 |
| NFR-16 | Minimum supported platform | Android 8.0 (API 26); a clear message on unsupported devices | SO4 |

### 3.4 Security, privacy and ethics

| ID | Requirement | Target | Traces to |
|---|---|---|---|
| NFR-17 | No secret, key or credential shall be committed to the repository | `gitleaks`/`trufflehog` clean in CI | §8.3 |
| NFR-18 | All API inputs shall be validated and typed | Pydantic v2 models on every endpoint; a malformed request returns 422, never 500 | §8.3 |
| NFR-19 | Uploaded files shall be validated by content, not by extension or client-supplied MIME type | Magic-byte check; a renamed non-image is rejected | §8.3 |
| NFR-20 | The API shall authenticate mutating requests | Token-based auth; 401 on missing/invalid token | §8.3 |
| NFR-21 | The API shall rate-limit requests | ≥ 60 req/min per client; 429 beyond | §8.3 |
| NFR-22 | Dependencies shall be scanned for known vulnerabilities | No unmitigated high/critical finding | §8.3 |
| NFR-23 | The system shall store no personally identifiable information; leaf photographs shall be the only user content | Schema review confirms no PII fields | §15.4 |
| NFR-24 | The application shall transmit no user data to any third-party service in its offline core | Packet capture shows no outbound request during the core flow | §15.3, §15.4 |
| NFR-25 | The application shall present the advisory notice and the KB's source attribution | Visible on the result screen | §15.4 |

### 3.5 Maintainability, reproducibility and portability

| ID | Requirement | Target | Traces to |
|---|---|---|---|
| NFR-26 | The repository shall include a README explaining how to build and run the system | Present, and verified by a clean-room follow-up | §8.1 |
| NFR-27 | A single documented command shall reproduce the data split and the training run | `make reproduce` or an equivalent; verified from a clean clone | §9.3, §9.7 |
| NFR-28 | Random seeds, library versions and an environment file shall be recorded for every reported result | `seeds.yaml`, `requirements.lock`, `environment.yml` | §9.3 |
| NFR-29 | A table shall link each reported result to the script that produced it | `results.md` in the repository | §9.7 |
| NFR-30 | Unit-test coverage on the inference wrapper, history layer and API | ≥ 80 % line coverage | §8.1, §10.1 |
| NFR-31 | The code shall follow a stated coding standard, with meaningful names and comments where logic is non-obvious | PEP 8 (Python) / `flutter analyze` clean + `analysis_options.yaml` (Dart) | §8.1 |
| NFR-32 | The dataset shall not be committed; instead, a documented download procedure and a split manifest shall be provided | Repo size < 50 MB; `data/README.md` with URLs | §8.5 |
| NFR-33 | Configuration shall be separated from code | `.env.example` per service; no hard-coded hosts or keys | §8.5 |
| NFR-34 | The system shall be demonstrable in an environment available at the defense | Mobile APK + web URL + a recorded backup video | §8.5 |
| NFR-35 | Third-party libraries, data and media shall be listed with their licences | `THIRD_PARTY_LICENSES.md` | §15.5 |

---

## 4. Data requirements

| ID | Requirement | Target | Traces to |
|---|---|---|---|
| DR-01 | The training corpus shall comprise at least four independently licensed public sources | ≥ 4 sources, ≥ 3 countries, all CC BY 4.0 or compatible | SO1 |
| DR-02 | The corpus shall contain ≥ 58,000 labelled images across the five classes | ≥ 58,000 | SO1 |
| DR-03 | Every image shall be assigned to exactly one of train / validation / test | 100 %, with the partition summing to the total | SO1, NFR-27 |
| DR-04 | Splits shall be performed **after** duplicate grouping and **before** any learned preprocessing | Enforced by the split script and asserted in CI | SO1, §9.3 |
| DR-05 | The external evaluation sets shall share no source with the training corpus | Uganda, RoCoLe, Saposoa, CoffeeLeaf-CO, Silva — all excluded from training in the headline model | SO3 |
| DR-06 | The corpus shall be accompanied by a datasheet recording provenance, collection method, licence, class distribution, known limitations and intended use | `data/datasheet.md` | SO1, §9.2, §9.6 |
| DR-07 | A model card shall describe the trained model: intended use, out-of-scope use, training data, metrics, per-class performance, calibration, known limitations | `data/model-card.md` | SO3, §9.6 |
| DR-08 | Labels for out-of-taxonomy conditions (red spider mite, weevil, *Mycena*) shall be preserved as a distinct `unsupported` label and shall never be mapped onto a disease class | Asserted in the data-preparation code | SO3, §2.4 |

---

## 5. Explicitly out of scope

Recorded here so that scope decisions are traceable (Guideline §4.6). Any change to this list is a
**major change** requiring a written request endorsed by the advisor and approved by the
Committee.

| Excluded | Reason |
|---|---|
| Detection and bounding-box localisation | Changes the model family and the evaluation protocol; a separate project |
| Disease severity quantification | BRACOL prior art reports 38.9 % accuracy for severity estimation [25]; not a credible target here |
| Nutrient-deficiency classification | Different task, different labels; a CoLeaf-DB-style dataset exists but is out of scope |
| Crops other than coffee | Title and problem statement are coffee-specific |
| Root, stem, berry and soil diagnosis | Explicitly excluded in the proposal §5.2 |
| Real-time video diagnosis | Adds latency and battery cost; a Should-level extension at most |
| User accounts, multi-tenant sync, cloud history | Deferred; v1 is local-only with optional export |
| Amharic-language user interface content | The **infrastructure** is required (NFR-15); the **translation content** is future work pending a qualified translator |
| DANN / adversarial domain adaptation | Evidence shows it can degrade accuracy to 0.252 [51]; excluded by design and documented as a deliberate omission |
| Test set reuse for model selection | §9.3 — the test set is touched once per configuration |

---

## 6. Traceability summary

Full matrix: `docs/requirements/traceability-matrix.md`.

| Objective | Functional requirements | Non-functional requirements | Data requirements |
|---|---|---|---|
| SO1 | — | NFR-09, NFR-27, NFR-28, NFR-32 | DR-01…DR-06, DR-08 |
| SO2 | FR-06, FR-07 | NFR-28, NFR-29, NFR-31 | DR-03, DR-04 |
| SO3 | FR-05, FR-07, FR-09, FR-10, FR-13 | NFR-11, NFR-28, NFR-29 | DR-05, DR-07, DR-08 |
| SO4 | FR-01…FR-04, FR-06…FR-12, FR-21, FR-31 | NFR-01…NFR-06, NFR-08, NFR-10, NFR-16, NFR-22, NFR-34 | — |
| SO5 | FR-11, FR-12, FR-13, FR-25, FR-32, FR-35…FR-37 | NFR-09, NFR-25 | DR-06, DR-07 |
| SO6 | FR-14…FR-20, FR-22…FR-24, FR-33 | NFR-07, NFR-23, NFR-24 | — |
| SO7 | FR-01…FR-37 (all) | NFR-11…NFR-13, NFR-17…NFR-21, NFR-26…NFR-31, NFR-35 | DR-07 |

---

## 7. Requirement change control

Guideline §7.3: *"Record each later change with its rationale and its effect on scope, schedule
and testing."*

| Change ID | Date | Requirement | Rationale | Effect on scope | Effect on schedule | Effect on testing | Approved by |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**Log every change in `docs/05-DECISION-LOG.md` as well.** An unrecorded requirement change is a
consistency violation under §7.5.
