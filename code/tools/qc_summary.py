#!/usr/bin/env python3
"""One correctness line per protein plus the disagreement list for the scientist (Claude-side; reads RelaxDB labels).

Per protein: evidence rows, rows corrected after second read / review (per 100 rows), amide residues where the
literature judgment, the deposited-data screen and the RelaxDB label can be compared, and every disagreement.
  qc_summary.py ENTRY [ENTRY ...]  -> outputs/qc/qc_summary.csv, outputs/qc/disagreements.csv
"""
import csv
import json
import sys
from pathlib import Path

WORK = Path.home() / "dynamics_atlas_work"
EVAL = Path.home() / "dynamics_atlas_eval/downloads/hf_relaxdb/relaxdb"
OUT = WORK / "outputs/qc"
EX = {"^": "ex", "b": "ex", "X": "ex", "Y": "ex", "A": "no", "v": "no"}


def labels():
    lab = {}
    for f in ("relaxdb_data.csv", "relaxdb-cpmg_data.csv"):
        for r in csv.DictReader(open(EVAL / f)):
            lab[r["id"]] = r["label"]
    return lab


def cases_for(entry):
    pilot = json.loads((WORK / "outputs/pilot133/case_sources.json").read_text())
    if entry in pilot:
        names = pilot[entry]
    else:
        names = [json.loads((WORK / "outputs/gina_review_round1/case_sources.json").read_text())[entry]]
        prefix = entry.split("_")[0]
        names += [p.name for p in (WORK / "cases").glob(f"S_{prefix}_*")]
    return names


def main():
    lab, corr = labels(), json.loads((WORK / "ledger/row_corrections.json").read_text())
    OUT.mkdir(parents=True, exist_ok=True)
    summary, dis = [], []
    for e in sys.argv[1:]:
        names = cases_for(e)
        n_rows = sum(sum(1 for x in (WORK / "cases" / c / "rows.jsonl").read_text().splitlines() if x.strip()) for c in names)
        # a row counts as corrected when a field other than a caveat note changed (caveats add context, not fixes)
        n_corr = sum(len([k for k, v in corr.get(c, {}).items() if not k.startswith("_")
                          and isinstance(v, dict) and set(v) - {"caveat_append", "caveat_note"}]) for c in names)
        tr = json.loads((WORK / "outputs/tracks" / f"{e}.json").read_text())
        dep_path = WORK / "outputs/deposition" / f"{e}.json"
        dep = json.loads(dep_path.read_text()).get("track") if dep_path.exists() else None
        L, seq = lab.get(e, ""), json.loads((WORK / "inputs" / f"{e}.json").read_text())["sequence"]
        # main track = the WT-apo amide track with the most residues judged (states are never merged:
        # e.g. K-Ras GDP and GTP give opposite answers for the same residues)
        cand = [t for t in tr["tracks"] if t.get("is_wt_apo") and t.get("probe", "amide") == "amide"]
        main = max(cand, key=lambda t: sum(c in "XA" for c in t["labels"]), default=None)
        lit = list(main["labels"]) if main else ["N"] * len(seq)
        src = {i: ",".join(main["provenance"].get(str(i + 1), [])) for i in range(len(seq))} if main else {}
        both_lr = both_ld = agree_lr = agree_ld = 0
        for i in range(len(seq)):
            l = {"X": "ex", "A": "no"}.get(lit[i])
            r = EX.get(L[i]) if i < len(L) else None
            d = {"X": "ex", "A": "no", "V": "no"}.get(dep[i]) if dep else None
            if l and r:
                both_lr += 1; agree_lr += l == r
            if l and d:
                both_ld += 1; agree_ld += l == d
            if l and ((r and l != r) or (d and l != d)):
                dis.append([e, f"{seq[i]}{i + 1}", l, d or "-", r or "-", src.get(i, ""), (main or {}).get("state", "")[:90]])
        summary.append([e, (main or {}).get("state", "")[:70], n_rows, n_corr, round(100 * n_corr / n_rows, 1) if n_rows else "", lit.count("X"), lit.count("A"),
                        f"{agree_lr}/{both_lr}", f"{agree_ld}/{both_ld}" if dep else "n/a"])
    with open(OUT / "qc_summary.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["entry", "main_state", "evidence_rows", "rows_corrected", "corrected_per_100", "lit_amide_exchange", "lit_amide_none",
                    "lit_vs_relaxdb_agree", "lit_vs_deposition_agree"])
        w.writerows(summary)
    with open(OUT / "disagreements.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["entry", "residue", "literature", "deposition_screen", "relaxdb_label", "judgments", "sample_state"])
        w.writerows(dis)
    for r in summary:
        print(r)
    print(len(dis), "disagreements")


if __name__ == "__main__":
    main()
