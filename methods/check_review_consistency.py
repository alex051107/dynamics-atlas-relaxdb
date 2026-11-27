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
import json
import pathlib
import re
import sqlite3
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent

SEALED = {
    "ALP", "ECOADK", "HMG1A", "HMG1B", "MLC1PC", "NUSGTD", "PYP", "VILHP",
    "19335", "CDNFCT", "RNASEHI", "UBE2G1",
}

LIVE_DOCS = [
    "README.md",
    "REVIEW_GUIDE.md",
    "PROPOSED_RULES_20261126.md",
    "ANTHROPIC_HANDOFF.md",
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

# Stale superseded numbers that must NOT appear as uncontrasted current totals in LIVE_DOCS
STALE_PATTERNS = [
    (re.compile(r"\b771\s*/\s*771\b"), "stale record count '771 / 771' (current verified total is 776 records / 757 DOIs)"),
    (re.compile(r"(?<!original )(?<!19,958 original )\b19,958\b(?! original)(?!\s*\+\s*31)"), "stale measurement count '19,958' without contrasting against current 19,989"),
    (re.compile(r"\b23\b[^\n]{0,25}\bunread\b", re.I), "stale '23 unread' claim (14 are in Release 0.1, 4 read on 2026-11-19, 2 twins; only 3 paywalled remain)"),
]

BANNED_PROSE_PHRASES = [
    (re.compile(r"—"), "em-dash '—' in prose (use short declarative sentences instead)"),
    (re.compile(r"\bit is worth noting\b", re.I), "filler phrase 'it is worth noting'"),
    (re.compile(r"\bit should be noted\b", re.I), "filler phrase 'it should be noted'"),
    (re.compile(r"\bdoes not mean\b", re.I), "defensive phrase 'does not mean'"),
]

# Internal batch/version/TLA+ jargon banned from reader-facing prose and statechart labels
# (folder/file paths inside markdown link targets (...) or inline code paths containing '/' are ignored)
BANNED_INTERNAL_JARGON = re.compile(
    r"(?<!-)\b(B1|B2|B3|B5|v3|v4|0\.2-draft|Release 0\.3|Nov-12|Nov 12|Gap 1|Gap 2|"
    r"TypeOK|NoSealedEntryRead|OnlyVerifiedInAtlas|NoUncheckedSampleBinding|"
    r"NoReleaseWithoutExpertAndBacklog|EnforceConditionGate|"
    r"expected_rows|out_of_reach|KEY_FORMAT|A/B/C/X)\b"
)

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


def check_internal_jargon(rel: str, text: str, errors: list[str]) -> None:
    for lineno, raw in enumerate(text.splitlines(), 1):
        # Strip markdown link targets (...), URLs, and inline backtick file paths containing '/'
        s = re.sub(r"\]\([^)]+\)", "]", raw)
        s = re.sub(r"https?://\S+", "", s)
        s = re.sub(r"`[^`]*[/\\][^`]*`", "", s)
        hits = BANNED_INTERNAL_JARGON.findall(s)
        if hits:
            errors.append(
                f"{rel}:{lineno}: confusing internal jargon {sorted(set(hits))} in reader-facing text "
                "(use plain English: 'October baseline', 'current draft', 'next extraction pass')"
            )


def check_prose_clarity(rel: str, text: str, errors: list[str]) -> None:
    in_code = False
    for lineno, raw in enumerate(text.splitlines(), 1):
        s = raw.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not s or s.startswith(("#", "|", "![", "---", ">")):
            continue
        # Strip inline quoted excerpts before prose-style checks so verbatim paper quotes are never flagged
        s_prose = re.sub(r"`\"[^\"]*\"`", "QUOTE", s)
        for pat, msg in BANNED_PROSE_PHRASES:
            if pat.search(s_prose):
                errors.append(f"{rel}:{lineno}: {msg}")
        s_clean = re.sub(r"^[-*]\s+|^\d+\.\s+", "", s_prose)
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
        check_internal_jargon(rel, txt, errors)

    # Also check rendered statechart Mermaid labels for internal jargon
    sc_rel = "methods/statechart/chart.mmd"
    sc_p = REPO / sc_rel
    if sc_p.exists():
        check_internal_jargon(sc_rel, sc_p.read_text(encoding="utf-8"), errors)

    # 4. Recompute frozen Nov 18 SQLite counts live and verify README numbers match disk
    sqlite_path = REPO / "data/expert_review_20261119/RelaxDB_expert_review_DRAFT.sqlite"
    if sqlite_path.is_file():
        con = sqlite3.connect(f"file:{sqlite_path}?mode=ro", uri=True)
        try:
            n_prot = con.execute("SELECT COUNT(*) FROM proteins").fetchone()[0]
            n_read = con.execute("SELECT COUNT(*) FROM proteins WHERE papers_read > 0").fetchone()[0]
            n_raw_m = con.execute("SELECT COUNT(*) FROM proteins WHERE measurements_raw > 0").fetchone()[0]
            n_clean_e = con.execute("SELECT COUNT(DISTINCT entry) FROM measurements_clean").fetchone()[0]
            n_clean = con.execute("SELECT COUNT(*) FROM measurements_clean").fetchone()[0]
            n_quar = con.execute("SELECT COUNT(*) FROM measurements_quarantine").fetchone()[0]
            n_qual = con.execute("SELECT COUNT(*) FROM dyna1_signals").fetchone()[0]
            n_cmp = con.execute("SELECT COUNT(*) FROM region_comparisons").fetchone()[0]
            n_obs = con.execute("SELECT COUNT(*) FROM observations").fetchone()[0]
        finally:
            con.close()
        readme_txt = (REPO / "README.md").read_text(encoding="utf-8")
        for label, needle in [
            ("SQLite open entries", f"`{n_prot}` open entries"),
            ("SQLite papers read entries", f"`{n_read}` with at least 1 paper read"),
            ("SQLite raw measurement entries", f"`{n_raw_m}` with raw measurements"),
            ("SQLite clean numeric entries", f"`{n_clean_e}` with clean numeric rows"),
            ("SQLite clean/quarantine split", f"`{n_clean + n_quar:,} original` measurements = `{n_clean:,}` clean + `{n_quar:,}` quarantined"),
            ("SQLite qualitative signals", f"`{n_qual}` qualitative residue sets"),
            ("SQLite comparisons", f"`{n_cmp}` region comparisons"),
            ("SQLite observations", f"`{n_obs}` observations"),
        ]:
            if needle not in readme_txt:
                errors.append(f"README.md: live SQLite mismatch for {label}; expected snippet {needle!r}")

    # 5. Hygiene for atlas_pipeline/, ANTHROPIC_HANDOFF.md, and Batch 1 open list
    ap_dir = REPO / "atlas_pipeline"
    if ap_dir.is_dir():
        for ap_file in sorted(ap_dir.rglob("*")):
            if not ap_file.is_file() or "__pycache__" in ap_file.parts:
                continue
            rel = str(ap_file.relative_to(REPO))
            if ap_file.suffix.lower() in {".png", ".jpg", ".jpeg", ".pdf"}:
                errors.append(f"{rel}: binary figure or PDF must not live inside atlas_pipeline/")
                continue
            txt = ap_file.read_text(encoding="utf-8", errors="ignore")
            if "/Users/" in txt or "dynamics_atlas_eval" in txt or re.search(r"data:image/[a-zA-Z+.-]+;base64,[A-Za-z0-9+/=]{24,}", txt):
                errors.append(f"{rel}: forbidden local path or embedded data:image URI")

    handoff_p = REPO / "ANTHROPIC_HANDOFF.md"
    if handoff_p.is_file():
        htxt = handoff_p.read_text(encoding="utf-8")
        if re.search(r"\b(?:sealed|held[- ]out)\b", htxt, re.I):
            errors.append("ANTHROPIC_HANDOFF.md: must not mention sealed/held-out entries to external runner")

    b1_p = REPO / "data/batch1_open_proteins_draft.json"
    if b1_p.is_file():
        b1 = json.loads(b1_p.read_text(encoding="utf-8"))
        leaked = {str(e.get("entry", "")).upper() for e in b1.get("entries", [])} & SEALED
        if leaked:
            errors.append(f"data/batch1_open_proteins_draft.json: sealed entries present {sorted(leaked)}")

    if errors:
        print(f"FAIL: {len(errors)} review consistency / clarity issues found:")
        for e in errors:
            print("  -", e)
        return 1

    print(
        f"PASS: 131/131 atlas pages, live SQLite parity verified, 0 broken links, 0 path leaks, "
        f"0 stale counts, all Mermaid diagrams valid, and prose clarity checks clean across {len(LIVE_DOCS)} live docs."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
