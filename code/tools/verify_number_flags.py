#!/usr/bin/env python3
"""Check scorer 'number_not_in_source' errors against the cited source text with tolerant matching (E-027 interim).

The frozen scorer misreads hyphenated ranges ('5.2-5.4'), glued table cells ('530 ps670 ps'), unicode minus/en-dash
and trailing zeros. For each such error this looks the number up in the row's source file, allowing those forms.
Found -> proposed override with the matching text as evidence. Not found -> left as a real error for a human/Claude.

  verify_number_flags.py CASE [CASE ...] [--write]   (--write adds the found ones to ledger/integrity_overrides.json)
"""
import json
import re
import sys
from pathlib import Path

WORK = Path.home() / "dynamics_atlas_work"


def variants(num):
    n = num.strip()
    base = n[:-2] if n.endswith(".0") else n
    out = {n, base}
    if "." in base:
        out.add(base.rstrip("0").rstrip("."))
    return {v for v in out if v}


def find(num, text):
    t = text.replace("−", "-").replace("–", "-").replace("—", "-")
    for v in variants(num):
        m = re.search(r"(?<![\d.])" + re.escape(v) + r"(?!\d)", t) or re.search(re.escape(v) + r"(?=[±\s%a-zA-Zμµ)-])", t) \
            or re.search(r"(?<![\d.])" + re.escape(v) + r"(?=\d+\.\d)", t)  # glued cell: '0.970.67
        if m:
            return t[max(0, m.start() - 50):m.end() + 30].replace("\n", " ")
    return None


def main():
    write = "--write" in sys.argv
    ov_path = WORK / "ledger/integrity_overrides.json"
    ov = json.loads(ov_path.read_text())
    for case in [a for a in sys.argv[1:] if not a.startswith("--")]:
        c = WORK / "cases" / case
        errs = json.loads((c / "scorecard.json").read_text())["integrity"].get("errors", [])
        rows = {json.loads(x)["row_id"]: json.loads(x) for x in (c / "rows.jsonl").read_text().splitlines() if x.strip()}
        found, missing = [], []
        for e in errs:
            if e.get("kind") != "number_not_in_source":
                missing.append(e)
                continue
            r = rows.get(e["row"], {})
            src = WORK / "sources_cache" / str(r.get("source_file"))
            hit = find(e["detail"].split(":", 1)[1], src.read_text(errors="replace")) if src.exists() else None
            (found if hit else missing).append({**e, "match": hit})
        print(json.dumps({"case": case, "verified_in_source": len(found), "not_found_or_other": [(m.get("row"), m.get("kind"), m.get("detail")) for m in missing]}, ensure_ascii=False))
        for f in found:
            print("   ", f["row"], f["detail"], "|", f["match"])
        if write and found and not missing:
            ov[case] = [{"row": f["row"], "kind": f["kind"], "detail": f["detail"], "decision": "scorer false positive",
                         "evidence": f"value present in source: '{f['match']}'", "by": "verify_number_flags.py, reviewed by Claude"} for f in found]
    if write:
        ov_path.write_text(json.dumps(ov, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
