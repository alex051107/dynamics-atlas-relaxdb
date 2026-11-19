#!/usr/bin/env python3
"""Zero-dependency CLI to query RelaxDB_expert_review_DRAFT.sqlite.

Answers Soojung & Gina's core Dynamics Atlas questions in milliseconds while
enforcing physical-scope separation, numeric quarantine, numbering-offset
warnings, phosphate-buffer flags, Dyna-1 missing-peak preservation, and
explicit Gap/BMRB provenance.

Usage:
  python3 query_atlas.py residue FKBP 59
  python3 query_atlas.py residue 16392 169
  python3 query_atlas.py exchange --window us-ms --limit 25
  python3 query_atlas.py transition FKBP
  python3 query_atlas.py bmrb 50020 --lowest-noe 5
  python3 query_atlas.py search "precipitated AND elevated AND temperature"
  python3 query_atlas.py audit
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sqlite3
import sys

DEFAULT_DB = Path(__file__).resolve().parent / "RelaxDB_expert_review_DRAFT.sqlite"


def connect(db_path: Path) -> sqlite3.Connection:
    if not db_path.is_file():
        sys.exit(f"Database not found: {db_path}")
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def cmd_residue(conn: sqlite3.Connection, entry: str, res_num: int):
    prot = conn.execute("SELECT * FROM proteins WHERE upper(entry)=upper(?)", (entry,)).fetchone()
    if not prot:
        return {"error": f"Entry '{entry}' not found in proteins"}
    e = prot["entry"]

    obs = [
        dict(r)
        for r in conn.execute(
            """
            SELECT DISTINCT o.obs_id, o.physical_scope, o.signal_class, o.quantity,
                   o.value_raw, o.unit_raw, o.region, o.sample_id, o.ligand_and_conditions,
                   o.verification_tier, o.eco_evidence_code, o.doi, o.source_locator
            FROM residue_bridge rb
            JOIN observations o ON o.obs_id = rb.entity_key
            WHERE rb.entry = ? AND rb.entity_type = 'observation'
              AND ? BETWEEN rb.res_start AND rb.res_end
            ORDER BY o.physical_scope, o.obs_id
            """,
            (e, res_num),
        ).fetchall()
    ]
    meas = [
        dict(r)
        for r in conn.execute(
            """
            SELECT DISTINCT m.meas_id, m.quantity, m.comparator, m.value_num, m.value_high,
                   m.unit_canonical, m.signal_observation_class, m.data_validity_flag,
                   m.residues_raw, m.sample, m.doi, m.location_in_paper
            FROM residue_bridge rb
            JOIN measurements_clean m ON CAST(m.meas_id AS TEXT) = rb.entity_key
            WHERE rb.entry = ? AND rb.entity_type = 'measurement'
              AND ? BETWEEN rb.res_start AND rb.res_end
            ORDER BY m.signal_observation_class, m.quantity, m.meas_id
            LIMIT 40
            """,
            (e, res_num),
        ).fetchall()
    ]
    bmrb_vals = [
        dict(r)
        for r in conn.execute(
            """
            SELECT bmrb_id, quantity, field_mhz, seq_id, auth_seq_id, comp_id,
                   val, err, units, standardized_rate_s_inv, is_scale_anomaly
            FROM bmrb_recovered_values
            WHERE entry = ? AND (auth_seq_id = ? OR (auth_seq_id IS NULL AND seq_id = ?))
            ORDER BY quantity, field_mhz
            """,
            (e, res_num, res_num),
        ).fetchall()
    ]
    quar_n = conn.execute("SELECT COUNT(*) FROM measurements_quarantine WHERE entry=?", (e,)).fetchone()[0]
    gaps = [
        dict(r)
        for r in conn.execute(
            "SELECT gap_triage, COUNT(*) AS n FROM gaps WHERE entry=? GROUP BY gap_triage",
            (e,),
        ).fetchall()
    ]
    return {
        "entry": e,
        "protein": prot["protein"],
        "uniprot": prot["uniprot"],
        "queried_residue": res_num,
        "warnings": {
            "numbering_offset_warning": prot["numbering_offset_warning"],
            "phosphate_only_flag": prot["phosphate_only_flag"],
            "quarantined_measurement_rows_for_entry": quar_n,
            "gaps_for_entry": gaps,
        },
        "curated_observations": obs,
        "clean_measurements": meas,
        "bmrb_direct_values_at_residue": bmrb_vals,
    }


def cmd_exchange(conn: sqlite3.Connection, min_kex: float | None, exclude_phosphate_only: bool, limit: int):
    sql = """
        SELECT o.entry, p.protein, p.uniprot, p.phosphate_only_flag, p.numbering_offset_warning,
               o.obs_id, o.region, o.quantity, o.value_raw, o.unit_raw, o.method,
               o.ligand_and_conditions, o.verification_tier, o.doi
        FROM observations o
        JOIN proteins p ON p.entry = o.entry
        WHERE o.physical_scope = 'solution_conformational_exchange'
    """
    params = []
    if exclude_phosphate_only:
        sql += " AND p.phosphate_only_flag != 'YES_PHOSPHATE_ONLY'"
    sql += " ORDER BY o.verification_tier DESC, o.entry, o.obs_id LIMIT ?"
    params.append(limit)
    curated = [dict(r) for r in conn.execute(sql, params).fetchall()]

    kex_sql = """
        SELECT m.entry, p.protein, m.residues_raw, m.comparator, m.value_num, m.value_high,
               m.unit_canonical, m.method, m.sample, m.doi, m.data_validity_flag
        FROM measurements_clean m
        JOIN proteins p ON p.entry = m.entry
        WHERE m.signal_observation_class = 'QUANTIFIED_EXCHANGE'
          AND lower(m.quantity) IN ('kex','kopen','kclose','kab','kba')
    """
    kparams = []
    if min_kex is not None:
        kex_sql += " AND m.value_num >= ?"
        kparams.append(min_kex)
    if exclude_phosphate_only:
        kex_sql += " AND p.phosphate_only_flag != 'YES_PHOSPHATE_ONLY'"
    kex_sql += " ORDER BY m.value_num DESC LIMIT ?"
    kparams.append(limit)
    rates = [dict(r) for r in conn.execute(kex_sql, kparams).fetchall()]

    dyna_missing = conn.execute(
        "SELECT COUNT(*) FROM dyna1_signals WHERE signal_observation_class='EXCHANGE_BROADENED_MISSING_PEAK'"
    ).fetchone()[0]
    assoc_blocked = conn.execute(
        "SELECT COUNT(*) FROM observations WHERE physical_scope='association'"
    ).fetchone()[0]
    return {
        "association_rows_excluded": assoc_blocked,
        "dyna1_missing_peak_regions_preserved": dyna_missing,
        "curated_solution_exchange_observations": curated,
        "clean_exchange_rate_rows": rates,
    }


def cmd_transition(conn: sqlite3.Connection, entry: str):
    prot = conn.execute("SELECT * FROM proteins WHERE upper(entry)=upper(?)", (entry,)).fetchone()
    if not prot:
        return {"error": f"Entry '{entry}' not found"}
    e = prot["entry"]
    comps = [
        dict(r)
        for r in conn.execute("SELECT * FROM region_comparisons WHERE entry=? ORDER BY comparison_id", (e,)).fetchall()
    ]
    obs = [
        dict(r)
        for r in conn.execute(
            "SELECT obs_id, physical_scope, signal_class, region, quantity, value_raw, unit_raw, sample_id, ligand_and_conditions, verification_tier, doi FROM observations WHERE entry=? ORDER BY obs_id",
            (e,),
        ).fetchall()
    ]
    samps = [
        dict(r)
        for r in conn.execute(
            "SELECT doi, sample, construct, ligand_state, temperature, ph, buffer, field_mhz, has_phosphate, is_superseded, is_referenced_by_dynamics FROM samples WHERE entry=? AND is_referenced_by_dynamics=1 ORDER BY doi, sample",
            (e,),
        ).fetchall()
    ]
    return {
        "protein": dict(prot),
        "region_comparisons": comps,
        "observations": obs,
        "active_dynamics_samples": samps,
    }


def cmd_bmrb(conn: sqlite3.Connection, entry: str, lowest_noe: int):
    summary = [
        dict(r)
        for r in conn.execute(
            "SELECT * FROM bmrb_recovered WHERE upper(entry)=upper(?) OR bmrb_id=?",
            (entry, entry),
        ).fetchall()
    ]
    low_noes = [
        dict(r)
        for r in conn.execute(
            """
            SELECT bmrb_id, comp_id, seq_id, auth_seq_id, val, err, field_mhz
            FROM bmrb_recovered_values
            WHERE (upper(entry)=upper(?) OR bmrb_id=?) AND quantity='NOE' AND is_scale_anomaly=0
            ORDER BY val ASC LIMIT ?
            """,
            (entry, entry, lowest_noe),
        ).fetchall()
    ]
    top_rex = [
        dict(r)
        for r in conn.execute(
            """
            SELECT bmrb_id, comp_id, seq_id, auth_seq_id, val, err, field_mhz
            FROM bmrb_recovered_values
            WHERE (upper(entry)=upper(?) OR bmrb_id=?) AND quantity='Rex' AND val > 0
            ORDER BY val DESC LIMIT ?
            """,
            (entry, entry, lowest_noe),
        ).fetchall()
    ]
    return {"bmrb_summary": summary, "lowest_clean_noe": low_noes, "highest_positive_rex": top_rex}


def cmd_search(conn: sqlite3.Connection, query: str, limit: int):
    rows = [
        dict(r)
        for r in conn.execute(
            "SELECT doc_type, entry, doc_key, doi, snippet(corpus_fts, 4, '[', ']', '...', 18) AS hit FROM corpus_fts WHERE corpus_fts MATCH ? LIMIT ?",
            (query, limit),
        ).fetchall()
    ]
    return {"query": query, "hits_count": len(rows), "hits": rows}


def cmd_audit(conn: sqlite3.Connection):
    return {
        "data_quality_audit": [dict(r) for r in conn.execute("SELECT * FROM data_quality_audit ORDER BY audit_id").fetchall()],
        "table_counts": {
            t: conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
            for t in (
                "proteins", "samples", "measurements_clean", "measurements_quarantine",
                "observations", "region_comparisons", "dyna1_signals", "residue_bridge",
                "gaps", "bmrb_recovered", "bmrb_recovered_values",
            )
        },
    }


def main():
    parser = argparse.ArgumentParser(description="Query RelaxDB_expert_review_DRAFT.sqlite")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB, help="Path to SQLite file")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_res = sub.add_parser("residue", help="Evidence for one protein at one residue number")
    p_res.add_argument("entry")
    p_res.add_argument("res_num", type=int)

    p_ex = sub.add_parser("exchange", help="Cross-protein solution conformational exchange")
    p_ex.add_argument("--min-kex", type=float, default=None)
    p_ex.add_argument("--exclude-phosphate-only", action="store_true")
    p_ex.add_argument("--limit", type=int, default=20)

    p_tr = sub.add_parser("transition", help="Transitions, observations, and exact conditions for one protein")
    p_tr.add_argument("entry")

    p_bm = sub.add_parser("bmrb", help="Direct BMRB recovered relaxation summary and outliers")
    p_bm.add_argument("entry")
    p_bm.add_argument("--lowest-noe", type=int, default=5)

    p_se = sub.add_parser("search", help="Full-text FTS5 search across quotes, notes, samples, and gaps")
    p_se.add_argument("query")
    p_se.add_argument("--limit", type=int, default=15)

    sub.add_parser("audit", help="Executive data quality audit and table counts")

    args = parser.parse_args()
    conn = connect(args.db)
    try:
        if args.cmd == "residue":
            out = cmd_residue(conn, args.entry, args.res_num)
        elif args.cmd == "exchange":
            out = cmd_exchange(conn, args.min_kex, args.exclude_phosphate_only, args.limit)
        elif args.cmd == "transition":
            out = cmd_transition(conn, args.entry)
        elif args.cmd == "bmrb":
            out = cmd_bmrb(conn, args.entry, args.lowest_noe)
        elif args.cmd == "search":
            out = cmd_search(conn, args.query, args.limit)
        else:
            out = cmd_audit(conn)
        print(json.dumps(out, indent=2, ensure_ascii=False))
    finally:
        conn.close()


if __name__ == "__main__":
    main()
