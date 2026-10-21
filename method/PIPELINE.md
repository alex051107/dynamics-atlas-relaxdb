# How a RelaxDB entry becomes a reviewed call

Each step writes files. The next step reads only those files, so every result can be traced back to a paper. The code for each step is in `code/tools/`.

## Roles

| Role | Who | Does |
|---|---|---|
| Worker | OpenAI Codex (one run at a time) | Screens papers, reads them and fills evidence rows. Re-reads rows. |
| Second reader | Claude | Re-reads every row against the paper, independently of Codex. |
| Adjudicator, drafter, reviewer | Claude subagents | Decide flagged rows, draft judgments, review them against the sources. |
| Deterministic checks | Python scripts | Check that every number and quote is in the cited source, check the judgment schema, keep row IDs stable. |
| Person | The project lead and the NMR collaborator | Decide the definition, check examples, approve every change of a scientific claim. |

The workers never see RelaxDB labels or the test keys.

## Steps

1. **Identity check** (`identity_preflight.py`). The card's UniProt accession must match the card's sequence. A mismatch stops the entry until a person sets the accession. Five of the 133 cards had a wrong accession.
2. **Search** (`auto_config.py`, `candidates.py`, `extra_channels.py`). Names come from UniProt, including all organisms with the identical sequence. Channels: the citation graph of seed papers, BMRB entries of the same protein, PDB primary citations, and Europe PMC name-and-method queries. The paper that RelaxDB took its data from is a seed.
3. **Screen** (`screen_candidates.py`). Each candidate gets a tier from its title and abstract: A (direct dynamics evidence), B (supporting), C (background) or X (not relevant). The RelaxDB source paper is always tier A.
4. **Read and fill** (`campaign.py fill`). The worker reads each A and B paper in full where it can and writes one row for each paper, experiment and condition. Each row has a quote of at least eight words, its location and the sample conditions. A scorer checks that every number and quote is in the source text.
5. **Double re-read** (`dual_read.py`, `second_read.py`). Codex and Claude each re-read every row against the source. A row goes to adjudication when a reader calls it wrong, or when both readers cannot verify it on a full-text paper.
6. **Adjudicate**. A reviewer opens the source and confirms or corrects each flagged row. Corrections go into one ledger with the source quote. Claude spot-checks the corrections before they are applied.
7. **Draft judgments** (`prompts/judgment_draft_v1.md`, `check_judgment.py`). One judgment is one region, one time window and one sample state. Abstract-only rows give at most `unresolved`. Exchange in a mutant or another construct is not exchange in the reference state.
8. **Independent review**. A separate model opens every number and residue list in the sources and counts verified errors.
9. **Alternate-APO call**. One row for each protein, from the judgments for the reference state.

## What the checks do not cover

- A row can match its paper and the experiment can still be wrong. We record buffers, controls and author caveats, but we do not filter experiments yet.
- All readers are language models. They share the same source text, so they can miss the same figure or supplementary table.
- The search recall test uses PDB and UniProt reference lists, which partly overlap with the PDB search channel.
