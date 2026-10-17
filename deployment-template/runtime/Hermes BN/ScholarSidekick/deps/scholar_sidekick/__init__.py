"""Scholar Sidekick — resolve, verify, format and audit scholarly citations.

A thin Python client for the Scholar Sidekick REST API. Every endpoint works
anonymously; an API key raises the rate limit but is never required.

    from scholar_sidekick import ScholarSidekick

    client = ScholarSidekick()

    # Format a DOI
    print(client.format(text="10.1038/nphys1170", style="vancouver").text)

    # Check whether a citation is real. A resolvable DOI is not enough:
    # the dominant AI-fabrication pattern is a real DOI with an invented title.
    result = client.verify(title="Measured measurement", doi="10.1038/nphys1170")
    print(result.verdict)   # matched | mismatch | ambiguous | not_found

    # Audit a whole bibliography — chunked and paced automatically
    report = client.audit_bibliography(references)
    print(report.summary)
"""

from __future__ import annotations

from .audit import AUDIT_MAX_ENTRIES
from .client import AsyncScholarSidekick, ScholarSidekick
from .config import DEFAULT_BASE_URL, client_tag
from .errors import (
    APIError,
    AuthError,
    RateLimitError,
    RateLimitWarning,
    ScholarSidekickError,
    TransportError,
    UpstreamError,
    ValidationError,
)
from .models import (
    AuditEntry,
    AuditReport,
    AuditSummary,
    ChunkError,
    FormatItemsResult,
    FormatResult,
    ParseError,
    VerifyResult,
)


def _resolve_version() -> str:
    try:
        from importlib.metadata import version

        return version("scholar-sidekick")
    except Exception:  # pragma: no cover - bare checkout without an install
        return "0.0.0+unknown"


# Derived from installed metadata; pyproject.toml is the only place a version
# string is written in this repository.
__version__ = _resolve_version()

__all__ = [
    "ScholarSidekick",
    "AsyncScholarSidekick",
    "AUDIT_MAX_ENTRIES",
    "DEFAULT_BASE_URL",
    "client_tag",
    "__version__",
    # errors
    "ScholarSidekickError",
    "APIError",
    "ValidationError",
    "AuthError",
    "RateLimitError",
    "UpstreamError",
    "TransportError",
    "RateLimitWarning",
    # models
    "FormatResult",
    "FormatItemsResult",
    "VerifyResult",
    "AuditReport",
    "AuditEntry",
    "AuditSummary",
    "ParseError",
    "ChunkError",
]
