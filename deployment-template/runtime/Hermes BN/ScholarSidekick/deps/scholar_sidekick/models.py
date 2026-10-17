"""Response models.

These deliberately **pass the API's shapes through** rather than normalising
them. Two inconsistencies are load-bearing and are preserved on purpose:

1. ``/api/format`` returns the formatted result as a whole-batch, newline-joined
   ``text``/``html`` string. There is no per-item ``citation`` field. Splitting
   that string to synthesise one would be wrong for styles whose entries contain
   newlines, and would misattribute citations whenever the resolver deduplicates.
2. ``/api/format-items`` calls the same concept ``output`` (not ``text``) and
   ``itemsUsed`` (not ``itemsOut``).

Every model keeps the undecoded payload on ``.raw``, so a field the server adds
tomorrow is reachable today without a release of this package.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

__all__ = [
    "FormatResult",
    "FormatItemsResult",
    "VerifyResult",
    "AuditEntry",
    "ParseError",
    "AuditSummary",
    "AuditReport",
    "ChunkError",
]


def _claimed_title(claimed: Optional[Any]) -> Optional[str]:
    """The title the caller supplied, for reporting which reference is at fault.

    Accepts either a claim dict or a raw reference string, matching the two input
    kinds ``audit_bibliography()`` takes.
    """
    if isinstance(claimed, dict):
        title = claimed.get("title")
        return title if isinstance(title, str) else None
    if isinstance(claimed, str):
        return claimed
    return None


def _summary_fields() -> dict[str, int]:
    return {
        "total": 0,
        "matched": 0,
        "mismatch": 0,
        "ambiguous": 0,
        "not_found": 0,
        "errored": 0,
        "retracted": 0,
    }


@dataclass
class FormatResult:
    """Result of ``POST /api/format``.

    ``text`` and ``html`` are **whole-batch** strings covering every input
    identifier, newline-joined. There is no per-item formatted field.
    """

    ok: bool
    text: Optional[str] = None
    html: Optional[str] = None
    formatter: Optional[str] = None
    style_requested: Optional[str] = None
    style_used: Optional[str] = None
    items_in: Optional[int] = None
    items_out: Optional[int] = None
    items: list[dict[str, Any]] = field(default_factory=list)
    warnings: list[Any] = field(default_factory=list)
    meta: dict[str, Any] = field(default_factory=dict)
    raw: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_response(cls, payload: dict[str, Any]) -> FormatResult:
        return cls(
            ok=bool(payload.get("ok", True)),
            text=payload.get("text"),
            html=payload.get("html"),
            formatter=payload.get("formatter"),
            style_requested=payload.get("styleRequested"),
            style_used=payload.get("styleUsed"),
            items_in=payload.get("itemsIn"),
            items_out=payload.get("itemsOut"),
            items=payload.get("items") or [],
            warnings=payload.get("warnings") or [],
            meta=payload.get("meta") or {},
            raw=payload,
        )


@dataclass
class FormatItemsResult:
    """Result of ``POST /api/format-items``.

    The formatted string is ``output`` — the server's own name for it, kept
    rather than aliased to ``text`` so the difference from :class:`FormatResult`
    stays visible.
    """

    ok: bool
    output: Optional[str] = None
    html: Optional[str] = None
    formatter: Optional[str] = None
    style_requested: Optional[str] = None
    style_used: Optional[str] = None
    items_in: Optional[int] = None
    items_used: Optional[int] = None
    items: list[dict[str, Any]] = field(default_factory=list)
    meta: dict[str, Any] = field(default_factory=dict)
    raw: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_response(cls, payload: dict[str, Any]) -> FormatItemsResult:
        return cls(
            ok=bool(payload.get("ok", True)),
            output=payload.get("output"),
            html=payload.get("html"),
            formatter=payload.get("formatter"),
            style_requested=payload.get("styleRequested"),
            style_used=payload.get("styleUsed"),
            items_in=payload.get("itemsIn"),
            items_used=payload.get("itemsUsed"),
            items=payload.get("items") or [],
            meta=payload.get("meta") or {},
            raw=payload,
        )


@dataclass
class VerifyResult:
    """Result of ``POST /api/verify``.

    A ``mismatch`` verdict is a normal, successful result — the API returns 200
    on every verdict, and this class is never raised as an exception.

    Verdicts:
        ``matched``    the claimed citation agrees with the resolved record.
        ``mismatch``   the identifier resolves to a *different* work. This is the
                       dominant AI-fabrication pattern.
        ``ambiguous``  a discrepancy that needs human eyes, not an accusation.
        ``not_found``  no record found. **Not** proof of fabrication — the work
                       may be real but outside the registries searched.
    """

    ok: bool
    verdict: Optional[str] = None
    confidence: Optional[str] = None
    matched: Optional[dict[str, Any]] = None
    mismatches: list[dict[str, Any]] = field(default_factory=list)
    candidates: list[dict[str, Any]] = field(default_factory=list)
    provenance: dict[str, Any] = field(default_factory=dict)
    raw: dict[str, Any] = field(default_factory=dict)

    @property
    def is_match(self) -> bool:
        return self.verdict == "matched"

    @property
    def needs_review(self) -> bool:
        """True for any verdict a human should look at before trusting it."""
        return self.verdict in ("mismatch", "ambiguous", "not_found")

    @classmethod
    def from_response(cls, payload: dict[str, Any]) -> VerifyResult:
        return cls(
            ok=bool(payload.get("ok", True)),
            verdict=payload.get("verdict"),
            confidence=payload.get("confidence"),
            matched=payload.get("matched"),
            mismatches=payload.get("mismatches") or [],
            candidates=payload.get("candidates") or [],
            provenance=payload.get("_provenance") or {},
            raw=payload,
        )


@dataclass
class AuditEntry:
    """One audited reference.

    ``input_index`` is the 0-based position in the list *you* passed in.
    ``api_index`` is the 1-based index the API returned for its own chunk. Under
    chunking these differ, and reporting the API's number against the caller's
    list would name the wrong reference.
    """

    input_index: int
    api_index: Optional[int] = None
    status: Optional[str] = None
    verdict: Optional[str] = None
    confidence: Optional[str] = None
    claimed_title: Optional[str] = None
    resolved_title: Optional[str] = None
    matched: Optional[dict[str, Any]] = None
    retracted: bool = False
    has_concern: bool = False
    has_corrections: bool = False
    notices: list[dict[str, Any]] = field(default_factory=list)
    provenance: dict[str, Any] = field(default_factory=dict)
    raw: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_response(
        cls,
        payload: dict[str, Any],
        *,
        offset: int,
        claimed: Optional[Any] = None,
    ) -> AuditEntry:
        api_index = payload.get("index")
        # The API's index is 1-based within its own chunk; translate back to a
        # 0-based position in the caller's original list.
        input_index = offset + (api_index - 1) if isinstance(api_index, int) else offset

        # The entry carries no title of its own; the resolved record's title lives
        # under `matched`. Keeping the two titles separately named matters: on a
        # mismatch they are different works, and showing the resolved one in a
        # column labelled "title" would misidentify which reference is at fault.
        matched = payload.get("matched")
        resolved_title = matched.get("title") if isinstance(matched, dict) else None

        retraction = payload.get("retraction")
        retraction = retraction if isinstance(retraction, dict) else {}

        return cls(
            input_index=input_index,
            api_index=api_index,
            status=payload.get("status"),
            verdict=payload.get("verdict"),
            confidence=payload.get("confidence"),
            claimed_title=_claimed_title(claimed),
            resolved_title=resolved_title,
            matched=matched if isinstance(matched, dict) else None,
            retracted=bool(retraction.get("isRetracted")),
            has_concern=bool(retraction.get("hasConcern")),
            has_corrections=bool(retraction.get("hasCorrections")),
            notices=retraction.get("notices") or [],
            provenance=payload.get("_provenance") or {},
            raw=payload,
        )


@dataclass
class ParseError:
    """A reference the parser could not read. ``input_index`` is 0-based."""

    input_index: int
    api_index: Optional[int] = None
    message: Optional[str] = None
    raw: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_response(cls, payload: dict[str, Any], *, offset: int) -> ParseError:
        api_index = payload.get("index")
        input_index = offset + (api_index - 1) if isinstance(api_index, int) else offset
        return cls(
            input_index=input_index,
            api_index=api_index,
            message=payload.get("message") or payload.get("error"),
            raw=payload,
        )


@dataclass
class ChunkError:
    """A chunk that failed outright, recorded rather than raised.

    A long audit that discards every completed chunk because one transient
    upstream failure occurred is not usable for real work, so failures are
    reported alongside the results that did succeed.
    """

    start_index: int
    end_index: int
    error: BaseException

    def __str__(self) -> str:  # pragma: no cover - convenience only
        return f"entries {self.start_index}-{self.end_index}: {self.error}"


@dataclass
class AuditSummary:
    """Verdict counts. Sums across every chunk of a multi-chunk audit."""

    total: int = 0
    matched: int = 0
    mismatch: int = 0
    ambiguous: int = 0
    not_found: int = 0
    errored: int = 0
    retracted: int = 0

    @classmethod
    def from_response(cls, payload: dict[str, Any]) -> AuditSummary:
        base = _summary_fields()
        for key in base:
            value = payload.get(key)
            if isinstance(value, int):
                base[key] = value
        return cls(**base)

    def add(self, other: AuditSummary) -> AuditSummary:
        return AuditSummary(
            total=self.total + other.total,
            matched=self.matched + other.matched,
            mismatch=self.mismatch + other.mismatch,
            ambiguous=self.ambiguous + other.ambiguous,
            not_found=self.not_found + other.not_found,
            errored=self.errored + other.errored,
            retracted=self.retracted + other.retracted,
        )


@dataclass
class AuditReport:
    """The aggregate result of an audit, possibly spanning many chunks."""

    entries: list[AuditEntry] = field(default_factory=list)
    parse_errors: list[ParseError] = field(default_factory=list)
    summary: AuditSummary = field(default_factory=AuditSummary)
    errors: list[ChunkError] = field(default_factory=list)
    format: Optional[str] = None
    chunks: int = 0
    raw: list[dict[str, Any]] = field(default_factory=list)

    @property
    def complete(self) -> bool:
        """False when at least one chunk failed and its entries are missing."""
        return not self.errors

    @property
    def needs_review(self) -> list[AuditEntry]:
        """Entries whose verdict a human should check before acting on it."""
        return [e for e in self.entries if e.verdict in ("mismatch", "ambiguous", "not_found")]

    def to_dataframe(self) -> Any:
        """Return the entries as a pandas ``DataFrame``.

        pandas is an optional dependency (``pip install scholar-sidekick[pandas]``)
        and is imported lazily so the base package stays dependency-light.
        """
        try:
            import pandas as pd
        except ImportError as exc:  # pragma: no cover - exercised via monkeypatch
            raise ImportError(
                "to_dataframe() requires pandas. Install it with: "
                "pip install 'scholar-sidekick[pandas]'"
            ) from exc

        return pd.DataFrame(
            [
                {
                    "index": e.input_index,
                    "claimed_title": e.claimed_title,
                    "resolved_title": e.resolved_title,
                    "verdict": e.verdict,
                    "confidence": e.confidence,
                    "status": e.status,
                    "retracted": e.retracted,
                    "has_concern": e.has_concern,
                }
                for e in self.entries
            ]
        )
