# Duplication audit — how many distinct images are actually there

**8 November 2026 · Hayredin**

Every number in `docs/12-DATASET-VERIFICATION.md` counts **files**. This document
counts **distinct images**. They are not the same number, and for the dataset the
whole field builds on, they differ by a factor of fifteen.

---

## 1. Method

Two passes over every image in `data/raw/`, run against the **publisher archives**
(Mendeley/Zenodo), not a mirror:

| Pass | What it finds | How |
|---|---|---|
| **Exact** | byte-identical files | MD5 over the whole file |
| **Perceptual** | the same scene re-encoded, re-cropped or re-coloured | 64-bit difference hash (dHash), union-find at Hamming ≤ 4/6/8/12 |

The exact pass is a hard fact: identical MD5 means identical bytes.
The perceptual pass is threshold-dependent and, on this corpus, **over-merges** —
see §6. It is reported as a range, never as a single number.

Reproduce:

```bash
python scripts/audit_duplicates.py --raw data/raw --out data/audit
```

Outputs `data/audit/duplication-report.md` and `.json`.

---

## 2. Headline

| Dataset | Files | Exact unique | Duplicate copies | Share duplicated |
|---|---:|---:|---:|---:|
| JMuBEN + JMuBEN2 | 58,550 | **3,757** | 54,793 | **93.6 %** |
| Uganda (Mendeley) | 3,322 | **1,810** | 1,512 | 45.5 % |
| RoCoLe | 1,560 | **1,493** | 67 | 4.3 % |
| Silva | 542 | **542** | 0 | 0 % |
| BRACOL | 1,747 | **1,746** | 1 | 0.1 % |

The headline corpus is not 58,549 distinct images. It is **3,757**, and one class
contributes almost none of them.

---

## 3. JMuBEN — the finding that matters

| Class | Files | Exact unique | Copies per image (typical) |
|---|---:|---:|---:|
| Leaf rust | 8,336 | **1,042** | 8 |
| Cercospora | 7,681 | **322** | 24 |
| Phoma | 6,571 | **691** | 10 |
| Healthy | 18,984 | **63** | 300 |
| Miner | 16,978 | **1,639** | 8–16 |
| **Total** | **58,550** | **3,757** | — |

Three independent proofs, in increasing strength:

1. `1 (1).jpg`, `2 (1).jpg` and `10 (1).jpg` are byte-identical (same MD5 and SHA-256).
2. The same holds when the files are read **straight out of the publisher's inner zip**
   (`unzip -p Healthy-….zip Healthy/1\ (1).jpg | md5sum`), so it is not an extraction artefact.
3. Visual: `data/figures/jmuben-healthy-63.png` shows all 63 distinct "Healthy"
   images. They are frames of **one leaf**, differing only in white balance.

Visually, the 63 healthy images appear to be frames of a single leaf: the vein
pattern is identical and only the colour balance moves. The file count is roughly
300× the scene count. This is a visual judgement from the montage, not a
provenance claim.

For the other four classes the distinct images are genuinely varied — the 16-image
sample in `data/figures/jmuben-unique-sample.png` shows different leaves and
different lesions. The duplication there is a copy artefact, not a single scene.

**Consequence:** a random split of JMuBEN puts the same image in train and test
eight to three hundred times. Any accuracy number computed that way is a
memorisation score, not a generalisation score. This is the mechanism behind the
published 1.9 % external rust recall (`ConnorLee08/coffee-leaf-efficientnet-b2`,
16/847) sitting next to 99 % in-dataset accuracy.

---

## 4. Uganda — duplication plus broken files

| Class | Files | Unique | Zero-byte |
|---|---:|---:|---:|
| Healthy | 1,179 | 739 | 100 |
| Leaf rust | 1,033 | 617 | 2 |
| Phoma | 1,110 | 454 | 0 |
| **Total** | **3,322** | **1,810** | **102** |

Two separate defects:

- **102 files are zero bytes.** The outer archive passes CRC, so this is a publisher
  defect, not a bad download. They must be dropped before any split, or they become
  a phantom "class" of unreadable images.
- **1,512 exact duplicate copies** (45.5 %). The largest single group is 100 identical
  files in Healthy.

Uganda remains the most valuable external set — African, field-collected, different
camera — but it is **1,810 usable images, not 3,322**.

---

## 5. RoCoLe — a leakage trap, not a duplicate problem

1,560 files → 1,493 unique. Only 67 duplicates, but they matter:

```
C11P19E1.jpg == C12P28E1.jpg
C12P34E1.jpg == C11P24E1.jpg
C11P24H1.jpg == C12P34H1.jpg
C12P36E1.jpg == C11P23E1.jpg
```

The same photograph appears under **two different plant IDs**. RoCoLe's protocol is
390 plants × 4 views, and we split by plant to avoid leakage — but a plant-level
split still puts one copy in train and the other in test. Deduplicate by hash
**before** assigning plants to folds.

Silva is clean: 542 files, 542 unique, no unreadable files.

---

## 6. Limitation — the perceptual pass over-merges

dHash at Hamming ≤ 8 collapses BRACOL's 1,747 **known-distinct** leaves into 429
clusters. BRACOL is 1,747 different leaves; the method is merging leaves that
merely look alike. So:

- The exact counts in §2–§5 are facts.
- The perceptual counts are a **floor**, not an estimate. Quote them as
  "at most N at threshold t", or not at all.
- The defensible claim is the exact one: **58,550 files, 3,757 distinct images**.

Calibrating the perceptual threshold against BRACOL (where every image is a
different leaf) is future work for the report's limitations section.

---

## 7. What changes in the project

| Item | Before | After |
|---|---|---|
| Headline training corpus | "58,549 images" | **3,757 distinct images** (58,550 files) |
| Split rule | stratified random, grouped by plant where available | **group by MD5 first**, then stratify; a hash is one group |
| Healthy class | 18,983 images | **62 usable distinct images** — report it, do not hide it |
| Uganda | 3,322 | **1,810 usable** after dropping 102 zero-byte files |
| RoCoLe | 1,560 | **1,493 distinct**, and dedup before the plant split |
| Any in-dataset accuracy | quoted as-is | must be labelled *"deduplicated split"* or it is not comparable |

**Grouping is not enough for training.** `scripts/prepare_data.py` already keeps duplicate hashes in
one split (test T-03), which prevents leakage. But training on 18,921 copies of one image still
weights that image 300× in the loss. The training loader should keep **one file per MD5** and use the
duplicates only for the leakage audit. Dedup for training, group for splitting.

Two consequences for the report:

1. **§3 methodology** must state the effective N, not the file count. This is the
   single most defensible number in the whole project.
2. **§2 literature review** can now say something no other FYP says: the field's
   primary benchmark is 93.6 % duplicate at the byte level, and its Healthy class is
   one leaf. That is a contribution, and it is the reason our external evaluation
   matters.

---

## 8. Open items

- **BRACOL is complete now, but not from Mendeley.** The publisher's archive is truncated
  (1,402 of 1,747 images; SHA-256 matches Mendeley's own manifest, so the file is broken at the
  source, not in transit). The missing 345 images were restored from the Hugging Face mirror
  `luisangelico/bracol`, whose `images/1.jpg` and `dataset.csv` are byte-identical to the Mendeley
  release. BRACOL is now 1,747 files, 1,746 distinct, all decodable.
- JMuBEN's `Healthy/2 (691).jpg` is corrupt in the publisher archive (36,531 bytes,
  no decodable frame). Drop it; it is 1 of 63.
- Decide whether the headline model trains on 3,757 distinct images or on a
  capped, balanced subset. 62 healthy images cannot support a 5-class model
  without augmentation — which is exactly the point the ablation should make.
