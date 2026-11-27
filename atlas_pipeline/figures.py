"""Figure inventory, 300 DPI crops, vector XY digitization with overlays, blind error gate, raster handoff stubs.

Inventory: every page is inspected. Graphic regions come from embedded raster rectangles (`get_images` +
`get_image_rects`) and vector paths (`get_drawings`), merged on a coarse occupancy grid, widened to nearby short
text (tick labels, axis titles, panel letters) and paired with the nearest caption block on the same page.
Each region is classified VECTOR_PLOT / RASTER_IMAGE / MIXED_VECTOR_RASTER and cropped at 300 DPI. Every crop is
`UNKNOWN_RESTRICTED`: an article licence is never read as permission to redistribute a figure.

Vector digitization (`extract_vector_xy_plot`): panels are found as bottom-left corners where a long horizontal and
a long vertical stroke meet; numeric words below / left of those axes are snapped to tick marks and fitted to
linear (or log10) page->data maps; small closed paths inside the panel become markers (grouped by colour and
shape), multi-segment strokes become polylines. A Matplotlib overlay draws magenta circles at every extracted point
on the 300 DPI render, and the rendered pixel under each point is checked for ink.
"""
from __future__ import annotations

import base64
import hashlib
import json
import math
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

from .adapters import docling_extract_layout
from .schema import (
    AxisCalibration,
    DigitizedSeries,
    DocumentRole,
    FigureAsset,
    PlotDigitizationResult,
    figure_number,
    normalize_minus,
)

DPI = 300
CAPTION_RE = re.compile(r"^\s*((?:Supplementary\s+|Extended\s+Data\s+)?Fig(?:ure)?\.?\s*(S?\d+))", re.I)
CAPTION_STRONG_RE = re.compile(r"^\s*(?:Supplementary\s+|Extended\s+Data\s+)?Fig(?:ure)?\.?\s*S?\d+\s*(?:[|.:—–-]|\s+[A-Z(]|$)", re.I)
NUMERIC_WORD_RE = re.compile(r"^[+-]?(?:\d+(?:\.\d+)?|\.\d+)$")
PANEL_LETTER_RE = re.compile(r"^[a-hA-H]$")
GRID_CELL_PT = 2.0
MERGE_GAP_PT = 6.0
TEXT_MARGIN_PT = 28.0
CROP_PAD_PT = 4.0
MAGENTA = "#FF00FF"


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _rect_tuple(r) -> tuple[float, float, float, float]:
    return (round(r.x0, 2), round(r.y0, 2), round(r.x1, 2), round(r.y1, 2))


def _color_hex(rgb) -> str:
    if not rgb:
        return "none"
    return "#" + "".join(f"{max(0, min(255, round(c * 255))):02x}" for c in rgb[:3])


def parse_numeric_label(text: str) -> float | None:
    t = normalize_minus(text or "").strip().replace(",", "").replace(" ", "")
    return float(t) if NUMERIC_WORD_RE.match(t) else None


def _touches(rect, clip) -> bool:
    """Bounding-box overlap that also works for zero-width or zero-height rects (straight lines)."""
    return not (rect.x1 < clip.x0 or rect.x0 > clip.x1 or rect.y1 < clip.y0 or rect.y0 > clip.y1)


def _open_page(pdf_path: Path | str, page_index: int):
    import pymupdf

    doc = pymupdf.open(str(pdf_path))
    page = doc[page_index]
    if page.rotation:
        page.remove_rotation()  # in-memory: drawings, words and renders share one upright frame
    return doc, page


# ============================================================================ inventory

def _is_decoration(rect, page_rect) -> bool:
    h, w = page_rect.height, page_rect.width
    if rect.width * rect.height > 0.6 * w * h:
        return True  # page backgrounds and frames
    if rect.y1 <= page_rect.y0 + 0.06 * h or rect.y0 >= page_rect.y1 - 0.06 * h:
        return True  # running headers, footers, publisher logos
    if (rect.height < 1.5 and rect.width > 0.7 * w) or (rect.width < 1.5 and rect.height > 0.7 * h):
        return True  # column and page rules
    return False


def _page_graphics(page) -> tuple[list[dict], list[Any]]:
    """Non-decorative vector paths and clipped raster rectangles of one page."""
    page_rect = page.rect
    paths = []
    for p in page.get_drawings():
        r = p["rect"]
        if r.is_empty and r.width == 0 and r.height == 0:
            continue
        fill = p.get("fill")
        if p.get("type") == "f" and fill and min(fill[:3]) > 0.98:
            continue  # white masks and backgrounds
        if _is_decoration(r, page_rect):
            continue
        paths.append(p)
    images = []
    for img in page.get_images(full=True):
        try:
            rects = page.get_image_rects(img[0])
        except Exception:  # noqa: BLE001 - a broken image xref must not stop the page inventory
            continue
        for r in rects:
            r = r & page_rect
            if not r.is_empty and r.width >= 2 and r.height >= 2:
                images.append(r)
    return paths, images


def _components(rects: list[Any], page_rect) -> list[Any]:
    """Connected components of rectangles (each widened by MERGE_GAP_PT/2) on a GRID_CELL_PT occupancy grid."""
    import numpy as np
    import pymupdf
    from scipy import ndimage

    if not rects:
        return []
    nx = int(math.ceil(page_rect.width / GRID_CELL_PT)) + 1
    ny = int(math.ceil(page_rect.height / GRID_CELL_PT)) + 1
    grid = np.zeros((ny, nx), dtype=bool)
    pad = MERGE_GAP_PT / 2
    for r in rects:
        x0 = max(0, int((r.x0 - pad - page_rect.x0) / GRID_CELL_PT))
        x1 = min(nx - 1, int((r.x1 + pad - page_rect.x0) / GRID_CELL_PT))
        y0 = max(0, int((r.y0 - pad - page_rect.y0) / GRID_CELL_PT))
        y1 = min(ny - 1, int((r.y1 + pad - page_rect.y0) / GRID_CELL_PT))
        grid[y0:y1 + 1, x0:x1 + 1] = True
    labels, _n = ndimage.label(grid)
    out = []
    for sl in ndimage.find_objects(labels):
        if sl is None:
            continue
        ys, xs = sl
        out.append(pymupdf.Rect(page_rect.x0 + xs.start * GRID_CELL_PT + pad, page_rect.y0 + ys.start * GRID_CELL_PT + pad,
                                page_rect.x0 + xs.stop * GRID_CELL_PT - pad, page_rect.y0 + ys.stop * GRID_CELL_PT - pad))
    return out


def _merge_overlapping(rects: list[Any]) -> list[Any]:
    rects = [r for r in rects if not r.is_empty]
    changed = True
    while changed:
        changed = False
        out: list[Any] = []
        for r in rects:
            for i, o in enumerate(out):
                if r.intersects(o):
                    out[i] = o | r
                    changed = True
                    break
            else:
                out.append(r)
        rects = out
    return rects


def _caption_blocks(blocks: list[tuple]) -> list[dict]:
    caps = []
    for b in blocks:
        if b[6] != 0:
            continue
        m = CAPTION_RE.match(b[4])
        if m:
            caps.append({"rect": b[:4], "label": re.sub(r"\s+", " ", m.group(1)).strip(), "text": re.sub(r"\s+", " ", b[4]).strip(),
                         "strong": bool(CAPTION_STRONG_RE.match(b[4]))})
    return caps


def _pair_caption(region, captions: list[dict]):
    """Nearest caption block: below the region first, then beside it, then above it."""
    import pymupdf

    best, best_score = None, float("inf")
    for c in captions:
        cr = pymupdf.Rect(c["rect"])
        h_overlap = min(region.x1, cr.x1) - max(region.x0, cr.x0)
        v_overlap = min(region.y1, cr.y1) - max(region.y0, cr.y0)
        if h_overlap > 0 and cr.y0 >= region.y0 + 0.5 * region.height and cr.y1 >= region.y1 - 6:
            score = max(0.0, cr.y0 - region.y1)  # below, possibly overlapping an image that runs under the caption
        elif v_overlap > 0 and (cr.x0 >= region.x1 - 6 or cr.x1 <= region.x0 + 6):
            score = 10 + max(cr.x0 - region.x1, region.x0 - cr.x1, 0)
        elif cr.y1 <= region.y0 + 6 and h_overlap > 0:
            score = 25 + region.y0 - cr.y1
        else:
            continue
        if not c["strong"]:
            score += 40
        if score < best_score:
            best, best_score = c, score
    return best


def _panel_letter(region, words: list[tuple]) -> str:
    import pymupdf

    zone = pymupdf.Rect(region.x0 - TEXT_MARGIN_PT, region.y0 - TEXT_MARGIN_PT, region.x1, region.y1)
    letters = [w for w in words if PANEL_LETTER_RE.match(w[4]) and pymupdf.Rect(w[:4]).intersects(zone)]
    return letters[0][4].lower() if len(letters) == 1 else ""


def _pair_following_page_captions(figures: list[FigureAsset], unpaired: list[dict]) -> tuple[list[FigureAsset], list[dict]]:
    """A caption alone on page k (no graphics there) belongs to the uncaptioned figure pages just before it."""
    out_unpaired = []
    by_page: dict[int, list[int]] = defaultdict(list)
    for i, f in enumerate(figures):
        by_page[f.page_index].append(i)
    for u in unpaired:
        targets: list[int] = []
        if not u["_page_has_figures"]:
            k = u["page_index"] - 1
            while k >= 0 and by_page.get(k) and all(not figures[i].caption_label for i in by_page[k]):
                targets = by_page[k] + targets
                k -= 1
        if targets:
            for i in targets:
                figures[i] = figures[i].model_copy(update={
                    "caption_label": u["label"], "figure_number": figure_number(u["label"]), "caption_text": u["_full_text"],
                    "caption_page_index": u["page_index"]})
        else:
            out_unpaired.append({k: v for k, v in u.items() if not k.startswith("_")})
    return figures, out_unpaired


def _classify_region(reg, in_paths: list[dict], in_images: list[Any]) -> tuple[str, float]:
    raster_area = sum((r & reg).get_area() for r in in_images)
    raster_frac = min(1.0, raster_area / max(reg.get_area(), 1e-9))
    if not in_images:
        cls = "VECTOR_PLOT"
    elif raster_frac >= 0.6 and len(in_paths) <= 25:
        cls = "RASTER_IMAGE"
    else:
        cls = "MIXED_VECTOR_RASTER"
    return cls, raster_frac


def inventory_pdf_figures(pdf_path: Path | str, out_dir: Path | str, document_role: DocumentRole, *,
                          license_scope: str = "unknown", stem: str | None = None,
                          use_docling_layout: bool = False) -> dict[str, Any]:
    """Inspect every page, crop every graphic region at 300 DPI, and return manifest entries (nothing is skipped silently).

    When `use_docling_layout=True` and Docling returns picture bounding boxes, those boxes and captions replace the
    PyMuPDF connected-component heuristics while preserving PyMuPDF 300 DPI cropping and VECTOR_PLOT/RASTER_IMAGE
    classification. If Docling is unavailable or finds no pictures, falls back cleanly to PyMuPDF.
    """
    import pymupdf

    pdf_path, out_dir = Path(pdf_path), Path(out_dir)
    crops_dir = out_dir / "crops"
    crops_dir.mkdir(parents=True, exist_ok=True)
    stem = stem or re.sub(r"[^A-Za-z0-9]+", "_", pdf_path.stem).strip("_")
    doc = pymupdf.open(str(pdf_path))
    docling_layout = docling_extract_layout(pdf_path) if use_docling_layout else None
    docling_by_page: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for pic in (docling_layout or {}).get("pictures") or []:
        bbox = pic.get("bbox")
        pidx = pic.get("page_index")
        if bbox and pidx is not None and 0 <= int(pidx) < doc.page_count:
            docling_by_page[int(pidx)].append(pic)
    use_docling = bool(docling_by_page)

    figures: list[FigureAsset] = []
    unpaired_captions: list[dict] = []
    skipped: list[dict] = []
    pages: list[dict] = []
    try:
        for pno, page in enumerate(doc):
            rotation = page.rotation
            if rotation:
                page.remove_rotation()
            paths, images = _page_graphics(page)
            blocks = page.get_text("blocks")
            words = page.get_text("words")
            captions = _caption_blocks(blocks)
            kept: list[tuple[Any, list[dict], list[Any], str | None]] = []
            if use_docling:
                for dp in sorted(docling_by_page.get(pno, []), key=lambda d: (round(d["bbox"][1]), d["bbox"][0])):
                    reg = pymupdf.Rect(dp["bbox"]) & page.rect
                    if reg.is_empty or reg.width < 40 or reg.height < 30:
                        skipped.append({"page_index": pno, "bbox": _rect_tuple(reg), "reason": "DOCLING_PICTURE_TOO_SMALL"})
                        continue
                    in_paths = [p for p in paths if reg.contains(p["rect"].tl + (p["rect"].br - p["rect"].tl) * 0.5)]
                    in_images = [r for r in images if r.intersects(reg)]
                    kept.append((reg, in_paths, in_images, (dp.get("caption") or "").strip() or None))
            else:
                try:
                    table_rects = [pymupdf.Rect(t.bbox) for t in page.find_tables().tables]
                except Exception:  # noqa: BLE001
                    table_rects = []
                regions = _components([p["rect"] for p in paths] + images, page.rect)
                caption_rects = [pymupdf.Rect(c["rect"]) for c in captions]
                for _ in range(2):  # widen to tick labels, axis titles and panel letters, then merge touching regions
                    grown = []
                    for reg in regions:
                        zone = reg + (-TEXT_MARGIN_PT, -TEXT_MARGIN_PT, TEXT_MARGIN_PT, TEXT_MARGIN_PT)
                        for b in blocks:
                            if b[6] != 0:
                                continue
                            br = pymupdf.Rect(b[:4])
                            lines = [ln for ln in b[4].splitlines() if ln.strip()]
                            if not lines or max(len(ln) for ln in lines) > 40 or any(br.intersects(cr) for cr in caption_rects):
                                continue
                            if _is_decoration(br, page.rect):
                                continue  # running header, footer or page number
                            if br.intersects(zone):
                                reg = reg | br
                        grown.append(reg)
                    regions = _merge_overlapping(grown)
                for reg in sorted(regions, key=lambda r: (round(r.y0), r.x0)):
                    if reg.width < 40 or reg.height < 30:
                        continue
                    in_paths = [p for p in paths if reg.contains(p["rect"].tl + (p["rect"].br - p["rect"].tl) * 0.5)]
                    in_images = [r for r in images if r.intersects(reg)]
                    if not in_images and len(in_paths) < 8:
                        continue  # a few rules or boxes, not a plot
                    if not in_paths and in_images and max(max(r.width, r.height) for r in in_images) < 15:
                        continue  # inline glyph images inside text
                    items = [it[0] for p in in_paths for it in p["items"]]
                    rect_share = items.count("re") / max(len(items), 1)
                    if (not in_images and rect_share >= 0.8
                            and any((reg & t).get_area() >= 0.6 * min(reg.get_area(), t.get_area()) for t in table_rects)):
                        skipped.append({"page_index": pno, "bbox": _rect_tuple(reg), "reason": "OVERLAPS_DETECTED_TABLE"})
                        continue  # find_tables also fires on histograms, so only rectangle-dominated regions count as tables
                    if not in_images and all(it[0] == "re" for p in in_paths for it in p["items"]):
                        skipped.append({"page_index": pno, "bbox": _rect_tuple(reg), "reason": "RECTANGLES_ONLY_TABLE_OR_BOX"})
                        continue
                    kept.append((reg, in_paths, in_images, None))
            page_figs = 0
            used_captions = set()
            for reg, in_paths, in_images, docling_cap in kept:
                cls, raster_frac = _classify_region(reg, in_paths, in_images)
                if docling_cap:
                    m_cap = CAPTION_RE.match(docling_cap)
                    cap_label = re.sub(r"\s+", " ", m_cap.group(1)).strip() if m_cap else ""
                    cap_text = docling_cap[:1200]
                    cap_page: int | None = pno
                    fnum = figure_number(cap_label) if cap_label else ""
                    for c in captions:
                        if (cap_label and c["label"].lower() == cap_label.lower()) or (fnum and figure_number(c["label"]) == fnum):
                            used_captions.add(c["label"] + str(c["rect"]))
                else:
                    cap = _pair_caption(reg, captions)
                    if cap:
                        used_captions.add(cap["label"] + str(cap["rect"]))
                        cap_label, cap_text, cap_page = cap["label"], cap["text"][:1200], pno
                    else:
                        cap_label, cap_text, cap_page = "", "", None
                page_figs += 1
                fid = f"{stem}_p{pno + 1:02d}_r{page_figs}"
                crop = (reg + (-CROP_PAD_PT, -CROP_PAD_PT, CROP_PAD_PT, CROP_PAD_PT)) & page.rect
                pix = page.get_pixmap(clip=crop, dpi=DPI)
                png = crops_dir / f"{fid}.png"
                pix.save(str(png))
                figures.append(FigureAsset(
                    figure_id=fid, source_pdf=str(pdf_path), document_role=document_role, page_index=pno, bbox=_rect_tuple(crop),
                    caption_label=cap_label, figure_number=figure_number(cap_label) if cap_label else "",
                    caption_page_index=cap_page,
                    panel=_panel_letter(reg, words), caption_text=cap_text, classification=cls,
                    n_vector_paths=len(in_paths), n_raster_images=len(in_images), raster_area_fraction=round(raster_frac, 4),
                    png_path=str(png), png_dpi=DPI, png_width_px=pix.width, png_height_px=pix.height, png_sha256=_sha256_file(png),
                    license_scope="article_level_unverified_for_third_party_figures" if license_scope != "unknown" else "unknown",
                ))
            for c in captions:
                if c["label"] + str(c["rect"]) not in used_captions and c["strong"]:
                    unpaired_captions.append({"page_index": pno, "label": c["label"], "bbox": [round(v, 2) for v in c["rect"]],
                                              "text": c["text"][:300], "reason": "NO_GRAPHIC_REGION_PAIRED_ON_PAGE",
                                              "_full_text": c["text"][:1200], "_page_has_figures": page_figs > 0})
            pages.append({"page_index": pno, "rotation": rotation, "n_vector_paths": len(paths), "n_raster_rects": len(images),
                          "n_caption_blocks": len(captions), "n_figure_regions": page_figs})
        page_count = doc.page_count
    finally:
        doc.close()
    figures, unpaired_captions = _pair_following_page_captions(figures, unpaired_captions)
    return {
        "pdf": str(pdf_path), "sha256": _sha256_file(pdf_path), "document_role": document_role, "page_count": page_count,
        "layout_source": "docling" if use_docling else "pymupdf",
        "pages_inspected": pages, "figures": figures, "unpaired_captions": unpaired_captions, "skipped_regions": skipped,
    }


# ============================================================================ vector digitization

def _segments(drawings: list[dict]) -> tuple[list[tuple], list[tuple]]:
    """Axis-aligned stroked segments: horizontals (x0, x1, y) and verticals (y0, y1, x)."""
    hs, vs = [], []
    for p in drawings:
        if "s" not in (p.get("type") or ""):
            continue
        for it in p["items"]:
            if it[0] == "l":
                a, b = it[1], it[2]
                if abs(a.y - b.y) <= 0.6 and abs(a.x - b.x) > 0.6:
                    hs.append((min(a.x, b.x), max(a.x, b.x), (a.y + b.y) / 2))
                elif abs(a.x - b.x) <= 0.6 and abs(a.y - b.y) > 0.6:
                    vs.append((min(a.y, b.y), max(a.y, b.y), (a.x + b.x) / 2))
            elif it[0] == "re":
                r = it[1]
                hs += [(r.x0, r.x1, r.y0), (r.x0, r.x1, r.y1)]
                vs += [(r.y0, r.y1, r.x0), (r.y0, r.y1, r.x1)]
    return hs, vs


def detect_panels(drawings: list[dict], clip) -> list[tuple[float, float, float, float]]:
    """Plot frames (x0, y0, x1, y1) from bottom-left corners of long horizontal + vertical strokes inside `clip`."""
    hs, vs = _segments(drawings)
    min_w, min_h = 35.0, 25.0
    long_h = [h for h in hs if h[1] - h[0] >= min_w and clip.y0 - 2 <= h[2] <= clip.y1 + 2 and h[0] >= clip.x0 - 2 and h[1] <= clip.x1 + 2]
    long_v = [v for v in vs if v[1] - v[0] >= min_h and clip.x0 - 2 <= v[2] <= clip.x1 + 2 and v[0] >= clip.y0 - 2 and v[1] <= clip.y1 + 2]
    panels: list[tuple[float, float, float, float]] = []
    for h in long_h:
        for v in long_v:
            if abs(v[2] - h[0]) <= 12 and abs(v[1] - h[2]) <= 12 and v[0] < h[2] - min_h * 0.5:
                cand = (min(v[2], h[0]), v[0], h[1], max(h[2], v[1]))
                if all(max(abs(a - b) for a, b in zip(cand, p)) > 2.5 for p in panels):
                    panels.append(cand)
    # keep the tightest frame per corner (a frame drawn as a rectangle also yields its outer edges)
    panels.sort(key=lambda p: (p[2] - p[0]) * (p[3] - p[1]))
    out: list[tuple[float, float, float, float]] = []
    for p in panels:
        if not any(abs(p[0] - q[0]) <= 2.5 and abs(p[3] - q[3]) <= 2.5 for q in out):
            out.append(p)
    return sorted(out, key=lambda p: (round(p[1]), p[0]))


def _tick_marks(drawings: list[dict], axis: str, line: float, lo: float, hi: float) -> list[float]:
    hs, vs = _segments(drawings)
    marks = []
    if axis == "x":
        for y0, y1, x in vs:
            if 1.5 <= y1 - y0 <= 12 and (abs(y0 - line) <= 1.6 or abs(y1 - line) <= 1.6) and lo - 1 <= x <= hi + 1:
                marks.append(x)
    else:
        for x0, x1, y in hs:
            if 1.5 <= x1 - x0 <= 12 and (abs(x0 - line) <= 1.6 or abs(x1 - line) <= 1.6) and lo - 1 <= y <= hi + 1:
                marks.append(y)
    return sorted(marks)


def _fit_line(pos: list[float], val: list[float]) -> tuple[float, float]:
    n = len(pos)
    mx, my = sum(pos) / n, sum(val) / n
    sxx = sum((p - mx) ** 2 for p in pos)
    if sxx == 0:
        raise ValueError("degenerate tick positions")
    slope = sum((p - mx) * (v - my) for p, v in zip(pos, val)) / sxx
    return slope, my - slope * mx


def fit_axis_calibration(axis: str, positions: list[float], values: list[float], max_residual_frac: float = 0.02) -> AxisCalibration | None:
    """Least-squares page->data map; tries linear then log10; drops one bad label when >=4 ticks; LOO error as blind check."""
    pairs = sorted({(round(p, 3), v) for p, v in zip(positions, values)})
    if len({v for _, v in pairs}) < 2 or len(pairs) < 2:
        return None

    def attempt(ps: list[float], vs: list[float], scale: str):
        tv = [math.log10(v) for v in vs] if scale == "log10" else vs
        slope, icpt = _fit_line(ps, tv)
        span = max(tv) - min(tv)
        if span <= 0 or slope == 0:
            return None
        resid = max(abs(slope * p + icpt - t) for p, t in zip(ps, tv)) / span
        return slope, icpt, resid, tv, span

    candidates = []
    subsets = [pairs] + ([[q for j, q in enumerate(pairs) if j != i] for i in range(len(pairs))] if len(pairs) >= 4 else [])
    for subset in subsets:
        ps, vs = [p for p, _ in subset], [v for _, v in subset]
        for scale in ("linear", "log10"):
            if scale == "log10" and min(vs) <= 0:
                continue
            got = attempt(ps, vs, scale)
            if got and got[2] <= max_residual_frac:
                candidates.append((len(subset) != len(pairs), got[2], scale, ps, vs, got))
        if candidates:
            break
    if not candidates:
        return None
    _dropped, resid, scale, ps, vs, (slope, icpt, _r, tv, span) = min(candidates, key=lambda c: (c[0], c[1]))
    loo = None
    if len(ps) >= 3:
        errs = []
        for i in range(len(ps)):
            rest_p = ps[:i] + ps[i + 1:]
            rest_t = tv[:i] + tv[i + 1:]
            s2, i2 = _fit_line(rest_p, rest_t)
            errs.append(abs(s2 * ps[i] + i2 - tv[i]) / span)
        loo = round(max(errs), 6)
    return AxisCalibration(axis=axis, scale=scale, slope=slope, intercept=icpt, tick_values=vs, tick_positions=ps,
                           max_residual_frac=round(resid, 6), loo_max_rel_error=loo)


def _axis_ticks(words: list[tuple], drawings: list[dict], panel: tuple, axis: str) -> tuple[list[float], list[float], int, int]:
    x0, y0, x1, y1 = panel
    pos, val, edge = [], [], []
    if axis == "x":
        marks = _tick_marks(drawings, "x", y1, x0, x1)
        for w in words:
            v = parse_numeric_label(w[4])
            cx = (w[0] + w[2]) / 2
            if v is not None and y1 - 2 <= w[1] <= y1 + 28 and x0 - 6 <= cx <= x1 + 6:
                pos.append(cx)
                val.append(v)
                edge.append(w[1])  # x tick labels share a top edge
    else:
        marks = _tick_marks(drawings, "y", x0, y0, y1)
        for w in words:
            v = parse_numeric_label(w[4])
            cy = (w[1] + w[3]) / 2
            if v is not None and x0 - 40 <= w[2] <= x0 + 1 and y0 - 6 <= cy <= y1 + 6:
                pos.append(cy)
                val.append(v)
                edge.append(w[2])  # y tick labels are right-aligned
    if edge:
        # keep the largest row/column of labels sharing one alignment edge; a neighbouring panel's labels sit elsewhere
        best = max(edge, key=lambda e: (sum(1 for f in edge if abs(f - e) <= 2.5), -abs(e - (y1 if axis == "x" else x0))))
        keep = [i for i, f in enumerate(edge) if abs(f - best) <= 2.5]
        pos, val = [pos[i] for i in keep], [val[i] for i in keep]
    snapped = 0
    for i, p in enumerate(pos):
        near = [m for m in marks if abs(m - p) <= 4.0]
        if near:
            pos[i] = min(near, key=lambda m: abs(m - p))
            snapped += 1
    return pos, val, snapped, len(marks)


def _subpaths(p: dict) -> list[dict]:
    """Split one drawing into connected subpaths; Illustrator-style figures pack a whole marker series into one path."""
    subs: list[dict] = []
    cur: dict | None = None
    for it in p["items"]:
        op = it[0]
        if op in ("re", "qu"):
            if cur:
                subs.append(cur)
                cur = None
            r = it[1] if op == "re" else it[1].rect
            corners = [(r.x0, r.y0), (r.x1, r.y0), (r.x1, r.y1), (r.x0, r.y1)]
            subs.append({"ops": [op], "pts": corners, "bbox_pts": corners, "closed": True})
            continue
        a, b = it[1], it[-1]
        if cur is None or math.dist(cur["pts"][-1], (a.x, a.y)) > 0.05:
            if cur:
                subs.append(cur)
            cur = {"ops": [], "pts": [(a.x, a.y)], "bbox_pts": [(a.x, a.y)], "closed": False}
        cur["ops"].append(op)
        cur["pts"].append((b.x, b.y))
        cur["bbox_pts"].extend([(q.x, q.y) for q in it[2:-1]] + [(b.x, b.y)])
    if cur:
        subs.append(cur)
    for sp in subs:
        xs = [q[0] for q in sp["bbox_pts"]]
        ys = [q[1] for q in sp["bbox_pts"]]
        sp["bbox"] = (min(xs), min(ys), max(xs), max(ys))
        if not sp["closed"]:
            sp["closed"] = len(sp["pts"]) > 2 and math.dist(sp["pts"][0], sp["pts"][-1]) < 0.3
    if len(subs) == 1 and p.get("closePath"):
        subs[0]["closed"] = True
    return subs


def _small_shape(bbox: tuple) -> bool:
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    return 0.8 <= w <= 14 and 0.8 <= h <= 14 and 0.4 <= (w + 1e-6) / (h + 1e-6) <= 2.5


def _seg_endpoints(seg: tuple) -> tuple[tuple[float, float], tuple[float, float]]:
    mid, ang, length = seg[0], seg[1], seg[2]
    rad = math.radians(ang)
    dx, dy = (length / 2.0) * math.cos(rad), (length / 2.0) * math.sin(rad)
    return (mid[0] - dx, mid[1] - dy), (mid[0] + dx, mid[1] + dy)


def _cross_markers(
    segments: list[tuple],
    *,
    extra_lines: list[tuple] | None = None,
    closed_shapes: list[tuple[tuple[float, float, float, float], str]] | None = None,
) -> list[tuple]:
    """'+' and 'x' markers: two short strokes of one colour sharing a midpoint at a wide angle.

    Rejects 2D error-bar intersections:
      - crossings centred on/inside a same-colour closed-shape marker (closed shapes take precedence);
      - stems whose endpoints both terminate at midpoints of perpendicular same-colour caps (I-beam stems);
      - caps whose midpoint terminates an unpaired/rejected perpendicular same-colour stem (T-junction caps).
    """
    by_cell: dict[tuple, list[int]] = defaultdict(list)
    for i, seg in enumerate(segments):
        by_cell[(round(seg[0][0] * 2), round(seg[0][1] * 2))].append(i)
    used: set[int] = set()
    pairs: list[tuple[int, int]] = []
    for i, (mid, ang, length, color) in enumerate(segments):
        if i in used:
            continue
        cx, cy = round(mid[0] * 2), round(mid[1] * 2)
        partner = None
        for j in (j for dx in (-1, 0, 1) for dy in (-1, 0, 1) for j in by_cell.get((cx + dx, cy + dy), ())):
            o = segments[j]
            if j == i or j in used or o[3] != color or math.dist(mid, o[0]) > 0.6:
                continue
            dang = abs(ang - o[1]) % 180
            if min(dang, 180 - dang) >= 60 and 0.6 <= length / max(o[2], 1e-6) <= 1.6:
                partner = j
                break
        if partner is not None:
            used.update((i, partner))
            pairs.append((i, partner))
    if not pairs:
        return []

    pool = list(segments) + list(extra_lines or ())
    endpoints = [_seg_endpoints(s) for s in pool]
    by_mid_cell: dict[tuple, list[int]] = defaultdict(list)
    by_ep_cell: dict[tuple, list[int]] = defaultdict(list)
    for idx, seg in enumerate(pool):
        mx, my = seg[0]
        by_mid_cell[(seg[3], round(mx), round(my))].append(idx)
        for ex, ey in endpoints[idx]:
            by_ep_cell[(seg[3], round(ex), round(ey))].append(idx)

    def _perp(a1: float, a2: float) -> bool:
        d = abs(a1 - a2) % 180
        return min(d, 180 - d) >= 60

    def _nearby(grid: dict[tuple, list[int]], color: str, pt: tuple[float, float]) -> Iterable[int]:
        gx, gy = round(pt[0]), round(pt[1])
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                yield from grid.get((color, gx + dx, gy + dy), ())

    shapes_by_color: dict[str, list[tuple[float, float, float, float]]] = defaultdict(list)
    for bb, col in (closed_shapes or ()):
        shapes_by_color[col].append(bb)

    rejected: set[int] = set()
    for pi, (i, j) in enumerate(pairs):
        s1, s2 = pool[i], pool[j]
        col = s1[3]
        cmid = ((s1[0][0] + s2[0][0]) / 2, (s1[0][1] + s2[0][1]) / 2)
        if any(bb[0] - 0.5 <= cmid[0] <= bb[2] + 0.5 and bb[1] - 0.5 <= cmid[1] <= bb[3] + 0.5 for bb in shapes_by_color.get(col, ())):
            rejected.add(pi)
            continue
        # Reject capped error-bar stems (both endpoints touch midpoints of perpendicular same-colour caps)
        for seg_idx in (i, j):
            seg = pool[seg_idx]
            ea, eb = endpoints[seg_idx]
            a_capped = any(k not in (i, j) and _perp(seg[1], pool[k][1]) and math.dist(ea, pool[k][0]) <= 0.35
                           for k in _nearby(by_mid_cell, col, ea))
            b_capped = any(k not in (i, j) and _perp(seg[1], pool[k][1]) and math.dist(eb, pool[k][0]) <= 0.35
                           for k in _nearby(by_mid_cell, col, eb))
            if a_capped and b_capped:
                rejected.add(pi)
                break

    # Iteratively reject caps touching endpoints of perpendicular unpaired/rejected error-bar stems
    clean_line_ids = {idx for pi, (i, j) in enumerate(pairs) if pi not in rejected for idx in (i, j)}
    changed = True
    while changed:
        changed = False
        for pi, (i, j) in enumerate(pairs):
            if pi in rejected:
                continue
            col = pool[i][3]
            for seg_idx in (i, j):
                seg = pool[seg_idx]
                if any(k not in clean_line_ids and _perp(seg[1], pool[k][1])
                       and min(math.dist(seg[0], endpoints[k][0]), math.dist(seg[0], endpoints[k][1])) <= 0.35
                       for k in _nearby(by_ep_cell, col, seg[0])):
                    rejected.add(pi)
                    clean_line_ids.discard(i)
                    clean_line_ids.discard(j)
                    changed = True
                    break

    out = []
    for pi, (i, j) in enumerate(pairs):
        if pi in rejected:
            continue
        s1, s2 = segments[i], segments[j]
        half = max(s1[2], s2[2]) / 2
        out.append(((s1[0][0] + s2[0][0]) / 2, (s1[0][1] + s2[0][1]) / 2, half, s1[3]))
    return out


def _digitize_panel(drawings: list[dict], words: list[tuple], panel: tuple, shared_x: AxisCalibration | None = None):
    import pymupdf

    x0, y0, x1, y1 = panel
    warnings: list[str] = []
    xp, xv, xs, xm = _axis_ticks(words, drawings, panel, "x")
    yp, yv, ys, ym = _axis_ticks(words, drawings, panel, "y")
    for name, n_labels, n_marks in (("X", len(xp), xm), ("Y", len(yp), ym)):
        if n_labels == 0 and n_marks >= 3:
            warnings.append(f"{name}_TICK_MARKS_WITHOUT_TEXT_LABELS:{n_marks}")  # labels drawn as outlined glyphs
    xcal = fit_axis_calibration("x", xp, xv) if len(xp) >= 2 else None
    ycal = fit_axis_calibration("y", yp, yv) if len(yp) >= 2 else None
    if xcal is None and shared_x is not None:
        xcal = shared_x
        warnings.append("X_CALIBRATION_SHARED_FROM_ALIGNED_PANEL")
    if xp and xs < len(xp):
        warnings.append(f"X_TICKS_UNSNAPPED:{len(xp) - xs}/{len(xp)}")
    if yp and ys < len(yp):
        warnings.append(f"Y_TICKS_UNSNAPPED:{len(yp) - ys}/{len(yp)}")
    zone = pymupdf.Rect(x0 - 3, y0 - 3, x1 + 3, y1 + 3)
    lines: list[tuple[str, list[tuple[float, float]]]] = []
    filled_segments = bars = 0
    candidates: list[tuple] = []  # (area, centre, colour, shape, bbox, ptype)
    short_strokes: list[tuple] = []  # (midpoint, angle_deg, length, colour)
    long_strokes: list[tuple] = []  # longer stems (>14 pt, non-spine) for error-bar T-junction detection

    def _in_panel_marker(pt: tuple[float, float], bb: tuple[float, float, float, float]) -> bool:
        return (x0 - 1.5 <= pt[0] <= x1 + 1.5 and y0 - 1.5 <= pt[1] <= y1 + 1.5
                and bb[2] >= x0 and bb[0] <= x1 and bb[3] >= y0 and bb[1] <= y1)

    max_span = max(x1 - x0, y1 - y0)
    for p in drawings:
        fill, ptype = p.get("fill"), p.get("type") or ""
        if ptype == "f" and fill and min(fill[:3]) > 0.98:
            continue  # axes background or white mask
        white_fill = bool(fill) and min(fill[:3]) > 0.98
        color = _color_hex(p.get("color") if (white_fill or not fill) and p.get("color") else fill)
        for sp in _subpaths(p):
            bx0, by0, bx1, by1 = sp["bbox"]
            c = ((bx0 + bx1) / 2, (by0 + by1) / 2)
            if not zone.contains(pymupdf.Point(*c)):
                continue
            ops = sp["ops"]
            w, h = bx1 - bx0, by1 - by0
            rect_like = ops == ["re"] or (set(ops) == {"l"} and len(ops) <= 5 and sp["closed"]
                                          and all(abs(a[0] - b[0]) < 0.3 or abs(a[1] - b[1]) < 0.3 for a, b in zip(sp["pts"], sp["pts"][1:])))
            if rect_like and abs(by1 - y1) <= 1.2 and by0 < y1 - 1 and w >= 0.8:
                bars += 1  # histogram or bar-chart rectangle standing on the x axis
                continue
            if ops == ["l"]:
                (ax, ay), (bx, by) = sp["pts"]
                length = math.dist((ax, ay), (bx, by))
                if length >= 0.8:
                    seg = (((ax + bx) / 2, (ay + by) / 2), math.degrees(math.atan2(by - ay, bx - ax)) % 180, length,
                           _color_hex(p.get("color") or fill))
                    if length <= 14:
                        short_strokes.append(seg)
                    elif length < 0.8 * max_span:
                        long_strokes.append(seg)
                continue  # lone strokes: ticks, error-bar stems and caps, axes, grid lines
            if _small_shape(sp["bbox"]) and (sp["closed"] or len(ops) >= 3) and _in_panel_marker(c, sp["bbox"]):
                candidates.append((w * h, c, color, f"{''.join(sorted(set(ops)))}{len(ops)}", sp["bbox"], ptype))
                continue
            if "s" in ptype and len(ops) >= 2 and w >= 0.15 * (x1 - x0):
                verts = sp["pts"]
                straight_h = all(abs(v[1] - verts[0][1]) < 0.6 for v in verts)
                straight_v = all(abs(v[0] - verts[0][0]) < 0.6 for v in verts)
                on_frame = sum(1 for v in verts if min(abs(v[0] - x0), abs(v[0] - x1)) <= 1.2 or min(abs(v[1] - y0), abs(v[1] - y1)) <= 1.2)
                if not (straight_h or straight_v or sp["closed"] or on_frame >= 0.8 * len(verts)):  # frames, boxes, axes
                    lines.append((_color_hex(p.get("color")), verts))
            elif ptype == "f" and set(ops) == {"l"} and len(ops) <= 6 and min(w, h) < 0.5 * max(w, h):
                filled_segments += 1
    closed_shapes = [(bb, col) for _a, _c, col, _sh, bb, _pt in candidates]
    for cx, cy, half, color in _cross_markers(short_strokes, extra_lines=long_strokes, closed_shapes=closed_shapes):
        cbb = (cx - half, cy - half, cx + half, cy + half)
        if _in_panel_marker((cx, cy), cbb):
            candidates.append(((2 * half) ** 2, (cx, cy), color, "cross", cbb, "cross"))
    if filled_segments:
        warnings.append(f"FILLED_LINE_SEGMENTS_IGNORED:{filled_segments}")
    if bars:
        warnings.append(f"BAR_RECTANGLES_IGNORED:{bars}")
    # one marker may be drawn as a fill plus outline pieces: fold smaller same-colour pieces or complementary
    # fill+stroke layers centred on a host, without collapsing distinct stacked identical markers or letting
    # inferred cross markers swallow closed shapes
    groups: dict[tuple, list[tuple[float, float]]] = defaultdict(list)
    half_size: dict[tuple, float] = {}
    accepted: list[tuple] = []
    for area, c, color, shape, bb, ptype in sorted(candidates, key=lambda t: (t[3] == "cross", -t[0])):
        host = next((
            a for a in accepted
            if a[2] == color
            and (a[3] != "cross" or shape == "cross")
            and a[4][0] - 0.01 <= c[0] <= a[4][2] + 0.01
            and a[4][1] - 0.01 <= c[1] <= a[4][3] + 0.01
            and (a[0] >= 1.2 * area or (math.dist(a[1], c) <= 0.3 and (a[5] != ptype or a[3] != shape)))
        ), None)
        if host is None:
            accepted.append((area, c, color, shape, bb, ptype))
            key = (color, shape, round(bb[2] - bb[0]), round(bb[3] - bb[1]))
            groups[key].append(c)
            half_size[key] = max(bb[2] - bb[0], bb[3] - bb[1]) / 2
    # legend entries: an isolated marker with a non-numeric word starting just to its right
    legend = set()
    for key, pts in groups.items():
        for c in pts:
            same_row = [p for p in pts if abs(p[1] - c[1]) <= 2.0]
            for w in words:
                horizontal = (w[2] - w[0]) >= 0.8 * (w[3] - w[1])
                gap = w[0] - c[0]
                if not (horizontal and w[0] < x1 and 0 <= gap <= 26 and abs((w[1] + w[3]) / 2 - c[1]) <= 4
                        and parse_numeric_label(w[4]) is None and len(w[4]) > 1):
                    continue
                if len(same_row) >= 3:
                    others_left = [c[0] - p[0] for p in same_row if p[0] < c[0] - 0.3]
                    has_right = any(p[0] > c[0] + 0.3 for p in same_row)
                    if has_right or (others_left and min(others_left) <= gap):
                        continue
                legend.add((key, c))
    if legend:
        warnings.append(f"LEGEND_MARKERS_EXCLUDED:{len(legend)}")
    series: list[tuple[str, str, list[tuple[float, float]], float]] = []
    for key, pts in groups.items():
        keep = [c for c in pts if (key, c) not in legend]
        if keep:
            series.append(("marker", key[0], sorted(keep), half_size[key]))
    for color, verts in lines:
        series.append(("polyline", color, verts, 0.0))
    return xcal, ycal, series, warnings


def _render_clip(page, clip, png_path: Path | None):
    pix = page.get_pixmap(clip=clip, dpi=DPI)
    if png_path is not None:
        png_path.parent.mkdir(parents=True, exist_ok=True)
        pix.save(str(png_path))
    return pix


def _pixel_alignment(pix, clip, probes: list[tuple[float, float, float]]) -> float | None:
    """Fraction of extracted points with rendered ink inside their own marker footprint (radius in pt).

    Open markers are white at the centre, so the probe covers the marker outline rather than one pixel.
    """
    import numpy as np

    if not probes:
        return None
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)[:, :, :3]
    sx, sy = pix.width / clip.width, pix.height / clip.height
    hits = 0
    for x, y, radius in probes:
        px, py = int(round((x - clip.x0) * sx)), int(round((y - clip.y0) * sy))
        r = max(1, int(round(radius * sx)))
        patch = img[max(0, py - r): py + r + 1, max(0, px - r): px + r + 1]
        if patch.size and (patch.min(axis=2) < 200).any():
            hits += 1
    return round(hits / len(probes), 4)


def render_overlay(pix, clip, page_points: list[tuple[float, float]], out_png: Path, ticks: list[tuple[float, float]] = ()) -> None:
    """Magenta circles at extracted points (and green crosses at calibration ticks) on the 300 DPI render."""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)[:, :, :3]
    sx, sy = pix.width / clip.width, pix.height / clip.height
    fig = plt.figure(figsize=(pix.width / 100, pix.height / 100), dpi=100)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.imshow(img, interpolation="nearest")
    if page_points:
        ax.scatter([(x - clip.x0) * sx for x, _ in page_points], [(y - clip.y0) * sy for _, y in page_points],
                   s=90, facecolors="none", edgecolors=MAGENTA, linewidths=1.6)
    if ticks:
        ax.scatter([(x - clip.x0) * sx for x, _ in ticks], [(y - clip.y0) * sy for _, y in ticks], s=60, marker="+", c="#00B050",
                   linewidths=1.4)
    ax.set_xlim(0, pix.width)
    ax.set_ylim(pix.height, 0)
    ax.axis("off")
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(str(out_png), dpi=100)
    plt.close(fig)


def extract_vector_panels(pdf_path: Path | str, page_index: int, clip_rect=None, out_dir: Path | str | None = None,
                          stem: str | None = None) -> list[PlotDigitizationResult]:
    """Digitize every detected panel in `clip_rect` (default: whole page); overlays/crops go to `out_dir/overlays` if given.

    Uncalibrated frames nested inside a calibrated panel (legend boxes, annotation boxes) are dropped.
    """
    import pymupdf

    doc, page = _open_page(pdf_path, page_index)
    clip = pymupdf.Rect(clip_rect) & page.rect if clip_rect is not None else page.rect
    drawings = [p for p in page.get_drawings() if _touches(p["rect"], clip)]
    words = page.get_text("words", clip=clip + (-45, -5, 45, 32))
    panels = detect_panels(drawings, clip)
    stem = stem or re.sub(r"[^A-Za-z0-9]+", "_", Path(pdf_path).stem).strip("_")
    raw = [(_digitize_panel(drawings, words, panel), panel) for panel in panels]
    for k, ((xcal, _ycal, _series, _warnings), panel) in enumerate(raw):
        if xcal is None:  # stacked panels often print x tick labels only under the bottom panel
            twin = next((r[0][0] for r in raw if r[0][0] is not None and abs(r[1][0] - panel[0]) <= 1.5 and abs(r[1][2] - panel[2]) <= 1.5), None)
            if twin is not None:
                raw[k] = (_digitize_panel(drawings, words, panel, shared_x=twin), panel)
    results = [_finish_result(page, pdf_path, page_index, panel, *dig, len(panels)) for dig, panel in raw]

    def inside(a, b) -> bool:
        return a is not b and a.frame and b.frame and a.frame[0] >= b.frame[0] - 1 and a.frame[1] >= b.frame[1] - 1 \
            and a.frame[2] <= b.frame[2] + 1 and a.frame[3] <= b.frame[3] + 1

    kept = [r for r in results if not (r.status == "ABSTAIN" and any(inside(r, o) for o in results if o.status == "OK"))]
    dropped = len(results) - len(kept)
    out = []
    for k, r in enumerate(kept):
        if dropped:
            r = r.model_copy(update={"warnings": r.warnings + [f"NESTED_UNCALIBRATED_FRAMES_DROPPED:{dropped}"],
                                     "panels_detected": len(kept)})
        if out_dir and r.status == "OK":
            r = _write_overlay(page, r, Path(out_dir) / "overlays" / f"{stem}_panel{k + 1}_overlay.png")
        out.append(r)
    doc.close()
    return out


def _finish_result(page, pdf_path, page_index, panel, xcal, ycal, series, warnings, n_panels) -> PlotDigitizationResult:
    import pymupdf

    pclip = pymupdf.Rect(panel[0] - 45, panel[1] - 12, panel[2] + 12, panel[3] + 32) & page.rect
    base = dict(source_pdf=str(pdf_path), page_index=page_index, clip=_rect_tuple(pclip), frame=tuple(round(v, 3) for v in panel),
                panels_detected=n_panels, warnings=warnings)
    if xcal is None or ycal is None:
        axes = ("x" if xcal is None else "") + ("y" if ycal is None else "")
        outlined = any("_TICK_MARKS_WITHOUT_TEXT_LABELS" in w for w in warnings)
        reason = "TICK_LABELS_NOT_TEXT_OUTLINED_GLYPHS" if outlined else "AXIS_CALIBRATION_FAILED"
        return PlotDigitizationResult(status="ABSTAIN", abstain_reason=f"{reason}:{axes}", **base)
    out_series, probes = [], []
    for kind, color, pts, half in series:
        probes.extend((x, y, half + 0.75) for x, y in pts)
        data = [(xcal.to_data(x), ycal.to_data(y)) for x, y in pts]
        out_series.append(DigitizedSeries(kind=kind, color=color, points=[(round(a, 6), round(b, 6)) for a, b in data],
                                          page_points=[(round(x, 3), round(y, 3)) for x, y in pts]))
    if not any(len(s.points) >= 2 for s in out_series):
        return PlotDigitizationResult(status="ABSTAIN", abstain_reason="NO_DATA_MARKS_FOUND", x_calibration=xcal, y_calibration=ycal, **base)
    pix = _render_clip(page, pclip, None)
    alignment = _pixel_alignment(pix, pclip, probes)
    return PlotDigitizationResult(status="OK", x_calibration=xcal, y_calibration=ycal, series=out_series,
                                  pixel_alignment_fraction=alignment, **base)


def _write_overlay(page, result: PlotDigitizationResult, overlay_path: Path) -> PlotDigitizationResult:
    """300 DPI crop + Matplotlib overlay (magenta circles = extracted points, green crosses = calibration ticks)."""
    import pymupdf

    clip = pymupdf.Rect(result.clip)
    name = overlay_path.name
    crop_path = overlay_path.with_name(name[: -len("_overlay.png")] + "_crop.png" if name.endswith("_overlay.png") else overlay_path.stem + "_crop.png")
    pix = _render_clip(page, clip, crop_path)
    fx0, _fy0, _fx1, fy1 = result.frame
    ticks = [(p, fy1) for p in result.x_calibration.tick_positions] + [(fx0, p) for p in result.y_calibration.tick_positions]
    render_overlay(pix, clip, [p for s in result.series for p in s.page_points], overlay_path, ticks)
    return result.model_copy(update={"overlay_png": str(overlay_path), "crop_png": str(crop_path)})


def extract_vector_xy_plot(pdf_path: Path | str, page_index: int, clip_rect=None, out_overlay_png: Path | str | None = None) -> PlotDigitizationResult:
    """Digitize the calibrated panel with the most points inside `clip_rect`; write a magenta overlay if requested."""
    import pymupdf

    results = extract_vector_panels(pdf_path, page_index, clip_rect)
    if not results:
        doc, page = _open_page(pdf_path, page_index)
        clip = pymupdf.Rect(clip_rect) & page.rect if clip_rect is not None else page.rect
        doc.close()
        return PlotDigitizationResult(source_pdf=str(pdf_path), page_index=page_index, clip=_rect_tuple(clip), status="ABSTAIN",
                                      abstain_reason="NO_AXIS_FRAME_FOUND")
    ok = [r for r in results if r.status == "OK"]
    best = max(ok, key=lambda r: r.n_points) if ok else results[0]
    if best.status == "OK" and out_overlay_png:
        doc, page = _open_page(pdf_path, page_index)
        best = _write_overlay(page, best, Path(out_overlay_png))
        doc.close()
    return best


# ============================================================================ blind printed-value gate

def verify_digitized_points(extracted_points: Iterable[tuple[float, float]], ground_truth_printed_values: Iterable[tuple[float, float]],
                            rel_tol: float = 0.05) -> dict[str, Any]:
    """One-to-one match (Hungarian) of extracted points to hidden printed values; pass only if every printed value is
    matched and every matched point is within `rel_tol` relative error on both coordinates.

    Relative error per coordinate is |extracted - printed| / max(|printed|, 1% of the printed range), so values at zero
    do not divide by zero.
    """
    import numpy as np
    from scipy.optimize import linear_sum_assignment

    ext = np.asarray(list(extracted_points), dtype=float).reshape(-1, 2)
    gt = np.asarray(list(ground_truth_printed_values), dtype=float).reshape(-1, 2)
    out: dict[str, Any] = {"n_ground_truth": int(len(gt)), "n_extracted": int(len(ext)), "rel_tol": rel_tol}
    if len(gt) == 0 or len(ext) == 0:
        out.update(n_matched=0, mae_x=None, mae_y=None, median_relative_error=None, max_relative_error=None, passed=False,
                   reason="EMPTY_INPUT")
        return out
    span = np.maximum(gt.max(axis=0) - gt.min(axis=0), 1e-12)
    floor = np.maximum(0.01 * span, 1e-12)
    cost = np.abs(gt[:, None, :] - ext[None, :, :]) / span
    cost = cost.max(axis=2)
    rows, cols = linear_sum_assignment(cost)
    matched = [(r, c) for r, c in zip(rows, cols) if cost[r, c] <= 0.10]
    if not matched:
        out.update(n_matched=0, mae_x=None, mae_y=None, median_relative_error=None, max_relative_error=None, passed=False,
                   reason="NO_POINT_WITHIN_10PCT_OF_RANGE")
        return out
    g = gt[[r for r, _ in matched]]
    e = ext[[c for _, c in matched]]
    abs_err = np.abs(e - g)
    rel = (abs_err / np.maximum(np.abs(g), floor)).max(axis=1)
    out.update(
        n_matched=len(matched),
        unmatched_ground_truth=int(len(gt) - len(matched)),
        extra_extracted=int(len(ext) - len(matched)),
        mae_x=float(abs_err[:, 0].mean()),
        mae_y=float(abs_err[:, 1].mean()),
        median_relative_error=float(np.median(rel)),
        max_relative_error=float(rel.max()),
    )
    out["passed"] = bool(len(matched) == len(gt) and out["max_relative_error"] < rel_tol)
    out["reason"] = "PASS" if out["passed"] else ("UNMATCHED_GROUND_TRUTH" if len(matched) < len(gt) else "RELATIVE_ERROR_ABOVE_TOL")
    return out


# ============================================================================ raster handoff

def export_webplotdigitizer_stub(png_path: Path | str, out_json: Path | str, result: PlotDigitizationResult | None = None,
                                 figure: FigureAsset | None = None) -> dict[str, Any]:
    """WebPlotDigitizer 4.x project JSON (XYAxes) for manual digitizing of a crop; pre-fills calibration if known."""
    calib, datasets = [], []
    if result is not None and result.x_calibration and result.y_calibration:
        sx = sy = DPI / 72.0
        cx0, cy0 = result.clip[0], result.clip[1]
        xc, yc = result.x_calibration, result.y_calibration
        x_axis_line, y_axis_line = result.frame[0], result.frame[3]  # left y-axis x, bottom x-axis y
        for pos, val in ((xc.tick_positions[0], xc.tick_values[0]), (xc.tick_positions[-1], xc.tick_values[-1])):
            calib.append({"px": (pos - cx0) * sx, "py": (y_axis_line - cy0) * sy, "dx": str(val), "dy": "0", "dz": None})
        for pos, val in ((yc.tick_positions[0], yc.tick_values[0]), (yc.tick_positions[-1], yc.tick_values[-1])):
            calib.append({"px": (x_axis_line - cx0) * sx, "py": (pos - cy0) * sy, "dx": "0", "dy": str(val), "dz": None})
        for k, s in enumerate(result.series):
            rgb = [int(s.color[i:i + 2], 16) for i in (1, 3, 5)] if s.color.startswith("#") else [255, 0, 255]
            datasets.append({"name": f"series_{k + 1}_{s.kind}", "axesName": "XY", "colorRGB": rgb + [255], "metadata": {},
                             "data": [{"x": (px - cx0) * sx, "y": (py - cy0) * sy, "value": [dx, dy]}
                                      for (px, py), (dx, dy) in zip(s.page_points, s.points)]})
    project = {
        "version": [4, 2],
        "axesColl": [{"name": "XY", "type": "XYAxes", "isLogX": bool(result and result.x_calibration and result.x_calibration.scale == "log10"),
                      "isLogY": bool(result and result.y_calibration and result.y_calibration.scale == "log10"), "noRotation": False,
                      "calibrationPoints": calib}],
        "datasetColl": datasets or [{"name": "Default Dataset", "axesName": "XY", "colorRGB": [200, 0, 0, 255], "metadata": {}, "data": []}],
        "measurementColl": [],
        "atlas_handoff": {
            "image_file": str(png_path),
            "image_dpi": DPI,
            "figure_id": figure.figure_id if figure else "",
            "caption_label": figure.caption_label if figure else "",
            "redistribution_permission": figure.redistribution_permission if figure else "UNKNOWN_RESTRICTED",
            "instructions": "Load image_file in WebPlotDigitizer, confirm or set the 4 XY calibration points, digitize each series, "
                            "then export CSV with series names. Calibration points are pre-filled only when vector ticks were fitted.",
        },
    }
    out_json = Path(out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(project, indent=2), encoding="utf-8")
    return project


VLM_OUTPUT_CONTRACT = {
    "panels": [{
        "panel": "letter or ''",
        "x_axis": {"label": "verbatim", "unit": "verbatim", "scale": "linear|log10", "tick_values": ["numbers as printed"]},
        "y_axis": {"label": "verbatim", "unit": "verbatim", "scale": "linear|log10", "tick_values": ["numbers as printed"]},
        "series": [{"legend_label": "verbatim or ''", "color": "name", "points": [["x", "y"]], "reading_precision": "half tick spacing or finer"}],
        "abstain_reason": "'' or why values cannot be read",
    }]
}


def build_vlm_figure_prompt(png_path: Path | str, caption_text: str = "", figure_label: str = "", *, quantity_hint: str = "",
                            model: str = "claude-opus-5-5", max_tokens: int = 4096) -> dict[str, Any]:
    """Claude Messages API request body (image + instructions) for a dense raster figure. Built only; never sent here."""
    data = base64.standard_b64encode(Path(png_path).read_bytes()).decode("ascii")
    instructions = "\n".join([
        f"Figure: {figure_label or 'unlabelled'}",
        f"Caption (verbatim): {caption_text[:1500]}" if caption_text else "Caption: not available",
        f"Quantity of interest: {quantity_hint}" if quantity_hint else "",
        "Read numbers only from what is drawn. Report each axis label, unit and printed tick values verbatim.",
        "For each series give the points you can read and the reading precision. Do not interpolate hidden points,",
        "do not infer values from the caption, and set abstain_reason when markers overlap or ticks are unreadable.",
        "Return one JSON object matching this contract and nothing else:",
        json.dumps(VLM_OUTPUT_CONTRACT),
    ])
    return {
        "request": {
            "model": model,
            "max_tokens": max_tokens,
            "system": "You digitize scientific plots for a curated NMR dynamics database. Precision and abstention beat coverage.",
            "messages": [{"role": "user", "content": [
                {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": data}},
                {"type": "text", "text": "\n".join(x for x in instructions.splitlines() if x)},
            ]}],
        },
        "atlas_meta": {"png_path": str(png_path), "png_sha256": hashlib.sha256(Path(png_path).read_bytes()).hexdigest(),
                       "status": "BUILT_NOT_SENT", "redistribution_permission": "UNKNOWN_RESTRICTED"},
    }


# ============================================================================ live run

def run_figures(specs: list[dict[str, Any]], out_dir: Path | str, *, max_digitize_per_pdf: int = 12,
                use_docling_layout: bool = False) -> dict[str, Any]:
    """Inventory + crops for each PDF, digitize vector regions, write figures_manifest.json. Returns the manifest."""
    import pymupdf

    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    sources, figures, digitizations, unpaired, skipped = [], [], [], [], []
    for spec in specs:
        inv = inventory_pdf_figures(spec["path"], out_dir, spec["document_role"], license_scope=spec.get("license_scope", "unknown"),
                                    stem=spec.get("stem"), use_docling_layout=use_docling_layout)
        for f in inv["figures"]:
            figures.append({"entry": spec.get("entry", ""), "doi": spec.get("doi", ""), **f.model_dump()})
        unpaired.extend({"entry": spec.get("entry", ""), "pdf": inv["pdf"], **u} for u in inv["unpaired_captions"])
        skipped.extend({"entry": spec.get("entry", ""), "pdf": inv["pdf"], **u} for u in inv["skipped_regions"])
        sources.append({k: inv[k] for k in ("pdf", "sha256", "document_role", "page_count", "pages_inspected")} | {"entry": spec.get("entry", ""), "doi": spec.get("doi", "")})
        attempted = 0
        for f in inv["figures"]:
            if f.classification == "RASTER_IMAGE" or attempted >= max_digitize_per_pdf:
                continue
            attempted += 1
            stem = f.figure_id
            for res in extract_vector_panels(spec["path"], f.page_index, pymupdf.Rect(f.bbox), out_dir, stem=stem):
                digitizations.append({"entry": spec.get("entry", ""), "figure_id": f.figure_id, "caption_label": f.caption_label,
                                      **res.model_dump()})
    manifest = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "tool": "atlas_pipeline.figures",
        "pymupdf_version": pymupdf.VersionBind,
        "dpi": DPI,
        "redistribution_note": "Every crop is UNKNOWN_RESTRICTED. Article-level licences are not per-figure permissions; "
                               "crops are for internal review previews only.",
        "sources": sources,
        "figures": figures,
        "unpaired_captions": unpaired,
        "skipped_regions": skipped,
        "digitizations": digitizations,
        "summary": {
            "n_pdfs": len(specs),
            "n_pages_inspected": sum(len(s["pages_inspected"]) for s in sources),
            "n_figure_regions": len(figures),
            "by_class": {c: sum(1 for f in figures if f["classification"] == c) for c in ("VECTOR_PLOT", "RASTER_IMAGE", "MIXED_VECTOR_RASTER")},
            "n_digitized_panels_ok": sum(1 for d in digitizations if d["status"] == "OK"),
            "n_overlays": sum(1 for d in digitizations if d["overlay_png"]),
        },
    }
    (out_dir / "figures_manifest.json").write_text(json.dumps(manifest, indent=2, default=str), encoding="utf-8")
    return manifest
