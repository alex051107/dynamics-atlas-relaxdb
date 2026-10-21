# Quality

This page says how far to trust the atlas, with numbers.

## Pre-registered test on 20 proteins

Before we ran 20 RelaxDB-133 proteins, we wrote down seven checks and their limits. We did not change the limits after the results.

| Check | Limit | Result | Pass? |
|---|---|---|---|
| Proteins that reach a reviewed call | 18 of 20 | 20 of 20 | yes |
| Rows corrected after the double re-read | 15 per 100 rows | 18.9 per 100 rows | no |
| Planted errors that the re-read catches | 70% | 13 of 20 (65%) | no |
| Machine time per protein | median 45 minutes | median 24 minutes | yes |
| External NMR papers that the search finds | 70% | 11 of 15 (73%) | at the limit |
| Number or sample errors that the final review finds | 1 per protein | 0.55 per protein | yes |
| Proteins with a call other than unknown | report only | 6 of 20 | report only |

Two checks failed:

- **Corrections.** 110 of the 153 corrections are in one protein, thioredoxin. Most come from one error: E. coli thioredoxin has the entry's exact sequence, but the worker labelled it a homolog. The worker now receives the accessions with an identical sequence. A test re-read of two papers gave 30 rows and no homolog labels.
- **Planted errors.** The 7 missed errors were all marked "cannot verify" by both readers, so they never reached adjudication. Such rows now go to adjudication when the paper was read in full. On a new set of 20 planted errors, the re-read caught 20 of 20. It also flagged 1 of 38 rows that had no planted error.

Two limits on these numbers:

- The search result is partly circular. PDB citations are both a search channel and part of the reference list. Without the RelaxDB source papers as seeds, the search found 10 of 15.
- The first set of planted errors was used to find the fix. It can no longer serve as an independent test.

## Reviews of the overnight records

On 20 to 21 October we re-read 11 RelaxDB source papers in full and rewrote 12 records. Two independent reviews checked them. They found 0.33 and 0.83 verified errors per protein. Each error was fixed. One review reversed a call: for one SH3 domain (entry 7036) the authors report no exchange, so the call went back to unknown.

## Errors in the pipeline

[`error_log.json`](error_log.json) lists every error that we found, with the evidence, the fix and the status. The most important kinds:

| What went wrong | Fix |
|---|---|
| 5 RelaxDB cards had a wrong UniProt accession | Identity check before any search |
| The RelaxDB source paper was screened out because its abstract did not mention dynamics | Source papers are always read |
| E. coli thioredoxin was labelled a homolog of the entry | The worker receives accessions with an identical sequence |
| Rows that both readers could not verify never reached adjudication | Those rows now go to adjudication |
| A failed re-read could inherit the file of the previous reader | Each reader starts with no file and must read every row |
| The exchange regime came from the authors' adjectives | When kex and Δω are printed, we compute the regime |
| A T1/T2 subscript was lost in the PDF text, and one sentence was read reversed | Statements that depend on subscripts or tables are read from the page image |

## What the checks do not cover

- All readers and reviewers so far are language models. No expert has checked the records.
- A row can match its paper while the experiment itself is wrong. We record buffers, controls and author caveats, but we do not filter experiments yet.
- The readers share the same source text, so they can miss the same figure or supplementary table.
