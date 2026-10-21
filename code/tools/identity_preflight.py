#!/usr/bin/env python3
"""Check that a RelaxDB card's UniProt accession is the protein in its sequence, before any search (E-028).

Search config is built from the card's UniProt names, so a wrong accession sends the whole literature line to the
wrong protein (17306, 18092 in batch 3). Overlap = share of the card's 10-mers found in the accession's sequence.

  match     >= 0.8   (tags and point mutations allowed)
  partial   0.3-0.8  (search runs, flagged for review)
  mismatch  < 0.3    (batch_run.py stops this entry until a person sets the identity)

  identity_preflight.py ENTRY [ENTRY ...]   -> ledger/identity_preflight.json (appends / overwrites per entry)
"""
import json
import sys
import time
import urllib.request
from pathlib import Path

WORK = Path.home() / "dynamics_atlas_work"
OUT = WORK / "ledger/identity_preflight.json"
K = 10


def uniprot_seq(acc):
    req = urllib.request.Request(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", headers={"User-Agent": "dynamics-atlas/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return "".join(r.read().decode().splitlines()[1:])


def check(entry):
    card = json.loads((WORK / "inputs" / f"{entry}.json").read_text())
    seq, acc = card.get("sequence", ""), card.get("uniprot", "")
    if not acc or len(seq) < K:
        return {"status": "mismatch", "overlap": None, "uniprot": acc, "note": "no accession or sequence on the card"}
    ref = uniprot_seq(acc)
    kmers = [seq[i:i + K] for i in range(len(seq) - K + 1)]
    ov = sum(k in ref for k in kmers) / len(kmers)
    status = "match" if ov >= 0.8 else ("partial" if ov >= 0.3 else "mismatch")
    return {"status": status, "overlap": round(ov, 2), "uniprot": acc, "card_len": len(seq), "uniprot_len": len(ref)}


def main():
    res = json.loads(OUT.read_text()) if OUT.exists() else {}
    for e in sys.argv[1:]:
        res[e] = {**check(e), "at": time.strftime("%F %T")}
        print(json.dumps({e: res[e]}), flush=True)
    OUT.write_text(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
