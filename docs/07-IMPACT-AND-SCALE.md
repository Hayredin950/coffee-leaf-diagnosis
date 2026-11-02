# Impact, Scale and Awards — Why This Is Not Just a Class Project

**What this file answers.** *What does this actually add to Ethiopia and to the world, and what would it
take to win something with it?* It is the file to read before writing Chapter 1, before the proposal's
significance section, and before any competition application.

**Rule for every number in this file.** A figure either has a source, or it carries `⟦VERIFY⟧` and may
not be quoted until someone opens the source. §9 is the ledger.

---

## 1. The problem, in numbers

### Ethiopia's stake in coffee

| Fact | Value | Source |
|---|---|---|
| Farmers directly engaged in coffee production | **≈ 5.9 million** | UNIDO, *Ethiopia Coffee Value Chain Analysis 2025* |
| Coffee export revenue, 2024/25 | **≈ US$2.89 billion**, ~7.43 million 60-kg bags | Daily Coffee News, Jun 2026 (reporting USDA/UNIDO figures) |
| Forecast production, 2026/27 | **≈ 12.1 million bags** (11.6 million in 2025/26) | UNIDO 2025 |
| Rank | **Africa's largest producer**; 5th in the world (496,200 t in 2022) | FAO |
| Share of government revenue from coffee exports | ≈ 10 % `⟦VERIFY⟧` — the figure is dated | — |
| Share of coffee consumed domestically | ≈ 50 % | older sources `⟦VERIFY⟧` |

**The point of the table:** this is not a niche crop. A one-percent improvement in disease response
timing touches tens of thousands of households.

### What disease actually costs

| Fact | Value | Source |
|---|---|---|
| Mean coffee leaf rust **incidence** in Ethiopia | **35.3 %** | Belachew *et al.* 2020, *Trop. Plant Pathol.* 45(5) — our ref [58] |
| Mean rust **severity** | **9.09 %** | same |
| Projected yield loss from climate-related abiotic stress by 2060 | **up to 70 %** | Tadesse, Tesfaye & Abera 2020, *Cogent Food & Agric.* |
| Classes that matter to a smallholder | Rust, Cercospora, Phoma, leaf miner, healthy | JMuBEN taxonomy |

**Incidence of 35 % with severity of 9 % is the shape of the problem.** A third of the plants carry rust;
most of them are not yet badly damaged. That is precisely the window in which a diagnosis changes the
outcome — and precisely the window in which a farmer without an extension officer does not act, because
the leaf "looks a bit off" and there is nobody to ask.

### Why the existing channel does not close it

1. **The extension visit is periodic and travel-bound.** The decision window for rust is days, not weeks.
2. **The knowledge exists and is not the bottleneck.** EIAR, JARC, FAO and APS all publish what to do.
   The bottleneck is *identification at the moment of noticing*.
3. **No public dataset contains an Ethiopian field photograph.** Verified 21 Oct 2026 across eight
   corpora and six countries. This is the single largest limitation of the project — and, see §4, the
   single largest opportunity in it.

---

## 2. What we are actually building, in one sentence

> A phone application that tells a farmer what is wrong with a coffee leaf **and how much to trust that
> answer**, works with the radio off, and turns every correction the farmer makes into the field data
> that does not exist.

The classifier is the easy half. The instrument is the contribution.

---

## 3. What this adds to Ethiopia — five layers, each measurable

| Layer | What the farmer gets | Why it changes behaviour | Measured by |
|---|---|---|---|
| **1. An honest answer** | "Rust" or "rust **or** Cercospora — check the underside" | A set with a coverage guarantee, not a number that looks confident | Empirical coverage ≥ `1 − α` on a held-out external set |
| **2. An actionable answer** | "That photo was too dark — retake" vs "the leaf itself is ambiguous — ask an officer" | The two failures need opposite actions; today both look like "the app is broken" | ≥ 80 % correct attribution on 30 + 30 images |
| **3. A verifiable answer** | Five confirmed field photos of the same disease | Visual proof the farmer can falsify in one second | Top-5 class-consistent ≥ 70 % |
| **4. An accountable answer** | "On your farm: 17 of 20 confirmed correct" | The app reports its own accuracy on *that* farm, not a paper's accuracy | Scorecard arithmetic correct on a scripted scenario |
| **5. The missing data** | Nothing directly — this one is for the country | Confirmed field labels are the asset no Ethiopian institution currently has | Packet round-trips; ≥ 200 confirmations across ≥ 20 farms in FYP II |

**Layers 1–4 are why a farmer keeps the app. Layer 5 is why an institution funds it.**

### The honest impact arithmetic

Not a claim — a model, with its assumptions visible, so anyone can attack it:

```
5.9 million coffee-farming households
  × 1 % reach            = 59,000 households
  × 20 diagnoses/year    = 1.18 million diagnoses/year
  × 1 in 5 changing a    = 236,000 decisions changed
    treatment decision
```

Every step is an assumption and every one is arguable. **The defensible claim is not the arithmetic — it
is that the system can measure its own hit rate**, which almost no agricultural app can. Say it that
way: *"we do not know the impact; we built the instrument that will tell us."*

---

## 4. What this adds to the world — the research contribution

Four things, in the order a reviewer would rank them:

1. **A measured internal→external generalisation gap for coffee leaf disease, per class, across five
   external corpora and two *Coffea* species.** The public record has accuracy claims; it does not have
   this table.
2. **A conformal prediction layer for a plant-disease classifier**, with reported coverage and set size.
   Conformal prediction is standard in ML; it is essentially absent from the agricultural deployment
   literature, and absent from every public coffee project we examined.
3. **An uncertainty attribution method** that separates input-quality failure from class ambiguity using
   test-time augmentation disagreement — cheap, offline, and evaluable on 60 images.
4. **A leakage-audited, reproducible split protocol** with executable invariants, for a corpus whose
   publishers already augmented it and did not release the originals. `scripts/prepare_data.py` runs and
   passes; the public projects do not ship this.

**And one public good:** the field-truth corpus. If FYP II produces a few hundred confirmed Ethiopian
field images with consent, that is a dataset no institution currently holds, and it is the thing that
makes the *next* project possible.

---

## 5. The standards test — "award by all measurements"

The most credible way to prove a project is not ordinary is to hold it against a published standard and
show the gaps. The **Digital Public Goods Standard** (DPGA, 9 indicators) is the right one: it is the
standard used by UN agencies, and it is checkable.

| # | DPG indicator | Our position today | What we must add |
|---|---|---|---|
| 1 | **SDG relevance** | Direct: SDG 1 (poverty), 2 (zero hunger), 8 (decent work), 9 (innovation), 12 (responsible production), 15 (life on land) | One paragraph per SDG in the proposal, with the mechanism, not the slogan |
| 2 | **Open licensing** | Datasets CC BY 4.0; our code licence **not chosen** (open decision O-08) | Pick a licence in W13 — MIT or Apache-2.0 for code, CC BY-SA 4.0 for content |
| 3 | **Clear ownership** | Four named authors, one repo owner | A `GOVERNANCE.md`: who owns what, who merges, how decisions are made |
| 4 | **Platform independence** | Android APK + a documented API; no vendor lock | Document the build; no proprietary dependency in the inference path |
| 5 | **Documentation** | Strong in the repo; **no user guide or installation guide yet** | Both, in FYP II; they are already on the submission checklist |
| 6 | **Mechanism for extracting data** | ★4 export packet; CSV export | Make the export format documented and schema-versioned |
| 7 | **Privacy and applicable laws** | No personal data; nothing leaves the device without an explicit action | An Ethiopian data-protection statement; cite the relevant proclamation `⟦VERIFY⟧` |
| 8 | **Standards and best practices** | IEEE citations; ISO-style requirement IDs; semantic versioning | Say which standards explicitly, in one table |
| 9A/9B/9C | **Data privacy, illegal content, harassment** | Not applicable to leaf images — **say so, with the reasoning** | A short "not applicable, and here is why" section; silence reads as an omission |

**Honest status: we meet roughly 5 of 9 today.** That is a good position for FYP I, and it gives FYP II
a concrete, externally-defined checklist instead of a vague ambition.

---

## 6. What "winning" would require — the criteria, not the competitions

Juries and panels across every programme we looked at score roughly the same six things. This is the
useful abstraction, because specific calls change every year.

| Criterion | What it means | Where we stand | What to do |
|---|---|---|---|
| **Problem significance** | Is the problem large, real, and locally grounded? | **Strong** — 5.9 M farmers, 35 % rust incidence, cited | Lead with two numbers, never five |
| **Novelty** | Is this different from what exists? | **Strong if ★1–★5 land; weak if we lead with the classifier** | The §9 answer in `06-DIFFERENTIATION.md` |
| **Evidence** | Is there a measurement, or an assertion? | **This is the whole bet** — every ★ has a pass condition | Report the negative results too |
| **Feasibility** | Can this team actually deliver it? | **Strong** — a tested pipeline, a plan with dates | Show `AUDIT PASSED`, show the plan |
| **Sustainability / scale** | Does it survive the team graduating? | **Weak today** — no partner, no licence, no governance | JARC partnership letter; DPG alignment; a named maintainer |
| **Human-centredness** | Was a real user involved? | **Weak today** — no user study until FYP II | The FYP II usability study is not optional for an award |

**The honest read:** we are strong on problem, novelty and feasibility, and weak on sustainability and
user evidence. Those two are exactly what separates "good FYP" from "award". They are also both fixable
with one letter and one study.

### Where to compete, in order of fit

| Category | Examples | Fit | When |
|---|---|---|---|
| **Department / university FYP award** | AAU CS best FYP | **Highest** — same document, same defense | W14 |
| **National innovation challenge** | Ministry of Innovation and Technology programmes; university innovation weeks `⟦VERIFY current cycle⟧` | High — local problem, local team | FYP II |
| **International student agritech / AI challenges** | MIT Solve (Climate, Economic Prosperity, Youth Innovation tracks); AI-for-Good style programmes | Medium-high — needs the impact story and a partner | After FYP II |
| **Open-source / digital public good recognition** | DPGA registry | Medium — a credential, not a prize | After the licence and governance exist |
| **Research publication** | A conference or journal paper on the generalisation gap + conformal layer | Medium — needs the FYP II results | After FYP II |

**Never enter a competition before the evidence exists.** A submission with a promise and no measurement
is the fastest way to lose, and it spends the credibility we need later.

---

## 7. The 12-month arc

| When | Milestone | What it unlocks |
|---|---|---|
| W4 (Nov 2026) | Proposal approved with ★1–★5 in the novelty section | The frame everything else is judged in |
| W11 (Jan 2027) | Phone diagnoses a leaf with the radio off | The demo exists |
| W13 (Jan 2027) | Design review with the ★ pass conditions frozen | Nothing can be hand-waved later |
| W14 (Jan 2027) | FYP I defense | Department award eligibility |
| FYP II | Model trained, quantised, evaluated on 5 external sets; ★1–★5 measured | The evidence |
| FYP II | Usability study (SUS) with farmers and extension officers | The human evidence |
| FYP II | JARC review of the knowledge base | Institutional credibility |
| After | 200+ confirmed field records from 20+ farms | **The Ethiopian field dataset** |
| After | Licence + governance + user guide → DPGA nomination | Public-good status |
| After | One paper: generalisation gap + conformal layer | Academic credibility |

---

## 8. What could kill this — stated before anyone asks

| Risk | Why it is real | Mitigation |
|---|---|---|
| **No Ethiopian field data, so the claim stays conditional** | No public corpus exists | ★4 is the route; scope every claim to "built for", never "validated on" |
| **The model is good in-domain and poor in the field** | Published evidence: 1.9 % external rust recall | That *is* the finding. Report it, and let ★1/★2 do the work |
| **No partner, so it dies when we graduate** | Four students, no institution | JARC letter in W5; a named maintainer and a governance file |
| **We build five features and measure none** | The classic FYP failure | Every ★ has a pass condition and a fallback; a fallback that is reported still counts |
| **The demo works and the document does not** | The panel marks the document | Documentation discipline from the repo, merged in W3 |
| **Overclaiming impact** | Tempting, and fatal to credibility | The §3 arithmetic model, with assumptions visible |

---

## 9. Verification ledger

| Figure | Status | Action |
|---|---|---|
| 5.9 M coffee farmers | ✔ UNIDO 2025 | Cite UNIDO, not Wikipedia |
| US$2.89 bn / 7.43 M bags, 2024/25 | ✔ Daily Coffee News, Jun 2026 | Cite the underlying USDA/UNIDO report |
| 12.1 M bags, 2026/27 | ✔ UNIDO 2025 | — |
| 496,200 t (2022), 5th world / 1st Africa | ✔ FAO | — |
| 35.3 % incidence / 9.09 % severity | ✔ Belachew *et al.* 2020 — ref [58] | Confirm page numbers at the W5 library pass |
| Up to 70 % yield loss by 2060 | ✔ Tadesse et al. 2020 | — |
| ≈10 % of government revenue | `⟦VERIFY⟧` dated | Find a current source or drop it |
| ≈50 % domestic consumption | `⟦VERIFY⟧` dated | Find a current source or drop it |
| Ethiopian data-protection proclamation | `⟦VERIFY⟧` | Name the instrument before citing it |
| DPG 9 indicators | ✔ digitalpublicgoods.net, fetched Nov 2026 | — |
| National innovation programme names | `⟦VERIFY⟧` | Check the current cycle before naming one in public |

---

## 10. The five numbers for one slide

If everything else is cut, these five survive:

1. **5.9 million** coffee-farming households.
2. **35 %** of plants carry rust — and most are not yet badly damaged.
3. **1.9 %** — the external rust recall a published offline model achieves.
4. **0** Ethiopian field images in any public corpus.
5. **200** confirmed field records — what we will have that no one else does.

Numbers 1–2 say why it matters. Number 3 says why the obvious solution fails. Numbers 4–5 say what we
add that is genuinely new.
