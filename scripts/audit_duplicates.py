#!/usr/bin/env python3
"""Exact-duplicate and near-duplicate audit of every dataset under `data/raw`.

The point of this script is the number nobody publishes: **how many distinct
images does a dataset actually contain?** A published total counts files. Files
can be byte-identical copies of each other, and a benchmark that reports 58,549
images may hold far fewer distinct scenes.

Two passes per class folder:

    1. exact      - MD5 over the whole file; identical bytes are identical images
    2. perceptual - 64-bit difference hash (dHash), union-find at a Hamming
                    threshold; catches the same scene re-encoded or re-cropped

The exact pass is a hard fact. The perceptual pass depends on the threshold, so
the report always prints a range (d<=4, 6, 8, 12) rather than one number.

Usage
-----
    python scripts/audit_duplicates.py --raw data/raw --out data/audit
    python scripts/audit_duplicates.py --raw data/raw --threshold 8 --no-png

Outputs
-------
    <out>/duplication-report.md
    <out>/duplication-report.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image

IMG_EXT = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp"}
THRESHOLDS = (4, 6, 8, 12)


def md5(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(chunk), b""):
            h.update(block)
    return h.hexdigest()


def dhash(path: Path, size: int = 8) -> int:
    with Image.open(path) as im:
        im = im.convert("L").resize((size + 1, size), Image.LANCZOS)
        px = list(im.getdata())
    bits = 0
    for row in range(size):
        base = row * (size + 1)
        for col in range(size):
            bits = (bits << 1) | (px[base + col] > px[base + col + 1])
    return bits


def cluster_count(hashes: list[int], threshold: int) -> int:
    """Union-find over Hamming distance."""
    parent = list(range(len(hashes)))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(len(hashes)):
        hi = hashes[i]
        for j in range(i + 1, len(hashes)):
            if (hi ^ hashes[j]).bit_count() <= threshold:
                a, b = find(i), find(j)
                if a != b:
                    parent[a] = b
    return len({find(i) for i in range(len(hashes))})


@dataclass
class ClassResult:
    dataset: str
    label: str
    files: int = 0
    exact_unique: int = 0
    perceptual: dict[int, int] = field(default_factory=dict)
    unreadable: list[str] = field(default_factory=list)
    largest_group: int = 0
    largest_group_example: list[str] = field(default_factory=list)

    @property
    def extra(self) -> int:
        return self.files - self.exact_unique


def class_label(path: Path, root: Path) -> str:
    """Deepest folder that is not just a wrapper name."""
    parts = list(path.relative_to(root).parts[:-1])
    generic = {"images", "image", "photos", "data", "dataset", "datasets", "leaf", "crop"}
    for part in reversed(parts):
        if part.lower() not in generic:
            return part
    return parts[-1] if parts else "all"


def audit_dataset(dataset_dir: Path, thresholds: tuple[int, ...]) -> list[ClassResult]:
    images = [p for p in dataset_dir.rglob("*") if p.suffix.lower() in IMG_EXT]
    buckets: dict[str, list[Path]] = defaultdict(list)
    for p in images:
        buckets[class_label(p, dataset_dir)].append(p)

    results = []
    for label, files in sorted(buckets.items()):
        res = ClassResult(dataset=dataset_dir.name, label=label, files=len(files))
        by_hash: dict[str, list[str]] = defaultdict(list)
        for p in files:
            if p.stat().st_size == 0:
                # a zero-byte file is not an image: it is a publisher defect
                res.unreadable.append(str(p.relative_to(dataset_dir)))
                continue
            by_hash[md5(p)].append(str(p.relative_to(dataset_dir)))

        res.exact_unique = len(by_hash)
        if by_hash:
            biggest = max(by_hash.values(), key=len)
            res.largest_group = len(biggest)
            res.largest_group_example = biggest[:3]

        hashes = []
        for group in by_hash.values():
            try:
                hashes.append(dhash(dataset_dir / group[0]))
            except Exception:  # corrupt or unreadable image
                res.unreadable.extend(group)
        for th in thresholds:
            res.perceptual[th] = cluster_count(hashes, th)
        results.append(res)
    return results


def render(results: list[ClassResult], thresholds: tuple[int, ...]) -> str:
    lines = ["# Duplication audit", ""]
    lines.append("Exact duplicates are byte-identical files (MD5). Perceptual clusters use "
                 "a 64-bit dHash with a Hamming threshold; the exact count is a hard fact, "
                 "the perceptual count is threshold-dependent.")
    lines.append("")
    lines.append("Zero-byte files and files that cannot be decoded are counted as unreadable and "
                 "excluded from the distinct count.")
    lines.append("")
    head = "| Dataset | Class | Files | Exact unique | Duplicate copies |"
    head += "".join(f" d<={t} |" for t in thresholds)
    head += " Unreadable |"
    lines.append(head)
    lines.append("|" + "---|" * (6 + len(thresholds)))
    for r in results:
        row = f"| {r.dataset} | {r.label} | {r.files:,} | {r.exact_unique:,} | {r.extra:,} |"
        row += "".join(f" {r.perceptual.get(t, 0):,} |" for t in thresholds)
        row += f" {len(r.unreadable)} |"
        lines.append(row)

    lines += ["", "## Totals", ""]
    tot_files = sum(r.files for r in results)
    tot_exact = sum(r.exact_unique for r in results)
    lines.append(f"- files: **{tot_files:,}**")
    lines.append(f"- exact-unique: **{tot_exact:,}**")
    lines.append(f"- duplicate copies: **{tot_files - tot_exact:,}** "
                 f"({(tot_files - tot_exact) / max(tot_files, 1):.1%})")
    for t in thresholds:
        n = sum(r.perceptual.get(t, 0) for r in results)
        lines.append(f"- perceptual clusters (d<={t}): **{n:,}**")

    big = sorted(results, key=lambda r: r.largest_group, reverse=True)[:5]
    lines += ["", "## Largest duplicate groups", ""]
    for r in big:
        if r.largest_group > 1:
            lines.append(f"- **{r.dataset}/{r.label}**: {r.largest_group} identical files, "
                         f"e.g. `{', '.join(r.largest_group_example)}`")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raw", type=Path, default=Path("data/raw"))
    ap.add_argument("--out", type=Path, default=Path("data/audit"))
    ap.add_argument("--threshold", type=int, default=8,
                    help="headline perceptual threshold (default 8)")
    ap.add_argument("--datasets", nargs="*", default=None,
                    help="subset of dataset folders to audit (default: all)")
    args = ap.parse_args()

    if not args.raw.exists():
        raise SystemExit(f"no such directory: {args.raw}")

    thresholds = tuple(sorted(set(THRESHOLDS) | {args.threshold}))
    dirs = [d for d in sorted(args.raw.iterdir()) if d.is_dir()]
    if args.datasets:
        dirs = [d for d in dirs if d.name in set(args.datasets)]

    results: list[ClassResult] = []
    for d in dirs:
        print(f"== {d.name}", flush=True)
        results.extend(audit_dataset(d, thresholds))

    for r in results:
        print(f"  {r.label:<20} {r.files:>7,} files | {r.exact_unique:>6,} exact | "
              f"{r.extra:>6,} dup | d<={args.threshold}: {r.perceptual[args.threshold]:>6,}")

    args.out.mkdir(parents=True, exist_ok=True)
    md = render(results, thresholds)
    (args.out / "duplication-report.md").write_text(md, encoding="utf-8")
    payload = {
        "thresholds": list(thresholds),
        "headline_threshold": args.threshold,
        "classes": [
            {
                "dataset": r.dataset,
                "label": r.label,
                "files": r.files,
                "exact_unique": r.exact_unique,
                "duplicate_copies": r.extra,
                "perceptual_clusters": {str(k): v for k, v in r.perceptual.items()},
                "unreadable": r.unreadable,
                "largest_group": r.largest_group,
                "largest_group_example": r.largest_group_example,
            }
            for r in results
        ],
        "totals": {
            "files": sum(r.files for r in results),
            "exact_unique": sum(r.exact_unique for r in results),
            "duplicate_copies": sum(r.extra for r in results),
            "perceptual_clusters": {str(t): sum(r.perceptual.get(t, 0) for r in results)
                                    for t in thresholds},
        },
    }
    (args.out / "duplication-report.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"\nwrote {args.out/'duplication-report.md'}")
    print(f"wrote {args.out/'duplication-report.json'}")


if __name__ == "__main__":
    main()
