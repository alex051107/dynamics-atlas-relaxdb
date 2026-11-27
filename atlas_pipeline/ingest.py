"""Main-article and supplementary ingest: PMC JATS XML (lxml), Excel SI (openpyxl), PDF main/SI (PyMuPDF).

Every reader returns an `IngestedDocument` whose `text` is the exact string later used for grounding; block and table
character offsets index that string. Supplementary files keep `document_role="supplement_si"` and are never dropped.

Identity (shared, fail-closed; stricter than harvest_public_fulltexts.check_identity on the title fallback):
  * text after the first References/Bibliography heading that opens a citation list is removed first,
  * only the first 4,500 characters (front matter) may establish identity,
  * the remaining body must hold at least 1,500 non-whitespace characters,
  * the article DOI (or a >=7-character DOI suffix) in the front matter passes; otherwise >=80% of the expected
    title's words must appear in order there, and an empty or too-short expected title fails.
A main article that fails identity is returned with empty text so it cannot ground anything.
"""
from __future__ import annotations

import hashlib
import re
import unicodedata
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from .adapters import docling_extract_layout
from .schema import DocumentRole

FRONT_MATTER_CHARS = 4500
MIN_BODY_NONWS = 1500
REF_HEADING_RE = re.compile(
    r"(?:^|\n)\s*(?:\d+\.?\s+)?(?:references(?:\s+and\s+notes)?|bibliography|literature\s+cited|works\s+cited)\s*(?:\n|$)", re.I)
BIB_ENTRY_RE = re.compile(r"(?m)^\s*\[?\d{1,3}[.\])]?\s+[A-Z][^\n]{8,}|\(\d{4}\)|\b(?:19|20)\d{2};|\bet al\.|\bdoi\b", re.I)
CAPTION_RE = re.compile(r"^\s*((?:Supplementary\s+|Extended\s+Data\s+)?Fig(?:ure)?\.?\s*S?\d+[a-z]?)\b", re.I)
TABLE_CAPTION_RE = re.compile(r"^\s*((?:Supplementary\s+)?Table\s+S?\d+)\b", re.I)
TITLE_MIN_ORDERED_FRACTION = 0.8
TITLE_MAX_GAP_TOKENS = 3
FUNCTION_WORDS = {"a", "an", "the", "of", "and", "in", "on", "for", "to", "by", "with", "at", "from", "as", "is", "its", "via"}


class _M(BaseModel):
    model_config = ConfigDict(extra="forbid")


class IdentityVerdict(_M):
    ok: bool
    reason: str
    body_nonws: int = 0


class TextBlock(_M):
    page: int | None = None
    bbox: tuple[float, float, float, float] | None = None
    char_start: int
    char_end: int
    kind: Literal["text", "caption", "table_caption", "heading"] = "text"


class TableData(_M):
    table_id: str
    label: str = ""
    page: int | None = None
    sheet: str | None = None
    bbox: tuple[float, float, float, float] | None = None
    rows: list[list[str]]
    char_start: int = 0
    char_end: int = 0


class CaptionRef(_M):
    label: str
    text: str
    page: int | None = None
    bbox: tuple[float, float, float, float] | None = None


class IngestedDocument(_M):
    doc_id: str
    path: str
    format: Literal["jats_xml", "pdf", "xlsx"]
    reader: str
    document_role: DocumentRole
    doi: str = ""
    title: str = ""
    identity_ok: bool
    identity_reason: str
    text: str
    sha256: str
    pages: int = 0
    rotated_pages: list[int] = Field(default_factory=list)
    blocks: list[TextBlock] = Field(default_factory=list)
    tables: list[TableData] = Field(default_factory=list)
    figure_captions: list[CaptionRef] = Field(default_factory=list)
    si_references: list[str] = Field(default_factory=list)

    @property
    def usable(self) -> bool:
        return bool(self.text) and (self.identity_ok or self.document_role == "supplement_si")


def _norm_doi(doi: str | None) -> str:
    return re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", (doi or "").strip(), flags=re.I).lower()


def split_front_and_main(text: str) -> tuple[str, str]:
    """Cut at the first reference heading (beyond 400 chars) that is followed by bibliography-like lines.

    A bare "References" entry in an SI table of contents is not a cut point; a heading followed by numbered or
    author-year citations is. Bibliography DOIs therefore never reach the front-matter window.
    """
    raw = text or ""
    cut = len(raw)
    for m in REF_HEADING_RE.finditer(raw, 400):
        if len(BIB_ENTRY_RE.findall(raw[m.end(): m.end() + 1200])) >= 3:
            cut = m.start()
            break
    main = raw[:cut]
    return main[:FRONT_MATTER_CHARS], main


def _tokens(text: str) -> list[str]:
    flat = unicodedata.normalize("NFKC", text or "").lower()
    flat = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", flat)  # re-join words hyphenated across PDF lines
    return [t for t in re.findall(r"[a-z0-9]+", flat) if t not in FUNCTION_WORDS]


def _ordered_title_fraction(title_tokens: list[str], front_tokens: list[str]) -> float:
    """Best fraction of title tokens found in order in the front matter, with at most TITLE_MAX_GAP_TOKENS between hits."""
    if not title_tokens:
        return 0.0
    best = 0
    for start, tok in enumerate(front_tokens):
        if tok != title_tokens[0] and tok != title_tokens[min(1, len(title_tokens) - 1)]:
            continue
        hits, ti, fi, gap = 0, 0, start, 0
        while ti < len(title_tokens) and fi < len(front_tokens) and gap <= TITLE_MAX_GAP_TOKENS:
            if front_tokens[fi] == title_tokens[ti]:
                hits, ti, gap = hits + 1, ti + 1, 0
            elif ti + 1 < len(title_tokens) and front_tokens[fi] == title_tokens[ti + 1]:
                hits, ti, gap = hits + 1, ti + 2, 0  # one title word missing from the extracted text
            else:
                gap += 1
            fi += 1
        best = max(best, hits)
    return best / len(title_tokens)


def verify_document_identity(text: str, expected_doi: str, expected_title: str) -> IdentityVerdict:
    """Fail-closed identity: front-matter DOI, else the title found in order near the top. Topic-word overlap is not enough.

    The ordered-title rule replaces the bag-of-words rule from harvest_public_fulltexts.check_identity, which accepted
    Eisenmesser 2005 (CypA) as Henzler-Wildman 2007 (AdK) on 5/6 shared title words.
    """
    front, main = split_front_and_main(text)
    body_nonws = len(re.sub(r"\s+", "", main))
    if body_nonws < MIN_BODY_NONWS:
        return IdentityVerdict(ok=False, reason="body_too_short", body_nonws=body_nonws)
    front_low = front.lower()
    doi = _norm_doi(expected_doi)
    if doi and re.search(r"(?<![a-z0-9./])" + re.escape(doi) + r"(?![a-z0-9])", front_low):
        return IdentityVerdict(ok=True, reason="front_matter_doi_match", body_nonws=body_nonws)
    if "/" in doi:
        suffix = doi.split("/", 1)[1]
        if len(suffix) >= 7 and re.search(r"(?<![a-z0-9])" + re.escape(suffix) + r"(?![a-z0-9])", front_low):
            return IdentityVerdict(ok=True, reason="front_matter_doi_suffix_match", body_nonws=body_nonws)
    title_tokens = _tokens(expected_title)
    if len(title_tokens) < 3:
        return IdentityVerdict(ok=False, reason="no_title_and_no_front_matter_doi", body_nonws=body_nonws)
    frac = _ordered_title_fraction(title_tokens, _tokens(front))
    label = f"{round(frac * len(title_tokens))}/{len(title_tokens)}"
    if frac >= TITLE_MIN_ORDERED_FRACTION:
        return IdentityVerdict(ok=True, reason=f"front_matter_title_in_order_{label}", body_nonws=body_nonws)
    return IdentityVerdict(ok=False, reason=f"identity_mismatch_title_in_order_{label}", body_nonws=body_nonws)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class _TextBuilder:
    def __init__(self) -> None:
        self.parts: list[str] = []
        self.length = 0

    def add(self, chunk: str, sep: str = "\n\n") -> tuple[int, int]:
        if self.parts:
            self.parts.append(sep)
            self.length += len(sep)
        start = self.length
        self.parts.append(chunk)
        self.length += len(chunk)
        return start, self.length

    def text(self) -> str:
        return "".join(self.parts)


def _finalize(doc: IngestedDocument, identity: IdentityVerdict) -> IngestedDocument:
    doc.identity_ok, doc.identity_reason = identity.ok, identity.reason
    if not identity.ok and doc.document_role == "main_article":
        doc.text, doc.blocks, doc.tables = "", [], []  # fail closed: a wrong or empty paper grounds nothing
    elif not identity.ok:
        doc.identity_reason = f"si_identity_unverified:{identity.reason}"
    return doc


# ----------------------------------------------------------------------------- JATS XML

def ingest_jats(path: Path, expected_doi: str, expected_title: str = "", document_role: DocumentRole = "main_article") -> IngestedDocument:
    from lxml import etree

    path = Path(path)
    parser = etree.XMLParser(resolve_entities=False, no_network=True, load_dtd=False, huge_tree=True, recover=False)
    root = etree.parse(str(path), parser).getroot()

    def local(el) -> str:
        return etree.QName(el).localname if isinstance(el.tag, str) else ""

    def text_of(el) -> str:
        return re.sub(r"\s+", " ", "".join(el.itertext())).strip()

    meta = next((el for el in root.iter() if local(el) == "article-meta"), None)
    doc_doi = ""
    title = ""
    if meta is not None:
        for el in meta.iter():
            if local(el) == "article-id" and (el.get("pub-id-type") or "").lower() == "doi" and not doc_doi:
                doc_doi = _norm_doi(text_of(el))
            if local(el) == "article-title" and not title:
                title = text_of(el)
    body = next((el for el in root.iter() if local(el) == "body"), None)
    doc = IngestedDocument(
        doc_id=f"{document_role}:{path.name}", path=str(path), format="jats_xml", reader="lxml", document_role=document_role,
        doi=doc_doi, title=title, identity_ok=False, identity_reason="pending", text="", sha256=_sha256(path),
    )
    if body is None:
        return _finalize(doc, IdentityVerdict(ok=False, reason="jats_without_body"))
    if not doc_doi or doc_doi != _norm_doi(expected_doi):
        return _finalize(doc, IdentityVerdict(ok=False, reason=f"jats_article_doi_mismatch:{doc_doi or 'missing'}"))

    tb = _TextBuilder()
    if title:
        s, e = tb.add(title)
        doc.blocks.append(TextBlock(char_start=s, char_end=e, kind="heading"))
    tb.add(f"DOI: {doc_doi}", sep="\n")
    abstract = next((el for el in meta.iter() if local(el) == "abstract"), None) if meta is not None else None
    if abstract is not None:
        s, e = tb.add(text_of(abstract))
        doc.blocks.append(TextBlock(char_start=s, char_end=e))
    skip = {"table-wrap", "fig", "ref-list", "supplementary-material"}

    def walk(el) -> None:
        name = local(el)
        if name in skip:
            return
        if name == "title":
            s, e = tb.add(text_of(el))
            doc.blocks.append(TextBlock(char_start=s, char_end=e, kind="heading"))
            return
        if name == "p":
            s, e = tb.add(text_of(el))
            doc.blocks.append(TextBlock(char_start=s, char_end=e))
            return
        for child in el:
            walk(child)

    walk(body)
    for el in body.iter():
        name = local(el)
        if name == "fig":
            label = next((text_of(c) for c in el if local(c) == "label"), "")
            cap = next((text_of(c) for c in el if local(c) == "caption"), "")
            s, e = tb.add(f"{label}. {cap}".strip(". "))
            doc.blocks.append(TextBlock(char_start=s, char_end=e, kind="caption"))
            doc.figure_captions.append(CaptionRef(label=label, text=cap))
        elif name == "table-wrap":
            label = next((text_of(c) for c in el if local(c) == "label"), "")
            cap = next((text_of(c) for c in el if local(c) == "caption"), "")
            rows = [[text_of(cell) for cell in tr if local(cell) in {"td", "th"}] for tr in el.iter() if local(tr) == "tr"]
            s, e = tb.add("\n".join([f"{label}. {cap}".strip(". ")] + [" | ".join(r) for r in rows]))
            doc.tables.append(TableData(table_id=f"T{len(doc.tables) + 1}", label=label, rows=rows, char_start=s, char_end=e))
        elif name == "supplementary-material":
            href = next((v for k, v in el.attrib.items() if k.endswith("href")), "")
            label = next((text_of(c) for c in el if local(c) == "label"), "")
            doc.si_references.append(href or label or "supplementary-material")
    doc.text = tb.text()
    identity = verify_document_identity(doc.text, expected_doi, expected_title or title)
    return _finalize(doc, identity)


# ----------------------------------------------------------------------------- PDF (main or SI)

def ingest_pdf(path: Path, expected_doi: str, expected_title: str = "", document_role: DocumentRole = "main_article",
               *, extract_tables: bool = True, use_docling: bool = False) -> IngestedDocument:
    import pymupdf

    path = Path(path)
    pdf = pymupdf.open(str(path))
    doc = IngestedDocument(
        doc_id=f"{document_role}:{path.name}", path=str(path), format="pdf", reader="pymupdf", document_role=document_role,
        doi=_norm_doi(expected_doi), title=expected_title, identity_ok=False, identity_reason="pending", text="",
        sha256=_sha256(path), pages=pdf.page_count,
    )
    tb = _TextBuilder()
    pending_tables: list[tuple[int, object, str]] = []
    docling_layout = docling_extract_layout(path) if (extract_tables and use_docling) else None
    docling_tables = (docling_layout or {}).get("tables") or []
    for pno, page in enumerate(pdf):
        if page.rotation:
            doc.rotated_pages.append(pno)
            page.remove_rotation()  # in-memory only; coordinates and text become upright
        for x0, y0, x1, y1, btext, _bno, btype in page.get_text("blocks"):
            if btype != 0 or not btext.strip():
                continue
            chunk = btext.strip()
            s, e = tb.add(chunk)
            kind = "caption" if CAPTION_RE.match(chunk) else "table_caption" if TABLE_CAPTION_RE.match(chunk) else "text"
            doc.blocks.append(TextBlock(page=pno, bbox=(x0, y0, x1, y1), char_start=s, char_end=e, kind=kind))
            if kind == "caption":
                doc.figure_captions.append(CaptionRef(label=CAPTION_RE.match(chunk).group(1), text=chunk[:600], page=pno,
                                                      bbox=(x0, y0, x1, y1)))
        if extract_tables and not docling_tables:
            try:
                found = page.find_tables()
                if not (found and found.tables):
                    found = page.find_tables(vertical_strategy="text", horizontal_strategy="text")
            except Exception:  # noqa: BLE001 - a table-finder failure must not drop the page text
                found = None
            for tab in (found.tables if found else []):
                caption = next((b for b in reversed(doc.blocks) if b.page == pno and b.kind == "table_caption"
                                and b.bbox and b.bbox[3] <= tab.bbox[1] + 2), None)
                label = TABLE_CAPTION_RE.match(tb.text()[caption.char_start:caption.char_end]).group(1) if caption else ""
                pending_tables.append((pno, tab, label))
    page_text = tb.text()
    if docling_tables:
        doc.reader = "pymupdf+docling_tables"
        for dt in docling_tables:
            pno = int(dt["page_index"])
            rows = dt["rows"]
            cap = dt.get("caption") or ""
            m_lbl = TABLE_CAPTION_RE.match(cap)
            label = m_lbl.group(1) if m_lbl else ""
            header_tag = f"[{label or 'Table'} | page {pno + 1} | Docling]"
            lines = [header_tag] + ([cap] if cap else []) + [" | ".join(r) for r in rows]
            s, e = tb.add("\n".join(lines))
            doc.tables.append(TableData(table_id=f"T{len(doc.tables) + 1}", label=label, page=pno,
                                        bbox=tuple(dt["bbox"]) if dt.get("bbox") else None, rows=rows,
                                        char_start=s, char_end=e))
    else:
        for pno, tab, label in pending_tables:
            rows = [[re.sub(r"\s+", " ", c or "").strip() for c in row] for row in tab.extract()]
            rows = [r for r in rows if any(r)]
            if not rows:
                continue
            s, e = tb.add("\n".join([f"[{label or 'Table'} | page {pno + 1} | PyMuPDF find_tables]"] + [" | ".join(r) for r in rows]))
            doc.tables.append(TableData(table_id=f"T{len(doc.tables) + 1}", label=label, page=pno, bbox=tuple(tab.bbox), rows=rows,
                                        char_start=s, char_end=e))
    doc.text = tb.text()
    identity = verify_document_identity(page_text, expected_doi, expected_title)
    return _finalize(doc, identity)


# ----------------------------------------------------------------------------- Excel SI

def ingest_xlsx(path: Path, parent_doi: str, document_role: DocumentRole = "supplement_si") -> IngestedDocument:
    from openpyxl import load_workbook

    path = Path(path)
    wb = load_workbook(str(path), read_only=True, data_only=True)
    doc = IngestedDocument(
        doc_id=f"{document_role}:{path.name}", path=str(path), format="xlsx", reader="openpyxl", document_role=document_role,
        doi=_norm_doi(parent_doi), identity_ok=False, identity_reason="pending", text="", sha256=_sha256(path),
    )
    tb = _TextBuilder()
    try:
        for ws in wb.worksheets:
            rows = []
            for row in ws.iter_rows(values_only=True):
                cells = ["" if v is None else str(v).strip() for v in row]
                while cells and not cells[-1]:
                    cells.pop()
                if any(cells):
                    rows.append(cells)
            if not rows:
                continue
            s, e = tb.add("\n".join([f"[Sheet: {ws.title}]"] + [" | ".join(r) for r in rows]))
            doc.tables.append(TableData(table_id=f"T{len(doc.tables) + 1}", label=ws.title, sheet=ws.title, rows=rows,
                                        char_start=s, char_end=e))
    finally:
        wb.close()
    doc.text = tb.text()
    doc.identity_ok = False
    doc.identity_reason = "xlsx_has_no_front_matter:identity_inherited_from_manifest"
    if document_role == "main_article":
        doc.text, doc.tables = "", []
    return doc


def ingest_any(path: Path, expected_doi: str, expected_title: str = "", document_role: DocumentRole = "main_article") -> IngestedDocument:
    suffix = Path(path).suffix.lower()
    if suffix in {".xml", ".nxml"}:
        return ingest_jats(path, expected_doi, expected_title, document_role)
    if suffix == ".pdf":
        return ingest_pdf(path, expected_doi, expected_title, document_role)
    if suffix in {".xlsx", ".xlsm"}:
        return ingest_xlsx(path, expected_doi, document_role)
    raise ValueError(f"unsupported source format: {path}")


def ingest_bundle(main_path: Path, si_paths: list[Path], expected_doi: str, expected_title: str = "") -> list[IngestedDocument]:
    """Main article plus every supplementary file; the SI list is returned in full even when a file fails identity."""
    docs = [ingest_any(main_path, expected_doi, expected_title, "main_article")]
    docs.extend(ingest_any(p, expected_doi, expected_title, "supplement_si") for p in si_paths)
    return docs
