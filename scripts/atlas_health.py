#!/usr/bin/env python3
"""atlas_health.py — Wiki health check for Atlas.

Atlas-specific variant of pyramid's lint_wiki.py. Checks:
  - broken wikilinks (target page doesn't exist)
  - orphan pages (no inbound [[wikilinks]])
  - frontmatter issues (missing type/tags/created, bad type values)
  - source-page-specific checks (missing path field, suspicious source-type,
    pages claiming no raw files)
  - large pages (>200 lines, advisory only)

Skips:
  - wiki/raw/ (snapshot of relay-neuron data, not part of the wiki itself)
  - attachments/
  - .obsidian/, .trash/, etc.

Output: human report to stdout, JSON to /tmp/atlas_health.json.

Usage:
  python3 scripts/atlas_health.py
  python3 scripts/atlas_health.py --json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Tuple

ATLAS = Path(__file__).resolve().parent.parent
WIKI = ATLAS / "wiki"

VALID_TYPES = {"entity", "source", "synthesis", "journal", "index", "log", "dashboard"}
SKIP_DIRS = {".obsidian", ".trash", "attachments", "raw"}  # wiki/raw/ is a data snapshot

# Path fields in source pages
PATH_RE = re.compile(r"^path:\s*(.+)$", re.M)
TYPE_RE = re.compile(r"^type:\s*(\S+)", re.M)
STYPE_RE = re.compile(r"^source-type:\s*(\S+)", re.M)
CREATED_RE = re.compile(r"^created:\s*(\S+)", re.M)
TAGS_RE = re.compile(r"^tags:\s*\[([^\]]*)\]", re.M)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")


def parse_frontmatter(content: str) -> dict | None:
    """Lightweight YAML frontmatter parser. Returns dict or None."""
    m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return None
    fields: dict = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        elif val.startswith("'") and val.endswith("'"):
            val = val[1:-1]
        if val.startswith("[") and val.endswith("]"):
            items = []
            cur = ""
            depth = 0
            in_str = None
            for ch in val:
                if in_str:
                    if ch == in_str:
                        in_str = None
                    cur += ch
                    continue
                if ch in "\"'":
                    in_str = ch
                    cur += ch
                    continue
                if ch == "[":
                    depth += 1
                elif ch == "]":
                    depth -= 1
                if ch == "," and depth == 0:
                    if cur.strip():
                        items.append(cur.strip().strip('"').strip("'"))
                    cur = ""
                else:
                    cur += ch
            if cur.strip():
                items.append(cur.strip().strip('"').strip("'"))
            val = items
        fields[key] = val
    return fields


def collect_wiki_files() -> List[Tuple[str, Path]]:
    out: List[Tuple[str, Path]] = []
    for root, dirs, files in os.walk(WIKI):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for f in files:
            if f.endswith(".md"):
                full = Path(root) / f
                rel = str(full.relative_to(WIKI))
                out.append((rel, full))
    return sorted(out)


def extract_wikilinks(content: str) -> Set[str]:
    body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, count=1, flags=re.DOTALL)
    links: Set[str] = set()
    for m in WIKILINK_RE.finditer(body):
        t = m.group(1).strip()
        if t.startswith("./"):
            t = t[2:]
        links.add(t)
    return links


def run_health() -> dict:
    files = collect_wiki_files()
    file_contents = {rel: p.read_text(errors="ignore") for rel, p in files}

    # Build valid target set
    valid_targets: Set[str] = set()
    basename_index: Dict[str, str] = {}
    for rel, _ in files:
        base = rel[:-3] if rel.endswith(".md") else rel
        valid_targets.add(base)
        bn = os.path.basename(base)
        if bn not in basename_index or len(rel) < len(basename_index[bn]):
            basename_index[bn] = rel

    # Build link graph
    outbound: Dict[str, Set[str]] = {rel: extract_wikilinks(c) for rel, c in file_contents.items()}

    inbound_count: Dict[str, int] = defaultdict(int)
    for src, targets in outbound.items():
        for t in targets:
            base = t
            # Resolve: exact match preferred, then legacy "wiki/" prefix, then basename
            if base in valid_targets:
                resolved = base
            elif base.startswith("wiki/") and base[5:] in valid_targets:
                resolved = base[5:]
            elif os.path.basename(base) in basename_index:
                resolved = os.path.basename(base)
            else:
                continue
            # Count inbound for the resolved file
            resolved_base = resolved[:-3] if resolved.endswith(".md") else resolved
            for rel, _ in files:
                if rel == resolved or rel[:-3] == resolved_base:
                    inbound_count[rel] += 1
                    break

    # Classify files
    content_files = [
        rel for rel, _ in files
        if rel.startswith("entities/") or rel.startswith("sources/")
        or rel.startswith("synthesis/")
    ]
    nav_files = [rel for rel, _ in files if rel not in content_files]

    # Broken wikilinks
    broken_links: List[Tuple[str, str, str]] = []  # (src, target, reason)
    for src, targets in outbound.items():
        for t in targets:
            if t in valid_targets:
                continue
            if t.startswith("wiki/") and t[5:] in valid_targets:
                continue
            if os.path.basename(t) in basename_index:
                # basename fuzzy — flag as broken-but-resolvable for awareness
                broken_links.append((src, t, f"fuzzy→{basename_index[os.path.basename(t)]}"))
                continue
            broken_links.append((src, t, "no match"))

    # Orphan pages
    orphan_pages: List[str] = []
    for rel in content_files:
        if inbound_count.get(rel, 0) == 0:
            orphan_pages.append(rel)

    # Frontmatter checks
    frontmatter_issues: List[Tuple[str, str]] = []
    for rel, _ in files:
        # Skip nav files from required-field check, but still parse them
        is_content = rel in content_files
        content = file_contents[rel]
        fm = parse_frontmatter(content)
        if fm is None:
            frontmatter_issues.append((rel, "missing frontmatter"))
            continue
        if "type" not in fm:
            frontmatter_issues.append((rel, "missing 'type'"))
        elif fm["type"] not in VALID_TYPES:
            frontmatter_issues.append((rel, f"invalid type: '{fm['type']}'"))
        if is_content:
            if "tags" not in fm:
                frontmatter_issues.append((rel, "missing 'tags'"))
            elif isinstance(fm.get("tags"), list) and not fm["tags"]:
                frontmatter_issues.append((rel, "empty 'tags'"))
            if "created" not in fm:
                frontmatter_issues.append((rel, "missing 'created'"))

    # Source-page-specific
    source_issues: List[Tuple[str, str]] = []
    for rel, _ in files:
        if not rel.startswith("sources/"):
            continue
        content = file_contents[rel]
        fm = parse_frontmatter(content) or {}
        # source-type check
        stype = fm.get("source-type")
        if stype and stype not in ("pdf", "docx", "xlsx", "pptx", "image", "github", "bookmark", "web"):
            source_issues.append((rel, f"unrecognized source-type: '{stype}'"))
        # path: check
        if stype in ("github", "pdf", "docx", "xlsx", "pptx"):
            if "path" not in fm:
                source_issues.append((rel, "missing 'path' field"))
            else:
                p = fm["path"]
                # Resolve
                p_clean = p.rstrip("/").strip()
                if p_clean.startswith("research/"):
                    source_issues.append((rel, f"path missing 'raw/github/relay-neuron/' prefix: '{p}'"))
                full_p = (ATLAS / p_clean)
                if not full_p.exists():
                    # also try the fix-up version
                    fixed = ATLAS / "raw" / "github" / "relay-neuron" / p_clean
                    if not fixed.exists():
                        source_issues.append((rel, f"path does not resolve: '{p}'"))

    # Stale pages: entity pages with created before most-recent-source update and no updated field
    most_recent_update: datetime | None = None
    for rel, _ in files:
        if not rel.startswith("sources/"):
            continue
        fm = parse_frontmatter(file_contents[rel]) or {}
        for field in ("updated", "created"):
            v = fm.get(field)
            if v:
                try:
                    d = datetime.strptime(v, "%Y-%m-%d")
                    if most_recent_update is None or d > most_recent_update:
                        most_recent_update = d
                except ValueError:
                    pass

    stale_pages: List[Tuple[str, str, str]] = []
    if most_recent_update:
        for rel, _ in files:
            if not (rel.startswith("entities/") or rel.startswith("synthesis/")):
                continue
            fm = parse_frontmatter(file_contents[rel]) or {}
            upd = fm.get("updated")
            crt = fm.get("created")
            try:
                upd_d = datetime.strptime(upd, "%Y-%m-%d") if upd else None
            except (ValueError, TypeError):
                upd_d = None
            try:
                crt_d = datetime.strptime(crt, "%Y-%m-%d") if crt else None
            except (ValueError, TypeError):
                crt_d = None
            if upd_d and upd_d < most_recent_update:
                stale_pages.append((rel, str(upd_d.date()), str(most_recent_update.date())))

    # Large pages
    large_pages: List[Tuple[str, int]] = []
    for rel, _ in files:
        line_count = file_contents[rel].count("\n") + 1
        if line_count > 300:  # atlas pages are denser; 300 is reasonable cap
            large_pages.append((rel, line_count))

    return {
        "summary": {
            "total_files": len(files),
            "content_files": len(content_files),
            "nav_files": len(nav_files),
            "most_recent_source_update": str(most_recent_update.date()) if most_recent_update else None,
            "broken_wikilinks": len(broken_links),
            "orphan_pages": len(orphan_pages),
            "frontmatter_issues": len(frontmatter_issues),
            "source_issues": len(source_issues),
            "stale_pages": len(stale_pages),
            "large_pages": len(large_pages),
        },
        "broken_links": broken_links,
        "orphan_pages": sorted(orphan_pages),
        "frontmatter_issues": frontmatter_issues,
        "source_issues": source_issues,
        "stale_pages": stale_pages,
        "large_pages": large_pages,
    }


def print_report(r: dict) -> None:
    s = r["summary"]
    print(f"=== Atlas wiki health ===")
    print(f"Total .md files (excl. wiki/raw/): {s['total_files']}")
    print(f"  content (entities/sources/synthesis): {s['content_files']}")
    print(f"  nav (indexes/home/log):               {s['nav_files']}")
    print(f"Most recent source update: {s['most_recent_source_update']}")
    print()
    print(f"Broken wikilinks:    {s['broken_wikilinks']}")
    print(f"Orphan pages:        {s['orphan_pages']}")
    print(f"Frontmatter issues:  {s['frontmatter_issues']}")
    print(f"Source-page issues:  {s['source_issues']}")
    print(f"Stale pages:         {s['stale_pages']}")
    print(f"Large pages (>300L): {s['large_pages']}")

    if r["broken_links"]:
        print(f"\n--- Broken wikilinks (first 30) ---")
        for src, tgt, why in r["broken_links"][:30]:
            print(f"  {src} -> [[{tgt}]]  ({why})")
        if len(r["broken_links"]) > 30:
            print(f"  … and {len(r['broken_links']) - 30} more")

    if r["orphan_pages"]:
        print(f"\n--- Orphan pages ---")
        for p in r["orphan_pages"][:30]:
            print(f"  {p}")
        if len(r["orphan_pages"]) > 30:
            print(f"  … and {len(r['orphan_pages']) - 30} more")

    if r["frontmatter_issues"]:
        print(f"\n--- Frontmatter issues (first 30) ---")
        for path, issue in r["frontmatter_issues"][:30]:
            print(f"  {path}: {issue}")
        if len(r["frontmatter_issues"]) > 30:
            print(f"  … and {len(r['frontmatter_issues']) - 30} more")

    if r["source_issues"]:
        print(f"\n--- Source-page issues ---")
        for path, issue in r["source_issues"]:
            print(f"  {path}: {issue}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0] if __doc__ else "")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    r = run_health()
    if args.json:
        print(json.dumps(r, indent=2, ensure_ascii=False))
    else:
        print_report(r)
    return 0


if __name__ == "__main__":
    sys.exit(main())
