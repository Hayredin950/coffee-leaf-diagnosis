# The Plan — content for the shared Google Doc

**What this is.** The content for the Google Doc John set up (`13szmjaUUDLhQ7T8v3FWmkzZ6HulLM50uko9F0hyKyAc`),
written against **the six headings he asked for, in his order**. Paste section by section; each one is
self-contained.

**The rule this document follows, because "clean and measurable" was the actual request:** every line
carries a **number**, a **date**, or a **pass condition**. If a sentence could be written by any group
on any project, it is not in here.

**Where each section comes from** — so nobody has to trust this file:

| § | Heading John asked for | Source of truth |
|---|---|---|
| 1 | Preparing a clean and measurable plan | `docs/02-WEEKLY-PLAN.md` |
| 2 | Task division | `docs/03-ROLES.md` §3–§4 |
| 3 | Knowing what we are building | `docs/design/ui-wireframes.md`, `docs/requirements/requirements-spec.md` |
| 4 | Gathering information about coffee and existing systems | `data/dataset-sources.md`, `docs/literature/`, `docs/06-DIFFERENTIATION.md` §2 |
| 5 | Determining the features | `docs/requirements/requirements-spec.md`, `docs/06-DIFFERENTIATION.md` §3–§5 |
| 6 | What gap we fill | `docs/06-DIFFERENTIATION.md` §2, §4 |

---

## 1. Preparing a clean and measurable plan

### 1.1 The shape

**16 weeks. Five gates. One artefact per person per week.** That is the whole plan, and everything
below is detail on those three numbers.

The reason it is 16 and not 14: W14 is the defense, and W15–W16 are corrections and submission. A
14-week plan that ends at the defense has nowhere to put the panel's conditions, and every group
discovers that in January.

### 1.2 The five gates

A gate is not a milestone we hope to reach. It is a date with a test, and the test is pass or fail.

| Gate | Week | Date | The test that proves it |
|---|---|---|---|
| **Proposal approval** | W4 | **Sun 15 Nov 2026** | 14 sections present in one file; ≥ 15 verified IEEE references; zero uncited claims; formatted to §11 |
| **Requirements baseline** | W7 | **Fri 4 Dec 2026** | Every FR / NFR / DR has an ID, a test and an owner; no orphan requirement; split script tested |
| **Design review** | W13 | **Wed 13 Jan 2027** | Chapters 1–4 assembled; architecture, data model, ML pipeline and UI all at 300 dpi; traceability chain unbroken |
| **Defense** | W14 | **18–24 Jan 2027** | Slides submitted 48 h ahead; two timed dry runs done |
| **Submission** | W16 | **7 Feb 2027** | Package assembled and receipted |

If a week slips, it slips *inside* a phase. **The gate does not move**, because the defense date is
fixed by the Department and not by us.

### 1.3 What "done" means for one week

A week is done when three things exist, and not before:

1. **The artefact** at its path — a file, a figure, a running build. "Worked on the data" is not an artefact.
2. **The commit** under the person's own name (`git log --author` is how it is checked, not how it is claimed).
3. **The four lines on Friday** to Nahom: what I did · what is blocked · what I need · what is next.

The logbook row is written from those four lines. **Nothing goes into the logbook that cannot be shown
as a commit, a screenshot or a document** — that is the rule that makes the logbook evidence rather
than a story.

### 1.4 How we know we are on track — the three numbers we track

| Number | Target | Where it is read |
|---|---|---|
| Commits per member per week | ≥ 1 | `git shortlog -sn --since` |
| Weeks with an empty logbook row | 0 | the logbook itself |
| Gate tests passed on the date | 5 of 5 | the table above |

There is no separate progress system. One plan, one logbook, one repository.

### 1.5 The honest starting position

W1–W2 were not clean, and the plan says so rather than backdating:

- The repository was created on **31 Oct**, not in W1, so the W1 gate test ("a commit from all four") failed and is backfilled.
- **Bemnet and Nahom did not have GitHub accounts**, so two of the four could not commit. `nahoom-sh` was issued on 1 Nov; Bemnet's is still outstanding.
- **CI is not configured yet** — carried to W3.
- The dataset download is not complete; the counts in the datasheet will be observed counts, not published ones.

None of that threatens the W4 gate. All of it is written down so that the W13 review sees a group that
knew where it stood in W2.

---

## 2. Task division

### 2.1 Four roles, one owner each

Every deliverable has exactly one accountable person. Four people sharing a deliverable is how a
deliverable goes missing.

| | Who | Owns | Measured by |
|---|---|---|---|
| **Project lead · app & UI/UX** | **Yohannes Berhanu** (UGR/9440/16) | The Flutter app, on-device inference, local storage, the web client, repository governance | The app builds and runs on a **real phone every week** — screenshot or 20-second clip, never "will fix later" |
| **Data & ML** | **Hayredin Mohammed** (UGR/2361/16) | Datasets, leakage-safe split, model, quantisation, calibration, external evaluation | Every count and licence claim traceable to a fetch; `--audit` passes; external numbers reported per class |
| **Backend, serving & KB implementation** | **Bemnet Tesfaye** (UGR/3266/16) | FastAPI service, database schema, KB asset + versioning, deployment, CI, security review | **CI green**; no secret, dataset or model binary in the repo |
| **Research, requirements & quality** | **Nahom Solomon** (UGR/3155/16) | Literature, gap analysis, requirements, test plan, KB content, ethics, usability study, report, logbook | Logbook compiled and sent **every Friday**; every claim cited to a page |

### 2.2 The standing weekly duty

These run alongside the week's task and are what goes in the report on a quiet week.

| Code | Standing duty | Evidence |
|---|---|---|
| **H** | Keep `data/` honest — every count and licence traceable | `data/dataset-sources.md` |
| **Y** | The app must run on the real phone, every week | screenshot |
| **B** | CI green; nothing forbidden committed; one commit per person per week | Actions tab |
| **N** | Logbook compiled and sent Friday; AI-use log current | Appendix L + logbook |

### 2.3 RACI for the five gates

| Gate | Responsible | Accountable | Consulted |
|---|---|---|---|
| Proposal (W4) | All four, one section each | **N** (integration and formatting) | Advisor |
| Requirements baseline (W7) | N (spec), B (non-functional), H (data) | **N** | Advisor, JARC |
| Design review (W13) | Y (UI), H (ML), B (architecture) | **Y** | Advisor |
| Defense (W14) | N (slides), all four rehearse | **Y** | Advisor |
| Submission (W16) | B (format, PDF), N (checklist) | **Y** | — |

### 2.4 Why it is split this way

It is not a preference. It follows the **Individual Contribution Factor** (Guideline §17.7): each
member must be able to explain their own modules *and* hold a working understanding of the others. A
split that gives each person a sealed box fails that test at the defense, which is why every gate has a
different accountable person and why the weekly 4-line report is read by all four.

---

## 3. Knowing what we are building

### 3.1 One paragraph

**BunaDoctor** is an Android application that a smallholder points at a coffee leaf. Offline, in under
three seconds, on a phone with 2 GB of RAM, it returns the most likely of **five classes** with a
stated confidence, a photograph-based explanation, and **cited agronomic guidance** in Amharic — then
keeps the diagnosis in a farm history the farmer can hand to a development agent.

It is not a classifier with a screen. The classifier is one component of four: capture quality,
diagnosis, guidance, and record.

### 3.2 The five classes, and the sixth that is not a class

| # | Class | Amharic |
|---|---|---|
| 1 | Coffee Leaf Rust (*Hemileia vastatrix*) | የቡና ቅጠል ዝገት |
| 2 | Cercospora Leaf Spot (*Cercospora coffeicola*) | ሴርኮስፖራ |
| 3 | Phoma Leaf Spot (*Phoma tarda*) | ፎማ |
| 4 | Leaf Miner (*Leucoptera coffeella*) | የቅጠል ትል |
| 5 | Healthy | ጤናማ |
| — | **`unsupported`** | — |

`unsupported` is deliberate and it is not a sixth disease. It is how the system refuses a leaf that is
not one of the five — a *Mycena* lesion, red spider mite damage, a different plant — instead of forcing
it into the nearest class. Every published system forces the answer. That is the single most common
cause of a confident wrong diagnosis, and it is why this project can measure its own failures.

### 3.3 The nine screens

| # | Screen | What it does |
|---|---|---|
| S1 | Home | Choose a task; last diagnosis as a shortcut |
| S2 | Capture | Frame and take the photograph, with live guidance |
| S3 | Preview | Confirm the image is usable before inference |
| S4 | Result | The answer, the confidence, and the abstention state |
| S5 | All diseases | Browse the five entries |
| S6 | Entry detail | One class, ten fields, sources |
| S7 | History | Saved diagnoses |
| S8 | Record detail | One past diagnosis as it was |
| S9 | About | Versions, licences, advisory statement, language |

**Nine is the whole application.** A tenth screen is a change request, because the design and the use
cases are in step (UC-01…UC-09) and that is checked at the W13 review.

### 3.4 Scope: FYP I versus FYP II

| | FYP I (now – Jan 2027) | FYP II (Feb – Jun 2027) |
|---|---|---|
| Deliver | Proposal, Chapters 1–4, design review, defense | Working app, trained model, evaluation, Chapters 5–7 |
| Model | Baselines only — a number to justify the design | Trained, quantised, calibrated, externally evaluated |
| App | Wireframes + a vertical slice in W11 | Nine screens, offline, on a real device |
| Evidence | The plan, the split script, the literature | External per-class recall, calibration error, SUS score |

**The vertical slice in W11 is the commitment that matters.** By 3 January the phone must diagnose one
leaf with the radio off, even if the model is weak and the screen is ugly. A design document that has
never run is a design document nobody believes.

### 3.5 The three numbers that define the product

If we hit these, it is usable in the field. If we miss any of them, it is a demo.

| Target | Value | Why that number |
|---|---|---|
| APK size | **≤ 40 MB** | it has to be sendable over WhatsApp to a phone that is not ours |
| Inference, end to end | **≤ 3 s** on a 2 GB Android 8 device | the farmer is standing in a field, not waiting at a desk |
| Diagnosis path that works offline | **100 %** | the network is an optional upgrade, never a requirement |

### 3.6 What we are deliberately not building

| Not building | Because |
|---|---|
| Severity percentage | needs lesion segmentation and a validated scale; "34 % infected" without one is worse than nothing |
| Product names or doses | legal and ethical line; the app names active-ingredient *classes* and refers to the label |
| A general chatbot | it invents pesticide advice, needs a network, and cannot be audited |
| Multi-crop | dilutes the taxonomy, the corpus and the knowledge base |
| User accounts | the farmer is anonymous by design; an account drags in a privacy statement we cannot support |
| iOS | one platform done properly beats two half-done; the target population is Android |

Each of these is a scope decision, not an oversight, and each one is written down so that a reviewer
sees a group that chose its boundary.

---

## 4. Gathering information about coffee and existing systems

Three separate bodies of information, with three different owners and three different deadlines.

### 4.1 The agronomy — what we must know before we write advice

| Question | What we found | Source |
|---|---|---|
| How bad is the problem nationally? | Mean leaf rust incidence **35.3 %**, severity **9.09 %**, across south-western Ethiopia | Belachew *et al.* 2020, *Trop. Plant Pathol.* 45(5) |
| What drives epidemics? | **Altitude** is the dominant driver, not variety or management | same survey |
| Why does early detection matter? | By the time symptoms are visible to a farmer, the cheap intervention window has closed | Berihun & Alemu 2022; Yirga 2020 |
| What does the farmer actually do today? | Asks a neighbour; waits for the development agent; sometimes nothing | stakeholder interviews, W5 |
| What are we allowed to say about chemicals? | Active-ingredient **classes only**, no brands, no doses; refer to the registered label and the extension service | ADR-010, decision D-005 |

**Owner:** Nahom · **Deadline:** the guidance content is final in **W12** (English + Amharic), because
the KB is the part that cannot be rushed at the end.

**Still open:** a written collaboration with **JARC's Plant Pathology Department** for review of the
knowledge base and for field photographs. The contact email is sent; there is no reply yet. This is
risk **R2** and it has a fallback (published sources only, with the limitation stated).

### 4.2 The datasets — verified, not assumed

Every row below was verified by a direct fetch on **21 October 2026**, including the machine-readable
file-listing API. Nothing is from memory or from another paper's table.

| Dataset | Classes | Size | Licence | Role |
|---|---|---|---|---|
| **JMuBEN** (`t2r6rszp5c`) | Rust, Cercospora, Phoma | 22,591 | CC BY 4.0 | primary training |
| **JMuBEN2** (`tgv3zb82nd`) | Healthy, Miner | 35,964 | CC BY 4.0 | primary training |
| **BRACOL** (`yy2k5y8mxg`) | all five | 1,747 leaves + 2,147 symptom crops | CC BY 4.0 | secondary training; different country, five phones |
| **RoCoLe** (`c5yvn32dzg`) | rust, miner, healthy | robusta, Ecuador | CC BY 4.0 | secondary; a different species |
| **Five external sets** | — | — | — | **never used in training** — the evaluation only |

**Three findings that change the method, and that no published paper in this field reports:**

1. **The JMuBEN images are already augmented.** The released images are cropped, resized and
   rotation/flipped; the original uncropped photographs were never published. A random train/test split
   therefore leaks near-duplicate images and inflates accuracy. We split by **group**, not by image.
2. **The paper's two record IDs are inverted** relative to the record titles. We cite the record IDs
   explicitly so a reviewer cannot think we mislabelled the classes.
3. **BRACOL's symptom crops are crops of its 1,747 leaves.** Used naively they leak across the split.

**Owner:** Hayredin · **Deadline:** observed counts in the datasheet by **Wed 4 Nov**; registry frozen
at the W4 gate.

### 4.3 The existing systems — the real competition

Eight public implementations, reviewed 21 October 2026 through the GitHub API and Hugging Face model
cards. **This, not another campus group, is what we are measured against.**

| System | Classes | Offline | The specific failure |
|---|---|---|---|
| Coffee Recognize | rust, miner | **No** — separate API service | no offline path at all |
| Manso *et al.* 2019 | rust, miner | not stated | two classes; no guidance layer |
| Hitimana *et al.* 2024 | 4 + GPS | not stated | no abstention; no external evaluation |
| Brewguard (Streamlit) | rust, Cercospora, algal, sooty | **No** | cloud-only; no field protocol |
| Omdena | all five | **No** | cloud-only |
| *sleepypioneer* | rust vs other | **No** | a binary task, not a diagnosis |
| ConvNeXt coffee (99 MB) | 7 | yes | 99 MB will not load on a low-end phone |
| EfficientNet-B2 (8.57 MB TFLite) | 8 | yes, in principle | **1.9 % external rust recall — 16 of 847** |

**Owner:** Nahom · **Deadline:** the comparison table is complete at the **W4 gate**.

### 4.4 The reading plan

15 sources read properly by **W5**, each logged with page numbers — not abstracts. Four people, four
themes: efficiency and edge (H), on-device inference (Y), offline systems and versioning (B),
agronomic synthesis and the gap statement (N).

---

## 5. Determining the features

### 5.1 The seven layers

The system is described as seven layers, not a feature list, because each layer fails differently and
needs a different test.

| Layer | What it does | The feature that matters |
|---|---|---|
| 1. Capture | gets a usable photograph, or refuses and says why | live blur / exposure / coverage coach |
| 2. Recognition | pixels → a calibrated answer | five classes + `unsupported`, int8 TFLite |
| 3. Explanation | shows why, in a form a farmer can check | Grad-CAM + differential top-3 with the discriminating symptom |
| 4. Guidance | label → action | ten-field cited KB, Amharic-first, no brands, no doses |
| 5. Record | the farm over time | history, plot timeline, recurrence flag |
| 6. Referral | hands the problem to a human | shareable referral card that works offline |
| 7. Platform | keeps it alive after graduation | versioned KB bundle, model registry, evaluation harness |

### 5.2 The features we already have specified

Twelve core (FT-A01…A12) and nine differentiators (FT-D01…D09). The nine are genuinely good and they
already put us ahead of every system in §4.3: Grad-CAM overlay, differential diagnosis, capture coach,
plot timeline with recurrence, shareable referral card, signed offline KB bundle, one-command
reproducible evaluation, Amharic-first reviewed wording, calibrated confidence strip.

**Keep all nine.** But they do not answer the instructor's question, because all nine accept the answer
and decorate it. A panel that has seen two similar projects reads nine presentation features as
polish.

### 5.3 The five that go beyond — each with the condition that makes it real

A feature without a number is a slide. Each row below is what the panel is allowed to ask for at the
design review.

| | Feature | What it replaces | Pass condition |
|---|---|---|---|
| **★1** | **Conformal prediction sets** — a *set* `{rust}` or `{rust, Cercospora}` with a `1 − α` coverage guarantee, instead of a percentage | "rust, 91 %", a number with no defined meaning | empirical coverage ≥ `1 − α` on an external set, within its binomial CI; mean set size reported |
| **★2** | **Uncertainty attribution** — says whether the *photo* is bad or the *leaf* is genuinely ambiguous | one "low confidence" message for two opposite problems | ≥ 80 % correct attribution on 30 degraded + 30 ambiguous images, two annotators |
| **★3** | **Offline look-alike retrieval** — five confirmed field photos of the predicted class from a ~300 KB on-device index | Grad-CAM, which shows where the model looked, not what it matched | top-5 class-consistent ≥ 70 %; < 50 ms; index ≤ 300 KB |
| **★4** | **Field-truth flywheel + local scorecard** — one tap to confirm or correct; the app reports its own accuracy on that farm; a signed anonymised packet carries the correction out | nothing — no published system learns whether it was right | packet round-trips and verifies; no image leaves the device without an explicit action |
| **★5** | **Colour-constancy normalisation** before inference | an implicit assumption that the training light is the field light | the measured gain on the cross-dataset evaluation, reported whether positive or negative |

### 5.4 The features we rejected, with the reason

| Rejected | Why |
|---|---|
| Signed KB bundle with PKI | a checksum chain does the job; PKI implies a key infrastructure we do not have and cannot defend |
| Severity percentage | needs lesion segmentation and a validated scale |
| A separate officer dashboard | a second application, a second login, a second thing to test; the API is the integration point |
| On-device retraining | no labelled field data exists yet — ★4 is how that changes |
| Cloud sync as a requirement | contradicts the premise |

Writing down what we rejected is not padding. It is the difference between a scope and an accident.

### 5.5 The MVP cut line

If time runs out, we cut in this order: **★3 → ★5 → ★4 → ★2 → ★1**.

**Never cut:** the five classes with abstention · the leakage-safe split · the external evaluation ·
the offline demo · the traceability chain.

---

## 6. What gap we are going to fill

### 6.1 The gap, stated once

> **No published system provides a five-class coffee leaf disease classifier — Coffee Leaf Rust,
> Cercospora Leaf Spot, Leaf Miner, Phoma Leaf Spot, Healthy — that (a) runs fully offline on a
> low-cost mobile device, (b) delivers actionable, sourced agronomic guidance and a persistent
> diagnosis history, and (c) is evaluated against external field photographs with per-class recall,
> calibration error and selective-risk analysis rather than in-domain accuracy alone.**

### 6.2 Why that is a real gap and not a wish

Three pieces of evidence, and each one is published, not asserted:

1. **The accuracy collapse is documented.** A coffee-leaf model reporting **94.09 % internal accuracy**
   accepts **1.9 % of external rust images — 16 out of 847**. A controlled-to-field benchmark reports
   a **67.7-point** accuracy drop with uncalibrated confidence. The failure is not hypothetical and it
   is not rare.
2. **The offline ones are too big, and the accurate ones need a network.** Of the eight systems in
   §4.3, four are cloud-only, one ships a 99 MB model, and the only small offline one is the one with
   1.9 % external recall.
3. **Nobody closes the loop.** Not one of the eight records whether it was right. So the field data
   that would fix the collapse is never produced — and Ethiopia, which has 5.9 million coffee farmers,
   has no confirmed coffee-leaf field dataset at all.

### 6.3 What fills it

The gap is not "nobody has classified coffee leaves" — that is solved, and claiming otherwise would be
the fastest way to lose the room. The gap is that **nobody has made a coffee-leaf classifier that is
honest about its own uncertainty, and nobody has built the loop that turns field use into field data.**

Those are the two contributions, and §5.3 is the mechanism for each:

| Contribution | Mechanism | Measured by |
|---|---|---|
| **Honesty about uncertainty** | ★1 sets + ★2 attribution + `unsupported` + abstention | coverage ≥ `1 − α`; ≥ 80 % attribution accuracy |
| **A loop from use to data** | ★3 retrieval + ★4 confirm/correct + signed packet | top-5 consistency ≥ 70 %; packet verifies; scorecard correct |

### 6.4 The claim, in one sentence

> Public projects ship a classifier that reports a probability. We ship an instrument that states what
> it does not know, shows the farmer **why** it does not know, proves the answer against confirmed
> field cases, and turns the farmer's correction into the first Ethiopian coffee-leaf field dataset —
> without an image leaving the phone unless the farmer says so.

Every clause maps to a numbered feature with a pass condition. That is the difference between a claim
and a slogan, and it is what the design review will test.

---

## 7. What I need back, and by when

| # | From | What | By |
|---|---|---|---|
| 1 | Bemnet | GitHub username, so you can commit and CI can be configured | **Tue 3 Nov** |
| 2 | All | Merge **PR #1** on the group repo — the 16-week plan replaces the sprint plan | **Tue 3 Nov** |
| 3 | All | Read §1 and §2 of this doc; if a task is wrong, say so now, not in W10 | **Wed 4 Nov** |
| 4 | Hayredin | Observed dataset counts in the datasheet | **Wed 4 Nov** |
| 5 | Yohannes | The app running on a phone, with a screenshot | **Wed 4 Nov** |
| 6 | Nahom | Appendix M and Appendix L into the repository | **Wed 4 Nov** |
