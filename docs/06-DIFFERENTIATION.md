# Differentiation — What This Project Adds That the Public Ones Do Not

**Why this file exists.** The instructor's instruction was: *"there are a bunch of similar projects out
there — you have to provide new features and functionality that adds value and is reasonably useful and
makes you stand out, maybe promoted to a startup."*

**The reference point is the public work, not another group.** The "bunch of similar projects" are the
public GitHub and Hugging Face repositories with the same idea (§2). That is what we are measured
against, and that is what this file compares us to.

**Correction to an earlier draft of this file.** An earlier version treated the repository
`jov1523/coffee_leaf_disease_diagnosis` as somebody else's work and framed the overlap as an integrity
risk. That was wrong. That repository is **ours**: it was created and pushed by **Yohannes Berhanu
(`byohannes767@gmail.com`)**, and it carries our four names and IDs. There is no second group and no
similarity problem between the two. The real problem is different and smaller — **we currently have two
copies of one project, and they disagree.** §8 fixes that.

---

## 1. What the two copies are

| | **The repo** (`jov1523/coffee_leaf_disease_diagnosis`) | **This workspace** |
|---|---|---|
| Author | Yohannes Berhanu | Hayredin Mohammed (with the group) |
| Commits | 1 | not yet a repo |
| Content | 43 files, 39 Markdown (~8,370 lines) | 40+ Markdown, plus a **tested** `scripts/prepare_data.py` |
| Plan | 14 weeks, sprints, 57 stories, points | **16 weeks**, one task per person per week |
| Requirements | **FR-01…FR-40, NFR-01…NFR-40, DR-01…DR-10** | requirements plan, not yet a register |
| Tests | **T-01…T-60 designed** | test plan |
| ADRs | **ADR-01…ADR-09** | decision log |
| Traceability | **matrix built**, verdicts deliberately empty | chain described, not tabulated |
| Logbook | **W1–W14 rows drafted** | empty |
| Novelty | 9 differentiators (FT-D01…D09) | **5 ★ features** (★1…★5) |
| Code | none | `prepare_data.py`, end-to-end tested, `AUDIT PASSED` |

**The two are complementary, not competing.** The repo is stronger on *documentation discipline*; this
workspace is stronger on *the plan, the novelty and anything that executes*. Neither alone is the
submission. §8 is the merge plan.

---

## 2. The actual competition: the public projects

Verified 21 Oct 2026 via the GitHub API and Hugging Face model cards:

| System | Classes | Form | Offline? | What it does not do |
|---|---|---|---|---|
| Coffee Recognize (Lucs1590) | Rust + Miner | Ionic mobile app | **No** — needs `Coffee_Recognize_API` | No offline path at all |
| Manso et al. 2019 (arXiv:1904.00742) | Rust + Miner | Mobile app | Not stated | Two classes; no guidance layer |
| Hitimana et al. 2024 (MDPI) | 4 + GPS | Mobile app | Not stated | No abstention; no external evaluation |
| Brewguard / `FTsune/kape` | Rust, Cercospora, Algal, Sooty | Streamlit web | **No** | Cloud-only; no field protocol |
| Omdena (`dimitramuni`) | all 5 | Gradio / Streamlit | **No** | Cloud-only |
| `sleepypioneer` | Rust vs other | Streamlit + AWS Lambda | **No** | Binary task |
| `ixrbhii/coffee-disease-convnext` | 7 | HF model, 99 MB | Yes | 99 MB will not load on a low-end phone |
| `ConnorLee08/coffee-leaf-efficientnet-b2` | 8 | HF model + 8.57 MB TFLite | Yes, but | **1.9 % external rust recall** — accepted 16 of 847 rust images |

**The gap in the public work, stated once:**

> Every public system is a classifier. None states what its answer is worth. The offline ones are large
> or demonstrably collapse out-of-distribution (1.9 % rust recall is not an edge case, it is the
> published state of the art on external data). The accurate ones need a network. None separates *a bad
> photograph* from *an ambiguous leaf*. None shows confirmed field cases beside a prediction. None
> measures its own accuracy in the field, and none keeps a record of being corrected.

That is the gap. It is not "nobody has classified coffee leaves" — that is solved. It is **nobody has
made a coffee-leaf classifier that is honest about its own uncertainty, and nobody has built the loop
that turns field use into field data.**

---

## 3. What the repo already gets right — credit where it is due

The nine differentiators already specified in `docs/03-requirements/features.md` are genuinely good, and
they already put us ahead of every public project in §2:

| # | Feature | Why it beats the public work |
|---|---|---|
| FT-D01 | Grad-CAM saliency overlay | No public coffee project exposes its reasoning |
| FT-D02 | Differential diagnosis: top-3 + the discriminating symptom | Public systems return one label |
| FT-D03 | Live capture coach: blur / exposure / coverage | Nobody else gates the input |
| FT-D04 | Plot timeline + recurrence flag | History exists elsewhere; recurrence does not |
| FT-D05 | Shareable referral card | Offline output that travels |
| FT-D06 | Signed offline KB bundle import | No public project versions its guidance at all |
| FT-D07 | One-command reproducible evaluation | Almost no student repo can regenerate its numbers |
| FT-D08 | Amharic-first, speaker-reviewed wording | No public project is localised for Ethiopia |
| FT-D09 | Calibrated confidence strip | Calibration is essentially absent from student work |

**Keep all nine.** They are cheap, they are defensible, and they are already written.

**But they do not answer the instructor.** All nine accept the answer and decorate it: a better
explanation, a better comparison, a better screen, a better export. A panel that has seen two similar
projects will read nine presentation features as polish, not as a contribution.

---

## 4. The line that actually separates us

| | The nine (presentation) | The five ★ (epistemic and operational) |
|---|---|---|
| Question answered | *"How do I show this result better?"* | *"What is this result actually worth, and what happens when it is wrong?"* |
| Unit of output | A label, a confidence, an explanation | A **set** with a coverage guarantee, an **attribution** of the uncertainty, a **record** of being corrected |
| Failure mode handled | A confusing screen | A confident wrong answer, and a model that never learns it was wrong |
| Over time | Nothing — each diagnosis is independent | A per-farm accuracy scorecard and an exportable field-truth packet |

**The one-sentence claim, and it is defensible:**

> Public projects ship a classifier that reports a probability. We ship an instrument that states what
> it does not know, shows the farmer **why** it does not know, proves the answer against confirmed field
> cases, and turns the farmer's correction into the first Ethiopian coffee-leaf field dataset — without
> an image leaving the phone unless the farmer says so.

Every clause maps to a numbered feature in §5 with a pass condition. No public project in §2 can make
that claim.

---

## 5. The five ★ features, with the pass condition that makes them real

A feature without a number is a slide. Each row is what the panel is allowed to ask for in W13.

### ★1 — Conformal prediction sets

**What it is.** Instead of "rust, 91 %", the app returns a *set*: `{rust}` when it is confident, or
`{rust, Cercospora}` when it is not — with a stated guarantee that the true class is in the set at least
`1 − α` of the time, on data the threshold never saw.

**Why it beats FT-D02 and FT-D09.** D02 shows the top-3 *when the runner-up is within 25 points* — an
arbitrary rule with no guarantee, calling a class "less likely" when it may be the truth. D09 reports
historical accuracy by bin, which is descriptive. Conformal prediction is **prescriptive**: it produces
a set with a coverage property, and the set's size is itself the honest answer.

**Pass condition.** On a held-out external set, empirical coverage ≥ `1 − α` within its binomial
confidence interval, with mean set size reported per dataset. Both numbers, or it did not happen.

**Fallback.** Top-3 probabilities with an explicit "not calibrated" caveat.

**Cost.** ~1 day: split conformal on the validation partition, one threshold per α, shipped as a tiny
JSON beside the model. The hard part is writing it honestly.

---

### ★2 — "Why am I unsure?" — attributing the uncertainty

**What it is.** When the system abstains, it says **which** of two very different things happened:

- *the photograph is bad* — blur, glare, low light, leaf too small → **advice: retake**
- *the leaf is genuinely ambiguous* — stable across test-time augmentations and still split between two
  classes → **advice: look at the underside / send to an extension officer**

**Why it beats FT-D03.** The capture coach runs **before** the shutter and measures the frame. Ours runs
**after** inference and asks a different question: is this uncertainty the camera's fault or the leaf's?
Those lead to opposite actions. A coach alone will accept a sharp photograph of an ambiguous leaf and
then abstain with no explanation — the exact state the UI design already admits is confusing.

**How it is computed.** Two offline signals: (a) the coach's quality measures, reused post-hoc; (b)
disagreement across test-time augmentations (flip + two brightness variants). Agreement ⇒ clean input,
ambiguous leaf. Scatter ⇒ unstable input.

**Pass condition.** ≥ 80 % correct attribution on 30 deliberately degraded and 30 genuinely ambiguous
images (two annotators; disagreements recorded).

**Fallback.** A single abstain message, as the repo already has.

**Cost.** ~1.5 days, because it reuses the coach's maths.

---

### ★3 — Offline look-alike retrieval of confirmed cases

**What it is.** Five confirmed field photographs of the predicted disease, retrieved on-device from a
~300 KB embedding index: *"these were confirmed as rust."* Visual proof, not a percentage.

**Why it beats FT-D01.** Grad-CAM shows where the model looked, and the repo's own risk note admits the
honest failure — on a studio-background corpus the heat map may point at the backdrop. Retrieval shows
what the model *matched against*, which the farmer can falsify in one second. "That is not my leaf" is a
legitimate response that a heat map cannot receive.

**Pass condition.** Top-5 class-consistent in ≥ 70 % of queries; < 50 ms per query on the reference
device; index ≤ 300 KB.

**Fallback.** Five static per-class exemplars (the repo's own D01 fallback) — say why we prefer that as
the primary, not the afterthought.

**Cost.** ~2 days, and it depends on confirmed field images — which ★4 produces.

---

### ★4 — Field-truth flywheel and the local scorecard

**What it is.** Every diagnosis can be confirmed or corrected in one tap. The app keeps a **local**
scorecard — *"on your farm: 17 of 20 confirmed correct"* — and can export a **signed, anonymised**
packet (class, predicted set, confirmation, quality signals, model version; **no image** unless the
farmer explicitly attaches one).

**Why it beats every public project.** They are stateless with respect to truth. They produce a
diagnosis, store it, and never learn whether it was right. Ours measures its own accuracy on the only
population that matters and produces the artefact no Ethiopian corpus contains: confirmed field labels.

**Pass condition.** Packet round-trips and verifies (signature + schema); no image leaves the device
without an explicit action; the scorecard arithmetic is correct on a scripted 20-record scenario.

**Fallback.** Local scorecard only, no export.

**Cost.** ~2 days. The signature can be a checksum chain rather than real PKI — state that plainly.

**Ethics.** The only feature touching human participants. Covered by Appendix M Q1/Q2: the confirmation
is a tap, no personal data, no image, and consent is the act of pressing export. Say this before the
panel asks.

---

### ★5 — Colour-constancy normalisation

**What it is.** Deterministic white-balance / illuminant correction before inference, so a model trained
on Kenyan plantation photographs under one light does not collapse on a Peruvian afternoon under another.

**Why it beats the public work.** None of them handle illumination at inference time. The repo's
augmentation includes brightness and contrast jitter, which is training-time and does nothing for a
deployment image. Colour-temperature shift is a documented field failure mode, and this is the cheapest
of the five to implement and the easiest to ablate honestly.

**Pass condition.** External macro-F1 improves on ≥ 2 of 3 external datasets, **or** the ablation is
reported as a negative result with the numbers. Both are publishable; only silence is not.

**Fallback.** Report the ablation as a finding (the same work).

**Cost.** ~1 day: grey-world or Shades-of-Grey on the input tensor, one ablation run.

---

## 6. What we reject, with the reason on the record

The repo's X01–X11 list is right, and we keep it. Our additions:

| Rejected | Why it is tempting | Why it is out |
|---|---|---|
| **FT-D06** signed KB bundle import | A demonstrable integrity story | Supply-chain engineering for an app with no update channel: no server push, no accounts, no second publisher. A version field plus a CI checksum gives 80 % of the value for 5 % of the cost. |
| Cloud sync / accounts (X01) | Convenient | Contradicts the offline premise; drags in authentication, hosting and a privacy statement we cannot support. |
| Product names and doses (X02) | Instant practicality | Makes the app the source of an illegal or harmful recommendation. Active-ingredient classes only. |
| Severity percentage (X03) | Sounds quantitative | Needs lesion segmentation and a validated severity scale. An unvalidated "34 % infected" is worse than nothing. |
| Multi-crop (X04) | Sounds bigger | Dilutes the corpus, the taxonomy and the KB. Coffee is the point. |
| LLM chatbot (X05) | Fashionable | Needs a network, cannot run offline, invents uncited advice — the exact failure the KB prevents. |
| Voice I/O (X06) | Helps low-literacy users | A separate accessibility workstream. Deferred with a reason. |
| On-device retraining (X07) | Sounds advanced | No labelled field data exists at the start — **★4 is how that changes**, which is why ★4 is the right version of this idea. |
| GPS and maps (X08) | Good demo | Unreliable indoors; adds a permission and a privacy question. A plot label gives the benefit without either. |
| Officer web dashboard (X09) | A second user is attractive | A second application. The API stays as the integration point. |
| Model marketplace (X10) | Elegant architecture | A two-model abstraction with one model. |
| Video capture (X11) | Would raise field accuracy | Storage, latency and thermal budget. The capture coach captures most of the benefit. |
| Blockchain on the ★4 packet | Currently fashionable | A checksum chain is sufficient, explainable in one sentence, and does not require a network. |
| Disease-spread prediction map | Looks like epidemiology | We have no epidemiological data and no way to validate one. |

---

## 7. Where the repo is ahead of this workspace — and the fix

Honest accounting, because a differentiation document that only lists wins is a sales brochure.

| The repo has | This workspace has | Fix | Owner | By |
|---|---|---|---|---|
| 90 requirement IDs with acceptance tests | a requirements plan | Write the register to the same standard, then freeze it | B (FR), H (DR), Y (NFR) | W7 |
| 60 designed test cases | a test plan | Produce T-01…T-60 in the same shape, covering ★1–★5 | N | W7 |
| 9 ADRs, each with the rejected alternative | a decision log | Write ADR-01…ADR-09; every ★ feature gets one | Y | W9 |
| A traceability matrix with empty verdicts | the chain described | Build the matrix; leave verdicts empty and say why | N | W13 |
| A populated logbook, W1–W14 | an empty logbook | Backfill W1–W2 by Fri 6 Nov, then write in-week | All | W2 backfill |
| A verified dataset registry (21 screened, 12 rejected) | the same sources, unverified in-repo | Record observed counts and checksums at first download | H | W1 backfill |
| A JARC expert-review request with lead time planned | the intent | Send the letter in W5, not W12 | N | W5 |
| — | **a tested `prepare_data.py`** | Merge it in; it is the one thing no public project has | H | W3 |
| — | **the 16-week per-person plan** | Merge it in as the single plan | Y | W3 |

**The pattern:** the repo is ahead on documentation discipline; this workspace is ahead on execution.
Close the documentation gap in W6–W7. Never close the execution gap in the other direction.

---

## 8. The merge — one project, one source of truth

This is the real problem, and it is a project-management problem, not an integrity one.

**The conflict.** The repo plans **14 weeks** across 8 sprints with 57 stories. This workspace plans
**16 weeks** with one task per person per week. Both claim the same group, title and dates. If both are
pushed to different repositories, the group has two sources of truth and the Friday report has two
possible answers — which is exactly the confusion John raised.

**The resolution.**

| Question | Answer |
|---|---|
| Which plan wins? | **The 16-week per-person plan.** It answers "what do I do this week" in one line; the sprint plan answers it in four files. |
| What happens to the sprints? | Kept as *history* in `docs/01-ROADMAP.md` (the 32-week phase view). Not deleted — demoted. |
| What happens to the 14-week numbering? | 14 weeks is FYP I **up to the defense**. 16 = 14 + corrections (W15) + submission (W16). Nothing is lost; two weeks are added. |
| Who owns the merge? | Yohannes (repo owner), with Hayredin on the plan and Nahom on the registers. |
| How is it reviewed? | A **pull request**, not a force-push. A PR keeps John's commit, shows every changed file, and lets him accept or reject each one. |

**This is why the PR is the right move.** Earlier I advised against opening one, on the false premise
that the repo belonged to someone else. It does not. A fork → branch → PR into `jov1523` is exactly how
four people should reconcile one project, and it leaves a reviewable record for the advisor.

---

## 9. How to answer "isn't this the same as everyone else's?"

The question will be asked. Three sentences, in this order:

1. **Concede the solved part.** *"Five-class coffee leaf classification is solved in-domain, and the
   public implementations — Coffee Recognize, Omdena, Brewguard, two Hugging Face models — all reach high
   accuracy on curated data. We say so rather than claiming it."*
2. **Name the gap in the literature.** *"What none of them does is state what the answer is worth. The
   published offline models collapse out-of-distribution — one accepts 1.9 % of rust images — and none
   gives a coverage guarantee, none separates a bad photograph from an ambiguous leaf, none shows
   confirmed field cases, and none measures its own accuracy in the field."*
3. **Point at the number.** *"Each of those is a requirement with a pass condition in the design-review
   pack: coverage at the stated α, 80 % attribution accuracy, 70 % top-5 class consistency, a scorecard
   that reproduces on a scripted scenario, and an ablation that either improves two datasets or is
   reported as a negative result."*

That answer is true, checkable, and does not depend on anyone else's repository.

---

## 10. Actions, owners, weeks

| # | Action | Owner | By | Evidence |
|---|---|---|---|---|
| 1 | Merge this workspace into the repo by PR; one plan, one logbook, one register set | Y + H | W3 | PR merged, `02-WEEKLY-PLAN.md` authoritative |
| 2 | Rewrite the proposal's novelty section around ★1–★5, conceding the solved part in one sentence | H + N | W3 | `proposal/Appendix-A-Proposal.md` §2 |
| 3 | Write ★1–★5 as requirements with pass conditions, in the register's own format | N | W9 | ★ table in `02-WEEKLY-PLAN.md` §5 |
| 4 | One ADR per ★ feature, each naming the alternative it beat | Y | W9 | ADR set |
| 5 | Conformal threshold + coverage table | H | W12 | Threshold file + coverage results |
| 6 | Uncertainty attribution experiment (30 + 30 images) | H + N | W12 | Attribution accuracy table |
| 7 | Exemplar index built from confirmed field images | H + B | W12 | Index ≤ 300 KB, latency measurement |
| 8 | Correction packet round-trip + scripted scorecard scenario | Y + B | W12 | Round-trip test log |
| 9 | Colour-constancy ablation on 3 external datasets | H | W10 | Ablation table (positive **or** negative) |
| 10 | Re-read this file before the defense | All | W14 | — |

**Protection order if we run out of time:** ★1 and ★2 first (they change how the work is judged), then
★5 (cheapest, and an honest negative result still counts), then ★4 (the startup story), then ★3 (nicest
demo, most dependent on data we may not have).

---

## 11. One paragraph for the advisor

> Five-class coffee leaf classification is solved in-domain, and we say so. What is not solved is what
> the answer is worth: the published offline models collapse out-of-distribution — one accepts 1.9 % of
> rust images — and no public system gives a coverage guarantee, separates a bad photograph from an
> ambiguous leaf, shows confirmed field cases, or measures its own accuracy in the field. Our
> contribution is those four things plus an illumination correction, each with a measurable pass
> condition and a stated fallback, specified in W9 and built by W12. The field-truth loop is also the
> only realistic route to the Ethiopian field data that no public corpus contains.

---

## 12. Appendix — the 43 files in the repo, and what each one is

Kept so that the reading is auditable, and so nobody re-reads 8,373 lines to find one table again. Line
counts are exact and verified against the repository.

| File | Lines | What it is | What we keep |
|---|---|---|---|
| `README.md` | 212 | Folder map, ID conventions, rules R1–R8, status | Structure |
| `docs/01-proposal/proposal.md` | 640 | The full 14-section proposal | Content |
| `docs/02-literature/comparison-table.md` | 91 | 5 comparable systems, 4 rows closed | Row structure |
| `docs/02-literature/reading-plan.md` | 133 | 7 themes, reader + second reader per theme | Second-reader rule |
| `docs/02-literature/references.md` | 96 | 21 entries, 9 verified, 6 leads, 3 excluded with reasons | The exclusion table |
| `docs/03-requirements/features.md` | 484 | FT-A01–A12, FT-D01–D09, FT-X01–X11 | The nine and the X-list |
| `docs/03-requirements/functional-requirements.md` | 108 | FR-01…FR-40 | Register |
| `docs/03-requirements/non-functional-requirements.md` | 114 | NFR-01…NFR-40 with instruments | "The number is the requirement" |
| `docs/03-requirements/data-requirements.md` | 94 | DR-01…DR-10, the `unsupported` rule | Register |
| `docs/03-requirements/use-cases.md` | 269 | UC-01…UC-09, plain text not UML | Actor table |
| `docs/03-requirements/test-plan.md` | 139 | T-01…T-60, designed not executed | The status convention |
| `docs/03-requirements/traceability-matrix.md` | 117 | SO → FR → design → test → verdict (empty) | The empty verdict column |
| `docs/04-design/architecture.md` | 302 | Context / container / component / runtime | 4-view framing |
| `docs/04-design/data-model.md` | 220 | ERD, DDL, KB document structure | Three kinds of data |
| `docs/04-design/ml-pipeline.md` | 339 | Six-wide output, split protocol, abstention, metrics | Contract |
| `docs/04-design/ui-design.md` | 281 | 9 screens, 5 principles, states matrix | "Say I don't know loudly" |
| `docs/04-design/design-decisions.md` | 269 | ADR-01…ADR-09 with rejected alternatives | The ADR rule |
| `docs/05-report/chapter-1-introduction.md` | 298 | Problem, objectives, questions, scope | Structure |
| `docs/05-report/chapter-2-literature-review.md` | 344 | Synthesis by theme | ⟦VERIFY⟧ discipline |
| `docs/05-report/chapter-3-methodology.md` | 285 | Design science + Scrum, two frames | Separation argument |
| `docs/05-report/chapter-4-requirements-and-design.md` | 332 | Analysis of the registers, not a copy | "State it once" |
| `docs/05-report/front-matter.md` | 260 | Title page, declaration, abstract, TOC, registers | Figure register |
| `docs/06-appendices/individual-contribution-statement.md` | 109 | Appendix G drafts with effort % | Format |
| `docs/06-appendices/presentation-outline.md` | 118 | 22 slides, speakers, minutes, pre-answered Q&A | The Q&A table |
| `docs/starter/agile-method.md` | 278 | Scrum working agreement, DoD, evidence pack | DoD wording |
| `docs/starter/semester-plan.md` | 454 | Day-level plan, W1–W14 | The day view, if the group wants it |
| `docs/starter/weekly-plan.md` | 375 | Sprint plan, 57 stories, 228 points | Nothing — this is the conflict |
| `docs/starter/team-roles-and-job-distribution.md` | 144 | Roles, RACI, bus-factor rules | Owner + reader |
| `docs/starter/title-selection.md` | 101 | 4 candidates scored /50 with rejections | The scoring table |
| `docs/starter/risk-register.md` | 63 | R1–R14 with fallbacks | Register |
| `docs/starter/decision-log.md` | 64 | D-001…D-012, O-01…O-09 | Open decisions with close-by weeks |
| `docs/starter/meeting-records.md` | 93 | Standing agenda, minute template | "Bring the artefact, not a description" |
| `docs/starter/logbook.md` | 186 | Appendix B columns + W1–W14 rows | The column rules |
| `docs/starter/ai-use-disclosure.md` | 67 | Appendix L with a verification log | The verification log |
| `docs/starter/ethics-screening.md` | 52 | Appendix M, Q1 and Q10 answered Yes | Content |
| `docs/starter/submission-checklist.md` | 70 | Appendix I trimmed, format checks | The format table |
| `data/dataset-sources.md` | 257 | 8 verified + 12 rejected, licences | Content |
| `data/datasheet.md` | 298 | Full datasheet with `[OBSERVE]` fields | Content |
| `data/knowledge-base.md` | 217 | KB content plan, source hierarchy | Content |
| `sources/guideline/FYP-Guideline-AAU-CS-Oct2026.pdf` | — | The guideline | — |
| `sources/progress-log/weekly-log-template.png` | — | The logbook sheet layout | — |
| `sources/synopsis/FYP1-synopsis-revised-2026-10-12.docx` | — | The revised synopsis | — |
| `.gitignore` | 55 | Data / model / secret / build exclusions | Already correct |
