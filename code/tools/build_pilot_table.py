#!/usr/bin/env python3
"""Evidence workbook for the RelaxDB-133 transfer pilot (same row format and corrections as build_gina_table.py).

Uses every V6 case of each pilot entry whose integrity check passed (chunked fills give several cases).
  build_pilot_table.py   -> outputs/pilot133/pilot133_evidence.xlsx and evidence_rows.csv
"""
import csv
import json
import os
import sys
from pathlib import Path

from openpyxl import Workbook

sys.path.insert(0, str(Path(__file__).parent))
import build_gina_table as G  # noqa: E402

WORK = Path.home() / "dynamics_atlas_work"
OUT = WORK / "outputs/pilot133"
PILOT = {"4762": "NTRC", "5839": "GB3", "17266": "SILB", "50410": "ALL4940",
         # recall-test sample 2 (2026-10-17)
         "VCPTH": "VCPTH", "RFAHTD": "RFAHTD", "27011": "SIGA", "6838": "PSE4", "REV1CT": "REV1CT", "17701": "YKUD",
         "VILD6": "VILD6", "CDNFCT": "CDNFCT"}


def cases(entry):
    good = []
    s6 = [] if os.environ.get("PILOT_NO_S6") else sorted(G.CASES.glob(f"S6_r6_{entry}_*"))
    sup = json.loads((WORK / "ledger/superseded_cases.json").read_text()) if (WORK / "ledger/superseded_cases.json").exists() else {}
    for p in [p for p in sorted(G.CASES.glob(f"V6_r6_{entry}_*")) + s6 if p.name not in sup]:
        try:
            sc = json.loads((p / "scorecard.json").read_text())
        except (OSError, ValueError):
            continue
        ov = json.loads((G.WORK_LEDGER / "integrity_overrides.json").read_text()).get(p.name, [])
        errs = sc.get("integrity", {}).get("errors") or []
        overridden = bool(errs) and all(any(o["row"] == e.get("row") and o["kind"] == e.get("kind") for o in ov) for e in errs)
        if (sc.get("integrity", {}).get("pass") or overridden) and (p / "rows.jsonl").exists():
            good.append(p)
    return good


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    entries = dict(PILOT)
    for f in sorted((WORK / "outputs/screen").glob("*.jsonl")):  # any other RelaxDB-133 entry with a fill case
        e = f.stem
        if e not in entries and not e.endswith("_CPMG") and "." not in e and list(G.CASES.glob(f"V6_r6_{e}_*")):
            entries[e] = e if not e.isdigit() else f"R{e}"
    G.PREFIX.update(entries)
    rows, used = [], {}
    for e in entries:
        cs = cases(e)
        if cs:
            used[e] = [c.name for c in cs]
            rows.extend(G.rows_from_case(cs[0], e, cs[1:]))
    main_rows = [r for r in rows if not str(r[1]).startswith("C")]
    appendix = [r for r in rows if str(r[1]).startswith("C")]
    wb = Workbook()
    wb.remove(wb.active)
    widths = [9, 14, 24, 30, 30, 22, 28, 24, 32, 34, 30, 32, 30, 32, 32, 36, 22, 20, 12, 30]
    G.sheet(wb.create_sheet("Evidence_rows"), G.COLS, main_rows, widths)
    G.sheet(wb.create_sheet("Appendix_rows"), G.COLS, appendix, widths)
    wb.save(OUT / "pilot133_evidence.xlsx")
    with open(OUT / "evidence_rows.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(G.COLS)
        w.writerows(main_rows + appendix)
    (OUT / "case_sources.json").write_text(json.dumps(used, indent=1))
    print(f"{OUT / 'pilot133_evidence.xlsx'} {len(main_rows)} main rows, {len(appendix)} appendix rows; cases {used}")


if __name__ == "__main__":
    main()
