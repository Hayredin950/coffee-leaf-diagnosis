# Notebooks

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Hayredin950/coffee-leaf-diagnosis/blob/main/notebooks/00-dataset-verification.ipynb)

| File | What it does |
|---|---|
| `00-dataset-verification.ipynb` | Counts every coffee-leaf image **before any preprocessing**, on Colab or Kaggle, and writes a dashboard plus JSON/CSV/Markdown |

The notebook is the executable half of `docs/12-DATASET-VERIFICATION.md`. If the two ever disagree,
**the notebook wins** — it is the one that opened the files.

---

## 1 · Run it in 30 seconds (no data, no account)

1. Open `00-dataset-verification.ipynb` in Colab or Kaggle.
2. **Runtime → Run all** (Colab) or **Run All** (Kaggle).
3. Leave `SETTINGS["download"] = False` in cell 2.

You will see, in order:

```
SELF-TEST PASS  9 synthetic images, 2 layouts, every count matched
11 of 11 records resolved
... dashboard ...
datasets counted   : 0 of 11
Still to open (11): ...
```

That is the **correct** result on a fresh machine. It proves three things before you download a
single byte: the counter is right, every DOI still resolves, and the notebook is honest about what
it does not have.

---

## 2 · The download table

### 2.1 Direct links — no login, no account

These work in a browser and in the notebook.

| Dataset | Link | Size | Notes |
|---|---|---|---|
| **CoffeeLeaf-CO v2** | https://zenodo.org/records/22756170/files/CoffeeLeaf-CO-v2.zip?download=1 | 167.5 MB | Zenodo, CC BY 4.0. `SETTINGS["download"]=True` fetches it automatically. |
| **Ethiopian** | https://www.kaggle.com/datasets/biniyamyoseph/ethiopian-coffee-leaf-disease | 2.12 GB | CC0. 12,000 images, 4 classes. Kaggle account needed to download. |
| **Uganda augmented** | https://www.kaggle.com/datasets/chelangatspecioza/coffeedataset34 | 435 MB | **CC BY-NC-SA 4.0 — non-commercial.** Research ablation only. |
| **JMuBEN (mirror)** | https://www.kaggle.com/datasets/noamaanabdulazeem/jmuben-coffee-dataset | 1.84 GB unpacked | 58,549 files, both JMuBEN and JMuBEN2. Cite Mendeley, not this. |
| **RoCoLe (mirror)** | https://www.kaggle.com/datasets/anitagarg123/coffee-leaves | 2.27 GB | 1,560 JPG + `RoCoLE-csv.csv`. |
| **Silva (mirror)** | https://www.kaggle.com/datasets/alvarole/coffee-leaves-disease | 1.50 GB | 542 JPG + 542 XML, uploaded by the same author. |

### 2.2 Mendeley — a browser login is required

The public API lists every file with its size and SHA-256, but **the bytes need a logged-in
session**. There is no anonymous download URL; every pattern returns 404. Open the page, click
**Download All**, and move the archive into `raw/<key>/`.

| Dataset | Page | Files | Total |
|---|---|---|---|
| **JMuBEN** | https://data.mendeley.com/datasets/t2r6rszp5c/1 | `Cerscospora-…zip` 252.2 MB · `Leaf rust-…zip` 69.5 MB · `Phoma-…zip` 227.5 MB | 549.2 MB |
| **JMuBEN2** | https://data.mendeley.com/datasets/tgv3zb82nd/1 | `Healthy-…zip` 566.9 MB · `Miner-…zip` 724.8 MB | 1,291.7 MB |
| **BRACOL** | https://data.mendeley.com/datasets/yy2k5y8mxg/1 | `BRACOL_coffee_leaf_ images_datasets.zip` 164.5 MB | 164.5 MB |
| **Saposoa, Peru** | https://data.mendeley.com/datasets/mfpxg4y65r/2 | `Coffe Leaf.rar` 3,448.4 MB | 3.45 GB |
| **RoCoLe** | https://data.mendeley.com/datasets/c5yvn32dzg/2 | 1,560 JPG + annotations · `RoCoLe-voc.tar.gz` 697.6 MB | 2.27 GB |
| **Silva 2020** | https://data.mendeley.com/datasets/vfxf4trtcg/5 | `miner_img_xml.zip` 667.6 MB · `rust_xml_image.zip` 828.3 MB | 1.50 GB |
| **Uganda** | https://data.mendeley.com/datasets/k36wnd6knb/1 | 3,322 individual JPG (`1_*.jpg`, `1200_*.jpg`, `2300_*.jpg`) | 25.4 MB |

> **Why `1_`, `1200_`, `2300_`?** The Uganda record encodes the class in the filename prefix:
> `1_` = Healthy (1,179), `1200_` = Rust (1,033), `2300_` = Phoma (1,110). The notebook knows this;
> without it, all 3,322 images would count as `unlabelled`.

### 2.3 Kaggle CLI — one line each

```bash
kaggle datasets download -d biniyamyoseph/ethiopian-coffee-leaf-disease -p raw/ethiopian
kaggle datasets download -d noamaanabdulazeem/jmuben-coffee-dataset      -p raw/jmuben_kaggle
kaggle datasets download -d anitagarg123/coffee-leaves                   -p raw/rocole
kaggle datasets download -d alvarole/coffee-leaves-disease               -p raw/silva
kaggle datasets download -d chelangatspecioza/coffeedataset34            -p raw/uganda_aug
```

The notebook runs these for you when `SETTINGS["download"] = True` and a Kaggle token is present.

---

## 3 · Colab, step by step

1. Upload `00-dataset-verification.ipynb` to https://colab.research.google.com (File → Upload notebook).
2. **Runtime → Change runtime type → CPU.** No GPU is needed.
3. Get a Kaggle token: kaggle.com → click your avatar → **Settings → API → Create New API Token**.
   A `kaggle.json` downloads.
4. In Colab, run cell 2 and set:

   ```python
   SETTINGS["download"] = True
   ```

   When the notebook asks for credentials, upload `kaggle.json`; or paste its contents into
   `SETTINGS["kaggle_json"]`.
5. **Runtime → Run all.**
6. When it finishes, open the **Files** pane on the left:
   `buna-verify/out/` → download `buna-verification.zip`.

For the Mendeley-only sets (JMuBEN, JMuBEN2, BRACOL, Saposoa, Silva, RoCoLe, Uganda), download the
archive in your browser and upload it to `buna-verify/raw/<key>/` with the Files pane, then re-run
from cell 8.

---

## 4 · Kaggle, step by step

1. Create a notebook and upload `00-dataset-verification.ipynb`.
2. **Add Input → Datasets** and add these slugs (the notebook finds them under `/kaggle/input/`):

   ```
   biniyamyoseph/ethiopian-coffee-leaf-disease
   noamaanabdulazeem/jmuben-coffee-dataset
   anitagarg123/coffee-leaves
   alvarole/coffee-leaves-disease
   chelangatspecioza/coffeedataset34
   ```

   No token is needed — mounted inputs are used in place and never copied.
3. **Run All.** Artefacts land in `/kaggle/working/buna-verify/out/` and are saved with the
   notebook when you click **Save Version**.

---

## 5 · Where to put a file you downloaded by hand

```
buna-verify/
├── raw/
│   ├── jmuben/          ← Cerscospora-…zip, Leaf rust-…zip, Phoma-…zip
│   ├── jmuben2/         ← Healthy-…zip, Miner-…zip
│   ├── bracol/          ← BRACOL_coffee_leaf_ images_datasets.zip
│   ├── saposoa/         ← Coffe Leaf.rar
│   ├── rocole/          ← RoCoLe-voc.tar.gz (or the 1,560 JPGs)
│   ├── silva/           ← miner_img_xml.zip, rust_xml_image.zip
│   ├── uganda/          ← the 3,322 JPGs (flat is fine)
│   ├── ethiopian/       ← the Kaggle zip, or the unzipped tree
│   └── uganda_aug/      ← the Kaggle zip, or the unzipped tree
├── extracted/           ← created by the notebook
└── out/                 ← created by the notebook
```

The key must match the registry: `jmuben`, `jmuben2`, `bracol`, `saposoa`, `rocole`, `silva`,
`uganda`, `ethiopian`, `uganda_aug`, `coffeeleaf_co`, `jmuben_kaggle`.

---

## 6 · What you will see

| Section | Output |
|---|---|
| Self-test | `SELF-TEST PASS` — the counter is proven before it is trusted |
| Probe | one line per record, with the HTTP status and the latency |
| Acquire | `local` / `kaggle-input` / `kaggle-download` / `http-download` / `NOT PRESENT` |
| Count | images, unlabelled, number of classes, per dataset |
| Verify | claimed vs observed, delta, `MATCH` / `CLOSE` / `MISMATCH` |
| Hash | SHA-256 of every archive, median/min/max dimensions |
| Dashboard | an HTML table and two PNG charts |
| Verdict | the exact sentences the group is allowed to say |

The dashboard is also written to `out/dashboard.png` and `out/claimed_vs_observed.png`, so it can go
straight into the report or the slides.

---

## 7 · Test it yourself without downloading anything

The self-test in cell 6 is the part to show a sceptical reviewer. It:

1. builds a tree with 9 images across 5 classes and 2 splits,
2. counts it,
3. asserts every number,
4. builds a second, **flat** tree with the Uganda filename convention and asserts the filename rules,
5. deletes both.

If it prints `SELF-TEST PASS`, the counter is correct. If you change `count_tree`, the self-test tells
you immediately whether you broke it.

---

## 8 · Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Every dataset says **NOT PRESENT** | `download = False`, nothing mounted | set `SETTINGS["download"] = True`, or add the Kaggle input |
| `no Kaggle credentials` | Colab has no token | upload `kaggle.json`, or paste it into `SETTINGS["kaggle_json"]` |
| `403` from Kaggle | the dataset licence was never accepted | open the dataset page once while logged in |
| `no unrar/7z available` | Saposoa is a `.rar` | Colab installs `unrar-free`; on Kaggle, unrar locally and upload the tree |
| A class shows as `unlabelled` | labels are in an annotation file, not folder names | add a `filename_rules` entry to that record in the registry cell |
| Count is 3–6 images off | the publisher's table is off | keep the observed count; the delta is the finding |
| `MISMATCH` | the archive is a partial mirror | check `source_kind`; a mirror is not the record |
| Out of memory | `run_phash` on 60k images | run it per dataset, or leave it off |

---

## 9 · What the numbers mean

- **A count is not a quality claim.** 58,549 is a count of files, not of distinct plants.
- **`unlabelled` is a finding.** If 3,894 images arrive with no class labels, the total is verified
  and the per-class split is not.
- **A mirror is not a source.** Cite the Mendeley/Zenodo DOI. Mirrors relabel the licence.
- **Silva is T2, not T1.** Its second release is the same author's own Kaggle upload.
- **The Ethiopian test split is the only Cercospora set we can verify and hold out.** It is CC0,
  self-uploaded, with no paper and no named annotator; its balanced `test/` split reflects curation,
  not random field sampling, so its accuracy is an upper bound.

Full evidence: `docs/12-DATASET-VERIFICATION.md`.
