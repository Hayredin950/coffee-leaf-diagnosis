# Agronomic Knowledge Base — Content Plan and Source Map

**Owner:** Nahom Solomon (content and sourcing) · **Expert review:** a plant pathologist at the
Ethiopian Institute of Agricultural Research, Jimma Agricultural Research Center (JARC),
Department of Plant Pathology · **Implementation:** Bemnet Tesfaye

> **Requirement FR-35:** each of the five class entries shall contain ten fields — display
> name, scientific name, local names, distinguishing symptoms, severity cues and progression,
> risk factors, organic control, chemical control, prevention, and a source list.
> **Requirement FR-36:** every field stating a chemical or cultural practice shall cite at
> least one peer-reviewed or institutional source. **A CI job fails the build if any practice
> is uncited.**
> **Requirement FR-12:** the result screen displays an advisory notice that the output is
> decision support and does not replace an extension officer.

---

## 1. The source hierarchy

Sources are used in this order of authority. A lower tier is never used when a higher tier
covers the same ground.

| Tier | Source | Use |
|---|---|---|
| 1 | **FAO** — *Coffee: A guide to the principal varieties and their characteristics*, Chapter 9, "Pests and diseases" [61] | The primary international authority for symptom description and control practice for Cercospora leaf spot, coffee leaf rust, black sooty mould and anthracnose |
| 2 | **Peer-reviewed Ethiopian literature** — Berihun & Alemu [56], Yirga [57], Belachew *et al.* [58], Negesa *et al.* [59], Daba *et al.* [60] | Ethiopian-specific epidemiology, cultivar susceptibility, altitude effects and rust management practice |
| 3 | **APS common names** [62] | The authoritative disease-name taxonomy mapping common names to pathogens |
| 4 | **EIAR / JARC** [64] | Cultivar resistance and local agronomic practice |
| 5 | **Published prior art** — Manso *et al.* [11], De Felipe Rendón *et al.* [31] | Corroboration for the symptom descriptions of leaf miner and rust |

**Sources deliberately excluded, and why:**

- **Ethiopian Coffee and Tea Authority** (`ethiocta.gov.et`) — the domain currently serves
  unrelated content and its information pages return 404. **It cannot be cited** because a
  marker cannot open it, and a citation that cannot be verified fails Guideline §11.11.
- **CABI Plantwise Knowledge Bank** — the coffee datasheets return HTTP 403 to every request
  made, so the content could not be verified.
- **Coffee and Tea Research Institute** — no live site; its functions now sit within EIAR/JARC.

---

## 2. The five entries

### 2.1 Coffee Leaf Rust

| Field | Content plan | Primary sources |
|---|---|---|
| Scientific name | *Hemileia vastatrix* | [62], [61] |
| Local names | የቡና ርስት (yebuna rist); "leaf rust", "orange leaf rust" | [56], [57] |
| Symptoms | Pale yellow spots on the **upper** leaf surface, up to about 3 mm; powdery yellow-to-orange pustules on the **underside**, enlarging to about 20 mm; chlorotic halo; premature leaf drop | [61], [56] |
| Severity cues | Progression from spots to pustules to defoliation; assess as the percentage of leaf area affected; the Ethiopian surveys record mean incidence of 35.3 % and severity of 9.09 % | [56], [57], [58] |
| Risk factors | Low altitude (< 1,500 m is the highest-risk band); high humidity and leaf wetness; dense canopies; susceptible cultivars — Catimor is resistant while Java and Typica are susceptible below about 1,000 m | [61], [58], [59] |
| Organic control | Remove and destroy infected leaves and fallen debris; prune for airflow; apply a balanced nitrogen and potassium regime; avoid overhead irrigation; use locally resistant varieties; shade management | [56], [57], [59] |
| Chemical control | Protective fungicides registered locally for coffee leaf rust, applied on the basis of the local extension recommendation and the product label. **Active-ingredient classes only — no product names, no doses.** Copper-based protectants and systemic triazoles are the classes cited in the literature | [56], [57], [61] |
| Prevention | Balanced nutrition; canopy management; resistant varieties; monitoring at the start of the wet season; quarantine of nursery material | [56], [59] |
| Sources | [56], [57], [58], [59], [60], [61], [62] | |

### 2.2 Cercospora Leaf Spot (brown eye spot)

| Field | Content plan | Primary sources |
|---|---|---|
| Scientific name | *Cercospora coffeicola* | [62] |
| Local names | "brown eye spot" (the English common name in Ethiopian extension usage) | [62] |
| Symptoms | Circular brown lesions with a light tan centre and a distinct darker margin — the "eye" appearance; lesions on both leaf surfaces; yellowing and defoliation in heavy infections | [61], [62] |
| Severity cues | Lesion size and density; defoliation of the lower canopy first | [61] |
| Risk factors | High humidity, dense canopy, warm wet conditions, and — importantly — **a relationship with the population of leaf miner, which opens entry points for the fungus** | [61] |
| Organic control | Control leaf miner to reduce infection entry points; canopy and shade management to raise humidity control; remove fallen infected leaves; avoid overhead irrigation | [61] |
| Chemical control | Copper formulations, applied per the local extension recommendation and the product label. **Active-ingredient classes only** | [61] |
| Prevention | Leaf miner control; airflow; balanced nutrition; regular monitoring | [61] |
| Sources | [61], [62], [11] | |

### 2.3 Leaf Miner

| Field | Content plan | Primary sources |
|---|---|---|
| Scientific name | *Leucoptera coffeella* | [62] |
| Local names | "leaf miner"; the American leaf miner | [62], [11] |
| Symptoms | Serpentine or blotch mines in the leaf blade — a pale winding trail or an irregular patch of translucent tissue; a mine is visible on the surface while the larva is inside the leaf; necrosis of the mine as it ages; heavy attack causes leaf drop | [11], [61] |
| Severity cues | The percentage of the leaf area mined; the proportion of leaves on a branch affected | [11] |
| Risk factors | Warm, humid conditions; young flush growth; a dense canopy; the leaf's proximity to the ground | [11], [61] |
| Organic control | Hand-picking and destroying mined leaves on heavily infested branches; prune to encourage a vigorous, well-shaded canopy; maintain plant vigour; conserve the natural enemies of the miner where they are present | [11], [56] |
| Chemical control | Insecticides registered locally for coffee leaf miner, timed to the flush and applied per the local extension recommendation and the product label. **Active-ingredient classes only** | [11], [56] |
| Prevention | Regular monitoring of the flush; canopy management; avoidance of excessive nitrogen that produces soft, attractive growth | [11] |
| Sources | [11], [56], [61], [62] | |

### 2.4 Phoma Leaf Spot (brown leaf spot)

| Field | Content plan | Primary sources |
|---|---|---|
| Scientific name | *Phoma costarricensis* | [62] |
| Local names | "brown leaf spot" | [62] |
| Symptoms | Pale to dark circular necrotic patches on the leaf, often with concentric rings and a dark margin; the affected tissue may drop out, leaving a shot-hole appearance; affects leaves, and in severe cases the berries and the green shoots | [61], [62] |
| Severity cues | Lesion count and the proportion of the canopy affected; the presence of shoot or berry infection raises the urgency | [61] |
| Risk factors | Cool, wet, high-altitude conditions; dense canopy and poor airflow; leaf wetness from rain or overhead irrigation | [61], [58] |
| Organic control | Remove and destroy infected material; prune for airflow; improve drainage; avoid overhead irrigation; apply balanced nutrition | [61] |
| Chemical control | Protective fungicides registered locally for coffee brown leaf spot, applied per the local extension recommendation and the product label. **Active-ingredient classes only** | [61] |
| Prevention | Airflow and canopy management; balanced nutrition; monitoring in cool, wet periods | [61] |
| Sources | [61], [62] | |

### 2.5 Healthy

| Field | Content plan | Primary sources |
|---|---|---|
| Scientific name | — (not applicable) | — |
| Local names | — | — |
| Symptoms | A healthy coffee leaf is uniformly green with intact margins, no necrotic lesions, no chlorotic spots, no powdery pustules on the underside, no serpentine mines, and no shot-holes | [61] |
| Severity cues | Not applicable | — |
| Risk factors | Not applicable. The entry instead carries the **differential-diagnosis note**: the common confusion is between the early chlorotic spots of rust and the pale lesions of Phoma, and between the pale trails of a fresh mine and the pale lesions of Cercospora | [61], [62] |
| Organic control | Not applicable. The entry carries the **general agronomic practice** for a healthy plantation: balanced nutrition, canopy management, regular monitoring and the avoidance of overhead irrigation | [56], [59], [61] |
| Chemical control | Not applicable. **No fungicide or insecticide is recommended on a healthy leaf.** | — |
| Prevention | Regular scouting; sanitation of fallen debris; cultivar selection | [56], [59] |
| Sources | [56], [59], [61], [62] | |

---

## 3. The rules that govern the content

1. **No product names and no dosages.** The chemical control sections name the *active
   ingredient class* and direct the user to a locally registered product, to its label, and to
   the local extension service. This is both a safety decision and an ethics decision: the app
   must not become the source of an incorrect or illegal dosage recommendation.
2. **Every practice carries a citation.** A CI job, `scripts/audit_kb.py`, verifies that every
   class has all ten fields populated and that every practice field carries at least one
   source. A failure breaks the build.
3. **Every entry ends with its sources**, visible in the application, so that a field officer
   can verify the recommendation and an extension officer can follow it up.
4. **The scientific name and the common name are both given**, because the Ethiopian extension
   literature uses several common names and the international literature uses the pathogen
   name.
5. **The advisory notice is on the result screen**, and the knowledge base is advisory too.
6. **The severity cues are qualitative and observational** — what to look for and in what
   order — because the app does not quantify severity. It must not imply that it does.

---

## 4. The JSON schema

```json
{
  "kb_version": "1.0.0",
  "updated_utc": "2027-03-01T00:00:00Z",
  "review": {
    "reviewer": "Plant Pathology Department, Jimma Agricultural Research Center, EIAR",
    "reviewed_utc": "2027-03-10T00:00:00Z",
    "note": "Reviewed for local relevance and for the absence of product-specific advice."
  },
  "classes": [
    {
      "class_key": "coffee_leaf_rust",
      "display_name": "Coffee Leaf Rust",
      "scientific_name": "Hemileia vastatrix",
      "local_names": ["የቡና ርስት", "leaf rust", "orange leaf rust"],
      "symptoms": "...",
      "severity_cues": "...",
      "risk_factors": "...",
      "organic_control": "...",
      "chemical_control": "...",
      "prevention": "...",
      "sources": [
        {
          "citation_key": "[56]",
          "title": "Status of coffee leaf rust (Hemileia vastatrix) and its management in Ethiopia: a review",
          "publisher": "Archives of Phytopathology and Plant Protection",
          "url": "https://doi.org/10.1080/03235408.2023.2168173",
          "accessed_date": "2026-10-21"
        }
      ]
    }
  ]
}
```

The same file is embedded as an application asset and served by the API, so the mobile and web
clients cannot present different guidance. The `kb_version` travels with every diagnosis
record, so a historic diagnosis can always be re-interpreted against the guidance that was
current when it was produced.

---

## 5. The expert review record

**To be completed after the review.**

| Item | Value |
|---|---|
| Reviewer | |
| Institution | |
| Role / position | |
| Date of review | |
| Material reviewed | The draft `knowledge_base.json` v0.9 |
| Outcome | ☐ Accepted  ☐ Accepted with amendments  ☐ Amendments required  ☐ Rejected |
| Amendments requested | |
| Amendments incorporated (date) | |
| Re-review outcome | |
| Evidence retained | This table, plus the reviewer's signed note, in the repository and in the submission package |

**Contact note.** The first approach should be the Department of Plant Pathology at JARC
(EIAR), whose staff appear as authors on the Ethiopian rust literature the group cites
[56], [57], [59]. A request for a 30–45 minute review of five short entries is a small ask and
is well within the normal academic relationship with a local research institute. The group's
proposal argues for exactly this collaboration, so the request is consistent with what has
already been submitted.

---

## 6. Traceability

| Requirement | Implemented by | Tested by | Evidence |
|---|---|---|---|
| FR-11 — the guidance renders for the predicted class | `mobile/lib/kb/resolver.dart`; `api/app/routers/kb.py` | T-27 | The result screen renders all ten fields |
| FR-12 — the advisory notice | The result screen widget | T-28 | Visible without scrolling |
| FR-13 — the knowledge-base browser | The "All Diseases" screen | T-31 | Every class opens |
| FR-25 — the API knowledge-base endpoints | `api/app/routers/kb.py` | T-51 | The schema validates |
| FR-35 — the ten fields per class | `data/knowledge_base.json` | T-27; E-12 | The schema audit |
| FR-36 — every practice is cited | `scripts/audit_kb.py` | T-30; E-12 | The CI job fails on an uncited practice |
| FR-37 — one versioned asset | The embedded asset and the server copy | T-32 | The versions match |
| SO5 | | E-12, E-13, E-14 | The audit, the expert review, the comprehension check |
