#!/usr/bin/env python3
"""Phase-1 driver: bring the remaining RelaxDB CPMG proteins to the AdK/CheY level.

Per protein: prefetch searches -> one headless `codex exec` worker -> integrity check -> one repair resume if needed.
Usage: phase1_driver.py --round R ENTRY [ENTRY ...]   (runs in parallel, concurrency 2)
Writes ledger/phase1.jsonl. Launched and monitored by Claude (see PLAN_TO_COMPLETION_ZH.md).
"""
import argparse
import concurrent.futures as cf
import json
import os
import shutil
import signal
import subprocess
import sys
import time
import tomllib
from pathlib import Path

WORK = Path.home() / "dynamics_atlas_work"
EVAL = Path.home() / "dynamics_atlas_eval"
CASES, CACHE, LEDGER = WORK / "cases", WORK / "sources_cache", WORK / "ledger"
CODEX = shutil.which("codex") or "/opt/homebrew/bin/codex"
SCHEMA = WORK / "schema/worker_result.schema.json"
TIMEOUT_S = 75 * 60

# First-pass leads from the 09-30 pilot (titles/DOIs only; worker must re-read and verify).
LEADS = {
    "BLAC_CPMG": ["10.1128/AAC.02025-19 (BlaC dynamics, 2020)", "PMC12274840 (G105 resistance, 2025)"],
    "BLVRB_CPMG": ["10.1016/j.jmb.2018.06.015", "10.3389/fmolb.2023.1244587", "10.3389/fmolb.2021.691208",
                   "10.3390/ijms252413233", "10.1093/jb/mvaa039", "10.1038/s41467-025-58497-9"],
    "CYPA_CPMG": ["10.1038/nature08615 (Fraser 2009)", "PMC6815256 (T-jump scattering 2019)",
                  "Eisenmesser 2005 Nature 'Intrinsic dynamics of an enzyme underlies catalysis' (original CPMG; not yet read)"],
    "VHR_CPMG": ["10.1021/acs.biochem.0c00245 (2020)", "PMC5549688 (2017)", "PMC11822521 (2025 fragments, apo crystals 8TK6/9DJ9)",
                 "RelaxDB source: Beaumont dissertation Table 7.10.3 (ProQuest 2395254828)"],
    "ARGKIN_CPMG": ["10.1021/bi101664u (2011)", "PMC2826323 (2009)", "PMC3017626 (2011 RDC)"],
    "RNASE_CPMG": ["10.1021/ja0514949 (Beach 2005)", "10.1021/bi400973e (buffer 2013)", "10.1021/acs.jpcb.5b00212 (pH 2015)"],
    "HTPDZ_CPMG": ["10.1038/s41467-024-48997-5 (2024)", "PMC9170070 (2022)", "PMC5759095 (2018)", "BMRB 51320"],
    "KRAS_CPMG": ["10.1038/s41594-023-01070-z (2023, GTP excited state)", "PMC9804424 (2022, GDP/Mg)"],
    "AQADK_CPMG": ["10.1038/nature06410", "10.1038/nature06407", "10.1038/ncomms10848", "10.1038/nsmb821",
                   "10.1038/s41586-022-04468-9 (check organism; may be a homolog)", "PMC4318763"],
    "CHEY_CPMG": ["PMC3552614 (2012, Table 2)", "PMC3703654 (2013)"],
}

EXTRA = """
## Phase-1 goal for this run
Bring this protein to the level a scientist can review: 4-8 key primary papers (prioritise the RelaxDB source paper and
independent methods), one row per paper/experiment/condition, every number copied as reported with its sample and condition,
the 11-class coverage answered, and a <=600-word summary. Leads from an earlier first pass are listed below; re-read each one
in the original before using it, and search beyond them. Mark homolog or other-construct evidence with species_relation.
"""


def overrides():
    cfg = tomllib.load(open(Path.home() / ".codex/config.toml", "rb"))
    o = ["-c", "notify=[]", "-c", 'model_reasoning_effort="high"', "-c", "features.memories=false",
         "-c", "memories.generate_memories=false", "-c", "memories.use_memories=false",
         "-c", "sandbox_workspace_write.network_access=true"]
    for n in cfg.get("mcp_servers", {}):
        o += ["-c", f'mcp_servers.{n}.enabled=false']
    for n in cfg.get("plugins", {}):
        o += ["-c", f'plugins.{n}.enabled=false']
    return o


def spawn(cmd, cwd, stdin_text, events, timeout_s):
    t0 = time.time()
    with open(events, "w") as out, open(str(events) + ".stderr", "w") as err:
        p = subprocess.Popen(cmd, cwd=str(cwd), stdin=subprocess.PIPE, stdout=out, stderr=err, text=True, start_new_session=True)
        p.stdin.write(stdin_text)
        p.stdin.close()
        status = "exited"
        while p.poll() is None:
            if (EVAL / "STOP").exists():
                status = "stopped"
            elif time.time() - t0 > timeout_s:
                status = "timeout"
            if status != "exited":
                for sig in (signal.SIGTERM, signal.SIGKILL):
                    try:
                        os.killpg(p.pid, sig)
                    except (ProcessLookupError, PermissionError):
                        try:
                            p.send_signal(sig)
                        except ProcessLookupError:
                            break
                    time.sleep(5)
                break
            time.sleep(10)
    return status, round(time.time() - t0)


def thread_id(events):
    for line in Path(events).read_text(errors="replace").splitlines():
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if e.get("type") == "thread.started":
            return e.get("thread_id")
    return None


def integrity(case):
    p = subprocess.run([sys.executable, str(EVAL / "eval/score.py"), str(case), "--integrity-only"], capture_output=True, text=True)
    sc = json.loads((case / "scorecard.json").read_text()) if (case / "scorecard.json").exists() else {}
    return p.returncode, sc.get("integrity", {})


def run_one(entry, rnd):
    case = CASES / f"p1r{rnd}_{entry}"
    if case.exists():
        shutil.rmtree(case)
    case.mkdir(parents=True)
    card = json.loads((WORK / "inputs" / f"{entry}.json").read_text())
    (case / "input.json").write_text(json.dumps(card, indent=1, ensure_ascii=False))
    (case / ".atlas_worker").write_text(json.dumps({"entry": entry, "phase": 1, "round": rnd}))
    rec = {"entry": entry, "round": rnd, "case": case.name, "started": time.strftime("%Y-%m-%dT%H:%M:%S")}
    pre = subprocess.run([sys.executable, str(WORK / "tools/prefetch.py"), "--case", str(case)], capture_output=True, text=True, timeout=1800)
    rec["prefetch"] = (pre.stdout or pre.stderr).strip()[-300:]
    prompt = (WORK / "prompts/worker_v4.md").read_text() + EXTRA + "\nLeads:\n" + "\n".join("- " + x for x in LEADS.get(entry, [])) + \
        "\n\n## This run\n" + f"- Input card:\n```json\n{json.dumps(card, indent=1, ensure_ascii=False)}\n```\n" + \
        f"- Write every output file in the current directory: {case}\n- Shared source cache: {CACHE}\n" + \
        f"- Output contract: {WORK / 'schema/atlas_contract.json'}\n- Finish with the JSON final message required by the output schema.\n"
    base = ["--skip-git-repo-check", "--json", "--output-schema", str(SCHEMA), "-o", str(case / "result.json")] + overrides()
    cmd = [CODEX, "exec", "-C", str(case), "-s", "workspace-write", "--add-dir", str(CACHE)] + base + ["-"]
    rec["status"], rec["wall_s"] = spawn(cmd, case, prompt, case / "events.jsonl", TIMEOUT_S)
    rc, integ = integrity(case)
    rec["integrity_first"] = {"pass": integ.get("pass"), "n_errors": integ.get("n_errors"), "by_kind": integ.get("by_kind")}
    tid = thread_id(case / "events.jsonl")
    if rc == 3 and tid and rec["status"] == "exited":
        msg = ("The integrity check found these problems. Fix them in place in rows.jsonl, coverage.json and summary.md. "
               "Re-open the cited source files and copy anchors and numbers exactly; drop a value you cannot locate. "
               "Do not invent values.\n" + json.dumps(integ.get("errors", [])[:60], ensure_ascii=False))
        rcmd = [CODEX, "exec", "resume", tid, "-c", 'sandbox_mode="workspace-write"',
                "-c", f'sandbox_workspace_write.writable_roots=["{CACHE}"]'] + base + ["-"]
        rec["repair_status"], w2 = spawn(rcmd, case, msg, case / "events_repair.jsonl", TIMEOUT_S // 2)
        rec["wall_s"] += w2
        rc, integ = integrity(case)
    rec["integrity_final"] = {"pass": integ.get("pass"), "n_errors": integ.get("n_errors"), "by_kind": integ.get("by_kind")}
    try:
        rows = [json.loads(x) for x in (case / "rows.jsonl").read_text().splitlines() if x.strip()]
    except Exception:
        rows = []
    rec["n_rows"] = len(rows)
    rec["papers"] = len({r.get("doi") or r.get("title") for r in rows})
    rec["result"] = json.loads((case / "result.json").read_text()) if (case / "result.json").exists() else None
    rec["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    with open(LEDGER / "phase1.jsonl", "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(json.dumps({k: rec[k] for k in ("entry", "status", "wall_s", "n_rows", "papers", "integrity_final")}, ensure_ascii=False), flush=True)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--round", type=int, required=True)
    ap.add_argument("entries", nargs="+")
    a = ap.parse_args()
    with cf.ThreadPoolExecutor(max_workers=2) as ex:
        list(ex.map(lambda e: run_one(e, a.round), a.entries))


if __name__ == "__main__":
    main()
