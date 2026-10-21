#!/usr/bin/env python3
"""Check judgment_v0 files against the contract and evidence workbook.

Usage: python3 tools/check_judgment.py [ENTRY ...]
Results go to stdout and ENTRY.check.json; --dry-run writes only stdout/stderr.
Generated *.check.json files are excluded from default discovery.
"""

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENUMS = ("time_window", "direction", "verdict", "evidence_strength")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_evidence(root):
    from openpyxl import load_workbook

    evidence = {}
    pilot = root / "outputs/pilot133/pilot133_evidence.xlsx"  # RelaxDB-133 transfer pilot rows (same format)
    for path in [root / "outputs/gina_review_round1/RelaxDB_CPMG_evidence_round1.xlsx"] + ([pilot] if pilot.exists() else []):
        workbook = load_workbook(path, read_only=True, data_only=True)
        try:
            for name in ("Evidence_rows", "Appendix_rows"):
                rows = iter(workbook[name].values)
                header = next(rows, ())
                if "ID" not in header or len(header) < 3:
                    raise ValueError(f"{name}: missing ID or protein column")
                id_column = header.index("ID")
                for row in rows:
                    row_id = row[id_column]
                    if row_id is not None:
                        evidence.setdefault(str(row_id), []).append(str(row[2] or ""))
        finally:
            workbook.close()
    return evidence


def check_entry(entry, root=ROOT, evidence=None):
    """Return (report, warnings). Dependency/read failures fail acceptance."""
    root = Path(root)
    errors, warnings = [], []
    report = {"entry": entry, "pass": False, "n_judgments": 0, "errors": errors}

    def issue(jid, kind, detail):
        errors.append({"judgment_id": jid, "kind": kind, "detail": detail})

    def required(value, template, path, jid):
        if not isinstance(value, dict):
            issue(jid, "schema", f"{path} must be an object")
            return
        for key, spec in template.items():
            name = f"{path}.{key}"
            if isinstance(spec, str) and spec.startswith("OPTIONAL:") and key not in value:
                continue
            if key not in value:
                issue(jid, "schema", f"Missing {name}")
            elif isinstance(spec, dict):
                required(value[key], spec, name, jid)

    try:
        contract = read_json(root / "schema/judgment_contract.json")
        data = read_json(root / "outputs/judgment_v0" / f"{entry}.json")
    except (OSError, ValueError) as exc:
        issue(None, "schema", f"Cannot read contract or judgment file: {exc}")
        return report, warnings
    if not isinstance(data, dict):
        issue(None, "schema", "Judgment file must be an object")
        return report, warnings

    summary = data.get("protein_summary")
    if not isinstance(summary, dict) or not isinstance(summary.get("wt_apo_answer"), str) or not summary["wt_apo_answer"].strip():
        issue(None, "summary_missing", "protein_summary.wt_apo_answer is missing or empty")
    required(summary, contract["protein_summary"], "protein_summary", None)
    rows = data.get("judgments")
    if not isinstance(rows, list):
        issue(None, "schema", "judgments must be a list")
        return report, warnings
    report["n_judgments"] = len(rows)

    if evidence is None:
        try:
            evidence = load_evidence(root)
        except (OSError, ValueError, KeyError, ImportError) as exc:
            issue(None, "schema", f"Cannot load evidence workbook: {exc}")
            evidence = None
    sequence_length = None
    try:
        input_path = root / "inputs" / f"{entry}.json"
        if input_path.exists():
            case_input = read_json(input_path)
        else:
            sources = read_json(root / "outputs/gina_review_round1/case_sources.json")
            case_name = sources[entry]
            if Path(case_name).name != case_name or case_name.startswith(("S_", "C_")):
                raise ValueError("reference cases cannot supply sequence metadata")
            case_input = read_json(root / "cases" / case_name / "input.json")
        sequence = case_input["sequence"]
        if not isinstance(sequence, str) or not sequence:
            raise ValueError("sequence must be a nonempty string")
        sequence_length = len(sequence)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        issue(None, "schema", f"Cannot load entry sequence: {exc}")

    by_id = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            issue(None, "schema", f"judgments[{index}] must be an object")
            continue
        jid = row.get("judgment_id")
        if not isinstance(jid, str) or not jid.strip():
            issue(None, "schema", f"judgments[{index}].judgment_id must be a nonempty string")
        elif jid in by_id:
            issue(jid, "schema", "Duplicate judgment_id")
        else:
            by_id[jid] = row

    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            continue
        jid = row.get("judgment_id")
        if not isinstance(jid, str):
            jid = None
        required(row, contract["judgment_row"], f"judgments[{index}]", jid)
        entry_id = row.get("entry_id")
        if not isinstance(entry_id, str) or entry_id != entry:
            issue(jid, "schema", f"entry_id must equal {entry!r}")
        for field in ENUMS:
            allowed = contract["judgment_row"][field].split(" | ")
            if field in row and row[field] not in allowed:
                issue(jid, "schema", f"Invalid {field}: {row[field]!r}; expected {allowed}")

        state = row.get("sample_state")
        if isinstance(state, dict):
            for field, literals, prefixes in (
                ("binding_state", ("apo", "mixed", "unknown"), ("bound:",)),
                ("construct", ("WT",), ("mutant:", "other construct:")),
            ):
                value = state.get(field)
                if field in state and (not isinstance(value, str) or not (value in literals or value.startswith(prefixes))):
                    issue(jid, "schema", f"Invalid sample_state.{field}: {value!r}")
            if "is_wt_apo" in state and not isinstance(state["is_wt_apo"], bool):
                issue(jid, "schema", "sample_state.is_wt_apo must be boolean")

        region = row.get("region")
        residues = region.get("residues_entry") if isinstance(region, dict) else None
        residue_basis = region.get("residue_basis") if isinstance(region, dict) else None
        if isinstance(region, dict) and "residue_basis" in region and residue_basis not in (
                "author_listed", "global_fit_unlocalized", "per_residue"):
            issue(jid, "schema", f"Invalid region.residue_basis: {residue_basis!r}")
        if isinstance(residues, list):
            for residue in residues:
                if isinstance(residue, (int, float)) and not isinstance(residue, bool):
                    if residue < 1 or (sequence_length is not None and residue > sequence_length):
                        issue(jid, "residue_out_of_range", f"Residue {residue} outside 1..{sequence_length}")
                if type(residue) is not int:
                    issue(jid, "schema", f"Residue must be an integer: {residue!r}")
        elif residues != "unlocalized":
            issue(jid, "schema", "region.residues_entry must be a list or 'unlocalized'")

        refs = row.get("evidence_rows")
        if not isinstance(refs, list) or any(not isinstance(ref, str) for ref in refs):
            issue(jid, "schema", "evidence_rows must be a list of strings")
        if not refs and row.get("direction") not in ("not_measured", "search_insufficient"):
            issue(jid, "evidence_missing", "This direction requires at least one evidence row")
        if isinstance(refs, list) and evidence is not None:
            for ref in refs:
                if not isinstance(ref, str):
                    continue
                if ref not in evidence:
                    issue(jid, "evidence_unknown_id", f"Evidence row {ref!r} not found")
                elif isinstance(entry_id, str) and any(not protein.startswith(entry_id) for protein in evidence[ref]):
                    issue(jid, "evidence_wrong_protein", f"Evidence row {ref!r}: protein {evidence[ref]!r} does not start with {entry_id!r}")

        detection = row.get("detection")
        detection = detection if isinstance(detection, dict) else {}
        window = detection.get("detection_window")
        if row.get("direction") == "measured_not_detected" and (not window or isinstance(window, str) and not window.strip()):
            issue(jid, "window_missing", "measured_not_detected requires detection.detection_window")

        conflicts = row.get("conflicts_with")
        if not isinstance(conflicts, list) or any(not isinstance(ref, str) for ref in conflicts):
            issue(jid, "schema", "conflicts_with must be a list of judgment ids")
        if isinstance(conflicts, list):
            for ref in conflicts:
                if not isinstance(ref, str):
                    continue
                other = by_id.get(ref)
                if other is None:
                    issue(jid, "conflict_mismatch", f"Unknown conflicting judgment {ref!r}")
                    continue
                other_region = other.get("region")
                other_residues = other_region.get("residues_entry") if isinstance(other_region, dict) else None
                if row.get("time_window") != other.get("time_window"):
                    issue(jid, "conflict_mismatch", f"{ref}: different time_window")
                if isinstance(residues, list) and isinstance(other_residues, list) and not any(r in other_residues for r in residues):
                    issue(jid, "conflict_mismatch", f"{ref}: no residues_entry overlap")

        if row.get("verdict") == "dynamic_in_window" and row.get("evidence_strength") in ("md_only", "structure_only"):
            warnings.append({"judgment_id": jid, "kind": "weak_dynamic_evidence", "detail": "dynamic_in_window is supported only by MD or structure evidence"})
        model = detection.get("fit_model")
        kex = detection.get("kex")
        if (isinstance(model, str) and "global" in model.lower() and isinstance(residues, list)
                and len(residues) > 1 and kex is not None and str(kex).strip()
                and residue_basis not in ("author_listed", "per_residue")):
            issue(jid, "global_kex_assignment", "Global kex on multiple residues requires author_listed or per_residue residue_basis")

    report["pass"] = not errors
    return report, warnings


def main(argv=None, root=ROOT):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entries", nargs="*")
    parser.add_argument("--dry-run", action="store_true", help="Check without creating or changing any file")
    args = parser.parse_args(argv)
    directory = Path(root) / "outputs/judgment_v0"
    entries = args.entries or sorted(p.stem for p in directory.glob("*.json") if not p.name.endswith(".check.json"))
    all_pass = True
    evidence = None
    if entries:
        try:
            evidence = load_evidence(Path(root))
        except (OSError, ValueError, KeyError, ImportError):
            pass  # check_entry records dependency failures for each entry.
    for entry in dict.fromkeys(entries):
        if Path(entry).name != entry or entry in (".", ".."):
            report = {"entry": entry, "pass": False, "n_judgments": 0, "errors": [{"judgment_id": None, "kind": "schema", "detail": "ENTRY must be a filename stem, not a path"}]}
            warnings = []
        else:
            report, warnings = check_entry(entry, root, evidence)
            if not args.dry_run:
                try:
                    directory.mkdir(parents=True, exist_ok=True)
                    (directory / f"{entry}.check.json").write_text(json.dumps(report, ensure_ascii=False) + "\n", encoding="utf-8")
                except OSError as exc:
                    report["pass"] = False
                    report["errors"].append({"judgment_id": None, "kind": "schema", "detail": f"Cannot write check report: {exc}"})
        print(json.dumps(report, ensure_ascii=False))
        for warning in warnings:
            print(json.dumps({"entry": entry, "warning": warning}, ensure_ascii=False), file=sys.stderr)
        all_pass = all_pass and report["pass"]
    return 0 if all_pass else 3


if __name__ == "__main__":
    sys.exit(main())
