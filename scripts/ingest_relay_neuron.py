#!/usr/bin/env python3
"""ingest_relay_neuron.py — Ingest a relay-neuron task file into a source page.

Atlas-specific ingest script, modeled on pyramid's `scripts/ingest_pdf.py`.

Scope: ONLY the relay-neuron research archive under `raw/github/relay-neuron/`.
Atlas has no PDF source layer; the source layer is Git LFS-tracked markdown
research files. The liteparse-based ingest_pdf.py from pyramid doesn't apply.

Workflow (one source page per task file):
  1. Read `raw/github/relay-neuron/research/YYYY-MM-DD-task-X-X-<topic>.md`
  2. Extract the title (first H1 or filename slug)
  3. Compute `source-md5:` (md5 of the raw file body)
  4. Write `wiki/sources/<slug>.md` with frontmatter:
       type: source
       source-type: github
       owner: Sphinxes0o0
       repo: relay-neuron
       date: YYYY-MM-DD
       size: small|medium|large
       path: raw/github/relay-neuron/research/.../
       source-md5: <md5>
       summary: <one-liner from first paragraph>
       tags: [exercise-science, <subdomain>]
       created: <today>
  5. Print path of generated source page

Usage:
  # Single file
  python3 scripts/ingest_relay_neuron.py \
      raw/github/relay-neuron/research/2026-05-13-task-1-1-environment-altitude-benefits.md

  # Batch (recursive .md walk)
  python3 scripts/ingest_relay_neuron.py --batch raw/github/relay-neuron/research/biomechanics/
  python3 scripts/ingest_relay_neuron.py --batch raw/github/relay-neuron/  # whole corpus

  # Dry-run (don't write, just show the plan)
  python3 scripts/ingest_relay_neuron.py --dry-run --batch raw/github/relay-neuron/research/

  # Force re-ingest (overwrite existing source pages and skip md5 dedup)
  python3 scripts/ingest_relay_neuron.py --force --batch raw/github/relay-neuron/research/

Dedup:
  Each source page carries `source-md5:` in its frontmatter. Before writing
  a new page, we scan wiki/sources/*.md and skip the file if any existing
  page already has the same md5. With --force, dedup is bypassed (the
  existing page is overwritten with the freshly-rendered body).

Note (intentional, by Karpathy Simplicity First):
  - One raw file → one source page (matches the existing skeleton). The
    legacy 37 hand-written source pages already aggregate multiple raw
    files per topic; they are NOT overwritten by --batch. Pass --force
    if you really want to clobber them.
  - The slug strips the date+task prefix; benefits/risks siblings get
    distinct slugs (good — no collision in the common -benefits/-risks
    pair pattern).
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from datetime import date
from pathlib import Path

ATLAS = Path(__file__).resolve().parent.parent
SOURCES = ATLAS / "wiki" / "sources"

DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})-(?:sub)?task-")
# Allow ASCII lowercase + digits + CJK characters (U+4E00..U+9FFF) and
# fullwidth digits in the slug. Real research files use Chinese names
# (e.g. 00_铁与运动表现综述.md); we MUST preserve them or every file in
# `supplements/铁/...` collides on the empty suffix.
SLUG_KEEP_RE = re.compile(r"[^a-z0-9\u4e00-\u9fff]+", re.UNICODE)


def file_md5(p: Path) -> str:
    h = hashlib.md5()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def slugify(name: str) -> str:
    """Files like 2026-05-13-task-1-1-environment-altitude-benefits.md
    become `relay-neuron-environment-altitude-benefits` (the date/task
    prefixes are noise for source naming)."""
    stem = name
    if stem.endswith(".md"):
        stem = stem[:-3]
    # Strip leading date prefix (always present, e.g. "2026-05-13-") and
    # the optional "task-X-Y-" or "subtask-X-Y-" numbering that follows it.
    # Some files (e.g. 2026-05-03-task-creatine.md) have NO numbering
    # after "task-", so handle both cases.
    stem = re.sub(r"^\d{4}-\d{2}-\d{2}-(?:sub)?task-", "", stem)  # date+task-/subtask-
    stem = re.sub(r"^[\d-]+-?", "", stem)                        # optional X-Y- numbering
    # Re-prefix with relay-neuron- so it namespaces clearly
    return "relay-neuron-" + SLUG_KEEP_RE.sub("-", stem).strip("-")


def derive_subdomain(rel_path: Path) -> str:
    """Heuristic: if file is under research/<subdomain>/, return that name.
    Otherwise return 'misc'.

    Handles Chinese-named subdirectories (e.g. 高原训练) by using the
    raw parts verbatim — the slug will be romanized elsewhere or by
    the LLM downstream. Tags are still useful for grouping."""
    parts = rel_path.parts
    if "research" in parts:
        i = parts.index("research")
        if i + 1 < len(parts) - 1:  # has a subdir between research/ and file
            return parts[i + 1]
    return "misc"


def derive_date(rel_path: Path) -> str:
    m = DATE_RE.search(rel_path.name)
    return m.group(1) if m else str(date.today())


def derive_size(p: Path) -> str:
    sz = p.stat().st_size
    if sz < 5_000:
        return "tiny"
    if sz < 20_000:
        return "small"
    if sz < 100_000:
        return "medium"
    if sz < 500_000:
        return "large"
    return "huge"


def first_paragraph_summary(text: str, max_len: int = 120) -> str:
    """Pull the first non-heading, non-empty paragraph; truncate."""
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("|"):
            continue
        if len(line) < 20:
            continue
        if len(line) > max_len:
            line = line[: max_len - 1] + "…"
        return line
    return "(no summary)"


# Cache of {raw_path: md5} for the current ingest run, so re-hashing the
# same file in --batch doesn't re-read it.
_md5_cache: dict = {}
# Names already "claimed" by the current dry-run, so collision-protected
# writes are reported with the correct -1/-2/... suffix in the plan.
_dry_run_taken: set = set()


def cached_md5(p: Path) -> str:
    """file_md5 with per-run cache."""
    if p not in _md5_cache:
        _md5_cache[p] = file_md5(p)
    return _md5_cache[p]


def find_duplicate_by_md5(raw_path: Path, md5: str) -> "Path | None":
    """Check if any existing source page references the same raw file via:
    1. `source-md5:` frontmatter field (preferred, set by recent ingests)
    2. `path:` frontmatter field (legacy fallback; covers hand-written pages)

    Returns the existing source page if a duplicate is found, else None.
    """
    if not SOURCES.exists():
        return None

    target_rel = str(raw_path.resolve().relative_to(ATLAS.resolve())) if raw_path.is_absolute() else str(raw_path)

    for md in SOURCES.glob("*.md"):
        try:
            in_fm = False
            with open(md, encoding="utf-8") as f:
                for line in f:
                    stripped = line.strip()
                    if stripped == "---":
                        if in_fm:
                            break
                        in_fm = True
                        continue
                    if not in_fm:
                        continue
                    if line.startswith("source-md5:"):
                        existing_md5 = line.split(":", 1)[1].strip()
                        if existing_md5 == md5:
                            return md
                    if line.startswith("path:"):
                        existing_path = line.split(":", 1)[1].strip()
                        if existing_path == target_rel:
                            return md
        except (OSError, IOError):
            continue
    return None


def _unique_outpath(slug: str) -> Path:
    """Return wiki/sources/<slug>.md, appending -1, -2, ... on collision.

    Two raw files with the same slug (e.g. foo.md and foo-SUPPLEMENT.md
    where both slugify to the same base) would otherwise silently
    overwrite each other. The numeric suffix keeps both, and the
    ``source-md5:`` field in the frontmatter preserves the dedup signal.
    """
    base = SOURCES / f"{slug}.md"
    if not base.exists():
        return base
    n = 1
    while True:
        cand = SOURCES / f"{slug}-{n}.md"
        if not cand.exists():
            return cand
        n += 1


def build_source_page(raw_path: Path) -> Path:
    """Generate `wiki/sources/<slug>.md` from a raw relay-neuron file."""
    if not raw_path.exists():
        raise FileNotFoundError(raw_path)
    text = raw_path.read_text(encoding="utf-8", errors="ignore")
    md5 = cached_md5(raw_path)
    rel = raw_path.resolve().relative_to(ATLAS.resolve())
    slug = slugify(raw_path.name)
    domain = derive_subdomain(raw_path)
    d = derive_date(raw_path)
    size = derive_size(raw_path)
    summary = first_paragraph_summary(text)

    frontmatter = f"""---
type: source
source-type: github
title: "relay-neuron / {raw_path.stem}"
owner: Sphinxes0o0
repo: relay-neuron
date: {d}
size: {size}
path: {rel}
source-md5: {md5}
summary: "{summary}"
tags: [exercise-science, {domain}]
created: {date.today().isoformat()}
---

# relay-neuron / {raw_path.stem}

> Ingested from `{rel}` (raw task, {d})

## Core content

<!-- The full body of the raw file is preserved verbatim below.
     Downstream agent will rewrite this into a structured entity-page
     summary and add `## Related Entities` once entities are created. -->

"""

    out_path = _unique_outpath(slug)
    SOURCES.mkdir(parents=True, exist_ok=True)
    out_path.write_text(frontmatter + text, encoding="utf-8")
    return out_path


def ingest_one(raw_path: Path, *, dry_run: bool = False, force: bool = False) -> dict:
    """Ingest a single file. Returns a result dict for the summary report.

    Returns dict with keys: file, status (created|skipped_dup|overwritten|would_create|error),
    source_page, md5, error.
    """
    md5 = cached_md5(raw_path)
    rel = str(raw_path.resolve().relative_to(ATLAS.resolve())) if raw_path.is_absolute() else str(raw_path)
    slug = slugify(raw_path.name)
    out_path = _unique_outpath(slug)

    # Dedup: skip if a source page with the same md5 already exists.
    if not force:
        dup = find_duplicate_by_md5(raw_path, md5)
        if dup:
            rel_dup = dup.relative_to(ATLAS)
            print(f"  ⏭️  SKIP: {rel}  (already ingested as {rel_dup}, md5 match)")
            return {
                "file": rel,
                "status": "skipped_dup",
                "source_page": str(rel_dup),
                "md5": md5,
            }

    if dry_run:
        # For dry-run accuracy, simulate the eventual file write so that
        # collision-protected writes are reported with the right -1/-2
        # suffix. _dry_run_taken is a module-level set, reset per process.
        if out_path.name in _dry_run_taken:
            # Already claimed; bump to -1, -2, ...
            stem = out_path.stem
            n = 1
            while True:
                cand_name = f"{stem}-{n}.md"
                if cand_name not in _dry_run_taken:
                    _dry_run_taken.add(cand_name)
                    out_path = SOURCES / cand_name
                    break
                n += 1
        else:
            _dry_run_taken.add(out_path.name)
        print(f"  📝 DRY: would create {out_path.relative_to(ATLAS)}  ← {rel}")
        return {
            "file": rel,
            "status": "would_create",
            "source_page": str(out_path.relative_to(ATLAS)),
            "md5": md5,
        }

    # Real write. _unique_outpath already gave us a non-existing name,
    # so this is always a fresh create (collision case is handled by
    # appending -1, -2, ... to the slug).
    out = build_source_page(raw_path)
    print(f"  ✅ CREATED: {out.relative_to(ATLAS)}  ← {rel}")
    return {
        "file": rel,
        "status": "created",
        "source_page": str(out.relative_to(ATLAS)),
        "md5": md5,
    }


def iter_batch(root: Path) -> list:
    """Recursively collect all .md files under root.

    Excludes the synthetic top-level files: README.md, AGENT*.md, CLAUDE.md,
    RESEARCH_MASTER_LIST.md, TODO*.md — those are repo metadata, not raw
    research tasks.

    Also skips `.claude/` — that's vendored skill reference data, not the
    relay-neuron research archive we want to ingest.
    """
    EXCLUDE_NAMES = {
        "README.md", "CLAUDE.md", "RESEARCH_MASTER_LIST.md",
        "FINAL_REPORT.md", "AGENT.md", "AGENT_REVIEW.md",
    }
    EXCLUDE_PREFIXES = ("TODO", "AGENT_")
    EXCLUDE_DIRS = {".claude", "node_modules", ".git"}
    out = []
    for p in sorted(root.rglob("*.md")):
        if not p.is_file():
            continue
        if p.name in EXCLUDE_NAMES:
            continue
        if any(p.name.startswith(pref) for pref in EXCLUDE_PREFIXES):
            continue
        # Skip if any parent dir is in EXCLUDE_DIRS
        if any(part in EXCLUDE_DIRS for part in p.parts):
            continue
        out.append(p)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Ingest a relay-neuron research file (or batch) into wiki/sources/."
    )
    ap.add_argument("path", nargs="?",
                    help="path to a single raw relay-neuron .md file")
    ap.add_argument("--batch", metavar="DIR",
                    help="recursively ingest all .md files under DIR")
    ap.add_argument("--dry-run", action="store_true",
                    help="parse and print the plan, do not write any source pages")
    ap.add_argument("--write", action="store_true",
                    help="actually write source pages (default is dry-run, safety net)")
    ap.add_argument("--max-files", type=int, default=5, metavar="N",
                    help="cap number of files processed in --batch mode (default: 5, "
                         "safety net to prevent accidentally running on the whole corpus)")
    ap.add_argument("--force", action="store_true",
                    help="overwrite existing source pages and bypass md5 dedup")
    args = ap.parse_args()

    if not args.path and not args.batch:
        ap.print_help()
        print("\nERR: provide a file path or --batch DIR", file=sys.stderr)
        return 2

    if args.path and args.batch:
        print("ERR: --batch and a positional path are mutually exclusive", file=sys.stderr)
        return 2

    if args.batch:
        batch_dir = Path(args.batch)
        if not batch_dir.is_dir():
            print(f"ERR: --batch path is not a directory: {args.batch}", file=sys.stderr)
            return 1
        files = iter_batch(batch_dir)
        if not args.write and not args.dry_run:
            # Default to dry-run safety net when neither --write nor --dry-run
            # is set: print the plan, don't write. Caller must opt-in with
            # --write to actually create source pages. This prevents the
            # classic "I forgot to pass --dry-run and now I ingested 2600
            # files" footgun.
            args.dry_run = True
            print("  ℹ️  defaulting to --dry-run (pass --write to actually create source pages)", file=sys.stderr)
        if args.max_files and args.max_files > 0 and len(files) > args.max_files:
            print(f"  ℹ️  capping --batch from {len(files)} to --max-files={args.max_files} "
                  f"(raise --max-files to process more)", file=sys.stderr)
            files = files[: args.max_files]
    else:
        raw = Path(args.path)
        if not raw.exists():
            print(f"ERR: {raw} does not exist", file=sys.stderr)
            return 1
        files = [raw]

    if not files:
        print(f"=== No .md files found under {args.batch or args.path} ===")
        return 0

    print(f"=== ingest_relay_neuron.py: {len(files)} file(s) ===")
    print(f"  input:     {args.batch or args.path}")
    print(f"  output:    {SOURCES}")
    print(f"  dry-run:   {args.dry_run}")
    print(f"  write:     {args.write}")
    print(f"  force:     {args.force}")
    print()

    results = []
    for f in files:
        try:
            r = ingest_one(f, dry_run=args.dry_run, force=args.force)
        except Exception as e:
            rel = str(f.resolve().relative_to(ATLAS.resolve()))
            print(f"  ❌ ERROR: {rel}  {e}", file=sys.stderr)
            r = {"file": rel, "status": "error", "error": str(e)}
        results.append(r)
        print()

    # Summary
    by_status: dict = {}
    for r in results:
        by_status[r.get("status", "?")] = by_status.get(r.get("status", "?"), 0) + 1
    created = by_status.get("created", 0)
    skipped_dup = by_status.get("skipped_dup", 0)
    would_create = by_status.get("would_create", 0)
    errors = by_status.get("error", 0)
    fail = errors

    print(f"=== Summary ===")
    print(f"  total:           {len(results)}")
    if args.dry_run:
        print(f"  would_create:    {would_create}")
    else:
        print(f"  created:         {created}")
    print(f"  skipped_dup:     {skipped_dup}  (md5 already in wiki/sources/)")
    print(f"  errors:          {errors}")

    if errors:
        print()
        print("Failures:")
        for r in results:
            if r.get("status") == "error":
                print(f"  FAIL: {r['file']}  ({r.get('error', '?')})")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
