#!/usr/bin/env python3
"""atlas_coverage.py — Report coverage of raw/github/relay-neuron/ against wiki/sources/.

Atlas-specific variant of pyramid's pdf_coverage.py. Atlas has no raw/PDFs/;
its sole source layer is `raw/github/relay-neuron/` (a research archive cloned
from Sphinxes0o0/relay-neuron).

Matching strategy (since relay-neuron files are Git LFS pointer files and
the ingest workflow never computes md5s):
  1. Prefer exact `path:` field match — frontmatter `path: raw/.../subdir/`
     resolves to a real on-disk directory. We count every md under that
     directory as "covered by this source page".
  2. Fall back to source-page basename matching the nearest subdir
     (e.g. `relay-neuron-nutrition.md` ↔ `research/nutrition/`) — this
     recovers pages whose `path:` is missing or wrong.
  3. Files at `raw/github/relay-neuron/research/` root (not in any subdir)
     are matched to the page that claims to be the umbrella overview
     (relay-neuron-overview.md) or any page that omits a path.

Output categories:
  - covered:     raw md is "claimed" by ≥1 source page
  - orphan_raw:  raw md has no matching source page
  - orphan_md:   source page whose path/dir has no raw files

Usage:
  python3 scripts/atlas_coverage.py            # human report
  python3 scripts/atlas_coverage.py --json     # machine-readable
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

ATLAS = Path(__file__).resolve().parent.parent
RAW_GH = ATLAS / "raw" / "github" / "relay-neuron"
SOURCES = ATLAS / "wiki" / "sources"

PATH_RE = re.compile(r"^path:\s*(.+)$", re.M)
TYPE_RE = re.compile(r"^type:\s*(\S+)", re.M)
STYPE_RE = re.compile(r"^source-type:\s*(\S+)", re.M)
TITLE_RE = re.compile(r'^title:\s*"?(.+?)"?\s*$', re.M)


def collect_raw_mds() -> Dict[Path, str]:
    """Return {md_path: relpath_str} for all .md under raw/github/relay-neuron/.

    Excludes top-level meta files (AGENT.md, CLAUDE.md, README.md, etc.)
    since they aren't research data.
    """
    out: Dict[Path, str] = {}
    if not RAW_GH.exists():
        return out
    for p in RAW_GH.rglob("*.md"):
        if p.is_file():
            out[p] = str(p.relative_to(ATLAS))
    return out


def collect_source_pages() -> List[dict]:
    """Return list of source-page descriptors parsed from wiki/sources/*.md."""
    out: List[dict] = []
    if not SOURCES.exists():
        return out
    for md in sorted(SOURCES.glob("*.md")):
        try:
            txt = md.read_text(errors="ignore")
        except Exception:
            continue
        if TYPE_RE.search(txt) is None:
            continue
        type_val = TYPE_RE.search(txt).group(1)  # type: ignore[union-attr]
        if type_val != "source":
            continue
        path_m = PATH_RE.search(txt)
        stype_m = STYPE_RE.search(txt)
        title_m = TITLE_RE.search(txt)
        out.append({
            "md": str(md.relative_to(ATLAS)),
            "name": md.stem,
            "path_field": path_m.group(1).strip() if path_m else None,
            "source_type": stype_m.group(1) if stype_m else None,
            "title": title_m.group(1) if title_m else None,
        })
    return out


def resolve_path_field_to_dir(path_str: str) -> Path | None:
    """Resolve a frontmatter `path:` string to a directory on disk.

    Tolerates:
      - `raw/...` (relative to repo root) — preferred
      - `research/...` (legacy, no raw/ prefix) — fix up
      - bare subdir name (e.g. `supplements/`) — look under research/
    """
    if not path_str:
        return None
    p_str = path_str.rstrip("/").strip()
    candidates = [
        ATLAS / p_str,
        ATLAS / "raw" / "github" / "relay-neuron" / p_str,
    ]
    for c in candidates:
        try:
            if c.is_dir():
                return c
        except OSError:
            continue
    return None


def coverage_report() -> dict:
    raw_mds = collect_raw_mds()
    source_pages = collect_source_pages()

    # For each source page, compute which raw mds it "claims"
    raw_to_claims: Dict[Path, List[str]] = {p: [] for p in raw_mds}
    page_to_raw: Dict[str, List[Path]] = {}

    for sp in source_pages:
        claimed: List[Path] = []
        if sp["path_field"]:
            d = resolve_path_field_to_dir(sp["path_field"])
            if d is not None:
                for p in raw_mds:
                    try:
                        p.relative_to(d)  # raises if not under d
                        claimed.append(p)
                    except ValueError:
                        continue
        page_to_raw[sp["md"]] = claimed
        for p in claimed:
            raw_to_claims[p].append(sp["md"])

    # Fuzzy fallback: source pages without a path_field or whose path didn't
    # resolve can still be matched by name ↔ subdir (e.g. relay-neuron-nutrition
    # ↔ research/nutrition/). This is intentionally a SECONDARY pass to avoid
    # double-counting raw files already claimed by path-based pages.
    for sp in source_pages:
        if page_to_raw[sp["md"]]:
            continue
        # Extract subdir hint from the page name: relay-neuron-<topic> → topic
        m = re.match(r"^relay-neuron-(.+)$", sp["name"])
        if not m:
            continue
        topic = m.group(1)
        # Try a few candidate subdirs under research/
        candidate_subdirs = [
            RAW_GH / "research" / topic,
            RAW_GH / "research" / topic.replace("-", "_"),
        ]
        for d in candidate_subdirs:
            if d.is_dir():
                for p in raw_mds:
                    try:
                        p.relative_to(d)
                        if sp["md"] not in raw_to_claims[p]:
                            page_to_raw[sp["md"]].append(p)
                            raw_to_claims[p].append(sp["md"])
                    except ValueError:
                        continue
                break

    # Classify
    covered_raw = [p for p, claims in raw_to_claims.items() if claims]
    orphan_raw = [
        {
            "path": str(p.relative_to(ATLAS)),
            "size_bytes": p.stat().st_size,
        }
        for p, claims in raw_to_claims.items()
        if not claims
    ]

    orphan_mds: List[dict] = []
    for sp in source_pages:
        # Web sources (source-type: web) have no raw files by design — they
        # reference a URL instead of a local path/. Skip them so they are
        # never reported as orphan. Only sources with a path: field that
        # failed to resolve (e.g. a typo'd path) should be flagged.
        if sp["source_type"] == "web":
            continue
        if not page_to_raw[sp["md"]]:
            orphan_mds.append({
                "md": sp["md"],
                "path_field": sp["path_field"],
                "source_type": sp["source_type"],
                "title": sp["title"],
            })

    # Sanity: pages that claim too many files (e.g. root-level path:
    # raw/github/relay-neuron/research/ swallows the entire research tree)
    suspicious_claims: List[dict] = []
    for sp in source_pages:
        n = len(page_to_raw[sp["md"]])
        if n > 200:  # probably the root-leak
            suspicious_claims.append({
                "md": sp["md"],
                "claims": n,
                "path_field": sp["path_field"],
            })

    return {
        "total_raw_mds": len(raw_mds),
        "covered_raw": len(covered_raw),
        "orphan_raw_count": len(orphan_raw),
        "orphan_raw_bytes": sum(o["size_bytes"] for o in orphan_raw),
        "total_source_pages": len(source_pages),
        "orphan_md_count": len(orphan_mds),
        "orphan_mds": orphan_mds,
        "suspicious_claims": suspicious_claims,
        "orphan_raw_sample": sorted(orphan_raw, key=lambda o: o["path"])[:50],
    }


def print_report(r: dict) -> None:
    total = r["total_raw_mds"]
    cov = r["covered_raw"]
    pct = 100 * cov / total if total else 0
    print(f"=== Atlas source coverage ===")
    print(f"Source layer:        raw/github/relay-neuron/")
    print(f"Total raw .md files: {total}")
    print(f"Covered:             {cov}  ({pct:.1f}%)")
    print(f"Orphan raw:          {r['orphan_raw_count']}  "
          f"({r['orphan_raw_bytes']/1e6:.1f} MB)")
    print(f"Source pages:        {r['total_source_pages']}")
    print(f"Orphan source pages: {r['orphan_md_count']}")

    if r["suspicious_claims"]:
        print(f"\n--- Suspicious claim sizes (path: points too high in tree) ---")
        for s in r["suspicious_claims"]:
            print(f"  {s['claims']:4d} files ← {s['md']}  (path: {s['path_field']})")

    if r["orphan_mds"]:
        print(f"\n--- Orphan source pages (no raw files claimed) ---")
        for o in r["orphan_mds"]:
            print(f"  {o['md']}  type={o['source_type']}  path={o['path_field']}")

    if r["orphan_raw_sample"]:
        print(f"\n--- Orphan raw files (sample, first 50) ---")
        for o in r["orphan_raw_sample"]:
            print(f"  {o['path']}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0] if __doc__ else "")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    r = coverage_report()
    if args.json:
        print(json.dumps(r, indent=2, ensure_ascii=False))
    else:
        print_report(r)
    return 0


if __name__ == "__main__":
    sys.exit(main())
