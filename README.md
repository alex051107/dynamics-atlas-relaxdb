# Dynamics Atlas

A database of protein conformational states that existing experiments already show, with the evidence for each state.

Release 0.1, 21 October 2026. Work in progress.

## What the atlas is for

Proteins move between shapes, and some of these shapes matter for function. Experiments, mainly NMR, have measured many such states. The results sit in the text and tables of papers. No database collects them as states.

The Dynamics Atlas collects them. Each record says which states a protein has, where they differ, how fast they exchange, how populated they are, and which deposited structure matches them. Each record points to the sentences in the papers that support it.

The atlas has two uses:

1. **A data source.** People who study a protein can see its known states and the evidence in one place.
2. **A benchmark.** Ensemble-generation models and molecular dynamics (MD) can be tested against states that experiments have measured.

An agent pipeline builds the atlas from the literature. The pipeline is a tool. The atlas is the product.

## Slice 1: alternate APO states

The atlas grows one kind of state at a time. Later slices can cover active and inactive enzymes, or open and closed loops. Each kind needs its own definition.

The first slice is **alternate APO states**: second shapes of a protein that binds nothing. We started here for two reasons:

- **It can be defined.** Our NMR collaborator's working definition: the second shape exchanges slowly enough for NMR to show two separate peaks.
- **It is useful.** The PDB leans towards bound (holo) structures, because bound proteins crystallize more easily. Drugs usually meet the free (APO) protein. Structure and co-folding models learn mostly from the PDB, so they do not see these states.

An example: free cyclophilin A (CypA). NMR measures a second shape at about 2%, near the active site. About three quarters of the CypA crystal structures (133 of 176) were measured at 120 K or below, and they show only the main shape. In our comparison, the second shape of the Phe113 side chain appears only in apo crystals measured at 240 K or above.

## What release 0.1 contains

42 RelaxDB proteins: the 10 with CPMG data, and 32 of the 133 others.

| Call | Proteins | Meaning |
|---|---|---|
| yes | 13 | A minor state with a measured population and rate, or a second peak set, in the free protein |
| possible | 18 | Exchange is detected in the free protein, but no population is measured |
| unknown | 11 | Not measured, or the key paper is not readable in full |

Three results stand out:

- **The definition changes the answer.** Under the strict two-peak reading, only 4 of the 42 qualify, and each of the 4 has a caveat. Our collaborator will decide which reading the atlas uses.
- **Deposited structures rarely show the second state.** In none of the 10 CPMG proteins does a ligand-free crystal have the other state's backbone. CypA is the one clear match, in side chains.
- **Full text matters.** On 20 to 21 October we read 11 of the papers that RelaxDB took its data from. The number of unknown proteins fell from 19 to 11.

[Browse the atlas](atlas/README.md): one page for each protein.

## How to use it

1. **Read a protein.** Open [`atlas/README.md`](atlas/README.md) and follow the link to the protein page.
2. **Use the data.** The tables are in [`data/`](data/). [`data/DATA_DICTIONARY.md`](data/DATA_DICTIONARY.md) defines every column.
3. **Check a claim.** Each protein page lists evidence row IDs. Find the row in [`data/evidence.csv`](data/evidence.csv). It gives the DOI, the location in the paper and a quote.

## How far to trust it

Every call goes through two independent re-reads, adjudication against the paper and an independent review. All readers and reviewers so far are language models. No expert has checked the records yet.

A record that passes our checks matches the cited paper. It does not prove that the experiment in the paper is correct. [`methods/quality.md`](methods/quality.md) gives the test results and the errors that we found.

## What is in this repository

| Folder | Contents |
|---|---|
| [`atlas/`](atlas/) | One readable page for each protein |
| [`data/`](data/) | Machine-readable tables: states, judgments, evidence rows, structure comparisons |
| [`methods/`](methods/) | Definitions, how the atlas is built, quality checks, error log |
| [`code/`](code/) | The pipeline that builds the atlas |
| [`CHANGELOG.md`](CHANGELOG.md) | What changed in each release |

The repository does not contain the full texts or abstracts of papers, because they are copyrighted. It also does not contain test keys, run folders or messages to collaborators.

## Next steps

1. Our NMR collaborator decides the definition of an alternate APO state.
2. We compare measured minor-state chemical shifts with shifts predicted from candidate structures.
3. We complete the 133 RelaxDB proteins, then start the second kind of state.
