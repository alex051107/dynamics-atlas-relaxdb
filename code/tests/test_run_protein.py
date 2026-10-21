"""Offline driver and backend acceptance with synthetic files and model stubs."""

import contextlib
import io
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import campaign
import check_judgment as checker
import run_protein as driver
import screen_candidates as screen

FIXTURES = ROOT / "tests/fixtures_driver"
ENTRY = "KRAS_CPMG"


class DriverTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.case = self.root / "cases/V6_r6_KRAS_CPMG_20261013000000"
        self.case.mkdir(parents=True)
        for folder in ("outputs/candidates", "outputs/screen", "ledger"):
            (self.root / folder).mkdir(parents=True)
        shutil.copyfile(FIXTURES / "candidates.json", self.root / "outputs/candidates/KRAS_CPMG.json")
        shutil.copyfile(FIXTURES / "screen.jsonl", self.root / "outputs/screen/KRAS_CPMG.jsonl")
        (self.case / "rows.jsonl").write_text('{"synthetic":true}\n')
        shutil.copyfile(FIXTURES / "score_pass.json", self.case / "scorecard.json")
        shutil.copyfile(FIXTURES / "reviewed.json", self.root / "ledger/judgment_reviewed.json")
        self.protein = driver.ProteinDriver(ENTRY, root=self.root, stop=self.root / "STOP")
        self.stack = contextlib.ExitStack()
        self.addCleanup(self.stack.close)
        self.stack.enter_context(patch.object(screen.urllib.request, "urlopen", side_effect=AssertionError("network forbidden")))
        self.stack.enter_context(patch.object(screen.subprocess, "Popen", side_effect=AssertionError("process forbidden")))
        self.candidates = self.stack.enter_context(patch.object(self.protein, "run_candidates"))
        self.screen = self.stack.enter_context(patch.object(screen, "run_screen"))
        self.fill = self.stack.enter_context(patch.object(campaign, "run_fill"))
        self.second_read = self.stack.enter_context(patch.object(self.protein, "run_second_read", return_value={
            "status": "done", "total_rows": 1, "checked_rows": 1, "wrong_count": 0,
            "wrong_rows": [], "errors_per_100": 0, "errors": []}))
        self.judgment = self.stack.enter_context(patch.object(self.protein, "run_judgment"))
        self.export = self.stack.enter_context(patch.object(self.protein, "run_export"))

    def add_judgment(self):
        directory = self.root / "outputs/judgment_v0"
        directory.mkdir()
        (directory / f"{ENTRY}.json").write_text("Do not read this file; checker is stubbed.")

    def run_driver(self, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            status = self.protein.run(**kwargs)
        self.output = output.getvalue()
        return status

    def test_existing_steps_skip_workers_and_export_after_gates(self):
        self.add_judgment()
        self.assertEqual(self.run_driver(), 0)
        for worker in (self.candidates, self.screen, self.fill):
            worker.assert_not_called()
        self.judgment.assert_called_once()
        self.second_read.assert_called_once()
        self.export.assert_called_once()
        state = json.loads(self.protein.state_path.read_text())
        self.assertTrue(all(step["status"] == "done" for step in state["steps"].values()))
        for name in driver.STEPS:
            record = state["steps"][name]
            self.assertTrue(record["started_at"] and record["ended_at"])
            self.assertTrue(record["input_files"] and record["output_files"])
        self.assertTrue(all(state["steps"][step]["skipped"] for step in driver.STEPS[:3]))

    def test_integrity_failure_names_row_and_prevents_all_later_calls(self):
        shutil.copyfile(FIXTURES / "score_fail.json", self.case / "scorecard.json")
        self.assertEqual(self.run_driver(), 1)
        record = self.protein.state["steps"]["integrity"]
        self.assertEqual(record["status"], "failed")
        self.assertIn('"row": 7', self.output)
        self.assertIn("number_not_in_source", self.output)
        self.judgment.assert_not_called()
        self.second_read.assert_not_called()
        self.fill.assert_not_called()
        self.export.assert_not_called()
        self.assertIn("integrity", self.protein.state["steps"]["export_gate"]["failure_reason"])

    def test_new_fill_with_bad_integrity_stops_at_integrity(self):
        shutil.rmtree(self.case)

        def fill(entry, backend):
            self.case.mkdir()
            shutil.copyfile(FIXTURES / "score_fail.json", self.case / "scorecard.json")
            return {"case": self.case.name, "status": "failed", "returncode": 0,
                    "integrity": {"pass": False}, "fill_errors": [], "result": {"status": "done"}}

        self.fill.side_effect = fill
        self.assertEqual(self.run_driver(), 1)
        self.assertEqual(self.protein.state["steps"]["fill"]["status"], "done")
        self.assertEqual(self.protein.state["steps"]["integrity"]["status"], "failed")

    def test_missing_review_refuses_export(self):
        self.add_judgment()
        (self.root / "ledger/judgment_reviewed.json").write_text("{}")
        self.assertEqual(self.run_driver(), 2)
        self.assertEqual(self.protein.state["steps"]["review_gate"]["status"], "blocked")
        self.assertIn("review_gate", self.protein.state["steps"]["export_gate"]["failure_reason"])
        self.export.assert_not_called()

    def test_deleted_review_is_rechecked_on_rerun(self):
        self.add_judgment()
        self.assertEqual(self.run_driver(), 0)
        self.export.reset_mock()
        (self.root / "ledger/judgment_reviewed.json").write_text("{}")
        self.assertEqual(self.run_driver(), 2)
        self.export.assert_not_called()

    def test_absent_judgment_is_blocked_without_reading_it(self):
        self.assertEqual(self.run_driver(), 2)
        record = self.protein.state["steps"]["judgment_check"]
        self.assertEqual(record["failure_reason"], "判断层未起草")
        self.judgment.assert_not_called()

    def test_judgment_error_reports_identifier(self):
        self.add_judgment()
        self.judgment.side_effect = driver.GateFailure("判断编号 KRAS-J7: global_kex_assignment",
                                                     errors=[{"judgment_id": "KRAS-J7", "kind": "global_kex_assignment"}])
        self.assertEqual(self.run_driver(), 1)
        self.assertIn("KRAS-J7", self.output)
        self.export.assert_not_called()

    def test_dry_run_does_not_read_or_write_files_or_invoke_workers(self):
        with patch.object(Path, "read_text", side_effect=AssertionError("dry-run must not read content")), \
                patch.object(Path, "write_text", side_effect=AssertionError("dry-run must not write")):
            self.assertEqual(self.run_driver(dry_run=True), 0)
        self.assertEqual(len(self.output.splitlines()), 8)
        for worker in (self.candidates, self.screen, self.fill, self.second_read, self.judgment, self.export):
            worker.assert_not_called()
        self.assertFalse(self.protein.state_path.exists())

    def test_until_stops_before_judgment_or_export(self):
        self.assertEqual(self.run_driver(until="integrity"), 0)
        self.second_read.assert_not_called()
        self.assertEqual(self.protein.state["steps"]["judgment_check"]["status"], "pending")
        self.judgment.assert_not_called()
        self.export.assert_not_called()

    def test_second_read_wrong_rate_blocks_judgment_and_export(self):
        self.add_judgment()
        self.second_read.return_value = {"status": "blocked", "total_rows": 15, "checked_rows": 15,
                                         "wrong_count": 1, "wrong_rows": [7], "errors_per_100": 100 / 15,
                                         "errors": [{"row_number": 7, "reason": "Mg-free rate assigned to Mg sample"}]}
        self.assertEqual(self.run_driver(), 2)
        self.assertEqual(self.protein.state["steps"]["second_read"]["status"], "blocked")
        self.assertIn("行号：[7]", self.output)
        self.judgment.assert_not_called()
        self.export.assert_not_called()

    def test_second_read_at_threshold_is_marked_without_blocking(self):
        self.second_read.return_value = {"status": "done", "total_rows": 20, "checked_rows": 20,
                                         "wrong_count": 1, "wrong_rows": [7], "errors_per_100": 5,
                                         "errors": [{"row_number": 7, "reason": "sample mismatch"}]}
        self.assertEqual(self.run_driver(until="second_read"), 0)
        self.assertEqual(self.protein.state["steps"]["second_read"]["summary"]["wrong_rows"], [7])
        self.judgment.assert_not_called()

    def test_old_seven_step_state_gets_pending_second_read(self):
        self.add_judgment()
        existing = json.loads(json.dumps(self.protein.state))
        del existing["steps"]["second_read"]
        for record in existing["steps"].values():
            record["status"] = "done"
        self.protein.state_path.parent.mkdir(parents=True)
        self.protein.state_path.write_text(json.dumps(existing))
        self.assertEqual(self.run_driver(until="integrity"), 0)
        self.assertEqual(self.protein.state["steps"]["second_read"]["status"], "pending")
        self.assertEqual(self.protein.state["steps"]["export_gate"]["status"], "pending")
        self.second_read.assert_not_called()

    def test_claude_can_be_selected_for_second_read_only(self):
        protein = driver.ProteinDriver(ENTRY, root=self.root, stop=self.root / "STOP", second_read_backend="claude")
        self.assertEqual(protein.backend, "codex")
        self.assertEqual(protein.second_read_backend, "claude")

    def test_stop_prevents_even_cached_work(self):
        (self.root / "STOP").touch()
        with self.assertRaisesRegex(driver.GateFailure, "STOP exists"):
            self.run_driver()
        self.assertFalse(self.protein.state_path.exists())

    def test_stop_appearing_during_stage_blocks_next_stage(self):
        (self.root / "outputs/candidates/KRAS_CPMG.json").unlink()
        self.candidates.side_effect = lambda: (self.root / "STOP").touch()
        self.assertEqual(self.run_driver(), 2)
        self.screen.assert_not_called()
        self.export.assert_not_called()

    def test_failed_step_is_not_retried_on_restart(self):
        (self.root / "outputs/candidates/KRAS_CPMG.json").unlink()
        self.candidates.side_effect = RuntimeError("synthetic failure")
        self.assertEqual(self.run_driver(), 1)
        self.assertEqual(self.run_driver(), 1)
        self.candidates.assert_called_once()

    def test_downstream_failure_is_not_erased_by_cached_steps(self):
        self.add_judgment()
        self.judgment.side_effect = driver.GateFailure("synthetic judgment failure")
        self.assertEqual(self.run_driver(), 1)
        self.assertEqual(self.run_driver(), 1)
        self.judgment.assert_called_once()

    def test_changed_rows_require_fresh_scorecard(self):
        score_time = (self.case / "scorecard.json").stat().st_mtime_ns
        os.utime(self.case / "rows.jsonl", ns=(score_time + 1000000000, score_time + 1000000000))
        self.assertEqual(self.run_driver(), 1)
        self.assertEqual(self.protein.state["steps"]["integrity"]["errors"][0]["kind"], "stale_scorecard")

    def test_incomplete_search_must_not_be_cached(self):
        path = self.root / "outputs/candidates/KRAS_CPMG.json"
        data = json.loads(path.read_text())
        data["search_status"] = "incomplete"
        path.write_text(json.dumps(data))
        self.candidates.side_effect = lambda: shutil.copyfile(FIXTURES / "candidates.json", path)
        self.assertEqual(self.run_driver(until="candidates"), 0)
        self.candidates.assert_called_once()

    def test_export_gate_directly_refuses_pending_steps(self):
        with self.assertRaisesRegex(driver.GateFailure, "candidates"):
            self.protein.perform("export_gate")
        self.export.assert_not_called()


class BackendTest(unittest.TestCase):
    def test_legacy_model_entrypoints_also_reject_blac_and_cypa(self):
        with patch.object(campaign, "new_case") as create:
            for entry in ("BLAC_CPMG", "CYPA_CPMG"):
                for function in (campaign.run_layered, campaign.run_baseline, campaign.run_recall):
                    with self.subTest(entry=entry, function=function.__name__):
                        with self.assertRaisesRegex(ValueError, "prohibited"):
                            function(entry, 1)
            create.assert_not_called()

    def test_claude_screen_uses_same_batches_and_normalized_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "prompts").mkdir()
            (root / "prompts/worker_v6_screen.md").write_text("Synthetic screening prompt.")
            candidate = json.loads((FIXTURES / "candidates.json").read_text())["candidates"][0]
            row = json.loads((FIXTURES / "screen.jsonl").read_text())
            worker_row = {key: value for key, value in row.items() if key not in {"had_abstract", "doi"}}
            worker_row["candidate_index"] = 0
            worker_row["title_first_words"] = screen.title_first_words(candidate.get("title"))

            def spawn(command, cwd, prompt, events, timeout_s):
                self.assertIn("--json-schema", command)
                self.assertTrue(prompt.startswith("Synthetic screening prompt."))
                self.assertEqual(cwd, root / "outputs/screen/batches/CYPA_CPMG")
                Path(events).write_text(json.dumps({"structured_output": {"results": [worker_row]}, "total_cost_usd": 0.1}))
                return {"status": "exited", "returncode": 0, "wall_s": 0}

            with patch.object(screen, "WORK", root), patch.object(screen, "RUNS", root / "ledger/v6_runs.jsonl"), \
                    patch.object(screen, "check_stop"), patch.object(screen, "check_entry", return_value={"entry_id": "CYPA_CPMG"}), \
                    patch.object(screen, "candidates_for", return_value=[candidate]), \
                    patch.object(screen, "method_keys", return_value=["nmr_relaxation_dispersion"]), \
                    patch.object(screen, "spawn_worker", side_effect=spawn) as worker, \
                    patch.object(screen.urllib.request, "urlopen", side_effect=AssertionError("network forbidden")), \
                    contextlib.redirect_stdout(io.StringIO()):
                result = screen.run_screen("CYPA_CPMG", "claude")
                worker.assert_called_once()
                records = screen.run_records()
            self.assertEqual(result["backend"], "claude")
            self.assertEqual(json.loads((root / "outputs/screen/CYPA_CPMG.jsonl").read_text()), row)
            self.assertTrue(all(record["backend"] == "claude" for record in records))
            self.assertEqual(next(record["total_cost_usd"] for record in records if "total_cost_usd" in record), 0.1)

    def test_claude_fill_runs_in_case_and_normalizes_result(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            case = root / "cases/V6_r6_CYPA_CPMG_20261013000000"
            (root / "prompts").mkdir()
            (root / "prompts/worker_v6_fill.md").write_text("Synthetic fill prompt.")
            candidate = json.loads((FIXTURES / "candidates.json").read_text())["candidates"][0]
            (root / "outputs/screen").mkdir(parents=True)
            shutil.copyfile(FIXTURES / "screen.jsonl", root / "outputs/screen/CYPA_CPMG.jsonl")
            stages = []

            def spawn(command, cwd, prompt, events, timeout_s):
                self.assertEqual(cwd, case)
                if "--max-budget-usd" in command:
                    stages.append("model")
                    self.assertTrue(prompt.startswith("Synthetic fill prompt."))
                    (case / "rows.jsonl").write_text(json.dumps({"doi": candidate["doi"]}) + "\n")
                    (case / "screen_log.jsonl").write_text(json.dumps({"doi": candidate["doi"]}) + "\n")
                    (case / "coverage.json").write_text("{}")
                    Path(events).write_text(json.dumps({"result": json.dumps({"entry_id": "CYPA_CPMG", "status": "done"}),
                                                       "total_cost_usd": 0.2}))
                elif command[-2].endswith("score.py"):
                    stages.append("score")
                    shutil.copyfile(FIXTURES / "score_pass.json", case / "scorecard.json")
                else:
                    stages.append("prefetch")
                return {"status": "exited", "returncode": 0, "wall_s": 0}

            def new_case(prefix, entry, round_id, arm):
                case.mkdir(parents=True)
                return case, {"entry_id": entry, "name": "Synthetic CypA"}

            with patch.object(campaign, "WORK", root), patch.object(campaign, "CACHE", root / "sources_cache"), \
                    patch.object(campaign, "new_case", side_effect=new_case), patch.object(campaign, "record"), \
                    patch.object(screen, "RUNS", root / "ledger/v6_runs.jsonl"), patch.object(screen, "check_stop"), \
                    patch.object(screen, "check_entry", return_value={}), patch.object(screen, "candidates_for", return_value=[candidate]), \
                    patch.object(screen, "method_keys", return_value=["nmr_relaxation_dispersion"]), \
                    patch.object(screen, "spawn_worker", side_effect=spawn):
                result = campaign.run_fill("CYPA_CPMG", "claude")
                records = screen.run_records()
            self.assertEqual(stages, ["prefetch", "model", "score"])
            self.assertEqual(result["status"], "exited")
            self.assertEqual(result["backend"], "claude")
            self.assertEqual(result["result"]["status"], "done")
            self.assertEqual(result["total_cost_usd"], 0.2)
            self.assertTrue(all(record["backend"] == "claude" for record in records))

    def test_claude_commands_have_schema_budgets_models_and_tools(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            schema = root / "schema.json"
            content = screen.output_schema(["nmr_relaxation_dispersion"])
            schema.write_text(json.dumps(content))
            command = screen.screen_command(schema, root, root / "result.json", "claude")
            self.assertIn("--json-schema", command)
            self.assertEqual(json.loads(command[command.index("--json-schema") + 1]), content)
            self.assertEqual(command[command.index("--max-budget-usd") + 1], "2")
            self.assertIn("claude-sonnet-5-5", command)
            command = campaign.fill_command(root, "claude")
            self.assertEqual(command[command.index("--max-budget-usd") + 1], "15")
            self.assertIn("claude-opus-5-5", command)
            self.assertIn("acceptEdits", command)
            self.assertEqual(command.count("--add-dir"), 2)
            self.assertIn("Read,Write,Edit,Bash,WebFetch", command)

    def test_blac_cypa_reject_codex_before_models(self):
        with patch.object(screen, "spawn_worker") as spawn:
            for entry in ("BLAC_CPMG", "CYPA_CPMG"):
                with self.subTest(entry=entry):
                    with self.assertRaisesRegex(ValueError, "prohibited"):
                        driver.ProteinDriver(entry, "codex")
                    with patch.object(screen, "check_stop"):
                        with self.assertRaisesRegex(ValueError, "prohibited"):
                            screen.run_screen(entry, "codex")
                        with self.assertRaisesRegex(ValueError, "prohibited"):
                            campaign.run_fill(entry, "codex")
                    screen.validate_backend(entry, "claude")
            spawn.assert_not_called()
        with self.assertRaisesRegex(ValueError, "only authorized"):
            screen.validate_backend("KRAS_CPMG", "claude")

    def test_claude_envelopes_preserve_model_output_and_cost(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for envelope in ({"structured_output": {"results": []}, "total_cost_usd": 0.1},
                             {"result": json.dumps({"status": "done"}), "usage": {"output_tokens": 20}}):
                events = root / "events.json"
                events.write_text(json.dumps(envelope))
                metadata = screen.save_claude_result(events, root / "result.json")
                self.assertTrue(metadata)
                self.assertIsInstance(json.loads((root / "result.json").read_text()), dict)
            events.write_text(json.dumps({"subtype": "error_max_budget_usd", "is_error": True}))
            with self.assertRaisesRegex(ValueError, "budget"):
                screen.save_claude_result(events, root / "result.json")

    def test_shared_budget_ledger_labels_backend(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(screen, "RUNS", Path(directory) / "runs.jsonl"):
            screen.append_run({"entry": "CYPA_CPMG", "stage": "screen_started"}, "claude")
            screen.append_run({"entry": "KRAS_CPMG", "stage": "screen_started"})
            self.assertEqual([record["backend"] for record in screen.run_records()], ["claude", "codex"])


class ResidueRuleTest(unittest.TestCase):
    def test_residue_basis_acceptance_and_dry_checker_writes_nothing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "schema").mkdir()
            (root / "inputs").mkdir()
            (root / "outputs/judgment_v0").mkdir(parents=True)
            shutil.copyfile(ROOT / "schema/judgment_contract.json", root / "schema/judgment_contract.json")
            (root / "inputs/TOY_CPMG.json").write_text(json.dumps({"sequence": "ACDE"}))
            template = json.loads((ROOT / "tests/fixtures_judgment/passing.json").read_text())
            evidence = {"TOY-r1": ["TOY_CPMG"], "TOY-a1": ["TOY_CPMG"]}
            for scenario in json.loads((FIXTURES / "residue_rules.json").read_text()):
                with self.subTest(scenario=scenario):
                    data = json.loads(json.dumps(template))
                    region = data["judgments"][0]["region"]
                    region.pop("residue_basis", None)
                    region["residues_entry"] = scenario["residues"]
                    if "basis" in scenario:
                        region["residue_basis"] = scenario["basis"]
                    (root / "outputs/judgment_v0/TOY_CPMG.json").write_text(json.dumps(data))
                    with patch.object(checker, "load_evidence", return_value=evidence), \
                            patch.object(Path, "write_text", side_effect=AssertionError("checker must not write")), \
                            contextlib.redirect_stdout(io.StringIO()) as output, contextlib.redirect_stderr(io.StringIO()):
                        status = checker.main(["TOY_CPMG", "--dry-run"], root=root)
                    report = json.loads(output.getvalue())
                    self.assertEqual(status != 0, scenario["error"])
                    self.assertEqual(not report["pass"], scenario["error"])
                    if scenario["error"]:
                        self.assertIn("global_kex_assignment", {error["kind"] for error in report["errors"]})
                    self.assertFalse((root / "outputs/judgment_v0/TOY_CPMG.check.json").exists())


if __name__ == "__main__":
    unittest.main()
