# Chapter 7 — Conclusion and Recommendations

> **Owner:** Nahom Solomon, with each member contributing their own package's conclusions.
> **Written during FYP II week 25**, and revised in weeks 28–29 after the advisor's draft
> review.
>
> **Guideline §5.2:** *"drawing conclusions must not be written as a specific objective,
> because every project ends with conclusions whether or not they are stated as an objective."*
> This chapter is the conclusion, not an objective.

---

## 7.1 Summary against the objectives

**Table 7.1** — The summary against each specific objective, with the achievement status and
the evidence. Guideline §10.5 requires the status and the evidence to be stated explicitly.

| ID | Objective | Status | The evidence |
|---|---|---|---|
| SO1 | A leakage-safe, multi-source, documented corpus | | The datasheet; the split manifest; the audit results (§6.2, Table 6.3) |
| SO2 | Lightweight models compared against baselines under identical conditions | | Table 6.2; the significance test in Table 6.8 |
| SO3 | The generalisation gap quantified and mitigated | | Tables 6.3–6.7; Figures 6.1–6.3 |
| SO4 | Offline on-device inference within the size and latency budget | | Tables 6.9, 6.10; Table 6.11 |
| SO5 | Per-class confidence and a sourced knowledge base | | Table 5.6; the citation audit; the expert review |
| SO6 | A persistent, searchable, exportable diagnosis history | | Tests T-33…T-40 |
| SO7 | The complete system tested and evaluated against every objective | | Appendix F; Tables 6.1, 6.12–6.15 |

*A status of "partially achieved" is an acceptable and honest answer, and it must carry a
reason. Guideline §10.5 requires the reason, not a better-sounding status.*

### 7.1.1 What the project achieved

*To be completed — three to five sentences, written after the numbers are in. It should
answer: what works, what does not, and what the reader should take away.*

---

## 7.2 Contributions

### 7.2.1 To the coffee leaf disease literature

**A leakage-safe, source-diverse corpus with a published split protocol.** The group
demonstrated that the three principal datasets in this literature contain duplication
structures — JMuBEN's published images are cropped and rotation/flip-augmented derivatives of
an unpublished original set; BRACOL's symptom images are crops of its whole-leaf photographs;
RoCoLE provides four views of each of 390 plants — and that a random split therefore leaks.
The group's grouped split, the four automated leakage invariants and the committed manifest
make the protocol reproducible.

**A quantified external evaluation.** The project measured the curated-to-field shift for a
coffee leaf classifier across five independently sourced field datasets with per-class recall,
calibration error and abstention — a methodology established in the wider plant-disease
literature [15] but not applied to coffee. The comparison against the published model cards,
whose external rust acceptance was 16 of 847 images (1.9 %) [14] and whose Cercospora recall
was 9.1 % [27], places the group's results in the context of the field's own evidence rather
than in isolation.

**A design response to a documented failure mode.** The acceptance threshold, the calibration
and the photo-quality gate are not features added for completeness; they are the engineering
consequence of the finding that the dominant failure mode of plant-disease classifiers in the
field is a *confidently wrong* prediction, with mean confidence remaining at 79.76 % while
accuracy collapsed by 67.7 points [15].

### 7.2.2 To the deployment literature

**An offline five-class system.** No published system provides a five-class coffee leaf
disease classifier that runs fully offline on a low-cost mobile device. The two published
mobile applications cover two diseases and require connectivity to reach a server-hosted model
[11], [12]; the five-class web applications run on cloud-hosted Streamlit or Gradio
infrastructure [13]; the two offline model artefacts cover seven and eight classes
respectively [33], [34]. This project closes that gap within a 10 MB model budget, together
with the agronomic guidance and the diagnosis history that the applied literature lacks.

**A reusable offline-first pattern for agricultural decision support.** The architecture — a
quantised on-device model, an embedded versioned knowledge base, a local database, and an
optional API for aggregation — is deliberately generic, and the group intends it to be
reusable for other crops and other extension services.

### 7.2.3 To the community

**A sourced, reviewed agronomic knowledge base.** The knowledge base is built from the FAO
Arabica manual [61], the peer-reviewed Ethiopian rust management literature [56], [57] and
the APS disease taxonomy [62], with every practice carrying a citation, a CI check that
enforces the citation, and a review by a plant pathologist at the Jimma Agricultural Research
Center. It is deliverable beyond this project.

**An honest performance profile for the deployment context.** By reporting per-class external
recall, the calibration error and the coverage curve rather than a single accuracy figure,
the project gives extension services a usable basis for deciding what the tool is good for.

---

## 7.3 Limitations

The limitations of the *system* are listed in Table 1.3 and of the *evaluation* in Table 6.15.
Those that bear most directly on how the results should be read are restated here.

1. **The field performance is modest, and that is the honest result.** The external macro-F1
   is materially lower than the internal test-split accuracy. The system is designed to be
   used in that condition rather than in spite of it: it abstains when it is not confident,
   it names the reasons, and it directs the user to an extension officer.
2. **No Ethiopian training data.** The target population is Ethiopian, and the corpus contains
   none. The single most valuable future contribution is Ethiopian field imagery.
3. **Two of the five classes are essentially untested in the field.** No public field corpus
   contains Cercospora, and Phoma appears in only one. The field performance for those
   classes is unknown rather than good.
4. **The labels themselves carry unquantified uncertainty.** Six of the eight sources report
   no annotator agreement, and the strongest uses a single expert.
5. **The evaluation was not blinded and was not independently replicated.** The datasets were
   inspected during the development of the method, so the external figures are stress tests
   rather than a fully blinded field trial.
6. **The guidance is advisory.** It summarises published recommendations and names
   active-ingredient classes rather than products or dosages. It does not replace a qualified
   extension officer, and the application says so.
7. **The Amharic user interface is infrastructure only.** The localisation framework is in
   place, but the Amharic strings await a qualified translator, so the shipped interface is
   English-only.

---

## 7.4 Recommendations for future work

**Table 7.2** — The recommendations, prioritised by the value delivered against the effort
required.

| # | Recommendation | Rationale | Priority | Effort |
|---|---|---|---|---|
| 1 | **Collect Ethiopian field imagery** through a partnership with JARC and the regional extension services, with an agreed labelling protocol and, ideally, multiple annotators with a reported agreement statistic | The single highest-value missing input. It addresses the largest limitation directly and would make the model's deployment context its training context | Very high | High — a field campaign |
| 2 | **Extend the model to the out-of-taxonomy classes** — red spider mite, coffee weevil and *Mycena citricolor* — as named classes rather than as a single `unsupported` bucket | The system currently refuses to name what it sees outside the taxonomy, which is safe but unhelpful to a farmer who can see a clear weevil infestation | High | Medium |
| 3 | **Replace the heuristic photo-quality gate with a trained quality classifier**, validated on the field sets | The gate was built from documented failure modes without being trained; a learned gate would be more accurate and would report a graded score rather than a pass/fail | Medium | Medium |
| 4 | **Add severity estimation**, building on the BRACOL severity bands and on the prior art's severity methodology | The prior art reports only 38.9 % accuracy at a 50 % IoU threshold [25], so the target should be set carefully and the segmentation-based BRACOL bands used as the reference | Medium | High |
| 5 | **Add automatic history synchronisation** for extension officers, with an explicit conflict rule | The current export is manual. An officer covering a district needs the records to aggregate automatically | Medium | Medium |
| 6 | **Replace the manual camera capture with a guided, single-shot capture flow** with live framing feedback | The usability study should identify whether capture quality is the dominant user difficulty; if it is, guided capture is the highest-value change | Medium | Low–medium |
| 7 | **Complete the Amharic interface** with a qualified translator and test it with Amharic-speaking users | The localisation infrastructure exists; the content and its validation do not | Medium | Low |
| 8 | **Add a detection mode** for localising the affected area of the leaf, with the classification as a second stage | A bounding box for the symptom is more actionable to a farmer than a whole-leaf class | Low | High |
| 9 | **Investigate the domain-adaptation alternatives that were excluded**, now that the baseline shift is measured | DANN-style adaptation degraded accuracy to 0.252 in the comparable study [15], but that was tested on a different dataset; with a measured baseline, the alternatives can be re-tested fairly | Low | Medium |
| 10 | **Release the corpus protocol and the model as a reusable package** for other Ethiopian agricultural AI projects | The split protocol, the leakage audit and the model card are the reusable artefacts | Low | Low |

---

## 7.5 Final remarks

The project set out to build a complete, offline, farmer-facing coffee leaf disease
diagnosis system, and to measure honestly how well such a system works on real field
photographs. Both aims were pursued together, because a system that is built without being
measured is of unknown value, and a measurement that is not built into a system is of no
practical use.

The group found that the published accuracy figures in this field, while high, do not survive
the transition to field imagery; that the most useful engineering response is not a larger
model but a system that knows when it does not know; and that the honest performance profile
of a coffee leaf disease classifier is a more useful contribution to the community than a
flattering one.

---

*To be completed: §7.1.1, and the specific numbers referenced in §7.2.1 and §7.3.*
