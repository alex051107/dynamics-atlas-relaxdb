"""SQLite persistence for validated PaperRecords, their grounding checks, figures and comparison outcomes.

The database is built in a temporary file next to the target, checked with PRAGMA integrity_check and row counts,
and only then moved into place with os.replace, so a failed build never leaves a half-written database behind.
"""
from __future__ import annotations

import json
import os
import sqlite3
import tempfile
from pathlib import Path
from typing import Any, Iterable

from .schema import ComparisonOutcome, PaperRecord

DDL = """
CREATE TABLE papers (entry TEXT, doi TEXT, title TEXT, stance TEXT, notes TEXT, n_samples INTEGER, n_measurements INTEGER,
                     n_primary_measurements INTEGER, n_qualitative INTEGER, PRIMARY KEY (entry, doi));
CREATE TABLE samples (entry TEXT, doi TEXT, sample_id TEXT, uniprot_accession TEXT, isoform_version TEXT, construct_label TEXT,
                      species_relation TEXT, same_as_deposit TEXT, ligand_state TEXT, temperature_raw TEXT, temperature_k REAL,
                      ph TEXT, buffer TEXT, field_mhz_raw TEXT, PRIMARY KEY (entry, doi, sample_id));
CREATE TABLE measurements (entry TEXT, doi TEXT, row_id TEXT, sample_id TEXT, quantity TEXT, quantity_canonical TEXT, value_raw TEXT,
                           value_num REAL, unit_raw TEXT, unit_canonical TEXT, residues_raw TEXT, source_role TEXT,
                           evidence_modality TEXT, document_role TEXT, locator TEXT, quote TEXT, char_start INTEGER,
                           char_end INTEGER, grounding_ok INTEGER, grounding_reasons TEXT, figure_link_status TEXT,
                           figure_id TEXT, PRIMARY KEY (entry, doi, row_id));
CREATE TABLE qualitative_observations (entry TEXT, doi TEXT, obs_id TEXT, sample_id TEXT, document_role TEXT, category TEXT,
                                       evidence_level TEXT, residues_raw TEXT, pdb_ids TEXT, summary TEXT, locator TEXT, quote TEXT,
                                       char_start INTEGER, char_end INTEGER, grounding_ok INTEGER, grounding_reasons TEXT,
                                       PRIMARY KEY (entry, doi, obs_id));
CREATE TABLE figures (entry TEXT, doi TEXT, figure_id TEXT, source_pdf TEXT, document_role TEXT, page_index INTEGER, bbox TEXT,
                      caption_label TEXT, classification TEXT, png_path TEXT, redistribution_permission TEXT, license_scope TEXT,
                      PRIMARY KEY (entry, doi, figure_id));
CREATE TABLE comparisons (comparison_id TEXT PRIMARY KEY, entry TEXT, quantity_role TEXT, status TEXT, reason_codes TEXT,
                          slot_states TEXT, doi_a TEXT, doi_b TEXT, condition_a TEXT, condition_b TEXT, n_shared_residues INTEGER,
                          n_value_agree INTEGER, median_rel_diff REAL, independence_basis TEXT, provenance_a TEXT,
                          provenance_b TEXT, sources TEXT);
"""


class StoreError(RuntimeError):
    pass


def _paper_rows(rec: PaperRecord, texts: dict[str, str] | None) -> dict[str, list[tuple]]:
    grounding = {g.row_id: g for g in rec.verify_grounding(texts)} if texts is not None else {}
    qual_grounding = {g.row_id: g for g in rec.verify_qualitative_grounding(texts)} if texts is not None else {}
    links = rec.figure_links()
    out: dict[str, list[tuple]] = {
        "papers": [], "samples": [], "measurements": [], "qualitative_observations": [], "figures": [],
    }
    primary = rec.primary_measurements()
    out["papers"].append((
        rec.entry, rec.doi, rec.title, rec.stance or "", rec.notes, len(rec.samples),
        len(rec.measurements), len(primary), len(rec.qualitative_observations),
    ))
    for s in rec.samples:
        out["samples"].append((
            rec.entry, rec.doi, s.sample_id, s.uniprot_accession, s.isoform_version, s.construct_label,
            s.species_relation, s.same_as_deposit, s.ligand_state, s.temperature_raw, s.temperature_k,
            s.ph, s.buffer, s.field_mhz_raw,
        ))
    for m in rec.measurements:
        g = grounding.get(m.row_id)
        link_status, fig_id = links.get(m.row_id, ("", None))
        out["measurements"].append((
            rec.entry, rec.doi, m.row_id, m.sample_id, m.quantity, m.quantity_canonical, m.value_raw, m.value_num, m.unit_raw,
            m.unit_canonical, m.residues_raw, m.source_role, m.evidence_modality, m.document_role, m.locator, m.quote,
            g.char_start if g else m.char_start, g.char_end if g else m.char_end, None if g is None else int(g.ok),
            ";".join(g.reasons) if g else "NOT_CHECKED", link_status, fig_id or ""))
    for q in rec.qualitative_observations:
        qg = qual_grounding.get(q.obs_id)
        out["qualitative_observations"].append((
            rec.entry, rec.doi, q.obs_id, q.sample_id, q.document_role, q.category, q.evidence_level, q.residues_raw,
            json.dumps(q.pdb_ids), q.summary, q.locator, q.quote,
            qg.char_start if qg else q.char_start, qg.char_end if qg else q.char_end,
            None if qg is None else int(qg.ok), ";".join(qg.reasons) if qg else "NOT_CHECKED",
        ))
    for f in rec.figures:
        out["figures"].append((rec.entry, rec.doi, f.figure_id, f.source_pdf, f.document_role, f.page_index, json.dumps(list(f.bbox)),
                               f.caption_label, f.classification, f.png_path, f.redistribution_permission, f.license_scope))
    return out


def write_store(db_path: Path | str, records: Iterable[PaperRecord], texts_by_doi: dict[str, dict[str, str]] | None = None,
                comparisons: Iterable[ComparisonOutcome] = ()) -> dict[str, Any]:
    """Build the database atomically. `texts_by_doi[doi]` maps document_role to ingested text for grounding checks."""
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    tables: dict[str, list[tuple]] = {
        "papers": [], "samples": [], "measurements": [], "qualitative_observations": [], "figures": [], "comparisons": [],
    }
    for rec in records:
        for name, rows in _paper_rows(rec, (texts_by_doi or {}).get(rec.doi)).items():
            tables[name].extend(rows)
    for c in comparisons:
        tables["comparisons"].append((c.comparison_id, c.entry, c.quantity_role, c.status, ";".join(c.reason_codes),
                                      json.dumps(c.slot_states), c.doi_a, c.doi_b, c.condition_a, c.condition_b, c.n_shared_residues,
                                      c.n_value_agree, c.median_rel_diff, c.independence_basis, c.provenance_a, c.provenance_b,
                                      ";".join(c.sources)))
    fd, tmp_name = tempfile.mkstemp(prefix=f".{db_path.name}.", suffix=".building", dir=db_path.parent)
    os.close(fd)
    tmp = Path(tmp_name)
    try:
        con = sqlite3.connect(tmp)
        try:
            con.executescript(DDL)
            for name, rows in tables.items():
                if rows:
                    con.executemany(f"INSERT INTO {name} VALUES ({','.join('?' * len(rows[0]))})", rows)
            con.commit()
            integrity = con.execute("PRAGMA integrity_check").fetchone()[0]
            counts = {name: con.execute(f"SELECT COUNT(*) FROM {name}").fetchone()[0] for name in tables}
        finally:
            con.close()
        if integrity != "ok":
            raise StoreError(f"integrity_check failed: {integrity}")
        expected = {name: len(rows) for name, rows in tables.items()}
        if counts != expected:
            raise StoreError(f"row-count parity failed: wrote {counts}, expected {expected}")
        os.replace(tmp, db_path)
    except BaseException:
        if tmp.exists():
            tmp.unlink()  # our own staging file; the published database is untouched
        raise
    return {"db_path": str(db_path), "integrity_check": integrity, "row_counts": counts}
