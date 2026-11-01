# Chapter 5 — Implementation

> **Owner:** the four members jointly; the lead for each subsection is named. This chapter is
> **written during FYP II** (weeks 15–29), because Guideline §11.8 requires the report to
> describe the implementation as it actually is. Sections are drafted as each component is
> completed, not afterwards.
>
> **Guideline §11.8:** *"Show only essential code excerpts in the report body. Full code
> belongs in the repository and, where needed, in an appendix."*

---

## 5.1 Implementation environment and structure

**Table 5.1** — The repository layout.

| Path | Contents | Owner |
|---|---|---|
| `scripts/` | `prepare_data.py` — the inventory, grouping, clustering, split and audit pipeline | Hayredin |
| `training/` | `train.py`, `evaluate_internal.py`, `evaluate_external.py`, `calibrate.py`, `ablate.py`, `significance.py`, `selective_risk.py` | Hayredin |
| `model/` | `export_tflite.py`, `model.tflite`, `labels.txt`, `metadata.json`, `model-card.md` | Hayredin |
| `mobile/` | The Flutter client — `lib/` (UI, acquisition, validation, quality, inference, calibration, abstention, KB resolver, repository), `test/`, `android/` | Yohannes |
| `api/` | The FastAPI service — `app/` (routers, services, models), `migrations/`, `openapi.json` | Bemnet |
| `web/` | The static web client | Bemnet + Yohannes |
| `data/` | `datasheet.md`, `dataset-sources.md`, `knowledge_base.json`, `knowledge-base.md`, `split_manifest.csv` | Hayredin + Nahom |
| `docs/` | All design, requirements, literature and report documents | All |
| `evidence/` | The test evidence — screenshots, logs and captures referenced from Appendix F | All |
| `results/` | One file per evaluation experiment, referenced from `results.md` | Hayredin |
| `.github/workflows/` | CI — lint, unit tests, the container build, the artefact check, the KB audit, the secret scan | Bemnet |

**Table 5.2** — The implementation languages and frameworks, with their versions.

| Component | Language | Framework / libraries | Version |
|---|---|---|---|
| Data and model pipeline | Python 3.11 | TensorFlow, Keras, Pillow, ImageHash, scikit-learn, SciPy, pandas | pinned in `requirements.lock` |
| Mobile client | Dart | Flutter, `tflite_flutter`, `image_picker`, `camera`, `sqflite`, `drift`, `path_provider`, `share_plus` | 3.x, pinned in `pubspec.yaml` |
| API service | Python 3.11 | FastAPI, Pydantic v2, SQLAlchemy 2, Alembic, `python-jose`, `slowapi`, PostgreSQL | pinned |
| Web client | HTML / CSS / JavaScript | No framework | — |

---

## 5.2 The data preparation pipeline

**Lead: Hayredin Mohammed**

The pipeline is implemented in `scripts/prepare_data.py` and executes five steps in a fixed
order, described in full in §4.1 of the datasheet.

```python
# scripts/prepare_data.py — the essential excerpt (full code in the repository)

def stratified_grouped_split(records, seed=42, ratios=SPLIT_RATIOS):
    """Assign every record a split, keeping every group inside a single split."""
    groups = defaultdict(list)
    for record in records:
        groups[record.group_id].append(record)

    group_class = {}
    for group_id, items in groups.items():
        labels = {item.class_key for item in items}
        if len(labels) > 1:                      # a group spanning classes is a data
            group_class[group_id] = sorted(labels)[0]   # problem: keep it whole, report it
        else:
            group_class[group_id] = next(iter(labels))

    rng = random.Random(seed)
    by_class = defaultdict(list)
    for group_id, label in group_class.items():
        by_class[label].append(group_id)

    assignment = {}
    for label, group_ids in sorted(by_class.items()):
        group_ids = sorted(group_ids)
        rng.shuffle(group_ids)
        total = len(group_ids)
        train_cut = int(round(total * ratios["train"]))
        val_cut = train_cut + int(round(total * ratios["validation"]))
        for index, group_id in enumerate(group_ids):
            assignment[group_id] = (
                "train" if index < train_cut
                else "validation" if index < val_cut
                else "test"
            )

    for record in records:
        record.split = assignment[record.group_id]
```

**The audit.** After the split, four invariants are asserted. The audit is a hard gate: the
script exits non-zero and no manifest is written if any invariant fails.

```python
def audit(records):
    failures = []

    # T-03: an exact duplicate must not span partitions
    by_hash = defaultdict(set)
    for r in records:
        by_hash[r.sha256].add(r.split)
    failures += [f"T-03: sha256 {h[:12]} appears in {sorted(s)}"
                 for h, s in by_hash.items() if len(s) > 1]

    # T-04: a near-duplicate cluster must not span partitions
    by_cluster = defaultdict(set)
    for r in records:
        if r.group_id.startswith("phash:"):
            by_cluster[r.group_id].add(r.split)
    failures += [f"T-04: phash cluster {c} appears in {sorted(s)}"
                 for c, s in by_cluster.items() if len(s) > 1]

    # T-05: a group must not span partitions; no external source may be in train
    by_group = defaultdict(set)
    for r in records:
        by_group[r.group_id].add(r.split)
    failures += [f"T-05: group {g} appears in {sorted(s)}"
                 for g, s in by_group.items() if len(s) > 1]
    external_in_train = {r.source for r in records
                         if r.split == "train" and r.source in EXTERNAL_ONLY}
    if external_in_train:
        failures.append(f"T-05: external sources in train: {sorted(external_in_train)}")

    # T-06: the partitions sum to the corpus; the class proportions are preserved
    ...
    return failures
```

**Table 5.3** — The audit results. *Completed after the first run; the numbers are reported in
Chapter 6.*

| Invariant | Test ID | Groups checked | Violations found |
|---|---|---|---|
| No SHA-256 hash spans a partition | T-03 | | |
| No pHash cluster spans a partition | T-04 | | |
| No group identifier spans a partition | T-05 | | |
| No external-only source appears in train | T-05 | | |
| The partitions sum to the corpus size | T-06 | | |
| The split is stratified by class at the group level | T-06 | | |

**What the audit found.** *To be completed.* The group expects a substantial number of
near-duplicate clusters in JMuBEN and JMuBEN2, given the documented rotation and flip
augmentation; the count and the effect on the resulting split sizes are reported in Chapter 6
as evidence for the leakage argument.

---

## 5.3 Model training, quantisation and export

**Lead: Hayredin Mohammed**

### 5.3.1 Training

Transfer learning is used throughout: the ImageNet-pretrained backbone is frozen for the first
few epochs and then fine-tuned at a reduced learning rate, following the recipe standard in
the coffee leaf disease literature [7]–[10] but with the group's own leakage-safe split.

**Table 5.4** — The training configuration.

| Parameter | Value |
|---|---|
| Input resolution | 224 × 224 × 3 |
| Optimiser | AdamW, cosine decay with a warm-up of 2 epochs |
| Learning rate | 1e-3 for the head, 1e-4 for the backbone, 10 epochs of head-only training before fine-tuning |
| Batch size | 32 (16 if the notebook's GPU memory requires it) |
| Epochs | 30, with early stopping on the validation macro-F1 with a patience of 5 |
| Loss | Sparse categorical cross-entropy with label smoothing of 0.05 |
| Seeds | 42, 43, 44 — every configuration is run three times |
| Checkpoint selection | The best validation macro-F1, never the best training loss |

### 5.3.2 Quantisation and export

The trained float32 model is converted to TensorFlow Lite with metadata and then quantised.

**Table 5.5** — The exported artefacts. *Measured values are reported in Chapter 6.*

| Artefact | Quantisation | Size (MB) | Notes |
|---|---|---|---|
| `model_fp32.tflite` | float32 | | The reference artefact |
| `model_fp16.tflite` | float16 | | The comparison point |
| `model_int8.tflite` | int8, post-training | | **The shipped artefact** |
| `labels.txt` | — | | The five labels, in the training order |
| `metadata.json` | — | | The model version, the KB version, the temperature `T`, the acceptance threshold, the input size, the quantisation and the label array |
| `model-card.md` | — | | The intended use, the out-of-scope use, the data, the metrics, the calibration and the known limitations |

The **acceptance threshold and the calibration temperature are stored in `metadata.json`
rather than compiled into the application code**, so that changing the deployed model cannot
leave the application threshold silently stale. Test T-13 asserts that the label order is
identical across `labels.txt`, the knowledge base, the API enum and the interface.

### 5.3.3 The preprocessing parity test

Because the application implements the preprocessing in Dart while the training pipeline
implements it in Python, a **golden-image test** compares the two element by element over a
fixed set of twenty images. A mismatch fails CI. This is the mechanism that prevents the
classic silent failure in which a deployed model performs worse than its reported accuracy
because of a normalisation mismatch.

---

## 5.4 The mobile client

**Lead: Bemnet Tesfaye**

### 5.4.1 The inference pipeline

The essential excerpt of the on-device inference and abstention logic:

```dart
// mobile/lib/inference/diagnoser.dart

Future<DiagnosisOutcome> diagnose(Uint8List bytes) async {
  final validated = await _validator.validate(bytes);
  if (!validated.isValid) {
    return DiagnosisOutcome.failure(validated.errorCode!);
  }

  final quality = _qualityGate.assess(validated.image);
  if (!quality.isAcceptable) {
    return DiagnosisOutcome.retake(quality.reason, quality.suggestions);
  }

  final input = _preprocessor.toInputTensor(validated.image);   // 1x224x224x3 int8
  final logits = _interpreter.invoke(input);                    // 5 raw logits
  final probabilities = _calibrator.apply(logits);               // softmax(logits / T)

  final ranked = _calibrator.rank(probabilities);
  final top1 = ranked.first;

  // The threshold comes from the model's metadata, not from a constant in the code.
  if (top1.probability < _metadata.acceptThreshold) {
    return DiagnosisOutcome.lowConfidence(ranked,
        _metadata.abstainReason);
  }

  final guidance = _kbResolver.resolve(top1.label);
  await _repository.save(DiagnosisRecord(
    id: const Uuid().v4(),
    timestampUtc: DateTime.now().toUtc(),
    imagePath: validated.storedPath,
    label: top1.label,
    top1Confidence: top1.probability,
    confidenceVector: probabilities,
    modelVersion: _metadata.modelVersion,
    kbVersion: _metadata.kbVersion,
  ));

  return DiagnosisOutcome.accepted(top1, ranked, guidance);
}
```

### 5.4.2 The user interface

Five screens were implemented: capture, result, guidance, history and the knowledge-base
browser. Two are worth describing in the report because they embody the design decisions of
Chapter 4:

- **The low-confidence screen.** When the abstention policy fires, the result screen does not
  display a class name at all. It states that the leaf could not be identified with enough
  certainty, lists the ranked candidates with their confidences *without* labelling any of
  them as a diagnosis, and offers concrete suggestions for a better photograph — brighter
  light, fill the frame, avoid blur — followed by a retake button.
- **The result screen's advisory notice.** A permanent notice states that the output is
  decision support and does not replace an extension officer, together with the knowledge
  base's source attribution.

### 5.4.3 The local repository and the history

The on-device store uses SQLite through Drift, with typed data objects and a forward-only
migration strategy. The history screen lists the records newest-first with the thumbnail, the
class, the confidence and the timestamp; it offers filter chips for the class, a date-range
picker, a free-text search, a delete action with a confirmation, and a CSV export to the
shared folder. The CSV export writes one row per record with a header row.

### 5.4.4 Offline operation

The application makes **no** network request during the core flow. This is verified by test
T-25, which captures the network traffic during a full capture-to-result cycle with the
device in airplane mode and asserts that zero outbound requests occur.

---

## 5.5 The knowledge base

**Lead: Nahom Solomon**

The knowledge base is a single JSON asset, versioned, with a checksum recorded in
`kb_version`. Each of the five classes has an entry with the ten fields described in
Chapter 4.

**Table 5.6** — The knowledge-base entries and their sources. *To be completed.*

| Class | Scientific name | Local names | Symptoms | Severity cues | Organic control | Chemical control | Prevention | Sources | Reviewed by |
|---|---|---|---|---|---|---|---|---|---|
| Coffee Leaf Rust | *Hemileia vastatrix* | | | | | | | [56], [57], [61] | |
| Cercospora Leaf Spot | *Cercospora coffeicola* | | | | | | [61], [62] | |
| Leaf Miner | *Leucoptera coffeella* | | | | | | [11], [61] | |
| Phoma Leaf Spot | *Phoma costarricensis* | | | | | | [61], [62] | |
| Healthy | — | | | | | | — | |

**The citation audit.** A CI job, `scripts/audit_kb.py`, verifies that every class has all ten
fields populated and that every field stating a practice carries at least one source. A
failure breaks the build.

**The expert review.** The draft knowledge base was submitted to a plant pathologist at the
Jimma Agricultural Research Center for review, and the review record is retained as evidence.
*Reviewer name, date and outcome: to be completed.*

**Two content constraints.** First, the chemical-control sections name active-ingredient
classes and direct the user to a locally registered product and to its label — never a
product name or a dosage. Second, every entry carries the sources inline, so that a
field officer can verify the recommendation and an extension officer can follow it up.

---

## 5.6 The API service and the web client

**Lead: Bemnet Tesfaye (API) with Yohannes Berhanu (web client)**

### 5.6.1 The API

The FastAPI service exposes ten endpoints under `/v1`, with an OpenAPI 3.1 schema committed to
the repository and validated against the running application in CI on every pull request.

**Table 5.7** — The endpoints.

| Method and path | Purpose | Auth |
|---|---|---|
| `POST /v1/predict` | Classify an uploaded image; returns the class, the confidence vector, the ranked alternatives, the abstention decision and the model version | Required |
| `GET /v1/diagnoses` | List the history, filtered by class and date range, with pagination | Required |
| `GET /v1/diagnoses/{id}` | Retrieve one diagnosis | Required |
| `POST /v1/diagnoses` | Record a diagnosis from the optional device export; idempotent on the client-generated id | Required |
| `DELETE /v1/diagnoses/{id}` | Delete a diagnosis | Required |
| `GET /v1/kb` | The complete knowledge base | Required |
| `GET /v1/kb/{class_key}` | One knowledge-base entry | Required |
| `GET /v1/health` | The service status and the deployed model version | Not required |
| `GET /v1/metrics` | The server's evaluation metrics, exactly as reported in Chapter 6 | Required |
| `GET /v1/metrics/model-card` | The model card | Not required |

The upload endpoint enforces a 20 MB limit, validates the content by its magic bytes rather
than by its extension or its client-supplied MIME type, and returns a structured error object
with a correlation identifier. Every mutating endpoint requires a JWT bearer token, and the
rate limiter returns 429 with a `Retry-After` header beyond 60 requests per minute.

### 5.6.2 The web client

The web client is a static HTML, CSS and JavaScript application with no build step. It
reuses the API's OpenAPI schema to generate its request shapes, and it mirrors the mobile
client's result, guidance and history screens. It adds a **dataset-note panel** listing the
model version and the macro-F1 achieved on each external dataset, so that a visitor sees the
honest performance profile rather than only the demonstration.

### 5.6.3 Deployment and CI

The API is packaged as a single Docker container running as a non-root user, deployed behind
a TLS-terminating proxy, with PostgreSQL as a managed instance. Migrations are applied by the
deployment script and never by hand.

**Table 5.8** — The CI pipeline.

| Job | Trigger | What it checks |
|---|---|---|
| `lint` | Every push and pull request | `ruff` for Python, `flutter analyze` for Dart, `eslint` for the web client |
| `unit-test` | Every push and pull request | The pytest and Dart test suites; the coverage gate at 80 % on the inference wrapper, the history layer and the API |
| `split-audit` | Every push | Re-runs the leakage audit against the committed manifest |
| `kb-audit` | Every push | Every class has all ten fields; every practice has a citation |
| `golden-image` | Every push | The Dart and Python preprocessing agree element by element |
| `openapi-diff` | Every push | The committed schema matches the running application |
| `secret-scan` | Every push and every pull request | `gitleaks` over the whole history |
| `container-build` | Every push to `main` | The Docker image builds and the health endpoint responds |
| `artefact-check` | On a release tag | The model artefact's size and checksum, and that `labels.txt` matches the API enum |

---

## 5.7 Reproducibility package (Guideline §9.7)

**Lead: Hayredin Mohammed with Yohannes Berhanu**

The package contains the code, the configuration, the environment file, the instructions for
obtaining the data, the trained model artefact and the training script, and `results.md` —
the table linking each reported result to the script that produced it.

**Table 5.9** — The reproducibility package contents. *To be completed.*

| Result reported in Chapter 6 | Script | Output file | Command |
|---|---|---|---|
| The internal test comparison (Table 6.2) | `training/evaluate_internal.py` | `results/E-02_internal.csv` | `python training/evaluate_internal.py --manifest data/split_manifest.csv --seeds 42,43,44` |
| The external evaluation (Table 6.3) | `training/evaluate_external.py` | `results/E-03_external.csv` | `python training/evaluate_external.py --model model/model_int8.tflite --sets uganda,rocole,peru,coffeeleafco,silva` |
| The ablation (Table 6.4) | `training/ablate.py` | `results/E-04_ablation.csv` | `python training/ablate.py --configs configs/ablation/*.yaml` |
| The calibration (Table 6.5) | `training/calibrate.py` | `results/E-05_calibration.md` | `python training/calibrate.py --split validation` |
| The coverage curve (Figure 6.3) | `training/selective_risk.py` | `results/E-06_coverage.csv` | `python training/selective_risk.py` |
| The significance test (Table 6.6) | `training/significance.py` | `results/E-07_significance.md` | `python training/significance.py --a results/E-02_internal.csv --b results/E-04_ablation.csv` |
| The on-device latency (Table 6.7) | `mobile/bench/` | `results/E-08_latency.csv` | `bash scripts/bench_device.sh` |
| The model size (Table 6.7) | `model/export_tflite.py` | `results/E-11_size.csv` | `python model/export_tflite.py --report` |

---

*Sections to complete as the work progresses: the observed audit results in §5.2, the
measured artefact sizes in §5.3, the knowledge-base table in §5.5, and the final command
list in §5.7.*
