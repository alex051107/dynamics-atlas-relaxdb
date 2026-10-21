#!/usr/bin/env python3
"""Run the second read with both backends on one case and list every row either reader flags as wrong, plus rows every reader
calls unverified on a paper read in full (E-030).

  dual_read.py CASE [--claude-only]  -> ledger/sr_dual/<CASE>_{codex,claude}.jsonl and ledger/sr_dual/<CASE>_flags.json
"""
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

WORK = Path.home() / "dynamics_atlas_work"
SR = WORK / "ledger/sr_dual"


def main():
    case = sys.argv[1]
    backends = ["claude"] if "--claude-only" in sys.argv else ["codex", "claude"]
    t0 = time.time()
    reads, failed = {}, {}
    rows = [json.loads(x) for x in (WORK / "cases" / case / "rows.jsonl").read_text().splitlines() if x.strip()]
    for b in backends:
        out = WORK / "cases" / case / "second_read.jsonl"
        out.unlink(missing_ok=True)  # never let a failed reader inherit the previous reader's file
        with open(SR / f"{case}_{b}.log", "w") as log:
            rc = subprocess.run([sys.executable, str(WORK / "tools/second_read.py"), case, "--backend", b], stdout=log, stderr=log, cwd=WORK).returncode
        got = [json.loads(x) for x in out.read_text().splitlines() if x.strip()] if out.exists() else []
        if rc != 0 or {r.get("row_number") for r in got} != set(range(1, len(rows) + 1)):
            failed[b] = f"returncode {rc}, {len(got)} of {len(rows)} rows read"
            (SR / f"{case}_{b}.jsonl").unlink(missing_ok=True)
            continue
        shutil.copy(out, SR / f"{case}_{b}.jsonl")
        reads[b] = got
    by = {}
    for b, rs in reads.items():
        for r in rs:
            by.setdefault(r["row_number"], {})[b] = r
    # E-030: a row every reader calls unverified on a paper read in full is also adjudicated (planted errors hid there)
    log = WORK / "cases" / case / "screen_log.jsonl"
    full = {json.loads(x)["doi"].lower() for x in log.read_text().splitlines()
            if x.strip() and json.loads(x).get("status") == "filled"} if log.exists() else set()
    flags = []
    for n, v in sorted(by.items()):
        both_unverified = len(v) == len(reads) and all(x.get("verdict") == "unverified" for x in v.values()) \
            and (rows[n - 1].get("doi") or "").lower() in full
        if any(x.get("verdict") == "wrong" for x in v.values()) or both_unverified:
            row = rows[n - 1]
            flags.append({"row_number": n, "row_id": row.get("row_id"), "doi": row.get("doi"),
                          "why": "all_unverified_full_text" if both_unverified and not any(x.get("verdict") == "wrong" for x in v.values()) else "wrong",
                          "readers": {b: [x.get("verdict"), x.get("reason")] for b, x in v.items()},
                          "row": {k: row.get(k) for k in ("experiment", "method_class", "residues_author", "timescale",
                                                          "population", "temperature", "construct_or_mutation")}})
    counts = {b: {k: sum(1 for r in rs if r.get("verdict") == k) for k in ("ok", "unverified", "wrong")} for b, rs in reads.items()}
    (SR / f"{case}_flags.json").write_text(json.dumps({"case": case, "counts": counts, "failed_readers": failed, "flags": flags}, indent=1, ensure_ascii=False))
    with open(WORK / "ledger/throughput.jsonl", "a") as fh:
        fh.write(json.dumps({"step": "second_read_dual", "case": case, "wall_s": round(time.time() - t0)}) + "\n")
    print(json.dumps({"case": case, "rows": len(rows), "counts": counts, "failed_readers": failed, "flagged": len(flags)}))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
