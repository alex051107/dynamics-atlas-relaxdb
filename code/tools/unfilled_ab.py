#!/usr/bin/env python3
"""Print the screened A/B DOIs of an entry that no fill case of that entry has taken as input yet.

  unfilled_ab.py ENTRY   (reads outputs/screen/ENTRY.jsonl and cases/*_r6_ENTRY_*/candidates.json; skips ledger/superseded_cases.json)
"""
import json
import sys
from pathlib import Path

WORK = Path.home() / "dynamics_atlas_work"
e = sys.argv[1]
ab = [json.loads(x)["doi"].lower() for x in (WORK / f"outputs/screen/{e}.jsonl").read_text().splitlines()
      if x.strip() and json.loads(x)["tier"] in ("A", "B")]
sup = json.loads((WORK / "ledger/superseded_cases.json").read_text())  # superseded cases do not count as read
done = set()
for c in WORK.glob(f"cases/*_r6_{e}_*/candidates.json"):
    if c.parent.name in sup:
        continue
    done |= {(x.get("doi") or "").lower() for x in json.loads(c.read_text())}
print(" ".join(d for d in ab if d not in done))
