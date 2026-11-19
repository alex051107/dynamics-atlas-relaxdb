#!/usr/bin/env python3
"""Deterministic consistency, prose-clarity, and diagram gate for Dynamics Atlas review docs.

Single source of truth:
  - data/v3_draft_20261118/proteins_summary.csv
  - data/v3_draft_20261118/RelaxDB_dynamics_from_papers_DRAFT_20261118.xlsx
  - atlas/all_proteins/*.md

Run from repository root:
  python3 methods/check_review_consistency.py
"""
from __future__ import annotations

import csv
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent

SEALED = {
    "ALP", "ECOADK", "HMG1A", "HMG1B", "MLC1PC", "NUSGTD", "PYP", "VILHP",
    "19335", "CDNFCT", "RNASEHI", "UBE2G1",
}

LIVE_DOCS = [
    "README.md",
    "REVIEW_GUIDE.md",
    "atlas/ATLAS_131.md",
    "methods/how_it_is_built.md",
    "methods/bugs_and_fixes.md",
    "methods/changes_since_v01.md",
    "data/v3_draft_20261118/README.md",
]

DOCS_REQUIRING_MERMAID = [
    "README.md",
    "REVIEW_GUIDE.md",
    "atlas/ATLAS_131.md",
    "methods/bugs_and_fixes.md",
    "methods/changes_since_v01.md",
]

SUPPORTED_MERMAID_HEADERS = (
    "stateDiagram-v2",
    "stateDiagram",
    "flowchart TD",
    "flowchart LR",
    "graph TD",
    "graph LR",
    "sequenceDiagram",
)

# Stale superseded numbers that must NOT appear as current totals in LIVE_DOCS
# (unless explicitly contrasted with the updated value on the same line, e.g. "original 19,958 + 31 = 19,989")
STALE_PATTERNS = [
    (re.compile(r"\b771\s*/\s*771\b"), "stale record count '771 / 771' (current verified total is 776 records / 757 DOIs)"),
    (re.compile(r"(?<!original )(?<!19,958 original )\b19,958\b(?! original)(?!\s*\+\s*31)"), "stale measurement count '19,958' without contrasting against current 19,989"),
    (re.compile(r"\b23\b[^\n]{0,25}\bunread\b", re.I), "stale '23 unread' claim (14 are in Release 0.1, 4 read on 2026-11-19, 2 twins; only 3 paywalled remain)"),
    (re.compile(r"\b104\s*(?:/|of)\s*131\b[^\n]{0,40}(?:open|read|done|today)", re.I), "stale '104/131' current coverage claim (unified coverage is 128/131; v3+supp papers is 108/131)"),
]

BANNED_PROSE_PHRASES = [
    (re.compile(r"—"), "em-dash '—' in prose (use short declarative sentences instead)"),
    (re.compile(r"\bit is worth noting\b", re.I), "filler phrase 'it is worth noting'"),
    (re.compile(r"\bit should be noted\b", re.I), "filler phrase 'it should be noted'"),
    (re.compile(r"\bdoes not mean\b", re.I), "defensive phrase 'does not mean'"),
]

MAX_PROSE_SENTENCE_WORDS = 48


def check_mermaid_blocks(rel: str, text: str, errors: list[str]) -> int:
    blocks = list(re.finditer(r"```mermaid\n(.*?)```", text, re.S))
    for i, m in enumerate(blocks, 1):
        body = m.group(1).strip()
        first_line = body.splitlines()[0].strip() if body else ""
        if not any(first_line.startswith(h) for h in SUPPORTED_MERMAID_HEADERS):
            errors.append(f"{rel}: mermaid block #{i} uses unsupported header {first_line!r}")
        if re.search(r"<br\s*/?>|<b>|<i>|</", body, re.I):
            errors.append(f"{rel}: mermaid block #{i} contains HTML tags (use plain text labels)")
        # Detect unquoted [...] labels containing parentheses
        for line in body.splitlines()[1:]:
            for lbl in re.finditer(r"\[([^\]\"]+)\]", line):
                if "(" in lbl.group(1) or ")" in lbl.group(1):
                    errors.append(
                        f"{rel}: mermaid block #{i} has unquoted parentheses in node [{lbl.group(1)}] "
                        "(quote as [\"...\"])"
                    )
    return len(blocks)


def check_prose_clarity(rel: str, text: str, errors: list[str]) -> None:
    in_code = False
    for lineno, raw in enumerate(text.splitlines(), 1):
        s = raw.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not s or s.startswith(("#", "|", "![", "---")):
            continue
        for pat, msg in BANNED_PROSE_PHRASES:
            if pat.search(s):
                errors.append(f"{rel}:{lineno}: {msg}")
        # Strip markdown links/code for sentence-length check on regular prose
        if s.startswith(">"):
            s_clean = s.lstrip("> ").strip()
        else:
            s_clean = re.sub(r"^[-*]\s+|^\d+\.\s+", "", s)
        # Replace [text](url) with text
        s_clean = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s_clean)
        s_clean = re.sub(r"`[^`]+`", "CODE", s_clean)
        # Split on sentence boundaries
        for sent in re.split(r"(?<=[.!?])\s+", s_clean):
            words = re.findall(r"[A-Za-z0-9_'-]+", sent)
            if len(words) > MAX_PROSE_SENTENCE_WORDS:
                errors.append(
                    f"{rel}:{lineno}: dense sentence ({len(words)} words > {MAX_PROSE_SENTENCE_WORDS}); "
                    f"split into short clear sentences: '{sent[:80]}...'"
                )


def main() -> int:
    errors: list[str] = []

    # 1. Verify source-of-truth counts
    summary_path = REPO / "data/v3_draft_20261118/proteins_summary.csv"
    with open(summary_path, encoding="utf-8") as f:
        prots = list(csv.DictReader(f))
    if len(prots) != 131:
        errors.append(f"proteins_summary.csv: expected 131 open rows, found {len(prots)}")

    atlas_pages = sorted((REPO / "atlas/all_proteins").glob("*.md"))
    if len(atlas_pages) != 131:
        errors.append(f"atlas/all_proteins: expected 131 pages, found {len(atlas_pages)}")

    # 2. Check sealed entries, path leaks, and broken links across repo Markdown (excl. Release 0.1 code/)
    for p in sorted(REPO.rglob("*.md")):
        rel = str(p.relative_to(REPO))
        if rel.startswith("code/"):
            continue
        txt = p.read_text(encoding="utf-8")
        if "/Users/" in txt or "/tmp/" in txt or "dynamics_atlas_eval" in txt:
            errors.append(f"{rel}: local path leak detected")
        if rel.startswith("atlas/all_proteins/") and p.stem in SEALED:
            errors.append(f"{rel}: sealed held-out entry must not appear in atlas/all_proteins/")
        if rel.startswith("atlas/all_proteins/"):
            if "Structure comparison:** []" in txt:
                errors.append(f"{rel}: raw empty JSON list '[]' in Structure comparison")
            secs = [int(m.group(1)) for m in re.finditer(r"^## (\d+)\.", txt, re.M)]
            if secs and secs != list(range(1, len(secs) + 1)):
                errors.append(f"{rel}: non-sequential section headings {secs}")
        for m in re.finditer(r"\[[^\]]+\]\(([^)#]+)", txt):
            t = m.group(1)
            if t.startswith(("http://", "https://", "mailto:")):
                continue
            if not (p.parent / t).resolve().exists():
                errors.append(f"{rel}: broken relative link -> {t}")

    # 3. Live doc checks: stale numbers, Mermaid diagrams, prose clarity
    for rel in LIVE_DOCS:
        p = REPO / rel
        if not p.exists():
            errors.append(f"{rel}: missing live doc")
            continue
        txt = p.read_text(encoding="utf-8")
        for lineno, line in enumerate(txt.splitlines(), 1):
            for pat, reason in STALE_PATTERNS:
                if pat.search(line):
                    errors.append(f"{rel}:{lineno}: {reason}")
        n_mermaid = check_mermaid_blocks(rel, txt, errors)
        if rel in DOCS_REQUIRING_MERMAID and n_mermaid == 0:
            errors.append(
                f"{rel}: missing inline Mermaid diagram (add a stateDiagram-v2 or flowchart answering this page's core logic)"
            )
        check_prose_clarity(rel, txt, errors)

    if errors:
        print(f"FAIL: {len(errors)} review consistency / clarity issues found:")
        for e in errors:
            print("  -", e)
        return 1

    print(
        f"PASS: 131/131 atlas pages, 0 broken links, 0 path leaks, 0 stale counts, "
        f"all Mermaid diagrams valid, and prose clarity checks clean across {len(LIVE_DOCS)} live docs."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
