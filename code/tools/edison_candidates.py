#!~/.venvs/atlas-tools/bin/python
"""Retrieve DOI-only literature candidates; never produce scientific evidence rows."""
import argparse
import html
import json
import logging
import math
import os
from pathlib import Path
import re
import sys
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DOI_PATTERN = re.compile(r"10\.\d{4,9}/[^\s<>\"'\[\]{}\\?#`*，。；：！？]+", re.IGNORECASE)
EVIDENCE_KEYS = {"answer", "formatted_answer", "references", "citations", "bibliography", "contexts"}
SKIP_KEYS = {"query", "task", "answer_reasoning", "reasoning", "agent_state", "deployment_config"}
TERMINAL = {"success", "fail", "cancelled", "truncated"}


class EdisonError(RuntimeError):
    pass


class ProteinIdentityError(ValueError):
    pass


def validate_entry(entry):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", entry):
        raise ValueError("ENTRY must be a single input filename stem")
    return entry


def normalize_doi(value):
    if not isinstance(value, str):
        return ""
    text = html.unescape(unquote(value.strip()))
    text = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", text, flags=re.IGNORECASE)
    text = text.rstrip(".,;:!?，。；：！")
    while text.endswith(")") and text.count(")") > text.count("("):
        text = text[:-1].rstrip(".,;:")
    return text.lower() if DOI_PATTERN.fullmatch(text) else ""


def extract_dois(response):
    found = set()

    def visit(value, evidence=False):
        if isinstance(value, str) and evidence:
            for match in DOI_PATTERN.finditer(html.unescape(unquote(value))):
                doi = normalize_doi(match.group())
                if doi:
                    found.add(doi)
        elif isinstance(value, dict):
            for key, child in value.items():
                if key not in SKIP_KEYS:
                    visit(child, evidence or key in EVIDENCE_KEYS)
        elif isinstance(value, list):
            for child in value:
                visit(child, evidence)

    visit(response, isinstance(response, str))
    return sorted(found)


def build_query(card, template):
    species = card.get("species") or card.get("organism")
    if isinstance(species, dict):
        species = species.get("scientific_name") or species.get("scientificName") or species.get("name")
    fields = {"name": card.get("name"), "species": species, "uniprot": card.get("uniprot")}
    missing = [key for key, value in fields.items() if not isinstance(value, str) or not value.strip()]
    if missing:
        raise ProteinIdentityError("input protein identity missing: " + ", ".join(missing))
    return template.format(**{key: value.strip() for key, value in fields.items()})


def read_api_key():
    key = os.environ.get("EDISON_API_KEY", "").strip()
    if not key:
        path = Path.home() / ".config/edison/api_key"
        try:
            key = path.read_text(encoding="utf-8").strip()
        except OSError:
            raise EdisonError("EDISON_API_KEY or ~/.config/edison/api_key is required") from None
    if not key:
        raise EdisonError("Edison API key is empty")
    return key


def write_json(path, payload, secret=""):
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if secret:
        text = text.replace(json.dumps(secret, ensure_ascii=False)[1:-1], "[REDACTED]")
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        temporary = Path(handle.name)
        handle.write(text)
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def quiet_call(function, *args, **kwargs):
    previous = logging.root.manager.disable
    logging.disable(sys.maxsize)
    try:
        return function(*args, **kwargs)
    finally:
        logging.disable(previous)


class EdisonSDK:
    def __init__(self, api_key):
        from edison_client import EdisonClient, JobNames

        self.job_name = JobNames.LITERATURE
        self.client = quiet_call(EdisonClient, api_key=api_key, verbose_logging=False)

    def create_task(self, query):
        method = type(self.client).create_task
        single_attempt = getattr(method, "__wrapped__", None)
        if single_attempt is None:
            raise EdisonError("SDK single-attempt submission is unavailable; no task submitted")
        return quiet_call(single_attempt, self.client, {"name": self.job_name, "query": query})

    def get_task(self, task_id):
        response = quiet_call(self.client.get_task, task_id, verbose=True)
        return response.model_dump(mode="json")

    def close(self):
        quiet_call(self.client.close)


def retrieve(entry, query, client, output, secret="", timeout=3600, poll_interval=15):
    validate_entry(entry)
    if not math.isfinite(timeout) or timeout <= 0 or not 0 < poll_interval <= 60:
        raise ValueError("timeout must be positive; poll interval must be in (0, 60]")
    output.mkdir(parents=True, exist_ok=True)
    raw_path = output / f"{entry}.raw.json"
    task_path = output / f"{entry}.task.json"
    if raw_path.exists():
        return json.loads(raw_path.read_text(encoding="utf-8"))
    if task_path.exists():
        receipt = json.loads(task_path.read_text(encoding="utf-8"))
        task_id = receipt.get("task_id")
        if not task_id:
            raise EdisonError("submission outcome unknown; inspect existing Edison task, do not resubmit")
    else:
        with task_path.open("x", encoding="utf-8") as handle:
            json.dump({"entry": entry, "job": "LITERATURE", "state": "submitting", "task_id": None}, handle)
        try:
            task_id = client.create_task(query)
        except Exception:
            raise EdisonError("submission failed or outcome unknown; task reservation retained, no retry") from None
        if not isinstance(task_id, str) or not task_id:
            raise EdisonError("submission returned no task ID; reservation retained, do not resubmit")
        write_json(task_path, {"entry": entry, "job": "LITERATURE", "state": "submitted", "task_id": task_id}, secret)
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            response = client.get_task(task_id)
        except Exception:
            raise EdisonError("task fetch failed; rerun to retrieve the same task, not submit another") from None
        status = response.get("status")
        if status in TERMINAL:
            write_json(raw_path, response, secret)
            return json.loads(raw_path.read_text(encoding="utf-8"))
        remaining = deadline - time.monotonic()
        if remaining > 0:
            time.sleep(min(poll_interval, remaining))
    raise EdisonError("wait timed out; task ID retained, rerun to retrieve the same task")


def crossref_lookup(doi):
    request = Request("https://api.crossref.org/works/" + quote(doi, safe=""),
                      headers={"User-Agent": "dynamics-atlas-edison/1.0", "Accept": "application/json"})
    try:
        with urlopen(request, timeout=30) as response:
            payload = json.load(response)
    except HTTPError as error:
        return None, "not_found_in_crossref" if error.code == 404 else f"http_{error.code}"
    except (URLError, OSError, ValueError):
        return None, "crossref_unavailable"
    message = payload.get("message") if isinstance(payload, dict) else None
    if not isinstance(message, dict) or normalize_doi(message.get("DOI")) != doi:
        return None, "crossref_doi_mismatch"
    return message, None


def candidate_from_metadata(doi, message):
    title = message.get("title") or []
    title = title[0] if isinstance(title, list) and title else title
    if not isinstance(title, str):
        title = ""
    year = None
    for field in ("published", "published-print", "published-online", "issued"):
        date = message.get(field) or {}
        parts = date.get("date-parts", []) if isinstance(date, dict) else []
        if parts and isinstance(parts[0], list) and parts[0] and type(parts[0][0]) is int:
            year = parts[0][0]
            break
    return {"doi": doi, "title": html.unescape(re.sub(r"<[^>]+>", "", title)), "year": year,
            "abstract": message.get("abstract") or None, "channel": "edison"}


def collect_candidates(entry, response, lookup=crossref_lookup):
    validate_entry(entry)
    if response.get("status") != "success" or response.get("has_successful_answer") is False:
        raise EdisonError("Edison did not return a successful answer; raw response retained")
    candidates, failures = [], []
    dois = extract_dois(response)
    for doi in dois:
        try:
            metadata, error = lookup(doi)
        except Exception:
            metadata, error = None, "crossref_unavailable"
        if error or not isinstance(metadata, dict):
            failures.append({"doi": doi, "reason": error or "crossref_invalid_metadata"})
        elif normalize_doi(metadata.get("DOI")) != doi:
            failures.append({"doi": doi, "reason": "crossref_doi_mismatch"})
        else:
            candidates.append(candidate_from_metadata(doi, metadata))
    if not dois:
        failures.append({"doi": None, "reason": "no_doi_in_answer_or_citations"})
    return {"entry": entry, "channel": "edison", "pool": len(dois), "kept": len(candidates),
            "search_status": "incomplete" if failures else "complete",
            "failed_requests": failures, "candidates": candidates}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entries", nargs="+", type=validate_entry)
    parser.add_argument("--dry-run", action="store_true", help="validate identity and print query without credentials or network")
    parser.add_argument("--revalidate", action="store_true", help="only recheck existing raw responses with Crossref; never submit")
    parser.add_argument("--timeout", type=float, default=3600)
    args = parser.parse_args(argv)
    if not math.isfinite(args.timeout) or args.timeout <= 0:
        parser.error("--timeout must be positive and finite")
    if args.dry_run and args.revalidate:
        parser.error("--dry-run and --revalidate are mutually exclusive")
    output = ROOT / "outputs/edison"
    client, secret, failed = None, "", False
    try:
        for entry in dict.fromkeys(args.entries):
            try:
                raw_path = output / f"{entry}.raw.json"
                if args.revalidate or (raw_path.exists() and not args.dry_run):
                    response = json.loads(raw_path.read_text(encoding="utf-8"))
                else:
                    card = json.loads((ROOT / "inputs" / f"{entry}.json").read_text(encoding="utf-8"))
                    template = (ROOT / "prompts/edison_query.md").read_text(encoding="utf-8")
                    query = build_query(card, template)
                    if args.dry_run:
                        print(f"--- {entry} ---\n{query}")
                        continue
                    if client is None:
                        secret = read_api_key()
                        client = EdisonSDK(secret)
                    response = retrieve(entry, query, client, output, secret, timeout=args.timeout)
                result = collect_candidates(entry, response)
                write_json(output / f"{entry}.candidates.json", result, secret)
                print(json.dumps({"entry": entry, "kept": result["kept"], "search_status": result["search_status"]}))
                failed = failed or result["search_status"] != "complete"
            except (ValueError, EdisonError) as error:
                failed = True
                message = str(error) if isinstance(error, (EdisonError, ProteinIdentityError)) else "invalid JSON; check input"
                print(f"{entry}: {message}", file=sys.stderr)
            except Exception:
                failed = True
                print(f"{entry}: operation failed; no automatic resubmission", file=sys.stderr)
    finally:
        if client is not None:
            try:
                client.close()
            except Exception:
                pass
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
