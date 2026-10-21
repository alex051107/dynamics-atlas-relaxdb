# Judgment drafting brief v1 (2026-10-20, rev. 14:50 CSV snapshot; fixed text, only the ENTRIES block changes per run)

You draft the judgment layer for RelaxDB proteins in the Dynamics Atlas project. Work in ~/dynamics_atlas_work/.
Plain English in JSON text fields.

Goal per protein: is it dynamic, where, on what timescale, under which sample conditions, with evidence for,
against and unclear; and is there an alternate APO state in the sense set by the scientist on 2026-09-17
(an APO state with slow motion, slow enough for separate NMR peaks). One judgment = protein x region x time window x
sample state. Build ONLY from the evidence rows listed; open cached sources to check any value you use. No new
papers, no web search.

Inputs:
- Contract schema/judgment_contract.json (v0.4). Format examples outputs/judgment_v0/VHR_CPMG.json and
  outputs/judgment_v0/5839.json (optional protein_summary.deposition_readback).
- Evidence rows: the CSV snapshot named in the ENTRIES block (a copy of outputs/pilot133/evidence_rows.csv taken after
  the last export; row IDs <PREFIX>-...; corrections already applied; follow the snapshot, not the live CSV).
- Second reads ledger/sr_dual/<case>_*.jsonl and _flags.json; adjudications ledger/batch3_adjudication_*.json.
- Sources: cases/<case>/prefetch/ and sources_cache/.
- Deposited-data readback outputs/deposition/<ENTRY>.json if present: lead only, never sets a verdict.
Do not read ~/dynamics_atlas_eval/, any RelaxDB label, outputs/tracks/, outputs/qc/.

Rules: detection window for every measured_not_detected; abstract-only rows give at most unresolved/not_measured;
ps-ns separate from us-ms; slower-than-ms only when the method gives a rate; mutants, homologs, other domains and
other constructs are inference or excluded; conditions (buffer, pH, temperature, ligand, metal) are part of the
claim; binding kinetics are not conformational dynamics; MD-only or structure-only -> that strength, window
undetermined; a global fit rate is not assigned to single residues unless the authors list them (residue_basis);
EPR line-shape or ENDOR is not DEER.

Output per entry: outputs/judgment_v0/<ENTRY>.json (judgment ids <PREFIX>-J1..). Run
`python3 tools/check_judgment.py <ENTRY>` until 0 errors. Do not edit checker, contract, evidence or CSV.
Then add one row per entry to outputs/alt_apo_states_batch3_v0.json (create or extend; same keys as
outputs/alt_apo_states_v0.json, including literal_two_peak = qualifies only if the source states slow exchange or
shows two peaks; does not if the source states fast or intermediate exchange; cannot tell otherwise; when the source prints
both kex and Δω, also compute kex/Δω at the field used and state the computed regime next to the authors' wording, E-033).
Report in under 200 words: per entry wt_apo_answer, judgments by verdict, alternate-APO call, evidence rows you think
are wrong (row id + reason).
