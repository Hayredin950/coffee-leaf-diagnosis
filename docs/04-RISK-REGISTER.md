# Appendix H — Project Risk Register

**Owner:** Yohannes Berhanu (maintains) · **Reviewed with the advisor monthly** (Guideline §6.3)
**Version:** 1.0 · **Last reviewed:** 2026-10-21

**Scales.** Probability: L (low, < 25 %) · M (medium, 25–60 %) · H (high, > 60 %).
Impact: L (negligible) · M (costs days or degrades a component) · H (threatens a milestone or
the defence).
**Rule:** every **High** impact risk must have a named fallback that reduces scope rather than
eliminating the deliverable.

---

## 1. Register

| ID | Risk | Category | P | I | Mitigation (preventive) | Fallback (if it occurs) | Owner | Status | Review date |
|---|---|---|---|---|---|---|---|---|---|
| **R1** | The JMuBEN author does not share the original un-augmented images | Data | M | M | Proceed without them; the released dataset is sufficient if duplicate grouping is done properly; request the originals as an enhancement | Use BRACOL + Uganda + Saposoa as the training corpus, and treat JMuBEN as one external set | Hayredin | Open | 2026-11-04 |
| **R2** | An external dataset proves unavailable, unlabelled or licence-restricted | Data | M | H | All five external sources are already verified with direct downloads; three are sufficient for SO3 | Report on the three that work; state the substitution in Chapter 6 | Hayredin | Open | 2026-11-04 |
| **R3** | No GPU available for training | Technology | M | M | Kaggle/Colab free-tier P100/T4 notebooks are the primary route; the reference architectures train in under 2 h | Reduce the architecture set to MobileNetV3-Small only and extend the training to a CPU run overnight | Hayredin | Open | 2026-11-04 |
| **R4** | Flutter + TFLite integration stalls (plugin/native build issues) | Technology | M | H | Scaffold in week 1; prove the toolchain with a placeholder model before writing any feature code | Fallback A: the TensorFlow Lite task library over a platform channel. Fallback B: a minimal Kotlin app loading the same `.tflite` artefact, with the Flutter app as the optional front-end | Yohannes | Open | 2026-11-04 |
| **R5** | The quantised model exceeds 10 MB or exceeds the latency budget on a low-end device | Technical | M | M | Progressive reduction ladder, applied in order: int8 PTQ → EfficientNet-Lite0 → MobileNetV2 → 160×160 input → a MobileNetV3-Small with reduced width multiplier | Publish the float16 model and report the accuracy/latency trade-off honestly; revise NFR-01/NFR-02 through change control | Hayredin + Yohannes | Open | 2026-11-04 |
| **R6** | External field accuracy is too low for the system to be useful | Technical | H | M | Abstention and calibration are built in from the start so a low-accuracy model degrades safely rather than confidently | **This is a finding, not a failure.** The contribution becomes the quantified gap plus the abstention mechanism. Report it as the central result and revise SO3's achievement status to "partially achieved" | All | Open | 2026-11-04 |
| **R7** | Scope expands into detection, severity estimation, more crops, or a cloud sync | Scope | M | H | Explicit non-goals in the proposal §5.1 and the requirements §5; a change-control table; the advisor reviews scope at each meeting | Apply the reduced-scope fallback: drop the web client first, then the optional export, then the alternative architectures | All | Open | 2026-11-04 |
| **R8** | Schedule delay from an unavailable member, an exam period, or illness | Schedule | M | M | Weekly cross-review rotation keeps knowledge distributed; every task in the roadmap has a named backup; the rotation table in `03-ROLES.md` §5 | Re-sequence the roadmap to protect the critical path (data → model → app). Defer the web client and the optional export | All | Open | 2026-11-04 |
| **R9** | The system is built but cannot be demonstrated at the defence | Deployment | L | H | The core flow is offline and needs no server; the APK is installed on at least two devices ahead of time; a recorded backup video is kept | Fall back to the recorded demonstration (permitted only with the Committee's prior approval — §17.2, so seek approval in advance) | Yohannes + Bemnet | Open | 2026-11-04 |
| **R10** | The agronomic guidance is challenged as inaccurate or unsafe | Content | M | M | Every KB field carries a citation; a JARC plant pathologist reviews before inclusion; the app names active-ingredient classes rather than products and directs the user to the label | Remove the disputed practice and replace it with the conservative recommendation; record the change in the KB version history | Nahom | Open | 2026-11-04 |
| **R11** | AI-generated content in the report is treated as misconduct | Academic | M | H | Appendix L is maintained from day one; every AI-assisted artefact is reviewed, understood and tested by a named member; the AI-use log is updated weekly | Remove the AI-assisted content and rewrite it from the primary sources; disclose the change in the log | All | **Active** | 2026-10-28 |
| **R12** | Personal data or identifiable photographs enter the repository | Privacy | L | M | No personal data is collected; only leaf photographs; `.gitignore` excludes raw uploads; a pre-commit secret scan runs in CI | Purge the history with `git filter-repo`, notify the advisor, and record the incident | Bemnet | Open | 2026-11-04 |
| **R13** | Data leakage inflates the reported accuracy and a reviewer detects it | Methodology | M | H | Duplicate grouping before splitting, enforced by tests T-03…T-06 and asserted in CI; the split manifest is committed with a checksum | Re-run all evaluations on the corrected split and restate every number in Chapter 6 | Hayredin | Open | 2026-11-04 |
| **R14** | The literature review is judged "mostly descriptive" rather than critical | Academic | M | M | The chapter is organised by theme with explicit comparison and judgement; the §2.7 gap statement is written to answer the four questions §5.4 requires | Rewrite the weakest two theme sections around the comparison table, which forces comparison | Nahom | Open | 2026-11-04 |
| **R15** | The proposal's High-complexity justification is rejected, so the fourth member is not approved | Governance | M | H | Argue all three limbs — real external data and a real stakeholder, a substantive research challenge with a documented failure phenomenon, and a substantial data-engineering task; engage the advisor before submission | Reduce the declared scope to the three-member minimum and drop the web client. The advisor is consulted *before* the Committee sees it, so the advisor's objection is the one that matters | Nahom + Hayredin | Open | 2026-10-28 |
| **R16** | The advisor is unavailable for more than two weeks | Governance | L | M | Meetings are scheduled fortnightly in advance; the logbook is kept current so a substitute advisor can take over (§13.4) | Request a replacement advisor through the Coordinator within one week | Yohannes | Open | 2026-10-28 |
| **R17** | A published model outperforms the group's model on the internal test set | Technical | M | L | Report the published models under our identical protocol so the comparison is fair; the contribution is the system, the offline deployment and the external evaluation, not the highest internal accuracy | State the comparison openly in Chapter 6 and explain the deployment trade-off | Hayredin | Open | 2026-12-16 |
| **R18** | The container host is unavailable or its free tier expires near the defence | Deployment | M | M | The container is reproducible from the repository; the web client is static and can be hosted anywhere; the mobile app does not depend on the server | Serve the web client as a static bundle from GitHub Pages, pointed at a local API for the demo; or demo from the recorded video | Bemnet | Open | 2027-04-21 |
| **R19** | The three reference phones for the performance evaluation become unavailable | Testing | L | M | Identify the devices in week 19 and keep them on a written loan agreement with the owners; include a device from the department if available | Use emulators for the functional part and report the latency on the subset of devices available, stating which | Hayredin + Bemnet | Open | 2027-03-10 |
| **R20** | The group produces results it cannot explain at the defence | Academic | M | H | The weekly cross-review rotation; every member can explain the whole system; the troubleshooting drill is logged in the decision log; the AI-use log forces named review | Reassign the presentation sections so that each member presents only what they can defend, and use the remaining slots for the results they understand | All | **Active** | 2026-10-28 |

---

## 2. Risk heat map

| | Impact L | Impact M | Impact H |
|---|---|---|---|
| **Probability H** | — | — | **R6** (external accuracy too low) |
| **Probability M** | — | R1, R3, R5, R7, R8, R10, R11, R12, R13, R14, R15, R17 | R2, R4, R18 |
| **Probability L** | — | — | **R9** (demonstration) |

**The two risks that are already active** are R11 (AI disclosure) and R20 (defensibility). Both
are cheap to mitigate now and expensive to fix later. R11 is mitigated by the AI-use log; R20
by the cross-review rotation.

**The highest-impact open risk is R6** — that the model simply does not perform well on field
photographs. The project has already decided how to handle it: report it honestly, ship the
abstention mechanism, and reframe the contribution as the quantified gap plus the mitigation.
Deciding this *now* is what stops it becoming a crisis in week 26.

## 3. Review record

| Date | Reviewer | Changes | Advisor present |
|---|---|---|---|
| 2026-10-21 | Yohannes Berhanu | Register created; R6, R11, R15, R20 flagged | ☐ |
| 2026-10-28 | | | ☐ |
| 2026-11-04 | | | ☐ |
| 2026-12-02 | | | ☐ |
| 2026-12-30 | | | ☐ |
| 2027-01-27 | | | ☐ |
| 2027-02-24 | | | ☐ |
| 2027-03-24 | | | ☐ |
| 2027-04-21 | | | ☐ |
| 2027-05-19 | | | ☐ |

**Guideline §6.3** requires the risk register to be reviewed with the advisor **at least once
a month**. The dates above are monthly. Each review is confirmed by the advisor's initials in
the logbook row for that week.
