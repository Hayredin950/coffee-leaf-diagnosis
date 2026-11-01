# Defense Slides Outline and Demonstration Script

**Project:** Design and Development of a Coffee Leaf Disease Diagnosis System Using Deep Learning
**Owner:** Nahom Solomon (slides) · **Demo owner:** Yohannes Berhanu
**Constraint (Guideline §12.4):** *"A general rule is one slide per minute. A 20-minute
presentation should have about 20 slides, and no more than 22 slides, including the title
slide, are allowed for the defense. Backup slides placed after the final slide are not
counted. Submit the slides to the Coordinator at least 48 hours before the defense."*
**Format (Guideline §12.2, §12.3):** a white background with little or no graphics; short
phrases rather than sentences; no more than about six bullets per slide; Arial in black; the
body text at 20–24 pt; slide titles at 30 pt; the title slide at 36 pt at most; every figure
and table legible from the back of the room.

**Submission to the Coordinator:** by **Sunday 9 May 2027** (48 hours before Monday 10 May).
**Owner:** Yohannes Berhanu.

---

## 1. Slide plan — 22 slides, 20 minutes

| # | Title | Content | Speaker | Time | Source |
|---|---|---|---|---|---|
| 1 | **Design and Development of a Coffee Leaf Disease Diagnosis System Using Deep Learning** | Title slide; the four names and IDs; the advisor's name; the university and department | Nahom | 0:30 | — |
| 2 | **The problem** | Farmers lack timely diagnosis; rust incidence 35.3 %; the diagnostician is far away | Nahom | 1:00 | Ch. 1.2 |
| 3 | **Why it is not solved today** | Two mobile apps need a server; five-class apps are cloud-only; no offline five-class system exists | Nahom | 1:00 | Table 1.1 |
| 4 | **The finding that shaped the design** | A published model: 94 % internal, **1.9 %** on external field rust. Field accuracy collapses; confidence does not | Hayredin | 1:30 | Ch. 2.5 |
| 5 | **Our goal and objectives** | The general objective; the seven specific objectives in one table | Nahom | 1:00 | Table 1.2 |
| 6 | **Research questions** | RQ1 the gap · RQ2 the best mitigation · RQ3 calibration · RQ4 the device budget | Nahom | 0:45 | §1.4.3 |
| 7 | **The gap we address** | One sentence in a box: no offline five-class system, with guidance, history and external evaluation | Nahom | 0:45 | §1.2.4 |
| 8 | **System architecture** | The context diagram; offline core in the phone; API and web optional | Bemnet | 1:00 | Fig. 4.1 |
| 9 | **The model pipeline** | Acquire → validate → quality → preprocess → TFLite → calibrate → abstain | Hayredin | 1:00 | §4.3.3 |
| 10 | **The dataset** | 9 corpora, 6 countries, 2 species, ~58 k images; the datasheet | Hayredin | 1:00 | Table 3.1 |
| 11 | **Why the split is the hard part** | JMuBEN is augmented and cropped; BRACOL crops come from leaves; RoCoLE has 4 views per plant → a random split leaks | Hayredin | 1:30 | §4.1.2 |
| 12 | **Our split** | Group → pHash cluster → stratified grouped split; 4 automated invariants; the audit | Hayredin | 1:00 | §5.2 |
| 13 | **Model and quantisation** | MobileNetV3-Small vs EfficientNet-Lite0 vs MobileNetV2; int8 PTQ; ≤ 10 MB | Hayredin | 1:00 | Table 5.4–5.5 |
| 14 | **Baselines** | Majority-class; our transfer-learning model; the two published models run on our split | Hayredin | 0:45 | §3.3.1 |
| 15 | **Internal results** | The comparison table; the macro-F1 and the per-class F1 | Hayredin | 1:00 | Table 6.2 |
| 16 | **The generalisation gap** | Internal vs 5 external datasets, per model; the gap stated | Hayredin | 1:30 | Table 6.3, Fig. 6.1 |
| 17 | **Which classes survive** | The per-class external recall table; the "n/a" cells shown honestly | Hayredin | 1:00 | Table 6.4 |
| 18 | **Calibration and abstention** | ECE before/after; the coverage curve; the chosen operating point | Hayredin | 1:00 | Table 6.6, Fig. 6.3 |
| 19 | **The system** | The five screens; offline; SQLite history; the knowledge base | Yohannes | 1:00 | Ch. 5.4–5.5 |
| 20 | **On-device performance** | Latency on 3 devices; memory; model size; airplane mode | Yohannes | 1:00 | Tables 6.9–6.11 |
| 21 | **Usability and testing** | 55 test cases; the SUS; what participants struggled with | Nahom | 1:00 | Tables 6.1, 6.12 |
| 22 | **Contributions, limitations, future work** | Three contributions; the honest limitations; the top recommendations | Nahom | 1:00 | Ch. 7 |

**Total: 20:30.** The presentation budget is 20 minutes (§17.1), so the speakers must run
**slightly under**. The rehearsal script targets 19:15, leaving 45 seconds of slack.

**Backup slides** (placed after slide 22; not counted toward the 22 limit):
B1 the full requirements table · B2 the API endpoints · B3 the database schema ·
B4 the knowledge-base schema · B5 the full external results per dataset · B6 the ablation
detail · B7 the defect register · B8 the traceability matrix · B9 the third-party licence
list · B10 the AI-use declaration summary.

---

## 2. Speaker allocation and handover

Each speaker has a contiguous block, which avoids the fragmented handovers that cost time.

| Speaker | Slides | Time | The one thing they must land |
|---|---|---|---|
| **Nahom** | 1–7 | 6:45 | The problem is real, the gap is specific, and it is not a repeat of published work |
| **Hayredin** | 9–18 | 10:30 | The dataset is not what it appears to be, the split is the hard part, and the honest external numbers are the contribution |
| **Yohannes** | 8 | 1:00 | The architecture is offline-first and the components are clean |
| **Yohannes** | 19–20 | 2:00 | It is a working, offline, usable system — and it is about to be demonstrated live |
| **Nahom** | 21–22 | 2:00 | It was tested properly, users found it usable, and here is what is left to do |

**Handover language.** Each speaker ends with a bridging sentence that names the next topic,
so the panel hears a coherent argument rather than a sequence of monologues:
- Nahom → Hayredin (slide 9): *"Before the architecture, one sentence about the hardest part
  of this project, which was not the model — it was the data."*
- Hayredin → Yohannes (slide 19): *"Those are the numbers. Now the part you actually wanted to
  see — a working system, on a phone, offline."*
- Bemnet → Nahom (slide 21): *"So it works. Now, how do we know it works?"*

**Time discipline.** The presenter who is speaking must watch the clock, not the slides. If
the group is 90 seconds behind at slide 15, slide 17 (the per-class table) is compressed to
the "n/a" message and the ablation is moved to a backup slide.

---

## 3. Demonstration script

**Owner:** Yohannes Berhanu · **Duration:** 10 minutes (§17.1) · **Backup:** a recorded video is
always prepared and kept on a second device.

### 3.1 Pre-demo checklist (done 15 minutes before)

- [ ] The phone is charged above 50 %, in airplane mode, and the app is installed and launched
- [ ] Three sample leaves are on the table: one clearly diseased, one healthy, one ambiguous
- [ ] The second reference phone is present with the same app installed
- [ ] The laptop is open with the web client, the API health endpoint green
- [ ] The screen is at the home screen and the camera permission is granted
- [ ] The recorded backup video is on the laptop, opened and ready, and the screen-saver is off
- [ ] The demonstration is on the *second* phone (a backup of the primary), so a crash does not
  end the demo

### 3.2 The script

| Time | Action | What is being demonstrated | The requirement it evidences |
|---|---|---|---|
| 0:00 | Hold the phone up. "This is running entirely on the device — no network." | The offline claim, stated before it is proven | NFR-08 |
| 0:20 | Show the airplane-mode icon. Take the camera to the diseased leaf and capture | Capture | FR-01 |
| 0:50 | The result appears | The class, the confidence, the ranked alternatives, the advisory notice | FR-06, FR-07, FR-10, FR-12 |
| 1:30 | Tap **See treatment guidance** | The knowledge base renders offline, with its sources | FR-11, NFR-09 |
| 2:30 | Scroll the guidance | Symptoms, severity cues, organic control, chemical control, prevention, sources | FR-35, FR-36 |
| 3:30 | Tap back → **History** | The record was saved automatically, with the thumbnail | FR-14, FR-15 |
| 4:00 | Tap a filter chip, then **All** | The filtering works | FR-16 |
| 4:30 | Tap **Export CSV** | The export | FR-19 |
| 5:00 | Switch to the gallery, pick the **ambiguous** leaf | The quality gate or the abstention path | FR-05, FR-09 |
| 6:00 | Show the "not confident enough" screen: no class name, the ranked candidates, the suggestions | **The most important moment of the demo.** This is what no prior system does | FR-09, RQ3 |
| 7:00 | Tap **Retake**; capture the healthy leaf | The healthy class, and the record is added | FR-06 |
| 8:00 | Show the second phone with the history | The history is per-device | SO6 |
| 8:30 | Switch to the laptop: the web client | The extension officer's view | FR-31…FR-33 |
| 9:00 | Upload the same diseased leaf on the web | The same model, the same result, a different interface | FR-31, P2 |
| 9:20 | Open the **dataset-note panel** on the web client | The honest performance profile is visible to any visitor | SO3 |
| 9:40 | "This is the full system: offline on the phone, and available to an extension officer on a laptop." | The closing statement | — |

### 3.3 Failure contingencies

**If the demo crashes.** Switch immediately to the second phone. Do not debug on stage. If
both fail, play the recorded video and say: *"The recorded demonstration shows the same flow
— we will follow it together."*

**If the network is required and fails.** The core flow does not need the network. Show the
airplane-mode icon again — it becomes the strongest moment of the demo rather than a problem.

**If the model gives an unexpected result on the sample leaf.** **Do not hide it.** Say:
*"This is exactly the behaviour the calibration is designed to produce — the model is not
confident on this image, so it declines to diagnose. That is the abstention path working."*
This is worth more credit than a flawless demo, because it demonstrates understanding of the
system's own behaviour.

**If time is short.** Cut the web client (1:30) and the second phone (0:30). The core flow
is 7 minutes and cannot be cut.

**Never do these.** Do not retake a photo repeatedly to get a good result — the panel will
notice and it undermines the claim that the system works on ordinary photographs. Do not
skip the ambiguous leaf; the abstention demo is the most persuasive part. Do not claim the
system is more accurate than the numbers in Chapter 6.

---

## 4. Panel questions — quick-reference answers

The full set is in `docs/appendices/Appendix-D-N-Defense.md` §N.4. The five most likely:

1. *"94 % internally, 41 % externally — why?"* → Different distribution: country, camera,
   background, lighting, processing. The internal figure measures separation within one
   source; the external figure measures the field. The published evidence shows the same
   effect [14], [15].
2. *"How do you know you do not leak?"* → Three automated invariants plus the source-group
   rules; the audit is a hard gate and the manifest is committed with checksums.
3. *"Why not a bigger model?"* → ConvNeXt-S is 99 MB with 9.1 % Cercospora recall; the gap is
   not capacity, it is the unmeasured shift. The phone target rules out the large models.
4. *"What if it is wrong?"* → It can be, and the design says so: abstention, the advisory
   notice, class-level rather than product-level guidance, and the honest per-class numbers.
5. *"What is your contribution beyond training a classifier?"* → The leakage-safe corpus, the
   external evaluation protocol, the offline five-class deployment with guidance and history,
   and the honest measurement.

---

## 5. Rehearsal schedule

| Rehearsal | When | Focus | Success criterion |
|---|---|---|---|
| 1 | FYP II week 28, Tuesday | The content; each speaker's block; the Q&A drill | Every speaker can deliver their block without notes; 19 minutes |
| 2 | FYP II week 28, Friday | The demo, end to end, twice | The demo runs in 9 minutes with no errors; the contingencies are rehearsed |
| 3 | FYP II week 29, Tuesday | The full run, timed, with the Q&A | 19 minutes; the handoffs are smooth; the hardest question is answered |

**The final rule.** If the rehearsal runs over 20 minutes, cut content — not the demo and not
the abstention moment. The panel sees the demo as the proof; the slides are the argument.
