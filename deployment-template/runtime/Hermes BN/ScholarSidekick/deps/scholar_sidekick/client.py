"""The Scholar Sidekick REST clients.

``ScholarSidekick`` is the sync client; ``AsyncScholarSidekick`` is its async
mirror. Both build requests and interpret responses through the same helpers in
``_http`` and the same planning logic in ``audit``, so they cannot drift apart in
what they send or how they read the answer — only in how they wait.

Every endpoint works anonymously. An API key raises the rate limit (roughly
fivefold on the free tier) but is never required.
"""

from __future__ import annotations

import asyncio
import time
from collections.abc import Sequence
from typing import Any, Optional, Union

import httpx

from . import audit as _audit
from ._http import (
    RETRYABLE_STATUSES,
    backoff_delay,
    build_url,
    interpret,
    new_idempotency_key,
    rate_limit_remaining,
    retry_after_seconds,
)
from .audit import AUDIT_MAX_ENTRIES, ProgressCallback
from .config import Config, resolve_config
from .errors import TransportError
from .models import (
    AuditReport,
    FormatItemsResult,
    FormatResult,
    VerifyResult,
)

__all__ = ["ScholarSidekick", "AsyncScholarSidekick", "AUDIT_MAX_ENTRIES"]

# Every `/api/*` path this client pins. The endpoint-contract test asserts this
# matches the paths actually referenced below, and the live check asserts each is
# still documented in the published OpenAPI spec. Keep sorted.
# `/api/detect` and `/api/lookup` are deliberately absent: both are live routes,
# but neither appears in the published OpenAPI spec, so pinning them from a
# released package would either freeze them or break installed users.
_ENDPOINTS = {
    "audit": "/api/audit",
    "export": "/api/export",
    "format": "/api/format",
    "format_items": "/api/format-items",
    "health": "/api/health",
    "verify": "/api/verify",
}

_MUTATING = frozenset({"POST"})


def _audit_body(
    *,
    bibliography: Optional[str],
    claims: Optional[Sequence[dict[str, Any]]],
    references: Optional[Sequence[str]],
    checks: Optional[Sequence[str]],
    format: Optional[str],
) -> dict[str, Any]:
    """Build an ``/api/audit`` body.

    The server's schema is strict and rejects unknown keys outright, and requires
    exactly one of the three input kinds — so this validates locally rather than
    spending a network round trip to be told.
    """
    provided = [
        k
        for k, v in (("bibliography", bibliography), ("claims", claims), ("references", references))
        if v is not None
    ]
    if len(provided) != 1:
        raise ValueError(
            "audit requires exactly one of bibliography=, claims= or references= "
            f"(got: {', '.join(provided) or 'none'})"
        )

    body: dict[str, Any] = {}
    if bibliography is not None:
        body["bibliography"] = bibliography
    elif claims is not None:
        body["claims"] = list(claims)
    else:
        body["references"] = list(references or [])

    if format is not None:
        body["format"] = format
    if checks is not None:
        body["options"] = {"checks": list(checks)}
    return body


class _ClientBase:
    """Configuration and request-shaping shared by both clients."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
        connect_timeout: float = 10.0,
        max_retries: int = 2,
    ) -> None:
        self.config: Config = resolve_config(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            connect_timeout=connect_timeout,
            max_retries=max_retries,
        )

    def _request_args(
        self,
        method: str,
        path: str,
        *,
        json: Optional[dict[str, Any]] = None,
        params: Optional[dict[str, Any]] = None,
        idempotency_key: Optional[str] = None,
    ) -> dict[str, Any]:
        headers = self.config.headers()
        if method in _MUTATING:
            headers["Idempotency-Key"] = idempotency_key or new_idempotency_key()
        args: dict[str, Any] = {
            "method": method,
            "url": build_url(self.config.base_url, path),
            "headers": headers,
        }
        if json is not None:
            args["json"] = json
        if params:
            args["params"] = params
        return args

    @staticmethod
    def _checks_params(
        checks: Optional[Sequence[str]] = None,
        provenance: Optional[str] = None,
    ) -> dict[str, Any]:
        params: dict[str, Any] = {}
        if checks:
            params["checks"] = ",".join(checks)
        if provenance:
            params["provenance"] = provenance
        return params

    @staticmethod
    def _format_body(
        text: Optional[str],
        lines: Optional[Sequence[str]],
        style: Optional[str],
        output: Optional[str],
    ) -> dict[str, Any]:
        if (text is None) == (lines is None):
            raise ValueError("format() requires exactly one of text= or lines=")
        body: dict[str, Any] = {"text": text} if text is not None else {"lines": list(lines or [])}
        if style is not None:
            body["style"] = style
        if output is not None:
            body["output"] = output
        return body


class ScholarSidekick(_ClientBase):
    """Synchronous Scholar Sidekick client.

    >>> client = ScholarSidekick()
    >>> result = client.format(text="10.1038/nphys1170", style="vancouver")
    >>> print(result.text)

    Usable as a context manager to close the underlying connection pool.
    """

    def __init__(self, api_key: Optional[str] = None, **kwargs: Any) -> None:
        super().__init__(api_key, **kwargs)
        self._client = httpx.Client(
            timeout=httpx.Timeout(self.config.timeout, connect=self.config.connect_timeout)
        )

    def __enter__(self) -> ScholarSidekick:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    def close(self) -> None:
        self._client.close()

    def _send(
        self,
        method: str,
        path: str,
        *,
        json: Optional[dict[str, Any]] = None,
        params: Optional[dict[str, Any]] = None,
        expect: str = "json",
        idempotency_key: Optional[str] = None,
    ) -> Union[dict[str, Any], str]:
        args = self._request_args(
            method, path, json=json, params=params, idempotency_key=idempotency_key
        )
        attempts = self.config.max_retries + 1
        last_exc: Optional[BaseException] = None

        for attempt in range(1, attempts + 1):
            try:
                response = self._client.request(**args)
            except httpx.HTTPError as exc:
                last_exc = TransportError(f"Request to {path} failed: {exc}")
                if attempt < attempts:
                    time.sleep(backoff_delay(attempt))
                    continue
                raise last_exc from exc

            if response.status_code in RETRYABLE_STATUSES and attempt < attempts:
                time.sleep(backoff_delay(attempt, retry_after=retry_after_seconds(response)))
                continue

            self._last_response = response
            return interpret(response, expect=expect)

        raise last_exc or TransportError(f"Request to {path} failed")  # pragma: no cover

    # -- endpoints ---------------------------------------------------------

    def health(self) -> dict[str, Any]:
        """Service liveness and diagnostics."""
        result = self._send("GET", _ENDPOINTS["health"])
        return result if isinstance(result, dict) else {}

    def format(
        self,
        *,
        text: Optional[str] = None,
        lines: Optional[Sequence[str]] = None,
        style: Optional[str] = None,
        output: Optional[str] = None,
        checks: Optional[Sequence[str]] = None,
        provenance: Optional[str] = None,
    ) -> FormatResult:
        """Resolve identifiers and format them.

        Returns whole-batch ``text``/``html`` strings covering every input, not
        one string per item — see :class:`~scholar_sidekick.models.FormatResult`.
        """
        payload = self._send(
            "POST",
            _ENDPOINTS["format"],
            json=self._format_body(text, lines, style, output),
            params=self._checks_params(checks, provenance),
        )
        return FormatResult.from_response(payload if isinstance(payload, dict) else {})

    def format_items(
        self,
        items: Sequence[dict[str, Any]],
        *,
        style: Optional[str] = None,
        output: Optional[str] = None,
        checks: Optional[Sequence[str]] = None,
        provenance: Optional[str] = None,
    ) -> FormatItemsResult:
        """Format already-resolved CSL-JSON items. The formatted string is ``.output``."""
        body: dict[str, Any] = {"items": list(items)}
        if style is not None:
            body["style"] = style
        if output is not None:
            body["output"] = output
        payload = self._send(
            "POST",
            _ENDPOINTS["format_items"],
            json=body,
            params=self._checks_params(checks, provenance),
        )
        return FormatItemsResult.from_response(payload if isinstance(payload, dict) else {})

    def export(
        self,
        *,
        text: Optional[str] = None,
        items: Optional[Sequence[dict[str, Any]]] = None,
        format: str = "ris",
        style: Optional[str] = None,
    ) -> str:
        """Export citations to a bibliography file format. Returns the file body as text."""
        if (text is None) == (items is None):
            raise ValueError("export() requires exactly one of text= or items=")
        body: dict[str, Any] = {"format": format}
        if text is not None:
            body["text"] = text
        else:
            body["items"] = list(items or [])
        if style is not None:
            body["style"] = style
        result = self._send("POST", _ENDPOINTS["export"], json=body, expect="text")
        return result if isinstance(result, str) else str(result)

    def verify(
        self,
        *,
        title: str,
        doi: Optional[str] = None,
        pmid: Optional[str] = None,
        pmcid: Optional[str] = None,
        isbn: Optional[str] = None,
        arxiv: Optional[str] = None,
        issn: Optional[str] = None,
        ads: Optional[str] = None,
        who_iris_url: Optional[str] = None,
        authors: Optional[Sequence[dict[str, str]]] = None,
        year: Optional[int] = None,
        container: Optional[str] = None,
        bypass_cache: bool = False,
    ) -> VerifyResult:
        """Check a claimed citation against the record its identifier resolves to.

        A ``mismatch`` verdict is returned as a value, never raised — it is the
        expected outcome for a fabricated citation and the reason this method
        exists. Following a DOI to see whether it loads does not catch that case;
        comparing the claimed title against the resolved record does.
        """
        claimed: dict[str, Any] = {"title": title}
        for key, value in (
            ("doi", doi),
            ("pmid", pmid),
            ("pmcid", pmcid),
            ("isbn", isbn),
            ("arxiv", arxiv),
            ("issn", issn),
            ("ads", ads),
            ("whoIrisUrl", who_iris_url),
        ):
            if value:
                claimed[key] = value
        if authors:
            claimed["authors"] = list(authors)
        if year is not None:
            claimed["year"] = year
        if container:
            claimed["container"] = container

        body: dict[str, Any] = {"claimed": claimed}
        if bypass_cache:
            body["options"] = {"bypassCache": True}
        payload = self._send("POST", _ENDPOINTS["verify"], json=body)
        return VerifyResult.from_response(payload if isinstance(payload, dict) else {})

    def audit(
        self,
        *,
        bibliography: Optional[str] = None,
        claims: Optional[Sequence[dict[str, Any]]] = None,
        references: Optional[Sequence[str]] = None,
        checks: Optional[Sequence[str]] = None,
        format: Optional[str] = None,
    ) -> AuditReport:
        """Audit up to 25 references in a single call.

        For longer bibliographies use :meth:`audit_bibliography`, which chunks and
        paces automatically.
        """
        body = _audit_body(
            bibliography=bibliography,
            claims=claims,
            references=references,
            checks=checks,
            format=format,
        )
        payload = self._send("POST", _ENDPOINTS["audit"], json=body)
        report = AuditReport()
        # Pass the caller's own entries so results can name the claim they came
        # from. A raw `bibliography` string has no per-entry list to map back to.
        supplied = list(claims or references or [])
        chunk = _audit.Chunk(index=0, offset=0, items=supplied)
        if isinstance(payload, dict):
            _audit.accumulate(report, payload, chunk=chunk)
        return report

    def audit_bibliography(
        self,
        entries: Sequence[Any],
        *,
        kind: str = "claims",
        checks: Optional[Sequence[str]] = None,
        progress: Optional[ProgressCallback] = None,
        stop_on_error: bool = False,
    ) -> AuditReport:
        """Audit a bibliography of any length, chunking and pacing automatically.

        Chunks of 25 are sent **serially** — the server already fans out
        internally, so parallelising here would compete with it for the same
        upstream budget — and the pause between chunks is driven by the server's
        own rate-limit headers.

        A chunk that fails is recorded in ``report.errors`` and the run continues,
        so one transient upstream failure does not discard several minutes of
        completed work. Check ``report.complete`` to see whether anything was lost.

        Args:
            entries: Reference dicts (``kind="claims"``) or raw strings
                (``kind="references"``).
            kind: ``"claims"`` for parsed references with a ``title``;
                ``"references"`` for raw prose strings, which are verified by
                containment instead of comparison.
            checks: Enrichment checks; defaults to retraction screening. Pass
                ``[]`` to skip.
            progress: Called as ``progress(chunks_done, chunks_total)``.
            stop_on_error: Raise on the first failed chunk instead of continuing.

        Returns:
            An :class:`~scholar_sidekick.models.AuditReport` whose entry indices
            refer to positions in ``entries``.
        """
        chunks = _audit.plan_chunks(entries)
        report = AuditReport()
        warned = False

        for chunk in chunks:
            is_last = chunk.index == len(chunks) - 1
            claims = None if kind == "references" else list(chunk.items)
            references = [str(item) for item in chunk.items] if kind == "references" else None

            try:
                body = _audit_body(
                    bibliography=None,
                    claims=claims,
                    references=references,
                    checks=checks,
                    format=None,
                )
                payload = self._send("POST", _ENDPOINTS["audit"], json=body)
                if isinstance(payload, dict):
                    _audit.accumulate(report, payload, chunk=chunk)
            except Exception as exc:  # noqa: BLE001 - recorded, see stop_on_error
                if stop_on_error:
                    raise
                _audit.record_failure(report, chunk, exc)

            if progress is not None:
                progress(chunk.index + 1, len(chunks))

            last = getattr(self, "_last_response", None)
            remaining = rate_limit_remaining(last) if last is not None else None
            delay = _audit.pace_delay(remaining, is_last=is_last)
            if delay:
                warned = _audit.warn_rate_limited(warned)
                time.sleep(delay)

        return report


class AsyncScholarSidekick(_ClientBase):
    """Asynchronous Scholar Sidekick client.

    Mirrors :class:`ScholarSidekick` method for method; only the awaiting differs.

    >>> async with AsyncScholarSidekick() as client:
    ...     result = await client.verify(title="…", doi="10.1038/nphys1170")
    """

    def __init__(self, api_key: Optional[str] = None, **kwargs: Any) -> None:
        super().__init__(api_key, **kwargs)
        self._client = httpx.AsyncClient(
            timeout=httpx.Timeout(self.config.timeout, connect=self.config.connect_timeout)
        )

    async def __aenter__(self) -> AsyncScholarSidekick:
        return self

    async def __aexit__(self, *exc_info: object) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        await self._client.aclose()

    async def _send(
        self,
        method: str,
        path: str,
        *,
        json: Optional[dict[str, Any]] = None,
        params: Optional[dict[str, Any]] = None,
        expect: str = "json",
        idempotency_key: Optional[str] = None,
    ) -> Union[dict[str, Any], str]:
        args = self._request_args(
            method, path, json=json, params=params, idempotency_key=idempotency_key
        )
        attempts = self.config.max_retries + 1
        last_exc: Optional[BaseException] = None

        for attempt in range(1, attempts + 1):
            try:
                response = await self._client.request(**args)
            except httpx.HTTPError as exc:
                last_exc = TransportError(f"Request to {path} failed: {exc}")
                if attempt < attempts:
                    await asyncio.sleep(backoff_delay(attempt))
                    continue
                raise last_exc from exc

            if response.status_code in RETRYABLE_STATUSES and attempt < attempts:
                await asyncio.sleep(
                    backoff_delay(attempt, retry_after=retry_after_seconds(response))
                )
                continue

            self._last_response = response
            return interpret(response, expect=expect)

        raise last_exc or TransportError(f"Request to {path} failed")  # pragma: no cover

    async def health(self) -> dict[str, Any]:
        """Service liveness and diagnostics."""
        result = await self._send("GET", _ENDPOINTS["health"])
        return result if isinstance(result, dict) else {}

    async def format(
        self,
        *,
        text: Optional[str] = None,
        lines: Optional[Sequence[str]] = None,
        style: Optional[str] = None,
        output: Optional[str] = None,
        checks: Optional[Sequence[str]] = None,
        provenance: Optional[str] = None,
    ) -> FormatResult:
        """Resolve identifiers and format them. Returns whole-batch strings."""
        payload = await self._send(
            "POST",
            _ENDPOINTS["format"],
            json=self._format_body(text, lines, style, output),
            params=self._checks_params(checks, provenance),
        )
        return FormatResult.from_response(payload if isinstance(payload, dict) else {})

    async def format_items(
        self,
        items: Sequence[dict[str, Any]],
        *,
        style: Optional[str] = None,
        output: Optional[str] = None,
        checks: Optional[Sequence[str]] = None,
        provenance: Optional[str] = None,
    ) -> FormatItemsResult:
        """Format already-resolved CSL-JSON items. The formatted string is ``.output``."""
        body: dict[str, Any] = {"items": list(items)}
        if style is not None:
            body["style"] = style
        if output is not None:
            body["output"] = output
        payload = await self._send(
            "POST",
            _ENDPOINTS["format_items"],
            json=body,
            params=self._checks_params(checks, provenance),
        )
        return FormatItemsResult.from_response(payload if isinstance(payload, dict) else {})

    async def export(
        self,
        *,
        text: Optional[str] = None,
        items: Optional[Sequence[dict[str, Any]]] = None,
        format: str = "ris",
        style: Optional[str] = None,
    ) -> str:
        """Export citations to a bibliography file format. Returns the file body as text."""
        if (text is None) == (items is None):
            raise ValueError("export() requires exactly one of text= or items=")
        body: dict[str, Any] = {"format": format}
        if text is not None:
            body["text"] = text
        else:
            body["items"] = list(items or [])
        if style is not None:
            body["style"] = style
        result = await self._send("POST", _ENDPOINTS["export"], json=body, expect="text")
        return result if isinstance(result, str) else str(result)

    async def verify(
        self,
        *,
        title: str,
        doi: Optional[str] = None,
        pmid: Optional[str] = None,
        pmcid: Optional[str] = None,
        isbn: Optional[str] = None,
        arxiv: Optional[str] = None,
        issn: Optional[str] = None,
        ads: Optional[str] = None,
        who_iris_url: Optional[str] = None,
        authors: Optional[Sequence[dict[str, str]]] = None,
        year: Optional[int] = None,
        container: Optional[str] = None,
        bypass_cache: bool = False,
    ) -> VerifyResult:
        """Check a claimed citation against the record its identifier resolves to.

        A ``mismatch`` verdict is returned as a value, never raised.
        """
        claimed: dict[str, Any] = {"title": title}
        for key, value in (
            ("doi", doi),
            ("pmid", pmid),
            ("pmcid", pmcid),
            ("isbn", isbn),
            ("arxiv", arxiv),
            ("issn", issn),
            ("ads", ads),
            ("whoIrisUrl", who_iris_url),
        ):
            if value:
                claimed[key] = value
        if authors:
            claimed["authors"] = list(authors)
        if year is not None:
            claimed["year"] = year
        if container:
            claimed["container"] = container

        body: dict[str, Any] = {"claimed": claimed}
        if bypass_cache:
            body["options"] = {"bypassCache": True}
        payload = await self._send("POST", _ENDPOINTS["verify"], json=body)
        return VerifyResult.from_response(payload if isinstance(payload, dict) else {})

    async def audit(
        self,
        *,
        bibliography: Optional[str] = None,
        claims: Optional[Sequence[dict[str, Any]]] = None,
        references: Optional[Sequence[str]] = None,
        checks: Optional[Sequence[str]] = None,
        format: Optional[str] = None,
    ) -> AuditReport:
        """Audit up to 25 references in a single call."""
        body = _audit_body(
            bibliography=bibliography,
            claims=claims,
            references=references,
            checks=checks,
            format=format,
        )
        payload = await self._send("POST", _ENDPOINTS["audit"], json=body)
        report = AuditReport()
        # Pass the caller's own entries so results can name the claim they came
        # from. A raw `bibliography` string has no per-entry list to map back to.
        supplied = list(claims or references or [])
        chunk = _audit.Chunk(index=0, offset=0, items=supplied)
        if isinstance(payload, dict):
            _audit.accumulate(report, payload, chunk=chunk)
        return report

    async def audit_bibliography(
        self,
        entries: Sequence[Any],
        *,
        kind: str = "claims",
        checks: Optional[Sequence[str]] = None,
        progress: Optional[ProgressCallback] = None,
        stop_on_error: bool = False,
    ) -> AuditReport:
        """Audit a bibliography of any length, chunking and pacing automatically.

        Chunks run serially even here: the constraint is the server's upstream
        fan-out budget, not this client's concurrency.
        """
        chunks = _audit.plan_chunks(entries)
        report = AuditReport()
        warned = False

        for chunk in chunks:
            is_last = chunk.index == len(chunks) - 1
            claims = None if kind == "references" else list(chunk.items)
            references = [str(item) for item in chunk.items] if kind == "references" else None

            try:
                body = _audit_body(
                    bibliography=None,
                    claims=claims,
                    references=references,
                    checks=checks,
                    format=None,
                )
                payload = await self._send("POST", _ENDPOINTS["audit"], json=body)
                if isinstance(payload, dict):
                    _audit.accumulate(report, payload, chunk=chunk)
            except Exception as exc:  # noqa: BLE001 - recorded, see stop_on_error
                if stop_on_error:
                    raise
                _audit.record_failure(report, chunk, exc)

            if progress is not None:
                progress(chunk.index + 1, len(chunks))

            last = getattr(self, "_last_response", None)
            remaining = rate_limit_remaining(last) if last is not None else None
            delay = _audit.pace_delay(remaining, is_last=is_last)
            if delay:
                warned = _audit.warn_rate_limited(warned)
                await asyncio.sleep(delay)

        return report
