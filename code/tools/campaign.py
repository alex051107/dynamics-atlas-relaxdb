#!/usr/bin/env python3
"""Campaign controller per PREREGISTRATION_ZH.md: layered vs baseline arms over the CPMG proteins.

  campaign.py run --rounds 1 2      run the listed rounds (both arms, concurrency 2), then evaluate and drift-check
  campaign.py screen --entries ENTRY [ENTRY ...]   classify every candidate, at most one screening pass per entry
  campaign.py fill --entries ENTRY [ENTRY ...]     fill screened A/B papers, with v6 budgets and one scoring call
Never deletes a case. Writes ledger/campaign.jsonl, ledger/campaign_config.json (frozen on first run),
ledger/drift_round<R>.json; writes ~/dynamics_atlas_eval/STOP when a drift check fails.
"""
import argparse
import concurrent.futures as cf
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import phase1_driver as P  # noqa: E402
import screen_candidates as S

WORK, EVAL, CASES, CACHE, LEDGER = P.WORK, P.EVAL, P.CASES, P.CACHE, P.LEDGER
MODEL, EFFORT, BUDGET_S, RUN_CAP = "gpt-6-astra", "high", 75 * 60, 20
RECALL_CAP = 14  # amendment 1: 10 proteins + up to 4 restarts
ROUNDS = {1: ["VHR_CPMG"], 2: ["CYPA_CPMG", "BLVRB_CPMG"], 3: ["KRAS_CPMG", "HTPDZ_CPMG"],
          4: ["ARGKIN_CPMG", "RNASE_CPMG"], 5: ["AQADK_CPMG", "CHEY_CPMG"]}
REPEAT = {3: "KRAS_CPMG", 5: "AQADK_CPMG"}
FROZEN = [WORK / "schema/atlas_contract.json", EVAL / "eval/score.py", WORK / "prompts/worker_v4.md", WORK / "prompts/baseline_v1.md"]
ALLOW = ("\nRead only files inside the current case directory and the shared source cache, plus the output contract path given below. "
         "Do not open any other file on this computer.\n")


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def config():
    f = LEDGER / "campaign_config.json"
    if f.exists():
        return json.loads(f.read_text())
    c = {"frozen_at": time.strftime("%Y-%m-%dT%H:%M:%S"), "model": MODEL, "effort": EFFORT, "budget_s": BUDGET_S,
         "run_cap": RUN_CAP, "rounds": ROUNDS, "repeat": REPEAT, "hashes": {str(p): sha(p) for p in FROZEN},
         "leads_sha": hashlib.sha256(json.dumps(P.LEADS, sort_keys=True).encode()).hexdigest()}
    f.write_text(json.dumps(c, indent=1))
    return c


def overrides():
    o = P.overrides()
    i = o.index('model_reasoning_effort="high"')
    del o[i - 1:i + 1]
    return o + ["-c", f'model="{MODEL}"', "-c", f'model_reasoning_effort="{EFFORT}"']


def runs_used():
    return sum(1 for p in list(CASES.glob("L_*")) + list(CASES.glob("B_*")) + list(CASES.glob("R_*")) if p.is_dir())


def new_case(prefix, entry, r, arm):
    case = CASES / f"{prefix}_r{r}_{entry}_{time.strftime('%Y%m%d%H%M%S')}"
    case.mkdir(parents=True)
    card = json.loads((WORK / "inputs" / f"{entry}.json").read_text())
    (case / "input.json").write_text(json.dumps(card, indent=1, ensure_ascii=False))
    (case / ".atlas_worker").write_text(json.dumps({"entry": entry, "arm": arm, "round": r}))
    return case, card


def tail(card, case, extra_paths):
    return (f"\n\n## This run\n- Input card:\n```json\n{json.dumps(card, indent=1, ensure_ascii=False)}\n```\n"
            f"- Write every output file in the current directory: {case}\n" + extra_paths +
            "- Finish with the JSON final message required by the output schema.\n")


def run_layered(entry, r, tag="L"):
    S.validate_backend(entry, "codex")
    case, card = new_case(tag, entry, r, "layered")
    t0 = time.time()
    pre = subprocess.run([sys.executable, str(WORK / "tools/prefetch.py"), "--case", str(case)], capture_output=True, text=True, timeout=1800)
    prompt = (WORK / "prompts/worker_v4.md").read_text() + P.EXTRA + ALLOW + "\nLeads:\n" + \
        "\n".join("- " + x for x in P.LEADS.get(entry, [])) + \
        tail(card, case, f"- Shared source cache: {CACHE}\n- Output contract: {WORK / 'schema/atlas_contract.json'}\n")
    base = ["--skip-git-repo-check", "--json", "--output-schema", str(P.SCHEMA), "-o", str(case / "result.json")] + overrides()
    left = BUDGET_S - (time.time() - t0)
    status, _ = P.spawn([P.CODEX, "exec", "-C", str(case), "-s", "workspace-write", "--add-dir", str(CACHE)] + base + ["-"],
                        case, prompt, case / "events.jsonl", max(60, left))
    rc, integ = P.integrity(case)
    left = BUDGET_S - (time.time() - t0)
    tid = P.thread_id(case / "events.jsonl")
    repaired = None
    if rc == 3 and tid and status == "exited" and left > 600:
        msg = ("The integrity check found these problems. Fix them in place in rows.jsonl, coverage.json and summary.md. "
               "Re-open the cited source files and copy anchors and numbers exactly; drop a value you cannot locate.\n" +
               json.dumps(integ.get("errors", [])[:60], ensure_ascii=False))
        repaired, _ = P.spawn([P.CODEX, "exec", "resume", tid, "-c", 'sandbox_mode="workspace-write"',
                               "-c", f'sandbox_workspace_write.writable_roots=["{CACHE}"]'] + base + ["-"],
                              case, msg, case / "events_repair.jsonl", left)
        rc, integ = P.integrity(case)
    subprocess.run([sys.executable, str(EVAL / "eval/score.py"), str(case)], capture_output=True)
    return record(case, entry, r, "layered", status, time.time() - t0, integ, prefetch=(pre.stdout or "")[-200:], repair=repaired)


def run_baseline(entry, r):
    S.validate_backend(entry, "codex")
    case, card = new_case("B", entry, r, "baseline")
    t0 = time.time()
    prompt = (WORK / "prompts/baseline_v1.md").read_text() + "\nLeads (may be incomplete):\n" + \
        "\n".join("- " + x for x in P.LEADS.get(entry, [])) + tail(card, case, "")
    base = ["--skip-git-repo-check", "--json", "--output-schema", str(P.SCHEMA), "-o", str(case / "result.json")] + overrides()
    status, _ = P.spawn([P.CODEX, "exec", "-C", str(case), "-s", "workspace-write"] + base + ["-"],
                        case, prompt, case / "events.jsonl", BUDGET_S)
    return record(case, entry, r, "baseline", status, time.time() - t0, {})


def record(case, entry, r, arm, status, wall, integ, **extra):
    events = (case / "events.jsonl").read_text(errors="replace") if (case / "events.jsonl").exists() else ""
    rec = {"case": case.name, "entry": entry, "round": r, "arm": arm, "status": status, "wall_s": round(wall),
           "bio_policy_block": "bio_policy" in events or "biological risk" in events,
           "integrity": {k: integ.get(k) for k in ("pass", "n_errors", "by_kind")}, **extra}
    with open(LEDGER / "campaign.jsonl", "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(json.dumps(rec, ensure_ascii=False), flush=True)
    return rec


def drift(r, cfg):
    fails, warns = [], []
    recs = [json.loads(x) for x in (LEDGER / "campaign.jsonl").read_text().splitlines() if x.strip()]
    window = [x for x in recs if x["round"] in (r - 1, r)]
    for e in {x["entry"] for x in window}:
        ok = []
        for x in window:
            if x["entry"] == e and x["arm"] == "layered" and (x.get("integrity") or {}).get("pass"):
                rows = []
                try:
                    rows = [json.loads(l) for l in (CASES / x["case"] / "rows.jsonl").read_text().splitlines() if l.strip()]
                except OSError:
                    pass
                if len({rw.get("doi") or rw.get("title") for rw in rows}) >= 4:
                    ok.append(x["case"])
        if not ok:
            fails.append(f"{e}: no layered case passing integrity with >=4 papers")
    for x in window:
        kinds = (x.get("integrity") or {}).get("by_kind") or {}
        if kinds.get("leakage_gold_path") or kinds.get("leakage_label_string"):
            fails.append(f"{x['case']}: leakage hit")
        if x["arm"] == "baseline" and ((CASES / x["case"] / "coverage.json").exists() or (CASES / x["case"] / "prefetch").exists()):
            fails.append(f"{x['case']}: baseline contaminated with layered artefacts")
        if x.get("bio_policy_block"):
            warns.append(f"{x['case']}: blocked by provider bio-risk filter")
    for p, h in cfg["hashes"].items():
        if sha(p) != h:
            fails.append(f"frozen file changed: {p}")
    if runs_used() > cfg["run_cap"]:
        fails.append(f"run cap exceeded: {runs_used()} > {cfg['run_cap']}")
    out = {"round": r, "fails": fails, "warns": warns, "at": time.strftime("%Y-%m-%dT%H:%M:%S")}
    (LEDGER / f"drift_round{r}.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    if fails:
        (EVAL / "STOP").write_text(json.dumps(out, ensure_ascii=False))
    return out


def run_recall(entry, r=9):
    """Amendment 1: worker_v5 over the citation-graph candidate list."""
    S.validate_backend(entry, "codex")
    case, card = new_case("R", entry, r, "recall")
    t0 = time.time()
    cand = json.loads((WORK / "outputs/candidates" / f"{entry}.json").read_text())
    (case / "candidates.json").write_text(json.dumps(cand["candidates"], indent=1, ensure_ascii=False))
    (case / "candidate_search_status.json").write_text(json.dumps({k: cand.get(k) for k in ("search_status", "failed_requests", "truncated", "kept")}, indent=1))
    subprocess.run([sys.executable, str(WORK / "tools/prefetch.py"), "--case", str(case)], capture_output=True, text=True, timeout=1800)
    prompt = (WORK / "prompts/worker_v5.md").read_text() + P.EXTRA + "\nLeads:\n" + \
        "\n".join("- " + x for x in P.LEADS.get(entry, [])) + \
        tail(card, case, f"- Shared source cache: {CACHE}\n- Output contract: {WORK / 'schema/atlas_contract.json'}\n")
    base = ["--skip-git-repo-check", "--json", "--output-schema", str(P.SCHEMA), "-o", str(case / "result.json")] + overrides()
    left = BUDGET_S - (time.time() - t0)
    status, _ = P.spawn([P.CODEX, "exec", "-C", str(case), "-s", "workspace-write", "--add-dir", str(CACHE)] + base + ["-"],
                        case, prompt, case / "events.jsonl", max(60, left))
    rc, integ = P.integrity(case)
    left = BUDGET_S - (time.time() - t0)
    tid = P.thread_id(case / "events.jsonl")
    if rc == 3 and tid and status == "exited" and left > 600:
        msg = ("The integrity check found these problems. Fix them in place in rows.jsonl, coverage.json and summary.md. "
               "Re-open the cited source files and copy anchors and numbers exactly; drop a value you cannot locate.\n" +
               json.dumps(integ.get("errors", [])[:60], ensure_ascii=False))
        P.spawn([P.CODEX, "exec", "resume", tid, "-c", 'sandbox_mode="workspace-write"',
                 "-c", f'sandbox_workspace_write.writable_roots=["{CACHE}"]'] + base + ["-"], case, msg, case / "events_repair.jsonl", left)
        rc, integ = P.integrity(case)
    subprocess.run([sys.executable, str(EVAL / "eval/score.py"), str(case)], capture_output=True)
    return record(case, entry, r, "recall_v5", status, time.time() - t0, integ)


def select_fill_candidates(candidates, screened):
    S.validate_rows(screened, candidates, S.method_keys())
    selected = []
    excluded = []
    for candidate, decision in zip(candidates, screened):
        if decision["tier"] in {"A", "B"}:
            selected.append({**candidate, "doi": decision["doi"], "screen": decision})
        elif decision["tier"] == "C":
            excluded.append({"doi": decision["doi"], "title": candidate.get("title", ""), "reason": "tier C, not filled"})
    selected.sort(key=lambda candidate: candidate["screen"]["tier"])
    return selected, excluded


def fill_command(case, backend="codex"):
    if backend == "claude":
        return [S.shutil.which("claude") or "claude", "-p", "--output-format", "json",
                "--max-budget-usd", "15", "--model", "claude-opus-5-5",
                "--permission-mode", "acceptEdits", "--add-dir", str(case), "--add-dir", str(CACHE),
                "--allowedTools", "Read,Write,Edit,Bash,WebFetch"]
    return [P.CODEX, "exec", "-C", str(case), "-s", "workspace-write", "--add-dir", str(CACHE),
            "--skip-git-repo-check", "--json", "--output-schema", str(P.SCHEMA), "-o", str(case / "result.json"),
            "-c", "sandbox_workspace_write.network_access=true"] + S.worker_overrides("high") + ["-"]


def run_fill(entry, backend="codex", chunk=None, only_dois=None):
    """chunk=(k, n): fill only the k-th of n consecutive slices of the A-then-B list (for entries with many papers).
    only_dois: re-read just these screened A/B papers from newly supplied full text (case prefix S6, own budget)."""
    card = S.check_entry(entry, backend)
    records = S.run_records()
    launches = [record for record in records if record.get("stage") == "fill_worker_started"]
    if only_dois:
        s6 = [r for r in launches if r.get("case", "").startswith(f"S6_r6_{entry}_")]
        if len(s6) >= 4:
            raise RuntimeError("full-text re-read budget exhausted for this entry")
        launches = []
    pilot = not entry.endswith("_CPMG")  # RelaxDB-133 transfer pilot has its own launch budget (2026-10-15)
    launches = [record for record in launches if record.get("entry", "").endswith("_CPMG") != pilot]
    if pilot:  # pilot budget is per batch: count launches since FILL_BUDGET_SINCE, cap FILL_BUDGET (default 30)
        launches = [r for r in launches if r.get("ts", "") >= os.environ.get("FILL_BUDGET_SINCE", "")]
    if len(launches) >= (int(os.environ.get("FILL_BUDGET", "30")) if pilot else 6) or sum(record.get("entry") == entry for record in launches) >= (4 if pilot else 2):
        raise RuntimeError("v6 filling run budget exhausted")
    candidates = S.candidates_for(entry)
    screened = [json.loads(line) for line in (WORK / "outputs/screen" / f"{entry}.jsonl").read_text().splitlines() if line.strip()]
    selected, excluded = select_fill_candidates(candidates, screened)
    if only_dois:
        want = {S.normalize_doi(d) for d in only_dois}
        missing = want - {c["doi"] for c in selected}
        if missing:
            raise ValueError(f"only_dois not among screened A/B papers: {sorted(missing)}")
        selected = [c for c in selected if c["doi"] in want]
        excluded = []
    if chunk:
        k, n = chunk
        size = -(-len(selected) // n)
        other = selected[:(k - 1) * size] + selected[k * size:]
        selected = selected[(k - 1) * size:k * size]
        excluded = excluded + [{"doi": c["doi"], "title": c.get("title", ""), "reason": f"tier {c['screen']['tier']}, other fill chunk"}
                               for c in other]
    case, card = new_case("S6" if only_dois else "V6", entry, 6,
                          "fulltext_reread" if only_dois else ("fill_v6" if not chunk else f"fill_v6_chunk{chunk[0]}of{chunk[1]}"))
    if not card.get("name"):
        card = {**card, "name": entry.removesuffix("_CPMG")}
        (case / "input.json").write_text(json.dumps(card, indent=1, ensure_ascii=False))
    (case / "candidates.json").write_text(json.dumps(selected, indent=1, ensure_ascii=False))
    (case / "not_read_in_full.json").write_text(json.dumps(excluded, indent=1, ensure_ascii=False))
    (case / "rows.jsonl").touch()
    (case / "screen_log.jsonl").touch()
    (case / "search_log.jsonl").touch()
    (case / "summary.md").write_text("Filling has not completed.\n")
    started = time.monotonic()
    S.append_run({"entry": entry, "stage": "fill_started", "case": case.name, "selected_count": len(selected)}, backend)
    try:
        S.check_stop()
        prefetch = S.spawn_worker([sys.executable, str(WORK / "tools/prefetch.py"), "--case", str(case)],
                                  case, "", case / "prefetch.events.jsonl", min(600, BUDGET_S))
        (case / "prefetch_run.json").write_text(json.dumps(prefetch, indent=2))
        S.check_stop()
        if prefetch["status"] != "exited" or prefetch["returncode"] != 0:
            raise RuntimeError("prefetch failed; no fill worker launched")
        prompt = (WORK / "prompts/worker_v6_fill.md").read_text() + tail(card, case,
            f"- Shared source cache: {CACHE}\n- Output contract: {WORK / 'schema/atlas_contract.json'}\n"
            f"- Already-screened selected papers: {len(selected)}; complete all, not only the first eight.\n")
        command = fill_command(case, backend)
        S.append_run({"entry": entry, "stage": "fill_worker_started", "case": case.name,
                      "events": str((case / "events.jsonl").relative_to(WORK))}, backend)
        receipt = S.spawn_worker(command, case, prompt, case / "events.jsonl",
                                 max(1, BUDGET_S - (time.monotonic() - started)))
        S.check_stop()
        if receipt["status"] != "exited" or receipt["returncode"] != 0:
            raise RuntimeError("fill worker failed; no retry or scoring")
        if backend == "claude":
            receipt.update(S.save_claude_result(case / "events.jsonl", case / "result.json"))
        unread = json.loads((case / "not_read_in_full.json").read_text())
        excluded_keys = {(paper["doi"], paper["title"]) for paper in excluded}
        unread = [paper for paper in unread if (paper.get("doi"), paper.get("title")) not in excluded_keys]
        (case / "not_read_in_full.json").write_text(json.dumps(excluded + unread, indent=1, ensure_ascii=False))
        score = S.spawn_worker([sys.executable, str(EVAL / "eval/score.py"), str(case)],
                               case, "", case / "score.events.jsonl", 300)
        S.check_stop()
        (case / "score_run.json").write_text(json.dumps(score, indent=2))
        scorecard = json.loads((case / "scorecard.json").read_text()) if (case / "scorecard.json").exists() else {}
        integrity = scorecard.get("integrity", {})
        rows = [json.loads(line) for line in (case / "rows.jsonl").read_text().splitlines() if line.strip()]
        log = [json.loads(line) for line in (case / "screen_log.jsonl").read_text().splitlines() if line.strip()]
        selected_dois = {candidate["doi"] for candidate in selected}
        fill_errors = []
        if len(log) != len(selected) or [item.get("doi") for item in log] != [item["doi"] for item in selected]:
            fill_errors.append("completion log must contain every selected paper in A-before-B order")
        if any(row.get("doi") not in selected_dois for row in rows):
            fill_errors.append("rows contain a paper outside the selected A/B list")
        if any("not_screened" in json.dumps(item) for item in log):
            fill_errors.append("completion log contains not_screened")
        result = json.loads((case / "result.json").read_text()) if (case / "result.json").exists() else None
        output = {"entry": entry, "backend": backend, "stage": "fill_finished", "case": case.name, **receipt,
                  "wall_s": round(time.monotonic() - started, 2), "score_returncode": score["returncode"],
                  "integrity": {key: integrity.get(key) for key in ("pass", "n_errors", "by_kind")},
                  "n_rows": len(rows), "papers": len({row.get("doi") or row.get("title") for row in rows}),
                  "not_screened": sum("not_screened" in json.dumps(item) for item in log),
                  "fill_errors": fill_errors, "result": result,
                  "events": str((case / "events.jsonl").relative_to(WORK))}
        if (fill_errors or score["status"] != "exited" or score["returncode"] != 0
                or not integrity.get("pass") or not result or result.get("status") != "done"):
            output["status"] = "failed"
        S.append_run(output)
        record(case, entry, 6, "fill_v6", output["status"], output["wall_s"], integrity, backend=backend)
        return output
    except Exception as error:
        S.append_run({"entry": entry, "stage": "fill_finished", "case": case.name, "status": "failed",
                      "error": str(error), "wall_s": round(time.monotonic() - started, 2),
                      "events": str((case / "events.jsonl").relative_to(WORK))}, backend)
        raise


def drift_recall(cfg):
    fails, warns = [], []
    recs = [json.loads(x) for x in (LEDGER / "campaign.jsonl").read_text().splitlines() if x.strip()]
    for x in [r for r in recs if r["arm"] == "recall_v5"]:
        kinds = (x.get("integrity") or {}).get("by_kind") or {}
        if kinds.get("leakage_gold_path") or kinds.get("leakage_label_string"):
            fails.append(f"{x['case']}: leakage hit")
        if x.get("bio_policy_block"):
            warns.append(f"{x['case']}: provider bio-risk filter")
        if not (x.get("integrity") or {}).get("pass"):
            warns.append(f"{x['case']}: integrity not passed")
    for p in [WORK / "schema/atlas_contract.json", EVAL / "eval/score.py", WORK / "prompts/worker_v5.md"]:
        key = str(p)
        h = sha(p)
        reg = LEDGER / "recall_hashes.json"
        hs = json.loads(reg.read_text()) if reg.exists() else {}
        if key not in hs:
            hs[key] = h
            reg.write_text(json.dumps(hs, indent=1))
        elif hs[key] != h:
            fails.append(f"frozen file changed: {key}")
    if sum(1 for p in CASES.glob("R_*") if p.is_dir()) > RECALL_CAP:
        fails.append("recall run cap exceeded")
    out = {"phase": "recall", "fails": fails, "warns": warns, "at": time.strftime("%Y-%m-%dT%H:%M:%S")}
    with open(LEDGER / "drift_recall.jsonl", "a") as f:
        f.write(json.dumps(out, ensure_ascii=False) + "\n")
    if fails:
        (EVAL / "STOP").write_text(json.dumps(out, ensure_ascii=False))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["run", "recall", "screen", "fill"])
    ap.add_argument("--rounds", type=int, nargs="*", default=[])
    ap.add_argument("--entries", nargs="*", default=[])
    ap.add_argument("--backend", choices=("codex", "claude"), default="codex")
    ap.add_argument("--chunk", default="", help="K/N: fill only slice K of N (fill only)")
    ap.add_argument("--only-doi", nargs="*", default=[], help="re-read only these A/B papers (new full text)")
    a = ap.parse_args()
    if a.cmd in {"screen", "fill"}:
        if not a.entries:
            ap.error("screen/fill require --entries")
        failed = False
        for entry in a.entries:
            S.check_stop()
            try:
                if a.cmd == "screen":
                    S.run_screen(entry, a.backend)
                else:
                    result = run_fill(entry, a.backend, tuple(map(int, a.chunk.split("/"))) if a.chunk else None,
                                      a.only_doi or None)
                    failed = failed or result["status"] != "exited"
            except (RuntimeError, ValueError, OSError) as error:
                S.check_stop()
                failed = True
                print(json.dumps({"entry": entry, "stage": a.cmd, "error": str(error)}, ensure_ascii=False), flush=True)
        if failed:
            raise SystemExit(1)
        return
    legacy_entries = a.entries if a.cmd == "recall" else [entry for round_id in a.rounds for entry in ROUNDS[round_id]]
    for entry in legacy_entries:
        S.validate_backend(entry, "codex")
    if a.backend != "codex":
        ap.error("--backend is supported only for screen/fill")
    cfg = config()
    if a.cmd == "recall":
        done_r = sum(1 for p in CASES.glob("R_*") if p.is_dir())
        for i in range(0, len(a.entries), 2):
            if (EVAL / "STOP").exists():
                print(json.dumps({"stopped": True}))
                return
            batch = a.entries[i:i + 2]
            if done_r + len(batch) > RECALL_CAP:
                print(json.dumps({"recall_cap": RECALL_CAP, "used": done_r}))
                return
            with cf.ThreadPoolExecutor(max_workers=2) as ex:
                list(ex.map(run_recall, batch))
            done_r += len(batch)
            d = drift_recall(cfg)
            print(json.dumps({"drift": d}, ensure_ascii=False), flush=True)
            if d["fails"]:
                return
        return
    cfg = config()
    for r in a.rounds:
        if (EVAL / "STOP").exists():
            print(json.dumps({"stopped_before_round": r}))
            return
        jobs = [(run_layered, e, r) for e in ROUNDS[r]] + [(run_baseline, e, r) for e in ROUNDS[r]]
        if r in REPEAT:
            jobs.append((lambda e, rr: run_layered(e, rr, tag="L_rep"), REPEAT[r], r))
        if runs_used() + len(jobs) > cfg["run_cap"]:
            print(json.dumps({"run_cap": cfg["run_cap"], "used": runs_used(), "needed": len(jobs)}))
            return
        with cf.ThreadPoolExecutor(max_workers=2) as ex:
            list(ex.map(lambda j: j[0](j[1], j[2]), jobs))
        subprocess.run([sys.executable, str(EVAL / "eval/compare.py"), "round", str(r)], capture_output=True)
        if r % 2 == 0 or r == max(ROUNDS):
            d = drift(r, cfg)
            print(json.dumps({"drift": d}, ensure_ascii=False), flush=True)
            if d["fails"]:
                return


if __name__ == "__main__":
    main()
