# RelaxDB data issues found while building the atlas (for the NMR collaborator; running list)

Each item: what we saw, where, how sure. None of these has been confirmed by the RelaxDB authors.

1. VCPTH: card sequence is Vibrio cholerae Pth (PDB 2MJL) but card UniProt P0A7D1 is E. coli Pth. Seen by the fill
   worker and confirmed in the judgment layer (2026-10-17).
2. 27011 (SigA): in all three deposited R2 lists (600/850/950 MHz) the error is larger than the value for most rows;
   labels built from them may be unreliable (BMRB 27011 readback, 2026-10-17).
3. 17701 (YkuD): deposited R1/R2 times are labelled seconds but look like milliseconds (median R1 0.0012 s-1 after
   conversion); ratios are unaffected (BMRB 17701 readback).
4. 5839 (GB3) V39: the source paper reports exchange at V39 at five fields; under the RelaxDB R1/R2/NOE rule V39 has
   dR2/R1 = 0.2080 against a threshold of 0.2088 (0.4% below), so it is labelled no exchange. Not an error; a
   threshold-edge case worth a note (our re-implementation of the rule, kappa 0.859 vs published labels).
5. 19335 (CCL5): BMRB 19335 and RelaxDB list 273 K, while the paper's 37 °C core averages match the deposited
   values exactly; the temperature field is probably wrong (judgment drafter, 2026-10-20; not yet checked by Claude
   against the paper text).
6. TRX: card UniProt P0AA29 is Salmonella typhi thioredoxin; the sequence is identical to E. coli TrxA (P0AA25),
   which is what the literature studies. Not an error, but a search on the card's organism misses the literature.
7. CD9K: the entry sequence carries P43G (card ...LLKGGSTLDE... vs UniProt P02633 ...LLKGPSTLDE..., checked by Claude
   2026-10-20), so the entry is the P43G mutant, not wild-type calbindin D9k; the card name does not say so.
8. Zenodo 20834076 README: KRAS is called "G12D", but the raw files contain G012N (WT) and the Dryad source is
   Hansen 2023 WT GTP; BLAC is called "TEM-1", but the entry is M. tuberculosis BlaC.
9. Card UniProt accessions that do not match the card sequence (10-mer overlap with the named accession):
   17306 0.00 (N1S0H6 is a fungal fragment, entry is a designed ankyrin), 18092 0.00 (P03355 is MoMLV Gag-Pol, the
   evidence is human eRF1 N-domain, P62495), 50410 0.00, VCPTH 0.05 (see item 1), BINASE 0.15; 50734 0.62 and 15255
   0.75 to check. Another 28 cards differ from their accession only by tags or point mutations (overlap >= 0.8).
   Source: ledger/card_identity_check_133.json (Claude, 2026-10-20).
