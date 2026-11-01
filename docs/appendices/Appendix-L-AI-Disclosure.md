# Appendix L — Generative-AI Use Disclosure and AI-Use Log

> **Guideline §15.3:** *"Each group must keep a record of significant AI use (tool, version,
> date, purpose) and submit the declaration in Appendix L with every report."*
> **Appendix L template fields:** Tool and version · Dates · Purpose · Where used (section or
> module) · **How the output was checked**.
>
> **Owner:** Nahom Solomon (maintains) · **Every member is individually responsible for their
> own entries.**
>
> **The rule that keeps this group safe:** no AI-generated text or code enters the repository
> or the report unless a named member has **read, understood and tested it**. Every row below
> has a "How the output was checked" cell filled in with something specific and verifiable. If
> you cannot fill that cell, do not use the output.

---

## 1. Declaration (to be signed and submitted with every report)

☐ **We did not use generative-AI tools in this project.** ← *do not tick this one*

☑ **We used generative-AI tools as listed below.**

> We confirm that all AI-assisted text and code was reviewed, understood and tested by us, that
> all references were verified, and that no confidential or personal data was entered into
> public AI services.

| Project title | Design and Development of a Coffee Leaf Disease Diagnosis System Using Deep Learning |
|---|---|
| **Group members** | Yohannes Berhanu (UGR/9440/16) · Hayredin Mohammed (UGR/2361/16) · Bemnet Tesfaye (UGR/3266/16) · Nahom Solomon (UGR/3155/16) |

**Signatures:** ____________________ (Yohannes) _______ (Hayredin) _______ (Bemnet) _______ (Nahom)

**Date:** ____________________

---

## 2. AI-use log

### 2.1 Log entries — Weeks 1–2 (Oct 2026)

| # | Tool and version | Date | Purpose | Where used | How the output was checked | Member |
|---|---|---|---|---|---|---|
| 1 | Claude (Anthropic, claude-sonnet-4.5 family) via OpenCode | Oct 2026 | Brainstorming the project scope, the role split and the roadmap | Planning conversation; `docs/01-ROADMAP.md`, `docs/03-ROLES.md` | Every claim about datasets, papers and prior art was re-verified independently against the publisher, Crossref, the Mendeley API, the Hugging Face API or the GitHub API — see the verification ledger in `docs/literature/references.md`. Three factual errors found in the earlier notes were corrected: the JMuBEN paper title, the inverted Mendeley record mapping, and the BRACOL DOI. | All |
| 2 | Claude via OpenCode | Oct 2026 | Verification research on 9 datasets and ~20 papers; prior-art survey of 14 coffee leaf disease systems | `docs/literature/*`, `data/dataset-sources.md` | Every URL was fetched (HTTP status recorded). Items that could not be fetched are marked "bibliographic only" in the ledger. Numbers attributed to unpublished systems were removed rather than guessed. | Nahom + Hayredin |
| 3 | Claude via OpenCode | Oct 2026 | Drafting the proposal, requirements specification, design documents and the appendix forms | `docs/proposal/Appendix-A-Proposal.md`, `docs/requirements/*`, `docs/design/*`, `docs/appendices/*` | Each document was checked against the Guideline sections it must satisfy, section by section, and each technical claim (targets, constraints, API paths, schema fields) was verified against the guideline or against the requirements specification it derives from. Placeholders are marked `[PENDING]` rather than invented. | Nahom (proposal, requirements) + Yohannes (design) |
| 4 | Claude via OpenCode | Oct 2026 | Drafting the email to the JMuBEN author requesting dataset access | Email body only — Hayredin sends it from his institutional account | Checked against the author's stated conditions (institutional email, citation, non-commercial use, permitted terms). No claim about the dataset's contents was asserted beyond what the Mendeley record states. | Hayredin |
| 5 | Claude via OpenCode | Oct 2026 | Producing the Mermaid source for the architecture, activity, sequence, state, ER and deployment diagrams | `docs/design/architecture.md`, `docs/design/database-and-api.md` | The Mermaid source was rendered and visually checked for syntax errors; the diagrams were checked against the requirements specification for consistency (Guideline §7.5). | Yohannes |

### 2.2 Log entries — Weeks 3+ (to be appended as work proceeds)

> **Copy this row template for every new use.** Do not batch entries at the end of the semester.

| # | Tool and version | Date | Purpose | Where used | How the output was checked | Member |
|---|---|---|---|---|---|---|
| 6 | | | | | | |
| 7 | | | | | | |

---

## 3. Standing rules for the group

### 3.1 What may be used

Per Guideline §15.3, AI tools may be used — **with the advisor's knowledge** — for:
brainstorming, language editing, code assistance, debugging, and finding literature.

**Action required:** inform the advisor at the next meeting that AI tools are in use, show him
this log, and confirm he is comfortable with it. §15.3 says "with the advisor's knowledge", so
the knowledge must be explicit.

### 3.2 What may never be done

| Prohibition | Guideline reference | How the group enforces it |
|---|---|---|
| Presenting AI-generated results or data as real measurements | §15.3 | Every number in Chapter 6 is produced by a script in `training/` and is linked to it in `results.md`. No AI writes a measured value. |
| Citing sources not verified | §15.3 | Every reference has a verification status in `docs/literature/references.md`. Items marked "bibliographic only" may not carry a quoted number until the PDF is read through the university library. |
| Submitting AI-generated code the student does not understand | §15.3, §18.1 | Every AI-assisted code block is reviewed by **another member** before merge, and the review is recorded in the pull request. |
| Substantial AI-generated code without attribution in the code comments | §15.3 | Any AI-assisted code carries a header comment: `// AI-assisted (Claude, <date>); reviewed by <name>.` |
| Entering confidential or personal data into a public AI service | §15.3 | No image from the datasets, no user data, no credentials and no unreleased report text is ever pasted into an AI tool. |
| Using AI during the defence | §15.3 | No AI tool is open or used during the defense. |
| Listing an AI tool as an author | §11.11 | AI tools appear only in this appendix, never in the reference list. |

### 3.3 The submission-day audit

Before the report is submitted, each member answers these individually in writing to Nahom:

1. List every AI tool you personally used, with the date and the purpose.
2. Point to the file and the line where each AI-assisted artifact lives.
3. State the specific check you ran on it, and the result.
4. State whether you could explain every line of it without the tool.
5. Confirm that no confidential or personal data was entered into any AI service.

Any answer that is incomplete means that artifact must be rewritten or removed before
submission.

---

## 4. Where AI assistance is and is not appropriate in this project

| Artifact | AI assistance | Rationale |
|---|---|---|
| Literature search strategy, source discovery | ✅ Allowed and expected | §15.3 explicitly permits "finding literature". The verification is still the student's job. |
| Reading and understanding a paper | ❌ Not substitutable | §5.4: *"a summary produced by an AI tool must not replace reading the source."* |
| Writing the proposal and the report prose | ✅ Allowed for language editing | §15.3 permits "language editing". The argument, the structure and every claim must be the group's own. |
| Inventing a literature synthesis | ❌ Prohibited | A synthesis is an act of judgement. Use AI to check that the themes are covered, not to produce them. |
| Writing code | ✅ Allowed | §15.3 permits "code assistance" and "debugging". It must be reviewed and tested. |
| Choosing the model architecture and the training protocol | ❌ Not substitutable | This is the methodological contribution; the group must be able to justify it. |
| Producing any measured result | ❌ Prohibited | Results come from scripts, never from a tool. |
| Writing the agronomic knowledge base | ⚠️ Allowed as a **draft only** | Every practice must be traced to a source and reviewed by JARC. The AI may suggest phrasing; it may not invent a recommendation. |
| Writing the test cases | ✅ Allowed | But the group must design the test strategy, and the expected results must be derived from the requirements. |

---

## 5. Advisor acknowledgement

I confirm that the group has informed me of its use of AI tools as recorded above, and I am
satisfied with the review and verification process described in Section 3.

**Advisor name:** ______________________________  **Signature:** ________________________  **Date:** ____________
