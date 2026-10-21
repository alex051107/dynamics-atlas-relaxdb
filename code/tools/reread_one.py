#!/usr/bin/env python3
"""Re-run one reader of the dual second read for a case, guarded against the stale-file error (E-032).

  reread_one.py CASE BACKEND   -> ledger/sr_dual/CASE_BACKEND.jsonl only if the read is complete; then recompute flags
"""
import json
import os
import subprocess
import sys
from pathlib import Path

from dual_read import complete, read_rows

WORK = Path(os.environ.get("DYNAMICS_ATLAS_WORK", Path.home() / "dynamics_atlas_work"))
case, backend = sys.argv[1], sys.argv[2]
out = WORK / "cases" / case / "second_read.jsonl"
out.unlink(missing_ok=True)
with open(WORK / "ledger/sr_dual" / f"{case}_{backend}.log", "w") as log:
    rc = subprocess.run([sys.executable, str(WORK / "tools/second_read.py"), case, "--backend", backend], stdout=log, stderr=log, cwd=WORK).returncode
rows = sum(1 for x in (WORK / "cases" / case / "rows.jsonl").read_text().splitlines() if x.strip())
got = read_rows(out)
ok = rc in (0, 2) and complete(got, rows)
if not ok:
    out.unlink(missing_ok=True)
if ok:
    (WORK / "ledger/sr_dual" / f"{case}_{backend}.jsonl").write_text(out.read_text())
    subprocess.run([sys.executable, str(WORK / "tools/dual_read.py"), case, "--reuse"], cwd=WORK, capture_output=True)
print(json.dumps({"case": case, "backend": backend, "returncode": rc, "rows": rows, "read": len(got), "saved": ok}))
sys.exit(0 if ok else 1)
