# Code

The scripts use only the Python standard library, plus numpy for the structure comparison. They expect a working folder at `~/dynamics_atlas_work` with the RelaxDB entry cards in `inputs/`. That folder is not in this repository because it holds cached papers and run folders.

| Folder | Contents |
|---|---|
| `tools/` | The pipeline steps (see `../methods/how_it_is_built.md`) and the table builders. Also the structure-state tool `pdb_states.py` and `ocr/vision_ocr.swift`, which reads scanned PDFs with macOS text recognition. |
| `prompts/` | The fixed instructions for the worker (`worker_v6_fill.md`, `worker_v6_screen.md`) and the judgment drafter (`judgment_draft_v1.md`). |
| `schema/` | The judgment contract and the worker result schema. |
| `config/` | Search configuration per entry, RelaxDB source-paper DOIs, identity overrides, and the residue ranges for the structure comparison (`pdb_states/`). |
| `tests/` | Unit tests with small fixtures. Run them with `python3 -m unittest discover -s tests` from this folder. In this repository 102 of the 123 tests pass. The 19 screening tests need the RelaxDB entry cards in `inputs/`, which are not included. One test needs the `edison_client` package, which is not installed. One test is skipped because the export script is not in this repository. |

Some file names contain the word "gina". They come from the first review package for our NMR collaborator. We kept the names so that the code runs unchanged.
