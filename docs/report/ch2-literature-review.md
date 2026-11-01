# Chapter 2 — Literature Review and Related Work

> **The chapter itself lives at `docs/literature/ch2-literature-review.md`.**
> This file is a pointer and a formatting checklist, so that the report folder is complete and
> so that whoever formats the report knows exactly what Chapter 2 must contain and how it must
> be laid out.

**Owner:** Nahom Solomon · **Co-owners:** Hayredin Mohammed (§2.2 — the model-accuracy
literature) and Bemnet Tesfaye (§2.4 — the deployment literature) · **Estimated length:**
5–7 pages

---

## Contents

| Section | Title | In `docs/literature/ch2-literature-review.md` |
|---|---|---|
| 2.1 | Datasets for coffee leaf disease recognition, and why the obvious split is wrong | §2.1 |
| 2.2 | Model accuracy on curated imagery: high, consistent, and not comparable | §2.2 |
| 2.3 | On-device deployment: a solved engineering problem that coffee disease has not used | §2.3 |
| 2.4 | Existing coffee leaf disease applications: narrow, cloud-bound, and rarely measured | §2.4 |
| 2.5 | Why curated-image accuracy does not survive the field | §2.5 |
| 2.6 | Agronomic knowledge for treatment guidance | §2.6 |
| 2.7 | **Gap statement** | §2.7 |
| — | How this review shaped the design (the required closing subsection) | The final table |

**The comparison table** is at `docs/literature/comparison-table.md` and becomes **Table 2.1**
(and Tables 2.2 and 2.3). **The reference list** is at `docs/literature/references.md`.

---

## Formatting checklist (Guideline §11)

- [ ] Times New Roman 12 pt, 1.5 line spacing, justified, A4
- [ ] Section headings 13 pt bold; sub-headings 12 pt bold; no heading deeper than the third order
- [ ] The comparison tables are numbered **Table 2.1, 2.2, 2.3**, with the label and caption
      **above** the table
- [ ] Every table is referred to in the text before it appears (§11.6)
- [ ] Every in-text citation is a square-bracketed number matching `references.md`
- [ ] No source is cited that has not been read (§5.4)
- [ ] The review is organised **by theme**, and no section reads as a sequence of one-source
      summaries (§5.4)
- [ ] Each theme ends with a judgement — "what the evidence shows as a whole"
- [ ] The chapter ends with the explicit gap statement, which must answer three questions:
      what existing work does not do, why that matters for the stakeholders named in Chapter 1,
      and how the proposed project responds (§5.4)
- [ ] The closing table shows how the review shaped the design decisions (§5.4's final
      requirement)

---

## The three things an examiner will look for in this chapter

1. **Critical judgement, not description.** For each theme, is there a statement about the
   *quality* of the evidence — small or unrepresentative data, weak evaluation, outdated
   technology, results that cannot be compared (§5.4)? §2.2.2 of the chapter is the model
   answer: the 93–99.78 % spread in the literature is not a meaningful scientific spread, it is
   protocol variation, and treating any of those numbers as a benchmark to beat would be a
   methodological error.

2. **An explicit, defensible gap.** The gap must be specific enough that a reader can check
   whether it is real by looking for a counter-example, and it must be the gap the project
   actually fills. §2.7 of the chapter is written this way, and §2.4 of the comparison table
   is the evidence.

3. **The link from the review to the design.** The closing table maps each piece of evidence
   to the design decision it produced. This is what turns a literature review into a
   methodology rather than a bibliography, and it is directly credited in the rubric under
   "Methodology" and "Analysis and design".
