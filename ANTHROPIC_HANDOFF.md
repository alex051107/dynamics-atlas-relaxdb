# Draft Extraction & QC Handoff for Anthropic Batch 1

> **Status: DRAFT (awaiting expert sign-off on core prompt).** Gina owns the finalized scientific prompt. This page defines the expected return structure, single canonical rule source, Batch 1 open-protein input list, and deterministic QC checks we run on returned records before scaling toward the broader candidate list.

## 1. Scope for Batch 1

- **Input list:** [`data/batch1_open_proteins_draft.json`](data/batch1_open_proteins_draft.json) (`12` stratified open proteins not used for prompt tuning: `4` rate/population entries, `4` Rex-only entries, `4` qualitative-region entries). UniProt strings carried from RelaxDB are tagged `from_relaxdb_unverified_sequence` until sequence-checked.
- **Target content:** Capture both quantitative dynamics measurements and qualitative descriptions (dynamic regions, alternate states, cryptic or transient pockets, no-dynamics controls, suspected artefacts) with verbatim supporting quotes and exact document locators.
- **Scale gate:** Evaluate Batch 1 with deterministic QC and expert spot checks before scaling toward larger candidate sets.

## 2. Single Canonical Rule Source

Do not maintain a parallel copy of prompt rules here. Every extraction rule and proposed boundary default lives in one file generated from [`atlas_pipeline/schema.py`](atlas_pipeline/schema.py):

- **[`atlas_pipeline/ACTIVE_EXTRACTION_PROMPT.md`](atlas_pipeline/ACTIVE_EXTRACTION_PROMPT.md)** (currently marked `STATUS: PROPOSED 2026-11-26, default strict-abstain` until [`PROPOSED_RULES_20261126.md`](PROPOSED_RULES_20261126.md) is finalized).

## 3. Expected Return JSON Shape (per paper)

One paper often studies several constructs or homologs and spans both main text and Supplementary Information. UniProt identity therefore belongs on each sample, and `document_role` belongs on each measurement or observation record.

```json
{
  "entry": "17881",
  "doi": "10.xxxx/example",
  "title": "Paper title",
  "stance": "supports | no_dynamics_in_window | unclear | artefact_suspected",
  "samples": [
    {
      "sample_id": "S1",
      "uniprot_accession": "P62157 (or null when absent; never 'x')",
      "isoform_version": "P62157-1 (or null)",
      "construct_label": "WT full-length",
      "species_relation": "target | same_protein_other_construct | homolog | unknown",
      "same_as_deposit": "yes | no | unclear",
      "ligand_state": "apo",
      "temperature_raw": "25 C",
      "ph": "6.5",
      "buffer": "20 mM HEPES",
      "field_mhz_raw": "600 MHz",
      "quote": "verbatim sample description"
    }
  ],
  "measurements": [
    {
      "row_id": "M1",
      "sample_id": "S1",
      "document_role": "main_article | supplement_si",
      "quantity": "kex | pB | Rex | R1 | R2 | NOE | S2 | delta_omega | ...",
      "value_raw": "98",
      "unit_raw": "s^-1",
      "uncertainty_raw": "6",
      "residues_raw": "L169, N170",
      "method": "15N CEST",
      "source_role": "this_study | cited_prior_work | uncertain",
      "evidence_modality": "text | table | si_table | figure_vector | figure_raster | figure_caption",
      "measured_entity": "conformational_exchange | oligomer_or_association | other | unknown",
      "locator": "Results, p. 4",
      "quote": "verbatim text containing printed value"
    }
  ],
  "qualitative_observations": [
    {
      "obs_id": "Q1",
      "sample_id": "S1",
      "document_role": "main_article | supplement_si",
      "category": "dynamic_region | alternate_state | cryptic_pocket | no_dynamics_in_window | artefact_suspected",
      "evidence_level": "experimental | author_interpretation | simulation_or_prediction",
      "residues_raw": "L169, N170, G236",
      "pdb_ids": ["1BTL"],
      "summary": "Short factual summary of the reported behavior",
      "locator": "Results, NMR and Simulations",
      "quote": "verbatim supporting sentence (no numeric token required)"
    }
  ],
  "alternate_states": [
    {
      "pdb_id": "1BTL",
      "state_label": "ground state",
      "relation": "target | same_protein_other_construct | homolog | unknown",
      "ligand": "apo",
      "source_role": "this_study | cited_prior_work | uncertain",
      "quote": "verbatim PDB reference"
    }
  ]
}
```

## 4. Deterministic QC We Run on Returned Records

Every returned JSON passes through [`atlas_pipeline/`](atlas_pipeline/) before entering review cards or SQLite:

1. **Identity and text grounding.** Verify front-matter paper identity, exact substring quote spans in `main_article` or `supplement_si`, and signed numeric token containment for every quantitative row.
2. **Physical unit and entity rules.** Reject spectrometer frequencies (`MHz`) used as `NOE` or rate units, reject time units on `S2` or rates, reject contradictory deposit flags, and block oligomer/dimer fractions from conformational `pB`.
3. **Sample-condition attribution.** Score five attribution slots (construct, ligand/ion state, temperature, quantity role, and numeric value) and flag residue-numbering offsets before comparing across studies.
4. **Separate metric reporting.** Report candidate coverage, full-text availability, verbatim grounding rate, five-slot attribution accuracy, wall time, and expert review cost separately. Report recall only when an independent ground-truth denominator exists.
