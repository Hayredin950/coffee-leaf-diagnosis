# Appendix F — Test Case Register

> **Guideline §10.2:** *"Prepare a test plan during design. Each test case must contain an ID,
> the requirement it covers, the input or precondition, the expected result, the actual result,
> the status, and where useful, evidence such as screenshots or logs. Appendix F gives the
> template. 'The system was tested and works' is not sufficient evidence."*
>
> **Template (Appendix F):** Test ID · Requirement · Precondition or input · Expected result ·
> **Actual result** · **Status** · Evidence or defect ID · Severity if failed.
>
> **Status values:** Pass · Fail · Blocked · Not run
>
> **Owner:** Nahom Solomon (register) · the member who owns the area executes its cases.
> **Execution window:** FYP II weeks 23–24 (22 March – 4 April 2027).
>
> **Rules.**
> 1. A test case with no actual result is **not run**. Do not submit this file with empty
>    "actual result" cells — write "Not run" instead, and explain why in Chapter 6.
> 2. Every Fail must have a defect ID and a severity.
> 3. Every Pass must have evidence where evidence is possible (a screenshot file named
>    `T-<id>-<slug>.png` in `evidence/`, a log excerpt, or a CI run URL).
> 4. A test that passes only because the tester did not try hard enough is not a test. The
>    "precondition or input" column must state the *worst* case that was tried.

---

## F.1 Summary (to be completed after execution)

| Area | Cases | Pass | Fail | Blocked | Not run |
|---|---|---|---|---|---|
| Data pipeline (T-01…T-06) | 6 | | | | |
| Model (T-07…T-16) | 10 | | | | |
| Mobile client (T-17…T-40) | 24 | | | | |
| API (T-51…T-60) | 10 | | | | |
| Web client (T-61…T-64) | 4 | | | | |
| Accessibility (T-65) | 1 | | | | |
| **Total** | **55** | | | | |

**Coverage against the specification:** every Must-priority requirement has at least one
executed, passing case. Every Should-priority requirement has at least one executed case.

---

## F.2 Data pipeline — Hayredin Mohammed

| Test ID | Requirement | Precondition or input | Expected result | Actual result | Status | Evidence / defect | Severity if failed |
|---|---|---|---|---|---|---|---|
| T-01 | DR-01, DR-02 | All nine source archives downloaded and extracted; every image file opened with Pillow | Every file opens; every file's parent folder maps to exactly one of the five classes or to an explicit `unsupported` class | | | | High |
| T-02 | DR-01, DR-06 | The extracted tree is counted per class and compared with the published counts | The observed counts are recorded in the datasheet, and every discrepancy against the published figure is written down with an explanation | | | | Medium |
| T-03 | SO1, NFR-27 | The split manifest is scanned for exact SHA-256 duplicates across partitions | No hash appears in more than one partition | | | | Critical |
| T-04 | SO1, NFR-27 | The split manifest is clustered by perceptual hash (pHash, Hamming distance ≤ 6) and the clusters are checked against the partitions | No duplicate cluster spans two partitions | | | | Critical |
| T-05 | SO1 | The source-group identifiers are checked: the BRACOL leaf ↔ its symptom crops, the RoCoLe plant ID (`C##P##`), and the CoffeeLeaf-CO source attribution | No group spans two partitions | | | | Critical |
| T-06 | DR-03 | The partition sizes are compared with the corpus size, and for each class the number of groups in each partition is compared with the target ratio | train + validation + test equals the corpus size exactly; for each class, the number of groups in each partition is within one group of the target ratio | | | | High |

---

## F.3 Model — Hayredin Mohammed

| Test ID | Requirement | Precondition or input | Expected result | Actual result | Status | Evidence / defect | Severity if failed |
|---|---|---|---|---|---|---|---|
| T-07 | SO2, FR-06 | The majority-class baseline is run on the training split and evaluated on the test split | The script reports the majority class's accuracy and a confusion matrix consistent with the class distribution | | | | Medium |
| T-08 | SO2, NFR-28 | A logged training configuration is re-run with the recorded seed and the same environment file | The metrics match the logged values within floating-point tolerance | | | | High |
| T-09 | SO2, FR-07 | Every trained model is evaluated on the internal test split | Per-class precision, recall and F1 plus the confusion matrix are produced for every model and every class | | | | High |
| T-10 | NFR-28 | The same trained model is run twice on the same inputs | The predictions are identical | | | | Medium |
| T-11 | SO4, NFR-02 | `model/export_tflite.py` is run for float32, float16 and int8 | All three conversions succeed; the tool emits no accuracy-affecting warning | | | | High |
| T-12 | SO4 | The TFLite model and the Keras model are both run on 1,000 held-out images | The accuracy difference is within 0.5 percentage points | | | | High |
| T-13 | FR-06, SO5 | `labels.txt` is compared against the training `class_index`, the KB key order and the API enum | All four orders are identical, with exactly five entries | | | | High |
| T-14 | SO3, NFR-29 | `training/calibrate.py` runs on the validation split | ECE and NLL are reported before and after temperature scaling, and the fitted temperature is written to `model-card.md` | | | | Medium |
| T-15 | SO3, FR-09 | The abstention policy is applied to the external predictions at the configured threshold | The abstention rate and the accepted accuracy are computed correctly on every external dataset | | | | High |
| T-16 | DR-08 | Images of red spider mite, coffee weevil and *Mycena citricolor* are passed through the pipeline | They are routed to the `unsupported` label and never to a disease class | | | | Critical |

---

## F.4 Mobile client — Bemnet Tesfaye

| Test ID | Requirement | Precondition or input | Expected result | Actual result | Status | Evidence / defect | Severity if failed |
|---|---|---|---|---|---|---|---|
| T-17 | FR-01 | The app is installed on a physical device; the camera permission is granted | The camera opens, a preview is shown and a captured frame reaches the inference pipeline within 1 s | | | | High |
| T-18 | FR-02 | A JPEG is present in the gallery | The image is loaded, displayed and reaches the pipeline; the original file is unmodified (checksum compared before and after) | | | | High |
| T-19 | FR-04 | A text file is renamed to `image.jpg` and selected from the gallery | The file is rejected with the "not an image" message; no crash; no network request | | | | High |
| T-20 | FR-04 | A 32×32 PNG is selected | Rejected with the "too small" message | | | | Medium |
| T-21 | FR-04 | A 25 MB JPEG is selected | Rejected with the "too large" message; no out-of-memory crash; the app remains responsive | | | | High |
| T-22 | FR-06 | A valid leaf image is submitted | The returned label is one of the five classes | | | | Critical |
| T-23 | FR-07 | 1,000 randomised inputs are pushed through the inference wrapper | The five confidences sum to 1.0 ± 1e-5 in every case | | | | High |
| T-24 | FR-08, NFR-08 | Airplane mode is enabled; the full capture→result flow is performed | The flow completes and a result is displayed | | | | Critical |
| T-25 | FR-08, NFR-24 | A packet capture runs across the whole core flow in airplane mode | Zero outbound requests are observed | | | | Critical |
| T-26 | SO4, NFR-01 | 50 inference runs on the low-cost reference device with a warm cache | Median ≤ 500 ms and p95 ≤ 1,000 ms | | | | High |
| T-27 | FR-11, FR-35 | Each of the five classes is forced as the prediction | Each renders a guidance entry with all ten fields populated | | | | High |
| T-28 | FR-12 | The result screen is viewed on the smallest supported device | The advisory notice is fully visible without scrolling | | | | Medium |
| T-29 | FR-11, NFR-09 | The app is run with no network and then restarted | The KB is still available after the restart | | | | Critical |
| T-30 | FR-36 | The CI check `scripts/audit_kb.py` runs against the KB | Every practice field has at least one citation; the check fails on any uncited practice | | | | High |
| T-31 | FR-13 | The All Diseases screen is opened and each class is tapped | Every class's guidance opens | | | | Low |
| T-32 | FR-37 | The KB version shown in the app is compared with the version in the build manifest | They are identical | | | | Low |
| T-33 | FR-14 | A diagnosis is completed | A history record exists with all seven fields populated | | | | Critical |
| T-34 | FR-15 | Five diagnoses are created in a known order | The history lists them newest-first | | | | Medium |
| T-35 | FR-16 | The history is filtered by each class in turn | Only the records of that class are returned | | | | Medium |
| T-36 | FR-16 | The history is filtered by a date range that excludes some records | Only the records within the range are returned | | | | Medium |
| T-37 | FR-16 | A filter is applied that matches no records | An explicit empty state is shown, not a blank list | | | | Low |
| T-38 | FR-18 | A record is deleted and the app is force-stopped and restarted | The record is still absent | | | | Medium |
| T-39 | FR-19 | The history is exported to CSV | The file opens in a spreadsheet with a header and one row per record, and the row count matches | | | | High |
| T-40 | FR-20 | A database created at schema v1 is opened by the v2 build | The v1 records are readable and intact after the migration | | | | High |

---

## F.5 API — Yohannes Berhanu

| Test ID | Requirement | Precondition or input | Expected result | Actual result | Status | Evidence / defect | Severity if failed |
|---|---|---|---|---|---|---|---|
| T-51 | FR-28 | The committed `api/openapi.json` is compared with the running app's generated schema | The schemas are identical; a difference fails the CI build | | | | High |
| T-52 | FR-30, NFR-18 | A text file is posted to `/v1/predict` | HTTP 422 with `UNSUPPORTED_MEDIA_TYPE`; never 500 | | | | High |
| T-53 | FR-30 | A 25 MB image is posted | HTTP 413 `PAYLOAD_TOO_LARGE` | | | | Medium |
| T-54 | NFR-19 | A `.txt` file with a JPEG magic-byte header forged | The magic-byte check accepts it only if the content really decodes; otherwise it is rejected | | | | Critical |
| T-55 | FR-29, NFR-20 | A mutating request is sent with no token, then with a malformed token | HTTP 401 in both cases | | | | Critical |
| T-56 | NFR-21 | 100 requests are sent in one minute | Requests beyond 60/minute return HTTP 429 with `Retry-After` | | | | Medium |
| T-57 | NFR-17 | `gitleaks detect` runs over the whole repository history | No findings | | | | Critical |
| T-58 | NFR-22 | `pip-audit` and `npm audit` run | No unmitigated high or critical advisory | | | | High |
| T-59 | NFR-05 | A load test at the target concurrency is run against staging | p95 latency ≤ 2,000 ms | | | | Medium |
| T-60 | NFR-06 | The health endpoint is polled every 5 minutes across the evaluation window | It returns 200 throughout; the uptime is ≥ 99 % | | | | Medium |

---

## F.6 Web client — Bemnet Tesfaye and Yohannes Berhanu

| Test ID | Requirement | Precondition or input | Expected result | Actual result | Status | Evidence / defect | Severity if failed |
|---|---|---|---|---|---|---|---|
| T-61 | FR-31 | A sample image is uploaded | A diagnosis is returned within 5 s | | | | High |
| T-62 | FR-32 | The same class is forced on the web client and on the mobile client | The rendered guidance is identical | | | | Medium |
| T-63 | FR-33 | The history is filtered and exported on the web client | The filter semantics and the CSV contents match the mobile client | | | | Medium |
| T-64 | FR-34 | The API container is stopped while the web client is open | An explicit error is displayed within 5 s; the page does not go blank | | | | Medium |

---

## F.7 Accessibility — Bemnet Tesfaye

| Test ID | Requirement | Precondition or input | Expected result | Actual result | Status | Evidence / defect | Severity if failed |
|---|---|---|---|---|---|---|---|
| T-65 | NFR-14 | `flutter analyze` plus a manual pass over every screen | No accessibility lint errors; every interactive element is ≥ 48×48 dp; the layout survives a font scale of 2.0 without clipping; no information is conveyed by colour alone | | | | Medium |

---

## F.8 Defect register (Guideline §10.3)

| Defect ID | Test ID | Severity | Description | Root cause | Fix | Re-test result | Status | Impact if unresolved |
|---|---|---|---|---|---|---|---|---|
| D-001 | | | | | | | | |

**Rules.** Every Important failure is recorded, analysed and re-tested. Known unresolved
defects are discussed in Chapter 6 with their impact, as §10.3 requires.

---

## F.9 Usability study results (Guideline §10.4)

**Participants:** ___ (target ≥ 10) · **Sessions:** ___ · **Date:** ___

| Participant | T1 capture | T2 read the diagnosis | T3 state the first action | T4 find a dated record | T5 export | Time on task (s) | SUS score |
|---|---|---|---|---|---|---|---|
| P01 | | | | | | | |
| P02 | | | | | | | |
| P03 | | | | | | | |
| P04 | | | | | | | |
| P05 | | | | | | | |
| P06 | | | | | | | |
| P07 | | | | | | | |
| P08 | | | | | | | |
| P09 | | | | | | | |
| P10 | | | | | | | |
| P11 | | | | | | | |
| P12 | | | | | | | |

| Measure | Value |
|---|---|
| Task success rate, "capture → diagnosis → guidance" | |
| Task success rate, "find a dated record" | |
| Task success rate, "export the history" | |
| Median time on the core flow | |
| **SUS score (mean)** | |
| SUS score (range) | |
| Number of participants who would recommend the app | |
| Comprehension check, T3 (participants correctly stating the recommended first action) | |

**Justification of the sample size (required by §10.4):** ___

---

## F.10 Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Test coordinator | Nahom Solomon | | |
| Mobile client | Bemnet Tesfaye | | |
| Model and data | Hayredin Mohammed | | |
| API and deployment | Yohannes Berhanu | | |
| Advisor | Surafiel Habib Asefa | | |
