"""Second-read acceptance uses synthetic KRAS text and model stubs, never model CLIs."""

import contextlib
import copy
import io
from itertools import product
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import second_read as reader


ANCHOR = "The Mg-free PBS/EDTA sample had kex = 120 s-1."
BUFFER = "PBS; 10 mM EDTA; no MgCl2"
SOURCE = ("KRAS WT residues 1-169 bound to GDP was measured at 298 K in PBS; 10 mM EDTA; no MgCl2.\n"
          + ANCHOR + " The 15N CPMG experiment reported G13 and T35, with an excited-state population of 4%.\n\n"
          "The separate GDP-bound WT HEPES; 5 mM MgCl2 sample had kex = 25 s-1 and population 1%.\n"
          "R1, heteronuclear NOE and model-free S2 were spin-relaxation measurements of ps-ns flexibility.\n")


def evidence(row_number=1):
    return {"row_id": f"r{row_number}", "entry_id": "KRAS_CPMG", "source_file": "KRAS_synthetic.txt",
            "anchor": ANCHOR, "buffer": BUFFER, "ligand_or_partner": "GDP; Mg-free",
            "construct_or_mutation": "KRAS WT residues 1-169", "temperature": "298 K",
            "timescale": "kex = 120 s-1", "population": "excited state 4%",
            "method_class": "nmr_relaxation_dispersion", "experiment": "15N CPMG",
            "residues_author": "G13, T35"}


def stub_model(requests, backend, batch_dir, timeout_s, check_stop):
    results = []
    for request in requests:
        row = request["evidence"]
        sample_match = (row["buffer"] == BUFFER and row["ligand_or_partner"] == "GDP; Mg-free"
                        and row["temperature"] == "298 K" and row["construct_or_mutation"] == "KRAS WT residues 1-169")
        value_match = sample_match and row["timescale"] == "kex = 120 s-1" and row["population"] == "excited state 4%"
        spin_only = row["experiment"] in {"R1", "NOE", "S2"}
        method_match = row["method_class"] == ("nmr_spin_relaxation" if spin_only else "nmr_relaxation_dispersion")
        residue_match = row["residues_author"] == "G13, T35"
        verdict = "ok" if all((sample_match, value_match, method_match, residue_match)) else "wrong"
        results.append({"row_number": request["row_number"], "sample_match": "match" if sample_match else "mismatch",
                        "value_match": "match" if value_match else "mismatch",
                        "method_match": "match" if method_match else "mismatch",
                        "residue_match": "match" if residue_match else "mismatch",
                        "verdict": verdict, "reason": "Bindings match." if verdict == "ok" else "Sample or experiment binding differs.",
                        "source_quote": ANCHOR})
    return {"results": results}


class SecondReadTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.case = self.root / "cases/V6_r6_KRAS_CPMG_synthetic"
        self.case.mkdir(parents=True)
        (self.root / "sources_cache").mkdir()
        self.source = self.root / "sources_cache/KRAS_synthetic.txt"
        self.source.write_text(SOURCE, encoding="utf-8")
        self.write_rows([evidence()])
        stack = contextlib.ExitStack()
        self.addCleanup(stack.close)
        stack.enter_context(patch.object(reader.screen.subprocess, "Popen", side_effect=AssertionError("model process forbidden")))
        stack.enter_context(patch.object(reader.screen.urllib.request, "urlopen", side_effect=AssertionError("network forbidden")))
        stack.enter_context(patch.object(reader.screen, "STOP", self.root / "STOP"))

    def write_rows(self, rows):
        (self.case / "rows.jsonl").write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")

    def run_case(self, **kwargs):
        return reader.run_case(self.case, root=self.root, model=kwargs.pop("model", stub_model), **kwargs)

    def results(self):
        return [json.loads(line) for line in (self.case / "second_read.jsonl").read_text().splitlines()]

    def ledger(self):
        return [json.loads(line) for line in (self.root / "ledger/v6_runs.jsonl").read_text().splitlines()]

    def test_mg_free_rate_attached_to_mg_sample_is_wrong_and_rows_are_preserved(self):
        row = evidence()
        row.update(buffer="HEPES; 5 mM MgCl2", ligand_or_partner="GDP; Mg2+")
        self.write_rows([row])
        original = (self.case / "rows.jsonl").read_bytes()
        summary = self.run_case()
        result = self.results()[0]
        self.assertEqual(result["verdict"], "wrong")
        self.assertEqual(result["sample_match"], "mismatch")
        self.assertEqual(result["value_match"], "mismatch")
        self.assertTrue(result["needs_adjudication"])
        self.assertEqual(summary["status"], "blocked")
        self.assertEqual(summary["wrong_rows"], [1])
        self.assertEqual(summary["wrong_per_100"], 100)
        self.assertEqual(summary["unverified_per_100"], 0)
        self.assertEqual((self.case / "rows.jsonl").read_bytes(), original)

    def test_correct_row_is_ok(self):
        summary = self.run_case()
        result = self.results()[0]
        self.assertEqual(result["verdict"], "ok")
        self.assertTrue(all(result[field] == "match" for field in reader.MATCH_FIELDS))
        self.assertFalse(result["needs_adjudication"])
        self.assertEqual(summary["status"], "done")
        self.assertEqual(summary["wrong_per_100"], 0)
        self.assertEqual(summary["unverified_per_100"], 0)
        self.assertEqual(self.ledger()[0]["stage"], "second_read")

    def test_spin_only_methods_cannot_be_relaxation_dispersion(self):
        for experiment in ("R1", "NOE", "S2"):
            with self.subTest(experiment=experiment):
                row = evidence()
                row["experiment"] = experiment
                self.write_rows([row])
                self.run_case()
                self.assertEqual(self.results()[0]["method_match"], "mismatch")
                self.assertEqual(self.results()[0]["verdict"], "wrong")
        self.assertIn("nmr_spin_relaxation", reader.PROMPT)
        self.assertIn("never evidence of us-ms", reader.PROMPT)

    def test_other_experiments_residues_are_wrong(self):
        row = evidence()
        row["residues_author"] = "A59"
        self.write_rows([row])
        self.run_case()
        self.assertEqual(self.results()[0]["residue_match"], "mismatch")

    def test_five_row_batches_preserve_order_and_compute_per_hundred_rates(self):
        rows = [evidence(index) for index in range(1, 32)]
        rows[16].update(buffer="HEPES; 5 mM MgCl2")
        self.write_rows(rows)
        batches = []

        def model(requests, *args):
            batches.append([request["row_number"] for request in requests])
            payload = stub_model(requests, *args)
            payload["results"].reverse()
            return payload

        summary = self.run_case(model=model)
        self.assertEqual([len(batch) for batch in batches], [5, 5, 5, 5, 5, 5, 1])
        self.assertEqual([result["row_number"] for result in self.results()], list(range(1, 32)))
        self.assertEqual(summary["wrong_rows"], [17])
        self.assertAlmostEqual(summary["wrong_per_100"], 100 / 31, places=6)
        self.assertEqual(summary["unverified_per_100"], 0)
        self.assertEqual(summary["batches_completed"], 7)
        self.assertEqual(summary["status"], "done")
        self.assertEqual(self.ledger()[-1], summary)

    def test_rate_threshold_is_strictly_greater_than_five(self):
        for count, expected in ((20, "done"), (19, "blocked")):
            with self.subTest(count=count):
                rows = [evidence(index) for index in range(1, count + 1)]
                rows[-1]["buffer"] = "HEPES; 5 mM MgCl2"
                self.write_rows(rows)
                self.assertEqual(self.run_case()["status"], expected)

    def test_all_three_state_combinations_map_to_the_expected_verdict(self):
        requests = [{"row_number": 1, "evidence": evidence(),
                     "source_windows": reader.source_windows(evidence(), self.root, {})}]
        for states in product(reader.MATCH_STATES, repeat=4):
            with self.subTest(states=states):
                expected = "wrong" if "mismatch" in states else "unverified" if "not_in_context" in states else "ok"
                payload = stub_model(requests, None, None, None, None)
                payload["results"][0].update(dict(zip(reader.MATCH_FIELDS, states)), verdict=expected)
                self.assertEqual(reader.validate_results(payload, requests)[0]["verdict"], expected)
                payload["results"][0]["verdict"] = "wrong" if expected != "wrong" else "ok"
                with self.assertRaisesRegex(ValueError, "verdict contradicts"):
                    reader.validate_results(payload, requests)
        schema = reader.output_schema()["properties"]["results"]
        self.assertEqual(schema["maxItems"], 5)
        for field in reader.MATCH_FIELDS:
            self.assertEqual(schema["items"]["properties"][field]["enum"], list(reader.MATCH_STATES))
        self.assertIn("not_in_context", reader.PROMPT)

    def test_wrong_and_unverified_rates_are_separate(self):
        self.write_rows([evidence(index) for index in range(1, 21)])

        def model(requests, *args):
            payload = stub_model(requests, *args)
            for result in payload["results"]:
                if result["row_number"] == 1:
                    result.update(sample_match="mismatch", value_match="not_in_context", verdict="wrong")
                else:
                    result.update(sample_match="not_in_context", verdict="unverified")
            return payload

        summary = self.run_case(model=model)
        self.assertEqual(summary["wrong_rows"], [1])
        self.assertEqual(summary["wrong_count"], 1)
        self.assertEqual(summary["wrong_per_100"], 5)
        self.assertEqual(summary["unverified_rows"], list(range(2, 21)))
        self.assertEqual(summary["unverified_count"], 19)
        self.assertEqual(summary["unverified_per_100"], 95)
        self.assertEqual(summary["status"], "done")

    def test_missing_quote_marks_row_unverified_without_aborting_or_blocking(self):
        self.write_rows([evidence(index) for index in range(1, 7)])

        def model(requests, *args):
            payload = stub_model(requests, *args)
            for result in payload["results"]:
                result.update(sample_match="mismatch", verdict="wrong", source_quote="fabricated quotation")
            return payload

        summary = self.run_case(model=model)
        self.assertEqual(summary["batches_completed"], 2)
        self.assertEqual(summary["status"], "done")
        self.assertEqual(summary["wrong_per_100"], 0)
        self.assertEqual(summary["unverified_per_100"], 100)
        self.assertTrue(all(result["quote_unverified"] and result["needs_adjudication"]
                            and result["verdict"] == "unverified" for result in self.results()))

    def test_batches_larger_than_five_are_refused_without_model(self):
        with patch.object(reader, "review_batch") as model:
            with self.assertRaisesRegex(ValueError, "1..5"):
                reader.run_case(self.case, root=self.root, batch_size=6)
            model.assert_not_called()

    def test_blank_lines_keep_physical_line_numbers(self):
        self.write_rows([evidence(1), evidence(2)])
        path = self.case / "rows.jsonl"
        path.write_text(path.read_text().replace("\n", "\n\n", 1))
        self.run_case()
        self.assertEqual([result["row_number"] for result in self.results()], [1, 3])

    def test_long_source_window_contains_anchor_and_1500_characters_on_each_side(self):
        text = "a" * 62000 + ANCHOR + "b" * 62000
        self.source.write_text(text)
        windows = reader.source_windows(evidence(), self.root, {})
        self.assertEqual(len(windows), 1)
        self.assertEqual(windows[0]["text"], "a" * 1500 + ANCHOR + "b" * 1500)
        self.assertEqual(windows[0]["start_char"], 60500)
        self.assertEqual(windows[0]["end_char"], 63500 + len(ANCHOR))

    def test_full_source_is_supplied_through_120000_characters(self):
        for length in (len(SOURCE), reader.MAX_CONTEXT_CHARS):
            with self.subTest(length=length):
                text = SOURCE + "z" * (length - len(SOURCE))
                self.source.write_text(text)
                windows = reader.source_windows(evidence(), self.root, {})
                self.assertEqual(windows, [{"start_char": 0, "end_char": length, "text": text}])

    def test_long_source_includes_method_sections_and_locator_paragraphs(self):
        row = evidence()
        row["locator"] = "Table 2; Fig. 3; Table S1; Figure 4"
        sections = "\n\n".join(f"## {title}\n{title.lower()} sample conditions."
                                  for title in ("Methods", "Materials and Methods", "Experimental procedures",
                                                "Sample preparation", "NMR spectroscopy"))
        captions = ("\n\n## Results\nOther experiment.\n\nTable 2: measured rate.\nMore table content."
                    "\n\nFig. 3: residue assignments.\nMore caption content."
                    "\n\nTable S1: sample composition.\n\nFigure 4: fitted states."
                    "\n\nTable 20: unrelated table.\n\nFig. 30: unrelated figure.")
        self.source.write_text(SOURCE + "z" * 125000 + "\n\n" + sections + captions)
        windows = reader.source_windows(row, self.root, {})
        context = "\n".join(window["text"] for window in windows)
        self.assertIn(ANCHOR, context)
        for title in ("Methods", "Materials and Methods", "Experimental procedures", "Sample preparation", "NMR spectroscopy"):
            self.assertIn(f"{title.lower()} sample conditions.", context)
        for caption in ("Table 2: measured rate.", "More table content.", "Fig. 3: residue assignments.",
                        "More caption content.", "Table S1: sample composition.", "Figure 4: fitted states."):
            self.assertIn(caption, context)
        self.assertNotIn("Other experiment.", context)
        self.assertNotIn("unrelated", context)

    def test_context_is_deduplicated_and_capped_at_120000_characters(self):
        self.source.write_text("## Methods\n" + SOURCE + "z" * 125000)
        windows = reader.source_windows(evidence(), self.root, {})
        self.assertEqual(sum(len(window["text"]) for window in windows), reader.MAX_CONTEXT_CHARS)
        ranges = sorted((window["start_char"], window["end_char"]) for window in windows)
        self.assertTrue(all(left[1] <= right[0] for left, right in zip(ranges, ranges[1:])))
        for window in windows:
            self.assertEqual(len(window["text"]), window["end_char"] - window["start_char"])

    def test_plain_and_tagged_methods_headings_select_their_sections(self):
        for heading, next_heading in (("2. Materials and Methods", "3. Results"),
                                      ("<h2>Experimental procedures</h2>", "<h2>Results</h2>"),
                                      ("<title>NMR spectroscopy</title>", "<title>Results</title>")):
            with self.subTest(heading=heading):
                self.source.write_text(SOURCE + "z" * 125000 + f"\n\n{heading}\nSample buffer details.\n\n{next_heading}\nExcluded details.")
                context = "\n".join(window["text"] for window in reader.source_windows(evidence(), self.root, {}))
                self.assertIn("Sample buffer details.", context)
                self.assertNotIn("Excluded details.", context)

    def test_inline_xml_titles_select_distant_methods(self):
        self.source.write_text(SOURCE + "z" * 125000 +
                               "<sec><title>Materials and Methods</title><p>Sample buffer details.</p></sec>"
                               "<sec><title>Results</title><p>Excluded details.</p></sec>")
        context = "\n".join(window["text"] for window in reader.source_windows(evidence(), self.root, {}))
        self.assertIn("Sample buffer details.", context)
        self.assertNotIn("Excluded details.", context)

    def test_methods_include_nested_subsections_but_not_the_next_peer_section(self):
        for headings in (("## Methods", "### Protein expression", "## Results"),
                         ("2. Methods", "2.1 Protein expression", "3. Results"),
                         ("<h2>Methods</h2>", "<h3>Protein expression</h3>", "<h2>Results</h2>")):
            with self.subTest(headings=headings):
                self.source.write_text(SOURCE + "z" * 125000 +
                                       f"\n\n{headings[0]}\nMethod details.\n\n{headings[1]}\nSample buffer details."
                                       f"\n\n{headings[2]}\nExcluded details.")
                context = "\n".join(window["text"] for window in reader.source_windows(evidence(), self.root, {}))
                self.assertIn("Sample buffer details.", context)
                self.assertNotIn("Excluded details.", context)

    def test_whitespace_wrapped_anchor_is_located(self):
        self.source.write_text(SOURCE.replace(ANCHOR, ANCHOR.replace("sample had", "sample\n  had")))
        self.assertEqual(self.run_case()["status"], "done")

    def test_all_repeated_anchor_windows_are_supplied(self):
        self.source.write_text(SOURCE + "z" * 125000 + SOURCE)
        requests = []

        def model(batch, *args):
            requests.extend(batch)
            return stub_model(batch, *args)

        self.run_case(model=model)
        self.assertEqual(len(requests[0]["source_windows"]), 2)
        self.assertEqual(len(self.results()[0]["source_windows"]), 2)

    def test_missing_anchor_becomes_unverified_without_a_model_call(self):
        self.source.write_text("No anchor in this synthetic file.")
        with patch.object(reader, "review_batch") as model:
            reader.run_case(self.case, root=self.root)
            model.assert_not_called()
        results = [json.loads(line) for line in (self.case / "second_read.jsonl").read_text().splitlines()]
        self.assertTrue(results and all(r["verdict"] == "unverified" for r in results))
        self.assertTrue(all("anchor not found" in r["reason"] for r in results))
        self.assertEqual(self.ledger()[-1]["wrong_count"], 0)

    def test_source_path_escape_and_symlink_escape_are_refused(self):
        outside = self.root / "outside.txt"
        outside.write_text(SOURCE)
        (self.root / "sources_cache/link.txt").symlink_to(outside)
        for source in (str(outside), "../outside.txt", "link.txt"):
            with self.subTest(source=source):
                row = evidence()
                row["source_file"] = source
                self.write_rows([row])
                with self.assertRaisesRegex(reader.SecondReadFailure, "inside sources_cache"):
                    self.run_case()

    def test_restricted_case_paths_are_refused_before_reading(self):
        for name in ("S_synthetic", "C_synthetic"):
            with patch.object(Path, "read_text", side_effect=AssertionError("restricted content forbidden")):
                with self.assertRaisesRegex(ValueError, "restricted cases"):
                    reader.run_case(self.root / "cases" / name, root=self.root)

    def test_empty_rows_cannot_pass(self):
        self.write_rows([])
        with self.assertRaisesRegex(reader.SecondReadFailure, "no evidence"):
            self.run_case()
        self.assertIsNone(self.ledger()[-1]["errors_per_100"])

    def test_partial_failure_does_not_publish_a_full_rate_or_overwrite_old_output(self):
        self.write_rows([evidence(index) for index in range(1, 17)])
        output = self.case / "second_read.jsonl"
        output.write_text("previous completed run\n")
        batches = []

        def model(requests, *args):
            batches.append(requests)
            if len(batches) == 2:
                raise RuntimeError("synthetic second batch failed")
            return stub_model(requests, *args)

        with self.assertRaises(reader.SecondReadFailure):
            self.run_case(model=model)
        summary = self.ledger()[-1]
        self.assertEqual(summary["status"], "failed")
        self.assertEqual(summary["checked_rows"], 5)
        self.assertEqual(summary["batches_completed"], 1)
        self.assertIsNone(summary["errors_per_100"])
        self.assertIsNone(summary["wrong_per_100"])
        self.assertIsNone(summary["unverified_per_100"])
        self.assertIsNone(summary["output"])
        self.assertEqual(output.read_text(), "previous completed run\n")
        self.assertEqual(len(batches), 2)

    def test_invalid_model_results_fail_closed(self):
        requests = [{"row_number": 1, "evidence": evidence(),
                     "source_windows": reader.source_windows(evidence(), self.root, {})}]
        valid = stub_model(requests, None, None, None, None)
        cases = []
        fabricated = copy.deepcopy(valid)
        fabricated["results"][0]["source_quote"] = "fabricated quotation"
        flagged = reader.validate_results(fabricated, requests)[0]
        self.assertEqual(flagged["verdict"], "unverified")
        self.assertTrue(flagged["quote_unverified"])
        for field, value in (("sample_match", "true"), ("sample_match", True), ("sample_match", []),
                             ("verdict", "wrong"), ("row_number", True), ("row_number", 2)):
            payload = copy.deepcopy(valid)
            payload["results"][0][field] = value
            cases.append(payload)
        cases.extend([{"results": []}, {"results": valid["results"] * 2}, {"results": valid["results"], "extra": True}])
        for payload in cases:
            with self.subTest(payload=payload):
                with self.assertRaises(ValueError):
                    reader.validate_results(payload, requests)

    def test_changed_evidence_or_source_during_review_is_not_published(self):
        for target in (self.case / "rows.jsonl", self.source):
            with self.subTest(target=target.name):
                self.write_rows([evidence()])
                self.source.write_text(SOURCE)

                def model(requests, *args):
                    target.write_text(target.read_text() + "\n")
                    return stub_model(requests, *args)

                with self.assertRaisesRegex(reader.SecondReadFailure, "changed during second read"):
                    self.run_case(model=model)
                self.assertFalse((self.case / "second_read.jsonl").exists())

    def test_stop_blocks_work_without_model(self):
        (self.root / "STOP").touch()
        with self.assertRaisesRegex(RuntimeError, "STOP exists"):
            self.run_case()
        self.assertFalse((self.root / "ledger/v6_runs.jsonl").exists())

    def test_blac_and_cypa_require_claude_before_model_invocation(self):
        for entry in ("BLAC_CPMG", "CYPA_CPMG"):
            with self.subTest(entry=entry):
                row = evidence()
                row["entry_id"] = entry
                self.write_rows([row])
                with patch.object(reader, "review_batch") as model:
                    with self.assertRaisesRegex(reader.SecondReadFailure, "prohibited"):
                        reader.run_case(self.case, root=self.root)
                    model.assert_not_called()
                self.assertEqual(self.run_case(backend="claude")["backend"], "claude")

    def test_real_backend_command_and_envelope_are_checked_with_spawn_stub(self):
        requests = [{"row_number": 1, "evidence": evidence(),
                     "source_windows": reader.source_windows(evidence(), self.root, {})}]
        payload = stub_model(requests, None, None, None, None)
        for backend in ("codex", "claude"):
            with self.subTest(backend=backend):
                batch_dir = self.root / backend
                batch_dir.mkdir()
                working_directories = []

                def spawn(command, cwd, prompt, events, timeout_s):
                    self.assertIn(reader.PROMPT, prompt)
                    self.assertIn(ANCHOR, prompt)
                    self.assertNotEqual(cwd, self.root)
                    self.assertTrue(Path(cwd).is_dir())
                    self.assertEqual(timeout_s, 600)
                    working_directories.append(cwd)
                    if backend == "codex":
                        self.assertIn("--output-schema", command)
                        self.assertIn('model_reasoning_effort="medium"', command)
                        Path(command[command.index("-o") + 1]).write_text(json.dumps(payload))
                        Path(events).write_text('{"type":"completed"}\n')
                    else:
                        self.assertIn("-p", command)
                        self.assertIn("--json-schema", command)
                        self.assertEqual(command[command.index("--model") + 1], "claude-sonnet-5-5")
                        self.assertEqual(command[command.index("--tools") + 1], "")
                        Path(events).write_text(json.dumps({"structured_output": payload, "total_cost_usd": 0.1}))
                    return {"status": "exited", "returncode": 0, "wall_s": 0}

                with patch.object(reader.screen, "spawn_worker", side_effect=spawn) as worker:
                    result = reader.review_batch(requests, backend, batch_dir, 600, lambda: None)
                    worker.assert_called_once()
                self.assertEqual(result, payload)
                self.assertTrue((batch_dir / "receipt.json").exists())
                self.assertFalse(Path(working_directories[0]).exists())

    def test_cli_reports_blocked_exit_code_without_a_worker(self):
        summary = {"status": "blocked", "wrong_rows": [7], "wrong_per_100": 10, "unverified_per_100": 0}
        with patch.object(reader, "run_case", return_value=summary) as run, contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(reader.main([self.case.name, "--backend", "claude"]), 2)
        run.assert_called_once_with(self.case.name, "claude", batch_size=5, timeout_s=600)
        self.assertEqual(json.loads(output.getvalue()), summary)

    def test_driver_uses_real_second_read_stage_with_stub_model_and_blocks(self):
        import run_protein as driver

        row = evidence()
        row.update(buffer="HEPES; 5 mM MgCl2", ligand_or_partner="GDP; Mg2+")
        self.write_rows([row])
        for folder in ("outputs/candidates", "outputs/screen"):
            (self.root / folder).mkdir(parents=True)
        (self.root / "outputs/candidates/KRAS_CPMG.json").write_text(json.dumps({"search_status": "complete", "candidates": []}))
        (self.root / "outputs/screen/KRAS_CPMG.jsonl").write_text("")
        (self.case / "scorecard.json").write_text(json.dumps({"integrity": {"pass": True, "n_errors": 0, "errors": []}}))
        protein = driver.ProteinDriver("KRAS_CPMG", root=self.root, stop=self.root / "STOP")
        with patch.object(reader, "review_batch", side_effect=stub_model) as model, \
                patch.object(protein, "run_judgment") as judgment, patch.object(protein, "run_export") as export, \
                contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(protein.run(), 2)
        model.assert_called_once()
        judgment.assert_not_called()
        export.assert_not_called()
        self.assertEqual(protein.state["steps"]["integrity"]["status"], "done")
        self.assertEqual(protein.state["steps"]["second_read"]["status"], "blocked")
        self.assertEqual(protein.state["steps"]["second_read"]["summary"]["wrong_rows"], [1])
        self.assertEqual(protein.state["steps"]["export_gate"]["status"], "blocked")
        self.assertEqual(self.results()[0]["verdict"], "wrong")
        self.assertEqual(self.ledger()[-1]["stage"], "second_read")

    def test_driver_reports_unverified_without_blocking(self):
        import run_protein as driver

        protein = driver.ProteinDriver("KRAS_CPMG", root=self.root, stop=self.root / "STOP")
        protein.case = self.case

        def model(requests, *args):
            payload = stub_model(requests, *args)
            payload["results"][0].update(sample_match="not_in_context", verdict="unverified")
            return payload

        with patch.object(reader, "review_batch", side_effect=model):
            self.assertFalse(protein.perform("second_read"))
        summary = protein.state["steps"]["second_read"]["summary"]
        self.assertEqual(summary["status"], "done")
        self.assertEqual(summary["wrong_per_100"], 0)
        self.assertEqual(summary["unverified_per_100"], 100)
        self.assertEqual(summary["unverified_rows"], [1])
        self.assertEqual(self.results()[0]["sample_match"], "not_in_context")
        self.assertTrue(self.results()[0]["needs_adjudication"])

    def test_driver_uses_wrong_rate_not_unverified_or_legacy_rate(self):
        import run_protein as driver

        protein = driver.ProteinDriver("KRAS_CPMG", root=self.root, stop=self.root / "STOP")
        summary = {"status": "done", "total_rows": 1, "checked_rows": 1, "wrong_count": 0,
                   "wrong_rows": [], "wrong_per_100": 0, "unverified_per_100": 100,
                   "errors_per_100": 100, "errors": []}
        with patch.object(protein, "run_second_read", return_value=summary):
            self.assertFalse(protein.perform("second_read"))


if __name__ == "__main__":
    unittest.main()
