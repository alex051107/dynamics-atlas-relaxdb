"""Focused mature open-source adapters (zero dead hooks; pruned per 2026-11-23 industrial stack review).

docling    structured table grids and figure/caption bounding boxes from IBM Docling (MIT), preserving
           page numbers and top-left PDF coordinates so PyMuPDF remains the canonical text-offset anchor.
datasette  command line to browse the SQLite output via `uvx datasette` (Apache-2.0) without polluting env.
"""
from __future__ import annotations

import importlib
import shutil
from functools import lru_cache
from pathlib import Path
from typing import Any


def optional_module(name: str):
    """Import `name` if available; any import-time failure counts as absent."""
    try:
        return importlib.import_module(name)
    except Exception:  # noqa: BLE001
        return None


def adapter_status() -> dict[str, bool]:
    return {
        "docling": optional_module("docling") is not None,
        "anthropic": optional_module("anthropic") is not None,
        "jinja2": optional_module("jinja2") is not None,
        "datasette_cli": shutil.which("datasette") is not None or shutil.which("uvx") is not None,
    }


@lru_cache(maxsize=1)
def _docling_converter():
    mod = optional_module("docling.document_converter")
    if mod is None:
        return None
    try:
        return mod.DocumentConverter()
    except Exception:  # noqa: BLE001
        return None


def _to_topleft_bbox(prov: Any, page_height: float | None) -> tuple[float, float, float, float] | None:
    """Convert Docling provenance bbox (usually BOTTOMLEFT origin) to PyMuPDF TOPLEFT (x0, y0, x1, y1)."""
    bbox = getattr(prov, "bbox", None)
    if bbox is None:
        return None
    l, r = float(bbox.l), float(bbox.r)
    t, b = float(bbox.t), float(bbox.b)
    origin = str(getattr(bbox, "coord_origin", "BOTTOMLEFT")).upper()
    if "BOTTOM" in origin and page_height:
        y0 = max(0.0, page_height - max(t, b))
        y1 = max(y0, page_height - min(t, b))
    else:
        y0, y1 = min(t, b), max(t, b)
    return (round(min(l, r), 2), round(y0, 2), round(max(l, r), 2), round(y1, 2))


def docling_extract_layout(pdf_path: Path | str) -> dict[str, Any] | None:
    """Extract structured tables (rows + bbox + caption) and figures (bbox + caption) via DoclingDocument.

    Returns None when Docling is unavailable or fails, allowing clean fallback to PyMuPDF.
    Never converts the whole paper to Markdown or discards PyMuPDF character offsets.
    """
    conv = _docling_converter()
    if conv is None:
        return None
    try:
        res = conv.convert(str(pdf_path))
        ddoc = res.document
    except Exception:  # noqa: BLE001
        return None

    page_heights: dict[int, float] = {}
    for pno, pinfo in (getattr(ddoc, "pages", None) or {}).items():
        sz = getattr(pinfo, "size", None)
        if sz is not None and getattr(sz, "height", None):
            page_heights[int(pno)] = float(sz.height)

    tables: list[dict[str, Any]] = []
    for t in getattr(ddoc, "tables", None) or []:
        grid_raw = getattr(getattr(t, "data", None), "grid", None) or []
        rows = [[" ".join((getattr(c, "text", "") or "").split()) for c in row] for row in grid_raw]
        rows = [row for row in rows if any(row)]
        if not rows:
            continue
        prov = (getattr(t, "prov", None) or [None])[0]
        pno = int(prov.page_no) if prov is not None and getattr(prov, "page_no", None) is not None else 1
        bbox = _to_topleft_bbox(prov, page_heights.get(pno))
        cap = (t.caption_text(ddoc) if hasattr(t, "caption_text") else "") or ""
        tables.append({
            "page_index": max(0, pno - 1),
            "bbox": bbox,
            "caption": " ".join(cap.split())[:600],
            "rows": rows,
        })

    pictures: list[dict[str, Any]] = []
    for pic in getattr(ddoc, "pictures", None) or []:
        prov = (getattr(pic, "prov", None) or [None])[0]
        if prov is None:
            continue
        pno = int(prov.page_no) if getattr(prov, "page_no", None) is not None else 1
        bbox = _to_topleft_bbox(prov, page_heights.get(pno))
        if bbox is None:
            continue
        cap = (pic.caption_text(ddoc) if hasattr(pic, "caption_text") else "") or ""
        pictures.append({
            "page_index": max(0, pno - 1),
            "bbox": bbox,
            "caption": " ".join(cap.split())[:1200],
        })

    return {"tables": tables, "pictures": pictures, "n_pages": len(page_heights)}


def datasette_command(db_path: Path) -> list[str]:
    exe = shutil.which("datasette")
    if exe:
        return [exe, str(db_path)]
    if shutil.which("uvx"):
        return ["uvx", "datasette", str(db_path)]
    return ["datasette", str(db_path)]
