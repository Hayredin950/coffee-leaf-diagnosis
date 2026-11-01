# Appendix D — Defense Checklist
# Appendix N — Examiner Assessment Sheet (self-audit)

> **Guideline Appendix D** is the list the examiners use to confirm what each student has shown.
> **FYP I:** the examiners assess the items on the basis of the FYP I document and the
> presentation. **FYP II:** the items marked *(FYP II only)* also apply to the live
> demonstration.
>
> **Why this file exists.** The group uses Appendix D as a **self-audit**: every item is
> rehearsed by the member who owns it before the defense, and a failing item is a gap to close
> in the remaining weeks. Appendix N is reproduced here so the group knows exactly what the
> examiner is scoring, and can prepare evidence for each row rather than hoping.

---

# Appendix D — Defense Checklist (group self-audit)

**Legend:** ✅ ready · 🟡 rehearsed, needs polish · ⬜ not yet ready · ➖ not applicable in FYP I

| # | Appendix D item | FYP I | FYP II | Owner | Evidence to show | Status |
|---|---|---|---|---|---|---|
| 1 | The student can state the problem and justify its significance | ✔ | ✔ | Nahom | The problem statement; the Ethiopian rust incidence figure (35.3 % incidence, 9.09 % severity); the stakeholder list | |
| 2 | The student can explain every specific objective and its evidence | ✔ | ✔ | Nahom | SO1–SO7 with their measurable targets; the traceability matrix | |
| 3 | The student can explain the methodology and justify the major choices | ✔ | ✔ | Nahom + Hayredin | The iterative-prototype method; why transfer learning over training from scratch; why a grouped split; why temperature scaling and not DANN | |
| 4 | The student can explain the system architecture and design | ✔ | ✔ | Yohannes | Figure 4.1–4.8; the design-decision record | |
| 5 | The student can demonstrate the major implemented functionality | ➖ | ✔ | Yohannes | The live demo: capture → diagnosis → guidance → history → export | |
| 6 | The student can explain the database, data or model design | ✔ | ✔ | Hayredin + Yohannes | The split strategy; the schema; the artefact contract; the model card | |
| 7 | The student can explain the testing and the failures encountered | ➖ | ✔ | All | The defect register; the representative failure cases; the honest account of what failed | |
| 8 | The student can interpret the evaluation results | ➖ | ✔ | Hayredin | The external results; the calibration; the abstention curve; what the numbers mean for a farmer | |
| 9 | The student can state limitations honestly | ✔ | ✔ | All | The Chapter 6 limitations: the external accuracy, the absent Ethiopian training data, the two untestable classes, the advisory-only guidance | |
| 10 | The student can explain their individual contribution | ✔ | ✔ | Each member | Their own Appendix G page; their own module; the commits under their name | |
| 11 | The student can map the implementation to the requirements and design | ➖ | ✔ | Yohannes | The Appendix E traceability matrix; the §5 design-consistency checklist | |
| 12 | The student can explain any use of AI tools and the checks made on AI-assisted work | ✔ | ✔ | Each member | Their own Appendix L entries; the specific checks they ran | |
| 13 | The student can discuss the ethical and security considerations | ✔ | ✔ | Nahom + Yohannes | Appendix M; the abstention rationale; the OWASP controls; the no-personal-data design | |
| 14 | The student can answer technical questions without relying on the report | ✔ | ✔ | All | The weekly troubleshooting drill (see `docs/05-DECISION-LOG.md`) | |
| 15 | The student can identify future improvements | ✔ | ✔ | All | The Chapter 7 future-work list, specific and prioritised | |

**Rehearsal protocol.** Three rehearsals in FYP II weeks 28–29. In rehearsal 1, each member
answers two questions from another member's area. In rehearsal 2, the group runs the demo
without notes. In rehearsal 3, the group runs the demo **with the network deliberately
disabled** to prove the offline claim, and answers the Appendix D items in a random order so
that no member relies on a fixed sequence.

---

# Appendix N — Examiner Assessment Sheet (group's understanding of the marking)

> The examiner scores each criterion by choosing a band — Excellent (90–100 % of the weight),
> Good (70–89 %), Adequate (50–69 %), Weak (30–49 %), Poor (0–29 %) — and then awarding a mark
> inside that band in proportion to the criterion weight. **Every mark must rest on identifiable
> evidence**, and the examiner records the justification for each criterion.

## N.1 The rubric, with the group's evidence mapped to each row

| Criterion | FYP I | FYP II | The group's evidence for this row | Who can answer it |
|---|---|---|---|---|
| Problem definition and significance | 15 | 10 | The problem statement; the stakeholder analysis; the Ethiopian epidemiological evidence; the deployment and generalisation evidence | Nahom |
| Literature review and related work | 15 | 10 | Chapter 2, organised into five themes with an explicit gap statement; the comparison table with three-plus systems; the "how the review shaped the design" table | Nahom (+ Hayredin for §2.2) |
| Objectives and requirements | 20 | 10 | SO1–SO7 with measurable targets; RQ1–RQ5 with hypotheses; 37 FRs, 35 NFRs and 8 DRs with IDs, priorities and acceptance criteria; the traceability matrix | Nahom |
| Methodology | 15 | 10 | The iterative-prototype method justified per objective; the baseline justification; the experimental protocol with seeds and versions; the risk register | Nahom + Hayredin |
| Analysis and design | 25 | 15 | Figures 4.1–4.14; the design-decision record with the alternatives rejected and why; the schema and the API contract; the consistency checklist | Bemnet + Yohannes |
| Technical implementation | 0 | 20 | The working app, the API, the web client, the model artefact, the training pipeline; the repository history; the reproducibility package | Yohannes + Bemnet + Hayredin |
| Testing and evaluation | 0 | 10 | 55 test cases with actual results and evidence; the defect register; the performance measurements; the usability study | All |
| Results, analysis and discussion | 0 | 5 | The external evaluation, the calibration, the ablation, the significance test, the error analysis; each objective with an achievement status | Hayredin |
| Documentation and report quality | 5 | 5 | The formatted report; the datasheet; the model card; the installation and user guides; the licence list | Nahom |
| Presentation, demonstration and defense | 5 | 5 | The ≤22-slide deck; the live demo; the individual contributions | All |

## N.2 What each band looks like for this project

| Criterion | Excellent (90–100 %) | Good (70–89 %) | Adequate (50–69 %) | Weak (30–49 %) |
|---|---|---|---|---|
| Problem definition | Precise, evidence-backed, with the Ethiopian stakeholders named and the deployment and generalisation gaps both quantified | Clear and relevant with some evidence and a stated gap | Understandable but the evidence is thin | Vague, with little evidence |
| Literature review | Comprehensive, thematic, critically synthesised, with a clearly justified gap | Relevant, organised, some critical comparison | Mostly descriptive — sources summarised one by one | Few sources, or a gap that is not supported |
| Objectives and requirements | Measurable, aligned with the problem, complete, and traceable to design and tests | Clear and mostly measurable, with minor traceability gaps | Some objectives or requirements are vague or unmeasurable | Inconsistent or incomplete |
| Methodology | Justified against alternatives and rigorously applied to every objective | Appropriate and reasonably justified | Identified but weakly justified | Poorly suited to the objectives |
| Analysis and design | Technically correct, complete, consistent across the models, traceable to requirements | Sound with minor inconsistencies | Gaps or inconsistencies, but the main design is usable | Incomplete or contradictory |
| Technical implementation | Robust, fully functional, maintainable and secure; the challenge is clearly met; reproducible from the submission | Functional and well structured, with minor weaknesses | Functional but with noticeable limitations in scope, quality or security | Partial, or major parts not working |
| Testing and evaluation | Systematic, covers all requirements, the levels are justified, evidence-rich | Covers most requirements with adequate evidence | Basic tests with limited evidence | Few tests, no link to requirements |
| Results and discussion | Accurate and critical; every objective linked to evidence with an achievement status; limitations and error analysis included | Accurate, linked to most objectives, some critical discussion | Results reported but the discussion is descriptive | Incomplete, unclear, or loosely linked |
| Documentation | Complete, well organised, in the required structure and format, correct IEEE citations | Complete and clear with minor errors | Mostly complete with noticeable gaps or format errors | Incomplete or poorly organised |
| Presentation and demo | Clear, well timed, confident, technically accurate answers, and a demo mapped to the requirements | Clear and accurate with minor weaknesses | Understandable with some unclear answers or a limited demo | Unclear delivery, poor timing, or answers showing limited understanding |

## N.3 The Individual Contribution Factor (Guideline §17.7)

| ICF | Evidence required | How this group earns it |
|---|---|---|
| **1.00** | Explains the whole system **and** their own modules in depth; answers troubleshooting questions without the report; the records show an equal or larger share of the work | The cross-review rotation; the weekly troubleshooting drill; the logbook; the commit history; the Appendix G page |
| **0.90** | Explains the system and their own modules well, with minor gaps | |
| **0.80** | Explains their own modules but the understanding of other parts is limited | **The most likely failure mode for this group.** The rotation exists to prevent it. |
| **0.70** | Explains their own modules only partly, or the records show a clearly smaller share | |
| **0.60** | Struggles to explain their own modules; the contribution is minimal | |
| **Below 0.60** | Cannot explain substantial submitted work → referred to the Committee under §18.1 | |

**The four questions each member must be able to answer without notes.** Each member picks one
question from another member's area at every rehearsal:

| Member | Own area | Must be able to answer about another member's area |
|---|---|---|
| **Hayredin** | Data, splits, training, quantisation, evaluation | How the app renders the guidance and where the threshold comes from; how the API validates an upload and why it rejects by magic bytes |
| **Yohannes** | The Flutter client, on-device inference, the history store | How the split prevents leakage and what "grouped" means; how the model was quantised and what changed |
| **Bemnet** | The API, the database, deployment, CI, security | How the external evaluation was set up and what the generalisation gap turned out to be; how the knowledge base was sourced and reviewed |
| **Nahom** | The literature, the requirements, the KB, the test plan, the report | How the model is trained and exported; how the offline operation was verified with a packet capture |

## N.4 The questions the panel is most likely to ask

Prepared answers for all four members. **These are practice questions, not scripts** — the
answers must be reasoned live.

1. *"Your model reports 94 % accuracy on your test set. Your external field set reports
   41 %. Why?"* → Because the training and internal test data share a source, a capture
   protocol, a resolution and an augmentation history, whereas the external sets differ in
   country, camera, background, lighting and image-processing pipeline. The internal figure
   measures the ability to separate classes of images from the same distribution; the external
   figure measures the ability to diagnose a leaf a farmer photographed. The first is what the
   literature reports; the second is what matters to the user. §2.5 of Chapter 2 cites the
   published evidence for the same effect.
2. *"How do you know your test set is not leaking into training?"* → Three checks: exact
   SHA-256 duplicates (T-03), perceptual-hash clusters (T-04), and source-group identity such
   as the BRACOL leaf and its crops and the RoCoLe plant ID (T-05). The split is performed on
   the grouped data **before** any learned preprocessing, and the manifest is committed with a
   checksum.
3. *"Why not use a bigger model?"* → A ConvNeXt-S coffee model is 99 MB and reports a 9.1 %
   recall on Cercospora; an EfficientNet-B2 is 8.57 MB but accepts only 1.9 % of external rust
   images correctly. The gap in this field is not model capacity; it is that no one has
   measured the shift and engineered for it. A larger model inside a 10 MB budget does not
   exist, and the phone target rules out the large ones anyway.
4. *"What happens if the model is wrong?"* → It can be wrong, and the design says so. The
   temperature scaling and the acceptance threshold mean the system abstains when it is not
   confident; the result screen shows an explicit "not confident enough" state instead of a
   label; the guidance is advisory and points to an extension officer; the report gives the
   measured external per-class recall, including the classes where it performs badly.
5. *"Why offline? Why not just use an API?"* → Because the published mobile applications
   require connectivity to reach a server-hosted model, and the target user — a smallholder in
   a remote kebelle — often has no signal. It also removes the per-inference cost and the data
   cost on a metered connection.
6. *"What would you do with more time?"* → Add Ethiopian field data, which is the single
   highest-value missing input; replace the heuristic quality gate with a trained quality
   classifier; add severity estimation; add the `unsupported` classes to the shipped model so
   the system can name what it does not know; and add automatic history synchronisation for
   extension officers.
7. *"How do you know the treatment guidance is correct?"* → Every field carries a citation to
   a peer-reviewed or institutional source — the FAO Arabica manual, the Ethiopian rust
   management literature from Jimma, and the APS taxonomy. The content was reviewed by a plant
   pathologist at EIAR's Jimma Agricultural Research Center before it shipped. The CI job
   `audit_kb.py` fails the build if any practice lacks a citation.
8. *"What is your contribution, beyond training a classifier?"* → The leakage-safe,
   multi-source corpus and its published split; the external field-photo evaluation protocol
   with calibration, abstention and significance testing, which no coffee study has applied;
   the offline five-class deployment with guidance and history, which no prior system
   provides; and the honest measurement of what remains unsolved.

## N.5 Self-assessment (to be completed in week 29 and used to target the final rehearsal)

| Criterion | FYP II weight | Our honest self-score | The evidence we would show | The gap we must close |
|---|---|---|---|---|
| Problem definition and significance | 10 | | | |
| Literature review and related work | 10 | | | |
| Objectives and requirements | 10 | | | |
| Methodology | 10 | | | |
| Analysis and design | 15 | | | |
| Technical implementation | 20 | | | |
| Testing and evaluation | 10 | | | |
| Results, analysis and discussion | 5 | | | |
| Documentation and report quality | 5 | | | |
| Presentation, demonstration and defense | 5 | | | |
| **Total** | **100** | | | |

**Be honest in this table.** The purpose is to find the two weakest rows in week 29 and fix
them in week 30, not to write a number that flatters the group.
