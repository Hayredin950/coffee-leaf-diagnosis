# Database Design and API Specification

**Owner:** Yohannes Berhanu
**Applies to:** the on-device SQLite store (mobile client) and the server-side PostgreSQL
store (API service). Guideline §8.2 requires: *"document the schema design, relationships,
constraints, normalization, indexing, transactions, security, and backup and recovery
considerations. Provide creation and migration scripts and seed data that contains no real
personal data."*

---

# Part A — Database design

## A.1 Design principles

1. **The device store is the source of truth for the user's history in v1.** The server store
   exists to serve the web client and to receive optional exports. There is no bidirectional
   sync in v1, so no conflict resolution is needed — this is a deliberate scope reduction.
2. **Same logical schema, two physical implementations.** The seven fields of FR-14 exist in
   both stores with the same names, types and semantics, so an export is a lossless copy.
3. **The confidence vector is stored as a JSON column**, not as five columns, because it is
   read and written as a unit and its shape may change with the class count in a future model
   version. The top-1 class and confidence are also stored as scalar columns because they are
   the fields that are filtered and sorted.
4. **Normalisation.** The `diagnoses` table is in 3NF for its own attributes; the only
   repetition — `model_version` and `kb_version` — is a version string, deliberately denormalised
   so a historic record can always be interpreted with the artefact that produced it.
5. **No personal data.** No name, no email, no location, no device identifier. The optional
   `notes` field is free text that the user types; it is their responsibility.

## A.2 Entity-relationship diagram (Figure 4.9)

```mermaid
erDiagram
    DIAGNOSIS {
        text_id          PK "uuid, client-generated"
        text_timestamp_utc "timestamptz NOT NULL"
        text_image_path  "text NOT NULL"
        text_label       "text NOT NULL"
        text_top1_confidence "real NOT NULL"
        text_confidence_vector "jsonb NOT NULL"
        text_model_version "text NOT NULL"
        text_kb_version  "text NOT NULL"
        text_device_note "text NULL"
        text_notes       "text NULL"
        text_created_at  "timestamptz NOT NULL"
    }
    DIAGNOSIS ||--o{ DIAGNOSIS_IMAGE : "has"
    DIAGNOSIS_IMAGE {
        text_id          PK "uuid"
        text_diagnosis_id FK
        text_uri         "text NOT NULL"
        text_sha256      "text NOT NULL"
        text_bytes       "integer NOT NULL"
    }
    MODEL_VERSION {
        text_version     PK "semver"
        text_sha256      "text NOT NULL"
        text_input_size  "integer NOT NULL"
        text_quantisation "text NOT NULL"
        real_temperature "real NOT NULL"
        real_accept_threshold "real NOT NULL"
        text_labels_json "jsonb NOT NULL"
        text_created_at  "timestamptz NOT NULL"
    }
    KB_VERSION {
        text_version     PK "semver"
        text_sha256      "text NOT NULL"
        text_created_at  "timestamptz NOT NULL"
    }
    DIAGNOSIS }o--|| MODEL_VERSION : "produced by"
    DIAGNOSIS }o--|| KB_VERSION : "interpreted with"
```

**Figure 4.9** — ER diagram.

## A.3 Table definitions

### A.3.1 Server — PostgreSQL

```sql
-- migrations/0001_initial.sql

CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE model_version (
    version            text PRIMARY KEY,
    sha256             text NOT NULL,
    input_size         integer NOT NULL,
    quantisation       text NOT NULL CHECK (quantisation IN ('float32','float16','int8')),
    temperature        real    NOT NULL CHECK (temperature > 0),
    accept_threshold   real    NOT NULL CHECK (accept_threshold BETWEEN 0 AND 1),
    labels_json        jsonb   NOT NULL,
    created_at         timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE kb_version (
    version      text PRIMARY KEY,
    sha256       text NOT NULL,
    created_at   timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE diagnosis (
    id                  uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp_utc       timestamptz NOT NULL,
    image_path          text NOT NULL,
    label               text NOT NULL,
    top1_confidence     real NOT NULL CHECK (top1_confidence BETWEEN 0 AND 1),
    confidence_vector   jsonb NOT NULL,
    model_version       text NOT NULL REFERENCES model_version(version),
    kb_version          text NOT NULL REFERENCES kb_version(version),
    device_note         text,
    notes               text,
    created_at          timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT confidence_vector_has_five CHECK (jsonb_array_length(confidence_vector) = 5),
    CONSTRAINT label_is_known CHECK (
        label IN ('coffee_leaf_rust','cercospora_leaf_spot','leaf_miner','phoma_leaf_spot','healthy')
    )
);

CREATE TABLE diagnosis_image (
    id           uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    diagnosis_id uuid NOT NULL REFERENCES diagnosis(id) ON DELETE CASCADE,
    uri          text NOT NULL,
    sha256       text NOT NULL,
    bytes        integer NOT NULL CHECK (bytes > 0)
);

CREATE INDEX idx_diagnosis_timestamp   ON diagnosis (timestamp_utc DESC);
CREATE INDEX idx_diagnosis_label       ON diagnosis (label);
CREATE INDEX idx_diagnosis_ts_label    ON diagnosis (timestamp_utc DESC, label);
CREATE INDEX idx_diagnosis_model_ver   ON diagnosis (model_version);
CREATE INDEX idx_image_diagnosis       ON diagnosis_image (diagnosis_id);
CREATE INDEX idx_diagnosis_vector_gin  ON diagnosis USING gin (confidence_vector);
```

**Why these indexes.** FR-22 requires filtering by class and by date range, and the history
list is always ordered newest-first — `idx_diagnosis_ts_label` serves the default list query and
the class-filtered list query. `idx_diagnosis_timestamp` serves the pure date-range query and
the pagination cursor. `idx_diagnosis_vector_gin` exists because the evaluation queries in
Chapter 6 need to select records by confidence range; it is optional and should be dropped if
the query plan shows it is unused.

### A.3.2 Device — SQLite (Drift)

```dart
// mobile/lib/data/tables/diagnoses_table.dart

class Diagnoses extends Table {
  TextColumn  get id              => text()();
  DateTimeColumn get timestampUtc => dateTime()();
  TextColumn  get imagePath       => text()();
  TextColumn  get label           => text()();
  RealColumn  get top1Confidence  => real()();
  TextColumn  get confidenceVector => text()();   // JSON-encoded map
  TextColumn  get modelVersion    => text()();
  TextColumn  get kbVersion       => text()();
  TextColumn  get deviceNote      => text().nullable()();
  TextColumn  get notes           => text().nullable()();
  DateTimeColumn get createdAt    => dateTime().withDefault(currentDateAndTime)();

  @override
  Set<Column> get primaryKey => {id};
}

class DiagnosisImages extends Table {
  TextColumn  get id           => text()();
  TextColumn  get diagnosisId  => text().references(Diagnoses, #id, onDelete: KeyAction.cascade)();
  TextColumn  get uri          => text()();
  TextColumn  get sha256       => text()();
  IntColumn   get bytes        => integer()();

  @override
  Set<Column> get primaryKey => {id};
}
```

**Device indices** (SQLite): `idx_diagnoses_timestamp (timestamp_utc DESC)`,
`idx_diagnoses_label (label)`. The dataset is at most a few thousand rows on a phone, so the
index set is deliberately minimal — over-indexing a phone database costs write performance for
no measurable query gain.

### A.3.3 Data dictionary

| Table | Column | Type | Null | Constraint | Meaning |
|---|---|---|---|---|---|
| diagnosis | `id` | uuid | no | PK | Client-generated UUID v4. Generated on-device so an export never needs a round trip |
| diagnosis | `timestamp_utc` | timestamptz / integer | no | — | The moment the diagnosis was produced, in UTC |
| diagnosis | `image_path` | text | no | — | URI of the stored leaf photograph (app-private path on device) |
| diagnosis | `label` | text | no | IN (5 classes) | The predicted class key |
| diagnosis | `top1_confidence` | real | no | 0 ≤ x ≤ 1 | The calibrated top-1 probability |
| diagnosis | `confidence_vector` | jsonb / text | no | 5 elements | The calibrated probability for each of the five classes |
| diagnosis | `model_version` | text | no | FK → model_version | The semver of the artefact that produced this record |
| diagnosis | `kb_version` | text | no | FK → kb_version | The semver of the KB that would interpret this record |
| diagnosis | `device_note` | text | yes | — | Optional free-text note entered by the user |
| diagnosis | `notes` | text | yes | — | Optional free-text note (kept separate from `device_note` for the server's use) |
| diagnosis | `created_at` | timestamptz | no | default now() | When the row was written |
| diagnosis_image | `id` | uuid | no | PK | Image record identifier |
| diagnosis_image | `diagnosis_id` | uuid | no | FK → diagnosis, CASCADE | Owning diagnosis |
| diagnosis_image | `uri` | text | no | — | Object-store URI or local path |
| diagnosis_image | `sha256` | text | no | — | Content hash, for integrity verification |
| diagnosis_image | `bytes` | integer | no | > 0 | File size in bytes |
| model_version | `version` | text | no | PK | Semver, e.g. `1.2.0` |
| model_version | `sha256` | text | no | — | Checksum of `model.tflite`; verified at load time |
| model_version | `input_size` | integer | no | — | 224 |
| model_version | `quantisation` | text | no | enum | float32 / float16 / int8 |
| model_version | `temperature` | real | no | > 0 | Temperature-scaling parameter T |
| model_version | `accept_threshold` | real | no | 0 ≤ x ≤ 1 | The abstention threshold |
| model_version | `labels_json` | jsonb | no | — | The ordered label array, so the order is data, not code |
| kb_version | `version` | text | no | PK | Semver of the knowledge base |
| kb_version | `sha256` | text | no | — | Checksum of `knowledge_base.json` |

## A.4 Transactions

| Operation | Transaction scope | Isolation |
|---|---|---|
| Record a diagnosis | Single transaction: insert `diagnosis` + insert `diagnosis_image` | SQLite: a single write transaction; PostgreSQL: `READ COMMITTED` |
| Delete a diagnosis | Single transaction: delete `diagnosis` (the image cascades) | — |
| Export history | A single read-only transaction with a consistent snapshot, so the CSV cannot contain a partially-written set | PostgreSQL: `REPEATABLE READ` for the export |
| Model/kb registration | Insert into `model_version` / `kb_version` **before** any diagnosis references it — the FK forbids the other order | — |
| Optional client export | One transaction per batch of records, with client-generated ids making the operation idempotent on retry | — |

**Idempotency.** Because the client generates the UUID, a retried export cannot create
duplicates. This is why the id is generated on the device rather than by the server.

## A.5 Migrations

- **Server:** Alembic. `alembic revision --autogenerate -m "..."`, then a hand-edited,
  reviewed migration file. Migrations are applied by the deployment script, never by hand.
- **Device:** Drift's `MigrationStrategy`. `schemaVersion` is stored in the app's shared
  preferences. The upgrade path from v1 to v2 is covered by test **T-40** with a fixture
  database created at v1.
- **Migration rules:** every migration is forward-only and must not destroy data; a destructive
  change requires a table rebuild plus a copy, and it must be reviewed by a second member.

## A.6 Seed data

`scripts/seed.sql` inserts:
- one row per `model_version` for each artefact the group releases, and
- one row per `kb_version`.

**It contains no diagnosis records and no personal data** (Guideline §8.2 requires seed data
with "no real personal data"). Diagnosis rows are created only by real usage or by the test
fixtures, which use synthetic records.

## A.7 Backup and recovery

| Store | Backup | Recovery | RPO / RTO |
|---|---|---|---|
| Device SQLite | The CSV export (FR-19) is the user-facing backup. An optional encrypted local snapshot may be added | Restore from the CSV | The history is reconstructible from the export; no server dependency |
| Server PostgreSQL | Managed automated daily snapshots (the host's standard offering), retained 7 days | Restore to a new instance and repoint the connection | RPO ≤ 24 h, RTO ≤ 1 h |
| Model artefacts | Stored in the repository under `model/` with a SHA-256 manifest; released as a versioned release asset | `git checkout` the tag and re-export | RPO 0 (version control) |
| Knowledge base | `data/knowledge_base.json` under version control with a version field and a checksum | `git checkout` the tag | RPO 0 |

**Deliberate non-goal:** no continuous archiving of user images. Storing leaf photographs in
the cloud indefinitely has privacy and cost implications that this project does not need, and
the app's value proposition is offline operation.

## A.8 Security of the data stores

- The device database lives in the app's private directory, sandboxed by the Android
  application sandbox. No world-readable storage.
- The server database uses a least-privilege application role; migrations use a separate
  role. No password is stored in the code or in the image — only a secret reference.
- No encryption-at-rest beyond the host's default disk encryption is claimed. This is stated
  as a limitation in Chapter 7.
- Because no personal data is stored, a data-subject request mechanism is not applicable —
  this is stated explicitly in Appendix M.

---

# Part B — API specification

**Base URL:** `https://<host>/v1`
**Media type:** `application/json`; uploads are `multipart/form-data`
**Authentication:** `Authorization: Bearer <JWT>` on all mutating endpoints.
**Documentation:** OpenAPI 3.1 at `/docs`; the schema is exported to `api/openapi.json` and
committed, so the contract is reviewable in a pull request.

## B.1 Error format

```json
{
  "error": {
    "code": "IMAGE_TOO_LARGE",
    "message": "The image is too large. The maximum accepted size is 20 MB.",
    "correlation_id": "5f3c9a1e-2b7d-4c8a-9f10-3a4b5c6d7e8f"
  }
}
```

| HTTP | `code` | When |
|---|---|---|
| 400 | `MALFORMED_REQUEST` | The body cannot be parsed |
| 401 | `UNAUTHORIZED` | Missing or invalid token on a mutating endpoint |
| 404 | `NOT_FOUND` | Unknown diagnosis id, class key or route |
| 413 | `PAYLOAD_TOO_LARGE` | Upload exceeds the size limit |
| 415 | `UNSUPPORTED_MEDIA_TYPE` | The upload is not an image (magic-byte check) |
| 422 | `VALIDATION_ERROR` | Pydantic validation failure; `details` lists the offending fields |
| 429 | `RATE_LIMITED` | The client exceeded the rate limit |
| 500 | `INTERNAL_ERROR` | An unexpected failure; the correlation id is logged |

## B.2 Endpoints

### `POST /v1/predict` — classify an image

**Auth:** required · **Request:** `multipart/form-data`, field `image` (a JPEG or PNG,
≤ 20 MB) · **Optional:** `apply_abstention` (bool, default `true`)

**200 response**
```json
{
  "label": "coffee_leaf_rust",
  "display_name": "Coffee Leaf Rust",
  "top1_confidence": 0.871,
  "confidence_vector": {
    "coffee_leaf_rust": 0.871,
    "cercospora_leaf_spot": 0.061,
    "leaf_miner": 0.037,
    "phoma_leaf_spot": 0.021,
    "healthy": 0.010
  },
  "ranked": [
    {"label": "coffee_leaf_rust", "confidence": 0.871},
    {"label": "cercospora_leaf_spot", "confidence": 0.061}
  ],
  "accepted": true,
  "abstain_reason": null,
  "model_version": "1.2.0",
  "kb_version": "1.0.0",
  "inference_ms": 143
}
```

**Behaviour:** with `apply_abstention=true` and a top-1 below the threshold, the response has
`accepted: false`, `abstain_reason: "LOW_CONFIDENCE"`, and `label: null` — the server does not
present an unconfident class as a diagnosis either. With `apply_abstention=false`, the label
is always returned; this mode exists for the evaluation harness in Chapter 6, which needs the
unfiltered vector.

**Errors:** 401, 413, 415, 422, 429.

### `GET /v1/diagnoses` — list history

**Auth:** required · **Query:** `label` (optional, one of the five), `from` and `to`
(ISO-8601 datetimes), `limit` (default 50, max 200), `cursor` (opaque pagination cursor).

**200 response**
```json
{
  "items": [
    {
      "id": "0f3c1a7e-8b2d-4a1c-9e3f-1d2c3b4a5e6f",
      "timestamp_utc": "2027-03-14T08:22:41Z",
      "label": "coffee_leaf_rust",
      "display_name": "Coffee Leaf Rust",
      "top1_confidence": 0.871,
      "confidence_vector": { "...": "..." },
      "model_version": "1.2.0",
      "kb_version": "1.0.0",
      "notes": null,
      "image": {"uri": "https://.../0f3c1a7e.jpg", "sha256": "9c1f...", "bytes": 184233}
    }
  ],
  "next_cursor": "eyJ0cyI6IjIwMjctMDMtMTRUMDg6MjI6NDFaIn0=",
  "total_estimate": 128
}
```

### `GET /v1/diagnoses/{id}`
**Auth:** required · Returns the object above, or 404.

### `POST /v1/diagnoses` — record a diagnosis (used by the optional device export)

**Auth:** required · **Request:** the diagnosis object; the `id` is client-generated.

**201 response:** the stored object. **Idempotent:** posting the same `id` twice returns the
existing record with 200 rather than creating a duplicate.

### `DELETE /v1/diagnoses/{id}`
**Auth:** required · **204** on success, **404** if unknown.

### `GET /v1/kb` — the whole knowledge base

**200 response**
```json
{
  "kb_version": "1.0.0",
  "classes": [
    {
      "class_key": "coffee_leaf_rust",
      "display_name": "Coffee Leaf Rust",
      "scientific_name": "Hemileia vastatrix",
      "local_names": ["የቡና ርስት", "leaf rust"],
      "symptoms": "...",
      "severity_cues": "...",
      "risk_factors": "...",
      "organic_control": "...",
      "chemical_control": "...",
      "prevention": "...",
      "sources": [
        {"citation_key": "[56]", "title": "...", "publisher": "...", "url": "...", "accessed_date": "2026-10-21"}
      ]
    }
  ]
}
```

### `GET /v1/kb/{class_key}`
**200** for one of the five keys · **404** for anything else.

### `GET /v1/health`
```json
{ "status": "ok", "model_version": "1.2.0", "kb_version": "1.0.0", "uptime_s": 51234 }
```
**No authentication** — it must be callable by a monitor and must not leak sensitive data.

### `GET /v1/metrics`
**Auth:** required · Returns the server-side evaluation metrics, exactly as reported in
Chapter 6: per-dataset macro-F1, per-class F1, the acceptance threshold, and the ECE.

## B.3 Security controls on the API

| Control | Implementation |
|---|---|
| Authentication | JWT bearer token, 1-hour expiry, signed with an environment secret |
| Authorisation | The token subject scopes which diagnoses are visible |
| Input validation | Pydantic v2 models on every request; a `field_validator` on the upload enforces the size and the magic bytes |
| Rate limiting | 60 requests/minute per client, token-bucket; 429 with `Retry-After` |
| CORS | Only the declared web origin; `allow_credentials` off for the public read path |
| HTTPS | Terminated at the host's proxy; HSTS |
| Secrets | Environment variables only; `.env.example` in the repo; `.env` gitignored; `gitleaks` in CI |
| Uploads | Stored outside the web root; served only through an authorised route; never executed |
| Logging | Structured, with a correlation id; no image bytes and no free-text notes in the logs |
| Container | Runs as a non-root user; read-only filesystem except the data volume |

## B.4 Versioning and compatibility

The API is versioned by the `/v1` path prefix. A breaking change requires `/v2` and a
deprecation window of at least one semester; the mobile app pins the API version it was
built against and warns if the server reports a newer major version. The **knowledge base**
and the **model artefact** are versioned independently by semver and carried on every record,
so a historic diagnosis can always be re-interpreted with the artefact that produced it.

## B.5 API test coverage

| Endpoint | Minimum tests |
|---|---|
| `POST /v1/predict` | Valid image; non-image; oversized; undersized; unauthenticated; rate-limited; abstention path returns `label: null` |
| `GET /v1/diagnoses` | Empty; filtered by label; filtered by date range; pagination; unauthorised subject sees only its own |
| `GET /v1/diagnoses/{id}` | Known id; unknown id |
| `POST /v1/diagnoses` | Created; duplicate id is idempotent; invalid payload rejected |
| `DELETE /v1/diagnoses/{id}` | Deleted; unknown id |
| `GET /v1/kb`, `/v1/kb/{key}` | All five keys; unknown key; the schema check confirms the 10 fields |
| `GET /v1/health` | 200 and the required fields |
| `GET /v1/metrics` | The numbers match the report exactly |

**Contract test.** The committed `api/openapi.json` is validated against the running app in CI
with a schema-diff check. A change to an endpoint without a matching change to the committed
schema fails the build — which is how the web client is prevented from breaking silently.
