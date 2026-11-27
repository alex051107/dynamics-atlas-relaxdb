"""Dynamics Atlas extraction pipeline.

Modules:
  schema   Pydantic v2 domain contract: samples, measurements, qualitative observations, figures, grounding.
  ingest   PMC JATS XML, Excel SI and PDF (main + SI) readers with a shared identity gate.
  figures  PyMuPDF figure inventory, 300 DPI crops, vector XY digitization and overlay checks.
  compare  5-tuple attribution scorer, cross-paper comparator and RelaxDB label recall benchmark.
  store    SQLite persistence for PaperRecord objects.
  cards    Five-question scientist cards (HTML + Markdown) built only from data.
  cli      `python -m atlas_pipeline.cli {ingest,figures,validate,compare,cards,e2e}`.

Held-out benchmark entries are refused by `schema.require_open_entry`.
"""

__version__ = "0.1.0"
