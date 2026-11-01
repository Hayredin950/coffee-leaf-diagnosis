# Decision Log and Technical Troubleshooting Drill

**Owner:** Yohannes Berhanu (maintains) · **Contributors:** all four
**Purpose:** (1) record the project's significant technical and organisational decisions with
their rationale, so that they are visible to the advisor and the examiners; and (2) provide the
weekly **troubleshooting drill**, which protects the Individual Contribution Factor
(Guideline §17.7: an ICF of 0.80 applies if a student "explains own modules but the
understanding of other parts is limited").

---

## Part A — Decision record

Format: ADR-## | Date | Decision | Rationale | Alternatives rejected | Affects | Status

| ADR | Date | Decision | Rationale | Alternatives rejected | Affects | Status |
|---|---|---|---|---|---|---|
| ADR-001 | 2026-10-21 | Use a **Flutter** mobile client with on-device TFLite inference | One codebase for Android and iOS; the best-supported TFLite plugin; a single language across a four-person team reduces coordination cost | React Native (weaker TFLite support, a second language); native Kotlin (schedule risk) | SO4, SO5, SO6 | Accepted |
| ADR-002 | 2026-10-21 | Build **one model and one knowledge base**, with two front-ends (mobile + web) | Guarantees the app and the web client cannot disagree; the web client serves extension officers and the defense demo | Two separate models or two knowledge bases (divergence risk) | SO4, SO5 | Accepted |
| ADR-003 | 2026-10-21 | Store the **acceptance threshold and the calibration temperature in `metadata.json`**, not in code | A deployed model change cannot leave the application threshold silently stale | Hard-coding the threshold in the Dart code | SO3, SO4 | Accepted |
| ADR-004 | 2026-10-21 | The API **never fetches a URL supplied by a client** | "Predict by URL", used by one prior-art system, is a server-side request forgery vector | Accepting a URL parameter for convenience | Security | Accepted |
| ADR-005 | 2026-10-21 | Treat `Mycena`, red spider mite and weevil as an explicit **`unsupported` label**, never as a disease class | Mapping them would corrupt both the training labels and the external evaluation, and would produce a flattering but false result | Forcing them into the nearest disease class (the standard practice in the literature) | SO1, SO3 | Accepted |
| ADR-006 | 2026-10-21 | **Do not use adversarial domain adaptation** in this project | The comparable benchmark found DANN degraded accuracy to 0.252 and AdaBN to 0.321, both worse than the baseline [15] | DANN, AdaBN, feature moment matching | SO3 | Accepted — excluded by design and documented as a deliberate omission |
| ADR-007 | 2026-10-21 | Build the web client with **no build step** | A build step in the final fortnight before the defense is an unacceptable schedule risk; the OpenAPI schema guarantees the contract | React, Vue, Svelte, Gradio | SO6 | Accepted |
| ADR-008 | 2026-10-21 | Use **PostgreSQL** on the server, **SQLite** on the device | Concurrent writes and `jsonb` on the server; SQL is queryable and auditable on the device | MySQL, MongoDB, a hosted NoSQL service | SO6 | Accepted |
| ADR-009 | 2026-10-21 | The device store is the **source of truth** for the user's history; the server is an optional export target | Removes the need for bidirectional sync and conflict resolution in v1, which is a real scope reduction | Automatic bidirectional sync | SO6 | Accepted |
| ADR-010 | 2026-10-21 | The **knowledge base names active-ingredient classes, never products or dosages** | The app must not become the source of an incorrect or illegal dosage recommendation; the user is directed to the product label and to a local authority | Naming specific products | SO5, Ethics | Accepted |
| ADR-011 | 2026-10-21 | Keep the **five external datasets out of the headline training corpus** | The external evaluation is the project's central contribution; contaminating it would destroy it | Mixing all sources for maximum training data | SO3 | Accepted |
| ADR-012 | 2026-10-21 | Split **before** any learned preprocessing, with duplicate grouping | Guideline §9.3 requires it, and three of the four principal datasets contain duplication structures | A random split (the field's usual practice) | SO1 | Accepted |
| ADR-013 | 2026-10-21 | Report the **macro-F1 and the per-class recall**, not accuracy alone | The corpus is imbalanced (Healthy is 32 %); accuracy would be inflated by the dominant classes | Accuracy alone | SO2, SO3 | Accepted |
| ADR-014 | 2026-10-21 | The API's `/predict` **applies abstention by default**, with an opt-out for the evaluation harness | The server must not present an unconfident class as a diagnosis either | Always returning the raw class | SO3, SO4 | Accepted |
| ADR-015 | 2026-10-21 | Deliver the **Amharic localisation infrastructure** but keep the shipped UI English-only | Shipping unreviewed Amharic text would be worse than shipping none; the translations need a qualified translator | Machine-translating the strings and shipping them | SO5, NFR-15 | Accepted — reported as a limitation |
| ADR-016 | 2026-11-01 | **`08-PRODUCT-VISION.md` is a product document, not the design baseline.** The FYP I design deliverable stays the wireframe set in `docs/design/ui-wireframes.md` (Screens 1–5 plus the web client); any screen in the vision that is not there enters through a change request (Part B) before it is built or reported. | Designing twenty screens at W2 would break the requirement trace that the W13 design review is scored on; writing them down anyway is what stops a W10 argument about a fourth tab from becoming a W12 redesign. | Designing the full set now | Chapter 4, W13 review | Accepted |

---

## Part B — Requirement and scope changes (Guideline §4.6)

> A change is **major** if it alters the problem, the general objective, any specific
> objective, the primary dataset or technology, the group membership or the advisor, or if it
> delays a milestone by more than two weeks. A major change needs a written request endorsed
> by the advisor and approved by the Committee **before** implementation expands.

| Change | Date | Description | Major? | Reason | Effect on scope | Effect on schedule | Effect on testing | Advisor endorsement | Committee decision |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

---

## Part C — Technical troubleshooting drill

**Rule.** Every Friday, each member answers **one question about another member's package**.
The question is asked by the owner of that package, and the answer is recorded here. This is
the cheapest possible insurance against an ICF of 0.80, and it produces a genuine record of
cross-system understanding.

**A question counts as answered** when the answer is given from understanding, not from the
report, and names the specific mechanism.

---

### Week 1

| Answerer | Package | Question | Answer recorded | Adequate? |
|---|---|---|---|---|
| Nahom | Data & model | "What exactly does the 'group' in a grouped split refer to, and why is it not the same as a class?" | | ☐ |
| Bemnet | Data & model | "How does the app know the five class names, and where do they come from?" | | ☐ |
| Yohannes | Data & model | "Why can a random split of JMuBEN give an accuracy that does not transfer to the field?" | | ☐ |
| Hayredin | Mobile app | "What exactly does the app do with an image it cannot classify?" | | ☐ |

### Week 2

| Answerer | Package | Question | Answer recorded | Adequate? |
|---|---|---|---|---|
| Hayredin | Backend | "How does the API reject a file that is not an image, and why is checking the extension not enough?" | | ☐ |
| Nahom | Backend | "What is the API's authentication model and what happens on an unauthenticated request?" | | ☐ |
| Yohannes | Mobile app | "What is stored in the device database, and why is the confidence vector a single column?" | | ☐ |
| Bemnet | Backend | "How does the app decide where the on-device database lives, and what protects it?" | | ☐ |

### Week 3

| Answerer | Package | Question | Answer recorded | Adequate? |
|---|---|---|---|---|
| Bemnet | Research | "What is the gap statement, in one sentence, and why is it not just 'nobody has done this'?" | | ☐ |
| Yohannes | Research | "Why did the group decide not to use adversarial domain adaptation?" | | ☐ |
| Nahom | Mobile app | "How does the low-confidence screen differ from the normal result screen, and why is the class name absent?" | | ☐ |
| Hayredin | Research | "How does the knowledge base get its content, and how is every claim sourced?" | | ☐ |

### Weeks 4–32

*Continue the rotation every week. The pattern above is the template.*

---

## Part D — Advisor meeting minutes (short form)

Every two weeks. The full logbook is in `docs/appendices/Appendix-B-Logbook.md` §Advisor
meeting record.

| # | Date | Present | The three most important decisions | The actions and their owners | The next milestone |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |
| 8 | | | | | |

---

## Part E — Repository governance record

| Item | Convention |
|---|---|
| Branching | `feature/<short-description>` from `develop`; `release/<version>` cut for a release |
| Commit messages | Conventional Commits: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:` — with a short imperative summary |
| Pull requests | One reviewer who is not the author; the reviewer must run the affected tests |
| Issue tracker | One issue per requirement or defect; linked to the requirement ID and the test ID |
| Milestone tags | `proposal`, `requirements`, `design`, `prototype`, `integrated`, `testing`, `report`, `defense` |
| Releases | Tagged with a semver; the model artefact is attached to the release with its checksum |
| Secrets | `.env` is gitignored; `.env.example` is committed; `gitleaks` runs in CI |
| Datasets | Never committed; `data/README.md` carries the download URLs and the checksums |
| AI-assisted code | A header comment: `// AI-assisted (Claude, <date>); reviewed by <name>` |
