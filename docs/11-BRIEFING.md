# Briefing — everything you need to be ready

**For:** Hayredin Mohammed (UGR/2361/16) — Data & Machine-Learning lead
**Written:** Mon 2 Nov 2026 (W3, day 1) · **Target:** ready to answer anything by Tue 3 Nov
**Read this first.** Everything else in `docs/` is the detail behind it.

---

## 0. How to use this file

Three routes. Pick one and do not skip the self-test at §15.

| You have | Read | Time |
|---|---|---|
| **45 minutes** | §1, §2, §3, §4, §11, §15 | 45 min |
| **3 hours** | the above + §5, §6, §7, §8, §12 | 3 h |
| **Tonight, properly** | all of it, then §13 in the order given | 5–6 h |

**The rule.** You do not need to memorise this. You need to be able to **find** any of it in ten
seconds and **say** the headline without notes. A panel forgives "let me show you the table"; it does
not forgive a blank face.

---

## 1. The project in sixty seconds

We are building **BunaDoctor**: an Android app that a coffee farmer points at a leaf. Offline, in
under three seconds, on a phone with 2 GB of RAM, it says which of **five conditions** the leaf has,
how sure it is, what to do about it in Amharic, and it keeps the record.

**But that is not the contribution.** Public projects already classify coffee leaves — eight of them,
and we have read all eight. They are all *classifiers*: they take a photo, return a label, and stop.
They do not say what the label is worth, they cannot tell a bad photograph from an ambiguous leaf, and
none of them ever finds out whether they were right.

**Our contribution is two things:**

1. **Honesty about uncertainty** — the app returns a *set* of possible diseases with a statistical
   coverage guarantee, and when it abstains it says whether the camera or the leaf is at fault.
2. **A loop from use to data** — one tap to confirm or correct, a per-farm accuracy scorecard, and a
   signed, anonymised packet that turns the farmer's correction into the first Ethiopian coffee-leaf
   field dataset. No image leaves the phone unless the farmer taps send.

**The sentence to remember:** *public projects ship a classifier that reports a probability; we ship an
instrument that states what it does not know.*

---

## 2. The problem — eight numbers you must know cold

If you know nothing else tomorrow, know these.

| # | Number | What it means | Source |
|---|---|---|---|
| 1 | **5.9 million** | Ethiopian households farm coffee | UNIDO, *Ethiopia Coffee Value Chain Analysis 2025* |
| 2 | **US$2.89 bn** | coffee export revenue, 2024/25 (≈7.43 M bags) | Daily Coffee News, Jun 2026 (USDA/UNIDO) |
| 3 | **35.3 %** | mean leaf rust **incidence** in south-western Ethiopia | Belachew *et al.* 2020, *Trop. Plant Pathol.* 45(5):511–521 |
| 4 | **9.09 %** | mean rust **severity** in the same survey; **altitude** is the dominant driver | same |
| 5 | **94.09 % → 1.9 %** | a published coffee-leaf model scores 94.09 % internally and accepts **16 of 847** external field rust images | `ConnorLee08/coffee-leaf-efficientnet-b2` model card |
| 6 | **67.7 points** | the accuracy collapse measured on controlled→field shift, while mean confidence stayed at **79.76 %** | Xiang *et al.* 2026, *Front. Plant Sci.* |
| 7 | **58,549** | images in the primary corpus (JMuBEN + JMuBEN2) | measured via the HF mirror API, 21 Oct 2026 |
| 8 | **8 / 8** | public systems that never record whether they were right | our review, 21 Oct 2026 |

**The one-sentence problem:** by the time a farmer can see the rust, the cheap intervention window has
closed — and the person who could have seen it earlier is a development agent covering 300–600
households on a motorbike.

---

## 3. The gap — verbatim, and why every clause is there

> **No published system provides a five-class coffee leaf disease classifier — Coffee Leaf Rust,
> Cercospora Leaf Spot, Leaf Miner, Phoma Leaf Spot, Healthy — that (a) runs fully offline on a
> low-cost mobile device, (b) delivers actionable, sourced agronomic guidance and a persistent
> diagnosis history, and (c) is evaluated against external field photographs with per-class recall,
> calibration error and selective-risk analysis rather than in-domain accuracy alone.**

Read the clauses as defences, because that is what they are:

| Clause | The question it pre-empts | Why it survives |
|---|---|---|
| **five-class** | "Isn't two classes enough?" | Phoma is 11 % of the corpus; dropping it discards a class a farmer will actually meet |
| **(a) fully offline** | "Just use a server" | four of the eight public systems are cloud-only; that is exactly the population that cannot use them |
| **(b) guidance + history** | "A label isn't a diagnosis" | a label is not an action; the farmer needs what to do today |
| **(c) external evaluation** | "94 % accuracy — prove it in a field" | the 1.9 % number is what happens when nobody does this |

**And the honest part, which you should say out loud:** the classifier half is *solved*. Anyone
claiming otherwise loses the room. The gap is that nobody made it honest about its uncertainty, and
nobody built the loop that turns field use into field data.

---

## 4. What we are building

### 4.1 The five classes, plus a sixth that is not a class

| # | Class | Pathogen | Amharic |
|---|---|---|---|
| 1 | Coffee Leaf Rust | *Hemileia vastatrix* | የቡና ቅጠል ዝገት |
| 2 | Cercospora Leaf Spot | *Cercospora coffeicola* | ሴርኮስፖራ |
| 3 | Phoma Leaf Spot | *Phoma tarda* / *costarricensis* | ፎማ |
| 4 | Leaf Miner | *Leucoptera coffeella* | የቅጠል ትል |
| 5 | Healthy | — | ጤናማ |
| — | **`unsupported`** | *Mycena citricolor*, red spider mite, weevil, other plants | — |

`unsupported` is the most important design decision in the project. Every published system forces an
answer into the nearest class. That is the single most common cause of a confident wrong diagnosis. We
refuse instead — and that refusal is measurable.

### 4.2 The system in components

```
        PHONE (always, offline)                    SERVER (optional, never required)
  ┌──────────────────────────────┐          ┌──────────────────────────────┐
  │ capture quality gate         │          │ knowledge-base authoring     │
  │ classifier (int8 TFLite)     │          │ model registry               │
  │ calibration + abstention     │          │ signed packet ingestion      │
  │ knowledge base (SQLite)      │          │ evaluation harness           │
  │ history + scorecard          │          │ analytics                    │
  └──────────────────────────────┘          └──────────────────────────────┘
```

**One model, one knowledge base, two front-ends** (Flutter app + a small web client for extension
officers). The server is never in the critical path of a diagnosis — that is a deliberate
architectural statement, not a limitation.

### 4.3 The nine screens

Home · Capture · Preview · Result · All diseases · Entry detail · History · Record detail · About.

Nine is the whole FYP I design. A tenth screen is a change request — the design and the use cases are
in step (UC-01…UC-09), and that is checked at the W13 review.

### 4.4 The three numbers that define the product

| Target | Value | Why |
|---|---|---|
| APK size | ≤ **40 MB** | it must be sendable over WhatsApp to a phone that is not ours |
| Inference | median ≤ **500 ms**, p95 ≤ **1 s** | the farmer is standing in a field |
| Offline diagnosis path | **100 %** | the network is an upgrade, never a requirement |

### 4.5 The five ★ features — your area, and the reason this isn't a copy

| | Feature | Pass condition |
|---|---|---|
| ★1 | **Conformal prediction sets** — `{rust}` or `{rust, Cercospora}` with a `1 − α` coverage guarantee | empirical coverage ≥ `1 − α` on an external set, within its binomial CI; mean set size reported |
| ★2 | **Uncertainty attribution** — bad photo vs ambiguous leaf | ≥ 80 % correct attribution on 30 degraded + 30 ambiguous images, two annotators |
| ★3 | **Offline look-alike retrieval** — five confirmed field photos, ~300 KB index | top-5 class-consistent ≥ 70 %; < 50 ms; ≤ 300 KB |
| ★4 | **Field-truth flywheel + local scorecard** | packet round-trips and verifies; no image leaves without an explicit action |
| ★5 | **Colour-constancy normalisation** | the measured gain on the cross-dataset evaluation, reported whether positive or negative |

**Cut order if time runs out:** ★3 → ★5 → ★4 → ★2 → ★1. Never cut: five classes with abstention,
the leakage-safe split, the external evaluation, the offline demo.

---

## 5. The data — this is your territory, so own it completely

### 5.1 Nine corpora, six countries, two species

| Dataset | Classes | Size | Licence | Role |
|---|---|---|---|---|
| **JMuBEN** (`t2r6rszp5c`) | Rust, Cercospora, Phoma | 22,591 | CC BY 4.0 | primary training |
| **JMuBEN2** (`tgv3zb82nd`) | Healthy, Miner | 35,964 | CC BY 4.0 | primary training |
| **BRACOL** (`yy2k5y8mxg`) | all five | 1,747 leaves + 2,147 crops | CC BY 4.0 | secondary; Brazil, five phones |
| **RoCoLe** (`c5yvn32dzg`) | rust, miner, healthy | robusta, Ecuador | CC BY 4.0 | secondary; **different species** |
| **Uganda 2025** (`k36wnd6knb`) | rust, Phoma, healthy | — | CC BY 4.0 | external only — **African field** |
| **Saposoa, Peru** (`mfpxg4y65r`) | rust, healthy + *Mycena* | — | CC BY 4.0 | external only |
| **CoffeeLeaf-CO v2** (Zenodo `22756170`) | rust, miner + weevil | — | CC BY 4.0 | external only |
| **Silva 2020** (`vfxf4trtcg`) | rust, miner | full-res 4000×2250 | CC BY 4.0 | external only |
| **RoCoLe** (again) | — | — | — | external only |

**Never train on the external five.** That is DR-07 / T-05 / decision D-006. The whole contribution is
that the external numbers are honest.

### 5.2 The leakage story — the thing that will make or break your mark

Three of the four training datasets contain near-duplicates that a random split leaks:

| Dataset | Leakage mechanism | Correct split unit |
|---|---|---|
| JMuBEN / JMuBEN2 | released images are **already cropped, resized and rotation/flip-augmented** from a smaller original set — the originals were never published | group by original capture, or perceptual-hash clustering |
| BRACOL | the 2,147 symptom crops **are crops of** the 1,747 whole leaves | group leaf ↔ its crops |
| RoCoLe | 4 images per plant (`C##P##`) | group by plant ID |

**How to say it in one breath:** *"A random split of these datasets measures the model's ability to
recognise a photograph it has already seen a slightly rotated version of. It reports 94 %. That number
is real and it means nothing."*

**Your defence is mechanical, not rhetorical:**
- `scripts/prepare_data.py` — grouping key → pHash cluster → stratified grouped split → **four automated
  invariants** → `--audit` gate.
- The split manifest is committed **with a checksum**.
- Tests T-03…T-06 assert the invariants in CI.
- It has been executed end to end: **AUDIT PASSED**.

### 5.3 Three findings you can claim as your own

No published paper in this field reports these:

1. **JMuBEN is pre-augmented** and the originals are unpublished — so the field's most-used dataset
   cannot be split naively.
2. **The paper's two record IDs are inverted** relative to the record titles. We cite record IDs
   explicitly so a reviewer cannot think we mislabelled.
3. **BRACOL's crops are crops of its leaves** — the obvious way to use it leaks.

Add the count reconciliation: paper says **58,555**, the machine-readable mirror says **58,549**. We
report the **observed count after download**, not the published one.

---

## 6. The model and the evaluation

### 6.1 What we compare

| Model | Why it is in the comparison |
|---|---|
| **Majority class** | the baseline that proves the model learned anything at all |
| **MobileNetV3-Small** | the primary — designed for exactly this budget |
| **EfficientNet-Lite0** | the accuracy-per-megabyte alternative |
| **MobileNetV2** | the field's default, so the comparison is fair |
| the two **published** coffee models | run on **our** split, under our protocol, for an honest comparison |

≥ 3 seeded runs each, mean ± sd, macro-F1. Not accuracy — the corpus is imbalanced (Healthy is 32 %).

### 6.2 Quantisation and calibration

- **int8 post-training quantisation**, float16 as the fallback; the accuracy delta is **reported**, not hidden.
- **Temperature scaling** fitted on the validation split. A probability that is not calibrated cannot
  support a threshold — that is the whole reason abstention works.
- **TTA** (flip + two brightness variants) gives the disagreement signal for ★2.
- **Split conformal** gives the sets for ★1: one threshold per α, shipped as a tiny JSON beside the model.

### 6.3 The evaluation — the part nobody else has

| What | How |
|---|---|
| Internal | macro-F1 + per-class F1 on a grouped split |
| **External** | the same model, preprocessing and inference code on 5 field datasets, per-class recall, with **n/a shown honestly** where a dataset has no such class |
| Calibration | ECE and NLL before/after temperature scaling |
| Selective risk | accuracy-vs-coverage curve; the operating point chosen and justified |
| Device | latency median and p95 on **three reference phones**, model size, memory, airplane mode |

**The number the panel will remember:** *94 % internally, 41 % externally* — if that is what we measure.
Say the real number. A group that reports a collapse is more credible than one that reports 94 %.

---

## 7. Objectives, research questions, hypotheses

### 7.1 SO1–SO7 (Table 1.2) — and which ones are yours

| ID | Objective | Measurable target | Owner |
|---|---|---|---|
| **SO1** | Curate a multi-source, **leakage-safe** corpus + datasheet + split manifest | ≥ 58,000 images, ≥ 4 licensed sources, 100 % assigned by a documented grouping rule | **You** |
| **SO2** | Train and compare lightweight CNNs against a naive baseline | ≥ 3 models + majority baseline, mean ± sd over ≥ 3 seeds, macro-F1 | **You** |
| **SO3** | **Quantify and mitigate the generalisation gap** on ≥ 3 external datasets | external macro-F1 per dataset; a threshold where ≥ 95 % of accepted diagnoses are correct, with coverage reported | **You** |
| SO4 | On-device inference: camera + gallery | TFLite ≤ 10 MB; median ≤ 500 ms, p95 ≤ 1 s; all core features in airplane mode | Yohannes |
| SO5 | Results + guidance experience | 100 % of five classes have a reviewed, sourced KB entry; offline asset | Nahom + Yohannes |
| SO6 | Persistent local history with search, filter, export | survives restart; query by class/date; CSV export | Yohannes |
| SO7 | Test and evaluate the whole system | ≥ 40 executed tests with evidence; SUS from ≥ 10 participants; traceability matrix | Nahom |

**SO1, SO2, SO3 are yours.** Three of seven. That is also your ICF defence.

### 7.2 RQ1–RQ5 and H1–H3

| RQ | Question | Hypothesis |
|---|---|---|
| **RQ1** | How large is the macro-F1 drop on external field photos, by class and by dataset? | **H1:** ≥ 20 macro-F1 points |
| **RQ2** | Which mitigation gains most per MB — augmentation, calibration+abstention, or adding African field data? | **H2:** Uganda data + field-realistic augmentation ≥ +5 external macro-F1 for < 1 MB |
| RQ3 | How much does calibration reduce miscalibration, and what coverage survives? | **H3:** ≥ 30 % relative ECE reduction at ≥ 60 % coverage |
| RQ4 | What performance is achievable under 10 MB and 1 s? | — |
| RQ5 | Can guidance be both defensible and comprehensible? | — |

**RQ2 is the interesting one** and it is a controlled ablation with a McNemar test — that is what
turns "we trained a model" into research.

---

## 8. The plan — 16 weeks, five gates

### 8.1 The gates

| Gate | Week | Date | The test that proves it |
|---|---|---|---|
| Proposal approval | W4 | **Sun 15 Nov 2026** | 14 sections, ≥ 15 verified IEEE refs, zero uncited claims, formatted to §11 |
| Requirements baseline | W7 | **Fri 4 Dec 2026** | every FR/NFR/DR has an ID, a test, an owner; no orphan |
| Design review | W13 | **Wed 13 Jan 2027** | Chapters 1–4 assembled; figures at 300 dpi; trace chain unbroken |
| Defense | W14 | **18–24 Jan 2027** | slides 48 h ahead; two timed dry runs |
| Submission | W16 | **7 Feb 2027** | package assembled and receipted |

A gate does not move. If a week slips, it slips **inside** a phase.

### 8.2 The whole 16 weeks, one line each

| W | Dates | The one thing true on Sunday night |
|---|---|---|
| 1 | 19–25 Oct | *(backfill)* repo exists, datasets counted, a commit from each |
| 2 | 26 Oct–1 Nov | *(backfill)* datasheet, ethics screen, nine-screen map |
| **3** | **2–8 Nov** | **all 14 proposal sections exist, even if thin** |
| 4 | 9–15 Nov | **proposal submitted** |
| 5 | 16–22 Nov | 15 sources read with page numbers; gap statement written |
| 6 | 23–29 Nov | FR/NFR/DR drafted, no orphan requirement |
| 7 | 30 Nov–6 Dec | **baseline signed**; split script tested |
| 8 | 7–13 Dec | training pipeline runs end to end; one real accuracy number |
| 9 | 14–20 Dec | model v1 + measured phone latency; ★ features specified |
| 10 | 21–27 Dec | **the generalisation gap is measured and written** |
| 11 | 28 Dec–3 Jan | **the phone diagnoses a leaf offline** — vertical slice |
| 12 | 4–10 Jan | three ★ features working; KB final in EN + Amharic |
| 13 | 11–17 Jan | **design review**; Chapters 1–4 assembled |
| 14 | 18–24 Jan | **defense** |
| 15 | 25–31 Jan | every panel condition closed, named owner |
| 16 | 1–7 Feb | submission package receipted |

**W10 and W11 are the two that decide the project.** W10 is where the honest number appears; W11 is
where it runs on a phone. Everything before is preparation for those two weeks.

### 8.3 What "done" means for any week

1. The **artefact** exists at its path. "Worked on the data" is not an artefact.
2. The **commit** exists under your own name.
3. The **four lines** on Friday to Nahom: what I did · what is blocked · what I need · what is next.

Nothing goes in the logbook that cannot be shown as a commit, a screenshot or a document.

---

## 9. This week — W3, and specifically your tasks

**The week's goal:** every one of the 14 proposal sections exists. Thin is allowed; missing is not.

| Who | Task | The thing you can show |
|---|---|---|
| **You (H)** | Proposal **§2 gap + novelty**, written from `06-DIFFERENTIATION.md`, with numbers from prior work (1.9 % external rust recall) | **2 pages, every number cited** — ✅ *already drafted in `Appendix-A-Proposal.md` §2.3 and §2.6; read it and make it yours* |
| Y | §10 condensed requirements + the proposed-system UI figure | one figure at 300 dpi |
| B | §9 method (design science) + §14 schedule + the High-complexity argument | 4 pages |
| N | §1 problem, §5 questions, §6 scope, §8 literature | 6 pages |

**Your other two obligations this week:**

- **Observed dataset counts** into `data/datasheet.md` by **Wed 4 Nov**. Download, count the actual
  files, record what is there — not what the paper says. This is SO1's evidence.
- **Retry the downloads** off-campus, and record the checksum of each archive in
  `data/dataset-sources.md`.

**If the download fails again:** say so on Wednesday, and use the Hugging Face mirror to get the counts
meanwhile. Do not let a blocked download become a silent week.

---

## 10. Who owns what

| | Who | Owns | Measured by |
|---|---|---|---|
| Lead · app & UI/UX | **Yohannes** | Flutter app, on-device inference, local storage, web client, repo governance | app runs on a real phone **every week** |
| **Data & ML** | **You** | datasets, split, model, quantisation, calibration, external evaluation | counts traceable to a fetch; `--audit` passes; external numbers per class |
| Backend & platform | **Bemnet** | FastAPI, schema, KB asset + versioning, CI, deployment, security | **CI green**; nothing forbidden committed |
| Research & quality | **Nahom** | literature, gap, requirements, tests, KB content, ethics, usability, report, logbook | logbook sent **every Friday** |

**You are accountable for:** dataset curation & datasheet · split script · model training & baselines ·
TFLite export · external evaluation · calibration · reproducibility package.
**You are consulted on:** everything else. **You are informed of:** the rest.

---

## 11. The five ways this project fails — and the fix for each

| # | Failure | The first sign | The fix |
|---|---|---|---|
| 1 | **Leakage inflates the number** (R13) | internal accuracy looks too good, ~99 % | duplicate grouping before splitting; invariants in CI; manifest with checksum |
| 2 | **External accuracy is low** (R6, already High×High) | W10 shows a large drop | **This is the expected result — it is the contribution.** Report it, and let abstention do the work |
| 3 | **Citation errors enter the report** | a number with the wrong source | every number traced to a page; the W5 library pass; see §16 for one I already fixed |
| 4 | **AI-generated content you cannot explain** (R11, active) | a paragraph you did not write | Appendix L kept weekly; never submit a line you cannot explain line-by-line |
| 5 | **Scope creep** (R7) | "let's also do severity" | the non-goals list is a defence, not a limitation |

**The two already-active risks are R11 (AI disclosure) and R20 (defensibility).** Both are cheap now
and expensive in January. R20 is why §12 exists.

---

## 12. The question bank — thirty questions, thirty answers

Say these out loud once. Not to memorise the wording — to find the ones you cannot answer.

### The obvious ones

**1. What is the project?**
An offline Android app that diagnoses five coffee leaf conditions from a photo and gives cited
agronomic guidance in Amharic, plus a record of the farm over time.

**2. Who is it for?**
The smallholder first — 0.4 ha, 2 GB Android phone, no signal at the farm, reads Amharic slowly. Then
the development agent who covers 300–600 households and needs a second opinion she can verify.

**3. Why not just use Plantix?**
Plantix is a cloud service with 150 M+ questions answered; it is excellent and it needs a network.
Four of the eight coffee-specific public systems are cloud-only. The population we target is precisely
the one without connectivity, and Plantix does not cover this five-class taxonomy with Ethiopian
guidance.

**4. Why five classes and not two?**
Rust and miner are the two everybody does. Phoma is 11 % of the corpus and a farmer will meet it.
Dropping it discards a real class to make the problem easier — which is the opposite of a contribution.

### The data ones — your ground

**5. How do you know you are not leaking?**
Grouping key → pHash clustering → stratified grouped split, four automated invariants, an `--audit`
gate that must pass, and the manifest committed with a checksum. T-03…T-06 assert it in CI.

**6. What is actually wrong with a random split here?**
JMuBEN's released images are already rotated and flipped copies of a smaller original set; BRACOL's
crops are crops of its leaves; RoCoLe has four views per plant. A random split puts near-duplicates on
both sides and measures memorisation.

**7. Why 58,549 and not 58,555?**
58,555 is the paper's table; 58,549 is what the machine-readable mirror reports and what anyone can
reproduce. We report the count we actually observe after download, and record the discrepancy.

**8. Why is the JMuBEN record ID confusing?**
The paper's abstract says the two records are "respectively" the other way round from the record
titles. We cite record IDs explicitly so nobody thinks we mislabelled the classes.

**9. Isn't using nine datasets just collecting?**
No — nine separately licensed corpora across six countries and two species, with different taxonomies,
capture conditions and duplication structures, harmonised into one leakage-safe protocol. That is the
data-engineering task, and it is why this is High complexity.

**10. What about the classes the datasets do not share?**
`unsupported`. *Mycena*, red spider mite and weevil are never folded into a disease class. That is
decision D-003 and ADR-005.

### The model ones

**11. Why MobileNetV3-Small?**
It is designed for this budget. ConvNeXt-S is 99 MB and will not load on the target phone — and the
published ConvNeXt coffee model gets 9.1 % Cercospora recall anyway. The gap is not capacity; it is the
unmeasured shift.

**12. What is your baseline?**
Majority class, plus the two published coffee models run on our split under our protocol. A model that
cannot beat majority class has not learned anything.

**13. Why macro-F1 and not accuracy?**
Healthy is 32 % of the corpus. Accuracy rewards the dominant classes; macro-F1 does not.

**14. Why int8 and not float16?**
4× smaller. The accuracy delta is measured and reported — whichever way it goes.

**15. 94 % internally, 41 % externally — why?**
Different distribution: country, camera, background, lighting, and the fact that the training images
were pre-processed. The internal figure measures separation within one source; the external figure
measures the field. The published evidence shows the same effect, at 1.9 %.

**16. What if external accuracy is 30 %?**
Then that is the finding. We report it, we show the coverage curve, and the contribution becomes the
quantified gap plus the abstention mechanism that makes a 30 % model safe to use. Deciding this now is
what stops it being a crisis in week 26.

**17. Why conformal prediction?**
It is the only method that gives a *guarantee* on coverage rather than a number that looks scientific.
It costs one threshold per α and a small JSON file.

**18. Isn't 1.9 % cherry-picked?**
It is one model card, and we say so. It is not our claim — it is the published state of the art on
external coffee rust data, and it is why we evaluate externally at all.

### The system ones

**19. Why offline?**
Because the target user has no signal at the farm, and a diagnosis that needs a network is a diagnosis
that does not exist there.

**20. How big is the app?**
≤ 40 MB, so it can be sent over WhatsApp. The model is ≤ 10 MB.

**21. What happens on a bad photo?**
It abstains, and it says *which* failure it is — too dark, blurry, leaf too small, glare — and tells the
user what to change. A bad photo with an honest "I cannot read this" beats a confident wrong answer.

**22. What is the difference between the two abstention states?**
Amber means the *camera* failed — retake. Blue means the *leaf* is genuinely ambiguous — a human should
look, and we offer a referral card. Same word, opposite action.

### The hard ones

**23. What is your contribution beyond training a classifier?**
Two things: honesty about uncertainty (conformal sets + attribution of *why* it is unsure), and a loop
from field use to field data (confirm/correct → local scorecard → signed packet). Plus the leakage-safe
corpus and the external evaluation protocol.

**24. Who reviews the agronomic advice?**
JARC's Plant Pathology department — the collaboration is requested, not yet confirmed. Until it is,
every entry cites FAO or peer-reviewed Ethiopian literature and the limitation is stated.

**25. Why no product names or doses?**
Legal and ethical. Naming a product and a rate makes the app the source of an incorrect or illegal
recommendation. We name active-ingredient *classes* and point to the registered label and the extension
service.

**26. What about privacy?**
No account, no name, no GPS by default. Nothing leaves the device without an explicit tap, and the tap
says exactly what leaves. The exported packet has no image.

**27. How is this High complexity?**
Three limbs: a real external stakeholder with real data (JMuBEN author, JARC), a substantive research
challenge (the measured generalisation gap and its mitigation), and a substantial data-engineering task
(nine corpora harmonised into one leakage-safe protocol).

**28. What did you personally do?** *(ICF — the question that matters most)*
I own SO1–SO3: the corpus and its datasheet, the leakage-safe split and its audit, the model comparison
and quantisation, the calibration, and the external evaluation. Concretely: `scripts/prepare_data.py`,
the datasheet, the split manifest, and the external results table in Chapter 6.

**29. What is the riskiest part?**
The external evaluation (R6). It is the part that decides whether the project has a result, and it is
the part we cannot control — the field data is what it is. The mitigation is built in from the start:
abstention and calibration mean a weak model degrades safely instead of confidently.

**30. What happens after graduation?**
The corpus, the evaluation harness and the knowledge base stay public. The field-truth loop is the part
that keeps producing data. JARC partnership and DPG alignment are the route to a pilot.

---

## 13. The reading list — in this order, with times

Do not read the 92,000 words. Read these, in this order, and stop when the clock says stop.

| # | File | Why | Time |
|---|---|---|---|
| 1 | **this file** | the map | 20 min |
| 2 | `docs/02-WEEKLY-PLAN.md` §1–§4 | the plan you will be asked about | 25 min |
| 3 | `docs/06-DIFFERENTIATION.md` §2, §4, §5 | the argument, and the five ★ with pass conditions | 25 min |
| 4 | `data/dataset-sources.md` §A.1–A.3, §B | your own territory — the numbers and the traps | 30 min |
| 5 | `docs/proposal/Appendix-A-Proposal.md` §2 (you just rewrote it) | say it in your own words | 20 min |
| 6 | `docs/design/architecture.md` §1–§3 | how the system fits together | 25 min |
| 7 | `docs/report/ch1-introduction.md` §1.4 | SO1–SO7 and RQ1–RQ5 — memorise the shape | 20 min |
| 8 | `docs/03-ROLES.md` §3–§4 | who owns what, and your RACI rows | 15 min |
| 9 | `docs/04-RISK-REGISTER.md` §1 | R1, R2, R6, R13 are yours | 15 min |
| 10 | `docs/requirements/requirements-spec.md` — skim IDs only | know that FR/NFR/DR exist and what they are | 15 min |
| 11 | `docs/defense/slides-and-demo.md` §4 | the five questions they will actually ask | 10 min |
| 12 | `scripts/prepare_data.py` — read it and run `--audit` | you must be able to explain every line | 30 min |

**Total: about 4 hours 10 minutes.** With breaks, that is an evening.

**Do not read tonight:** the full literature review, Chapters 2–4, the appendices. They are reference,
not briefing.

---

## 14. Tonight, by the clock

| Time | Do | Output |
|---|---|---|
| 19:00–19:20 | §1–§4 of this file | the 60-second version, out loud |
| 19:20–19:45 | `02-WEEKLY-PLAN.md` §1–§4 | you can name the five gates and their dates |
| 19:45–20:10 | `06-DIFFERENTIATION.md` §2, §4, §5 | you can state the gap and the five ★ |
| 20:10–20:20 | break | |
| 20:20–20:50 | `data/dataset-sources.md` | the nine corpora and the three traps |
| 20:50–21:10 | Proposal §2 | say §2.3 and §2.6 without reading |
| 21:10–21:35 | `architecture.md` §1–§3 | draw the phone/server split from memory |
| 21:35–21:45 | break | |
| 21:45–22:05 | `ch1` §1.4 | SO1–SO7, RQ1–RQ5 |
| 22:05–22:20 | `03-ROLES.md` §3–§4 | your eight "A/R" rows |
| 22:20–22:35 | `04-RISK-REGISTER.md` | R1, R2, R6, R13 |
| 22:35–23:05 | `prepare_data.py` + run `--audit` | you can explain the split line by line |
| 23:05–23:20 | §12 — answer out loud, no notes | mark the ones you fumbled |
| 23:20–23:30 | §15 self-test | anything under 15/20, reread that section |

---

## 15. Tomorrow's self-test — twenty questions, no notes

Answer out loud. A blank is a pointer to the section, not a failure.

1. What are the five classes, and what is the sixth label? → §4.1
2. What is the gap statement, in one sentence? → §3
3. Name four of the eight public systems and what each one fails at. → §2, `06-DIFFERENTIATION` §2
4. What are the two contributions of this project? → §1
5. Why does a random split leak on JMuBEN, BRACOL and RoCoLe? → §5.2
6. What are the four invariants the split script asserts? → `prepare_data.py`
7. How many images, and why 58,549 and not 58,555? → §5.2
8. What are SO1, SO2 and SO3 — and which are yours? → §7.1
9. What is H1, and what would falsify it? → §7.2
10. Name the five gates and their dates. → §8.1
11. What is the W10 deliverable, and why is it the important one? → §8.2
12. What are the three product numbers (APK, latency, offline)? → §4.4
13. What is ★1 and what is its pass condition? → §4.5
14. What is the difference between the amber and blue abstention states? → §12 Q22
15. Why macro-F1 rather than accuracy? → §12 Q13
16. Why `unsupported` and not "nearest class"? → §4.1
17. What is your personal deliverable this week? → §9
18. What are the two already-active risks, and why? → §11
19. If external accuracy comes back at 30 %, what do you say? → §12 Q16
20. What is the one sentence you want the panel to remember? → §1

---

## 16. Known defects and open decisions — read this, it protects you

These are the things that are currently **not clean**. Better you find them than the panel.

### 16.1 Fixed today

- **The 35.3 % figure was cited to three different sources.** `ch1` cited `[5]` (a Mendeley *dataset*
  record), `07-IMPACT` cited a *review* (Berihun & Alemu), and the proposal cited the actual survey
  (Belachew *et al.* 2020). All three now point to **Belachew *et al.* 2020, ref [58]**, which is the
  large-scale survey that produced the number and identifies altitude as the driver. **This is exactly
  the class of error the W5 library pass exists to catch — expect more, and check every number.**

### 16.2 Still open — decide or fix before the W4 gate

| # | Issue | Why it matters | Action |
|---|---|---|---|
| 1 | **Amharic-first vs English-only** — ADR-015 says ship English-only until a native reviewer signs off; the design says Amharic-first | It is the difference between a product for a farmer and a product for a panel | Decide, and name the reviewer. **Your call to raise with Yohannes** |
| 2 | **Bemnet's GitHub username** | he cannot commit, so the "one commit each" gate is still open | chase it |
| 3 | **CI is not configured** | it is W2's gate test and it is still failing | Bemnet, W3 |
| 4 | **`docs/00-STATUS.md` is a W1 snapshot** | it says the proposal is not done and the logbook is empty — both are now false | refresh it before anyone reads it |
| 5 | **JARC has not replied** | R2/R10 — the KB review has no named reviewer yet | Nahom chases; the fallback is published sources only, with the limitation stated |
| 6 | **The reference registry has 59 entries, the proposal lists 29** | renumbering at the W4 gate will break in-text citations | one pass, one person, before 15 Nov |

**Rule for the next two weeks:** every number in the proposal must trace to a page in a source you have
opened. If you cannot point at the page, cut the number.

---

## 17. The sixty-second status update

When the advisor or John asks *"where are we?"* — say this, in this order:

> We are at W3 of 16. The plan is 16 weeks with five gates; the next one is proposal approval on
> **15 November**. The repository is up with 43 files and the full requirements and design baseline.
> The 16-week plan is in PR #1 waiting to be merged, and the Google Doc has the six sections you asked
> for. On the data side, the nine corpora are verified with licences and counts, and the leakage-safe
> split script runs and passes its audit. This week I am writing the proposal's gap and novelty section,
> and getting the observed dataset counts into the datasheet by Wednesday. The main open item is CI and
> the two GitHub accounts, and the JARC review of the knowledge base.

Sixty seconds. Numbers, dates, and one honest open item. That is what makes an advisor relax.

---

## 18. The one-page summary

| | |
|---|---|
| **What** | An offline five-class coffee leaf diagnosis app with cited Amharic guidance and a farm history |
| **For whom** | Ethiopian smallholders, then development agents |
| **Why now** | 35.3 % rust incidence; the diagnostician is a motorbike ride away; the cheap intervention window closes early |
| **Why not the others** | Eight public systems are classifiers. They do not say what their answer is worth, cannot tell a bad photo from an ambiguous leaf, and never learn they were wrong |
| **The contribution** | Honest uncertainty (conformal sets + attribution) and a loop from field use to field data |
| **Your part** | SO1–SO3: the corpus, the leakage-safe split, the model, the calibration, the external evaluation |
| **The risk** | External accuracy may be low — and that is the result, not the failure |
| **The test** | A phone in airplane mode diagnoses a leaf in under three seconds, on 3 January |
