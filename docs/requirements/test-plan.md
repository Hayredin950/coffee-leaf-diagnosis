# Test Plan

**Project:** Design and Development of a Coffee Leaf Disease Diagnosis System Using Deep Learning
**Version:** 1.0
**Owner:** Nahom Solomon · **Contributors:** Yohannes Berhanu (API/security), Bemnet Tesfaye (UI), Hayredin Mohammed (model/performance)
**Gate:** Prepared during design; executed in FYP II weeks 23–24 (Guideline Table 16.1, "Testing and evaluation").
**Template:** Appendix F — Test ID · Requirement · Precondition/input · Expected result · Actual result · Status · Evidence or defect ID · Severity if failed.

---

## 1. Purpose and scope

This plan defines what will be tested, at which level, with what method, and what evidence will
be retained. It is written during design (Guideline §10.2) so that testability is a design
constraint rather than an afterthought.

**In scope:** the mobile client, the API service, the web client, the on-device inference
pipeline, the knowledge base, the local history store, and the model artefact itself.

**Out of scope:** third-party services (Kaggle, Mendeley, Hugging Face, the container host);
the accuracy of the JMuBEN/BRACOL source labels; and the agronomic correctness of published
recommendations beyond the JARC review that is performed (E-13).

## 2. Test levels and justification (Guideline §10.1)

*"Not every project needs every level, but the test plan must justify each exclusion."*

| Level | Applied? | Justification |
|---|---|---|
| **Unit** | ✅ Yes | Core logic worth isolating: the confidence-vector normalisation, the abstention decision, the KB resolver, the history DAOs, the API validators. Automated, ≥80 % coverage on these modules (NFR-30) |
| **Integration** | ✅ Yes | The mobile client ↔ TFLite interpreter, the API ↔ database, the API ↔ model artefact, the KB asset ↔ the resolver |
| **System** | ✅ Yes | The end-to-end flow on a physical device: capture → inference → result → guidance → history |
| **Acceptance** | ✅ Yes | Each functional requirement demonstrated against its acceptance criterion in the specification |
| **Performance** | ✅ Yes | Latency, memory and model size are explicit objectives (SO4) with numeric targets (NFR-01…NFR-03) |
| **Usability** | ✅ Yes | The system has human users; SUS and task success are required by §10.4 and NFR-11/NFR-12 |
| **Security** | ✅ Yes (scoped) | The API handles uploads and stores records. Testing is confined to the group's own deployed instance, within the limits of §15.6 — no external systems, no offensive testing, no vulnerability scanning of third-party hosts |
| **Regression** | ✅ Yes (continuous) | CI runs the unit and integration suites on every pull request |
| **Soak / endurance** | ❌ No | The system has no long-running server component with accumulated state beyond the history table; a 24-hour soak would not exercise a distinct failure mode. The history table's growth is covered by the 10,000-record query benchmark (E-17) |
| **Formal verification / model checking** | ❌ No | Disproportionate to the risk and to the available time; the safety-critical property here (confident misdiagnosis) is addressed by the abstention mechanism, which is tested behaviourally |
| **Formal theorem proving** | ❌ No | Not applicable to a neural-network inference pipeline |
| **Hardware-in-the-loop** | ⚠️ Partially | On-device inference is tested on physical phones, but the full native-LiteRT delegate matrix (all CPU/ABI variants) is out of scope; the supported ABI set is documented instead |

## 3. Test environment

| Component | Specification |
|---|---|
| **Low-cost reference device** | Android 8.0+, ≤ 2 GB RAM, a 2018–2020 class SoC. This is the device the NFR-01 latency target is measured against |
| **Mid-range device** | Android 11+, 4–6 GB RAM |
| **High-end device** | Android 13+, ≥ 8 GB RAM |
| **Server** | The staging deployment; PostgreSQL managed instance |
| **Training environment** | Kaggle notebook, NVIDIA Tesla P100 16 GB — the environment recorded in `environment.yml` |
| **CI** | GitHub Actions, `ubuntu-latest`; unit + integration + lint + container build + KB audit |
| **Network condition for offline tests** | Android airplane mode, verified by packet capture during the test |

**Reference devices must be identified in the report by model, Android version, RAM and SoC** —
"a mid-range phone" is not a reproducible test environment.

## 4. Test data

| Set | Size | Purpose | Source |
|---|---|---|---|
| Smoke set | 10 images (2 per class) | Fast CI sanity check | Held-out internal test split |
| Functional set | 50 images | Feature-level testing | Held-out internal test split |
| Edge-case set | ~25 images | Invalid input, wrong aspect ratio, very dark, very bright, blurred, non-leaf, multi-leaf, tiny crop, greyscale, PNG with alpha | Purpose-built + external sets |
| External set | Uganda + RoCoLE + Saposoa + CoffeeLeaf-CO + Silva | Model evaluation | Public datasets (never trained on) |
| Performance set | 100 images | Latency measurement | Internal test split |
| Usability set | 25 images | Task-based usability sessions | Internal test split + 5 field photos |

**Rule:** no image used for testing may be used for training, and no image used to tune a
hyperparameter may appear in the test partition.

## 5. Test techniques

| Technique | Where |
|---|---|
| Assertion-based unit tests (pytest, Dart `test`) | All pure logic |
| Golden-image regression tests | Preprocessing pipeline — a fixed input must produce a fixed tensor |
| Property-based tests (Hypothesis) | Image validation, confidence normalisation |
| Integration tests against a test database (SQLAlchemy testcontainers or SQLite in-memory) | API + persistence |
| Manual scripted walkthrough with a screen recording | UI flows, offline mode |
| `adb shell` scripted measurements | Latency, memory |
| Packet capture (Wireshark / mitmproxy) | Offline-mode verification (no outbound requests) |
| `pytest-benchmark` / `locust` | API performance |
| OWASP ZAP baseline scan against the group's own staging deployment only | API security |
| `gitleaks` / `trufflehog` | Secret leakage in the repository |
| `pip-audit`, `npm audit`, `flutter pub outdated` | Dependency vulnerabilities |
| SUS questionnaire + task success observation | Usability |

## 6. Entry and exit criteria

**Entry criteria for the testing phase (FYP II week 23):**
- All FYP II implementation work merged to `main` and tagged.
- The model artefact, the KB asset and the schema migrations are frozen.
- The environment file reproduces the deployment.
- The test suites (unit, integration) pass in CI.

**Exit criteria for the testing phase (end of week 24):**
- ≥ 95 % of planned test cases executed.
- 100 % of *Must*-priority functional requirements covered by at least one **passed** test.
- 0 open Critical or High severity defects.
- All Medium defects either fixed or documented with an impact statement in Chapter 6.
- The traceability matrix contains no `[PENDING]` values.
- The evaluation review (Gate 7) is passed by the advisor.

## 7. Test cases by area

The full executable list, with actual results, lives in
`docs/appendices/Appendix-F-Test-Cases.md`. This section defines the areas and the minimum
coverage per area.

### 7.1 Data pipeline (Hayredin) — T-01…T-06

| Test ID | Area | Check |
|---|---|---|
| T-01 | Corpus | Every downloaded image is readable and assigned to exactly one class folder |
| T-02 | Corpus | The observed per-class counts match the datasheet within the documented tolerance, and the discrepancy against the published counts is recorded |
| T-03 | Leakage | No image hash appears in more than one split |
| T-04 | Leakage | No perceptual-hash duplicate cluster spans two splits |
| T-05 | Leakage | No source-image group (BRACOL leaf ↔ its crops; RoCoLe plant ID) spans two splits |
| T-06 | Splits | train + validation + test equals the total corpus size; for each class, the number of groups in each partition is within one group of the target ratio |

### 7.2 Model (Hayredin) — T-07…T-16

| Test ID | Area | Check |
|---|---|---|
| T-07 | Baseline | The majority-class baseline script runs and produces the expected accuracy and confusion matrix |
| T-08 | Training | A training run reproduces the logged metrics when re-run with the recorded seed |
| T-09 | Inference | The evaluation script produces per-class precision, recall, F1 and a confusion matrix for every model |
| T-10 | Determinism | Two runs with the same seed produce identical predictions |
| T-11 | Export | The TFLite conversion succeeds for float32, float16 and int8 without an accuracy-affecting warning |
| T-12 | Export | The exported model's predictions match the Keras model's predictions on 1,000 held-out images to within 0.5 % accuracy difference |
| T-13 | Labels | `labels.txt` contains exactly five entries, in the same order as the training `class_index`, and matches the KB and the API schema |
| T-14 | Calibration | The temperature-scaling script reports ECE and NLL before and after scaling on the validation set |
| T-15 | Abstention | At the configured threshold, the abstention rate and accepted accuracy are computed correctly on the external sets |
| T-16 | Unsupported class | Red spider mite, weevil and *Mycena* images are routed to `unsupported` and never to a disease class |

### 7.3 Mobile client (Bemnet) — T-17…T-40

| Test ID | Area | Check |
|---|---|---|
| T-17 | Capture | The camera opens and returns a frame (device emulator + 1 physical device) |
| T-18 | Gallery | A gallery image is loaded and displayed |
| T-19 | Validation | A file that is not a decodable image is rejected with the specified message |
| T-20 | Validation | An image smaller than 64×64 is rejected with the specified message |
| T-21 | Validation | An image larger than 20 MB is rejected without an out-of-memory crash |
| T-22 | Inference | A valid image produces a prediction whose label is one of the five classes |
| T-23 | Inference | The five confidences sum to 1.0 ± 1e-5 over 1,000 inputs |
| T-24 | Offline | With airplane mode on, the full capture→result flow completes |
| T-25 | Offline | A packet capture during the core flow shows zero outbound requests |
| T-26 | Performance | Median latency ≤ 500 ms and p95 ≤ 1,000 ms on the low-cost reference device |
| T-27 | Guidance | Each of the five classes renders its KB entry with all ten fields populated |
| T-28 | Guidance | The advisory notice is visible on the result screen without scrolling |
| T-29 | Guidance | The KB is available with no network and after an app restart |
| T-30 | Guidance | No uncited practice appears in the KB (automated audit in CI) |
| T-31 | Guidance | The user can open the KB for any class, not only the predicted one |
| T-32 | Guidance | The KB version displayed matches the version in the build manifest |
| T-33 | History | A completed diagnosis appears in the history with all seven fields |
| T-34 | History | The history is ordered newest-first |
| T-35 | History | Filtering by class returns only that class |
| T-36 | History | Filtering by date range returns only records in that range |
| T-37 | History | An empty filter result shows an explicit empty state, not a blank list |
| T-38 | History | A deleted record is still absent after an app restart |
| T-39 | History | The CSV export opens in a spreadsheet with one row per record and a header |
| T-40 | History | A record written at schema v1 is readable after migration to v2 |

### 7.4 API (Yohannes) — T-51…T-60

| Test ID | Area | Check |
|---|---|---|
| T-51 | Contract | The OpenAPI schema validates every request and response in CI |
| T-52 | Validation | A non-image upload returns 422, not 500 |
| T-53 | Validation | An upload exceeding the size limit returns 413 |
| T-54 | Security | A renamed non-image is rejected by the magic-byte check |
| T-55 | Security | An unauthenticated mutating request returns 401 |
| T-56 | Security | A request beyond the rate limit returns 429 |
| T-57 | Secrets | `gitleaks` reports no findings in the repository history |
| T-58 | Dependencies | `pip-audit` reports no unmitigated high or critical finding |
| T-59 | Performance | p95 API latency ≤ 2,000 ms for a 224×224 upload at the target concurrency |
| T-60 | Availability | The health endpoint returns 200 throughout the evaluation window; uptime ≥ 99 % |

### 7.5 Web client (Bemnet + Yohannes) — T-61…T-64

| Test ID | Area | Check |
|---|---|---|
| T-61 | Upload | Uploading an image returns a diagnosis within 5 s |
| T-62 | Guidance | The guidance rendered matches the mobile client's rendering for the same class |
| T-63 | History | The history filters and the CSV export behave identically to the mobile client |
| T-64 | Resilience | With the API stopped, the client shows an explicit error rather than a blank screen |

### 7.6 Usability and ethics (Nahom) — T-65, E-18

| Test ID | Area | Check |
|---|---|---|
| T-65 | Accessibility | Every interactive element has a touch target ≥ 48×48 dp; `flutter analyze` reports no accessibility lint errors |
| E-18 | Usability | SUS questionnaire and task success with ≥10 participants; consent obtained; no personal data recorded |

## 8. Usability study protocol (Guideline §10.4, §15.4)

**Participants.** 12 participants (target minimum 10), recruited among university students,
agriculture students and members of local coffee-farming families. **Rationale for the number:**
12 exceeds the 5-participant threshold that the System Usability Scale literature associates
with a stable mean score, and it matches the sample sizes reported for comparable
small-scale mobile applications in the plant-disease literature [30]. The number is stated and
justified in the report, as §10.4 requires.

**Tasks.** Each participant completes, in order:
1. Open the app and take a photograph of a provided leaf sample.
2. Read the diagnosis and state which disease it is.
3. Open the guidance and state the **first action** you would take.
4. Find a previous diagnosis from a specific date.
5. Export the history to a file.

**Measures.** SUS (10 items, 0–100 scale), task success (binary), time on task, and the
comprehension check in task 3 (E-14).

**Ethics.** Informed consent with a plain-language form explaining the purpose, that no personal
data is collected, that participation is voluntary and may be stopped at any time, and that
results appear only in aggregate. Participants are assigned a pseudonymous code (P01…P12).
No names, photographs of faces, or contact details are recorded. Sessions are conducted with
consent for note-taking; no audio or video is recorded without separate explicit permission.
Completed consent forms are retained; the data itself is stored on an encrypted device held by
Nahom Solomon and destroyed after the defence unless the participant consents to retention.

**Analysis.** SUS scored with the standard published formula. Task success reported as a
proportion with the count. Time on task reported as median and range. The comprehension check
reported as a proportion. No inferential statistics on n = 12 — the sample is too small and the
report will say so.

## 9. Defect management (Guideline §10.3)

| Severity | Definition | Response |
|---|---|---|
| **Critical** | The core flow fails, data is lost or corrupted, a security hole allows unauthorised access | Fix immediately; block the release; re-test the full affected area |
| **High** | A Must requirement fails; the offline flow is broken; a wrong diagnosis is displayed without the abstention guard | Fix before the evaluation review; re-test |
| **Medium** | A Should requirement fails; a non-core edge case is mishandled | Fix if time allows; otherwise document with an impact statement in Chapter 6 |
| **Low** | Cosmetic; a wording or layout issue | Fix opportunistically; otherwise document |

Every defect record contains: ID, description, severity, the requirement or test case it
breaches, the environment, a reproduction procedure, a screenshot or log, the root-cause
analysis, the fix, and the re-test result. Known unresolved defects are discussed in Chapter 6
with their impact, as §10.3 requires.

## 10. Evidence to be retained

For each executed test case: the actual result, the status, and evidence (screenshot, log
excerpt, or video timestamp). Evidence is stored in `evidence/` in the repository, named
`T-<id>-<short-description>.<ext>`, and referenced from Appendix F.

## 11. Test schedule

| FYP II week | Testing activity |
|---|---|
| 15 | Unit tests for the inference wrapper; the API test harness |
| 16 | Integration tests for the API and the database; KB schema test |
| 17 | UI test cases drafted; security checklist prepared |
| 18 | Core prototype tested manually; defects logged |
| 19–22 | Regression runs after each integration; offline verification; performance baseline |
| 23 | Full formal execution: T-01…T-66; evidence captured |
| 24 | Defect fixes and re-tests; usability study; evaluation written up; traceability completed |
