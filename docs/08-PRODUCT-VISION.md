# Product Vision — BunaDoctor, End to End

**What this file is.** The picture of the finished product: who uses it, what every screen looks like,
every path a user can take through it, what each layer of AI actually does, and what has to be true for
a farmer in Jimma to keep it installed after the novelty wears off.

**What this file is not.** It is not the requirements register (`docs/requirements/`), the architecture
(`docs/design/architecture.md`) or the plan (`docs/02-WEEKLY-PLAN.md`). Those say *what we must build
and when*. This says *what it feels like when it works*, so that every design decision has something
to be measured against.

**How to use it.** Read §1–§3 before designing anything. Use §6 as the screen checklist and §7 as the
test script — if a flow in §7 cannot be walked on a real phone, the product is not finished. §8 is the
honest account of what the AI does and does not do, which is what the panel will attack. §14 is the
image-generation prompt set, one prompt per screen.

**Status markers.** `[FYP I]` specified and designed by W13 · `[FYP II]` built and evaluated in weeks
17–32 · `[POST]` after graduation, deliberately out of scope now · `⟦VERIFY⟧` a figure or platform
capability that must be checked before it is quoted.

---

## 1. The user

Three people use this system. They are not the same person, and designing for the average of them
produces something none of them will use.

### 1.1 Abebe — the smallholder (primary)

| | |
|---|---|
| **Who** | 42, farms 0.4 ha of garden coffee under shade trees near Jimma, plus maize and enset |
| **Phone** | 2 GB RAM Android 10, 32 GB storage with 3 GB free, one shared device in the household, 4G where the road is, nothing at the farm |
| **Literacy** | Reads Amharic slowly; reads no English; comfortable with WhatsApp voice notes and mobile money |
| **What he does today** | Notices a leaf looks wrong → asks a neighbour → waits for the development agent → sometimes does nothing |
| **What he is afraid of** | Spending money on the wrong chemical, and losing the tree |
| **What he will not do** | Create an account, read a paragraph of instructions, type a search query, use an app that needs the internet |

**His job, in his words:** *"Tell me if this is the rust, tell me what to do before it spreads, and do
not lie to me if you are not sure."*

### 1.2 Tigist — the development agent / extension officer (secondary)

| | |
|---|---|
| **Who** | Covers 300–600 households across four kebeles; motorbike, smartphone, notebook |
| **What she needs** | To triage 40 farms in a day, to not be wrong in front of a farmer, and to leave something behind that the farmer can act on |
| **What she will not do** | Enter data twice, carry a laptop, or trust a black box she cannot check |

**Her job:** *"Give me a second opinion I can verify, and a record I can hand to the woreda."*

### 1.3 Dr. Bekele — the agronomist / reviewer (tertiary)

| | |
|---|---|
| **Who** | Plant pathologist at a research centre; reviews the knowledge base and the field-truth packets |
| **What he needs** | To see what the app tells farmers, to correct it, and to see where the model is failing |
| **What he will not do** | Sign off on advice he has not read, or on a corpus he cannot audit |

**His job:** *"Show me every sentence the app can say, and let me fix the wrong ones."*

### 1.4 What this means for design

| Because Abebe… | The product must… |
|---|---|
| reads slowly, in Amharic | lead with a picture and a colour, not a paragraph; every screen readable at 200 % text size |
| shares one phone | never require an account; never leak one household's data into another's view |
| has no signal at the farm | work fully offline, always; treat the network as an optional upgrade |
| fears wasting money | show cost and safety before the chemical, never a brand or a dose |
| has been lied to by apps before | say "I am not sure" out loud, and show the evidence behind every answer |

---

## 2. The seven principles

Every screen is judged against these. When two conflict, the lower number wins.

1. **The camera is the home screen.** One tap from anywhere to a diagnosis. No menu in front of the
   only thing the app is for.
2. **No typing, ever.** Every action is a tap, a swipe, a photo or a spoken word. Search exists; it is
   never required.
3. **Answer first, evidence second, detail third.** A farmer who wants one word gets one word. A
   researcher who wants the confusion matrix can scroll to it.
4. **Never a dead end.** Every state — bad photo, ambiguous leaf, no camera permission, no storage —
   offers the next best action. An error message that only says "failed" is a design defect.
5. **Say "I don't know" loudly.** Abstention is a first-class screen with its own colour, its own
   advice and its own referral path. It is never a toast, never a grey small-print line.
6. **The phone is the source of truth.** Offline is the default. Sync is an upgrade that must never be
   required to complete a diagnosis.
7. **The farmer owns the data.** Nothing leaves the device without an explicit tap, and the tap says
   exactly what leaves.

---

## 3. The product in one page

**BunaDoctor is a field instrument, not a classifier.**

```
        ┌─────────────────────────────────────────────────────────┐
        │  A farmer points the phone at a coffee leaf.            │
        │  In under three seconds, offline, on a 2 GB phone:      │
        │                                                         │
        │   •  what it probably is — as a SET, not a fake number  │
        │   •  how sure, and WHY it is unsure if it is            │
        │   •  what to do today, this week, and next season       │
        │   •  five confirmed field photos to compare against     │
        │   •  a way to say "you were wrong", which makes the     │
        │      next answer better — for this farm and for everyone│
        └─────────────────────────────────────────────────────────┘
```

| It is | It is not |
|---|---|
| A diagnosis with a stated confidence and a coverage guarantee | A percentage that looks scientific and means nothing |
| An offline knowledge base, every claim cited | A chatbot that invents advice |
| A record of the farm over time | A one-shot novelty app |
| A way to produce the field data Ethiopia does not have | A scrape of somebody else's dataset |
| A tool a development agent can verify | A black box |

**One sentence for the panel:** *public projects ship a classifier that reports a probability; this
ships an instrument that states what it does not know, shows the farmer why, proves the answer against
confirmed field cases, and turns the farmer's correction into field data — without an image leaving the
phone unless the farmer says so.*

---

## 4. The feature map

Seven layers. Each has an owner in `docs/03-ROLES.md` and a week in `docs/02-WEEKLY-PLAN.md`.

| Layer | What it does | Key features | Phase |
|---|---|---|---|
| **1. Capture** | Gets a usable photograph, or refuses and says why | live quality ring · burst of 3 frames · torch · zoom guide · gallery import · WhatsApp-shared image import · symptom checklist fallback | FYP I (W10) |
| **2. Recognition** | Turns pixels into a calibrated answer | 5 classes + `unsupported` · int8 TFLite · temperature scaling · **conformal prediction sets (★1)** · TTA disagreement · out-of-distribution gate | FYP II |
| **3. Explanation** | Shows why, in a form a farmer can falsify | Grad-CAM overlay · differential top-2 with the discriminating symptom · **look-alike confirmed cases (★3)** · **uncertainty attribution (★2)** | FYP II |
| **4. Guidance** | Turns a label into an action | 10-field cited KB · Amharic-first · organic / cultural / chemical *classes* · cost band · safety card · seasonal calendar · referral card | FYP I (KB), FYP II (UI) |
| **5. Ask (RAG)** | Answers a free question, grounded | offline retrieval over the KB · grounded generation · citation-locked · refusal when retrieval is weak · optional online model | FYP II |
| **6. Field truth** | Closes the loop | one-tap confirm/correct · **local scorecard (★4)** · signed anonymised export · recurrence detection | FYP II |
| **7. Platform** | Keeps it alive after graduation | KB bundle with version + checksum · model registry · signed packet ingestion · officer console · evaluation harness · analytics | FYP II / POST |

Two things cut across every layer and are not features but constraints: **colour-constancy
normalisation (★5)** sits between capture and recognition, and **accessibility** sits on top of
everything (§10).

---

## 5. Navigation and information architecture

Four tabs. Not five — a fifth tab costs a farmer a decision every time he opens the app, and the
settings screen is not worth that.

```
┌──────────────────────────────────────────────────────────────┐
│  BunaDoctor                                    [ 🌐 ] [ 👤 ] │  ← language, settings
├──────────────────────────────────────────────────────────────┤
│                                                              │
│                        screen content                        │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│    📷 Scan        🌿 Farm        📚 Learn        💬 Ask       │
└──────────────────────────────────────────────────────────────┘
```

| Tab | Contains | Why it is a tab |
|---|---|---|
| **Scan** | camera, capture review, result, guidance, look-alikes, confirm | the only thing 80 % of users ever open |
| **Farm** | history, plots, scorecard, export | the reason they come back next season |
| **Learn** | KB by class and by symptom, seasonal calendar, safety cards | works with no photo at all |
| **Ask** | grounded question answering | the escape hatch when the camera fails or the question is not visual |

**Modal / full-screen routes** (no tab): first-run language picker, onboarding, analysing, referral
card, export sheet, officer mode.

**Back behaviour is sacred.** Android back always goes up one level, never out of the app, and never
loses a diagnosis in progress. A half-finished diagnosis survives a phone call.

---

## 6. Screen by screen

Format: **purpose → what you see → what you can do → states**. Screens marked ★ are the ones that
decide whether the panel believes the project is different.

### 6.1 First run — language `[FYP I]`

**Purpose:** get to a diagnosis in under 45 seconds without asking the user to read.

**You see:** three large cards, each with a flag-free illustration, the language name in its own
script, and a sample sentence in that language:

```
        ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
        │   አማርኛ      │  │  Afaan      │  │   English   │
        │  ቡና ይመርምሩ    │  │  Oromoo     │  │  Check your │
        │             │  │  Buna qoradhu│  │  coffee     │
        └─────────────┘  └─────────────┘  └─────────────┘
                    [ Continue / ቀጥል ]
```

**You can:** tap a card (it previews by speaking the sentence aloud), tap continue.

**States:** default only. No empty, no error, no loading — this screen must never fail.

### 6.2 Onboarding — three cards `[FYP I]`

**Purpose:** teach the one thing that determines accuracy — how to hold the phone.

**You see:** three full-bleed illustrations, each with one sentence and a short looping animation:

1. *"Fill the frame with one leaf."* — a leaf growing until it touches the guide corners.
2. *"Put the leaf in shade, not in direct sun."* — a shadow crossing the leaf, the quality ring going
   from red to green.
3. *"Hold still for one second."* — a shutter animation and a tick.

**You can:** swipe, skip (always visible, top right), continue.

**States:** skippable at every step; never shown again after completion; re-openable from Learn.

### 6.3 ★ Scan — live camera `[FYP I]`

**Purpose:** the home screen. Everything else is one tap away from here.

**You see:**

```
┌──────────────────────────────────────────────┐
│  ☀  ቅጠሉን በሙሉ ሙላ        ⚡   🔍−   🔍+       │  ← tip, torch, zoom
│                                              │
│        ╭────────────────────────╮            │
│        │                        │            │
│        │      [ leaf guide ]    │            │  ← rounded square, 70 % of width
│        │                        │            │
│        ╰────────────────────────╯            │
│                                              │
│              ◜◝  quality ring                │  ← green arc = ready
│                                              │
│   ●●●○○  3 of 5 frames captured              │
│                                              │
│              (  ◉  )                         │  ← shutter, 72 dp
│                                              │
│   🖼 Gallery          📝 No camera? Answer 5 questions │
└──────────────────────────────────────────────┘
```

**What the quality ring actually measures** (all on-device, ~15 ms per frame):

| Signal | Threshold | What the farmer is told |
|---|---|---|
| Blur (variance of Laplacian) | below τ_blur | *"Hold still"* + a shake icon |
| Exposure (mean luma) | outside 60–190 | *"Too dark" / "Too bright — step into shade"* |
| Leaf coverage (green-mask fraction inside the guide) | below 35 % | *"Move closer"* |
| Glare (clipped-highlight fraction) | above 8 % | *"Tilt away from the sun"* |

**You can:** tap the shutter (auto-captures 3 frames when the ring is green), pinch-zoom, toggle torch,
import from gallery, or switch to the five-question symptom checklist.

**States:**

| State | Behaviour |
|---|---|
| Camera permission denied | full-screen card: what the permission is for, a *Grant* button, and a *Use gallery instead* button — never a blank view |
| No camera hardware | auto-switch to gallery + symptom checklist |
| Storage below 100 MB | warn once, offer to clear old diagnoses (photos are the bulk) |
| Battery below 15 % | suggest the checklist path, which needs no camera |
| Bright sunlight | high-contrast overlay, black guide lines, no thin white text |

### 6.4 Capture review — the quality gate `[FYP I]`

**Purpose:** the single highest-leverage screen in the app. Most field failures are bad photographs,
not bad models.

**You see:** the captured frame, full width, with the three worst signals flagged by icon and a
one-line fix. When it passes, a green check and the sharpest of the three frames.

```
┌──────────────────────────────────────────────┐
│                  [ photo ]                   │
│                                              │
│  ⚠ Too dark        →  Step into the shade    │
│  ✓ Sharp                                     │
│  ✓ Leaf fills the frame                      │
│                                              │
│   [ Retake ]                    [ Use this ] │
└──────────────────────────────────────────────┘
```

**You can:** retake, use anyway (allowed — the model gets a vote too), or use a different frame from
the burst (a small filmstrip).

**States:** pass / warn / fail. *Fail* still allows *Use anyway*, because a bad photo with a
"probably not sure" answer is better than no answer at all — and it is a labelled training example.

### 6.5 Analysing `[FYP I]`

**Purpose:** cover the ~1.5 s of inference without pretending.

**You see:** the leaf thumbnail, a progress bar, and a line of text that says what is happening:
*"Reading the leaf…"* → *"Comparing with known cases…"*. An **offline badge** (a crossed-out cloud) is
always visible here, so the user learns that no network is involved.

**You can:** cancel (returns to review, keeps the photo).

**States:** if inference exceeds 5 s, show *"This phone is slower than expected — still working"* and
offer the checklist path.

### 6.6 ★ Result — confident `[FYP I]`

**Purpose:** one answer, one action.

```
┌──────────────────────────────────────────────┐
│  ◀                              ⤴  ⋯         │
│                                              │
│   ┌────────┐   COFFEE LEAF RUST              │
│   │        │   የቡና ቅጠል ዝገት                  │
│   │ photo  │   ────────────────────          │
│   │        │   ●●●●●  Strong evidence        │
│   └────────┘   (9 of 10 similar leaves agreed)│
│                                              │
│   ⚠  Act within 7 days                       │
│                                              │
│   ┌──────────────────────────────────────┐   │
│   │  What to do now                    → │   │
│   └──────────────────────────────────────┘   │
│   ┌──────────────┐  ┌──────────────────┐     │
│   │ See similar  │  │ Was this right?  │     │
│   │ field cases  │  │  ✓      ✗        │     │
│   └──────────────┘  └──────────────────┘     │
│                                              │
│   Why this answer?  ▾                        │
└──────────────────────────────────────────────┘
```

**What "Strong evidence" means, precisely.** It is not a percentage. It is: *the conformal set at
α = 0.10 contains exactly one class, and the test-time-augmentation agreement is above 90 %.* The
farmer sees dots; the *Why this answer?* drawer shows the actual numbers, the model version, and the
date.

**You can:** open guidance, open look-alikes, confirm, correct, share, or expand the explanation.

**States:** the dots change with evidence strength (5 filled / 3 filled / 1 filled), and the wording
changes with them — *Strong*, *Fair*, *Weak* — never a false precision.

### 6.7 ★ Result — a set, not a label `[FYP I]`

**Purpose:** the screen that makes the whole project defensible. When two classes are genuinely
possible, the app says so and tells the farmer how to separate them.

```
┌──────────────────────────────────────────────┐
│  ◀                              ⤴  ⋯         │
│                                              │
│   Two possibilities                          │
│   ሁለት አማራጮች አሉ                             │
│                                              │
│   ┌────────────────────────────────────┐     │
│   │ ●  Coffee Leaf Rust            55% │     │
│   │    የቡና ቅጠል ዝገት                    │     │
│   ├────────────────────────────────────┤     │
│   │ ●  Cercospora Leaf Spot        38% │     │
│   │    ሴርኮስፖራ                          │     │
│   └────────────────────────────────────┘     │
│                                              │
│   ┌──────────────────────────────────────┐   │
│   │  How to tell them apart            → │   │
│   │  Turn the leaf over. Rust has        │   │
│   │  orange powder on the underside.     │   │
│   │  Cercospora has grey-brown spots     │   │
│   │  with a lighter centre.              │   │
│   └──────────────────────────────────────┘   │
│                                              │
│   [ Take a photo of the underside ]          │
│   [ Show me both diseases ]                  │
│   [ Ask an extension officer ]               │
└──────────────────────────────────────────────┘
```

**Why the two percentages are shown here and not on the confident screen:** they are *ranked
plausibility within the set*, and the set itself carries the guarantee. Showing 55 % / 38 % without
the set would be the fake precision we criticise everyone else for.

**You can:** follow the discriminating-symptom card, take a second photo of the underside (which
re-runs inference and often collapses the set to one class), open either disease's guidance, or start a
referral.

**States:** 2-class set (common), 3-class set (rare — triggers the ambiguous path in §6.9).

### 6.8 ★ Result — abstain because the photo is bad `[FYP I]`

**Purpose:** the most common abstention, and the one every other app gets wrong.

```
┌──────────────────────────────────────────────┐
│                                              │
│              ⚠  (amber, not red)             │
│                                              │
│   I can't read this photo                    │
│   ፎቶውን ማንበብ አልቻልኩም                         │
│                                              │
│   The leaf is too dark on the left side.     │
│   Move into the shade and try again.         │
│                                              │
│   ┌──────────────────────────────────────┐   │
│   │        Retake the photo            → │   │
│   └──────────────────────────────────────┘   │
│   [ Use a photo from my gallery ]            │
│   [ Answer 5 questions instead ]             │
│                                              │
│   Why? The image is 3× darker than the       │
│   photographs this model was trained on.     │
└──────────────────────────────────────────────┘
```

**What makes this different:** the app knows *which* failure this is. It is not "low confidence" — it
is *input quality*, and the fix is a camera action, not an agronomy action.

**You can:** retake (opens the camera with the previous framing as a ghost overlay), import, or take
the checklist path.

### 6.9 ★ Result — abstain because the leaf is ambiguous `[FYP I]`

**Purpose:** the opposite failure, with the opposite advice.

```
┌──────────────────────────────────────────────┐
│                                              │
│              ⚠  (blue, not amber)            │
│                                              │
│   This leaf is hard to call                  │
│   ቅጠሉ ግልጽ አይደለም                            │
│                                              │
│   The photo is clear — but the leaf looks    │
│   like three diseases at once. That is not   │
│   your fault, and guessing would be worse    │
│   than saying so.                            │
│                                              │
│   ┌──────────────────────────────────────┐   │
│   │  Show the 3 closest field cases    → │   │
│   └──────────────────────────────────────┘   │
│   ┌──────────────────────────────────────┐   │
│   │  Send this to an extension officer → │   │
│   └──────────────────────────────────────┘   │
│   [ Look at the leaf more closely ]          │
└──────────────────────────────────────────────┘
```

**The colour difference is the point.** Amber = *the camera failed, fix it*. Blue = *the leaf is
genuinely ambiguous, a human should look*. Same word ("unsure"), opposite action.

**You can:** open the look-alike gallery, generate a referral card, or open the guidance for each
candidate class.

### 6.10 Guidance — the action screen `[FYP I content / FYP II UI]`

**Purpose:** what the farmer actually came for.

```
┌──────────────────────────────────────────────┐
│  ◀   Coffee Leaf Rust                        │
│      የቡና ቅጠል ዝገት          [ 🔊 Listen ]       │
├──────────────────────────────────────────────┤
│  ┌── Do this today ───────────────────────┐  │
│  │ 1. Pick and remove the worst leaves.   │  │
│  │    Put them in a hole, not on the      │  │
│  │    ground.                             │  │
│  │ 2. Do not move tools between trees     │  │
│  │    without cleaning them.              │  │
│  └────────────────────────────────────────┘  │
│                                              │
│  ┌── This week ───────────────────────────┐  │
│  │ • Check the underside of 10 leaves on  │  │
│  │   each of 5 trees.                     │  │
│  │ • If more than 1 in 10 is affected,    │  │
│  │   talk to your development agent.      │  │
│  └────────────────────────────────────────┘  │
│                                              │
│  ┌── Prevention, next season ─────────────┐  │
│  │ • Shade management: 40–50 % cover      │  │
│  │ • Prune to open the canopy             │  │
│  └────────────────────────────────────────┘  │
│                                              │
│  ┌── If you use a fungicide ──────────────┐  │
│  │  Active-ingredient CLASS only:         │  │
│  │  a copper-based product.               │  │
│  │  ⚠ No brand, no dose here. Ask your    │  │
│  │  development agent for the approved    │  │
│  │  product and rate.                     │  │
│  │  ⚠ Wear a mask and gloves. Do not      │  │
│  │  spray within 7 days of harvest.       │  │
│  └────────────────────────────────────────┘  │
│                                              │
│  Sources: 4 citations ▾     Cost band: low   │
└──────────────────────────────────────────────┘
```

**Rules baked into the content model** (not the UI, so they cannot be bypassed):

- **No brand names and no doses.** Active-ingredient *classes* only, with a referral to the agent. This
  is a legal and an ethical line, not a style choice.
- **Every claim carries a citation** that expands into author, year, and what it actually says.
- **Three time horizons**, always in the same order: today / this week / next season. A farmer who
  reads one block gets the urgent one.
- **Cost band** (low / medium / high) rather than a price, because prices move and the app must not be
  wrong about money.
- **Listen** button reads the whole screen in Amharic, because the target user reads slowly.

**You can:** listen, expand citations, share the card, mark *I did this*, or jump to the next candidate
class if the result was a set.

### 6.11 ★ Look-alike confirmed cases `[FYP II]`

**Purpose:** replace a number with something falsifiable in one second.

```
┌──────────────────────────────────────────────┐
│  ◀   Confirmed rust cases                    │
│      near your area, photographed in the field│
├──────────────────────────────────────────────┤
│   ┌────────┐ ┌────────┐ ┌────────┐           │
│   │ field  │ │ field  │ │ field  │           │
│   │ photo  │ │ photo  │ │ photo  │           │
│   └────────┘ └────────┘ └────────┘           │
│   ┌────────┐ ┌────────┐                      │
│   │ field  │ │ field  │                      │
│   └────────┘ └────────┘                      │
│                                              │
│   "These were confirmed as rust by a         │
│    development agent. Does your leaf look    │
│    like these?"                              │
│                                              │
│   [ Yes, similar ]   [ No, different ]       │
└──────────────────────────────────────────────┘
```

**The "No, different" button is the feature.** A Grad-CAM heat map cannot receive that answer. A
retrieval gallery can — and that tap is a labelled disagreement, which is exactly the data that does
not exist.

**You can:** swipe the gallery, tap a case to see its full record (date, altitude band, confirmation
source), answer yes/no.

**States:** if the index has fewer than 3 cases for a class, fall back to static curated exemplars and
say so (*"these are reference photos, not local cases"*). Honesty over a fuller-looking grid.

### 6.12 Confirm or correct `[FYP II]`

**Purpose:** the two-tap loop that makes ★4 possible.

```
┌──────────────────────────────────────────────┐
│   Was this right?                            │
│                                              │
│   ┌──────────────────────────────────────┐   │
│   │  ✓  Yes, it is rust                  │   │
│   └──────────────────────────────────────┘   │
│   ┌──────────────────────────────────────┐   │
│   │  ✗  No — it is something else        │   │
│   └──────────────────────────────────────┘   │
│   ┌──────────────────────────────────────┐   │
│   │  ?  I don't know yet                 │   │
│   └──────────────────────────────────────┘   │
│                                              │
│   Your answer stays on this phone unless     │
│   you choose to send it.                     │
└──────────────────────────────────────────────┘
```

**"No" opens a 5-icon picker** (rust / Cercospora / Phoma / miner / healthy / not sure), no text entry.

**You can:** answer, or dismiss. Dismissing is not failure — it is an unanswered case, and the
scorecard counts it as such rather than assuming it was correct.

### 6.13 Farm — history and plots `[FYP I]`

**Purpose:** the reason to come back.

```
┌──────────────────────────────────────────────┐
│  Farm                              ⚙  ⤴       │
├──────────────────────────────────────────────┤
│  ┌────────────────────────────────────────┐  │
│  │ On your farm:  17 of 20 confirmed      │  │
│  │ correct                                │  │
│  │ ████████████████░░░  85 %              │  │
│  └────────────────────────────────────────┘  │
│                                              │
│  Plot: [ Home garden ▾ ]     + Add plot      │
│                                              │
│  This season                                 │
│  ┌────┬─────────────────┬──────────┬──────┐  │
│  │ 📷 │ Coffee leaf rust│ 12 Jan   │ ✓    │  │
│  │ 📷 │ Healthy         │ 08 Jan   │ —    │  │
│  │ 📷 │ Cercospora      │ 02 Jan   │ ✗    │  │
│  │ 📷 │ Coffee leaf rust│ 28 Dec   │ ✓    │  │
│  └────┴─────────────────┴──────────┴──────┘  │
│                                              │
│  ⚠ Rust seen 3 times on this plot since      │
│    November — check the shaded side.         │
│                                              │
│  [ Export records ]                          │
└──────────────────────────────────────────────┘
```

**Recurrence detection** is a rule, not magic: *the same class on the same plot, ≥ 2 times in 60 days*
→ a banner. It is explainable in one sentence, which is why it survives a defense.

**You can:** filter by plot or class, open any record, add a plot, export CSV/PDF, or open the
scorecard detail.

**States:** empty (a friendly illustration + *"Your first diagnosis will appear here"*), single record,
no plots yet, storage warning.

### 6.14 ★ Scorecard detail `[FYP II]`

**Purpose:** the app reports its own accuracy on the only population that matters.

```
┌──────────────────────────────────────────────┐
│  How well does this app work on your farm?   │
├──────────────────────────────────────────────┤
│  Confirmed correct        17 / 20   85 %     │
│  Confirmed wrong           3 / 20            │
│  Not answered              9                 │
│                                              │
│  Where it was wrong:                         │
│   • 2 × said rust, was Cercospora            │
│   • 1 × said healthy, was leaf miner         │
│                                              │
│  This is not the app's overall accuracy.     │
│  It is what you checked, on your farm.       │
│                                              │
│  [ Send my corrections to help improve it ]  │
└──────────────────────────────────────────────┘
```

**The sentence at the bottom matters more than the number.** It is the difference between an honest
instrument and a marketing claim, and it is the first thing a critical examiner will test.

### 6.15 ★ Ask — grounded question answering `[FYP II]`

**Purpose:** the escape hatch. When the camera fails, or the question is not visual, the farmer can
still get an answer — without a hallucinating chatbot.

```
┌──────────────────────────────────────────────┐
│  Ask about your coffee                       │
├──────────────────────────────────────────────┤
│  Try:                                        │
│   • When should I prune?                     │
│   • Is rust worse after rain?                │
│   • What does leaf miner damage look like?   │
│                                              │
│  ┌────────────────────────────────────────┐  │
│  │ 🎤  Ask by voice                       │  │
│  └────────────────────────────────────────┘  │
│                                              │
│  You asked: "rust after rain?"               │
│  ┌────────────────────────────────────────┐  │
│  │ Yes. Rust spreads faster in wet, warm  │  │
│  │ weather. Scout weekly for 4 weeks      │  │
│  │ after the long rains start.            │  │
│  │                                        │  │
│  │ Source: Berehanu 2023, p. 41  ▾        │  │
│  │ Also: KB-rust-04 "Seasonal risk"       │  │
│  └────────────────────────────────────────┘  │
│                                              │
│  This answer comes only from the app's       │
│  reviewed coffee knowledge. It cannot browse │
│  the internet.                               │
└──────────────────────────────────────────────┘
```

**What it will not do, by design:**

| Behaviour | Why |
|---|---|
| Refuse when retrieval is weak — *"I don't have a reviewed answer for that. Here is how to ask an officer."* | An invented answer about a pesticide is worse than no answer |
| Never answer outside coffee agronomy | The corpus is the boundary |
| Never produce a brand or a dose | Content rule, enforced at the retrieval layer, not the prompt |
| Always show the source chunk | A farmer cannot check a citation, but an officer can |
| Work with the radio off | The whole point |

**Architecture:** retrieval over ~120 reviewed chunks → grounded generation → citation check →
refusal gate. Full design in §8.4.

### 6.16 Learn — the library `[FYP I]`

**Purpose:** the app is useful with no photograph at all.

**You see:** two entry points, because farmers think in two different ways:

```
┌──────────────────────────────────────────────┐
│  Learn                                       │
├──────────────────────────────────────────────┤
│  By what I see          By disease name      │
│  ┌──────┐ ┌──────┐      ┌────────────────┐   │
│  │orange│ │ grey │      │ Coffee leaf    │   │
│  │powder│ │spots │      │ rust           │   │
│  └──────┘ └──────┘      ├────────────────┤   │
│  ┌──────┐ ┌──────┐      │ Cercospora     │   │
│  │white │ │holes │      ├────────────────┤   │
│  │lines │ │in leaf│     │ Phoma          │   │
│  └──────┘ └──────┘      ├────────────────┤   │
│                         │ Leaf miner     │   │
│  Seasonal calendar  →   └────────────────┘   │
│  Spray safety card  →                        │
└──────────────────────────────────────────────┘
```

**"By what I see"** is a visual symptom index — six photo tiles, no reading required. It is the
single most accessible feature in the app and costs almost nothing to build.

### 6.17 Referral card `[FYP II]`

**Purpose:** hand the problem to a human, without the farmer having to explain it.

**You see:** a generated card — leaf photo, predicted set, date, plot label, GPS *only if the user
opts in*, and a QR code — exportable as an image for WhatsApp, a PDF, or a printed page.

```
┌────────────────────────────────┐
│  BunaDoctor referral           │
│  ┌──────┐  Coffee leaf rust    │
│  │photo │  or Cercospora       │
│  └──────┘  12 Jan 2027         │
│  Plot: home garden             │
│  Farmer note: "started after   │
│  the rain, lower leaves first" │
│                                │
│  ▓▓▓ QR ▓▓▓   Case #A7F2       │
└────────────────────────────────┘
```

**You can:** share to WhatsApp, save as image, print, or show the QR to an officer.

**Privacy rule:** the photo and the note leave the device *because the farmer pressed share*. Nothing
is attached silently.

### 6.18 Settings and accessibility `[FYP I]`

| Group | Settings |
|---|---|
| Language | Amharic · Afaan Oromoo · English (per-screen, not per-app: an officer may want English while the farmer keeps Amharic) |
| Reading | Text size (100 / 125 / 150 / 200 %) · **Read screens aloud** · high contrast · reduce motion |
| Data | Offline-only mode (hard switch, hides every network feature) · Wi-Fi-only updates · clear photo cache |
| Storage | What is using space, with a one-tap clear of photos older than 90 days |
| Model | Version, size, last updated, accuracy on the last 30 confirmed cases |
| Knowledge | Bundle version, checksum, last updated, source count |
| Privacy | What is stored, what can leave, delete everything |
| About | Model card, licences, dataset attributions, the four names, the advisor |

**Every setting is reachable in three taps from anywhere** — because the user who needs 200 % text is
the user least able to hunt for it.

### 6.19 Officer mode `[FYP II / POST]`

**Purpose:** the second user, without building a second app.

**You see:** a PIN-gated list of cases shared to this officer, sorted by age and uncertainty, each with
the photo, the set, the farmer's note, and a *Confirm / Correct / Reply* action.

**Why it is a mode and not a product:** a separate officer dashboard is a separate application, and
`docs/06-DIFFERENTIATION.md` §6 rejects that with a reason. The API stays as the integration point for
a cooperative that wants to build one.

### 6.20 Update states `[FYP II]`

| Update | Mechanism | Safety rule |
|---|---|---|
| **Knowledge bundle** | download or import a file / QR from an officer | checksum + version + signature; the old bundle is kept until the new one validates |
| **Model** | background download on Wi-Fi, or sideload from an officer's phone | never swap a model mid-diagnosis; shadow-compare for one week before it becomes default |
| **App** | Play Store, or a shared APK | APK stays under 40 MB so it can be sent over WhatsApp |

**Every update path must work with no internet at all** — a file, a QR, or another phone. That is what
"offline-first" actually means in a place where the last mile is a motorbike.

---

## 7. The flows

Twelve paths, written as test scripts. If any of them cannot be walked on a real phone, the product is
not done.

### F1 — First run to first answer (target: 45 seconds)

```
install → language card → 3 onboarding cards (skippable)
        → camera permission (explained, with a fallback)
        → scan screen → shutter (ring green)
        → capture review (pass) → analysing (1.5 s)
        → result: one class, 5 dots → guidance
```

**Pass:** a first-time user reaches a guidance screen in under 60 s without help, measured on 5 users.

### F2 — The happy path, repeated

```
Scan → shutter → result → "What to do now" → read/listen → back
→ Farm: the record is already there → confirm ✓ → scorecard +1
```

**Pass:** the record appears without any save action. Saving is not a user decision.

### F3 — The uncertain path

```
Scan → result: 2-class set
     → "How to tell them apart" → "photograph the underside"
     → second scan → set collapses to one class
```

**Pass:** the underside instruction is specific enough that a user can follow it without asking what
"underside" means — verified with an illustration, not a word.

### F4 — The bad-photo path

```
shutter → quality gate: "Too dark" → retake with ghost overlay
        → still dark → "Use anyway"
        → result: amber abstain "I can't read this photo"
        → retake → pass
```

**Pass:** a user who fails twice is never left without an action. The app never shows a bare error.

### F5 — The ambiguous-leaf path

```
result: blue abstain → "3 closest field cases"
                    → "No, different" → 5-icon picker → correction saved
                    → "Send to an extension officer" → referral card → WhatsApp
```

**Pass:** the referral card is produced in ≤ 2 taps from the abstain screen.

### F6 — Fully offline (the acceptance test)

```
airplane mode ON → scan → result → guidance → learn → ask → confirm → export to file
```

**Pass:** every step works. The only visible difference is a badge. **This is the single most
important test in the project** and it is the one the panel will ask for.

### F7 — Correction to export

```
confirm ✗ → picker → record updated → scorecard recalculates
        → "Send my corrections" → consent sheet (shows exactly what leaves)
        → signed packet written → share via file / QR
```

**Pass:** the consent sheet lists every field; no image is included unless explicitly ticked.

### F8 — Knowledge update with no internet

```
officer sends a .kbpkg over WhatsApp → open → checksum verifies
→ "Knowledge updated to v1.3 (12 new entries)" → new content visible
```

**Pass:** a corrupted file is rejected with a readable message and the old bundle keeps working.

### F9 — Ask, grounded

```
Ask → suggested question → retrieval → answer + citation
    → ask something outside the corpus → refusal + officer path
```

**Pass:** 60-question evaluation set: ≥ 90 % of in-corpus answers correct, 100 % of out-of-corpus
questions refused, 100 % of answers carry a valid citation. (Numbers are the target; report what is
measured.)

### F10 — The farm over a season

```
add plot → diagnoses accumulate → recurrence banner after 2 in 60 days
→ export PDF for the cooperative
```

**Pass:** the PDF is readable by someone who was not there and contains the dates, classes, and
confirmation status.

### F11 — Accessibility path

```
200 % text → TalkBack on → "Read screens aloud" on
→ complete F2 using only the screen reader and voice
```

**Pass:** no truncated labels, no icon-only controls without content descriptions, no colour-only
meaning.

### F12 — Hostile conditions

| Condition | Required behaviour |
|---|---|
| Battery 10 % | offer the checklist path, disable the torch |
| Storage 50 MB | offer to clear old photos, refuse new captures gracefully |
| Camera permission permanently denied | full functionality via gallery + checklist |
| Android 8, 2 GB RAM | app launches in < 4 s, inference < 3 s |
| Screen in direct sun | all text passes contrast at 200 % brightness |
| Phone shared by two people | no account, no cross-contamination, a *clear this session* action |

---

## 8. The AI, honestly

This is the section a panel will attack. It is written to survive that.

### 8.1 What runs where

```
                    ON THE PHONE (always)              SERVER (optional)
  ┌─────────────────────────────────────────┐   ┌──────────────────────────┐
  │ capture quality gate      ~15 ms        │   │ model registry           │
  │ colour constancy (★5)     ~20 ms        │   │ KB authoring + review    │
  │ classifier (int8 TFLite)  ~300–800 ms   │   │ packet ingestion         │
  │ TTA ×3 + conformal (★1)   ~1–2 s        │   │ officer console          │
  │ Grad-CAM                  ~50 ms        │   │ evaluation harness       │
  │ retrieval index (★3)      ~20 ms        │   │ analytics                │
  │ KB + Ask retrieval        ~30 ms        │   │ larger LLM (online only) │
  │ TTS (optional)            streaming     │   │                          │
  └─────────────────────────────────────────┘   └──────────────────────────┘
```

**The server is never in the critical path of a diagnosis.** It exists for authoring, review,
distribution and measurement. That is a deliberate architectural statement, not a limitation.

### 8.2 The vision model

| Decision | Choice | Why |
|---|---|---|
| Backbone | MobileNetV3-Small, compared against EfficientNet-Lite0 and MobileNetV2 | the comparison is a result, not a preference |
| Quantisation | int8 post-training, with a float16 fallback | 4× smaller; accuracy delta reported |
| Classes | rust · Cercospora · Phoma · leaf miner · healthy + `unsupported` | `unsupported` is how the app refuses an out-of-taxonomy leaf instead of forcing it into one of five |
| Calibration | temperature scaling on the validation split | a probability that is not calibrated cannot support a threshold |
| Uncertainty | TTA (flip + 2 brightness) agreement, plus max-softmax and entropy | three cheap signals, all offline |
| Sets | split conformal, one threshold per α | the only method that gives a *guarantee*, and it costs a JSON file |
| OOD gate | embedding distance to the training manifold | catches "this is not a coffee leaf" before the classifier lies |

**What the model is not:** a general plant-disease model, a severity estimator, or a detector. It
classifies one leaf, cropped by the user, into six buckets. Saying that plainly is what makes the rest
credible.

### 8.3 The retrieval layer (★3)

A ~300 KB index of embeddings over confirmed field photographs.

```
query image → 128-d embedding (from the classifier's penultimate layer, no extra model)
            → cosine top-k over 200–400 confirmed cases
            → return 5 with their metadata
```

**Why the penultimate layer:** it costs nothing — no second model, no extra download — and the
embeddings are already aligned with the classes the model was trained on. A dedicated metric-learning
head is the upgrade path if the pass condition is not met.

### 8.4 Ask — the RAG design `[FYP II]`

The naive version of this feature is "put a small LLM on the phone and let it chat". That version
invents pesticide advice and is worse than nothing. The design below is the one that can be defended.

**The corpus.** ~120 chunks, authored by a human, reviewed by an agronomist:

| Source | Chunks | Example chunk |
|---|---|---|
| 5 classes × 10 KB fields | 50 | `KB-rust-04` — seasonal risk, cited to Berehanu 2023 |
| 30 farmer FAQ | 30 | "Why do the lower leaves go first?" |
| 5 symptom descriptions | 5 | "What leaf miner damage looks like" |
| Safety and handling | 10 | PPE, pre-harvest interval, disposal |
| Seasonal calendar | 12 | month → what to scout for |
| Referral and escalation | 8 | when to call an officer, what to bring |
| Out-of-scope refusal set | 5 | "How much does a litre of Roundup cost?" → refuse |

**The pipeline.**

```
question (text or Amharic voice → ASR)
   │
   ├─ normalise (Ethiopic-aware tokenisation, synonym map: "ዝገት"→rust, "rust"→rust)
   │
   ├─ retrieve: hybrid BM25 (SQLite FTS5) + 384-d embedding, top 5, rerank
   │
   ├─ GATE: if top score < τ  →  REFUSE with the officer path   ← the most important box
   │
   ├─ generate:
   │     offline → template assembly from the retrieved chunks (no LLM)
   │     online  → LLM, constrained to the chunks, with a citation requirement
   │
   ├─ verify: every sentence must map to a chunk id; if not → drop it
   │
   └─ answer + citations + "this comes only from reviewed coffee knowledge"
```

**Why the offline path is template-first, not LLM-first.** A 270M-parameter model scores 15.4 on
TriviaQA and 26.7 on BIG-Bench Hard — it cannot be trusted to answer a question about a fungicide.
The templates are boring and correct. The LLM is an *optional* rephrasing layer, and when it is used
it is constrained by constrained decoding and a citation check. If we ship a 270M model on-device at
all, it is to make the answer read more naturally in Amharic, not to decide what is true.

**The refusal gate is the feature.** Every chatbot demo fails by answering. Ours is judged on whether
it refuses correctly, and that is measurable: a 60-question set with 20 deliberately out-of-corpus
questions.

**Evaluation (this is what goes in Chapter 6):**

| Metric | Target | How |
|---|---|---|
| Retrieval recall@5 | ≥ 0.90 | 60 questions with a known correct chunk |
| Answer correctness (in-corpus) | ≥ 0.90 | two raters, disagreements recorded |
| Citation validity | 1.00 | every sentence maps to a retrieved chunk |
| Correct refusal (out-of-corpus) | 1.00 | 20 adversarial questions |
| Amharic answer readability | ≥ 4/5 | 5 native speakers, 20 answers |

### 8.5 Voice

| Function | Approach | Phase |
|---|---|---|
| Read the guidance aloud (Amharic) | on-device TTS, streaming | FYP II |
| Ask a question by voice | on-device ASR, Amharic | FYP II (stretch) |
| Both | must work offline | — |

LiteRT ships offline TTS and ASR sample pipelines and runs on Android API 24+ ⟦VERIFY Amharic model
availability and quality before committing⟧. **Fallback if Amharic TTS is unusable:** pre-recorded
audio for the 20 most common guidance blocks (about 3 MB) — a farmer does not need every sentence
spoken, only the important ones.

### 8.6 What we deliberately do not do

| Not doing | Because |
|---|---|
| Severity percentage | needs lesion segmentation and a validated scale; an unvalidated "34 % infected" is worse than nothing |
| Product names or doses | legal and ethical line |
| A general chatbot | invents advice, needs a network, cannot be audited |
| Multi-crop | dilutes the corpus, the taxonomy and the KB |
| On-device retraining | no labelled field data exists yet — ★4 is how that changes |
| Cloud sync as a requirement | contradicts the premise; accounts drag in a privacy statement we cannot support |

---

## 9. The platform

### 9.1 Components

```
┌──────────────┐   optional, never required   ┌───────────────────────────┐
│ Flutter app  │ ───────────────────────────► │ FastAPI                   │
│  · TFLite    │   KB bundle · model · packet │  · /kb/bundle             │
│  · SQLite    │ ◄─────────────────────────── │  · /models/latest         │
│  · FTS5      │                              │  · /packets (signed)      │
└──────────────┘                              │  · /officer/cases         │
                                              │  · /analytics             │
┌──────────────┐                              └─────────┬─────────────────┘
│ Web client   │ ─────────────────────────────────────► │
│ (officers)   │                                        │
└──────────────┘                              ┌─────────▼─────────────────┐
                                              │ PostgreSQL + pgvector     │
                                              │  · KB chunks + embeddings │
                                              │  · model registry         │
                                              │  · field packets          │
                                              │  · officer cases          │
                                              └───────────────────────────┘
```

### 9.2 The data model, in one table

| Table | Holds | Leaves the phone? |
|---|---|---|
| `diagnoses` | photo path, class set, confidence, model version, plot, timestamp | no (photo) / yes (metadata, if exported) |
| `confirmations` | confirmed / corrected / unknown, corrected class | yes, in the signed packet |
| `plots` | label, size band, altitude band | yes, if the farmer names it |
| `kb_chunks` | text, class, citations, version | n/a (shipped) |
| `kb_fts` | FTS5 index over the chunks | n/a |
| `embeddings` | 384-d vectors, chunk ids | n/a |
| `exemplars` | 128-d vectors, class, provenance | n/a (shipped) |
| `scorecard` | derived counts per plot | no |

### 9.3 The signed packet

The artefact that makes ★4 real, and the only thing that ever leaves the device.

```json
{
  "schema": "bunadoctor.packet/1",
  "device": "anon-7f3a…",
  "model": {"id": "mnv3s-int8", "version": "1.2.0", "checksum": "sha256:…"},
  "kb":    {"version": "1.3", "checksum": "sha256:…"},
  "records": [
    {"ts": "2027-01-12T09:14:00+03:00", "set": ["rust"], "pred": "rust",
     "confirmed": "rust", "quality": {"blur": 0.81, "luma": 132, "cover": 0.62},
     "plot": "home-garden", "alt_band": "1600-1800"}
  ],
  "signature": "sha256-chain:…"
}
```

**No image, no name, no GPS, no phone number.** The signature is a checksum chain, not PKI — say that
plainly rather than implying more security than exists.

---

## 10. Accessibility and localisation

| Requirement | Target | How |
|---|---|---|
| Text scaling | 200 % with no truncation | no fixed-height text containers |
| Contrast | WCAG 2.2 AA (4.5:1 body, 3:1 large) | tested in direct sunlight, not on a desk |
| Touch targets | ≥ 48 dp, 56 dp for primary actions | — |
| Screen reader | full TalkBack traversal, meaningful content descriptions | tested with TalkBack on |
| Colour | never the only signal | icon + colour + word, always |
| Reading level | Amharic at a grade-4 level | reviewed by a native speaker, not translated word-for-word |
| Language | Amharic · Afaan Oromoo · English | per-screen switching |
| Script | Ethiopic rendered with an embedded Noto Sans Ethiopic | bundled, not fetched |
| Voice | read-aloud for every guidance screen | TTS or pre-recorded fallback |
| Illiteracy | the whole F1→F2 path completable with zero reading | icon-first, voice-first |

**The test that matters:** hand the phone to someone who cannot read, and see whether they can get a
diagnosis. If they cannot, the accessibility work is not done.

---

## 11. Non-functional targets

| Target | Value | Why this number |
|---|---|---|
| APK size | ≤ 40 MB | sendable over WhatsApp |
| Model size | ≤ 10 MB int8 | fits with the KB and the app |
| Cold start | ≤ 4 s on a 2 GB device | beyond that, users assume it is broken |
| Inference | ≤ 3 s end-to-end including TTA | the farmer is standing in a field |
| Battery | ≤ 3 % for 20 diagnoses | must not be the reason the phone dies |
| Storage | ≤ 25 MB for 100 diagnoses | photos dominate; compress to 720 px |
| Works offline | 100 % of the diagnosis path | non-negotiable |
| Crash-free sessions | ≥ 99.5 % | measured in FYP II beta |
| Min Android | 8.0, API 26, 2 GB RAM | covers the installed base we can reach |

---

## 12. What ships when

| Phase | Ships | Evidence produced |
|---|---|---|
| **FYP I (W1–W16)** | design, KB content, the plan, the split pipeline, the vertical slice in W11 | Chapters 1–4, the design review, the defense |
| **FYP II (W17–W32)** | trained + quantised model, the app with ★1–★5, the API, the evaluation | Chapters 5–7, the external evaluation, the usability study |
| **POST** | Play Store listing, officer console, cooperative licensing, the field dataset | a paper, a DPG nomination, a pilot |

**The MVP cut line, if time runs out** (same order as `docs/02-WEEKLY-PLAN.md` §8):
★3 retrieval → ★5 normalisation → ★4 flywheel → ★2 attribution → ★1 sets. Never cut: the five
classes with abstention, the leakage-safe split, the external evaluation, the offline demo.

---

## 13. What could ruin the experience

| Risk | What the user sees | Design response |
|---|---|---|
| Model is confident and wrong | a farmer sprays the wrong thing | conformal sets + abstention + "was this right?" + never a dose |
| Photo quality is poor in the field | "the app doesn't work" | the quality gate, with the fix named |
| Amharic translation reads like a machine | distrust | native review, grade-4 reading level, read-aloud |
| App is 120 MB | never installed | 40 MB budget, enforced in CI |
| KB goes stale | wrong advice for a new season | versioned bundles, officer-distributed updates |
| The demo works and the field does not | exactly the published failure mode | external evaluation is a gate, not an afterthought |
| Nobody uses it after graduation | a dead repo | JARC partnership, DPG alignment, a named maintainer |

---

## 14. Seeing it before building it

The eighteen screens above are written as prompts you can paste into an image generator, so the group
can argue about a picture instead of an adjective — and so the proposal has figures before the app
exists.

**The prompts live in their own file: [`09-APP-IMAGE-PROMPTS.md`](09-APP-IMAGE-PROMPTS.md).** They are
kept separate because they are meant to be copied one at a time, and a prompt buried in a 900-line
document is a prompt nobody uses.

Three rules when you generate them:

1. **One aspect ratio for all eighteen** (9:19.5), or the set will not look like one product.
2. **Check the Amharic.** Most generators render Ethiopic script as boxes or invented glyphs. Either
   accept English-only labels, or add the Amharic in Figma afterwards. **Never put a screenshot with
   fake Amharic in the report** — a panel that reads Amharic will notice, and it undermines every other
   figure on the page.
3. **Generate P3, P6 and P7 first.** Those three — the scan screen, the confident result, and the
   two-class set — are the argument. If those three do not communicate the idea in five seconds, the
   rest of the set will not save it.

---

## 15. The one-page summary for the panel

> A farmer photographs one coffee leaf. Offline, in under three seconds, on a phone that costs less
> than a bag of fertiliser, the app returns a **set** of possible diseases with a statistical guarantee
> rather than a fake percentage; says **whether the uncertainty is the camera's fault or the leaf's**,
> because those need opposite actions; shows **five confirmed field cases** the farmer can falsify at a
> glance; gives **cited, brand-free guidance** in Amharic, read aloud; and records whether it was right,
> so that the app can report its own accuracy on that farm — and so that the corrections become the
> first Ethiopian coffee-leaf field dataset.
>
> Everything except the optional officer referral works with the radio off. Nothing leaves the phone
> unless the farmer taps send. And every claim the app makes is traceable to a source a plant
> pathologist has read.
