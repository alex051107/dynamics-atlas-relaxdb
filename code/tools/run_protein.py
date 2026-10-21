#!/usr/bin/env python3
"""Run one protein through cached preparation and fail-closed export gates."""

import argparse
from datetime import datetime
import json
from pathlib import Path
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import campaign
import screen_candidates as screen
import second_read


ROOT = Path(__file__).resolve().parents[1]
STEPS = ("candidates", "screen", "fill", "integrity", "second_read", "judgment_check", "review_gate", "export_gate")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def timestamp():
    return datetime.now().astimezone().isoformat(timespec="seconds")


class GateFailure(RuntimeError):
    def __init__(self, reason, status="failed", errors=None):
        super().__init__(reason)
        self.status = status
        self.errors = errors or []


class ProteinDriver:
    def __init__(self, entry, backend="codex", root=ROOT, stop=None, second_read_backend=None):
        screen.validate_backend(entry, backend)
        second_read.validate_backend(entry, second_read_backend or backend)
        self.entry = entry
        self.backend = backend
        self.second_read_backend = second_read_backend or backend
        self.root = Path(root)
        self.stop = Path(stop) if stop is not None else screen.STOP
        self.state_path = self.root / "state" / f"{entry}.json"
        self.case = None
        self.state = {"entry": entry, "backend": backend, "second_read_backend": self.second_read_backend, "case": None, "steps": {
            step: {"status": "pending", "input_files": [], "output_files": [],
                   "started_at": None, "ended_at": None, "failure_reason": None}
            for step in STEPS}}
        for step, record in self.state["steps"].items():
            record["input_files"], record["output_files"] = self.files_for(step)

    def check_stop(self):
        if self.stop.exists():
            raise GateFailure("STOP exists; no further runs are allowed", "blocked")

    def save(self):
        self.state["updated_at"] = timestamp()
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.state_path.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(self.state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        temporary.replace(self.state_path)

    def files_for(self, step):
        entry = self.entry
        candidates = f"outputs/candidates/{entry}.json"
        screened = f"outputs/screen/{entry}.jsonl"
        judgment = f"outputs/judgment_v0/{entry}.json"
        case = str(self.case.relative_to(self.root)) if self.case else f"cases/V6_*_{entry}_*"
        files = {
            "candidates": ([f"inputs/{entry}.json"], [candidates]),
            "screen": ([f"inputs/{entry}.json", candidates], [screened]),
            "fill": ([candidates, screened], [f"{case}/{name}" for name in (
                "rows.jsonl", "coverage.json", "screen_log.jsonl", "not_read_in_full.json",
                "summary.md", "search_log.jsonl", "scorecard.json")]),
            "integrity": ([f"{case}/scorecard.json", f"{case}/rows.jsonl"], [str(self.state_path)]),
            "second_read": ([f"{case}/rows.jsonl", "sources_cache/"], [f"{case}/second_read.jsonl", "ledger/v6_runs.jsonl"]),
            "judgment_check": ([judgment, "schema/judgment_contract.json"], [str(self.state_path)]),
            "review_gate": (["ledger/judgment_reviewed.json"], [str(self.state_path)]),
            "export_gate": ([str(self.state_path), "ledger/judgment_reviewed.json"], [
                "outputs/gina_review_round1/RelaxDB_CPMG_evidence_round1.xlsx",
                "outputs/gina_review_round1/evidence_rows.csv", "outputs/gina_review_round1/case_sources.json"]),
        }
        return files[step]

    def run_command(self, command, step, timeout_s=600):
        self.check_stop()
        events = self.state_path.parent / f"{self.entry}.{step}.events.log"
        receipt = screen.spawn_worker(command, self.root, "", events, timeout_s)
        self.check_stop()
        if receipt["status"] != "exited" or receipt["returncode"] != 0:
            raise GateFailure(f"{step} command failed: {receipt}; see {events}")

    def run_candidates(self):
        self.run_command([sys.executable, str(self.root / "tools/candidates.py"), self.entry], "candidates", 4500)

    def run_second_read(self):
        try:
            return second_read.run_case(self.case, self.second_read_backend, root=self.root, stop_check=self.check_stop)
        except second_read.SecondReadFailure as error:
            self.state["steps"]["second_read"]["summary"] = error.summary
            raise

    def run_judgment(self):
        self.check_stop()
        result = subprocess.run([sys.executable, str(self.root / "tools/check_judgment.py"),
                                 self.entry, "--dry-run"], cwd=self.root, capture_output=True, text=True, timeout=300)
        self.check_stop()
        try:
            reports = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
        except ValueError as error:
            raise GateFailure(f"judgment checker returned invalid output: {error}") from error
        if len(reports) != 1 or reports[0].get("entry") != self.entry:
            raise GateFailure("judgment checker did not return this protein's report")
        report = reports[0]
        if result.returncode != 0 or report.get("pass") is not True:
            raise GateFailure("判断检查不通过；判断编号及错误：" + json.dumps(report.get("errors", []), ensure_ascii=False),
                              errors=report.get("errors", []))

    def run_export(self):
        self.run_command([sys.executable, str(self.root / "tools/build_gina_table.py")], "export_gate")

    def candidate_list(self):
        data = read_json(self.root / "outputs/candidates" / f"{self.entry}.json")
        if not isinstance(data, dict) or data.get("search_status") != "complete" or not isinstance(data.get("candidates"), list):
            raise GateFailure("candidate search is not complete")
        return data["candidates"]

    def latest_case(self):
        cases = sorted((self.root / "cases").glob(f"V6_*_{self.entry}_*"), reverse=True)
        return next((case for case in cases if case.is_dir() and not case.is_symlink()), None)

    def perform(self, step):
        if step == "candidates":
            path = self.root / "outputs/candidates" / f"{self.entry}.json"
            if path.exists() and read_json(path).get("search_status") == "complete":
                self.candidate_list()
                return True
            self.run_candidates()
            self.check_stop()
            self.candidate_list()
        elif step == "screen":
            path = self.root / "outputs/screen" / f"{self.entry}.jsonl"
            count = len(self.candidate_list())
            if path.exists() and len([line for line in path.read_text().splitlines() if line.strip()]) == count:
                return True
            screen.run_screen(self.entry, backend=self.backend)
            self.check_stop()
            if not path.exists() or len([line for line in path.read_text().splitlines() if line.strip()]) != count:
                raise GateFailure("screening does not cover every candidate")
        elif step == "fill":
            self.case = self.latest_case()
            if self.case:
                self.state["case"] = str(self.case.relative_to(self.root))
                score_path = self.case / "scorecard.json"
                if not score_path.exists():
                    raise GateFailure("latest fill has no scorecard; no automatic retry")
                if read_json(score_path).get("integrity", {}).get("pass") is True:
                    return True
                return False
            result = campaign.run_fill(self.entry, backend=self.backend)
            self.check_stop()
            case_name = result.get("case", "")
            if not case_name.startswith("V6_") or Path(case_name).name != case_name or f"_{self.entry}_" not in case_name:
                raise GateFailure("fill returned an invalid case directory")
            self.case = self.root / "cases" / case_name
            self.state["case"] = str(self.case.relative_to(self.root))
            integrity_failed = result.get("integrity", {}).get("pass") is False
            completed = (result.get("returncode") == 0 and not result.get("fill_errors")
                         and isinstance(result.get("result"), dict) and result["result"].get("status") == "done")
            if result.get("status") != "exited" and not (integrity_failed and completed):
                raise GateFailure(f"fill failed: {result.get('error') or result.get('status')}")
            if not (self.case / "scorecard.json").exists():
                raise GateFailure("fill produced no scorecard")
        elif step == "integrity":
            score_path = self.case / "scorecard.json"
            integrity = read_json(score_path).get("integrity", {})
            if integrity.get("pass") is not True or integrity.get("n_errors", 0) or integrity.get("errors"):
                errors = integrity.get("errors", [])
                detail = json.dumps(errors or integrity.get("by_kind", {}), ensure_ascii=False)
                raise GateFailure("integrity 不通过；行号及错误类型：" + detail, errors=errors)
            changed = [name for name in ("rows.jsonl", "coverage.json", "screen_log.jsonl")
                       if (self.case / name).exists() and (self.case / name).stat().st_mtime_ns > score_path.stat().st_mtime_ns]
            if changed:
                raise GateFailure("scorecard is stale; rescore changed files before export: " + ", ".join(changed),
                                  errors=[{"kind": "stale_scorecard", "files": changed}])
        elif step == "second_read":
            report = self.run_second_read()
            self.state["steps"][step]["summary"] = report
            wrong_per_100 = report.get("wrong_per_100", report.get("errors_per_100"))
            if (report.get("status") not in {"done", "blocked"} or wrong_per_100 is None
                    or not report.get("total_rows") or report.get("checked_rows") != report["total_rows"]):
                raise GateFailure("二读未完成；拒绝进入判断检查", errors=report.get("errors", []))
            if wrong_per_100 > 5:
                raise GateFailure(f"二读矛盾率 {wrong_per_100}/100 超过 5/100；行号：{report['wrong_rows']}",
                                  "blocked", errors=report["errors"])
        elif step == "judgment_check":
            if not (self.root / "outputs/judgment_v0" / f"{self.entry}.json").exists():
                raise GateFailure("判断层未起草", "blocked")
            self.run_judgment()
        elif step == "review_gate":
            path = self.root / "ledger/judgment_reviewed.json"
            if not path.exists() or self.entry not in read_json(path):
                raise GateFailure("审查台账没有这个蛋白；拒绝导出", "blocked")
        elif step == "export_gate":
            blockers = [name for name in STEPS[:-1] if self.state["steps"][name]["status"] != "done"]
            if blockers:
                raise GateFailure("拒绝导出；卡在 " + ", ".join(blockers), "blocked")
            self.run_export()
        return False

    def run(self, until="export_gate", dry_run=False):
        self.check_stop()
        selected = STEPS[:STEPS.index(until) + 1]
        if dry_run:
            actions = {
                "candidates": "tools/candidates.py; skip only when search_status=complete",
                "screen": "screen_candidates.run_screen; skip when line count equals candidate count",
                "fill": "campaign.run_fill; reuse latest V6 scorecard; never retry failed fill automatically",
                "integrity": "read selected scorecard; reject errors with row numbers and kinds, or stale scoring",
                "second_read": f"independent {self.second_read_backend} model; at most 5 rows/batch; block above 5 wrong/100; report unverified without blocking; preserve rows",
                "judgment_check": "tools/check_judgment.py ENTRY --dry-run; block if judgment file absent",
                "review_gate": "require this protein in ledger/judgment_reviewed.json",
                "export_gate": "tools/build_gina_table.py only if all preceding seven steps are done",
            }
            for step in selected:
                inputs, outputs = self.files_for(step)
                print(f"{step}: backend={self.backend}; inputs={inputs}; outputs={outputs}; "
                      f"{actions[step]}; stop on failure")
            return 0
        if self.state_path.exists():
            existing = read_json(self.state_path)
            existing_steps = set(existing.get("steps", {}))
            if existing.get("entry") != self.entry or existing_steps not in (set(STEPS), set(STEPS) - {"second_read"}):
                raise GateFailure("invalid state file; refusing to overwrite")
            if "second_read" not in existing_steps:
                existing["steps"]["second_read"] = self.state["steps"]["second_read"]
                for later in STEPS[STEPS.index("second_read") + 1:]:
                    if existing["steps"][later]["status"] != "failed":
                        existing["steps"][later]["status"] = "pending"
            self.state = existing
            self.state["backend"] = self.backend
            self.state["second_read_backend"] = self.second_read_backend
        for step in selected:
            record = self.state["steps"][step]
            if record["status"] == "failed":
                print(f"{step}: failed; no automatic retry: {record['failure_reason']}")
                return 1
            for later in STEPS[STEPS.index(step) + 1:]:
                if self.state["steps"][later]["status"] != "failed":
                    self.state["steps"][later]["status"] = "pending"
            inputs, outputs = self.files_for(step)
            record.update(status="pending", input_files=inputs, output_files=outputs,
                          started_at=timestamp(), ended_at=None, failure_reason=None, errors=[], skipped=False)
            try:
                self.check_stop()
                self.save()
                record["skipped"] = self.perform(step)
                self.check_stop()
                record["status"] = "done"
            except (GateFailure, OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
                record.update(status=getattr(error, "status", "failed"), failure_reason=str(error),
                              errors=getattr(error, "errors", []))
                export = self.state["steps"]["export_gate"]
                if step != "export_gate":
                    export.update(status="blocked", failure_reason=f"拒绝导出；卡在 {step}: {error}")
            record["input_files"], record["output_files"] = self.files_for(step)
            record["ended_at"] = timestamp()
            self.save()
            print(f"{step}: {record['status']}" + (" (cached)" if record["skipped"] else "") +
                  (f" — {record['failure_reason']}" if record["failure_reason"] else ""))
            if record["status"] != "done":
                return 2 if record["status"] == "blocked" else 1
        return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entry")
    parser.add_argument("--until", choices=STEPS, default="export_gate")
    parser.add_argument("--backend", choices=("codex", "claude"), default="codex")
    parser.add_argument("--second-read-backend", choices=("codex", "claude"), help="defaults to --backend; Claude may second-read any entry")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    try:
        return ProteinDriver(args.entry, args.backend, second_read_backend=args.second_read_backend).run(args.until, args.dry_run)
    except (GateFailure, OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
