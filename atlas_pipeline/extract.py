"""Layer 3 structured extraction runner (Anthropic SDK native structured outputs + local Claude CLI + swarm direct path).

Turns ingested main + SI text (and cropped raster figures) into validated, verbatim-grounded PaperRecord objects:
  - Primary backend (`anthropic_sdk`): uses `anthropic.Anthropic().messages.parse(..., output_format=...)` when
    ANTHROPIC_API_KEY is set, plus `build_batch_request()` for Anthropic Message Batches API (>20 papers).
  - Local sanctioned backend (`claude_cli`): when ANTHROPIC_API_KEY is absent, invokes the authenticated local
    `claude -p --output-format json --json-schema ...` CLI so extraction runs live with zero extra key setup.
  - Direct swarm-agent path (`swarm_agent_direct` via `load_and_ground_payload()`): when neither external API key
    nor live Claude CLI OAuth session is available, feeds a structured `_RawExtractionPayload` produced by direct
    agent reading through the exact same `_validate_and_ground()` + `verify_grounding()` + Pydantic physical gates,
    with explicit, auditable backend and auth diagnostics recorded in every output summary.

Every extracted row is validated individually against Pydantic physical rules AND `verify_grounding(source_text)`.
Rows failing physical validation or verbatim grounding are quarantined into `rejected_rows` with explicit codes.
"""
from __future__ import annotations

import base64
import json
import os
import re
import shutil
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field, ValidationError

from .figures import VLM_OUTPUT_CONTRACT
from .ingest import IngestedDocument, split_front_and_main
from .schema import (
    ACTIVE_PROMPT_PATH,
    AlternateStatePDB,
    DocumentRole,
    MeasurementRow,
    PaperRecord,
    PhysicalValidationError,
    QualitativeObservation,
    SampleSpec,
    Stance,
    canonical_prompt_rules,
    export_active_prompt,
)

DEFAULT_SDK_MODEL = "claude-sonnet-4-6"
DEFAULT_CLI_MODEL = "sonnet"
CLAUDE_BIN = shutil.which("claude") or str(Path.home() / ".local/bin/claude")
MAX_DOC_CHARS = 55_000

_VALID_STANCES = frozenset({"supports", "no_dynamics_in_window", "unclear", "artefact_suspected"})
_VALID_SOURCE_ROLES = frozenset({"this_study", "cited_prior_work", "uncertain"})
_VALID_MODALITIES = frozenset({"text", "table", "si_table", "figure_vector", "figure_raster", "figure_caption"})
_VALID_DOC_ROLES = frozenset({"main_article", "supplement_si"})
_ENTITY_ALIASES = {
    "conformational_exchange": "conformational_exchange",
    "conformational_state": "conformational_exchange",
    "oligomer_or_association": "oligomer_or_association",
    "other": "other",
    "bulk_relaxation": "other",
    "unknown": "unknown",
}
_SAMPLE_KEY_ALIASES = {
    "construct": "construct_label",
    "pH": "ph",
    "temperature": "temperature_raw",
    "field_mhz": "field_mhz_raw",
    "notes": "note",
}
_ALT_STATE_KEY_ALIASES = {
    "state_description": "state_label",
    "state": "state_label",
}


class _RawSample(BaseModel):
    """Permissive wire schema for SampleSpec so one contradictory sample is quarantined instead of aborting."""
    sample_id: str = ""
    uniprot_accession: str | None = None
    isoform_version: str | None = None
    construct_label: str = ""
    species_relation: str = "unknown"
    same_as_deposit: str = "unclear"
    ligand_state: str = ""
    temperature_raw: str = ""
    ph: str = ""
    buffer: str = ""
    field_mhz_raw: str = ""
    note: str = ""
    quote: str = ""


class _RawQualitativeObservation(BaseModel):
    """Permissive wire schema for non-numeric qualitative observations (regions, states, cryptic pockets)."""
    obs_id: str = ""
    sample_id: str = "S1"
    document_role: str = "main_article"
    category: str = "dynamic_region"
    evidence_level: str = "experimental"
    residues_raw: str = ""
    pdb_ids: list[str] = Field(default_factory=list)
    summary: str
    locator: str = ""
    quote: str


class _RawAlternateState(BaseModel):
    """Permissive wire schema for AlternateStatePDB."""
    pdb_id: str = ""
    state_label: str = ""
    relation: str = "unknown"
    ligand: str = ""
    source_role: str = "this_study"
    quote: str = ""


class _RawMeasurement(BaseModel):
    """Permissive wire schema so one bad row is quarantined instead of aborting the whole paper."""
    row_id: str = ""
    sample_id: str = "S1"
    quantity: str
    value_raw: str
    value_num: float | None = None
    unit_raw: str = ""
    uncertainty_raw: str = ""
    residues_raw: str = ""
    method: str = ""
    source_role: str = "this_study"
    evidence_modality: str = "text"
    measured_entity: str = "unknown"
    document_role: str = "main_article"
    locator: str = ""
    quote: str


class _RawExtractionPayload(BaseModel):
    stance: Stance = "supports"
    notes: str = ""
    samples: list[_RawSample] = Field(default_factory=list)
    measurements: list[_RawMeasurement] = Field(default_factory=list)
    qualitative_observations: list[_RawQualitativeObservation] = Field(default_factory=list)
    alternate_states: list[_RawAlternateState] = Field(default_factory=list)


def auth_status(*, check_cli: bool = True) -> dict[str, str]:
    """Report current authentication state of Anthropic SDK and local Claude CLI without reading key files."""
    sdk_state = "SET" if os.environ.get("ANTHROPIC_API_KEY") else "UNSET_ANTHROPIC_API_KEY"
    cli_state = "NOT_CHECKED"
    if check_cli:
        if not Path(CLAUDE_BIN).is_file() and shutil.which("claude") is None:
            cli_state = "CLI_NOT_FOUND"
        else:
            try:
                proc = subprocess.run([CLAUDE_BIN, "auth", "status"], capture_output=True, text=True, timeout=10)
                info = json.loads(proc.stdout) if proc.stdout.strip().startswith("{") else {}
                cli_state = "AUTHENTICATED" if info.get("loggedIn") is True else "OAUTH_EXPIRED_REAUTH_NEEDED"
            except Exception:  # noqa: BLE001
                cli_state = "OAUTH_EXPIRED_REAUTH_NEEDED"
    return {"anthropic_sdk_auth": sdk_state, "claude_cli_auth": cli_state}


@dataclass
class ExtractionRunResult:
    record: PaperRecord
    rejected_rows: list[dict[str, Any]] = field(default_factory=list)
    rejected_samples: list[dict[str, Any]] = field(default_factory=list)
    backend: str = ""
    model: str = ""
    elapsed_s: float = 0.0
    usage: dict[str, Any] = field(default_factory=dict)
    auth: dict[str, str] = field(default_factory=dict)

    def summary(self) -> dict[str, Any]:
        out = {
            "entry": self.record.entry,
            "doi": self.record.doi,
            "backend": self.backend,
            "model": self.model,
            "elapsed_s": round(self.elapsed_s, 2),
            "stance": self.record.stance,
            "n_samples_accepted": len(self.record.samples),
            "n_samples_rejected": len(self.rejected_samples),
            "n_measurements_accepted": len(self.record.measurements),
            "n_measurements_primary": len(self.record.primary_measurements()),
            "n_measurements_rejected": len(self.rejected_rows),
            "n_qualitative_accepted": len(self.record.qualitative_observations),
            "n_alternate_states": len(self.record.alternate_states),
            "rejected_reasons": [r.get("reason") for r in self.rejected_rows[:12]],
            "usage": self.usage,
        }
        if self.auth:
            out.update(self.auth)
        return out


def _strip_references_for_prompt(text: str, *, is_supplement: bool = False) -> str:
    """Keep full body while trimming trailing bibliography in main articles (never cutting SI tables/methods)."""
    if is_supplement:
        return text
    _, main = split_front_and_main(text)
    return main


def canonical_system_prompt() -> str:
    """Single canonical system prompt consumed by SDK, Claude CLI, and Message Batches API (never truncated)."""
    return (
        "You extract structured protein conformational dynamics measurements and qualitative observations for "
        "Dynamics Atlas. Precision, verbatim quotes, and sample/condition attribution strictly beat guessing.\n\n"
        + canonical_prompt_rules()
    )


def _format_prompt_input(entry: str, doi: str, title: str, docs: dict[DocumentRole, IngestedDocument]) -> str:
    parts = [
        f"Target entry: {entry}",
        f"Paper DOI: {doi}",
        f"Paper title: {title or '(see text)'}",
        "",
        "Follow the canonical extraction rules in the system prompt. Keep exact printed characters (including OCR"
        " tokens like s21 or uC) inside `quote`. For large per-residue SI tables (>20 rows), extract all global/group"
        " fitted rates and populations first plus representative per-residue rows spanning the reported range.",
        "",
    ]
    for role in ("main_article", "supplement_si"):
        doc = docs.get(role)
        if doc is None or not doc.text:
            continue
        budget = MAX_DOC_CHARS
        tables_start = min((t.char_start for t in doc.tables if t.char_start > 0), default=len(doc.text))
        raw_body = doc.text[:tables_start]
        raw_tables = doc.text[tables_start:]
        # Preserve Docling / XML / Excel tables unconditionally; skip huge PyMuPDF full-page text-strategy duplicates.
        keep_tables = bool(raw_tables) and (
            doc.reader == "pymupdf+docling_tables"
            or doc.format in {"jats_xml", "xlsx"}
            or len(raw_tables) <= 15_000
        )
        tables_tail = raw_tables if keep_tables else ""
        body = _strip_references_for_prompt(raw_body, is_supplement=(role == "supplement_si"))
        if tables_tail:
            if len(body) + len(tables_tail) + 2 <= budget:
                combined = f"{body}\n\n{tables_tail}"
            else:
                table_alloc = min(len(tables_tail), max(8_000, budget - 8_000))
                keep_main = max(4_000, budget - table_alloc - 40)
                combined = body[:keep_main] + "\n...[middle truncated]...\n" + tables_tail[:table_alloc]
        else:
            combined = body[:budget]
        parts.append(f"=== DOCUMENT ROLE: {role} ({doc.doc_id}) ===")
        parts.append(combined)
        parts.append("")
    return "\n".join(parts)


def _locate_quote_in_texts(quote: str, preferred_role: str, texts: dict[str, str]) -> tuple[str | None, int | None, int | None, str]:
    """Find exact verbatim span; if whitespace/newline differs slightly, slice the exact substring from source_text."""
    if not quote or not quote.strip():
        return None, None, None, quote
    order = [preferred_role] + [r for r in texts if r != preferred_role]
    for role in order:
        src = texts.get(role, "")
        if not src:
            continue
        idx = src.find(quote)
        if idx >= 0:
            return role, idx, idx + len(quote), quote
    # Whitespace-tolerant anchor: map regex of quote tokens back onto exact source slice (never fabricates text)
    tokens = [t for t in re.split(r"\s+", quote.strip()) if t]
    if len(tokens) >= 3:
        pat = re.compile(r"\s+".join(re.escape(t) for t in tokens))
        for role in order:
            src = texts.get(role, "")
            if not src:
                continue
            m = pat.search(src)
            if m:
                return role, m.start(), m.end(), src[m.start():m.end()]
    return None, None, None, quote


def _short_validation_reason(exc: Exception) -> str:
    if isinstance(exc, ValidationError) and exc.errors():
        msgs = [str(e.get("msg") or "") for e in exc.errors()[:2] if e.get("msg")]
        if msgs:
            return "; ".join(msgs)[:240]
    return str(exc).splitlines()[0][:240]


def _normalize_sample_dict(s_raw: Any, idx: int) -> dict[str, Any]:
    raw_d = s_raw.model_dump() if isinstance(s_raw, BaseModel) else dict(s_raw)
    for alias, target in _SAMPLE_KEY_ALIASES.items():
        if alias in raw_d and not raw_d.get(target):
            raw_d[target] = raw_d.pop(alias)
        elif alias in raw_d:
            raw_d.pop(alias)
    valid_fields = set(SampleSpec.model_fields)
    cleaned = {k: v for k, v in raw_d.items() if k in valid_fields}
    if not str(cleaned.get("sample_id") or "").strip():
        cleaned["sample_id"] = f"S{idx + 1}"
    if not str(cleaned.get("construct_label") or "").strip():
        cleaned["construct_label"] = "not stated"
    return cleaned


def _validate_and_ground(
    entry: str,
    doi: str,
    title: str,
    raw: _RawExtractionPayload,
    docs: dict[DocumentRole, IngestedDocument],
) -> tuple[PaperRecord, list[dict[str, Any]], list[dict[str, Any]]]:
    texts = {role: doc.text for role, doc in docs.items() if doc and doc.text}
    accepted_samples: list[SampleSpec] = []
    rejected_samples: list[dict[str, Any]] = []
    seen_sids: set[str] = set()
    rejected_sids: set[str] = set()
    for i, s_raw in enumerate(raw.samples):
        if not isinstance(s_raw, (dict, BaseModel)):
            continue
        s_dict = _normalize_sample_dict(s_raw, i)
        if s_dict["sample_id"] in seen_sids:
            continue
        try:
            sp = SampleSpec.model_validate(s_dict)
            accepted_samples.append(sp)
            seen_sids.add(sp.sample_id)
        except (ValidationError, PhysicalValidationError, ValueError) as exc:
            rejected_sids.add(str(s_dict.get("sample_id") or ""))
            rejected_samples.append({"sample": s_dict, "reason": _short_validation_reason(exc)})

    used_default_sample = False
    if not accepted_samples and not rejected_samples:
        accepted_samples.append(SampleSpec(sample_id="S1", construct_label="not stated"))
        seen_sids.add("S1")
        used_default_sample = True

    accepted_rows: list[MeasurementRow] = []
    rejected_rows: list[dict[str, Any]] = []
    seen_rids: set[str] = set()
    for i, m in enumerate(raw.measurements):
        rid = m.row_id.strip() or f"M{i + 1}"
        while rid in seen_rids:
            rid = f"{rid}_{i + 1}"
        raw_sid = (m.sample_id or "").strip()
        if raw_sid in rejected_sids:
            rejected_rows.append({"row_id": rid, "quantity": m.quantity, "value_raw": m.value_raw,
                                  "unit_raw": m.unit_raw, "reason": f"REJECTED_SAMPLE_REF:{raw_sid}"})
            continue
        elif raw_sid in seen_sids:
            sid = raw_sid
        elif raw_sid == "unknown":
            sid = "unknown"
        elif used_default_sample or (not raw_sid and len(accepted_samples) == 1):
            sid = accepted_samples[0].sample_id
        else:
            rejected_rows.append({"row_id": rid, "quantity": m.quantity, "value_raw": m.value_raw,
                                  "unit_raw": m.unit_raw, "reason": f"UNKNOWN_SAMPLE_ID:{raw_sid}"})
            continue

        pref_role = m.document_role if m.document_role in texts else next(iter(texts), "main_article")
        matched_role, cs, ce, exact_quote = _locate_quote_in_texts(m.quote, pref_role, texts)
        doc_role = matched_role or pref_role
        payload = {
            "row_id": rid,
            "sample_id": sid,
            "quantity": m.quantity,
            "value_raw": m.value_raw,
            "value_num": m.value_num,
            "unit_raw": m.unit_raw,
            "uncertainty_raw": m.uncertainty_raw,
            "residues_raw": m.residues_raw,
            "method": m.method,
            "source_role": m.source_role if m.source_role in _VALID_SOURCE_ROLES else "this_study",
            "evidence_modality": m.evidence_modality if m.evidence_modality in _VALID_MODALITIES else "text",
            "measured_entity": _ENTITY_ALIASES.get(m.measured_entity, "unknown"),
            "document_role": doc_role if doc_role in _VALID_DOC_ROLES else "main_article",
            "locator": m.locator,
            "quote": exact_quote,
            "char_start": cs,
            "char_end": ce,
        }
        try:
            row = MeasurementRow.model_validate(payload)
        except (ValidationError, PhysicalValidationError, ValueError) as exc:
            rejected_rows.append({"row_id": rid, "quantity": m.quantity, "value_raw": m.value_raw,
                                  "unit_raw": m.unit_raw, "reason": _short_validation_reason(exc)})
            continue
        src = texts.get(row.document_role, "")
        g = row.verify_grounding(src)
        if not g.ok:
            rejected_rows.append({"row_id": rid, "quantity": row.quantity, "value_raw": row.value_raw,
                                  "unit_raw": row.unit_raw, "reason": ";".join(g.reasons), "quote": row.quote[:160]})
            continue
        accepted_rows.append(row)
        seen_rids.add(rid)

    accepted_qual: list[QualitativeObservation] = []
    seen_oids: set[str] = set()
    for i, q in enumerate(raw.qualitative_observations):
        oid = q.obs_id.strip() or f"Q{i + 1}"
        while oid in seen_oids:
            oid = f"{oid}_{i + 1}"
        raw_sid = (q.sample_id or "").strip()
        if raw_sid in rejected_sids:
            rejected_rows.append({"kind": "qualitative_observation", "row_id": oid, "reason": f"REJECTED_SAMPLE_REF:{raw_sid}"})
            continue
        elif raw_sid in seen_sids:
            sid = raw_sid
        elif raw_sid == "unknown":
            sid = "unknown"
        elif used_default_sample or (not raw_sid and len(accepted_samples) == 1):
            sid = accepted_samples[0].sample_id
        else:
            rejected_rows.append({"kind": "qualitative_observation", "row_id": oid, "reason": f"UNKNOWN_SAMPLE_ID:{raw_sid}"})
            continue

        pref_role = q.document_role if q.document_role in texts else next(iter(texts), "main_article")
        matched_role, cs, ce, exact_quote = _locate_quote_in_texts(q.quote, pref_role, texts)
        doc_role = matched_role or pref_role
        q_payload = {
            "obs_id": oid,
            "sample_id": sid,
            "document_role": doc_role if doc_role in _VALID_DOC_ROLES else "main_article",
            "category": q.category,
            "evidence_level": q.evidence_level,
            "residues_raw": q.residues_raw,
            "pdb_ids": q.pdb_ids,
            "summary": q.summary,
            "locator": q.locator,
            "quote": exact_quote,
            "char_start": cs,
            "char_end": ce,
        }
        try:
            obs = QualitativeObservation.model_validate(q_payload)
        except (ValidationError, ValueError) as exc:
            rejected_rows.append({"kind": "qualitative_observation", "row_id": oid, "reason": _short_validation_reason(exc)})
            continue
        src = texts.get(obs.document_role, "")
        g = obs.verify_grounding(src)
        if not g.ok:
            rejected_rows.append({"kind": "qualitative_observation", "row_id": oid, "reason": ";".join(g.reasons), "quote": obs.quote[:160]})
            continue
        accepted_qual.append(obs)
        seen_oids.add(oid)

    accepted_states: list[AlternateStatePDB] = []
    seen_states: set[tuple[str, str]] = set()
    alt_fields = set(AlternateStatePDB.model_fields)
    for st in raw.alternate_states:
        if not isinstance(st, (dict, BaseModel)):
            continue
        st_d = st.model_dump() if isinstance(st, BaseModel) else dict(st)
        for alias, target in _ALT_STATE_KEY_ALIASES.items():
            if alias in st_d and not st_d.get(target):
                st_d[target] = st_d.pop(alias)
            elif alias in st_d:
                st_d.pop(alias)
        if st_d.get("quote"):
            _r, st_cs, st_ce, st_q = _locate_quote_in_texts(str(st_d["quote"]), next(iter(texts), "main_article"), texts)
            if st_cs is not None and st_ce is not None:
                st_d["quote"] = st_q
                st_d["char_start"] = st_cs
                st_d["char_end"] = st_ce
        cleaned_st = {k: v for k, v in st_d.items() if k in alt_fields}
        if cleaned_st.get("source_role") not in _VALID_SOURCE_ROLES:
            cleaned_st["source_role"] = "this_study"
        try:
            obj = AlternateStatePDB.model_validate(cleaned_st)
        except (ValidationError, ValueError):
            continue
        key = (obj.pdb_id, obj.state_label)
        if key not in seen_states:
            accepted_states.append(obj)
            seen_states.add(key)

    stance: Stance = raw.stance if raw.stance in _VALID_STANCES else "unclear"
    rec = PaperRecord(
        entry=entry,
        doi=doi,
        title=title,
        stance=stance,
        samples=accepted_samples,
        measurements=accepted_rows,
        qualitative_observations=accepted_qual,
        alternate_states=accepted_states,
        notes=raw.notes,
    )
    return rec, rejected_rows, rejected_samples


def _parse_cli_envelope(stdout: str) -> tuple[dict[str, Any], dict[str, Any]]:
    envelope = json.loads(stdout)
    structured = envelope.get("structured_output")
    if structured is None:
        raw_res = envelope.get("result")
        if isinstance(raw_res, dict):
            structured = raw_res
        elif isinstance(raw_res, str):
            m = re.search(r"\{.*\}", raw_res, re.S)
            structured = json.loads(m.group(0)) if m else {}
        else:
            structured = {}
    usage = {
        "cost_usd": envelope.get("total_cost_usd"),
        "duration_ms": envelope.get("duration_ms"),
        "usage": envelope.get("usage", {}),
    }
    return structured if isinstance(structured, dict) else {}, usage


def _call_anthropic_sdk(system_prompt: str, user_prompt: str, model: str = DEFAULT_SDK_MODEL) -> tuple[_RawExtractionPayload, dict[str, Any]]:
    import anthropic

    client = anthropic.Anthropic()
    resp = client.messages.parse(
        model=model,
        max_tokens=8192,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
        output_format=_RawExtractionPayload,
    )
    usage = {"input_tokens": getattr(resp.usage, "input_tokens", None), "output_tokens": getattr(resp.usage, "output_tokens", None)}
    return resp.parsed_output, usage


def _call_claude_cli(system_prompt: str, user_prompt: str, model: str = DEFAULT_CLI_MODEL, timeout_s: int = 240) -> tuple[_RawExtractionPayload, dict[str, Any]]:
    schema_str = json.dumps(_RawExtractionPayload.model_json_schema(), separators=(",", ":"))
    cmd = [
        CLAUDE_BIN, "-p",
        "--model", model,
        "--output-format", "json",
        "--json-schema", schema_str,
        "--no-session-persistence",
        "--tools", "",
        "--append-system-prompt", system_prompt,
    ]
    proc = subprocess.run(cmd, input=user_prompt, capture_output=True, text=True, timeout=timeout_s)
    if proc.returncode != 0:
        raise RuntimeError(f"claude CLI exited {proc.returncode}: {(proc.stderr or proc.stdout)[:400]}")
    structured, usage = _parse_cli_envelope(proc.stdout)
    return _RawExtractionPayload.model_validate(structured), usage


def build_batch_request(custom_id: str, entry: str, doi: str, title: str, docs: dict[DocumentRole, IngestedDocument],
                        model: str = DEFAULT_SDK_MODEL) -> dict[str, Any]:
    """Build one Anthropic Message Batches API item (50% cost, async) for runs >20 papers."""
    if not ACTIVE_PROMPT_PATH.is_file():
        export_active_prompt()
    return {
        "custom_id": custom_id,
        "params": {
            "model": model,
            "max_tokens": 8192,
            "system": canonical_system_prompt(),
            "messages": [{"role": "user", "content": _format_prompt_input(entry, doi, title, docs)}],
            "output_config": {"format": {"type": "json_schema", "schema": _RawExtractionPayload.model_json_schema()}},
        },
    }


def load_and_ground_payload(
    entry: str,
    doi: str,
    title: str,
    raw_payload: _RawExtractionPayload | dict[str, Any] | Path | str,
    docs: dict[DocumentRole, IngestedDocument],
    *,
    backend: str = "swarm_agent_direct",
    model: str = "swarm_extractor_direct_read",
    auth: dict[str, str] | None = None,
    elapsed_s: float = 0.0,
) -> ExtractionRunResult:
    """Validate and verbatim-ground a pre-produced raw extraction payload through the exact live pipeline gates.

    Used for auditable `swarm_agent_direct` runs when external API / CLI auth is unavailable, or for offline replay.
    """
    t0 = time.time()
    if isinstance(raw_payload, (Path, str)):
        raw_obj = _RawExtractionPayload.model_validate_json(Path(raw_payload).read_text(encoding="utf-8"))
    elif isinstance(raw_payload, dict):
        raw_obj = _RawExtractionPayload.model_validate(raw_payload)
    else:
        raw_obj = raw_payload
    rec, rej_rows, rej_samples = _validate_and_ground(entry, doi, title, raw_obj, docs)
    dt = elapsed_s if elapsed_s > 0 else (time.time() - t0)
    return ExtractionRunResult(
        record=rec,
        rejected_rows=rej_rows,
        rejected_samples=rej_samples,
        backend=backend,
        model=model,
        elapsed_s=dt,
        usage={"source": backend, "n_raw_samples": len(raw_obj.samples), "n_raw_measurements": len(raw_obj.measurements)},
        auth=auth if auth is not None else auth_status(check_cli=True),
    )


def extract_paper(
    entry: str,
    doi: str,
    title: str,
    docs: dict[DocumentRole, IngestedDocument],
    *,
    backend: str = "auto",
    model: str | None = None,
    raw_payload: _RawExtractionPayload | dict[str, Any] | Path | str | None = None,
) -> ExtractionRunResult:
    """Run structured extraction for one paper (main + SI) and enforce Pydantic + verbatim grounding gates."""
    if not ACTIVE_PROMPT_PATH.is_file():
        export_active_prompt()
    chosen = backend
    if chosen == "auto":
        chosen = "anthropic_sdk" if os.environ.get("ANTHROPIC_API_KEY") else "claude_cli"

    if chosen == "swarm_agent_direct":
        if raw_payload is None:
            raise ValueError("backend='swarm_agent_direct' requires raw_payload")
        return load_and_ground_payload(
            entry, doi, title, raw_payload, docs,
            backend="swarm_agent_direct",
            model=model or "swarm_extractor_direct_read",
        )

    system_prompt = canonical_system_prompt()
    user_prompt = _format_prompt_input(entry, doi, title, docs)
    auth = auth_status(check_cli=(chosen == "claude_cli"))

    t0 = time.time()
    if chosen == "anthropic_sdk":
        mdl = model or DEFAULT_SDK_MODEL
        raw, usage = _call_anthropic_sdk(system_prompt, user_prompt, model=mdl)
    elif chosen == "claude_cli":
        mdl = model or DEFAULT_CLI_MODEL
        raw, usage = _call_claude_cli(system_prompt, user_prompt, model=mdl)
    else:
        raise ValueError(f"Unknown backend: {chosen}")
    dt = time.time() - t0

    rec, rej_rows, rej_samples = _validate_and_ground(entry, doi, title, raw, docs)
    return ExtractionRunResult(
        record=rec,
        rejected_rows=rej_rows,
        rejected_samples=rej_samples,
        backend=chosen,
        model=mdl,
        elapsed_s=dt,
        usage=usage,
        auth=auth,
    )


def read_raster_figure_vision(
    png_path: Path | str,
    caption_text: str = "",
    figure_label: str = "",
    *,
    backend: str = "auto",
    model: str | None = None,
    direct_result: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Execute live Vision structured read on a cropped raster/outlined figure PNG (SDK, Claude CLI, or swarm direct)."""
    png = Path(png_path).resolve()
    if not png.is_file():
        raise FileNotFoundError(str(png))
    chosen = "anthropic_sdk" if (backend == "auto" and os.environ.get("ANTHROPIC_API_KEY")) else ("claude_cli" if backend == "auto" else backend)
    t0 = time.time()

    if chosen == "swarm_agent_direct":
        if direct_result is None:
            raise ValueError("backend='swarm_agent_direct' requires direct_result matching VLM_OUTPUT_CONTRACT")
        parsed = direct_result
        mdl = model or "swarm_extractor_direct_vision"
        usage: dict[str, Any] = {"source": "swarm_agent_direct"}
        auth = auth_status(check_cli=True)
    else:
        prompt_txt = "\n".join([
            f"Figure: {figure_label or png.name}",
            f"Caption: {caption_text[:1200]}" if caption_text else "",
            "Inspect the figure image carefully. Report each XY plot panel's verbatim axis labels, units, printed tick values, "
            "and readable data points (only points clearly distinguishable; abstain with abstain_reason if unreadable or non-XY structure image).",
            "Return ONLY JSON matching this structure:",
            json.dumps(VLM_OUTPUT_CONTRACT),
        ])
        auth = auth_status(check_cli=(chosen == "claude_cli"))

        if chosen == "anthropic_sdk":
            import anthropic

            mdl = model or DEFAULT_SDK_MODEL
            data = base64.standard_b64encode(png.read_bytes()).decode("ascii")
            client = anthropic.Anthropic()
            resp = client.messages.create(
                model=mdl,
                max_tokens=4096,
                system="You digitize scientific plots for an NMR dynamics database. Precision and abstention beat coverage.",
                messages=[{"role": "user", "content": [
                    {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": data}},
                    {"type": "text", "text": prompt_txt},
                ]}],
            )
            txt = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
            m = re.search(r"\{.*\}", txt, re.S)
            parsed = json.loads(m.group(0)) if m else {"panels": [], "parse_error": txt[:200]}
            usage = {"input_tokens": getattr(resp.usage, "input_tokens", None), "output_tokens": getattr(resp.usage, "output_tokens", None)}
        elif chosen == "claude_cli":
            mdl = model or DEFAULT_CLI_MODEL
            vlm_schema = {
                "type": "object",
                "properties": {
                    "panels": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "panel": {"type": "string"},
                                "x_axis": {"type": "object"},
                                "y_axis": {"type": "object"},
                                "series": {"type": "array"},
                                "abstain_reason": {"type": "string"},
                            },
                            "required": ["panel", "abstain_reason"],
                        },
                    }
                },
                "required": ["panels"],
            }
            cmd = [
                CLAUDE_BIN, "-p",
                "--model", mdl,
                "--output-format", "json",
                "--json-schema", json.dumps(vlm_schema, separators=(",", ":")),
                "--permission-mode", "dontAsk",
                "--allowedTools", "Read",
                "--no-session-persistence",
                "--add-dir", str(png.parent),
                "--", f"Read the image file {png} with the Read tool, then follow these instructions:\n{prompt_txt}",
            ]
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
            if proc.returncode != 0:
                raise RuntimeError(f"claude vision CLI exited {proc.returncode}: {(proc.stderr or proc.stdout)[:400]}")
            parsed, usage = _parse_cli_envelope(proc.stdout)
        else:
            raise ValueError(f"Unknown backend: {chosen}")

    return {
        "png_path": str(png),
        "figure_label": figure_label,
        "backend": chosen,
        "model": mdl,
        **auth,
        "elapsed_s": round(time.time() - t0, 2),
        "status": "READ_OK" if isinstance(parsed, dict) and "panels" in parsed else "READ_ERROR",
        "result": parsed,
        "usage": usage,
    }


def _to_score_dict_from_measurement(m: MeasurementRow, sample: SampleSpec | None) -> dict[str, Any]:
    return {
        "row_id": m.row_id,
        "quantity": m.quantity,
        "value": m.value_num if m.value_num is not None else m.value_raw,
        "unit": m.unit_raw,
        "sample_construct": sample.construct_label if sample else "",
        "ligand_state": sample.ligand_state if sample else "",
        "temperature": sample.temperature_raw if sample else "",
        "quote": m.quote,
        "residues_raw": m.residues_raw,
        "locator": m.locator,
        "document_role": m.document_role,
    }


def _to_score_dict_from_gold(g: Any) -> dict[str, Any]:
    return {
        "quantity": g.quantity,
        "value": g.value,
        "unit": g.unit_raw,
        "sample_construct": g.construct,
        "ligand_state": g.ligand,
        "temperature": g.temp_raw,
        "quote": g.quote,
        "residues_raw": g.residues_raw,
        "locator": g.location,
        "source": g.source,
    }


def score_live_extractions(
    records: list[PaperRecord],
    *,
    backend: str = "swarm_agent_direct",
    auth: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Score accepted live PaperRecord measurements against F14 batch1 + read-only SQLite gold using 5-tuple score_record()."""
    from collections import Counter
    from datetime import datetime

    from .compare import (
        DB_PATH,
        F14_BATCHES,
        _connect,
        load_f14_rows,
        load_sqlite_rows,
        parse_single_residue,
        score_record,
    )

    entries = {r.entry for r in records}
    con = _connect(DB_PATH)
    try:
        sq_rows = load_sqlite_rows(con, entries)
    finally:
        con.close()
    f14_rows = load_f14_rows(entries, [F14_BATCHES[0]])
    all_gold = sq_rows + f14_rows

    auth_info = auth if auth is not None else auth_status(check_cli=True)
    per_paper: list[dict[str, Any]] = []
    slot_totals: Counter = Counter()
    reason_totals: Counter = Counter()
    total_matched = total_all5 = total_naive2 = total_same_doi_gold = total_same_doi_gold_dyn = 0

    for rec in records:
        sample_map = {s.sample_id: s for s in rec.samples}
        live_primary = rec.primary_measurements()
        live_dicts = [(_to_score_dict_from_measurement(m, sample_map.get(m.sample_id)), m) for m in live_primary]
        same_doi_gold = [g for g in all_gold if g.entry == rec.entry and g.doi == rec.doi.lower()]
        other_doi_gold = [g for g in all_gold if g.entry == rec.entry and g.doi != rec.doi.lower()]
        same_doi_dyn = [g for g in same_doi_gold if g.role != "other"]

        # Build all candidate (gold, live) pairs of the same canonical quantity and pair globally best-first
        # so duplicate gold restatements never steal a live row from its true matching condition/value.
        candidates: list[tuple[tuple, int, int, dict[str, Any]]] = []
        for gi, g in enumerate(same_doi_dyn):
            g_dict = _to_score_dict_from_gold(g)
            g_res = g.residue
            for li, (p_dict, m) in enumerate(live_dicts):
                if m.quantity_canonical != g.role:
                    continue
                p_res = parse_single_residue(m.residues_raw)
                if g_res is not None and p_res is not None and p_res[1] != g_res[1]:
                    continue
                sc = score_record(p_dict, g_dict)
                slot_sum = sum(int(sc[k]) for k in ("quantity_ok", "value_ok", "construct_ok", "ligand_state_ok", "temperature_ok"))
                res_exact = int(g_res is not None and p_res is not None and p_res[1] == g_res[1])
                pv, gv = p_dict["value"], g_dict["value"]
                rel = abs(float(pv) - float(gv)) / max(abs(float(gv)), 1e-9) if isinstance(pv, (int, float)) and isinstance(gv, (int, float)) else 999.0
                if not sc["value_ok"] and not (sc["construct_ok"] and sc["ligand_state_ok"] and rel < 0.5):
                    continue
                cand_key = (int(sc["all_5_ok"]), res_exact, int(sc["value_ok"]), int(sc["construct_ok"]),
                            int(sc["ligand_state_ok"]), slot_sum, -rel)
                candidates.append((cand_key, gi, li, sc))

        candidates.sort(key=lambda x: x[0], reverse=True)
        used_gold: set[int] = set()
        used_live: set[int] = set()
        matched_by_gold: dict[int, tuple[int, dict[str, Any]]] = {}
        for _key, gi, li, sc in candidates:
            if gi in used_gold or li in used_live:
                continue
            used_gold.add(gi)
            used_live.add(li)
            matched_by_gold[gi] = (li, sc)

        scored_pairs: list[dict[str, Any]] = []
        unmatched_gold: list[dict[str, Any]] = []
        for gi, g in enumerate(same_doi_dyn):
            if gi in matched_by_gold:
                li, best_score = matched_by_gold[gi]
                p_dict, m = live_dicts[li]
                scored_pairs.append({
                    "gold_index": gi,
                    "live_row_id": m.row_id,
                    "quantity_canonical": g.role,
                    "gold_value": g.value,
                    "gold_unit": g.unit_raw,
                    "gold_residues": g.residues_raw,
                    "gold_locator": g.location,
                    "gold_construct": g.construct,
                    "gold_ligand": g.ligand,
                    "gold_temperature": g.temp_raw,
                    "live_value": p_dict["value"],
                    "live_unit": m.unit_raw,
                    "live_residues": m.residues_raw,
                    "live_locator": m.locator,
                    "live_construct": p_dict["sample_construct"],
                    "live_ligand": p_dict["ligand_state"],
                    "live_temperature": p_dict["temperature"],
                    "score": best_score,
                })
                total_matched += 1
                total_all5 += int(best_score["all_5_ok"])
                total_naive2 += int(best_score["two_tuple_naive_ok"])
                for k in ("quantity_ok", "value_ok", "construct_ok", "ligand_state_ok", "temperature_ok"):
                    slot_totals[k] += int(best_score[k])
                for rc in best_score["failure_reasons"]:
                    reason_totals[rc.split(":")[0]] += 1
            else:
                unmatched_gold.append({
                    "gold_index": gi,
                    "quantity": g.quantity,
                    "role": g.role,
                    "value": g.value,
                    "unit": g.unit_raw,
                    "residues": g.residues_raw,
                    "locator": g.location,
                    "source": g.source,
                })

        cross_doi_checks: list[dict[str, Any]] = []
        if not same_doi_gold and other_doi_gold:
            for g in [x for x in other_doi_gold if x.role == "kex"][:4]:
                g_dict = _to_score_dict_from_gold(g)
                kex_live = [(p_dict, m) for p_dict, m in live_dicts if m.quantity_canonical == "kex"]
                if kex_live:
                    p_dict, m = kex_live[0]
                    cross_doi_checks.append({
                        "live_doi": rec.doi,
                        "gold_doi": g.doi,
                        "live_row_id": m.row_id,
                        "gold_value": g.value,
                        "live_value": p_dict["value"],
                        "score": score_record(p_dict, g_dict),
                    })

        total_same_doi_gold += len(same_doi_gold)
        total_same_doi_gold_dyn += len(same_doi_dyn)
        n_p_matched = len(scored_pairs)
        n_p_all5 = sum(1 for x in scored_pairs if x["score"]["all_5_ok"])
        n_p_naive2 = sum(1 for x in scored_pairs if x["score"]["two_tuple_naive_ok"])
        per_paper.append({
            "entry": rec.entry,
            "doi": rec.doi,
            "n_live_total": len(rec.measurements),
            "n_live_primary": len(live_primary),
            "n_same_doi_gold_total": len(same_doi_gold),
            "n_same_doi_gold_dynamics": len(same_doi_dyn),
            "n_same_doi_gold_other_excluded": len(same_doi_gold) - len(same_doi_dyn),
            "n_other_doi_gold": len(other_doi_gold),
            "other_doi_gold_dois": sorted({g.doi for g in other_doi_gold}),
            "same_doi_gold_status": "SCORED" if same_doi_gold else "NO_SAME_DOI_GOLD_STANDARD",
            "n_matched_pairs": n_p_matched,
            "n_all_5_ok": n_p_all5,
            "n_two_tuple_naive_ok": n_p_naive2,
            "all_5_rate_on_matched": round(n_p_all5 / n_p_matched, 4) if n_p_matched else None,
            "slot_pass_counts": {
                k: sum(1 for x in scored_pairs if x["score"][k])
                for k in ("quantity_ok", "value_ok", "construct_ok", "ligand_state_ok", "temperature_ok")
            },
            "failure_reason_counts": dict(Counter(
                rc.split(":")[0] for x in scored_pairs for rc in x["score"]["failure_reasons"]
            )),
            "unmatched_gold_dynamics_count": len(unmatched_gold),
            "unmatched_gold_dynamics": unmatched_gold,
            "cross_doi_sanity_checks": cross_doi_checks,
            "scored_pairs": scored_pairs,
        })

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "scorer": "atlas_pipeline.compare.score_record (default strict tolerances: temp_tol_k=1.0, rel_tol=0.02)",
        "gold_sources": [str(DB_PATH), str(F14_BATCHES[0])],
        "backend": backend,
        **auth_info,
        "summary": {
            "n_papers": len(records),
            "n_live_measurements_total": sum(len(r.measurements) for r in records),
            "n_live_primary": sum(len(r.primary_measurements()) for r in records),
            "n_same_doi_gold_total": total_same_doi_gold,
            "n_same_doi_gold_dynamics": total_same_doi_gold_dyn,
            "n_matched_pairs": total_matched,
            "n_all_5_ok": total_all5,
            "n_two_tuple_naive_ok": total_naive2,
            "all_5_rate_on_matched": round(total_all5 / total_matched, 4) if total_matched else None,
            "two_tuple_rate_on_matched": round(total_naive2 / total_matched, 4) if total_matched else None,
            "slot_pass_counts": dict(slot_totals),
            "failure_reason_counts": dict(reason_totals),
        },
        "papers": per_paper,
    }
