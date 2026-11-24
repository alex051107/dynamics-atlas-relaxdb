# Dynamics Atlas | Portfolio case study

An evidence-traceable atlas of experimentally reported protein conformations. The project turns dispersed findings into records a reader can inspect, qualify, and trace back to their sources. The atlas is the product; the literature-processing pipeline builds it.

[Public repository](https://github.com/alex051107/dynamics-atlas-relaxdb) · [Architecture and evidence states](docs/portfolio/architecture.md) · [Public quality report](https://github.com/alex051107/dynamics-atlas-relaxdb/blob/main/methods/quality.md)

![Conceptual illustration of alternate conformations and evidence records](docs/portfolio/concept.jpg)

*ImageGen concept illustration. No experimental structures are depicted.*

## What shipped

| Public snapshot | Scope |
| --- | --- |
| **0.0 · October 20, 2026** | First public repository snapshot: 42 protein-level calls, evidence and judgment tables, structure comparisons for seven proteins, and pipeline code. |
| **0.1 · October 21, 2026** | First atlas-format snapshot: per-protein pages and machine-readable tables for 42 proteins in the unbound-state slice, with structure comparisons for all ten CPMG proteins. |

These are dated milestones in the [project changelog](https://github.com/alex051107/dynamics-atlas-relaxdb/blob/main/CHANGELOG.md), not GitHub Release objects or a claim of current dataset size. This case study describes the publicly documented 0.1 snapshot.

## The design choice

A searchable bibliography tells readers where to look. An atlas entry tells them what the available evidence supports, what remains unresolved, and where to inspect the basis for the call. Evidence references, structured judgments and readable entries work together: the same claim can be browsed by a scientist or checked programmatically.

- **Keep the call separate from its support.** The workflow checks identity, records what a source supports, routes disagreements for adjudication, and then publishes a qualified call.
- **Make abstention visible.** An unknown call is not a negative result. Missing measurements or material the pipeline cannot read do not count as evidence of absence.
- **Report failures as well as improvements.** In the public 20-protein engineering test, the initial seeded-error check caught **13 of 20**, below its target. The report documents the blind spot and the follow-up test. It also explains why the original set was no longer an independent test after it informed the fix.

## What the checks establish

The public 0.1 workflow used language models for source re-reads, adjudication and review. These checks help assess whether a record is faithful to its cited source. They do not independently confirm the experiment, the biological interpretation, or model benchmark performance. The repository reported no expert review of those records at that snapshot.

This is a project-level account. The public repository establishes the artifact and documented methods; it does not by itself establish individual ownership of components. The overlay includes no paper passages or underlying measurement data.
