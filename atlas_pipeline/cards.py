"""Scientist cards v2: five questions per RelaxDB-CPMG entry, answered only from data loaded at run time.

The CPMG entry list comes from the curated label file (`relaxdb_cpmg_open`). Each card answers
  Q1 which residues exchange (RelaxDB label vs literature evidence, recall split by label-source / independent papers),
  Q2 on what timescale (fitted exchange rates -> tau_ex window),
  Q3 fitted rates and populations per condition (construct, ligand, temperature, paper; never pooled),
  Q4 methods and cross-paper comparison status (data_driven_comparisons outcomes),
  Q5 alternate-state PDB entries (Excel `States` sheet, entry and twin entries),
and shows cropped figure previews from figures_manifest.json, NIH S3 links matched by entry, twin or DOI, and the
verbatim span of each quoted value in the ingested full text when this run ingested that paper.
Figure previews are UNKNOWN_RESTRICTED: internal review only, never a redistribution grant.
"""
from __future__ import annotations

import base64
import html
import io
import json
import re
import statistics
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

from .compare import DB_PATH, LABEL_CLASS, STRICT_POSITIVE, Row, _connect, _norm_doi
from .schema import numeric_values

XLSX_PATH = DB_PATH.with_suffix(".xlsx")
RATE_ROLES = ("kex", "kab", "kba", "kopen", "kclose", "kct")
POP_ROLES = ("pb", "pa", "population")
SHIFT_ROLES = ("delta_omega",)
KINETIC_ROLES = RATE_ROLES + POP_ROLES + SHIFT_ROLES + ("tau_ex",)
MAX_FIGS_PER_CARD = 6
THUMB_WIDTH = 460


# ----------------------------------------------------------------------------- helpers

def residue_ranges(seq: str, idx: list[int]) -> str:
    """[12,13,14,61] -> 'G12–A14, Q61' using 1-based sequence positions."""
    idx = sorted(set(idx))
    out, i = [], 0
    while i < len(idx):
        j = i
        while j + 1 < len(idx) and idx[j + 1] == idx[j] + 1:
            j += 1
        a, b = idx[i], idx[j]
        la = f"{seq[a - 1] if 0 < a <= len(seq) else '?'}{a}"
        out.append(la if a == b else f"{la}–{seq[b - 1] if 0 < b <= len(seq) else '?'}{b}")
        i = j + 1
    return ", ".join(out)


# Conventional exchange-rate ranges of the NMR experiments (approximate): rates below ~100 s^-1 are CEST/ZZ territory,
# ~100-10^4 s^-1 is the CPMG window, ~10^4-10^5 s^-1 needs R1rho.
EXCHANGE_WINDOWS = (("CEST/ZZ range (kex ~1-100 s^-1)", 1.0, 100.0), ("CPMG range (kex ~100-10^4 s^-1)", 100.0, 1e4),
                    ("R1rho range (kex ~10^4-10^5 s^-1)", 1e4, 1e5))


def timescale_window(rates_s1: list[float]) -> dict[str, Any]:
    pos = sorted(r for r in rates_s1 if r and r > 0)
    if not pos:
        return {"band": "no fitted exchange rate in s^-1", "n": 0}
    lo, hi = pos[0], pos[-1]
    hits = [name for name, a, b in EXCHANGE_WINDOWS if lo < b and hi >= a]
    return {"band": " + ".join(hits) or "outside 1-10^5 s^-1", "n": len(pos), "rate_min": lo, "rate_max": hi,
            "tau_ex_ms_min": round(1000.0 / hi, 4), "tau_ex_ms_max": round(1000.0 / lo, 4)}


def strip_tags(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text or "")).strip()


def _norm_for_search(text: str) -> str:
    t = unicodedata.normalize("NFKC", text or "")
    t = re.sub(r"-\s*\n\s*", "", t)
    return re.sub(r"\s+", " ", strip_tags(t)).strip().lower()


def verbatim_span(quote: str, texts: dict[str, str]) -> dict[str, Any]:
    """Exact char span of the quote in an ingested text, else a whitespace/hyphenation-normalised hit, else not found."""
    if not quote or not texts:
        return {"status": "NOT_CHECKED_NO_INGESTED_TEXT"}
    for role, text in texts.items():
        i = text.find(quote)
        if i >= 0:
            return {"status": "VERBATIM_EXACT", "document_role": role, "char_start": i, "char_end": i + len(quote)}
    nq = _norm_for_search(quote)
    if len(nq) >= 12:
        for role, text in texts.items():
            i = _norm_for_search(text).find(nq)
            if i >= 0:
                return {"status": "VERBATIM_AFTER_WHITESPACE_NORMALISATION", "document_role": role, "normalised_offset": i}
    return {"status": "NOT_FOUND_IN_INGESTED_TEXT"}


def highlight(quote: str, value_raw: str | float | None) -> str:
    """HTML-escaped quote with the reported value's numeric tokens marked (token-bounded, sign-aware)."""
    q = strip_tags(quote)
    targets = [v for v in numeric_values(str(value_raw if value_raw is not None else ""))][:3]
    if not targets:
        return html.escape(q)
    spans = []
    for m in re.finditer(r"(?<![\w.])[−\-+]?\d+(?:[.,]\d+)?(?:[eE][−\-+]?\d+)?(?![\w])", q):
        tok = m.group(0).replace("−", "-")
        tok = tok.replace(",", "") if re.fullmatch(r"[-+]?\d{1,3},\d{3}", tok) else tok.replace(",", ".")
        try:
            val = float(tok)
        except ValueError:
            continue
        if any(abs(val - t) <= 1e-9 * max(1.0, abs(t)) for t in targets):
            spans.append((m.start(), m.end()))
    if not spans:
        return html.escape(q)
    out, pos = [], 0
    for a, b in spans:
        out.append(html.escape(q[pos:a]))
        out.append(f"<mark>{html.escape(q[a:b])}</mark>")
        pos = b
    out.append(html.escape(q[pos:]))
    return "".join(out)


def _thumb_data_uri(png_path: str) -> str | None:
    try:
        from PIL import Image
    except Exception:  # noqa: BLE001
        return None
    p = Path(png_path)
    if not p.is_file():
        return None
    with Image.open(p) as im:
        im = im.convert("RGB")
        if im.width > THUMB_WIDTH:
            im = im.resize((THUMB_WIDTH, max(1, round(im.height * THUMB_WIDTH / im.width))))
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=80)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("ascii")


def load_states(xlsx_path: Path = XLSX_PATH) -> dict[str, list[dict[str, str]]]:
    import openpyxl

    wb = openpyxl.load_workbook(xlsx_path, read_only=True, data_only=True)
    try:
        rows = list(wb["States"].iter_rows(values_only=True))
    finally:
        wb.close()
    header = [str(h or "").strip().lower() for h in rows[0]]
    col = {name: header.index(name) for name in ("entry", "doi", "pdb", "state", "location in paper", "quote")}
    by_entry: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in rows[1:]:
        if r and r[col["entry"]]:
            by_entry[str(r[col["entry"]]).strip()].append({k: str(r[i] or "").strip() for k, i in col.items()})
    return by_entry


def load_entry_meta(entries: list[str], db_path: Path = DB_PATH) -> tuple[dict[str, dict], list[dict]]:
    con = _connect(db_path)
    try:
        meta = {r["entry"]: dict(r) for r in con.execute(
            "SELECT entry, protein, uniprot, evidence_tier, papers_read, twin_entries, numbering_offset_warning FROM proteins")}
        links = [dict(r) for r in con.execute(
            "SELECT entries, doi, pmcid, fig_label, s3_figure_url, s3_high_dpi_pdf_url, license_spdx, public_release_permission "
            "FROM figure_s3_links")]
    finally:
        con.close()
    return {e: meta.get(e, {}) for e in entries}, links


# ----------------------------------------------------------------------------- card assembly

def build_cards(data: dict[str, Any], outcomes: list[Any], bench: dict[str, Any], figures_manifest: dict[str, Any] | None,
                texts_by_doi: dict[str, dict[str, str]] | None, states: dict[str, list[dict[str, str]]],
                f14_papers: dict[str, list[str]] | None = None) -> list[dict[str, Any]]:
    curated = data["curated"]
    entries = sorted(e for e, c in curated.items() if c["dataset"] == "relaxdb_cpmg_open")
    meta, links = load_entry_meta(entries)
    bench_by_entry = {b["entry"]: b for b in bench["entries"]}
    rows_by_entry: dict[str, list[Row]] = defaultdict(list)
    for r in data["rows"]:
        rows_by_entry[r.entry].append(r)
    outs_by_entry: dict[str, list[Any]] = defaultdict(list)
    for o in outcomes:
        outs_by_entry[o.entry].append(o)
    figs = (figures_manifest or {}).get("figures", [])
    digs = (figures_manifest or {}).get("digitizations", [])
    texts_by_doi = {_norm_doi(k): v for k, v in (texts_by_doi or {}).items()}
    cards = []
    for entry in entries:
        cur, m = curated[entry], meta.get(entry, {})
        seq, lab = cur["sequence"], cur["label"]
        twins = [t.strip() for t in (m.get("twin_entries") or "").split(",") if t.strip()]
        rows = rows_by_entry.get(entry, [])
        b = bench_by_entry.get(entry, {})
        positives = [i + 1 for i, ch in enumerate(lab) if LABEL_CLASS.get(ch) == "EXCHANGE_POSITIVE"]
        strict = [i + 1 for i, ch in enumerate(lab) if ch in STRICT_POSITIVE]
        dois = sorted({r.doi for r in rows if r.doi} | {_norm_doi(d) for d in (f14_papers or {}).get(entry, [])})
        # Q2 + Q3: kinetic rows grouped by condition, one group per paper x construct x ligand x temperature
        groups: dict[tuple, list[Row]] = defaultdict(list)
        rates = []
        for r in rows:
            if r.role not in KINETIC_ROLES or r.value_base is None:
                continue
            groups[(r.doi, r.construct.strip() or "construct not stated", r.ligand.strip() or "ligand not stated",
                    f"{r.temp_k:.1f} K" if r.temp_k is not None else (r.temp_raw or "T not stated"), r.secondary)].append(r)
            if r.secondary:
                continue  # a value the paper cites from earlier work is listed as cited, never as this paper's fitted rate
            if r.role in RATE_ROLES and r.dim == "rate":
                rates.append(r.value_base)
            if r.role == "tau_ex" and r.dim == "time" and r.value_base > 0:
                rates.append(1.0 / r.value_base)
        q3 = []
        for (doi, construct, ligand, temp, secondary), grs in sorted(groups.items()):
            by_role: dict[str, list[Row]] = defaultdict(list)
            for r in grs:
                by_role[r.role].append(r)
            for role, rr in sorted(by_role.items()):
                vals = [r.value_base for r in rr]
                rep = rr[0]
                unit = {"rate": "s^-1", "fraction": "fraction", "chemical_shift": "ppm", "time": "s"}.get(rep.dim, rep.dim)
                span = verbatim_span(rep.quote, texts_by_doi.get(doi, {}))
                q3.append({"doi": doi, "construct": construct, "ligand": ligand, "temperature": temp, "quantity": role,
                           "origin": "cited_or_secondary" if secondary else "this_paper",
                           "n_rows": len(rr), "n_residue_specific": sum(1 for r in rr if r.residue), "median": statistics.median(vals),
                           "min": min(vals), "max": max(vals), "unit_base": unit, "source": rep.source,
                           "example_value_raw": rep.value if rep.value is not None else "", "example_unit_raw": rep.unit_raw,
                           "example_residue": rep.residues_raw, "example_location": rep.location,
                           "example_quote_html": highlight(rep.quote, rep.value), "example_span": span})
        span_counts = Counter(verbatim_span(r.quote, texts_by_doi.get(r.doi, {}))["status"] for r in rows if r.quote) \
            if any(texts_by_doi.get(d) for d in dois) else Counter()
        methods = Counter((r.doi, r.method or "method not stated") for r in rows)
        outs = outs_by_entry.get(entry, [])
        status_counts = Counter(o.status for o in outs)
        shown = sorted(outs, key=lambda o: ({"AGREE_INDEPENDENT": 0, "CONDITIONAL_DIFF": 1, "REVIEW_SECONDARY": 2,
                                             "LABEL_SOURCE_ONLY": 3, "NOT_COMPARABLE_ABSTAIN": 4}[o.status], o.comparison_id))[:10]
        alt = [dict(s, via=e) for e in [entry, *twins] for s in states.get(e, [])]
        s3 = [l for l in links if entry in [x.strip() for x in str(l["entries"] or "").split(",")]
              or any(t in [x.strip() for x in str(l["entries"] or "").split(",")] for t in twins)
              or _norm_doi(l["doi"]) in dois]
        fig_rows = [f for f in figs if f.get("entry") == entry]
        fig_cards = []
        for f in fig_rows[:MAX_FIGS_PER_CARD]:
            d_ok = [d for d in digs if d.get("figure_id") == f["figure_id"] and d.get("status") == "OK"]
            d_ab = [d for d in digs if d.get("figure_id") == f["figure_id"] and d.get("status") != "OK"]
            fig_cards.append({
                "figure_id": f["figure_id"], "doi": f.get("doi", ""), "caption_label": f.get("caption_label", ""),
                "classification": f["classification"],
                "page": f["page_index"] + 1, "document_role": f["document_role"], "caption": (f.get("caption_text") or "")[:300],
                "thumb": _thumb_data_uri(f.get("png_path", "")), "png_path": f.get("png_path", ""),
                "digitized_ok": [{"n_points": d.get("n_points"), "overlay": _thumb_data_uri(d.get("overlay_png", "")),
                                  "overlay_path": d.get("overlay_png", ""), "alignment": d.get("pixel_alignment_fraction"),
                                  "x_scale": (d.get("x_calibration") or {}).get("scale"),
                                  "y_scale": (d.get("y_calibration") or {}).get("scale")} for d in d_ok[:2]],
                "digitize_abstain": sorted({d.get("abstain_reason", "") for d in d_ab if d.get("abstain_reason")}),
                "permission": f.get("redistribution_permission", "UNKNOWN_RESTRICTED"),
            })
        cards.append({
            "entry": entry, "protein": m.get("protein", ""), "uniprot": m.get("uniprot", ""), "twin_entries": twins,
            "evidence_tier": m.get("evidence_tier", ""), "sequence_length": len(seq), "dois": dois,
            "q1": {"label_class_counts": dict(Counter(LABEL_CLASS.get(ch, "OTHER") for ch in lab)),
                   "n_positive": len(positives), "n_positive_strict": len(strict), "positive_ranges": residue_ranges(seq, positives),
                   "papers": b.get("papers", []), "recall_label_source": b.get("recall_label_source"),
                   "recall_independent": b.get("recall_independent"), "recall_provenance_unknown": b.get("recall_provenance_unknown"),
                   "independent_agreement": b.get("independent_agreement"), "label_source_dois": b.get("label_source_dois", [])},
            "q2": timescale_window(rates),
            "q3": q3,
            "q4": {"methods": [{"doi": d, "method": meth, "n_rows": n} for (d, meth), n in methods.most_common(12)],
                   "comparison_status_counts": dict(status_counts),
                   "comparisons": [o.model_dump() for o in shown]},
            "q5": alt,
            "figures": fig_cards, "n_figures_in_manifest": len(fig_rows),
            "s3_links": s3, "verbatim_span_counts": dict(span_counts), "n_rows": len(rows),
            "rows_by_source": dict(Counter(r.source for r in rows)),
        })
    return cards


# ----------------------------------------------------------------------------- rendering

TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"


def _fmt(v: Any) -> str:
    if v is None:
        return "—"
    if isinstance(v, float):
        return f"{v:.4g}"
    return str(v)


def render_html(cards: list[dict[str, Any]], meta: dict[str, Any], *, public_safe: bool = False) -> str:
    """Render scientist cards via Jinja2 template (BSD-3, autoescape=True).

    When `public_safe=True`, strip all inline base64 `thumb` and `overlay` images so no restricted publisher
    figure crops can enter public HTML exports.
    """
    from jinja2 import Environment, FileSystemLoader

    render_cards = cards
    if public_safe:
        render_cards = []
        for c in cards:
            c_copy = dict(c)
            safe_figs = []
            for f in c.get("figures", []):
                f_copy = {k: v for k, v in f.items() if k != "thumb"}
                f_copy["thumb"] = None
                f_copy["digitized_ok"] = [{k: v for k, v in d.items() if k != "overlay"} | {"overlay": None}
                                          for d in f.get("digitized_ok", [])]
                safe_figs.append(f_copy)
            c_copy["figures"] = safe_figs
            render_cards.append(c_copy)

    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)), autoescape=True)
    env.filters["fmt"] = _fmt
    tpl = env.get_template("scientist_cards.html.j2")
    return tpl.render(
        cards=render_cards,
        meta=meta,
        positive_chars=" ".join(k for k, v in LABEL_CLASS.items() if v == "EXCHANGE_POSITIVE"),
        strict_chars=" ".join(sorted(STRICT_POSITIVE)),
    )


def render_markdown(cards: list[dict[str, Any]], meta: dict[str, Any]) -> str:
    lines = ["# RelaxDB-CPMG scientist cards v2", "",
             f"Generated {meta['generated_at']} by `atlas_pipeline.cards` from the expert-review SQLite (read-only), the F14 CPMG "
             "sprint extractions, curated RelaxDB labels, the Excel States sheet and this run's figure manifest. Figure previews are "
             "UNKNOWN_RESTRICTED (internal review only).", ""]
    for c in cards:
        q1, q2 = c["q1"], c["q2"]
        lines += [f"## {c['entry']} · {c['protein']}", "",
                  f"UniProt {c['uniprot'] or '—'}; twins {', '.join(c['twin_entries']) or 'none'}; tier {c['evidence_tier'] or '—'}; "
                  f"{c['n_rows']} rows; papers {', '.join(c['dois']) or 'none'}.", "",
                  "**Q1 · Which residues exchange?**", "",
                  f"RelaxDB label: {q1['n_positive']} exchange-positive residues of {c['sequence_length']} (strict ^/Y: "
                  f"{q1['n_positive_strict']}): {q1['positive_ranges'] or 'none'}. Label-source papers: "
                  f"{', '.join(q1['label_source_dois']) or 'none identified'}. Recall: label-source {q1['recall_label_source']}, "
                  f"independent {q1['recall_independent']}, provenance unknown {q1['recall_provenance_unknown']}; independent agreement "
                  f"{q1['independent_agreement']}.", ""]
        for p in q1["papers"]:
            lines.append(f"- {p['doi']} ({p['role']}): {p['offset_status']}; {p['n_mapped']} mapped residues, "
                         f"{p['n_on_label_positive']} on label positives")
        lines += ["", "**Q2 · Timescale**", "",
                  (f"{q2['band']}: {q2['n']} fitted rates, {q2['rate_min']:.4g}–{q2['rate_max']:.4g} s^-1, tau_ex "
                   f"{q2['tau_ex_ms_min']:.4g}–{q2['tau_ex_ms_max']:.4g} ms." if q2["n"] else q2["band"] + "."), "",
                  "**Q3 · Fitted rates and populations by condition**", ""]
        if c["q3"]:
            lines += ["| paper | construct | ligand | T | quantity | n | median [min–max] | span |", "|---|---|---|---|---|---|---|---|"]
            for g in c["q3"]:
                cell = lambda s: str(s).replace("|", "/")[:60]  # noqa: E731
                quantity = g["quantity"] + (" (cited)" if g["origin"] != "this_paper" else "")
                lines.append(f"| {g['doi']} | {cell(g['construct'])} | {cell(g['ligand'])} | {g['temperature']} | {quantity} | "
                             f"{g['n_rows']} | {g['median']:.4g} [{g['min']:.4g}–{g['max']:.4g}] {g['unit_base']} | {g['example_span']['status']} |")
        else:
            lines.append("No fitted kinetic rows.")
        lines += ["", "**Q4 · Methods and comparison**", "",
                  "Methods: " + "; ".join(f"{x['method']} ({x['n_rows']}, {x['doi']})" for x in c["q4"]["methods"]) + ".",
                  "Comparison status: " + (", ".join(f"{k} {v}" for k, v in sorted(c["q4"]["comparison_status_counts"].items())) or "none") + ".", ""]
        for o in c["q4"]["comparisons"]:
            lines.append(f"- {o['status']} {o['quantity_role']}: {o['doi_a']} vs {o['doi_b'] or '—'} — {'; '.join(o['reason_codes'])}")
        lines += ["", "**Q5 · Alternate-state PDBs**", ""]
        lines += [f"- {s['pdb']} — {s['state'][:120]} ({s['doi']}, via {s['via']})" for s in c["q5"]] or ["None in the States sheet."]
        lines += ["", "**Figures**", ""]
        for f in c["figures"]:
            ok = f"; digitised {f['digitized_ok'][0]['n_points']} points, overlay `{f['digitized_ok'][0]['overlay_path']}`" if f["digitized_ok"] else ""
            lines.append(f"- {f['caption_label'] or f['figure_id']} ({f['classification']}, {f['document_role']} p.{f['page']} of {f['doi']}, "
                         f"{f['permission']}): `{f['png_path']}`{ok}")
        if not c["figures"]:
            lines.append("No local PDF processed for this entry in this run.")
        for l in c["s3_links"][:12]:
            lines.append(f"- S3: [{l['fig_label'] or 'figure'}]({l['s3_figure_url']}) · {l['doi']} · {l['license_spdx'] or 'licence unknown'}")
        lines.append("")
    return "\n".join(lines)


def write_cards(out_dir: Path | str, data: dict[str, Any], outcomes: list[Any], bench: dict[str, Any],
                figures_manifest: dict[str, Any] | None, texts_by_doi: dict[str, dict[str, str]] | None = None,
                f14_papers: dict[str, list[str]] | None = None) -> dict[str, Any]:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    states = load_states()
    cards = build_cards(data, outcomes, bench, figures_manifest, texts_by_doi, states, f14_papers)
    meta = {"generated_at": datetime.now().isoformat(timespec="seconds"),
            "label_alphabet_provenance": bench.get("label_alphabet_provenance", "")}
    html_path, md_path, json_path = (out_dir / "cpmg_scientist_cards_v2.html", out_dir / "cpmg_scientist_cards_v2.md",
                                     out_dir / "cpmg_scientist_cards_v2.json")
    html_path.write_text(render_html(cards, meta), encoding="utf-8")
    md_path.write_text(render_markdown(cards, meta), encoding="utf-8")
    slim = [{k: v for k, v in c.items() if k != "figures"} | {"figures": [{k: v for k, v in f.items() if k != "thumb"} for f in c["figures"]]}
            for c in cards]
    for c in slim:
        for f in c["figures"]:
            f["digitized_ok"] = [{k: v for k, v in d.items() if k != "overlay"} for d in f["digitized_ok"]]
    json_path.write_text(json.dumps({"meta": meta, "cards": slim}, indent=1, ensure_ascii=False, default=str), encoding="utf-8")
    return {"html": str(html_path), "md": str(md_path), "json": str(json_path), "n_cards": len(cards),
            "entries": [c["entry"] for c in cards],
            "n_figure_previews": sum(1 for c in cards for f in c["figures"] if f["thumb"]),
            "entries_with_figure_previews": [c["entry"] for c in cards if any(f["thumb"] for f in c["figures"])]}


def f14_papers_read(batches) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for p in batches:
        for ent in json.loads(Path(p).read_text(encoding="utf-8")).get("entries", []):
            if isinstance(ent.get("papers_read"), list):
                out[ent["entry"]] = [str(d) for d in ent["papers_read"]]
    return out
