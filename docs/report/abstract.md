# Abstract

> **Guideline §11.2:** the abstract must be **200 to 300 words** with keywords.
> **Owner:** Nahom Solomon · **Finalise:** FYP II week 25, after the numbers are in.
>
> ⚠️ **The bracketed values must be replaced with the measured results.** Do not write an
> abstract that overstates the system. The reviewers read the abstract and then check the
> numbers in Chapter 6.

---

## Draft (structure fixed; fill the numbers in week 25)

Coffee leaf disease — principally coffee leaf rust, Cercospora leaf spot, leaf miner and Phoma
leaf spot — is a major constraint on Ethiopian coffee production, and it is detected late
because agronomic services are concentrated far from the farms that need them. Automated
coffee leaf disease classifiers report in-domain accuracies in the mid- to high-90 % range, but
those figures are measured on curated imagery: when such models are tested on real field
photographs their accuracy can collapse, and their confidence does not fall with it. This
project addresses both the deployment gap and the evaluation gap. It presents a complete,
**fully offline** Android application that classifies five coffee leaf conditions on a
low-cost phone using a quantised TensorFlow Lite model, resolves the prediction against a
versioned, cited agronomic knowledge base, and records every diagnosis in a local,
searchable database. The model is trained on a **leakage-safe** corpus of nine independently
licensed public datasets spanning six countries and two *Coffea* species; because three of
the principal datasets contain near-duplicate structures, images are grouped by perceptual
hash and by source identity **before** the split, and four automated invariants assert that
no duplicate, cluster or group spans a partition. The central evaluation measures the
internal-to-external generalisation gap across five held-out field datasets, reports
per-class recall, and applies temperature scaling with an explicit acceptance threshold so
that the system abstains rather than guessing when it is not confident. On the internal test
split the model achieves **[macro-F1]**, against a majority-class baseline of **[value]**; on
the external field datasets it achieves **[macro-F1]**, a gap of **[value]** macro-F1 points.
The deployed artefact is **[size] MB** with a median inference latency of **[value] ms** on a
low-cost reference device, and all core functions were verified in airplane mode. A usability
study with **[n]** participants produced a System Usability Scale score of **[value]**. The
paper reports the generalisation gap as its central finding rather than concealing it, and
proposes that the deployment of an offline, abstaining diagnostic assistant is a more
defensible contribution than a further improvement in curated-image accuracy.

**Keywords:** coffee leaf disease; deep learning; on-device inference; TensorFlow Lite;
domain shift; data leakage; mobile application; precision agriculture; Ethiopia.

---

## Word-count check

The final abstract must be between 200 and 300 words. The draft above is approximately 285
words with the placeholders; after the numbers are inserted, recount and adjust if necessary.

---

## Checklist before submission

- [ ] Between 200 and 300 words
- [ ] Five to seven keywords, comma-separated, in sentence case
- [ ] Every number matches Chapter 6 exactly
- [ ] No claim is stronger than the evidence supports
- [ ] The gap and the honest result are both present — an abstract that only reports the
      internal accuracy would misrepresent the work
- [ ] It matches the abstract in the final report
