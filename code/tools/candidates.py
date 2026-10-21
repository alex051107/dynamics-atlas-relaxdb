#!/usr/bin/env python3
"""Recall-first candidate paper lists via the citation graph (OpenAlex).

Seeds = RelaxDB source paper + known leads. Candidates = seeds + their references + papers citing them,
kept only when title/abstract names the protein AND mentions a dynamics/structure method. Deterministic.

  candidates.py ENTRY [ENTRY ...]      -> outputs/candidates/<ENTRY>.json and a combined CSV
"""
import csv
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

WORK = Path.home() / "dynamics_atlas_work"
OUT = WORK / "outputs/candidates"
UA = {"User-Agent": "dynamics-atlas/1.0 (mailto:noreply@example.org)"}

SEEDS = {
    "AQADK_CPMG": ["10.1038/nature06410", "10.1038/nature06407", "10.1038/nsmb821", "10.1038/ncomms10848", "10.1038/nsmb.2941"],
    "BLAC_CPMG": ["10.1128/AAC.02025-19"],
    "BLVRB_CPMG": ["10.1016/j.jmb.2018.06.015", "10.3389/fmolb.2023.1244587", "10.3389/fmolb.2021.691208"],
    "CYPA_CPMG": ["10.1038/nature04105", "10.1038/nature08615"],
    "VHR_CPMG": ["10.1021/acs.biochem.0c00245"],
    "ARGKIN_CPMG": ["10.1021/bi101664u"],
    "RNASE_CPMG": ["10.1021/ja0514949", "10.1021/bi400973e", "10.1021/acs.jpcb.5b00212"],
    "CHEY_CPMG": ["10.1016/j.str.2012.05.008"],
    "HTPDZ_CPMG": ["10.1038/s41467-024-48997-5"],
    "KRAS_CPMG": ["10.1038/s41594-023-01070-z"],
}
ALIASES = {
    "AQADK_CPMG": [r"adenylate kinase", r"\badk\b", r"\badk[ae]?\b"],
    "BLAC_CPMG": [r"\bblac\b", r"beta-lactamase", r"β-lactamase"],
    "BLVRB_CPMG": [r"\bblvrb\b", r"biliverdin reductase", r"flavin reductase"],
    "CYPA_CPMG": [r"cyclophilin", r"\bcypa\b", r"\bppia\b"],
    "VHR_CPMG": [r"\bvhr\b", r"\bdusp3\b", r"vaccinia h1"],
    "ARGKIN_CPMG": [r"arginine kinase"],
    "RNASE_CPMG": [r"ribonuclease a\b", r"\brnase a\b"],
    "CHEY_CPMG": [r"\bchey\b"],
    "HTPDZ_CPMG": [r"\bhtra2\b", r"omi/htra2", r"\bomi\b"],
    "KRAS_CPMG": [r"\bk-?ras\b", r"\bras\b"],
}
SEARCH_TERMS = {
    "AQADK_CPMG": ["adenylate kinase"], "BLAC_CPMG": ["BlaC", "beta-lactamase tuberculosis"],
    "BLVRB_CPMG": ["biliverdin reductase", "BLVRB"], "CYPA_CPMG": ["cyclophilin"], "VHR_CPMG": ["VHR", "DUSP3"],
    "ARGKIN_CPMG": ["arginine kinase"], "RNASE_CPMG": ["ribonuclease A", "RNase A"], "CHEY_CPMG": ["CheY"],
    "HTPDZ_CPMG": ["HtrA2"], "KRAS_CPMG": ["KRAS", "K-Ras"],
}
_PILOT = WORK / "config/pilot_seeds.json"  # extra entries (RelaxDB-133 pilot): seeds = BMRB citation paper only
if _PILOT.exists():
    for _e, _c in json.loads(_PILOT.read_text()).items():
        if not _e.startswith("_"):
            SEEDS[_e], ALIASES[_e], SEARCH_TERMS[_e] = _c["seeds"], _c["aliases"], _c["search_terms"]
DYN = re.compile(r"dynamic|relaxation|dispersion|cpmg|cest|exchange|conformation|nmr|crystal structure|room.temperature|"
                 r"fret|deer|\bepr\b|hydrogen.deuterium|hdx|molecular dynamics|simulation|allosteric|flexib|ensemble|transition", re.I)


FAILED = []


def get(url):
    for i in range(7):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except Exception:
            time.sleep(2 * (i + 1))
    FAILED.append(url)
    return None


def abstract(w):
    inv = w.get("abstract_inverted_index") or {}
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))


def slim(w, channel):
    return {"openalex": w.get("id", "").split("/")[-1], "doi": (w.get("doi") or "").replace("https://doi.org/", "").lower(),
            "title": w.get("title") or "", "year": w.get("publication_year"), "abstract": abstract(w)[:2000],
            "oa": bool((w.get("open_access") or {}).get("is_oa")), "oa_url": (w.get("open_access") or {}).get("oa_url"),
            "cited_by_count": w.get("cited_by_count", 0), "channel": channel}


SELECT = "id,doi,title,publication_year,abstract_inverted_index,open_access,cited_by_count,referenced_works"


def build(entry):
    pool = {}
    FAILED.clear()
    truncated = []
    for doi in SEEDS[entry]:
        w = get(f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi)}?select={SELECT}")
        if not w:
            pool.setdefault("doi:" + doi, {"openalex": "", "doi": doi.lower(), "title": "(seed; metadata lookup failed)", "year": None,
                                           "abstract": "", "oa": False, "oa_url": None, "cited_by_count": 0, "channel": "seed"})
            continue
        pool[w["id"]] = slim(w, "seed")  # a seed overrides an earlier reference/citing entry
        refs = [r.split("/")[-1] for r in (w.get("referenced_works") or [])]
        for i in range(0, len(refs), 50):
            j = get("https://api.openalex.org/works?per-page=50&select=" + SELECT + "&filter=openalex:" + "|".join(refs[i:i + 50]))
            for x in (j or {}).get("results", []):
                pool.setdefault(x["id"], slim(x, "reference"))
        wid = w["id"].split("/")[-1]
        for term in SEARCH_TERMS[entry]:
            cursor = "*"
            flt = f"cites:{wid},title_and_abstract.search:{urllib.parse.quote(term)}"
            for _ in range(10):
                j = get(f"https://api.openalex.org/works?per-page=200&select={SELECT}&filter={flt}&cursor={cursor}")
                if not j:
                    break
                for x in j.get("results", []):
                    pool.setdefault(x["id"], slim(x, "citing"))
                cursor = (j.get("meta") or {}).get("next_cursor")
                if not cursor or not j.get("results"):
                    break
            else:
                truncated.append(f"{wid}:{term}")
        cursor = "*"
        for _ in range(10):  # citing papers without abstracts: protein name may be absent, keep by title method terms below
            j = get(f"https://api.openalex.org/works?per-page=200&select={SELECT}&filter=cites:{wid},has_abstract:false&cursor={cursor}")
            if not j:
                break
            for x in j.get("results", []):
                if x["id"] not in pool:
                    pool[x["id"]] = slim(x, "citing_no_abstract")
            cursor = (j.get("meta") or {}).get("next_cursor")
            if not cursor or not j.get("results"):
                break
        else:
            truncated.append(f"{wid}:no_abstract")
        time.sleep(0.3)
    names = [re.compile(a, re.I) for a in ALIASES[entry]]
    keep = []
    for c in pool.values():
        text = c["title"] + " " + c["abstract"]
        in_title = any(n.search(c["title"]) for n in names)
        named = in_title or any(n.search(c["abstract"]) for n in names)
        no_abs_keep = (not c["abstract"]) and c["channel"].startswith("citing") and bool(DYN.search(c["title"]))
        if c["channel"] == "seed" or (named and DYN.search(text)) or no_abs_keep:
            c["score"] = (3 if c["channel"] == "seed" else 0) + (2 if in_title else (0 if no_abs_keep and not named else 1)) + (1 if DYN.search(c["title"]) else 0) + \
                min(2, (c["cited_by_count"] or 0) / 100)
            keep.append(c)
    keep.sort(key=lambda c: -c["score"])
    OUT.mkdir(parents=True, exist_ok=True)
    status = "complete" if not FAILED and not truncated else "incomplete"
    (OUT / f"{entry}.json").write_text(json.dumps({"entry": entry, "pool": len(pool), "kept": len(keep), "search_status": status,
                                                   "failed_requests": FAILED[:50], "truncated": truncated, "candidates": keep}, indent=1, ensure_ascii=False))
    print(json.dumps({"entry": entry, "pool": len(pool), "kept": len(keep), "oa": sum(c["oa"] for c in keep), "status": status,
                      "failed": len(FAILED), "truncated": len(truncated)}), flush=True)
    return keep


def main():
    entries = sys.argv[1:] or list(SEEDS)
    rows = []
    for e in entries:
        for c in build(e):
            rows.append([e, c["doi"], c["title"], c["year"], c["channel"], "yes" if c["oa"] else "no", round(c["score"], 2)])
    with open(OUT / "candidates_all.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["entry", "doi", "title", "year", "channel", "open_access", "score"])
        w.writerows(rows)


if __name__ == "__main__":
    main()
