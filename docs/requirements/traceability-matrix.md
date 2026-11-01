# Objective-to-Evidence Traceability Matrix (Appendix E)

> **Guideline §10.6:** *"Use the matrix in Appendix E to connect objectives, requirements, design,
> implementation, tests and results. Start the matrix in Final Year Project I and complete it in
> Final Year Project II."* §10.5: *"The final report must state whether each objective was
> achieved, partially achieved, or not achieved, and must cite the evidence."*
>
> **Template (Appendix E):** Objective · Requirement(s) · Design artifact · Implementation or
> research output · Test/evaluation · Result · Achievement.
> **Achievement values:** achieved · partially achieved · not achieved. *"Each claim must be
> supported by identifiable evidence."*
>
> **Status:** ☐ Started in FYP I  ☑ Started (v0.1, FYP I week 7)  ☐ Completed (FYP II week 24)
> **Owner:** Nahom Solomon · **Contributors:** all four members sign off their own rows.

---

## Legend

| Code | Meaning |
|---|---|
| `T-##` | Test case ID — see `docs/requirements/test-plan.md` and `docs/appendices/Appendix-F-Test-Cases.md` |
| `E-##` | Evaluation experiment ID — see §3 below |
| `[PENDING]` | Not yet produced. **Replace every one of these before FYP II week 24.** |
| `[FIG 4.x]` | A figure in the report |
| `[CH x.y]` | A section in the report |

---

## 1. Objectives → requirements → design → implementation → test → result

| Objective | Requirement(s) | Design artifact | Implementation or research output | Test / evaluation | Result | Achievement |
|---|---|---|---|---|---|---|
| **SO1** — Curate and document a leakage-safe, multi-source coffee leaf corpus with a datasheet and a documented split | DR-01…DR-06, DR-08; NFR-09, NFR-27, NFR-28, NFR-32 | [FIG 4.1] corpus composition diagram; [FIG 4.2] duplicate-grouping and split pipeline; `data/datasheet.md` | `scripts/prepare_data.py` (grouping + split); `data/split_manifest.csv`; `data/datasheet.md` | T-01…T-06; E-01 (split integrity audit) | `[PENDING]` | `[PENDING]` |
| **SO2** — Train and compare ≥3 lightweight models against baselines under identical conditions | FR-06, FR-07; NFR-28, NFR-29, NFR-31 | [FIG 4.3] training pipeline; `docs/design/architecture.md` §5 | `training/` — majority-class baseline, MobileNetV3-Small, EfficientNet-Lite0, MobileNetV2; `configs/*.yaml`; `results.md` | T-07…T-10; E-02 (internal test comparison, 3 seeds) | `[PENDING]` | `[PENDING]` |
| **SO3** — Quantify the generalisation gap on ≥3 external field datasets, and mitigate it with abstention | FR-05, FR-07, FR-09, FR-10, FR-13; NFR-11, NFR-28, NFR-29; DR-05, DR-07, DR-08 | [FIG 4.4] evaluation protocol; [FIG 4.5] external dataset map; `data/model-card.md` | `training/evaluate_external.py`; `training/calibrate.py` (temperature scaling); `training/ablate.py`; `data/model-card.md` | T-11…T-16; E-03 (5 external datasets); E-04 (ablation); E-05 (calibration + ECE); E-06 (coverage/selective-risk curve); E-07 (McNemar significance) | `[PENDING]` | `[PENDING]` |
| **SO4** — On-device inference: capture/upload, quantised TFLite, ≤10 MB, ≤500 ms median, fully offline | FR-01…FR-04, FR-06…FR-12, FR-21, FR-31; NFR-01…NFR-06, NFR-08, NFR-10, NFR-16, NFR-22, NFR-34 | [FIG 4.6] deployment diagram; [FIG 4.7] inference sequence diagram; [FIG 4.8] app state diagram | `mobile/` Flutter app; `model/` `model.tflite` + `labels.txt` + `metadata.json`; `model/export_tflite.py` | T-17…T-26; E-08 (latency on 3 devices); E-09 (memory footprint); E-10 (airplane-mode feature pass); E-11 (model size) | `[PENDING]` | `[PENDING]` |
| **SO5** — Results and guidance: per-class confidence plus a sourced agronomic knowledge base | FR-11, FR-12, FR-13, FR-25, FR-32, FR-35…FR-37; NFR-09, NFR-25 | [FIG 4.9] KB schema; [FIG 4.10] result→guidance flow | `data/knowledge_base.json`; `data/knowledge-base.md` (sources); `mobile/lib/kb/` resolver; `api/app/routers/kb.py` | T-27…T-32; E-12 (KB schema + citation audit); E-13 (JARC review sign-off); E-14 (user comprehension check) | `[PENDING]` | `[PENDING]` |
| **SO6** — Persistent local diagnosis history with search, filter and export | FR-14…FR-20, FR-22…FR-24, FR-33; NFR-07, NFR-23, NFR-24 | [FIG 4.11] ER diagram; `docs/design/database-schema.md`; [FIG 4.12] history sequence diagram | `mobile/lib/data/` (SQLite/Drift schema, DAOs, migrations); `api/app/` (SQLAlchemy models, Alembic migrations) | T-33…T-40; E-15 (restart persistence); E-16 (migration test); E-17 (10k-record query benchmark) | `[PENDING]` | `[PENDING]` |
| **SO7** — Test and evaluate the complete system against every objective | All FR/NFR/DR | [FIG 4.13] test-level pyramid; `docs/requirements/test-plan.md` | `tests/` (unit, integration, system, performance, security, usability); `docs/appendices/Appendix-F-Test-Cases.md` | T-01…T-46; E-18 (SUS study, ≥10 participants); E-19 (defect register summary) | `[PENDING]` | `[PENDING]` |

---

## 2. Objective → research question → evidence

| Objective | Research question | Hypothesis | Experiment | Decision rule (fixed **before** running) | Result | Achievement |
|---|---|---|---|---|---|---|
| SO3 | RQ1 — How large is the internal→external macro-F1 drop, and how does it vary by class and dataset? | H1: the drop on external field photographs is ≥ 20 macro-F1 points | E-03 | Report the drop; H1 is **supported** if the mean drop across the five external datasets is ≥ 20 points | `[PENDING]` | `[PENDING]` |
| SO3 | RQ2 — Which of augmentation / calibration / African-field-data inclusion most improves external macro-F1 per MB of deployed size? | H2: adding the Uganda field dataset + field-realistic augmentation gains ≥ 5 external macro-F1 points at < 1 MB extra | E-04 | The variant with the best external macro-F1 per MB wins; pairwise significance by McNemar at α = 0.05 | `[PENDING]` | `[PENDING]` |
| SO3 | RQ3 — Calibration and abstention | H3: temperature scaling + threshold reduce ECE by ≥ 30 % relative, retaining ≥ 60 % coverage | E-05, E-06 | H3 supported if relative ECE reduction ≥ 30 % at coverage ≥ 60 % | `[PENDING]` | `[PENDING]` |
| SO4 | RQ4 — Accuracy under a 10 MB / 1 s budget | — | E-08, E-09, E-11 | Report the accuracy/latency/size Pareto frontier across float32, float16 and int8 | `[PENDING]` | `[PENDING]` |
| SO5 | RQ5 — Is the guidance defensible and comprehensible? | — | E-12, E-13, E-14 | All 5 classes complete; 100 % of practices cited; ≥ 80 % of participants correctly state the recommended first action | `[PENDING]` | `[PENDING]` |

---

## 3. Evaluation experiment register

Each experiment has one script and one results file. The "script that produced it" column is
mandatory in §9.7 and is also the "results-to-script table" of the reproducibility package.

| E-ID | Experiment | Script | Input | Output artefact | Report reference |
|---|---|---|---|---|---|
| E-01 | Split integrity audit (no image or duplicate group spans two splits) | `training/audit_split.py` | `data/split_manifest.csv` | `results/E-01_split_audit.md` | [CH 4.3] |
| E-02 | Internal test comparison — 4 models × 3 seeds | `training/train.py`, `training/evaluate_internal.py` | `data/splits/` | `results/E-02_internal.csv` | [CH 6.2] |
| E-03 | External evaluation on 5 field datasets | `training/evaluate_external.py` | trained models + `data/external/` | `results/E-03_external.csv` | [CH 6.3] |
| E-04 | Ablation: augmentation × training-data source | `training/ablate.py` | `configs/ablation/*.yaml` | `results/E-04_ablation.csv` | [CH 6.4] |
| E-05 | Temperature scaling + ECE | `training/calibrate.py` | validation split + external sets | `results/E-05_calibration.md` | [CH 6.5] |
| E-06 | Acceptance-coverage and selective-risk curves | `training/selective_risk.py` | external predictions | `results/E-06_coverage.csv` | [CH 6.5] |
| E-07 | McNemar significance test for the headline comparison | `training/significance.py` | paired predictions | `results/E-07_significance.md` | [CH 6.6] |
| E-08 | On-device latency, 3 devices × 50 runs | `mobile/bench/` + `scripts/bench_device.sh` | `.tflite` artefact | `results/E-08_latency.csv` | [CH 6.7] |
| E-09 | Memory footprint | `adb shell dumpsys meminfo` | app running | `results/E-09_memory.md` | [CH 6.7] |
| E-10 | Airplane-mode feature verification | manual protocol `docs/requirements/test-plan.md` §7 | app build | `results/E-10_offline.md` | [CH 6.8] |
| E-11 | Model size across quantisations | `model/export_tflite.py` | float32 checkpoint | `results/E-11_size.csv` | [CH 6.7] |
| E-12 | KB schema + citation completeness audit | `scripts/audit_kb.py` | `data/knowledge_base.json` | `results/E-12_kb_audit.md` | [CH 5.4] |
| E-13 | JARC expert review | manual, `docs/appendices/Appendix-G-Contribution.md` (review record) | KB draft | signed review note | [CH 5.4] |
| E-14 | User comprehension check | `docs/requirements/test-plan.md` §8 | usability session | `results/E-14_comprehension.csv` | [CH 6.9] |
| E-15 | History persistence across restart | `mobile/test/` | app build | test-case record | [CH 6.2] |
| E-16 | Schema migration v1→v2 | `mobile/test/migration_test.dart` | migration fixtures | test-case record | [CH 6.2] |
| E-17 | History query benchmark at 10k records | `scripts/bench_history.py` | seeded DB | `results/E-17_query_bench.csv` | [CH 6.7] |
| E-18 | SUS usability study | `docs/requirements/test-plan.md` §8 | ≥10 participants | `results/E-18_sus.csv` | [CH 6.9] |
| E-19 | Defect register summary | `docs/appendices/Appendix-F-Test-Cases.md` | all test cases | `results/E-19_defects.md` | [CH 6.10] |

---

## 4. Requirement → test coverage check

Guideline §10.5 requires every objective to have a corresponding implementation and evaluation
method; §10.2 requires each test case to name the requirement it covers. This table proves
coverage in the other direction: **every requirement is covered by at least one test.**

| Requirement group | Covered by | Status |
|---|---|---|
| FR-01…FR-05 (acquisition, validation, quality) | T-17…T-21, T-50 | `[PENDING]` |
| FR-06…FR-13 (inference, confidence, abstention, guidance) | T-22…T-26, T-42, T-43 | `[PENDING]` |
| FR-14…FR-20 (history) | T-33…T-40 | `[PENDING]` |
| FR-21…FR-30 (API) | T-51…T-60 | `[PENDING]` |
| FR-31…FR-34 (web client) | T-61…T-64 | `[PENDING]` |
| FR-35…FR-37 (KB content) | T-27…T-32, E-12, E-13 | `[PENDING]` |
| NFR-01…NFR-07 (performance) | T-45…T-48, E-08, E-09, E-11, E-17 | `[PENDING]` |
| NFR-08…NFR-10 (offline) | T-49, T-50, E-10 | `[PENDING]` |
| NFR-11…NFR-16 (usability, localisation, platform) | E-18, E-14, T-65 | `[PENDING]` |
| NFR-17…NFR-25 (security, privacy) | T-52, T-53, T-54, T-55, T-56 | `[PENDING]` |
| NFR-26…NFR-35 (maintainability, reproducibility) | T-57, T-58, T-59, T-60; CI configuration | `[PENDING]` |
| DR-01…DR-08 (data) | T-01…T-06, E-01, E-03, E-12 | `[PENDING]` |

---

## 5. Design consistency check (Guideline §7.5)

*"Diagrams must represent the actual proposed or implemented system. Requirements, models,
database structures, interfaces and implementation must not contradict one another."*

| Pair to check | Check | Status |
|---|---|---|
| FR-21…FR-30 ↔ `api/` routers and the OpenAPI schema | Endpoint paths, methods, status codes and payload fields match the specification exactly | `[PENDING]` |
| FR-14…FR-20 ↔ `docs/design/database-schema.md` ↔ `mobile/lib/data/` ↔ `api/app/models.py` | The seven logged fields in FR-14 exist as columns in both the on-device and the server schema, with matching names and types | `[PENDING]` |
| FR-06 ↔ `data/knowledge_base.json` ↔ `model/labels.txt` | The five label strings are identical across the model artefact, the KB, the API schema and the UI | `[PENDING]` |
| FR-09 ↔ the threshold in `model/model-card.md` ↔ the value read by the app at inference time | One constant; changing it changes the model card and the behaviour together | `[PENDING]` |
| FR-35 (10 KB fields) ↔ the KB JSON schema ↔ the rendering widgets | Every field in the JSON is rendered; no field is rendered that is not in the schema | `[PENDING]` |
| NFR-02 (≤10 MB) ↔ the artefact actually shipped in the APK | Measured, not asserted | `[PENDING]` |

---

## 6. Completion checklist before FYP II submission

- [ ] Every `[PENDING]` in this file is replaced by a real value with a citation to the results file.
- [ ] Every objective has an explicit **achieved / partially achieved / not achieved** value and a reason.
- [ ] Every test case in Appendix F has an actual result and a status.
- [ ] Every experiment in §3 has a results file committed to the repository.
- [ ] The results-to-script table in `results.md` maps every reported number to its script.
- [ ] Objective-to-evidence consistency with Chapters 1, 2, 6 and 7 is verified by Nahom Solomon.
- [ ] Each member confirms the rows that reflect their own work.
