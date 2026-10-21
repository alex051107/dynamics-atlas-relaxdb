#!/usr/bin/env python3
"""Add two deterministic recall channels to an entry's candidate list (no LLM).

  bmrb_same_protein : citations of every BMRB entry mapped to the same UniProt accession
  epmc_method_query : Europe PMC  <name query> AND <method words>, top 400 per query by relevance
  pdb_primary_citation : primary citation of each PDB entry listed for the protein (no name filter)

Name queries come from config/pilot_seeds.json ("epmc_name"). Existing candidates keep their channel;
new ones are appended with the same name+method filter as candidates.py.

  extra_channels.py ENTRY [ENTRY ...]   -> updates outputs/candidates/<ENTRY>.json in place (adds "channels_added")
"""
import json
import re
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import candidates as C  # noqa: E402

CFG = json.loads((C.WORK / "config/pilot_seeds.json").read_text())
# v2 (2026-10-15): v1 lacked plain "NMR" / "relaxation" / "dipolar coupling" and missed Volkman 2001 and GB3 RDC papers.
METHODS = ('(NMR OR "nuclear magnetic resonance" OR relaxation OR dispersion OR CEST OR "dipolar coupling" OR '
           '"dipolar couplings" OR "order parameter" OR "model-free" OR "hydrogen exchange" OR "molecular dynamics" OR '
           '"conformational exchange" OR microsecond OR millisecond OR "conformational dynamics")')
LIMIT = 400
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"


def epmc(query, limit=LIMIT):
    out, cursor = [], "*"
    while len(out) < limit:
        j = C.get(EPMC + "?" + urllib.parse.urlencode({"query": query, "format": "json", "pageSize": 100,
                                                       "resultType": "core", "cursorMark": cursor}))
        if not j:
            break
        res = (j.get("resultList") or {}).get("result", [])
        out += res
        nxt = j.get("nextCursorMark")
        if not res or not nxt or nxt == cursor:
            break
        cursor = nxt
    return out[:limit]


def from_epmc(r, channel):
    return {"openalex": "", "doi": (r.get("doi") or "").lower(), "pmid": r.get("pmid"), "title": r.get("title") or "",
            "year": int(r["pubYear"]) if str(r.get("pubYear", "")).isdigit() else None,
            "abstract": re.sub(r"<[^>]+>", "", r.get("abstractText") or "")[:2000],
            "oa": r.get("isOpenAccess") == "Y", "oa_url": None, "cited_by_count": r.get("citedByCount", 0), "channel": channel}


def bmrb_pmids(uniprot):
    maps = C.get("https://api.bmrb.io/v2/mappings/uniprot/bmrb?format=json") or []
    ids = next((x["bmrb_ids"] for x in maps if x.get("uniprot_id") == uniprot), [])
    allp = C.get("https://api.bmrb.io/v2/search/get_all_values_for_tag/_Citation.PubMed_ID") or {}
    return sorted({p for i in ids for p in allp.get(str(i), []) if p and p.isdigit()}), ids


def run(entry):
    path = C.OUT / f"{entry}.json"
    data = json.loads(path.read_text())
    card = json.loads((C.WORK / "inputs" / f"{entry}.json").read_text())
    have = {c["doi"] for c in data["candidates"] if c.get("doi")}
    names = [re.compile(a, re.I) for a in C.ALIASES[entry]]
    added, report = [], {}
    pmids, bmrb_ids = bmrb_pmids(card.get("uniprot", ""))
    new = []
    for i in range(0, len(pmids), 50):
        new += epmc(" OR ".join(f"EXT_ID:{p}" for p in pmids[i:i + 50]) + " AND SRC:MED", 100)
    report["bmrb_same_protein"] = {"bmrb_entries": len(bmrb_ids), "pmids": len(pmids), "records": len(new)}
    for r in new:  # same-protein BMRB data papers: keep without the name filter
        c = from_epmc(r, "bmrb_same_protein")
        if c["doi"] and c["doi"] not in have:
            have.add(c["doi"]); added.append(c)
    pdbs = sorted({c.split(":")[0].strip() for c in (card.get("pdb_chains_all") or "").split(",") if c.strip()})
    prim = set()
    for pid in pdbs[:80]:  # primary citation of every deposited structure of this protein (v3, 2026-10-17)
        cit = (C.get(f"https://data.rcsb.org/rest/v1/core/entry/{pid}") or {}).get("rcsb_primary_citation") or {}
        doi = (cit.get("pdbx_database_id_DOI") or "").lower()
        if doi:
            prim.add(doi)
    recs = [r for d in sorted(prim) for r in epmc(f'DOI:"{d}"', 1)]
    report["pdb_primary_citation"] = {"pdb_entries": len(pdbs), "dois": len(prim), "records": len(recs)}
    for r in recs:
        c = from_epmc(r, "pdb_primary_citation")
        if c["doi"] and c["doi"] not in have:
            have.add(c["doi"]); added.append(c)
    queries = CFG[entry]["epmc_name"]
    queries = [queries] if isinstance(queries, str) else queries  # several narrow name queries beat one broad one
    hits = [r for q in queries for r in epmc(f"{q} AND {METHODS}")]
    report["epmc_method_query"] = {"queries": queries, "records": len(hits)}
    for r in hits:
        c = from_epmc(r, "epmc_method_query")
        text = c["title"] + " " + c["abstract"]
        if c["doi"] and c["doi"] not in have and any(n.search(text) for n in names) and C.DYN.search(text):
            have.add(c["doi"]); added.append(c)
    for c in added:
        c["score"] = (2 if any(n.search(c["title"]) for n in names) else 1) + (1 if C.DYN.search(c["title"]) else 0) + \
            min(2, (c["cited_by_count"] or 0) / 100)
    data["candidates"] += sorted(added, key=lambda c: -c["score"])
    data["kept"] = len(data["candidates"])
    data["channels_added"] = report | {"added": len(added)}
    if C.FAILED:
        data["search_status"] = "incomplete"; data["failed_requests"] = (data.get("failed_requests") or []) + C.FAILED[:50]
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False))
    print(json.dumps({"entry": entry, "added": len(added), "kept": data["kept"], **report}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    for e in sys.argv[1:]:
        C.FAILED.clear()
        run(e)
