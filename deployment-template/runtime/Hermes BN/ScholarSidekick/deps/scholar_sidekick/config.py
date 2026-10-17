"""Client configuration: base URL, auth resolution and the client handshake tag."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional

__all__ = ["Config", "DEFAULT_BASE_URL", "CLIENT_NAME", "client_tag", "resolve_config"]

DEFAULT_BASE_URL = "https://scholar-sidekick.com"

# The handshake-tag suffix. Must stay exactly "python": the server maps
# `scholar-sidekick-<suffix>` to a funnel surface through a closed lookup table,
# and an unlisted suffix silently falls back to the generic "api" surface.
CLIENT_NAME = "scholar-sidekick-python"

ENV_API_KEY = "SCHOLAR_SIDEKICK_API_KEY"
ENV_BASE_URL = "SCHOLAR_SIDEKICK_BASE_URL"


def _version() -> str:
    """The installed package version — the single source of the version string."""
    try:
        from importlib.metadata import version

        return version("scholar-sidekick")
    except Exception:  # pragma: no cover - only when running from a bare checkout
        return "0.0.0+unknown"


def client_tag() -> str:
    """The ``X-Scholar-Client`` value, e.g. ``scholar-sidekick-python/0.1.0``."""
    return f"{CLIENT_NAME}/{_version()}"


@dataclass(frozen=True)
class Config:
    """Resolved client configuration."""

    base_url: str = DEFAULT_BASE_URL
    api_key: Optional[str] = None
    timeout: float = 30.0
    connect_timeout: float = 10.0
    max_retries: int = 2

    @property
    def is_authenticated(self) -> bool:
        return bool(self.api_key)

    def headers(self) -> dict[str, str]:
        """Base headers for every request.

        ``X-Scholar-Client`` is always present and is not user-suppressible: it
        is the only mechanism by which this package's usage is attributable
        server-side, and a sibling client that stopped sending it once already
        made an entire surface report zero traffic.
        """
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": client_tag(),
            "X-Scholar-Client": client_tag(),
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers


def resolve_config(
    *,
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
    timeout: float = 30.0,
    connect_timeout: float = 10.0,
    max_retries: int = 2,
) -> Config:
    """Resolve configuration from explicit arguments, then environment, then defaults.

    Auth precedence is explicit argument > ``SCHOLAR_SIDEKICK_API_KEY`` > anonymous.
    Anonymous is a fully supported first-class path — every endpoint this client
    wraps works without a key, at a lower rate limit.
    """
    key = api_key if api_key is not None else os.environ.get(ENV_API_KEY) or None
    url = base_url or os.environ.get(ENV_BASE_URL) or DEFAULT_BASE_URL
    return Config(
        base_url=url.rstrip("/"),
        api_key=key,
        timeout=timeout,
        connect_timeout=connect_timeout,
        max_retries=max_retries,
    )
