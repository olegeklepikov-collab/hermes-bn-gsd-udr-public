"""Bibliography-audit chunking and pacing.

``POST /api/audit`` accepts at most 25 entries per call and is rate-limited to 4
calls per 30 seconds. A real systematic review has hundreds of references, so the
useful unit of work is "audit this whole bibliography", not "audit 25 of them".

Three properties matter more than speed here:

* **Serial, never parallel.** The server already fans out internally at
  concurrency 4 against Crossref and PubMed. A client that parallelises chunks is
  competing with that fan-out for the same upstream budget.
* **Paced from response headers, not from a fixed sleep.** A hardcoded delay
  encodes a rate-limit policy that lives on the server and can change.
* **Partial results survive.** A 600-reference audit takes minutes; discarding
  every completed chunk because chunk 14 hit a transient 502 makes the tool
  unusable for the work it exists to do.

This module holds the pure planning logic so the sync and async clients share one
implementation of the tricky parts (chunk boundaries, index translation,
aggregation) and differ only in how they sleep.
"""

from __future__ import annotations

import warnings
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any, Callable, Optional

from .errors import RateLimitWarning
from .models import AuditEntry, AuditReport, AuditSummary, ChunkError, ParseError

__all__ = ["AUDIT_MAX_ENTRIES", "Chunk", "plan_chunks", "accumulate", "pace_delay"]

# Mirrors AUDIT_MAX_ENTRIES on the server. Sending more in one call is rejected.
AUDIT_MAX_ENTRIES = 25

# When the server says this few requests remain in the window, pause before the
# next chunk rather than pressing on into a 429 we would then have to recover from.
_LOW_REMAINING = 1
_PACE_SECONDS = 8.0

ProgressCallback = Callable[[int, int], None]


@dataclass(frozen=True)
class Chunk:
    """One planned request: ``items`` and where they came from in the caller's list."""

    index: int
    offset: int
    items: list[Any]

    @property
    def start_index(self) -> int:
        return self.offset

    @property
    def end_index(self) -> int:
        return self.offset + len(self.items) - 1


def plan_chunks(items: Sequence[Any], *, size: int = AUDIT_MAX_ENTRIES) -> list[Chunk]:
    """Split ``items`` into server-sized chunks, recording each one's offset.

    The offset is what makes index translation possible later: the API numbers
    entries 1-based within a chunk, so chunk 3's "entry 7" is the caller's
    reference 56 and must be reported as such.
    """
    if size < 1:
        raise ValueError("chunk size must be at least 1")
    return [
        Chunk(index=i, offset=start, items=list(items[start : start + size]))
        for i, start in enumerate(range(0, len(items), size))
    ]


def pace_delay(remaining: Optional[int], *, is_last: bool) -> float:
    """Seconds to wait before the next chunk.

    Returns 0 after the final chunk, or whenever the server reports enough
    allowance left to proceed immediately.
    """
    if is_last:
        return 0.0
    if remaining is None:
        return 0.0
    if remaining <= _LOW_REMAINING:
        return _PACE_SECONDS
    return 0.0


def warn_rate_limited(already_warned: bool) -> bool:
    """Warn once per run that the limit was hit, naming the fix. Returns the new flag."""
    if already_warned:
        return True
    warnings.warn(
        "Rate limit reached; pausing before continuing. A free API key raises the "
        "audit allowance about fivefold — see https://scholar-sidekick.com/account",
        RateLimitWarning,
        stacklevel=3,
    )
    return True


def accumulate(
    report: AuditReport,
    payload: dict[str, Any],
    *,
    chunk: Chunk,
) -> None:
    """Fold one chunk's response into the running report, translating indices."""
    entries = payload.get("entries") or []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        # Attach the caller's own claim so a flagged row names the reference the
        # caller recognises, not just the record the identifier resolved to.
        api_index = entry.get("index")
        claimed = None
        if isinstance(api_index, int) and 0 <= api_index - 1 < len(chunk.items):
            claimed = chunk.items[api_index - 1]
        report.entries.append(AuditEntry.from_response(entry, offset=chunk.offset, claimed=claimed))

    for parse_error in payload.get("parseErrors") or []:
        if isinstance(parse_error, dict):
            report.parse_errors.append(ParseError.from_response(parse_error, offset=chunk.offset))

    summary = payload.get("summary")
    if isinstance(summary, dict):
        report.summary = report.summary.add(AuditSummary.from_response(summary))

    if report.format is None:
        fmt = payload.get("format")
        if isinstance(fmt, str):
            report.format = fmt

    report.chunks += 1
    report.raw.append(payload)


def record_failure(report: AuditReport, chunk: Chunk, error: BaseException) -> None:
    """Record a failed chunk without discarding the chunks that succeeded."""
    report.errors.append(
        ChunkError(start_index=chunk.start_index, end_index=chunk.end_index, error=error)
    )
