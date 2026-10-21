#!~/.venvs/atlas-tools/bin/python
"""Merge citation-graph and Edison candidate lists by normalized DOI, offline."""
import argparse
from copy import deepcopy
import json
from pathlib import Path
import sys

from edison_candidates import normalize_doi, validate_entry, write_json

ROOT = Path(__file__).resolve().parents[1]


def candidate_rows(document, entry):
    if not isinstance(document, dict) or document.get("entry") != entry:
        raise ValueError("candidate source entry does not match requested ENTRY")
    rows = document.get("candidates")
    if not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
        raise ValueError("candidate source must contain a list of candidate objects")
    return rows


def merge_candidates(entry, graph, edison):
    validate_entry(entry)
    merged, counts, without_doi = {}, {}, []
    for source, document in (("citation_graph", graph), ("edison", edison)):
        rows = candidate_rows(document, entry)
        counts[source] = len(rows)
        for row in rows:
            doi = normalize_doi(row.get("doi"))
            if row.get("doi") and not doi:
                raise ValueError("invalid DOI in " + source)
            channel = row.get("channel") or source
            if not isinstance(channel, str):
                raise ValueError("candidate channel must be a string")
            if not doi and source == "edison":
                raise ValueError("Edison candidates must have a verified DOI")
            if not doi or doi not in merged:
                candidate = deepcopy(row)
                candidate.update(doi=doi, channel=channel, sources=[source], channels=[channel])
                if doi:
                    merged[doi] = candidate
                else:
                    without_doi.append(candidate)
            else:
                candidate = merged[doi]
                for key, value in row.items():
                    if key not in {"doi", "channel", "sources", "channels"} and not candidate.get(key) and value is not None:
                        candidate[key] = deepcopy(value)
                if source not in candidate["sources"]:
                    candidate["sources"].append(source)
                if channel not in candidate["channels"]:
                    candidate["channels"].append(channel)
    candidates = list(merged.values()) + without_doi
    failures = [{"source": source, "detail": failure}
                for source, document in (("citation_graph", graph), ("edison", edison))
                for failure in document.get("failed_requests", [])]
    statuses = {"citation_graph": graph.get("search_status", "incomplete"),
                "edison": edison.get("search_status", "incomplete")}
    return {"entry": entry, "kept": len(candidates), "source_counts": counts,
            "source_status": statuses, "search_status": "complete" if not failures and all(
                status == "complete" for status in statuses.values()) else "incomplete",
            "failed_requests": failures, "candidates": candidates}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entries", nargs="+", type=validate_entry)
    args = parser.parse_args(argv)
    failed = False
    for entry in dict.fromkeys(args.entries):
        try:
            graph = json.loads((ROOT / "outputs/candidates" / f"{entry}.json").read_text(encoding="utf-8"))
            edison = json.loads((ROOT / "outputs/edison" / f"{entry}.candidates.json").read_text(encoding="utf-8"))
            result = merge_candidates(entry, graph, edison)
            write_json(ROOT / "outputs/candidates_merged" / f"{entry}.json", result)
            print(json.dumps({"entry": entry, "kept": result["kept"], "search_status": result["search_status"]}))
            failed = failed or result["search_status"] != "complete"
        except (OSError, ValueError, TypeError):
            failed = True
            print(f"{entry}: missing or invalid candidate source; merged output not updated", file=sys.stderr)
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
