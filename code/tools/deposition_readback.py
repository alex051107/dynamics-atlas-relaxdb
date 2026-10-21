#!/usr/bin/env python3
"""Read the relaxation data deposited in BMRB for an entry and screen it per residue (no LLM).

Per-residue R1, R2 (or R1rho), heteronuclear NOE under the deposited conditions, then a fixed screen:
  fast_motion       NOE < 0.65
  possible_exchange R2/R1 > mean + 1.5 SD of residues with NOE >= 0.65 (one pass, termini kept out by the NOE cut)
These are screening heuristics, not fits. R2/R1 is also raised by anisotropic tumbling (e.g. the GB3 helix,
Hall & Fushman 2003), so a possible_exchange flag is a lead to check against the literature, never a verdict. The RelaxDB-133 labels were computed from the same deposited numbers,
so any agreement with them checks this readback, never the science.

  deposition_readback.py ENTRY [ENTRY ...]   (ENTRY = inputs/<ENTRY>.json with bmrb_id)
  -> outputs/deposition/<ENTRY>.json ; raw API responses cached in sources_cache/bmrb/
"""
import json
import statistics
import sys
import urllib.request
from pathlib import Path

WORK = Path.home() / "dynamics_atlas_work"
CACHE = WORK / "sources_cache/bmrb"
OUT = WORK / "outputs/deposition"
AA = {"ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C", "GLN": "Q", "GLU": "E", "GLY": "G", "HIS": "H", "ILE": "I",
      "LEU": "L", "LYS": "K", "MET": "M", "PHE": "F", "PRO": "P", "SER": "S", "THR": "T", "TRP": "W", "TYR": "Y", "VAL": "V"}
FRAMES = {"T1": "heteronucl_T1_relaxation", "T2": "heteronucl_T2_relaxation", "T1rho": "heteronucl_T1rho_relaxation",
          "NOE": "heteronucl_NOEs", "cond": "sample_conditions"}


def frame(bmrb, cat):
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"{bmrb}_{cat}.json"
    if not path.exists():
        url = f"https://api.bmrb.io/v2/entry/{bmrb}?saveframe_category={cat}"
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "dynamics-atlas/1.0"}), timeout=60) as r:
            path.write_bytes(r.read())
    return json.loads(path.read_text()).get(str(bmrb), {}).get(cat, [])


def tag(sf, name):
    return next((v for k, v in sf.get("tags", []) if k == name), None)


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def rows(sf, kind):
    """(seq_id, comp, value, error) for the 15N rows of one relaxation list, values as rates in s-1 where units allow."""
    want = {"T1": "_T1", "T2": "_T2", "T1rho": "_T1rho", "NOE": "_Heteronucl_NOE"}[kind]
    loop = next((lp for lp in sf.get("loops", []) if lp["category"] == want), None)
    if not loop:
        return [], {}
    t = loop["tags"]
    if kind == "NOE":
        seq, comp, val, err = t.index("Seq_ID_1"), t.index("Comp_ID_1"), t.index("Val"), t.index("Val_err")
        units = tag(sf, "Heteronuclear_NOE_val_type")
    else:
        vcol = {"T1": "Val", "T2": "T2_val", "T1rho": "T1rho_val"}[kind]
        ecol = {"T1": "Val_err", "T2": "T2_val_err", "T1rho": "T1rho_val_err"}[kind]
        if vcol not in t:
            vcol, ecol = "Val", "Val_err"
        seq, comp, val, err = t.index("Seq_ID"), t.index("Comp_ID"), t.index(vcol), t.index(ecol)
        units = tag(sf, {"T1": "T1_val_units", "T2": "T2_val_units", "T1rho": "T1rho_val_units"}[kind])
    out, n_err_gt = [], 0
    for d in loop["data"]:
        v, e = num(d[val]), num(d[err])
        if v is None or not str(d[seq]).isdigit():
            continue
        if e is not None and e > abs(v):
            n_err_gt += 1
        if kind != "NOE" and units in ("s", "ms"):
            scale = 1000.0 if units == "ms" else 1.0
            r = scale / v if v else None
            e = (e / v) * r if (e is not None and v and r) else None
            v = r
        out.append((int(d[seq]), d[comp], v, e))
    info = {"units_deposited": units, "converted_to_rate": kind != "NOE" and units in ("s", "ms"),
            "field_1H_MHz": tag(sf, "Spectrometer_frequency_1H"), "n": len(out),
            "error_larger_than_value": n_err_gt,
            "consistent": units in ("s", "ms", "s-1", "1/s") or kind == "NOE"}
    if out and n_err_gt > 0.2 * len(out):
        info["consistent"] = False
        info["problem"] = "error column larger than value for >20% of rows; columns may be swapped or mislabelled"
    return out, info


def offset(dep_seq, entry_seq):
    """Shift d such that entry index = bmrb seq_id + d, chosen to maximise residue-type matches."""
    best = (0, 0)
    for d in range(-60, 61):
        m = sum(1 for s, c in dep_seq.items() if 1 <= s + d <= len(entry_seq) and entry_seq[s + d - 1] == c)
        best = max(best, (m, d))
    return best[1], best[0]


def readback(entry, bmrb_override=None):
    card = json.loads((WORK / "inputs" / f"{entry}.json").read_text())
    bmrb, seq = bmrb_override or card.get("bmrb_id") or entry, card["sequence"]
    lists = {}
    for kind in ("T1", "T2", "T1rho", "NOE"):
        for i, sf in enumerate(frame(bmrb, FRAMES[kind])):
            data, info = rows(sf, kind)
            if data:
                lists[f"{kind}_{i + 1}"] = {"info": info | {"conditions_label": tag(sf, "Sample_condition_list_label")}, "data": data}
    conds = [{"label": sf.get("name"), "values": [lp["data"] for lp in sf.get("loops", []) if lp["category"] == "_Sample_condition_variable"]}
             for sf in frame(bmrb, FRAMES["cond"])]
    report = {"entry": entry, "bmrb_id": bmrb, "sample_conditions": conds, "lists": {k: v["info"] for k, v in lists.items()},
              "screen_rule": "fast_motion: NOE < 0.65; possible_exchange: R2/R1 > mean + 1.5 SD over residues with NOE >= 0.65",
              "circularity": "RelaxDB-133 labels derive from these deposited numbers; agreement checks this readback only"}
    if not lists:
        report["status"] = "no relaxation lists deposited"
        return report
    dep_seq = {s: AA.get(c, "X") for v in lists.values() for s, c, _, _ in v["data"]}
    d, matches = offset(dep_seq, seq)
    report["numbering"] = {"entry_index = bmrb_seq_id +": d, "type_matches": matches, "residues_deposited": len(dep_seq)}
    if matches < 0.9 * len(dep_seq):
        report["status"] = "numbering could not be matched to the entry sequence"
        return report
    for v in lists.values():  # a 15N R1 at 400-900 MHz lies near 0.5-3 s-1; far outside means mislabelled units
        rates = sorted(x[2] for x in v["data"] if x[2] is not None)
        if rates and v["info"]["units_deposited"] != "relative intensities" and not v["info"].get("units_deposited", "").startswith("peak"):
            med = rates[len(rates) // 2]
            if med < 0.05 or med > 200:
                v["info"]["units_suspect"] = f"median {med:.4g} s-1 after conversion; absolute values unreliable, ratios kept"
    pick = lambda k: next((v for n, v in lists.items() if n.startswith(k) and v["info"]["consistent"]), None)
    r1, r2, noe = pick("T1_"), pick("T2_") or pick("T1rho_"), pick("NOE_")
    per = {}
    for name, lst in (("R1", r1), ("R2", r2), ("NOE", noe)):
        for s, c, v, e in (lst or {}).get("data", []):
            per.setdefault(s + d, {"res": f"{c and AA.get(c, '?')}{s + d}"})[name] = round(v, 4) if v is not None else None
    usable = r1 is not None and r2 is not None
    report["status"] = "screened" if usable else "R1 or R2 list missing or inconsistent; values listed, no screen"
    if usable:
        rig = [p["R2"] / p["R1"] for p in per.values() if p.get("R1") and p.get("R2") and (p.get("NOE") is None or p["NOE"] >= 0.65)]
        if len(rig) >= 5:
            cut = statistics.mean(rig) + 1.5 * statistics.pstdev(rig)
            report["r2_r1_cut"] = round(cut, 3)
            for p in per.values():
                if p.get("NOE") is not None and p["NOE"] < 0.65:
                    p["flag"] = "fast_motion"
                elif p.get("R1") and p.get("R2"):
                    p["flag"] = "possible_exchange" if p["R2"] / p["R1"] > cut else "none"
    track = ["N"] * len(seq)
    for i, p in per.items():
        if 1 <= i <= len(seq):
            track[i - 1] = {"possible_exchange": "X", "none": "A", "fast_motion": "V"}.get(p.get("flag"), "M")
    report["track"] = "".join(track)
    report["residues"] = dict(sorted(per.items()))
    return report


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for arg in sys.argv[1:]:  # ENTRY or ENTRY=BMRB_ID when the input card has no BMRB id
        e, _, b = arg.partition("=")
        rep = readback(e, b or None)
        (OUT / f"{e}.json").write_text(json.dumps(rep, indent=1, ensure_ascii=False))
        print(json.dumps({"entry": e, "status": rep["status"], "lists": {k: (v["units_deposited"], v["n"], v["consistent"]) for k, v in rep["lists"].items()},
                          "numbering": rep.get("numbering"), "X": rep.get("track", "").count("X"), "V": rep.get("track", "").count("V")}))


if __name__ == "__main__":
    main()
