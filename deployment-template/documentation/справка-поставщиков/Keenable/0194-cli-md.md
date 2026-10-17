> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Keenable: cli-md

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.keenable.ai/llms.txt
> Use this file to discover all available pages before exploring further.

## # CLI

> Authenticate, configure MCP, and search from the terminal

[`keenable-cli`](https://github.com/keenableai/keenable-cli) is a single-binary CLI for Keenable — configure MCP for your AI clients, search the web, and manage API keys from the terminal.
Run `keenable login` once to authenticate; the CLI stores your credentials and reuses them for every command. See authentication (локальный ресурс исходного примера не включён) for the details, and rate limits (локальный ресурс исходного примера не включён) for the caps that apply with and without a key.

## Installation

<CodeGroup>
  ```bash Homebrew theme={"system"}
  brew install keenableai/tap/keenable-cli
  ```

  ```bash macOS / Linux theme={"system"}
  curl --proto '=https' --tlsv1.2 -LsSf \
    https://github.com/keenableai/keenable-cli/releases/latest/download/keenable-cli-installer.sh \
    | sh
  ```

  ```powershell PowerShell theme={"system"}
  irm https://github.com/keenableai/keenable-cli/releases/latest/download/keenable-cli-installer.ps1 | iex
  ```

  ```bash Source theme={"system"}
  cargo install --git https://github.com/keenableai/keenable-cli
  ```
</CodeGroup>

## Quick start

```bash theme={"system"}
# Login with your Keenable account
keenable login

# Configure MCP for your AI clients (Claude Code, Cursor, etc.)
keenable configure-mcp --all

# Search the web
keenable search "rust async patterns" -p
```

## Authentication

```bash theme={"system"}
# Device-code login (opens browser)
keenable login

# Save API key directly (CI, servers)
keenable login --api-key <KEY>

# Clear stored credentials
keenable logout
```

## MCP setup

```bash theme={"system"}
# Show client status
keenable configure-mcp

# Configure all detected clients
keenable configure-mcp --all

# Configure a specific client
keenable configure-mcp --cursor

# Remove Keenable from all clients
keenable reset --all
```

Supported clients: Claude Code, Cursor, Windsurf, Codex, OpenCode.

## Search

```bash theme={"system"}
# YAML output (for agents)
keenable search "AI news"

# Pretty output (for humans)
keenable search "AI news" -p

# Restrict to site
keenable search "AI news" --site techcrunch.com

# Date filter
keenable search "AI news" --published-after 2026-01-01

# Date filter
keenable search "AI news" --acquired-before 2026-05-01

# Longer snippets, in characters (180-10000)
keenable search "rust async" --snippet-max-length 2000

# More results (1-50, default 10)
keenable search "rust async" --max-results 25

# Point-in-time search: the index as it stood then
keenable search "AI news" --query-time 2026-01-01T00:00:00Z

# Use a specific API key
keenable search "AI news" --api-key KEY
```

### Date and time filters

`--acquired-after`, `--acquired-before`, `--published-after`, and `--published-before` each accept **one** of the following formats:

* **Date** in RFC 3339 `full-date` form (`YYYY-MM-DD`) — covers that whole day in UTC. On an `--*-after` flag it resolves to `00:00:00` on that date; on a `--*-before` flag it resolves to `23:59:59.999` on that date, so pages from the named day are kept at either end. Pass a timestamp instead to cut at an exact instant.
* **Timestamp** in ISO 8601 form (`YYYY-MM-DDTHH:MM:SS[.sss][±HH:MM]`). When a timezone offset is not provided, the timezone is interpreted as UTC.
* **Relative delta** (`<number><unit>`, e.g. `7d`, `30min`) — resolves to the request time minus the delta, truncated to minute precision, or to [`--query-time`](#point-in-time-search) minus the delta when that is set. Supported units: `min` (minutes), `h` (hours), `d` (days), `mo` (months), `y` (years).

```bash theme={"system"}
# Resolves to 2026-01-15T00:00:00Z
keenable search "AI news" --published-after 2026-01-15

# Resolves to 2026-01-15T23:59:59.999Z — the 15th is kept
keenable search "AI news" --published-before 2026-01-15

# No offset → UTC
keenable search "AI news" --published-after 2026-01-15T10:30:00
keenable search "AI news" --published-after 2026-01-15T10:30:00.500-05:00

# 7 days before request time
keenable search "AI news" --acquired-after 7d

# 30 minutes before request time
keenable search "AI news" --acquired-after 30min
```

Relative deltas may be combined with absolute values across the two bounds of a window:

```bash theme={"system"}
keenable search "AI news" --published-after 1y --published-before 6mo
keenable search "AI news" --acquired-after 2024-01-01 --acquired-before 30d
```

For example, at request time `2026-05-18T14:23:45Z`, `--acquired-after 2h` resolves to `2026-05-18T12:23:00Z` — a document acquired at `12:22:59Z` is dropped, one acquired at `12:23:00Z` is kept.

Mind the difference between a date and a timestamp on a `--*-before` flag: `--acquired-before 2026-05-01` keeps a page acquired at `2026-05-01T14:31:13Z`, while `--acquired-before 2026-05-01T00:00:00Z` drops it. Use the date form to mean "up to and including that day", and the timestamp form to cut at midnight.

### Point-in-time search

`--query-time` moves the whole search back to an instant: a page acquired after it is not a candidate at all, so the answer is the one the index would have given then rather than today's answer filtered down. It takes the same formats as the filters above.

```bash theme={"system"}
keenable search "champions league final" --query-time 2025-05-30T00:00:00Z
```

It also **re-bases every relative delta in the same command**. A delta resolves against the request time only when `--query-time` is absent; with it, `--published-after 30d` means thirty days before `--query-time`:

```bash theme={"system"}
keenable search "cloud computing" --query-time 2026-06-13T00:00:00Z --published-after 30d
```

returns pages published between `2026-05-14` and `2026-06-13` — not the last thirty days. Absolute bounds are unaffected.

A date-only `--query-time` resolves to `00:00:00` UTC, which is the opposite end of the day from a date-only `--*-before` flag: `--query-time 2026-06-13` cuts at the start of 13 June, while `--acquired-before 2026-06-13` keeps all of it.

## Fetch

```bash theme={"system"}
# Fetch page content (YAML)
keenable fetch https://example.com

# Pretty output
keenable fetch https://example.com -p

# LLM extraction: return only the instruction's output instead of the full page
keenable fetch https://example.com --prompt "List all pricing tiers with their monthly prices"
```

## Updating

The CLI checks for updates automatically once per hour. To update manually:

```bash theme={"system"}
# Homebrew
brew update && brew upgrade keenable-cli
```

Or re-run the installer script.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
