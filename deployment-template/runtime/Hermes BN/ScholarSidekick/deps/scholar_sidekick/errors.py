"""Exception hierarchy for the Scholar Sidekick client.

The API contract states that the ``code`` field is the stable contract and that
HTTP statuses MAY change. Every exception here is therefore selected by ``code``
rather than by status, and carries the originating ``request_id`` so a user's bug
report is actionable.

Note what is deliberately NOT an exception: a ``mismatch`` verdict from
``verify()``. The API returns 200 on every verdict, and a fabricated-citation
finding is the tool working correctly, not an error.
"""

from __future__ import annotations

from typing import Any, Optional

__all__ = [
    "ScholarSidekickError",
    "APIError",
    "ValidationError",
    "AuthError",
    "RateLimitError",
    "UpstreamError",
    "TransportError",
    "RateLimitWarning",
    "error_from_response",
]


class ScholarSidekickError(Exception):
    """Base class for every error raised by this package."""


class TransportError(ScholarSidekickError):
    """A connection failure or timeout — no HTTP response was received.

    Distinct from :class:`APIError`: there is no status, code or request id,
    because the request never reached a server that could supply them.
    """


class APIError(ScholarSidekickError):
    """The API returned an error response.

    Attributes:
        code: The stable machine-readable error code (the contract).
        message: The human-readable message from the response body.
        status: The HTTP status. Informational — do not branch on it.
        request_id: The ``x-request-id`` header, for support requests.
        payload: The raw decoded error body, if it was JSON.
    """

    def __init__(
        self,
        message: str,
        *,
        code: Optional[str] = None,
        status: Optional[int] = None,
        request_id: Optional[str] = None,
        payload: Optional[dict[str, Any]] = None,
    ) -> None:
        detail = f"{code}: {message}" if code else message
        if request_id:
            detail = f"{detail} (request id: {request_id})"
        super().__init__(detail)
        self.code = code
        self.message = message
        self.status = status
        self.request_id = request_id
        self.payload = payload or {}


class ValidationError(APIError):
    """The request was rejected as malformed or invalid.

    Examples: ``MISSING_TITLE`` (verify without a claimed title),
    ``IDEMPOTENCY_KEY_REUSED`` (same key, different body).
    """


class AuthError(APIError):
    """The request was rejected for authentication or entitlement reasons.

    Includes ``LLM_SCREEN_FORBIDDEN`` — ``screen_with_llm`` is gated to
    authenticated callers, so an anonymous caller requesting it lands here.
    """


class RateLimitError(APIError):
    """The rate limit was exceeded.

    ``retry_after`` is the server-supplied delay in seconds when present. The API
    synthesizes ``Retry-After`` only on 429, so prefer it over any computed
    backoff when it is available.
    """

    def __init__(self, message: str, *, retry_after: Optional[float] = None, **kwargs: Any) -> None:
        super().__init__(message, **kwargs)
        self.retry_after = retry_after


class UpstreamError(APIError):
    """A scholarly data source failed after the API's own bounded retries.

    Covers ``UPSTREAM_TIMEOUT``, ``UPSTREAM_UNAVAILABLE``,
    ``UPSTREAM_RATE_LIMITED``, ``UPSTREAM_NETWORK_ERROR`` and ``UPSTREAM_ERROR``.
    These are transient by nature: the citation data is fine, the lookup failed.
    """


class RateLimitWarning(UserWarning):
    """Warned once when a long run first hits the rate limit and has to wait."""


# Codes that mean "your request was wrong" rather than "something failed".
_VALIDATION_CODES = frozenset(
    {
        "MISSING_TITLE",
        "IDEMPOTENCY_KEY_REUSED",
        "INVALID_BODY",
        "INVALID_STYLE",
        "INVALID_FORMAT",
        "TOO_MANY_ITEMS",
        "BODY_TOO_LARGE",
        "EMPTY_INPUT",
    }
)

_AUTH_CODES = frozenset(
    {
        "LLM_SCREEN_FORBIDDEN",
        "UNAUTHORIZED",
        "FORBIDDEN",
        "INVALID_API_KEY",
        "API_KEY_REQUIRED",
    }
)


def error_from_response(
    *,
    status: int,
    payload: Optional[dict[str, Any]],
    request_id: Optional[str],
    retry_after: Optional[float] = None,
    fallback_message: str = "",
) -> APIError:
    """Build the most specific :class:`APIError` for an error response.

    Selection is by ``code`` first, because that is the documented contract;
    status is only consulted when the body carried no usable code (for example a
    proxy-generated 502 with an HTML body).
    """
    body = payload or {}
    code = body.get("code")
    # RFC 9457 problem+json uses `detail`/`title`; the default envelope uses `error`.
    message = (
        body.get("error")
        or body.get("detail")
        or body.get("title")
        or fallback_message
        or f"HTTP {status}"
    )
    if not isinstance(message, str):  # pragma: no cover - defensive
        message = str(message)
    code_str = code if isinstance(code, str) else None

    kwargs: dict[str, Any] = {
        "code": code_str,
        "status": status,
        "request_id": request_id,
        "payload": body,
    }

    if status == 429 or code_str == "RATE_LIMITED":
        return RateLimitError(message, retry_after=retry_after, **kwargs)
    if code_str and code_str.startswith("UPSTREAM_"):
        return UpstreamError(message, **kwargs)
    if code_str in _AUTH_CODES:
        return AuthError(message, **kwargs)
    if code_str in _VALIDATION_CODES:
        return ValidationError(message, **kwargs)

    # No recognised code: fall back to status bands.
    if status in (401, 403):
        return AuthError(message, **kwargs)
    if 400 <= status < 500:
        return ValidationError(message, **kwargs)
    if status >= 500:
        return UpstreamError(message, **kwargs)
    return APIError(message, **kwargs)
