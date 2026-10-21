#!/usr/bin/env python3
"""Apply the E-029 rule to existing screen files: a RelaxDB source paper screened C/X is promoted to tier A.

  promote_source_papers.py [--write]   -> prints entry, doi, old tier; --write rewrites outputs/screen/<entry>.jsonl
"""
import json
import sys
from pathlib import Path

WORK = Path.home() / "dynamics_atlas_work"
src = json.loads((WORK / "config/relaxdb_source_dois.json").read_text())
for entry, dois in src.items():
    p = WORK / f"outputs/screen/{entry}.jsonl"
    if not p.exists():
        continue
    rows = [json.loads(x) for x in p.read_text().splitlines() if x.strip()]
    want, hit = {d.lower() for d in dois}, False
    for r in rows:
        if r.get("doi", "").lower() in want and r.get("tier") not in ("A", "B"):
            print(entry, r["doi"], r["tier"])
            r.update(tier="A", needs_full_text=True,
                     reason=f"RelaxDB source paper (promoted from {r['tier']}): {r.get('reason', '')}")
            hit = True
    found = {r.get("doi", "").lower() for r in rows}
    for d in want - found:
        print(entry, d, "not among candidates")
    if hit and "--write" in sys.argv:
        p.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
