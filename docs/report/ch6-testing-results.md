# Chapter 6 — Testing, Results and Discussion

> **Owner:** the four members jointly; Hayredin leads §6.2–§6.6, Nahom leads §6.1 and §6.9,
> Bemnet leads §6.7 and §6.8, Yohannes leads §6.10.
>
> **This chapter is completed during FYP II weeks 23–29, from the actual test results and the
> actual evaluation outputs.** No number in this chapter may be written from memory, from an
> expectation, or from an AI tool. Every figure is copied from a file in `results/`, and every
> table has a pointer to the script that produced it.
>
> **Guideline §10.5:** *"Every specific objective must have a corresponding implementation or
> research output and an evaluation method. The final report must state whether each objective
> was achieved, partially achieved, or not achieved, and must cite the evidence."*

---

## 6.1 Testing strategy and levels

The test plan was written during the design phase, as Guideline §10.2 requires, and is
recorded in `docs/requirements/test-plan.md`. Seven levels were applied, with the exclusions
justified: unit, integration, system, acceptance, performance, usability and scoped security
testing. Soak testing, endurance testing and formal verification were excluded, with reasons
recorded in the plan.

**Table 6.1** — The test coverage achieved.

| Area | Test IDs | Planned | Executed | Passed | Failed | Blocked |
|---|---|---|---|---|---|---|
| Data pipeline | T-01…T-06 | 6 | | | | |
| Model | T-07…T-16 | 10 | | | | |
| Mobile client | T-17…T-40 | 24 | | | | |
| API | T-51…T-60 | 10 | | | | |
| Web client | T-61…T-64 | 4 | | | | |
| Accessibility | T-65 | 1 | | | | |
| **Total** | | **55** | | | | |

The full register, with the actual results, the evidence file and the defect identifier for
every case, is Appendix F.

---

## 6.2 Evaluation on the internal test split

### 6.2.1 The baselines

**Table 6.2** — The internal test-split comparison. Every model was trained and evaluated
under identical conditions: the same split, the same preprocessing, the same seeds, the same
evaluation script. Results are the mean ± the standard deviation over three seeds.

| Model | Accuracy | Macro-F1 | Cercospora F1 | Rust F1 | Healthy F1 | Miner F1 | Phoma F1 |
|---|---|---|---|---|---|---|---|
| Majority-class predictor | | | | | | | |
| MobileNetV2 | | | | | | | |
| EfficientNet-Lite0 | | | | | | | |
| MobileNetV3-Small (proposed) | | | | | | | |
| ConvNeXt-S (published baseline, run on our split) | | | | | | |
| EfficientNet-B2 (published baseline, run on our split) | | | | | | |

*Script: `training/evaluate_internal.py`. Output: `results/E-02_internal.csv`.*

### 6.2.2 Discussion

*To be completed.* The discussion must address:
- the size of the gap over the majority-class baseline, and what that says about the class
  imbalance;
- whether the published external models, run on the group's split, outperform or underperform
  the group's model, and if they outperform it, why that does not change the project's
  contribution (the deployed artefact's size and latency, the offline operation, the guidance,
  the history, and the external evaluation);
- whether the three-seed variance is large enough to change any conclusion, and the answer
  must reference the significance test in §6.6.

---

## 6.3 The generalisation gap on external field photographs

This is the central result of the project.

**Table 6.3** — The external evaluation. Every model is evaluated on five external field
datasets that share no source with the training corpus, using the identical model, the
identical preprocessing and the identical inference code. The macro-F1 is reported per
dataset, together with the drop from the internal test split.

| Model | Internal macro-F1 | Uganda | RoCoLE | Saposoa Peru | CoffeeLeaf-CO | Silva 2020 | Mean external | **Gap** |
|---|---|---|---|---|---|---|---|---|
| MobileNetV3-Small | | | | | | | | |
| EfficientNet-Lite0 | | | | | | | | |
| MobileNetV2 | | | | | | | | |
| ConvNeXt-S (published) | | | | | | | | |
| EfficientNet-B2 (published) | | | | | | | | |

*Script: `training/evaluate_external.py`. Output: `results/E-03_external.csv`.*

### 6.3.1 Per-class external performance

**Table 6.4** — The per-class recall of the proposed model on each external dataset. This
table is the one that matters most, because it shows *which* diseases survive the shift.

| Dataset | Cercospora | Rust | Healthy | Miner | Phoma |
|---|---|---|---|---|---|
| Uganda 2025 | n/a | | | n/a | |
| RoCoLE | n/a | | | n/a | n/a |
| Saposoa Peru | n/a | | | n/a | n/a |
| CoffeeLeaf-CO | n/a | | | | n/a |
| Silva 2020 | n/a | | | | n/a |

**Note the "n/a" cells.** No public field corpus contains Cercospora, and Phoma appears in
only one. The absence of a number is itself a finding and is reported as a limitation, not
hidden. This table can be compared directly with the published EfficientNet-B2 card, whose
external rust acceptance was 16 of 847 images (1.9 %) [14], and whose ConvNeXt counterpart
recorded a Cercospora recall of 9.1 % [27].

### 6.3.2 Figure 6.1 — the internal-to-external gap per dataset

> **Figure 6.1** — The macro-F1 of each model on the internal test split and on each external
> dataset. The vertical drop is the generalisation gap. Produced by
> `training/plot_gap.py` from `results/E-03_external.csv`. Original work by the group.

### 6.3.3 Discussion

*To be completed.* The discussion must:
- state the size of the gap and compare it with the published evidence — the 67.7-point
  collapse from PlantVillage to PlantDoc [15] and the 1.9 % external rust acceptance of the
  published EfficientNet-B2 [14];
- explain the gap by mechanism rather than by restating the number, using the field
  failure modes of Barbedo [16]: background clutter, uncontrolled illumination, the
  co-occurrence of symptoms, and the dominance of the leaf in frame;
- identify which class survives the shift and which does not, and why;
- report the bootstrap confidence intervals, so that a reader can see whether the gap is
  larger than the sampling noise.

---

## 6.4 The mitigation: an ablation study

**Table 6.5** — The ablation. Each variant was trained with three seeds and evaluated on the
external sets. The deployed-size column records the cost of the intervention, which matters
because the model must fit inside a 10 MB budget.

| Variant | Training data | Augmentation | Deployed size (MB) | Internal macro-F1 | Mean external macro-F1 | Δ vs baseline | Δ size (MB) |
|---|---|---|---|---|---|---|---|
| A — baseline | JMuBEN + JMuBEN2 | standard | | | | — | — |
| B — + African field data | A + Uganda | standard | | | | | |
| C — + field-realistic augmentation | A | + JPEG, grayscale, low-light | | | | | |
| D — A + B + C | A + Uganda | + JPEG, grayscale, low-light | | | | | |
| E — D + calibration and abstention | A + Uganda | + JPEG, grayscale, low-light | | | | | |

*Script: `training/ablate.py`. Output: `results/E-04_ablation.csv`.*

**Figure 6.2** — the external macro-F1 against the deployed model size for each variant — the
Pareto frontier of the accuracy/size trade-off.

**Discussion.** *To be completed.* This section answers RQ2 and tests H2. It must state which
intervention was most effective per megabyte, whether H2 is supported, and — importantly —
whether the improvement was consistent across the five external datasets or driven by one.
An improvement driven by a single dataset is not a general improvement and must be described
as such.

---

## 6.5 Calibration and abstention

**Table 6.6** — The calibration results. The temperature was fitted on the validation
partition and then applied unchanged to the external sets.

| Dataset | ECE before | ECE after | NLL before | NLL after | T | Relative ECE reduction |
|---|---|---|---|---|---|---|
| Internal test | | | | | | |
| Uganda | | | | | | |
| RoCoLE | | | | | | |
| Saposoa Peru | | | | | | |
| CoffeeLeaf-CO | | | | | | |
| Silva 2020 | | | | | | |

*Script: `training/calibrate.py`. Output: `results/E-05_calibration.md`.*

**Figure 6.3** — the acceptance-coverage and selective-risk curves. At each threshold, the
figure shows the fraction of predictions accepted (coverage) against the fraction of accepted
predictions that are correct (selective risk). The operating point chosen for the shipped
system is marked.

**Table 6.7** — The chosen operating point.

| Threshold | Coverage | Accuracy among accepted | Accepted diagnoses | Correct | Wrong |
|---|---|---|---|---|---|
| 0.50 | | | | | |
| 0.60 | | | | | |
| 0.70 | | | | | |
| 0.80 | | | | | |
| **Shipped threshold** | | | | | |

*Script: `training/selective_risk.py`. Output: `results/E-06_coverage.csv`.*

**Discussion.** *To be completed.* This section answers RQ3 and tests H3. It must report the
selected threshold with its coverage and its accepted accuracy side by side — the coverage is
reported explicitly because a high accepted accuracy achieved by accepting only a handful of
predictions is not a useful system, and hiding the coverage would be the same error the
published literature makes. It must also connect the result to the prior art: both published
model cards advise asking for a better photo below roughly 45 % confidence [14], [27], and
the group reports whether its own threshold agrees with that guidance.

---

## 6.6 Statistical significance

**Table 6.8** — The McNemar test for the decisive model comparison. The test is applied to
the paired predictions of two models on the same test images.

| Comparison | Dataset | Discordant pairs (b, c) | χ² | p | Conclusion at α = 0.05 |
|---|---|---|---|---|---|
| Proposed vs the best internal baseline | Internal test | | | | |
| Proposed vs the best internal baseline | Uganda | | | | |
| Proposed vs the best internal baseline | RoCoLE | | | | |
| Variant D vs variant A | Mean external | | | | |

*Script: `training/significance.py`. Output: `results/E-07_significance.md`.*

**Guideline §9.4** requires a significance test whenever one method is claimed to be better
than another. Where the test is not significant, the report must say so plainly and must not
use the phrase "better".

---

## 6.7 Performance on the device

**Table 6.9** — The on-device performance on three reference devices. The low-cost device is
the one against which NFR-01 is measured.

| Device | Android version | RAM | SoC | Median (ms) | p95 (ms) | Peak RSS (MB) | Model size (MB) |
|---|---|---|---|---|---|---|---|
| Low-cost reference | | | | | | | |
| Mid-range | | | | | | | |
| High-end | | | | | | | |

**Table 6.10** — The accuracy/size/latency trade-off across the quantisations.

| Artefact | Size (MB) | Median (ms), low-cost device | Internal macro-F1 | Mean external macro-F1 |
|---|---|---|---|---|
| float32 | | | | |
| float16 | | | | |
| int8 | | | | |

*Scripts: `mobile/bench/`, `scripts/bench_device.sh`. Outputs: `results/E-08_latency.csv`,
`results/E-11_size.csv`.*

**Discussion.** *To be completed.* This section answers RQ4. It must report whether NFR-01 and
NFR-02 are met, and if not, it must state the trade-off honestly and record the requirement
change in the change-control table rather than quietly adjusting the claim.

---

## 6.8 Offline operation

**Table 6.11** — The airplane-mode verification. Every core feature was exercised with the
device in airplane mode, and a packet capture was taken across the full flow.

| Feature | Requirement | Offline result | Packet capture | Evidence |
|---|---|---|---|---|
| Camera capture | FR-01 | | | |
| Gallery upload | FR-02 | | | |
| Inference | FR-06…FR-08 | | | |
| Result and confidence | FR-09, FR-10 | | | |
| Knowledge-base guidance | FR-11 | | | |
| Diagnosis history | FR-14…FR-17 | | | |
| CSV export | FR-19 | | | |

*Test T-24 and T-25. Evidence: `evidence/T-24-*`, `evidence/T-25-*`.*

**Discussion.** *To be completed.* The requirement is the **zero outbound requests** result,
not merely that the features worked. A feature that worked while a background request was
still being made in the background would not satisfy NFR-08.

---

## 6.9 Usability evaluation

**Table 6.12** — The usability study results. Twelve participants completed five defined
tasks.

| Measure | Value |
|---|---|
| Participants | 12 (target ≥ 10) |
| Task success — capture → diagnosis → read the diagnosis | |
| Task success — read the guidance and state the first action | |
| Task success — find a dated record | |
| Task success — export the history | |
| Median time on the core flow (s) | |
| **SUS score (mean)** | |
| SUS score (range) | |
| Participants who would recommend the application | |

*Protocol: `docs/requirements/test-plan.md` §8. Results: `results/E-18_sus.csv`.*

**Justification of the sample size (Guideline §10.4 requires this).** *To be completed —
state how many participants were used and why that number is adequate.*

**The comprehension check.** Of the participants who opened the guidance, *n* correctly stated
the recommended first action. This is the objective check on RQ5, and it is more informative
than the SUS score alone: a high SUS with a low comprehension score would mean the interface
is liked but the guidance is not understood.

**Discussion.** *To be completed.* The discussion must report what the participants actually
struggled with, and what the group changed as a result. §10.4 is satisfied by reporting the
measures; it is exceeded by reporting the qualitative findings and the changes made.

---

## 6.10 Defects and limitations

### 6.10.1 The defect register

**Table 6.13** — The defect summary. The full register is in Appendix F §F.8.

| Severity | Opened | Fixed and re-tested | Open at submission | Impact if unresolved |
|---|---|---|---|---|
| Critical | | | | |
| High | | | | |
| Medium | | | | |
| Low | | | | |

**Known unresolved defects.** *To be completed.* Guideline §10.3 requires the known
unresolved defects to be discussed with their impact. "None" is an acceptable answer, but only
if it is true.

### 6.10.2 The objective-to-evidence matrix

**Table 6.14** — The traceability summary required by Guideline §10.5 and Appendix E. The full
matrix, with the design artefacts and the individual test identifiers, is in
`docs/requirements/traceability-matrix.md`.

| Objective | Requirements | Design artefacts | Implementation | Tests / evaluation | Result | **Achievement** |
|---|---|---|---|---|---|---|
| SO1 | DR-01…DR-08 | Figures 4.1, 4.3; the datasheet | `scripts/prepare_data.py`; the manifest | T-01…T-06; E-01 | | |
| SO2 | FR-06, FR-07 | §4.3, §5.3 | `training/` | T-07…T-10; E-02 | | |
| SO3 | FR-05, FR-07, FR-09, FR-10 | §4.3.3, §4.4 | `training/evaluate_external.py`, `calibrate.py`, `ablate.py` | T-11…T-16; E-03…E-07 | | |
| SO4 | FR-01…FR-12, FR-21, FR-31 | Figures 4.1, 4.2 | `mobile/`; `model/` | T-17…T-26; E-08…E-11 | | |
| SO5 | FR-11…FR-13, FR-25, FR-32, FR-35…FR-37 | §4.3.5 | `data/knowledge_base.json` | T-27…T-32; E-12…E-14 | | |
| SO6 | FR-14…FR-20, FR-22…FR-24, FR-33 | Figure 4.3; §4.4 | `mobile/lib/data/`; `api/app/models.py` | T-33…T-40; E-15…E-17 | | |
| SO7 | All | §4.1, §4.3 | `tests/`; `evidence/` | T-01…T-66; E-18, E-19 | | |

**Achievement values: achieved · partially achieved · not achieved. Each claim must be
supported by identifiable evidence.** *To be completed for each objective, with the reason
stated.*

### 6.10.3 The limitations of the evaluation

**Table 6.15** — The limitations of the evaluation itself. These are separate from the
limitations of the *system* listed in Table 1.3, and both are reported.

| # | Limitation |
|---|---|
| E1 | No public field corpus contains Cercospora, so the field performance of that class is unmeasured |
| E2 | The training corpus contains no Ethiopian field imagery, so the reported field performance is measured on other countries' conditions |
| E3 | RoCoLE is Robusta while the deployment target is Arabica, so the RoCoLE figures measure a harder shift than the deployment target |
| E4 | Saposoa Peru was collected under a uniform protocol with blurred and occluded images excluded, so it is not fully representative of field capture |
| E5 | The labels in six of the eight sources carry no annotator-agreement statistic, and the strongest source uses a single expert; the ground truth itself carries unquantified uncertainty |
| E6 | The external evaluation is not blinded — the datasets were inspected during the development of the method, so the figures are stress tests rather than a fully blinded field trial |
| E7 | The evaluation was performed by the group that built the system, with no independent replication |
| E8 | The usability study used 12 participants drawn from a university and local community; the results may not generalise to the full spectrum of smallholder farmers in the target regions |

---

*Results to be inserted: Tables 6.1–6.15, Figures 6.1–6.3. Each is produced by a script in
`training/` or `scripts/` and stored in `results/`. Nothing in this chapter is written from
memory.*
