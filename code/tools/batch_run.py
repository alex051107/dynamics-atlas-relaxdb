#!/usr/bin/env python3
"""Run the literature line for a batch of RelaxDB entries, one protein at a time (Codex runs are never parallel).

Per entry: identity preflight (stops on a card accession mismatch unless config/identity_overrides.json sets it) -> search config (UniProt names) -> candidates + extra channels -> screen -> fill (chunks of <= 30 A/B papers)
-> dual second read. A fill blocked by the OpenAI bio filter is logged in ledger/bio_blocked.json and re-run with the
Claude backend. Resumable: finished steps are recorded in ledger/<batch>_state.json and skipped.

  batch_run.py BATCH_NAME ENTRY [ENTRY ...]
"""
import json
import math
import subprocess
import sys
import time
from pathlib import Path

WORK = Path.home() / "dynamics_atlas_work"
TOOLS = WORK / "tools"
CHUNK = 30


def sh(args, log):
    with open(log, "a") as fh:
        fh.write(f"\n$ {' '.join(map(str, args))}\n")
        fh.flush()
        return subprocess.run(list(map(str, args)), stdout=fh, stderr=fh, cwd=WORK).returncode


def ab_count(entry):
    p = WORK / "outputs/screen" / f"{entry}.jsonl"
    return sum(json.loads(x)["tier"] in ("A", "B") for x in p.read_text().splitlines() if x.strip()) if p.exists() else None


def fill_cases(entry, since):
    runs = [json.loads(x) for x in (WORK / "ledger/v6_runs.jsonl").read_text().splitlines() if x.strip()]
    return [r for r in runs if r.get("entry") == entry and r.get("stage") == "fill_finished" and r.get("ts", "") >= since]


def bio_blocked(case):
    ev = WORK / "cases" / case / "events.jsonl"
    return ev.exists() and "bio_policy" in ev.read_text(errors="replace")


def main():
    batch, entries = sys.argv[1], sys.argv[2:]
    state_p, log = WORK / f"ledger/{batch}_state.json", WORK / f"ledger/{batch}_run.log"
    state = json.loads(state_p.read_text()) if state_p.exists() else {}
    cfg = json.loads((WORK / "config/pilot_seeds.json").read_text())
    for e in entries:
        st = state.setdefault(e, {})
        t_entry = time.time()

        def done(step, **info):
            st[step] = {"at": time.strftime("%F %T"), **info}
            state_p.write_text(json.dumps(state, indent=1))

        if "identity" not in st:  # E-028: a wrong card accession sends the search to another protein
            sh([sys.executable, TOOLS / "identity_preflight.py", e], log)
            idc = json.loads((WORK / "ledger/identity_preflight.json").read_text()).get(e, {})
            done("identity", status=idc.get("status"), overlap=idc.get("overlap"))
        overrides = json.loads((WORK / "config/identity_overrides.json").read_text()) if (WORK / "config/identity_overrides.json").exists() else {}
        if st["identity"].get("status") == "mismatch" and e not in overrides:
            print(json.dumps({"entry": e, "skipped": "card UniProt does not match card sequence; set config/identity_overrides.json"}), flush=True)
            continue
        if "config" not in st:
            if e not in cfg:
                sh([sys.executable, TOOLS / "auto_config.py", e], log)
            done("config")
        if "candidates" not in st:
            t = time.time()
            if not (WORK / "outputs/candidates" / f"{e}.json").exists():
                sh([sys.executable, TOOLS / "candidates.py", e], log)
            sh([sys.executable, TOOLS / "extra_channels.py", e], log)
            done("candidates", wall_s=round(time.time() - t))
        if "screen" not in st:
            t = time.time()
            if ab_count(e) is None:
                sh([sys.executable, TOOLS / "campaign.py", "screen", "--entries", e], log)
            done("screen", wall_s=round(time.time() - t), ab=ab_count(e))
        if st["screen"].get("ab") is None:  # screening failed (often the bio filter): skip, report, never guess
            print(json.dumps({"entry": e, "skipped": "screen produced no output; see log"}), flush=True)
            continue
        if "fill" not in st and not ab_count(e):
            done("fill", ab=0, chunks=0, cases=[], note="no A/B paper after screening: nothing to read")
        if "fill" not in st:
            n = ab_count(e) or 0
            k = max(1, math.ceil(n / CHUNK))
            since, t, cases = time.strftime("%Y-%m-%dT%H:%M:%S"), time.time(), []
            for i in range(1, k + 1):
                args = [sys.executable, TOOLS / "campaign.py", "fill", "--entries", e] + (["--chunk", f"{i}/{k}"] if k > 1 else [])
                sh(args, log)
                last = fill_cases(e, since)
                case = last[-1]["case"] if last else None
                if case and bio_blocked(case):
                    bb = json.loads((WORK / "ledger/bio_blocked.json").read_text())
                    bb.setdefault(e, {"case": case, "date": time.strftime("%F"), "evidence": "fill events contain bio_policy"})
                    (WORK / "ledger/bio_blocked.json").write_text(json.dumps(bb, indent=1))
                    sh(args + ["--backend", "claude"], log)
                    last = fill_cases(e, since)
                    case = last[-1]["case"] if last else None
                if case:
                    cases.append(case)
            done("fill", wall_s=round(time.time() - t), ab=n, chunks=k, cases=cases)
        if "dual_read" not in st:
            t = time.time()
            blocked = e in json.loads((WORK / "ledger/bio_blocked.json").read_text())
            for case in st["fill"].get("cases", []):
                if (WORK / "cases" / case / "rows.jsonl").exists():
                    sh([sys.executable, TOOLS / "dual_read.py", case] + (["--claude-only"] if blocked else []), log)
            done("dual_read", wall_s=round(time.time() - t))
        st["entry_wall_s"] = round(time.time() - t_entry) + st.get("entry_wall_s", 0)
        state_p.write_text(json.dumps(state, indent=1))
        print(json.dumps({"entry": e, "steps": {k: v for k, v in st.items() if isinstance(v, dict)}}), flush=True)


if __name__ == "__main__":
    main()
