"""Corpus-first recall check (no LLM): BMRB citations + UniProt citations + PubTator3 method queries vs our 10-protein table."""
import json, time, urllib.parse, urllib.request, glob
from pathlib import Path
W = Path.home() / "dynamics_atlas_work"; OUT = Path(__file__).parent
UA = {"User-Agent": "dynamics-atlas/1.0"}
def get(u, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60) as r: return json.loads(r.read().decode("utf-8","replace"))
        except Exception: time.sleep(2*(i+1))
    return None
P = {  # entry: (uniprot accessions, PubTator text name)
 "AQADK_CPMG": (["O66490"], '"adenylate kinase" AND Aquifex'),
 "BLAC_CPMG": (["P9WKD3"], 'BlaC AND tuberculosis'),
 "BLVRB_CPMG": (["P30043"], '"biliverdin reductase B" OR BLVRB'),
 "CYPA_CPMG": (["P62937"], '"cyclophilin A" OR CypA'),
 "VHR_CPMG": (["P51452"], 'VHR OR DUSP3'),
 "ARGKIN_CPMG": (["P51541"], '"arginine kinase"'),
 "RNASE_CPMG": (["P61824", "P61823"], '"ribonuclease A" OR "RNase A"'),
 "CHEY_CPMG": (["P0AE67"], 'CheY'),
 "HTPDZ_CPMG": (["O43464"], 'HtrA2'),
 "KRAS_CPMG": (["P01116"], 'KRAS OR K-Ras'),
}
METHODS = '(CPMG OR "relaxation dispersion" OR CEST OR "R1rho" OR "conformational exchange" OR "spin relaxation" OR "NMR dynamics")'
bmrb_map = {x["uniprot_id"]: x["bmrb_ids"] for x in get("https://api.bmrb.io/v2/mappings/uniprot/bmrb?format=json")}
bmrb_pmid = get("https://api.bmrb.io/v2/search/get_all_values_for_tag/_Citation.PubMed_ID")
def pmid2doi(pmids):
    out = {}
    pm = [p for p in pmids if p and p.isdigit()]
    for i in range(0, len(pm), 100):
        j = get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&pageSize=100&resultType=lite&query=" +
                urllib.parse.quote(" OR ".join(f"EXT_ID:{p}" for p in pm[i:i+100])))
        for r in (j or {}).get("resultList", {}).get("result", []):
            if r.get("doi"): out[r.get("pmid") or r.get("id")] = r["doi"].lower()
    return out
res = {}
for e, (accs, name) in P.items():
    ch = {"bmrb": set(), "uniprot": set(), "pubtator": set()}
    bm = [b for a in accs for b in bmrb_map.get(a, [])]
    pm_b = {p for b in bm for p in bmrb_pmid.get(b, []) if p and p != "."}
    pm_u = set()
    for a in accs:
        j = get(f"https://rest.uniprot.org/uniprotkb/{a}?fields=lit_pubmed_id&format=json") or {}
        for ref in j.get("references", []):
            for x in ref.get("citation", {}).get("citationCrossReferences", []):
                if x.get("database") == "PubMed": pm_u.add(x["id"])
    d = pmid2doi(pm_b | pm_u)
    ch["bmrb"] = {d[p] for p in pm_b if p in d}; ch["uniprot"] = {d[p] for p in pm_u if p in d}
    q = f"({name}) AND {METHODS}"; page = 1; n = None
    while True:
        j = get("https://www.ncbi.nlm.nih.gov/research/pubtator3-api/search/?text=" + urllib.parse.quote(q) + f"&page={page}")
        if not j: break
        n = j.get("count"); ch["pubtator"] |= {(r.get("doi") or "").lower() for r in j.get("results", []) if r.get("doi")}
        if page >= (j.get("total_pages") or 1) or page >= 30: break
        page += 1; time.sleep(0.4)
    pre = e.split("_")[0]
    cases = json.loads((W / "outputs/gina_review_round1/case_sources.json").read_text())
    main = W / "cases" / cases[e]
    ours_all = {json.loads(l).get("doi", "").lower() for l in open(main / "rows.jsonl")} - {""}
    sup = set()
    for s in glob.glob(str(W / f"cases/S_{pre}_*/rows.jsonl")):
        sup |= {json.loads(l).get("doi", "").lower() for l in open(s)} - {""}
    union = ch["bmrb"] | ch["uniprot"] | ch["pubtator"]
    res[e] = {"bmrb_entries": len(bm), "n_bmrb": len(ch["bmrb"]), "n_uniprot": len(ch["uniprot"]), "pubtator_count": n, "n_pubtator": len(ch["pubtator"]),
              "n_union": len(union), "ours_main": len(ours_all), "ours_main_found": len(ours_all & union),
              "supp": len(sup - ours_all), "supp_found": len((sup - ours_all) & union),
              "new_not_in_ours": len(union - ours_all - sup), "supp_missed": sorted((sup - ours_all) - union),
              "channels": {k: sorted(v) for k, v in ch.items()}}
    print(e, {k: v for k, v in res[e].items() if k not in ("channels", "supp_missed")}, flush=True)
(OUT / "recall_results.json").write_text(json.dumps(res, indent=1))
