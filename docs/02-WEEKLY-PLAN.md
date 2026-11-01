# The 16-Week Plan — FYP I

**What this file is.** The one plan the group agrees on. Sixteen weeks, one row per week, **one task per
person per week**, and for every task the *thing you can show* when it is finished. If a task has no
output, it is not a task.

**Why 16 weeks.** The weekly progress log is submitted weekly, so the plan must be weekly. FYP I runs
W1–W16; the defense is W14, and W15–W16 are corrections and final submission. (The 32-week view —
including all of FYP II — is in `01-ROADMAP.md`. This file is only FYP I.)

**Week 1 begins Monday 19 October 2026.** Today is Sunday 1 November 2026, so **W1 and W2 are already
behind us and must be backfilled this week** — see §7.

| | |
|---|---|
| Group | Yohannes Berhanu (UGR/9440/16) · Hayredin Mohammed (UGR/2361/16) · Bemnet Tesfaye (UGR/3266/16) · Nahom Solomon (UGR/3155/16) |
| Title | Design and Development of a Coffee Leaf Disease Diagnosis System Using Deep Learning |
| Complexity | **High** (4 members, real datasets, measured research question) — Guideline §2.4 |
| FYP I defense | **W14, 18–24 January 2027** |

**The four roles, used as column headings below.**

| Code | Person | Owns |
|---|---|---|
| **H** | Hayredin | Data & model — datasets, splits, training, quantisation, evaluation |
| **B** | Bemnet | Mobile app — capture, on-device inference, result screen, history |
| **Y** | Yohannes | Backend & platform — API, database, CI, security, repository, document assembly |
| **N** | Nahom | Research & quality — literature, requirements, test plan, KB content, ethics, report |

---

## 1. The flow — what depends on what

Read this once. It is the whole project in eight boxes, and it explains why the weeks are in this order.

```
   ┌──────────────┐
   │ 1. DATASETS  │  H: JMuBEN + JMuBEN2 counted, licensed, documented
   └──────┬───────┘
          │  (W1–W2)
   ┌──────▼───────┐
   │ 2. PROPOSAL  │  all: problem, gap, objectives, method, schedule
   └──────┬───────┘  GATE W4 — nothing starts before it is approved
          │
   ┌──────▼───────┐
   │ 3. EVIDENCE  │  N: literature read → the gap is real and specific
   └──────┬───────┘  (W5)
   ┌──────▼───────┐
   │ 4. REQS      │  all: FR / NFR / DR, use cases, test plan
   └──────┬───────┘  GATE W7 — frozen, then changes need a change request
          │
   ┌──────▼───────┐
   │ 5. SPLIT     │  H: leakage-safe split (group first, then split)
   └──────┬───────┘  everything downstream is invalid without this
          │
   ┌──────▼───────┐
   │ 6. MODEL     │  H: train → evaluate → quantise → int8 artifact
   └──────┬───────┘
          │
   ┌──────▼───────┐
   │ 7. SYSTEM    │  B + Y: phone app ← artifact → API, KB, history
   └──────┬───────┘  W11: vertical slice works with airplane mode ON
          │
   ┌──────▼───────┐
   │ 8. EVIDENCE  │  H + N: external evaluation, calibration, the honest gap
   └──────────────┘  W13 GATE — then W14 defense
```

**Two rules that follow from the flow.**

1. **The split (5) blocks everything.** A model trained on a leaky split produces numbers that cannot be
   defended, and re-doing it in January is not possible. It is finished and tested in W7.
2. **The vertical slice (7) is the demo.** A beautiful design chapter with no working phone is a weak
   defense. W11 is the week the phone diagnoses a leaf with the radio off.

---

## 2. All sixteen weeks on one page

| W | Dates | Phase | The one thing that must be true on Sunday night |
|---|---|---|---|
| 1 | Oct 19–25 | Orientation | Repo exists, datasets counted, first commit from every member *(backfill)* |
| 2 | Oct 26–Nov 1 | Orientation | Datasheet, ethics screen and 9-screen map done *(backfill)* |
| 3 | Nov 2–8 | Proposal | All 14 proposal sections exist, even if thin |
| 4 | Nov 9–15 | **GATE** | **Proposal submitted for approval — Sun 15 Nov** |
| 5 | Nov 16–22 | Literature | 15 sources read with page numbers; the gap statement is written |
| 6 | Nov 23–29 | Requirements | FR / NFR / DR drafted, no orphan requirement |
| 7 | Nov 30–Dec 6 | **GATE** | **Requirements baseline signed — Fri 4 Dec**; split script tested |
| 8 | Dec 7–13 | Design | Training pipeline runs end to end; one real accuracy number exists |
| 9 | Dec 14–20 | Design | Model v1 + measured phone latency; the ★ features are specified |
| 10 | Dec 21–27 | Design | **The generalisation gap is measured and written** |
| 11 | Dec 28–Jan 3 | Design | **The phone diagnoses a leaf offline** — vertical slice |
| 12 | Jan 4–10 | Design | Three ★ features working; KB content final in EN + Amharic |
| 13 | Jan 11–17 | **GATE** | **Design review — Wed 13 Jan**; Chapters 1–4 assembled |
| 14 | Jan 18–24 | **DEFENSE** | Slides submitted 48 h ahead; two timed dry runs done |
| 15 | Jan 25–31 | Corrections | Every panel condition closed, with a named owner |
| 16 | Feb 1–7 | Submission | Submission package assembled and receipted |

**Five hard gates, and nothing else is a gate:** W4 proposal · W7 baseline · W13 design review ·
W14 defense · W16 submission. If a week slips, it slips *inside* a phase — the gate does not move.

---

## 3. Who does what, every single week

These run alongside the weekly tasks, and they are what you write in the report on a quiet week.

| Code | Standing duty | Where it is recorded |
|---|---|---|
| **H** | Keep `data/` honest: every count and licence claim traceable to a fetch | `data/dataset-sources.md` |
| **B** | The app must build and run on the real phone, every week — never "will fix later" | screenshot or 20 s clip |
| **Y** | CI green; no secret, dataset or model binary committed; one commit per person per week | repo + Actions tab |
| **N** | Logbook compiled and sent Friday; AI-use log kept current | `Appendix-L` + logbook |

**Every Friday, each person sends N four lines.** N compiles and sends the logbook to the advisor.
That is the whole reporting system — no separate system to maintain.

---

## 4. Week by week

Each week has: a goal, four tasks, and the gate test. `★` marks a task that is part of our
differentiation (§5) — the reason this is not the same project as everyone else's.

### W1 · 19–25 Oct · Orientation *(backfill)*

**Goal:** the inputs exist and every member has committed something.

| Code | Task | The thing you can show |
|---|---|---|
| **H** | Download JMuBEN (`t2r6rszp5c`) and JMuBEN2 (`tgv3zb82nd`); count images per class | `data/dataset-sources.md` with per-class counts |
| **B** | Create the Flutter project; run it on a **physical phone** | Photo of the app running on the device |
| **Y** | Create the GitHub repo, folder tree, `.gitignore` for data/models/secrets | Repo URL the advisor can open |
| **N** | Extract obligations from Guideline §1–§7; score 4 candidate titles | Title record with the rejection reasons |

**Gate test:** `git log --author` shows a commit from all four.

### W2 · 26 Oct – 1 Nov · Scope and ethics *(backfill)*

**Goal:** we know exactly what data we have and what we are allowed to do with it.

| Code | Task | The thing you can show |
|---|---|---|
| **H** | Datasheet: composition, licences, the 5 external test sets, limitations | `data/datasheet.md` |
| **B** | Nine-screen inventory + navigation map; camera plugin spike | Wireframes v0 + a captured photo in-app |
| **Y** | CI (lint + test), security NFRs, branch protection | Green CI run |
| **N** | Ethics screening (App. M) + AI-use log (App. L); first 3 comparison-table rows | Completed Appendix M |

**Gate test:** the advisor has seen the outline and the dataset counts.

### W3 · 2–8 Nov · Proposal draft

**Goal:** every section of the proposal exists. Thin is allowed; missing is not.

| Code | Task | The thing you can show |
|---|---|---|
| **H** | Proposal §2 gap + novelty, written from `06-DIFFERENTIATION.md`, with numbers from prior work (e.g. 1.9 % external rust recall) | 2 pages, every number cited |
| **B** | §10 condensed requirements + the proposed-system UI figure | One figure at 300 dpi |
| **Y** | §9 method (design science) + §14 schedule + the High-complexity argument (§2.4) | 4 pages |
| **N** | §1 problem, §5 questions, §6 scope, §8 literature | 6 pages |

**Gate test:** the 14 sections are all present in one file.

### W4 · 9–15 Nov · **GATE: proposal approval**

| Code | Task | The thing you can show |
|---|---|---|
| **H** | Dataset registry final, with checksums and a reproducibility plan | `data/dataset-sources.md` frozen |
| **B** | Architecture / container figure | 300 dpi figure referenced in the text |
| **Y** | Format to §11 (TNR 12, 1.5 spacing, margins), approval block, searchable PDF | Submission PDF |
| **N** | ≥15 verified references in IEEE order; zero uncited claims; proofread | Reference registry |

**Gate test:** **submitted Sunday 15 November.** A late proposal moves every later week and the defense
date does not move with it.

### W5 · 16–22 Nov · Literature, read properly

**Goal:** the gap statement is defensible, not asserted.

| Code | Task | The thing you can show |
|---|---|---|
| **H** | 5 efficiency/edge papers → model comparison (params, size, accuracy) | Filled comparison columns |
| **B** | 5 on-device inference papers → the latency/size budget we must hit | NFR targets with sources |
| **Y** | 3 offline/system/KB-versioning works → our security and versioning constraints | Design constraints list |
| **N** | Synthesis themes 1–3 (argue, do not summarise) + gap statement v1 | Gap statement, 1 paragraph, checkable |

**Gate test:** 15 sources read and logged with page numbers — not abstracts.

### W6 · 23–29 Nov · Requirements

| Code | Task | The thing you can show |
|---|---|---|
| **H** | DR-01…DR-08, with the split invariants written as testable statements | Data requirements table |
| **B** | FR for capture, result, history, KB — each with an acceptance criterion | FR register, app side |
| **Y** | FR for the service + NFR for performance/security; reference device decided | NFR table with numbers |
| **N** | Use cases UC-01…UC-08; consolidate the FR/NFR register | Use case document |

**Gate test:** no requirement without an actor, a condition and a test.

### W7 · 30 Nov – 6 Dec · **GATE: requirements baseline**

| Code | Task | The thing you can show |
|---|---|---|
| **H** | Implement and **test** the leakage-safe splitter; publish the manifest hash | `scripts/prepare_data.py` + `AUDIT PASSED` log |
| **B** | App-side test cases with preconditions and expected results | Test-case register |
| **Y** | Traceability matrix rows + the baseline sign-off pack | Signed baseline |
| **N** | Full test plan; run the baseline meeting; write the minutes | Minutes + signature |

**Gate test:** **signed Friday 4 December.** After this, a new requirement is a change request.

### W8 · 7–13 Dec · Design + first training run

| Code | Task | The thing you can show |
|---|---|---|
| **H** | Training pipeline end to end on a 20 % subset | **One real accuracy number** |
| **B** | All nine screens specified, including empty / loading / error states | Screen spec |
| **Y** | ERD + SQLite DDL + the API contract (OpenAPI) | Schema file + OpenAPI JSON |
| **N** | Chapter 2 final; Chapter 4 §4.1–4.2 | Chapters with figures referenced |

**Gate test:** a number exists that was produced by our own code.

### W9 · 14–20 Dec · Model v1 and the ★ specification

| Code | Task | The thing you can show |
|---|---|---|
| **H** | Model v1 on the full internal split; confusion matrix, per-class recall | Confusion matrix + per-class table |
| **B** | TFLite inference spike on the phone; measured ms per image | Latency measurement on the real device |
| **Y** | API skeleton: `/health`, `/predict` stub, model checksum pin | Running service + curl output |
| **N** | ★ The five unique features written as requirements **with pass conditions** | ★ spec table (§5) |

**Gate test:** accuracy *and* on-device latency both measured.

### W10 · 21–27 Dec · External evaluation — the key result

| Code | Task | The thing you can show |
|---|---|---|
| **H** | Evaluate v1 on Uganda, ROCoLE, Saposoa → **the generalisation gap** | Per-dataset table + the gap |
| **B** | ★ Capture coach: blur, exposure, leaf-coverage measured pre-shutter | Warning fires correctly on 10 bad photos |
| **Y** | Model artifact contract + a CI job that checks size and checksum | CI model check |
| **N** | Error analysis + threats to validity | 2 pages, with examples |

**Gate test:** the gap is a number, and it is written down even if it is bad. **A bad number is a result;
a missing number is a failure.**

### W11 · 28 Dec – 3 Jan · Quantise, and make the phone work

| Code | Task | The thing you can show |
|---|---|---|
| **H** | int8 TFLite export; size / latency / accuracy-delta table | Artifact + the three-way table |
| **B** | **Camera → prediction → guidance → history, offline, on the phone** | 30 s clip, airplane mode ON |
| **Y** | KB JSON schema, version field, checksum, served by the API | Validated KB asset |
| **N** | Chapter 3 final | Chapter 3 |

**Gate test:** **the vertical slice runs with the radio off.** This is the demo; everything after it is
polish and evidence.

### W12 · 4–10 Jan · The ★ features

| Code | Task | The thing you can show |
|---|---|---|
| **H** | ★ Conformal threshold + uncertainty attribution (TTA disagreement) | Shipped threshold file + coverage table |
| **B** | ★ Result screen: prediction set, "why unsure", look-alike cases | Three screens |
| **Y** | ★ Correction packet (signed, anonymised) + local scorecard | Round-trip test |
| **N** | ★ KB content final in English + Amharic; citation audit; reviewer sign-off | Signed content review |

**Gate test:** at least three ★ features work; the rest have a pass condition and a fallback.

### W13 · 11–17 Jan · **GATE: design review**

| Code | Task | The thing you can show |
|---|---|---|
| **H** | Evaluation design frozen: sets, metrics, baselines, statistical tests | Evaluation protocol |
| **B** | All wireframes exported at 300 dpi + figure list | Figure folder |
| **Y** | Document assembled to §11; similarity check run | PDF + similarity report |
| **N** | Chapters 1–4 final; traceability complete for the FYP I columns | Complete document |

**Gate test:** **design review Wednesday 13 January**; the document is defensible as it stands.

### W14 · 18–24 Jan · **FYP I DEFENSE**

| Code | Task | The thing you can show |
|---|---|---|
| **All** | Two timed dry runs (Mon, Wed); each member answers 3 questions outside their own area | Rehearsal notes |
| **Y** | Slides + document submitted **48 h ahead**; receipt kept | Submission receipt |
| **B** | Live demo rehearsed on the actual phone, battery charged, backup video recorded | Backup clip |
| **N** | Logbook, contribution statements and declarations complete and signed | Signed Appendix G |

**Gate test:** the defense is delivered. Note: **Timket (19–20 Jan) may move the date** — confirm with
the Coordinator in W5, not in January.

### W15 · 25–31 Jan · Corrections

| Code | Task | The thing you can show |
|---|---|---|
| **H** | Re-run any experiment the panel questioned; update the tables | Updated results |
| **B** | Fix the UI findings; re-export the affected figures | Updated figures |
| **Y** | Apply the corrections; archive the evidence pack | Corrected document |
| **N** | Revise the chapters; update the traceability matrix | Updated chapters |

**Gate test:** every panel condition has an owner and is closed or explicitly deferred in writing.

### W16 · 1–7 Feb · Final submission

| Code | Task | The thing you can show |
|---|---|---|
| **H** | Freeze the model card and the results tables | `data/model-card.md` |
| **B** | Freeze the APK and the demo script | Tagged release |
| **Y** | Assemble the submission package; keep the receipt | Receipt |
| **N** | Final proofread, reference pass, contribution statements signed | Final PDF |

**Gate test:** submitted, receipted, and the repository is tagged.

---

## 5. The ★ features — what makes this not a copy

The instructor's requirement is a project that adds value and could become a product. Five features do
that. Each is small, offline, and has a **measurable pass condition**, so none of them can be hand-waved
at the defense. The full comparison against the similar public projects — and the features we
deliberately rejected — is `06-DIFFERENTIATION.md`; the proposal's novelty section is written from it
before **W4**.

| # | Feature | In one line | Passes when | Fallback |
|---|---|---|---|---|
| **★1** | Prediction sets (conformal) | Instead of "rust, 91 %", the app says *"rust"* or *"rust **or** Cercospora — check the underside"* — with a statistical guarantee | Measured coverage ≥ target on a held-out external set, with the average set size reported | Show top-3 probabilities |
| **★2** | "Why am I unsure?" | Separates *bad photo* from *genuinely ambiguous leaf*, so the advice is "retake" vs "look closer" | ≥ 80 % correct attribution on 30 degraded vs 30 ambiguous images | Single abstain message |
| **★3** | Look-alike confirmed cases | Five confirmed field photos of the same disease, retrieved offline from a ~300 KB index — visual proof, not a percentage | Top-5 are class-consistent ≥ 70 % of the time; < 50 ms on device | Static per-class exemplars |
| **★4** | Field-truth flywheel | Farmer confirms or corrects a diagnosis; the app keeps a **local scorecard** ("on your farm: 17/20 correct") and can export a signed, anonymised packet | Packet round-trips and verifies; no image leaves the phone without an explicit action | Local scorecard only |
| **★5** | Colour-constancy normalisation | Studio-trained models break on field light; normalise white balance before inference | External macro-F1 improves on ≥ 2 of 3 datasets — **or** it is reported as a negative result | Report the ablation as a finding |

**Why these and not a chatbot, a web dashboard or severity scoring:** a chatbot needs a network and
invents advice; a dashboard is a second application; a severity percentage needs a validated scale we do
not have. Each is rejected with a stated reason, so the panel sees judgement rather than gaps.

**The product story, in one sentence:** everyone else ships a classifier; we ship an instrument that
knows when it does not know, shows a farmer *why*, and turns field use into the data a cooperative would
pay for.

---

## 6. What you write in the weekly report

Five lines, every Friday, to Nahom. This is the same content as the logbook columns, so nothing is
written twice.

```
W<n> · <dates> · <name>
PLANNED : <copied from this plan>
DONE    : <what is actually finished> — <link or file path>
NOT DONE: <what slipped, and why, in one honest sentence>
NEXT    : <the next task from this plan>
```

**Two rules.**

1. **If it has no link, it did not happen.** A claim without a commit, a file, a figure or a measurement
   is not evidence, and the panel asks for evidence.
2. **Write it in the week.** A logbook reconstructed in January is visible in the file dates and it is
   the easiest mark in the project to lose (Guideline §13.2).

---

## 7. Backfill: W1–W2, this week

Both weeks are already past. Do not rewrite history — do the work and say when it was done.

| Do this | Who | By |
|---|---|---|
| Count the datasets and fill `data/dataset-sources.md` | H | Wed 4 Nov |
| Flutter app running on a phone; screenshot | B | Wed 4 Nov |
| Repo, folder tree, CI green, one commit each | Y | Tue 3 Nov |
| Appendix M + Appendix L + title record | N | Wed 4 Nov |
| Write the W1 and W2 logbook rows, marked *"completed retrospectively on <date>"* | All | Fri 6 Nov |

Then W3 starts on time. **W3 does not wait for W1–W2 to be perfect.**

---

## 8. When it goes wrong

| Symptom | The first sign | What we do |
|---|---|---|
| Model pipeline slips | No accuracy number by end of W8 | Cut external sets from 5 to 3. The model matters more than evaluation breadth. |
| App slips | No real prediction on the phone by end of W11 | Drop the ★3 retrieval and the web client. The phone demo is what the panel sees. |
| A member is behind | Two weeks with no commit and an empty report | Raise it that week with the advisor. Contribution is a scored factor (§14.4, §17.7); a quiet workaround is worse than a documented conversation. |
| External accuracy is poor | W10 shows a large drop | **This is the expected result.** It is the contribution. Report it, and let ★1/★2 do the work. |
| The proposal is returned | The advisor asks something the page cannot answer | `00-STATUS.md` §2.1 and §2.6 already contain the argument. |

**Never cut, at any point:** the five-class taxonomy with abstention · the leakage-safe split · the
external evaluation · the test evidence · the traceability chain · the AI-use declaration · the live
demo.

**Cut in this order if forced:** ★3 retrieval → ★5 normalisation → ★4 flywheel → ★2 attribution →
★1 prediction sets. (★1 and ★2 are the two that change how the work is judged, so they go last.)
