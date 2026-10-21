#!/usr/bin/env python3
"""Mechanical search configuration for new entries (recall test v2): no hand-written search words.

  seeds         DOIs of the BMRB citations of the entry's own BMRB id (none for non-BMRB entries)
  aliases       UniProt recommended / alternative / short names and gene names, as word-bounded regexes
  epmc_name     one Europe PMC query per name group: protein names, then gene names
  search_terms  the recommended name and the primary gene name (citing-paper filter in candidates.py)

  auto_config.py ENTRY [ENTRY ...]   -> merged into config/pilot_seeds.json ("auto": true)
"""
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

WORK = Path.home() / "dynamics_atlas_work"
CFG = WORK / "config/pilot_seeds.json"
UA = {"User-Agent": "dynamics-atlas/1.0"}


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def uniprot_names(acc):
    u = get(f"https://rest.uniprot.org/uniprotkb/{acc}.json")
    d = u.get("proteinDescription", {})
    names = []
    for block in [d.get("recommendedName")] + d.get("alternativeNames", []) + [x.get("recommendedName") for x in d.get("contains", [])]:
        if block:
            names.append(block.get("fullName", {}).get("value"))
            names += [s.get("value") for s in block.get("shortNames", [])]
    genes = []
    for g in u.get("genes", []):
        genes += [g.get("geneName", {}).get("value")] + [s.get("value") for s in g.get("synonyms", [])]
    clean = lambda xs: list(dict.fromkeys(x for x in xs if x and len(x) >= 3))
    return clean(names), clean(genes)


def bmrb_seed_dois(bmrb):
    if not bmrb or not str(bmrb).isdigit():
        return []
    allp = get("https://api.bmrb.io/v2/search/get_all_values_for_tag/_Citation.PubMed_ID")
    pmids = [p for p in allp.get(str(bmrb), []) if p.isdigit()]
    dois = []
    for p in pmids:
        q = urllib.parse.urlencode({"query": f"EXT_ID:{p} AND SRC:MED", "format": "json"})
        res = get(f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?{q}")["resultList"]["result"]
        if res and res[0].get("doi"):
            dois.append(res[0]["doi"].lower())
    return dois


def rx(name):
    """Word-bounded, case-free regex; hyphens, spaces and letter-digit joins are interchangeable
    ("Calbindin-D9k" ~ "calbindin D9k", "APOBEC-2" ~ "APOBEC2")."""
    parts = re.findall(r"[a-z]+|[0-9]+|[^a-z0-9\s-]+", name.lower())
    return r"\b" + r"[-\s]?".join(re.escape(x) for x in parts) + r"\b"


def organism(acc):
    """Organisms of every Swiss-Prot entry with exactly this sequence (UniParc), the card's own first.
    v4: the RelaxDB card's accession is not always the organism the literature uses (TRX: P0AA29 Salmonella typhi
    is identical to E. coli TrxA P0AA25)."""
    own = get(f"https://rest.uniprot.org/uniprotkb/{acc}.json").get("organism", {}).get("scientificName", "")
    names = [own] if own else []
    try:
        upi = get(f"https://rest.uniprot.org/uniparc/search?query=uniprotkb:{acc}&format=json&size=1")["results"][0]["uniParcId"]
        refs = get(f"https://rest.uniprot.org/uniparc/{upi}/databases?format=json&size=200").get("results", [])
        for c in refs:
            o = (c.get("organism") or {}).get("scientificName", "")
            if c.get("database") == "UniProtKB/Swiss-Prot" and c.get("active") and o:
                o = re.sub(r"\s*\(.*\)$", "", o)
                if o not in names:
                    names.append(o)
    except (KeyError, IndexError, TypeError, ValueError):
        pass
    out = []
    for o in names[:6]:
        g = o.split()
        out += [o] + ([f"{g[0][0]}. {g[1]}"] if len(g) >= 2 else [])
    return list(dict.fromkeys(out))


GREEK = {"alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "kappa": "κ"}


def greek_variants(names):
    """'TGF-alpha' is written 'TGF-α' in many papers (v4)."""
    out = []
    for n in names:
        for w, g in GREEK.items():
            if re.search(rf"\b{w}\b", n, re.I):
                out.append(re.sub(rf"[-\s]?\b{w}\b", lambda m: ("-" if m.group(0).startswith("-") else " ") + g, n, flags=re.I))
    return [x for x in dict.fromkeys(out) if x not in names]


def build(entry):
    """v3 (2026-10-17): flexible aliases and a base-name + organism query, fixed after recall test v2 sample 1."""
    card = json.loads((WORK / "inputs" / f"{entry}.json").read_text())
    ov = WORK / "config/identity_overrides.json"  # human-set accession when the card's is wrong (E-028)
    if ov.exists() and entry in json.loads(ov.read_text()):
        card["uniprot"] = json.loads(ov.read_text())[entry]["uniprot"]
    names, genes = uniprot_names(card["uniprot"])
    # an all-caps acronym ending a long name is often the field's name for the protein ("... protein RANTES")
    names += [w for n in names if " " in n for w in [n.split()[-1]] if re.fullmatch(r"[A-Z][A-Z0-9-]{3,}", w) and w not in names]
    names += greek_variants(names)
    quote = lambda xs: "(" + " OR ".join(f'"{x}"' for x in xs) + ")"
    queries = [q for q in (quote(names[:12]) if names else "", quote(genes[:6]) if genes else "") if q]
    base = re.sub(r"\s+(?:[0-9]+|[A-Z])$", "", names[0]) if names else ""
    base = base if len(base.split()) == 1 else ""  # only one-word bases ("Thioredoxin"), never a family name
    org = organism(card["uniprot"])
    extra = []
    if base and base != names[0] and org:  # "Thioredoxin 1" is called "thioredoxin" in its organism's papers
        # v5: title-restricted, since a bare common name ("thioredoxin") returns ~21,000 hits, mostly fusion-tag papers
        queries.append(f'TITLE:"{base}" AND {quote(org)}')
        extra = [base]
    # v6: seed with the paper RelaxDB curated the data from (config/relaxdb_source_dois.json, provenance only, no labels);
    # 8 of 13 checked entries had missed it under v5
    src = json.loads((WORK / "config/relaxdb_source_dois.json").read_text()).get(entry, []) if (WORK / "config/relaxdb_source_dois.json").exists() else []
    seeds = list(dict.fromkeys(src + bmrb_seed_dois(card.get("bmrb_id"))))
    return {"auto": True, "auto_version": 6, "uniprot": card["uniprot"], "seeds": seeds,
            "aliases": [rx(x) for x in names + genes + extra], "epmc_name": queries,
            "search_terms": [x for x in (names[:1] + genes[:1])]}


def main():
    cfg = json.loads(CFG.read_text())
    for e in sys.argv[1:]:
        cfg[e] = build(e)
        print(json.dumps({e: {k: v for k, v in cfg[e].items() if k != "aliases"}}, ensure_ascii=False))
    CFG.write_text(json.dumps(cfg, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
