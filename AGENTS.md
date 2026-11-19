# Repository Agent Instructions (`dynamics-atlas-relaxdb`)

Every contributor (human or agent) editing documentation, atlas pages, or workbooks on a review branch must run `python3 methods/check_review_consistency.py` before committing. Keep Release `0.1` files (`atlas/proteins/`, `data/*.csv`, `data/structures/`, `code/`) untouched unless explicitly updating Release `0.1`.

## Rule-to-Enforcer Table

| Rule | What enforces it | Why it exists |
|---|---|---|
| Keep `12` held-out entries physically excluded from all open atlas pages and workbooks | `methods/check_review_consistency.py` (checks `atlas/all_proteins/`) + `methods/statechart/WorkflowV3.tla` (`NoSealedEntryRead`) | Prevents benchmark contamination |
| Keep cross-document totals synced to the single source of truth (`proteins_summary.csv`, `RelaxDB_dynamics_from_papers_DRAFT_20261118.xlsx`, `atlas/all_proteins/`) | `methods/check_review_consistency.py` (blocks stale superseded counts like `19,958`, `771 / 771`, `23 unread`, `104 / 131`) | Eliminates contradictory numbers across `README.md`, `REVIEW_GUIDE.md`, and `methods/*.md` |
| Keep every prose sentence short, direct, and logically explicit (`<= 48` words, no em-dashes, no defensive filler) | `methods/check_review_consistency.py` (`check_prose_clarity`) | Stops wall-of-text paragraphs that hide scientific decisions |
| Anchor every core review, architecture, and status page with a valid inline Mermaid statechart or flowchart | `methods/check_review_consistency.py` (`DOCS_REQUIRING_MERMAID` + `check_mermaid_blocks`) | Ensures logic, state transitions, and decision forks are readable visually at a glance |
| Keep all internal Markdown links valid, zero host home/temp/eval path leaks, and clean sequential headings in generated protein pages | `methods/check_review_consistency.py` | Catches broken reader paths and generator formatting bugs before push |
| Keep Release `0.1` (`main`) and frozen extraction assets untouched during review iterations | Git branch isolation (`review/*` only) + external SHA-256 hash verification | Preserves published Release `0.1` reproducibility |
