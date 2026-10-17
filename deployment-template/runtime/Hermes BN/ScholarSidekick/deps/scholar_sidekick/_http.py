"""Transport internals shared by the sync and async clients.

Request building, response interpretation, retry policy and backoff computation
all live here as pure functions so the two clients differ only in how they await
the network. Duplicating this logic between them would double the surface on
which they can silently drift apart.
"""

from __future__ import annotations

import random
import uuid
from typing import Any, Optional, Union

import httpx

from .errors import TransportError, error_from_response

__all__ = [
    "RETRYABLE_STATUSES",
    "build_url",
    "decode_json",
    "interpret",
    "new_idempotency_key",
    "backoff_delay",
    "retry_after_seconds",
    "rate_limit_remaining",
]

# 429 is retryable because the server tells us exactly how long to wait; 5xx
# because the API's own upstream retries have already been exhausted, so a brief
# pause is the only remaining option. 4xx is never retried: the request is wrong
# and will stay wrong.
RETRYABLE_STATUSES = frozenset({429, 500, 502, 503, 504})

_MAX_BACKOFF = 30.0


def build_url(base_url: str, path: str) -> str:
    return f"{base_url.rstrip('/')}{path}"


def new_idempotency_key() -> str:
    """A fresh key so a retried POST replays instead of repeating the work.

    Constrained to the API's accepted alphabet (``[A-Za-z0-9_.:-]``, 1-255 chars).
    """
    return uuid.uuid4().hex


def retry_after_seconds(response: httpx.Response) -> Optional[float]:
    """Parse ``Retry-After``, falling back to the legacy reset-after header.

    The API synthesizes ``Retry-After`` only on 429, so it is authoritative when
    present and worth preferring over any locally computed backoff.
    """
    for header in ("retry-after", "x-ratelimit-reset-after"):
        raw = response.headers.get(header)
        if not raw:
            continue
        try:
            value = float(raw)
        except (TypeError, ValueError):
            continue
        if value >= 0:
            return value
    return None


def rate_limit_remaining(response: httpx.Response) -> Optional[int]:
    """Requests left in the current window, if the server reported it."""
    for header in ("ratelimit-remaining", "x-ratelimit-remaining"):
        raw = response.headers.get(header)
        if raw is None:
            continue
        try:
            return int(raw)
        except (TypeError, ValueError):
            continue
    return None


def backoff_delay(attempt: int, *, retry_after: Optional[float] = None) -> float:
    """Delay before retry ``attempt`` (1-based).

    A server-supplied ``Retry-After`` always wins — guessing at a policy the
    server just told us is pointless. Otherwise exponential with jitter, so
    concurrent callers do not resynchronise onto the same retry instant.
    """
    if retry_after is not None:
        return min(retry_after, _MAX_BACKOFF)
    base = min(2.0 ** (attempt - 1), _MAX_BACKOFF)
    return base * (0.5 + random.random() / 2)


def decode_json(response: httpx.Response) -> Optional[dict[str, Any]]:
    """Decode a JSON body, returning ``None`` when it is absent or not an object."""
    if not response.content:
        return None
    try:
        payload = response.json()
    except ValueError:
        return None
    return payload if isinstance(payload, dict) else None


def interpret(response: httpx.Response, *, expect: str = "json") -> Union[dict[str, Any], str]:
    """Return the successful body, or raise the mapped :class:`APIError`.

    ``expect="text"`` is for ``/api/export``, whose success body is a raw string
    (RIS, BibTeX, CSV…) rather than JSON. Error bodies are still JSON, so the
    error path is identical for both.
    """
    request_id = response.headers.get("x-request-id")

    if response.is_success:
        if expect == "text":
            return response.text
        payload = decode_json(response)
        if payload is None:
            raise TransportError(
                f"Expected a JSON response but got {response.headers.get('content-type')!r} "
                f"(request id: {request_id})"
            )
        return payload

    raise error_from_response(
        status=response.status_code,
        payload=decode_json(response),
        request_id=request_id,
        retry_after=retry_after_seconds(response),
        fallback_message=response.text[:200] if response.content else "",
    )
