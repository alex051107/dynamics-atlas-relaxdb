#!/usr/bin/env python3
"""Turn judgment-layer files into RelaxDB-style per-residue label tracks and compare them with RelaxDB labels.

One track = one protein x one sample state (construct; binding state; conditions) in the us-ms window.
Track letters (one per entry residue):
  X  exchange detected (judgment direction detected / unclear_second_process)
  A  measured, not detected in this window (measured_not_detected)
  F  artefact suspected
  N  no residue-level judgment (not measured, unlocalized, or not covered)
Residues named by several judgments of one state keep the strongest letter (X > F > A > N) and list every judgment id.

  judgment_to_tracks.py [ENTRY ...]   -> outputs/tracks/<ENTRY>.json and outputs/tracks/summary.csv
RelaxDB labels are read only for comparison (Claude-side evaluation file), never fed back into judgments.
"""
import csv
import json
import sys
from pathlib import Path

WORK = Path.home() / "dynamics_atlas_work"
JUDG = WORK / "outputs/judgment_v0"
OUT = WORK / "outputs/tracks"
LABELS = Path.home() / "dynamics_atlas_eval/downloads/hf_relaxdb/relaxdb/relaxdb-cpmg_data.csv"
LABELS_133 = Path.home() / "dynamics_atlas_eval/downloads/hf_relaxdb/relaxdb/relaxdb_data.csv"
RANK = {"N": 0, "A": 1, "F": 2, "X": 3}
LETTER = {"detected": "X", "unclear_second_process": "X", "measured_not_detected": "A", "artefact_suspected": "F"}
# RelaxDB CPMG letters (HF data card): X, Y = exchange; A = no exchange; '.' = missing peak; N = not measured; P = proline
RELAXDB = {"X": "ex", "Y": "ex", "A": "no", ".": "missing", "N": "na", "P": "na"}
# RelaxDB-133 letters (HF data card, R1/R2/NOE set): ^ Rex, b mixed fast/slow = exchange; A, v (fast motion) = no exchange;
# '.' missing peak (Dyna-1 scores it positive, but a missing peak is not literature exchange evidence: kept separate)
RELAXDB_133 = {"^": "ex", "b": "ex", "A": "no", "v": "no", ".": "missing", "t": "na", "x": "na", "p": "na"}


def sequence(entry):
    card = WORK / "inputs" / f"{entry}.json"
    if not entry.endswith("_CPMG") and card.exists():
        return json.loads(card.read_text())["sequence"]
    cases = json.loads((WORK / "outputs/gina_review_round1/case_sources.json").read_text())
    return json.loads((WORK / "cases" / cases[entry] / "input.json").read_text())["sequence"]


def probe(j):
    """RelaxDB labels are backbone-amide labels; side-chain methyl data are a different probe and are not compared."""
    d = j.get("detection", {})
    text = " ".join(str(d.get(k, "")) for k in ("method", "observable")).lower()
    if "methyl" in text:
        return "methyl"
    if any(k in text for k in ("cα", "calpha", "c′", "c'", "13c", "multiple-quantum", "multiple quantum")):
        return "carbon"
    return "amide"


def state_key(j):
    s = j.get("sample_state", {})
    return f"{s.get('construct', '')} | {s.get('binding_state', '')} | {s.get('conditions', '')} | probe:{probe(j)}"


def tracks(entry):
    seq = sequence(entry)
    data = json.loads((JUDG / f"{entry}.json").read_text())
    out = {}
    for j in data.get("judgments", []):
        if j.get("time_window") != "us-ms" or j.get("direction") not in LETTER:
            continue
        key = state_key(j)
        t = out.setdefault(key, {"state": key, "is_wt_apo": j.get("sample_state", {}).get("is_wt_apo"), "probe": probe(j),
                                 "labels": ["N"] * len(seq), "provenance": {}, "unlocalized_judgments": []})
        res = j.get("region", {}).get("residues_entry")
        if not isinstance(res, list):
            t["unlocalized_judgments"].append(j["judgment_id"])
            continue
        letter = LETTER[j["direction"]]
        for r in res:
            if isinstance(r, int) and 1 <= r <= len(seq):
                i = r - 1
                if RANK[letter] > RANK[t["labels"][i]]:
                    t["labels"][i] = letter
                t["provenance"].setdefault(str(r), []).append(j["judgment_id"])
    for t in out.values():
        t["labels"] = "".join(t["labels"])
    return seq, list(out.values())


def relaxdb_labels():
    rows = {}
    for path, vocab in ((LABELS_133, RELAXDB_133), (LABELS, RELAXDB)):  # CPMG ids end in _CPMG, so no clash
        if path.exists():
            with open(path, newline="") as fh:
                for r in csv.DictReader(fh):
                    rows[r["id"]] = {**r, "_vocab": vocab}
    return rows


def compare(track, label, seq, vocab=RELAXDB):
    if not label or len(label) != len(seq):
        return None
    both = agree = 0
    disagree = []
    for i, (ours, ref) in enumerate(zip(track["labels"], label)):
        ref_c = vocab.get(ref)
        if ours not in ("X", "A") or ref_c not in ("ex", "no"):
            continue
        both += 1
        if (ours == "X") == (ref_c == "ex"):
            agree += 1
        else:
            disagree.append(f"{seq[i]}{i + 1}:ours={ours},relaxdb={ref}")
    covered_ex = sum(1 for ref in label if vocab.get(ref) == "ex")
    ours_on_ex = sum(1 for o, ref in zip(track["labels"], label) if vocab.get(ref) == "ex" and o != "N")
    return {"residues_both_informative": both, "agree": agree,
            "agreement": round(agree / both, 3) if both else None,
            "relaxdb_exchange_residues": covered_ex, "of_which_we_cover": ours_on_ex, "disagreements": disagree}


def main():
    entries = sys.argv[1:] or sorted(p.stem for p in JUDG.glob("*_CPMG.json"))
    OUT.mkdir(parents=True, exist_ok=True)
    ref = relaxdb_labels()
    summary = []
    for e in entries:
        seq, ts = tracks(e)
        label = (ref.get(e) or {}).get("label")
        vocab = (ref.get(e) or {}).get("_vocab", RELAXDB)
        for t in ts:
            t["vs_relaxdb"] = compare(t, label, seq, vocab) if t["probe"] == "amide" else None
            c = t["vs_relaxdb"] or {}
            summary.append([e, t["state"][:120], t["is_wt_apo"], t["labels"].count("X"), t["labels"].count("A"),
                            len(t["unlocalized_judgments"]), c.get("residues_both_informative"), c.get("agree"),
                            c.get("relaxdb_exchange_residues"), c.get("of_which_we_cover")])
        (OUT / f"{e}.json").write_text(json.dumps({"entry": e, "sequence_length": len(seq), "relaxdb_label": label,
                                                    "tracks": ts}, indent=1, ensure_ascii=False))
    with open(OUT / "summary.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["entry", "state", "is_wt_apo", "n_X", "n_A", "n_unlocalized_judgments", "both_informative", "agree",
                    "relaxdb_exchange_residues", "of_which_we_cover"])
        w.writerows(summary)
    print(f"{len(summary)} tracks -> {OUT}")


if __name__ == "__main__":
    main()
