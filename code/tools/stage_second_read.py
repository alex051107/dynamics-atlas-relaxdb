#!/usr/bin/env python3
"""Stage workbook evidence rows (with source-verified corrections and exclusions applied) as SR_<case> copies for second_read."""
import json
import shutil
from pathlib import Path

WORK = Path.home() / "dynamics_atlas_work"
L = WORK / "ledger"
corr = json.loads((L / "row_corrections.json").read_text())
excl = json.loads((L / "row_exclusions.json").read_text())
for entry, case in json.loads((L / "second_read_workbook_queue.json").read_text()):
    src, dst = WORK / "cases" / case, WORK / "cases" / f"SR_{case}"
    dst.mkdir(exist_ok=True)
    shutil.copyfile(src / "input.json", dst / "input.json")
    rows = []
    for line in (src / "rows.jsonl").read_text().splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        if r.get("row_id") in excl.get(case, {}):
            continue
        for k, v in corr.get(case, {}).get(r.get("row_id"), {}).items():
            if k.endswith("_append"):
                f = {"caveat_append": "caveat_note"}.get(k, k[:-7])
                r[f] = f"{r.get(f) or ''}; {v}".strip("; ")
            else:
                r[k] = v
        rows.append(r)
    (dst / "rows.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    print(dst.name, len(rows))
