#!/usr/bin/env python3
"""Run the second read with both backends on one case and list every row either reader flags as wrong, plus rows every reader
calls unverified on a paper read in full (E-030).

  dual_read.py CASE [--claude-only] [--reuse]  -> ledger/sr_dual/<CASE>_{codex,claude}.jsonl and ledger/sr_dual/<CASE>_flags.json
"""
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

WORK = Path(os.environ.get("DYNAMICS_ATLAS_WORK", Path.home() / "dynamics_atlas_work"))
SR = WORK / "ledger/sr_dual"


def read_rows(path):
    try:
        return [json.loads(x) for x in path.read_text().splitlines() if x.strip()]
    except (OSError, ValueError):
        return []


def complete(got, count):
    return len(got) == count and all(isinstance(r, dict) and type(r.get("row_number")) is int for r in got) and {r.get("row_number") for r in got} == set(range(1, count + 1))


def main():
    SR.mkdir(parents=True, exist_ok=True)
    case = sys.argv[1]
    backends = ["claude"] if "--claude-only" in sys.argv else ["codex", "claude"]
    t0 = time.time()
    reads, failed = {}, {}
    rows = [json.loads(x) for x in (WORK / "cases" / case / "rows.jsonl").read_text().splitlines() if x.strip()]
    for b in backends:
        if "--reuse" in sys.argv:  # recompute flags from saved reads in ledger/sr_dual, no new model calls
            got = read_rows(SR / f"{case}_{b}.jsonl")
            if not complete(got, len(rows)):
                failed[b] = f"saved read incomplete: {len(got)} of {len(rows)} rows read"
                continue
            reads[b] = got
            continue
        out = WORK / "cases" / case / "second_read.jsonl"
        out.unlink(missing_ok=True)  # never let a failed reader inherit the previous reader's file
        with open(SR / f"{case}_{b}.log", "w") as log:
            rc = subprocess.run([sys.executable, str(WORK / "tools/second_read.py"), case, "--backend", b], stdout=log, stderr=log, cwd=WORK).returncode
        got = read_rows(out)
        if rc not in (0, 2) or not complete(got, len(rows)):  # 2 = complete read, >5% wrong (blocked), still a valid read
            failed[b] = f"returncode {rc}, {len(got)} of {len(rows)} rows read"
            out.unlink(missing_ok=True)
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
        both_unverified = len(v) == len(backends) and all(x.get("verdict") == "unverified" for x in v.values()) \
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
