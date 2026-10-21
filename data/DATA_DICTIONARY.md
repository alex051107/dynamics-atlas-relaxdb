# Data dictionary

The files in this folder are generated from the working folders by `code/tools/export_public_repo.py`. Do not edit them by hand.

## `states.csv` and `states.json`

One record for each protein. 42 records in release 0.1.

| Column | Meaning |
|---|---|
| `entry` | RelaxDB entry name. `_CPMG` marks the 10 proteins with CPMG data. |
| `set` | `CPMG-10` or `RelaxDB-133`. |
| `protein` | Protein, organism and construct, as identified from the entry sequence. |
| `call` | `yes`, `possible`, `no_evidence` or `unknown`. See [`../methods/definitions.md`](../methods/definitions.md). |
| `literal_two_peak` | The strict two-peak reading (`qualifies`, `does not`, `cannot tell`) and its reason. |
| `reference_state` | The free-protein sample that the call is about, with its conditions. |
| `kex`, `pB`, `regime` | Exchange rate, minor-state population and exchange regime, as printed in the source, with the evidence row. |
| `residues` | Residues or regions with the exchange. |
| `structure_match` | Deposited structures that the papers relate to the states, and the relation. |
| `evidence_rows`, `judgments` | IDs of the rows and judgments that support the call. |
| `caveats` | Limits that change how to read the call. |

## `judgments.jsonl`

One judgment on each line. A judgment is one claim about one region, in one time window, in one sample state. It has a verdict, such as `dynamic_in_window`, `no_evidence_in_window` or `unresolved`. It also has the detection details (method, kex, pB, Δω, field, temperature) and the evidence rows it uses. The field rules are in [`../code/schema/judgment_contract.json`](../code/schema/judgment_contract.json).

## `evidence.csv`

One row for each paper, experiment and condition.

| Column | Meaning |
|---|---|
| `set` | `CPMG-10` or `RelaxDB-133`. |
| `ID` | Stable row ID. Judgments and protein pages use it. |
| `Review priority` | `A` rows carry the call, `B` rows support it, `C` rows are background. |
| `Paper`, `Link` | Title and DOI link. |
| `What we read` | `full_text`, `si` (supplementary information) or `abstract_only`. A row from an abstract cannot carry a call on its own. |
| `Organism / construct vs entry` | `target`, `same_protein_other_construct` or `homolog`, then the construct. |
| `Method`, `Experiment and conditions` | The experiment and its sample conditions. |
| `Residues / region`, `Dynamics observed`, `Timescale (as reported)`, `Population (as reported)` | What the paper reports, in its own terms. |
| `Location in paper`, `Values checked` | Where to find the sentence, and which values a script checked against the source. |
| `Expert check` columns | Empty. No expert has checked the rows yet. |

## `structures/<entry>.md`

One table for each CPMG protein. Each row is one chain of one deposited structure. It gives the class (apo, ligand-bound, complex), ligands, mutations and conditions. It also gives the Cα RMSD to two reference chains after core superposition. `closure` is 0 when the chain is like the first reference and 1 when it is like the second. The note at the top gives the reference chains, the residue ranges and their sources.

## `relaxdb_data_issues.md`

Problems that we found in RelaxDB entries: wrong UniProt accessions, units, error columns and temperatures. The RelaxDB authors have not confirmed them.
