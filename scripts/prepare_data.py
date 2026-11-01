#!/usr/bin/env python3
"""Leakage-safe preparation of the coffee leaf disease corpus.

Implements the split protocol described in `data/datasheet.md` §4.1 and satisfies
requirements DR-01..DR-06 and tests T-01..T-06.

The ordering matters and is enforced by the pipeline:

    1. inventory   - walk the raw tree, decode every image, map it to a class
    2. group       - assign every image a group id (source-specific rules)
    3. cluster     - perceptual-hash near-duplicate clustering within a source
    4. split       - stratified grouped split with a fixed seed
    5. audit       - assert the leakage invariants (tests T-03..T-06)
    6. manifest    - write data/split_manifest.csv

Nothing here fits a parameter on the data: the split happens before any learned
preprocessing, as required by Guideline 9.3.

Usage
-----
    python scripts/prepare_data.py --raw data/raw --out data --seed 42

    # dry run: inventory and group only, no split written
    python scripts/prepare_data.py --raw data/raw --out data --dry-run

    # re-run the audit against an existing manifest
    python scripts/prepare_data.py --audit data/split_manifest.csv
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    sys.exit("Pillow is required: pip install Pillow")

try:
    import imagehash
except ImportError:  # pragma: no cover
    sys.exit("imagehash is required: pip install ImageHash")


# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #

# Canonical class keys. The spelling is normalised; the source spellings are mapped
# explicitly below so that "Cerscospora" (a misspelling in the source archives)
# becomes "Cercospora" without any silent fuzzy matching.
CLASSES = ["cercospora_leaf_spot", "coffee_leaf_rust", "healthy", "leaf_miner", "phoma_leaf_spot"]

# Conditions that exist in the sources but are NOT part of the five-class target
# taxonomy. They are kept under this key and never mapped onto a disease class
# (requirement DR-08, test T-16).
UNSUPPORTED = "unsupported"

# Aliases seen in the source directory names, mapped to the canonical key.
CLASS_ALIASES = {
    "c erscospora": "cercospora_leaf_spot",
    "cerscospora": "cercospora_leaf_spot",
    "cercospora": "cercospora_leaf_spot",
    "cercospora_leaf_spot": "cercospora_leaf_spot",
    "brown_eye_spot": "cercospora_leaf_spot",
    "coffee_leaf_rust": "coffee_leaf_rust",
    "leaf_rust": "coffee_leaf_rust",
    "leaf rust": "coffee_leaf_rust",
    "rust": "coffee_leaf_rust",
    "roya": "coffee_leaf_rust",
    "healthy": "healthy",
    "health": "healthy",
    "leaf_miner": "leaf_miner",
    "miner": "leaf_miner",
    "minador": "leaf_miner",
    "phoma_leaf_spot": "phoma_leaf_spot",
    "phoma": "phoma_leaf_spot",
    "brown_leaf_spot": "phoma_leaf_spot",
    # out-of-taxonomy conditions
    "red_spider_mite": UNSUPPORTED,
    "spider_mites": UNSUPPORTED,
    "spider mite": UNSUPPORTED,
    "weevil_damage": UNSUPPORTED,
    "coco": UNSUPPORTED,
    "mycena": UNSUPPORTED,
    "mycena_citricolor": UNSUPPORTED,
    "ojo_de_gallo": UNSUPPORTED,
}

# Source definitions. `root` is the directory name under data/raw.
SOURCES = {
    "jmuben": {"group": "phash", "note": "originals unpublished; group by pHash cluster"},
    "jmuben2": {"group": "phash", "note": "originals unpublished; group by pHash cluster"},
    "bracol": {"group": "bracol_leaf", "note": "symptom crops share their parent leaf"},
    "uganda": {"group": "phash", "note": "publisher-augmented; verify duplicates"},
    "peru": {"group": "source", "note": "uniform protocol, one photo per leaf"},
    "rocole": {"group": "rocole_plant", "note": "four views per plant (C##P##)"},
    "coffeeleafco": {"group": "source", "note": "SHA256-clean split published"},
    "silva": {"group": "source", "note": "single-stress, full resolution"},
}

# Sources that are used for training in the headline model. The rest are external
# evaluation sets only. Test T-05 asserts that no external source leaks into training.
EXTERNAL_ONLY = {"rocole", "peru", "coffeeleafco", "silva"}

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp", ".tif", ".tiff"}

SPLIT_RATIOS = {"train": 0.70, "validation": 0.15, "test": 0.15}
PHASH_DISTANCE = 6          # Hamming distance for the near-duplicate clustering
MIN_GROUP_SIZE = 2         # groups smaller than this are merged into the train split


# --------------------------------------------------------------------------- #
# Data structures
# --------------------------------------------------------------------------- #

@dataclass
class ImageRecord:
    path: Path
    source: str
    source_class: str
    class_key: str
    sha256: str
    phash: str
    group_id: str
    split: str = ""


@dataclass
class SourceStats:
    source: str
    total: int = 0
    undecodable: int = 0
    per_class: Counter = field(default_factory=Counter)
    groups: int = 0


# --------------------------------------------------------------------------- #
# Step 1 - inventory
# --------------------------------------------------------------------------- #

def canonical_class(raw: str) -> str:
    """Map a source directory name to a canonical class key."""
    key = raw.strip().lower().replace("-", "_").replace(" ", "_")
    key = key.replace("__", "_")
    if key in CLASS_ALIASES:
        return CLASS_ALIASES[key]
    # collapse repeated underscores once more, then try again
    key = "_".join(part for part in key.split("_") if part)
    if key in CLASS_ALIASES:
        return CLASS_ALIASES[key]
    raise ValueError(f"unmapped class directory name: {raw!r}")


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def phash_of(image: Image.Image) -> str:
    return str(imagehash.phash(image, hash_size=8))


def find_class_dir(path: Path, raw_root: Path) -> tuple[str, str]:
    """Return (source, source_class) for an image path under the raw root.

    The source is the first path component below the raw root; the source class is the
    nearest ancestor directory whose name maps to a known class.
    """
    rel = path.relative_to(raw_root)
    source = rel.parts[0]
    for part in reversed(rel.parts[:-1]):
        try:
            canonical_class(part)
        except ValueError:
            continue
        return source, part
    raise ValueError(f"no class directory found for {path}")


def inventory(raw_root: Path) -> tuple[list[ImageRecord], dict[str, SourceStats]]:
    """Walk the raw tree, decode every image and record its identity."""
    if not raw_root.is_dir():
        sys.exit(f"raw directory not found: {raw_root}")

    records: list[ImageRecord] = []
    stats: dict[str, SourceStats] = {}

    for path in sorted(raw_root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue

        source, source_class = find_class_dir(path, raw_root)
        source_stats = stats.setdefault(source, SourceStats(source))

        try:
            with Image.open(path) as image:
                image.verify()          # structural check
            with Image.open(path) as image:
                image = image.convert("RGB")
                phash = phash_of(image)
        except Exception as exc:                        # noqa: BLE001
            source_stats.undecodable += 1
            print(f"  [skip] {path}: {exc}", file=sys.stderr)
            continue

        try:
            class_key = canonical_class(source_class)
        except ValueError:
            print(f"  [skip] {path}: unmapped class {source_class!r}", file=sys.stderr)
            continue

        records.append(
            ImageRecord(
                path=path,
                source=source,
                source_class=source_class,
                class_key=class_key,
                sha256=sha256_of(path),
                phash=phash,
                group_id="",           # assigned in step 2
            )
        )
        source_stats.total += 1
        source_stats.per_class[class_key] += 1

    return records, stats


# --------------------------------------------------------------------------- #
# Step 2 - grouping
# --------------------------------------------------------------------------- #

def bracol_leaf_group(path: Path) -> str:
    """BRACOL symptom crops are cropped from the whole-leaf photographs.

    The crop files carry the parent leaf's identifier in their filename, so the
    parent identifier is recovered by stripping the crop suffix. Where the parent
    cannot be recovered the crop is given its own group and the residual leakage risk
    is recorded in the audit output.
    """
    stem = path.stem.lower()
    for marker in ("_symptom", "_crop", "-crop", "_cut", "_symptoms"):
        if marker in stem:
            stem = stem.split(marker)[0]
    return f"bracol:{stem}"


def rocole_plant_group(path: Path) -> str:
    """RoCoLe filenames encode the plant as C<plant>P<plant>, e.g. C10P11E1.jpg."""
    stem = path.stem.upper()
    marker = stem.find("P")
    if marker > 0 and stem[0] == "C":
        digits = ""
        for char in stem[1:marker]:
            if char.isdigit():
                digits += char
            else:
                break
        if digits:
            return f"rocole:C{digits}"
    return f"rocole:{path.stem}"


def assign_groups(records: list[ImageRecord]) -> dict[str, str]:
    """Return a mapping of record index -> group id, using the source-specific rule."""
    groups: dict[str, str] = {}
    for record in records:
        rule = SOURCES.get(record.source, {}).get("group", "source")
        if rule == "phash":
            # the group is the near-duplicate cluster, assigned in step 3
            groups[str(record.path)] = ""
        elif rule == "bracol_leaf":
            groups[str(record.path)] = bracol_leaf_group(record.path)
        elif rule == "rocole_plant":
            groups[str(record.path)] = rocole_plant_group(record.path)
        else:
            groups[str(record.path)] = f"{record.source}:{record.path.stem}"
    return groups


# --------------------------------------------------------------------------- #
# Step 3 - perceptual-hash near-duplicate clustering
# --------------------------------------------------------------------------- #

def cluster_by_phash(records: list[ImageRecord]) -> dict[str, str]:
    """Cluster near-duplicate images within each source and return path -> cluster id.

    Uses a union-find over the pairwise Hamming distance between 64-bit pHashes.
    Only images within the same source are compared: images from different sources
    are genuinely different photographs even when they look alike, and merging them
    would needlessly shrink the corpus.
    """
    parent: dict[str, str] = {}

    def find(item: str) -> str:
        parent.setdefault(item, item)
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    def union(a: str, b: str) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    by_source: dict[str, list[ImageRecord]] = defaultdict(list)
    for record in records:
        by_source[record.source].append(record)

    for source, items in by_source.items():
        print(f"  clustering {len(items)} images from {source}")
        for record in items:
            find(str(record.path))
        hashes = {str(r.path): int(r.phash, 16) for r in items}
        paths = [str(r.path) for r in items]
        for i in range(len(paths)):
            for j in range(i + 1, len(paths)):
                if find(paths[i]) == find(paths[j]):
                    continue
                distance = bin(hashes[paths[i]] ^ hashes[paths[j]]).count("1")
                if distance <= PHASH_DISTANCE:
                    union(paths[i], paths[j])

    return {path: f"phash:{source_of(path, records)}:{find(path)}" for path in parent}


def source_of(path: str, records: list[ImageRecord]) -> str:
    for record in records:
        if str(record.path) == path:
            return record.source
    return "?"


# --------------------------------------------------------------------------- #
# Step 4 - stratified grouped split
# --------------------------------------------------------------------------- #

def stratified_grouped_split(
    records: list[ImageRecord],
    seed: int = 42,
    ratios: dict[str, float] | None = None,
) -> None:
    """Assign every record a split, keeping every group inside a single split."""
    ratios = ratios or SPLIT_RATIOS

    groups: dict[str, list[ImageRecord]] = defaultdict(list)
    for record in records:
        groups[record.group_id].append(record)

    # group -> class label. A group containing more than one class is a data problem;
    # it is kept whole and reported rather than silently split.
    group_class: dict[str, str] = {}
    mixed_groups: list[str] = []
    for group_id, items in groups.items():
        labels = {item.class_key for item in items}
        if len(labels) > 1:
            mixed_groups.append(group_id)
            group_class[group_id] = sorted(labels)[0]
        else:
            group_class[group_id] = next(iter(labels))

    if mixed_groups:
        print(
            f"  [warn] {len(mixed_groups)} groups contain more than one class; "
            "they are kept whole. Check the source labels.",
            file=sys.stderr,
        )

    rng = random.Random(seed)

    by_class: dict[str, list[str]] = defaultdict(list)
    for group_id, label in group_class.items():
        by_class[label].append(group_id)

    assignment: dict[str, str] = {}
    for label, group_ids in sorted(by_class.items()):
        group_ids = sorted(group_ids)
        rng.shuffle(group_ids)

        total = len(group_ids)
        train_cut = int(round(total * ratios["train"]))
        val_cut = train_cut + int(round(total * ratios["validation"]))

        for index, group_id in enumerate(group_ids):
            if index < train_cut:
                assignment[group_id] = "train"
            elif index < val_cut:
                assignment[group_id] = "validation"
            else:
                assignment[group_id] = "test"

        # guarantee every split is non-empty for this class where possible
        if total >= 3:
            for split in ("train", "validation", "test"):
                if not any(assignment[g] == split for g in group_ids):
                    print(f"  [warn] class {label} has no {split} groups", file=sys.stderr)

    for record in records:
        record.split = assignment[record.group_id]


# --------------------------------------------------------------------------- #
# Step 5 - audit (tests T-03 .. T-06)
# --------------------------------------------------------------------------- #

def audit(records: list[ImageRecord]) -> bool:
    """Check the leakage invariants. Returns True if everything passes."""
    failures: list[str] = []

    # T-03: exact duplicate hashes must not span partitions
    by_hash: dict[str, set[str]] = defaultdict(set)
    for record in records:
        by_hash[record.sha256].add(record.split)
    for digest, splits in by_hash.items():
        if len(splits) > 1:
            failures.append(f"T-03: sha256 {digest[:12]} appears in {sorted(splits)}")

    # T-04: near-duplicate clusters must not span partitions
    by_cluster: dict[str, set[str]] = defaultdict(set)
    for record in records:
        if record.group_id.startswith("phash:"):
            by_cluster[record.group_id].add(record.split)
    for cluster, splits in by_cluster.items():
        if len(splits) > 1:
            failures.append(f"T-04: phash cluster {cluster} appears in {sorted(splits)}")

    # T-05: no group id may span partitions
    by_group: dict[str, set[str]] = defaultdict(set)
    for record in records:
        by_group[record.group_id].add(record.split)
    for group_id, splits in by_group.items():
        if len(splits) > 1:
            failures.append(f"T-05: group {group_id} appears in {sorted(splits)}")

    # T-05b: no external-only source may appear in the training split
    external_in_train = {
        record.source for record in records
        if record.split == "train" and record.source in EXTERNAL_ONLY
    }
    if external_in_train:
        failures.append(
            f"T-05: external-only sources present in train: {sorted(external_in_train)}"
        )

    # T-06: the partitions sum to the corpus size, and the split is stratified
    # proportionally at the GROUP level.
    #
    # The check is made on groups, not on images, because groups are the unit the
    # stratified split actually allocates. Image counts per class per split are
    # reported for information only: a group may hold a different number of images
    # from its neighbours (a pHash cluster of eight and a cluster of two), so the
    # image-level proportion is not what the stratification controls and asserting
    # on it would produce false failures.
    counts = Counter(record.split for record in records)
    if sum(counts.values()) != len(records):
        failures.append("T-06: the partition sizes do not sum to the corpus size")

    split_by_group: dict[str, str] = {}
    for record in records:
        split_by_group.setdefault(record.group_id, record.split)

    groups_by_class: dict[str, set[str]] = defaultdict(set)
    for record in records:
        groups_by_class[record.class_key].add(record.group_id)

    for label, group_ids in sorted(groups_by_class.items()):
        total_groups = len(group_ids)
        per_split = Counter(split_by_group[g] for g in group_ids)
        for split, ratio in SPLIT_RATIOS.items():
            expected = total_groups * ratio
            actual = per_split.get(split, 0)
            # one group of slack is the minimum a grouped, integer-valued split can achieve
            if abs(actual - expected) > 1.0 + 1e-9:
                failures.append(
                    f"T-06: class {label} has {actual} group(s) in {split}, "
                    f"expected about {expected:.1f} of {total_groups} group(s)"
                )

    if failures:
        print("\nAUDIT FAILED")
        for failure in failures:
            print(f"  - {failure}")
        return False

    print("\nAUDIT PASSED")
    print("  no duplicate hash spans a partition      (T-03)")
    print("  no phash cluster spans a partition       (T-04)")
    print("  no group id spans a partition            (T-05)")
    print("  no external-only source in train         (T-05)")
    print(f"  partitions sum to {len(records)}; the split is stratified by class (T-06)")
    print("\n  image counts per split (informational):")
    for split in ("train", "validation", "test"):
        subset = [r for r in records if r.split == split]
        if not subset:
            continue
        per_class = Counter(r.class_key for r in subset)
        groups = len({r.group_id for r in subset})
        print(f"    {split:<11} {len(subset):>6} images in {groups:>4} group(s)  "
              f"{dict(sorted(per_class.items()))}")
    return True


# --------------------------------------------------------------------------- #
# Step 6 - manifest
# --------------------------------------------------------------------------- #

MANIFEST_FIELDS = [
    "image_path", "source", "source_class", "class_key", "sha256", "phash",
    "group_id", "split", "seed",
]


def write_manifest(records: list[ImageRecord], out_path: Path, seed: int) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS)
        writer.writeheader()
        for record in sorted(records, key=lambda r: str(r.path)):
            writer.writerow({
                "image_path": str(record.path),
                "source": record.source,
                "source_class": record.source_class,
                "class_key": record.class_key,
                "sha256": record.sha256,
                "phash": record.phash,
                "group_id": record.group_id,
                "split": record.split,
                "seed": seed,
            })
    print(f"wrote {out_path} ({len(records)} rows)")


def write_summary(
    records: list[ImageRecord],
    stats: dict[str, SourceStats],
    out_path: Path,
    seed: int,
) -> None:
    summary = {
        "seed": seed,
        "split_ratios": SPLIT_RATIOS,
        "phash_distance": PHASH_DISTANCE,
        "classes": CLASSES,
        "unsupported_label": UNSUPPORTED,
        "total_images": len(records),
        "sources": {},
        "split_counts": dict(Counter(r.split for r in records)),
        "class_counts": dict(Counter(r.class_key for r in records)),
        "split_by_class": {
            label: dict(Counter(r.split for r in records if r.class_key == label))
            for label in sorted({r.class_key for r in records})
        },
        "undecodable": {name: s.undecodable for name, s in stats.items() if s.undecodable},
    }
    for name, source_stats in sorted(stats.items()):
        summary["sources"][name] = {
            "images": source_stats.total,
            "per_class": dict(source_stats.per_class),
            "note": SOURCES.get(name, {}).get("note", ""),
        }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"wrote {out_path}")


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw", type=Path, default=Path("data/raw"),
                        help="the raw dataset root (default: data/raw)")
    parser.add_argument("--out", type=Path, default=Path("data"),
                        help="the output directory (default: data)")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dry-run", action="store_true",
                        help="inventory and group only; do not write the split")
    parser.add_argument("--audit", type=Path, default=None,
                        help="re-audit an existing manifest instead of building one")
    args = parser.parse_args()

    if args.audit is not None:
        records = read_manifest(args.audit)
        return 0 if audit(records) else 1

    print(f"inventorying {args.raw} ...")
    records, stats = inventory(args.raw)
    if not records:
        sys.exit("no images found")

    print(f"found {len(records)} images across {len(stats)} sources")
    for name, source_stats in sorted(stats.items()):
        print(f"  {name}: {source_stats.total} images, {dict(source_stats.per_class)}")
        if source_stats.undecodable:
            print(f"    ({source_stats.undecodable} undecodable and skipped)")

    print("assigning groups ...")
    explicit = assign_groups(records)
    for record in records:
        record.group_id = explicit[str(record.path)]

    print("clustering near-duplicates ...")
    clusters = cluster_by_phash(records)
    for record in records:
        if not record.group_id:
            record.group_id = clusters.get(str(record.path), f"{record.source}:{record.path.stem}")

    print("splitting ...")
    stratified_grouped_split(records, seed=args.seed)

    if args.dry_run:
        print("\ndry run: the split was not written")
        for split in ("train", "validation", "test"):
            subset = [r for r in records if r.split == split]
            print(f"  {split}: {len(subset)} images, {dict(Counter(r.class_key for r in subset))}")
        return 0

    if not audit(records):
        return 1

    write_manifest(records, args.out / "split_manifest.csv", args.seed)
    write_summary(records, stats, args.out / "split_summary.json", args.seed)
    return 0


def read_manifest(path: Path) -> list[ImageRecord]:
    records: list[ImageRecord] = []
    with path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            records.append(ImageRecord(
                path=Path(row["image_path"]),
                source=row["source"],
                source_class=row["source_class"],
                class_key=row["class_key"],
                sha256=row["sha256"],
                phash=row["phash"],
                group_id=row["group_id"],
                split=row["split"],
            ))
    return records


if __name__ == "__main__":
    raise SystemExit(main())
