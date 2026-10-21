"""Offline Edison integration tests: all submissions and HTTP requests are replaced."""
import contextlib
import copy
import io
import json
import os
from pathlib import Path
import socket
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import edison_candidates as edison
import merge_candidates as merge

ANSWER = {"status": "success", "answer": "Original studies: **10.5555/ALPHA**; "
          "[paper](https://doi.org/10.5555/beta(2026)). Duplicate doi:10.5555/alpha.",
          "references": [{"doi": "10.5555/gamma", "title": "Fake study"}],
          "query": "Not evidence: 10.5555/query-only", "answer_reasoning": "10.5555/reasoning-only"}


class FakeClient:
    def __init__(self, response=None):
        self.response = copy.deepcopy(ANSWER if response is None else response)
        self.submissions = []
        self.fetches = []

    def create_task(self, query):
        self.submissions.append(query)
        return "synthetic-task-id"

    def get_task(self, task_id):
        self.fetches.append(task_id)
        return self.response

    def close(self):
        pass


def metadata(doi):
    return {"DOI": doi.upper(), "title": ["Synthetic <i>experimental</i> study"],
            "published": {"date-parts": [[2026, 1]]}}


class EdisonTest(unittest.TestCase):
    def setUp(self):
        self.network_guard = patch.object(socket.socket, "connect", side_effect=AssertionError("offline test"))
        self.network_guard.start()
        self.addCleanup(self.network_guard.stop)
        self.dns_guard = patch.object(socket, "getaddrinfo", side_effect=AssertionError("offline DNS"))
        self.dns_guard.start()
        self.addCleanup(self.dns_guard.stop)
        self.local_prices = patch.dict(os.environ, {"LITELLM_LOCAL_MODEL_COST_MAP": "true"})
        self.local_prices.start()
        self.addCleanup(self.local_prices.stop)
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.card = {"entry_id": "FAKE", "name": "Synthetic protein", "species": "Synthetic organism", "uniprot": "SYNTHETIC"}
        (self.root / "inputs").mkdir()
        (self.root / "inputs/FAKE.json").write_text(json.dumps(self.card))
        (self.root / "prompts").mkdir()
        (self.root / "prompts/edison_query.md").write_text((ROOT / "prompts/edison_query.md").read_text())

    def test_extract_answer_citations_and_deduplicate(self):
        self.assertEqual(edison.extract_dois(ANSWER), ["10.5555/alpha", "10.5555/beta(2026)", "10.5555/gamma"])

    def test_extract_verbose_sdk_structure_and_encoded_doi(self):
        response = {"environment_frame": {"state": {"state": {"response": {
            "answer": {"formatted_answer": "https://doi.org/10.5555%2FDELTA."},
            "references": [{"url": "https://dx.doi.org/10.5555/EPSILON"}]}}}}}
        self.assertEqual(edison.extract_dois(response), ["10.5555/delta", "10.5555/epsilon"])

    def test_query_contains_identity_and_required_methods(self):
        query = edison.build_query(self.card, (ROOT / "prompts/edison_query.md").read_text())
        for text in ["Synthetic protein", "Synthetic organism", "SYNTHETIC", "CEST", "R1ρ", "PRE/RDC", "FRET", "EPR/DEER", "HDX-MS", "原始研究", "不列综述"]:
            self.assertIn(text, query)
        self.assertNotIn("curator_note", query)
        with self.assertRaisesRegex(ValueError, "species"):
            edison.build_query({**self.card, "species": None}, "{name}")

    def test_key_sources_and_environment_precedence(self):
        with patch.dict(os.environ, {"EDISON_API_KEY": " synthetic-env-key "}, clear=True), patch.object(Path, "read_text", side_effect=AssertionError("must not read file")):
            self.assertEqual(edison.read_api_key(), "synthetic-env-key")
        path = self.root / ".config/edison/api_key"
        path.parent.mkdir(parents=True)
        path.write_text("synthetic-file-key\n")
        with patch.dict(os.environ, {"EDISON_PLATFORM_API_KEY": "not-an-allowed-source"}, clear=True), patch.object(Path, "home", return_value=self.root):
            self.assertEqual(edison.read_api_key(), "synthetic-file-key")
            path.unlink()
            with self.assertRaises(edison.EdisonError):
                edison.read_api_key()

    def test_crossref_http_success_and_doi_mismatch(self):
        with patch.object(edison, "urlopen", return_value=io.BytesIO(json.dumps({"message": metadata("10.5555/alpha")}).encode())) as request:
            result, error = edison.crossref_lookup("10.5555/alpha")
        self.assertIsNone(error)
        self.assertEqual(result["DOI"], "10.5555/ALPHA")
        self.assertTrue(request.call_args.args[0].full_url.endswith("10.5555%2Falpha"))
        with patch.object(edison, "urlopen", return_value=io.BytesIO(b'{"message":{"DOI":"10.5555/other"}}')):
            self.assertEqual(edison.crossref_lookup("10.5555/alpha"), (None, "crossref_doi_mismatch"))

    def test_crossref_failure_types_are_not_valid_candidates(self):
        for exception, reason in [(HTTPError("fake", 404, "absent", None, None), "not_found_in_crossref"),
                                  (HTTPError("fake", 429, "rate limited", None, None), "http_429"),
                                  (URLError("offline"), "crossref_unavailable")]:
            with self.subTest(reason=reason), patch.object(edison, "urlopen", side_effect=exception):
                self.assertEqual(edison.crossref_lookup("10.5555/alpha"), (None, reason))

    def test_collect_only_verified_metadata_and_record_failures(self):
        calls = []

        def lookup(doi):
            calls.append(doi)
            if doi.endswith("gamma"):
                raise TimeoutError("synthetic failure")
            if doi.endswith("alpha"):
                return metadata(doi), None
            return None, "not_found_in_crossref"

        result = edison.collect_candidates("FAKE", ANSWER, lookup)
        self.assertEqual(len(calls), 3)
        self.assertEqual(result["search_status"], "incomplete")
        self.assertEqual(result["kept"], 1)
        self.assertEqual(result["candidates"][0], {"doi": "10.5555/alpha", "title": "Synthetic experimental study", "year": 2026, "abstract": None, "channel": "edison"})
        self.assertEqual(len(result["failed_requests"]), 2)

    def test_failed_task_and_empty_answer_are_not_complete(self):
        for status in ["in progress", "fail", "cancelled", "truncated"]:
            with self.subTest(status=status), self.assertRaises(edison.EdisonError):
                edison.collect_candidates("FAKE", {**ANSWER, "status": status})
        result = edison.collect_candidates("FAKE", {"status": "success", "answer": "No papers found"})
        self.assertEqual(result["search_status"], "incomplete")
        self.assertEqual(result["kept"], 0)

    def test_one_submission_raw_saved_and_reused(self):
        client = FakeClient()
        first = edison.retrieve("FAKE", "query", client, self.root / "edison")
        second = edison.retrieve("FAKE", "query", client, self.root / "edison")
        self.assertEqual(first, ANSWER)
        self.assertEqual(first, second)
        self.assertEqual(client.submissions, ["query"])
        self.assertEqual(client.fetches, ["synthetic-task-id"])
        self.assertEqual(json.loads((self.root / "edison/FAKE.raw.json").read_text()), ANSWER)

    def test_ambiguous_submission_cannot_be_retried_or_leak_secret(self):
        client = FakeClient()
        with patch.object(client, "create_task", side_effect=RuntimeError("synthetic-secret")) as create:
            for attempt in range(2):
                with self.subTest(attempt=attempt), self.assertRaises(edison.EdisonError) as error:
                    edison.retrieve("FAKE", "query", client, self.root / "edison")
                self.assertNotIn("synthetic-secret", str(error.exception))
            self.assertEqual(create.call_count, 1)
        self.assertNotIn("synthetic-secret", (self.root / "edison/FAKE.task.json").read_text())

    def test_fetch_failure_and_timeout_resume_same_task(self):
        client = FakeClient()
        with patch.object(client, "get_task", side_effect=TimeoutError("synthetic-secret")):
            with self.assertRaises(edison.EdisonError):
                edison.retrieve("FAKE", "query", client, self.root / "edison")
        with patch.object(edison.time, "monotonic", side_effect=[0, 0, 2, 2]):
            client.response = {"status": "in progress"}
            with self.assertRaises(edison.EdisonError):
                edison.retrieve("FAKE", "query", client, self.root / "edison", timeout=1)
        client.response = ANSWER
        self.assertEqual(edison.retrieve("FAKE", "query", client, self.root / "edison"), ANSWER)
        self.assertEqual(client.submissions, ["query"])

    def test_secret_redacted_from_raw_response(self):
        response = {**ANSWER, "metadata": {"echo": "synthetic-secret"}}
        edison.retrieve("FAKE", "query", FakeClient(response), self.root / "edison", "synthetic-secret")
        for path in (self.root / "edison").iterdir():
            self.assertNotIn("synthetic-secret", path.read_text())

    def test_sdk_adapter_uses_installed_literature_enum_and_single_attempt(self):
        from edison_client import EdisonClient, JobNames

        sdk = edison.EdisonSDK.__new__(edison.EdisonSDK)
        sdk.job_name = JobNames.LITERATURE
        sdk.client = EdisonClient(api_key="synthetic-only-key", cleanup_on_exit=False)
        self.addCleanup(sdk.client.close)
        with patch.object(EdisonClient, "client") as transport:
            transport.post.return_value.json.return_value = {"trajectory_id": "fake-task"}
            self.assertEqual(sdk.create_task("synthetic query"), "fake-task")
            self.assertEqual(transport.post.call_count, 1)
            payload = transport.post.call_args.kwargs["json"]
            self.assertEqual(payload["name"], JobNames.LITERATURE.value)
        with patch.object(EdisonClient, "client") as transport:
            transport.post.side_effect = TimeoutError("synthetic-secret")
            with self.assertRaises(TimeoutError):
                sdk.create_task("synthetic query")
            self.assertEqual(transport.post.call_count, 1)

    def test_merge_deduplicates_doi_and_preserves_sources(self):
        graph = {"entry": "FAKE", "search_status": "complete", "candidates": [
            {"doi": "https://doi.org/10.5555/ALPHA", "title": "Graph title", "abstract": "", "channel": "seed", "openalex": "W_FAKE"},
            {"doi": "", "title": "Graph paper without DOI", "channel": "reference"}]}
        source = edison.collect_candidates("FAKE", ANSWER, lambda doi: (metadata(doi), None))
        source["candidates"][0]["abstract"] = "Crossref abstract"
        original = copy.deepcopy(graph)
        result = merge.merge_candidates("FAKE", graph, source)
        self.assertEqual(result["kept"], 4)
        self.assertEqual(result["search_status"], "complete")
        shared = result["candidates"][0]
        self.assertEqual(shared["doi"], "10.5555/alpha")
        self.assertEqual(shared["sources"], ["citation_graph", "edison"])
        self.assertEqual(shared["channels"], ["seed", "edison"])
        self.assertEqual(shared["title"], "Graph title")
        self.assertEqual(shared["abstract"], "Crossref abstract")
        self.assertEqual(shared["openalex"], "W_FAKE")
        self.assertEqual(graph, original)

    def test_merge_incomplete_source_propagates_and_wrong_entry_rejected(self):
        graph = {"entry": "FAKE", "search_status": "complete", "candidates": []}
        source = {"entry": "FAKE", "search_status": "incomplete", "failed_requests": [{"doi": "10.5555/alpha", "reason": "http_429"}], "candidates": []}
        result = merge.merge_candidates("FAKE", graph, source)
        self.assertEqual(result["search_status"], "incomplete")
        self.assertEqual(result["failed_requests"][0]["source"], "edison")
        with self.assertRaises(ValueError):
            merge.merge_candidates("OTHER", graph, source)
        for entry in ["../forbidden", "/tmp/entry", ""]:
            with self.subTest(entry=entry), self.assertRaises(ValueError):
                edison.validate_entry(entry)

    def test_dry_run_and_missing_identity_never_read_credentials_or_submit(self):
        with patch.object(edison, "ROOT", self.root), patch.object(edison, "read_api_key", side_effect=AssertionError("no keys")), patch.object(edison, "EdisonSDK", side_effect=AssertionError("no real SDK")), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(edison.main(["FAKE", "--dry-run"]), 0)
            self.card["species"] = None
            (self.root / "inputs/FAKE.json").write_text(json.dumps(self.card))
            self.assertEqual(edison.main(["FAKE"]), 1)
        self.assertFalse((self.root / "outputs").exists())

    def test_cli_pipeline_and_revalidation_never_resubmit(self):
        client = FakeClient()
        with patch.object(edison, "ROOT", self.root), patch.object(edison, "read_api_key", return_value="synthetic-only-key"), patch.object(edison, "EdisonSDK", return_value=client), patch.object(edison, "collect_candidates", wraps=lambda entry, response: edison_collect(entry, response, lambda doi: (metadata(doi), None))), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(edison.main(["FAKE", "FAKE"]), 0)
        self.assertEqual(len(client.submissions), 1)
        with patch.object(edison, "ROOT", self.root), patch.object(edison, "EdisonSDK", side_effect=AssertionError("no client")), patch.object(edison, "read_api_key", side_effect=AssertionError("no keys")), patch.object(edison, "collect_candidates", wraps=lambda entry, response: edison_collect(entry, response, lambda doi: (metadata(doi), None))), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(edison.main(["FAKE", "--revalidate"]), 0)
        graph_path = self.root / "outputs/candidates/FAKE.json"
        graph_path.parent.mkdir()
        graph_path.write_text(json.dumps({"entry": "FAKE", "search_status": "complete", "candidates": []}))
        with patch.object(merge, "ROOT", self.root), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(merge.main(["FAKE"]), 0)
        self.assertEqual(json.loads((self.root / "outputs/candidates_merged/FAKE.json").read_text())["kept"], 3)


edison_collect = edison.collect_candidates


if __name__ == "__main__":
    unittest.main()
