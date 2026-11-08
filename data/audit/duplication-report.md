# Duplication audit

Exact duplicates are byte-identical files (MD5). Perceptual clusters use a 64-bit dHash with a Hamming threshold; the exact count is a hard fact, the perceptual count is threshold-dependent.

Zero-byte files and files that cannot be decoded are counted as unreadable and excluded from the distinct count.

| Dataset | Class | Files | Exact unique | Duplicate copies | d<=4 | d<=6 | d<=8 | d<=12 | Unreadable |
|---|---|---|---|---|---|---|---|---|---|
| bracol | coffee-datasets | 1,747 | 1,746 | 1 | 1,383 | 871 | 429 | 42 | 0 |
| jmuben | Cerscospora | 7,681 | 322 | 7,359 | 78 | 77 | 76 | 65 | 0 |
| jmuben | Leaf rust | 8,336 | 1,042 | 7,294 | 456 | 404 | 339 | 233 | 0 |
| jmuben | Phoma | 6,571 | 691 | 5,880 | 176 | 173 | 166 | 148 | 0 |
| jmuben2 | Healthy | 18,984 | 63 | 18,921 | 11 | 11 | 11 | 10 | 1 |
| jmuben2 | Miner | 16,978 | 1,639 | 15,339 | 311 | 297 | 279 | 228 | 0 |
| rocole | RoCoLe A robusta coffee leaf images dataset | 1,560 | 1,493 | 67 | 1,474 | 1,459 | 1,451 | 1,438 | 0 |
| silva | miner_img_xml | 257 | 257 | 0 | 257 | 256 | 247 | 109 | 0 |
| silva | rust_xml_image | 285 | 285 | 0 | 284 | 276 | 244 | 113 | 0 |
| uganda | Health leaves | 1,179 | 739 | 440 | 721 | 710 | 685 | 600 | 100 |
| uganda | leaf rust | 1,033 | 617 | 416 | 592 | 582 | 568 | 507 | 2 |
| uganda | phoma | 1,110 | 454 | 656 | 446 | 435 | 412 | 337 | 0 |

## Totals

- files: **65,721**
- exact-unique: **9,348**
- duplicate copies: **56,373** (85.8%)
- perceptual clusters (d<=4): **6,189**
- perceptual clusters (d<=6): **5,551**
- perceptual clusters (d<=8): **4,907**
- perceptual clusters (d<=12): **3,830**

## Largest duplicate groups

- **jmuben2/Healthy**: 520 identical files, e.g. `Healthy-20210326T083815Z-001/Healthy/2 (907).jpg, Healthy-20210326T083815Z-001/Healthy/1 (4206).jpg, Healthy-20210326T083815Z-001/Healthy/10 (933).jpg`
- **jmuben2/Miner**: 80 identical files, e.g. `Miner-20210326T082341Z-001/Miner/1 (8258).jpg, Miner-20210326T082341Z-001/Miner/1 (16358).jpg, Miner-20210326T082341Z-001/Miner/1 (14626).jpg`
- **jmuben/Cerscospora**: 24 identical files, e.g. `Cerscospora-20210326T085017Z-001/Cerscospora/9 (3755).jpg, Cerscospora-20210326T085017Z-001/Cerscospora/6 (183).jpg, Cerscospora-20210326T085017Z-001/Cerscospora/6 (199).jpg`
- **uganda/phoma**: 24 identical files, e.g. `A Machine  Learning Dataset for Classification of Common Coffee Leaf Diseases in Uganda/coffee dataset/phoma/2300_383.jpg, A Machine  Learning Dataset for Classification of Common Coffee Leaf Diseases in Uganda/coffee dataset/phoma/2300_654.jpg, A Machine  Learning Dataset for Classification of Common Coffee Leaf Diseases in Uganda/coffee dataset/phoma/2300_327.jpg`
- **uganda/leaf rust**: 15 identical files, e.g. `A Machine  Learning Dataset for Classification of Common Coffee Leaf Diseases in Uganda/coffee dataset/leaf rust/1200_72.jpg, A Machine  Learning Dataset for Classification of Common Coffee Leaf Diseases in Uganda/coffee dataset/leaf rust/1200_19.jpg, A Machine  Learning Dataset for Classification of Common Coffee Leaf Diseases in Uganda/coffee dataset/leaf rust/1200_90.jpg`
