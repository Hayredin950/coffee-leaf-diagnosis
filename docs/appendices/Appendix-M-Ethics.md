# Appendix M — Ethical Screening Checklist

**Project:** Design and Development of a Coffee Leaf Disease Diagnosis System Using Deep Learning
**Completed:** 21 October 2026 by Nahom Solomon · **To be reviewed by the advisor and the
Committee as part of the approval gate** (Guideline §4.5, §15.4)

> **Guideline §15.4:** *"Every proposal must complete the ethical screening checklist in
> Appendix M. A project that involves human participants, identifiable personal data, health,
> biometric, financial or education records, minors or other vulnerable people, or confidential
> sponsor data needs the written approval of the advisor and the Committee, and must be referred
> to the college or University ethics review where that review is required."*
>
> **Note:** *"A 'Yes' to any of the first five questions requires the written approval described
> in Section 15.4."* The group answers **Yes** to question 1 (the usability study), so the
> advisor's and the Committee's written approval are required before the usability study runs.

---

## 1. Screening questions

| # | Question | Yes/No | Safeguards and notes |
|---|---|---|---|
| 1 | Does the project involve human participants (surveys, interviews, user tests)? | **YES** | The usability evaluation in SO7 involves 12 participants completing defined tasks and answering the SUS questionnaire (≈15 minutes). **Safeguards:** a plain-language information sheet and an informed-consent form explaining the purpose, the voluntary nature, the right to stop at any time, and that no personal data is collected; a pseudonymous participant code (P01–P12) used throughout; no names, contact details, audio or video recorded without separate explicit consent; sessions run on the participant's own device; the SUS responses stored in a spreadsheet with codes only, on an encrypted device held by Nahom Solomon, and destroyed after the defence unless the participant consents to retention; the results reported only in aggregate, with no participant identifiable. **This triggers the written approval requirement of §15.4 — advisor and Committee approval must be obtained before any session is run.** |
| 2 | Does it collect or process identifiable personal data? | **No** | The application collects only: a leaf photograph, a UTC timestamp, a predicted class, a confidence vector, a model version, and optional free-text notes that the user chooses to type. There are no accounts, no names, no email addresses, no location data, and no device identifiers. The API stores the same fields. The optional `notes` field is the user's own free text and is their responsibility. |
| 3 | Does it use health, biometric, financial or education records? | **No** | The system classifies coffee leaves. No human health data of any kind is processed. |
| 4 | Does it involve minors or other vulnerable people? | **No** | Participants are adults (university students, agriculture students, adult members of local coffee-farming families). No minors are approached or recruited. |
| 5 | Does it use confidential data from a sponsor? | **No** | No sponsor agreement is in place. The group holds an open data-sharing correspondence with the JMuBEN author, which is a public research dataset under CC BY 4.0, not confidential sponsor data. A letter of support from a coffee research centre, if obtained, would be treated as non-confidential and would be disclosed to the advisor. |
| 6 | Does it collect data from websites or third-party platforms? | **Yes** | All nine datasets are downloaded from Mendeley Data, Zenodo and Kaggle, each under CC BY 4.0 (or an explicitly compatible licence). **Safeguards:** the terms of use of each platform are respected; no scraping is performed; no paywalled or login-gated content is accessed; the licence and the citation for each source are recorded in the datasheet; the data is used for non-commercial academic research only; no dataset is redistributed in the repository — a download procedure with URLs is provided instead (NFR-32). The group's own collection is limited to leaf photographs taken by or for the team, with no third-party image scraping. |
| 7 | Does it involve security testing or offensive techniques? | **Yes, scoped** | The API is tested against the OWASP Top 10 using a scanner (OWASP ZAP baseline) **against the group's own staging deployment only**. No external host, no third-party system and no production service is tested. No exploit is published; no malicious software is created or released. No scanning of dependency targets beyond `pip-audit`/`npm audit` against public advisories. This complies with §15.6. |
| 8 | Does it involve hardware with a safety risk? | **No** | Only standard consumer Android phones and a laptop are used. No laboratory electrical work, no soldering, no hazardous materials. |
| 9 | Will project data be sent to an external AI service? | **No** | No image, no user data, no credential and no unreleased report text is entered into any AI service (§15.3). The training data is processed locally on the group's own machines or on free Kaggle notebooks, which are used only for model training on public image data — no personal data is involved. The AI-use log in Appendix L records every AI interaction with its purpose and its verification. |
| 10 | Could the system cause harm or unfair treatment if it fails or is biased? | **Yes** | This is the most important answer on the form, and it is the reason the system has an abstention mechanism. **Safeguards:** (a) the system classifies *plant* leaves, not people, so no individual is denied a service or a benefit — the harm pathway is economic (a farmer acting on a wrong diagnosis), not discriminatory; (b) a confidence-acceptance threshold means the system refuses to give a diagnosis when it is not confident, rather than guessing; (c) the result screen displays an explicit notice that the output is decision support and does not replace an extension officer; (d) the guidance names active-ingredient classes rather than specific products or dosages, and directs the user to the product label and to a local authority; (e) the agronomic knowledge base is reviewed by a plant pathologist from the Ethiopian Institute of Agricultural Research before it ships; (f) the report states the measured external accuracy honestly, including where it is poor, and the model card lists the out-of-scope classes explicitly; (g) no class in the taxonomy maps to a person or a community, so there is no protected-group dimension and therefore no disparate-impact pathway. |

---

## 2. Summary of the safeguards

| Area | Safeguard | Where it is implemented |
|---|---|---|
| **Human participants** | Informed consent, pseudonymous codes, withdrawal at any time, aggregate reporting, destruction of the data after the defence | `docs/requirements/test-plan.md` §8; `docs/appendices/Appendix-G-Contribution.md` (the review record) |
| **Privacy** | No accounts, no PII, no location, no device identifiers; the only user content is a leaf photograph and the user's own optional note | FR-14; `docs/design/database-and-api.md` §A.3 |
| **Data sourcing** | CC BY 4.0 datasets, no scraping, licences and citations recorded, no redistribution of the data | `data/dataset-sources.md`, `data/datasheet.md` |
| **Security testing** | Scoped to the group's own deployment; no offensive artefact is published | `docs/requirements/test-plan.md` §5 |
| **Potential harm** | Abstention, advisory notice, class-level rather than product-level guidance, expert review, honest reporting | FR-09, FR-12, FR-36; `data/knowledge-base.md` |
| **Fairness** | The classification target is a plant condition, so there is no protected-group dimension; no individual is denied a service | §1 of this checklist |
| **AI use** | Disclosed, verified and documented | `docs/appendices/Appendix-L-AI-Disclosure.md` |

---

## 3. Decision

| Role | Name | Outcome | Signature | Date |
|---|---|---|---|---|
| **Advisor** | Surafiel Habib Asefa | ☐ Approved  ☐ Approved with conditions  ☐ Rejected | | |
| **Committee** | | ☐ Approved  ☐ Approved with conditions  ☐ Rejected | | |

### Conditions or notes

<br><br><br><br>

---

## 4. Items to be completed before the usability study runs

- [ ] The advisor has signed above (§15.4 written approval).
- [ ] The Committee has signed above.
- [ ] The information sheet and the consent form are drafted and approved by the advisor.
- [ ] The participant recruitment message names no personal data to be collected.
- [ ] The data-handling plan (where the SUS responses are stored, in what form, and when they
      are destroyed) is written down and shared with the participants.
- [ ] The consent form includes an explicit statement that the results will be published in
      the project report in aggregate.
- [ ] A withdrawal procedure exists: a participant may withdraw at any time, and their data is
      deleted on request without explanation.
