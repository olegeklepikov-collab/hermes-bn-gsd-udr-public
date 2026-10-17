> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Firecrawl: browser

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


https://docs.firecrawl.dev/features/browser

> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.firecrawl.dev/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.firecrawl.dev/features/browser#content-area)

For agent workflows, use [Interact](https://docs.firecrawl.dev/features/interact). Interact is the supported CLI/MCP path and can be driven with prompts or code after a scrape; MCP also supports opening from a URL directly.

| Surface | Use it for | Entry point | Agent surface |
| --- | --- | --- | --- |
| Browser Sandbox | Standalone browser sessions for API/SDK users that need a sandbox, CDP URL, live view, or persistent session lifecycle | `POST /v2/interact` | API and SDKs; hidden CLI browser command is legacy |
| Interact | Acting on a scraped page; MCP can also open from a URL with `firecrawl_interact` URL mode | `POST /v2/scrape/{scrapeId}/interact`, CLI `interact` after scrape, or MCP `firecrawl_interact` | Recommended for CLI/MCP agent workflows |

Firecrawl Browser Sandbox gives API and SDK users a secure browser environment where agents can interact with the web. Fill out forms, click buttons, authenticate, and more.
No local setup, no Chromium installs, no driver compatibility issues. Agent browser and playwright are pre-installed.Available via [API](https://docs.firecrawl.dev/api-reference/endpoint/browser-create), [Node SDK](https://docs.firecrawl.dev/sdks/node#browser), [Python SDK](https://docs.firecrawl.dev/sdks/python#browser), and [Vercel AI SDK](https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/vercel-ai-sdk). The hidden `firecrawl browser` CLI command is legacy; CLI and MCP agent flows should use scrape + interact instead.To add Interact support to an AI coding agent (Claude Code, Codex, Open Code, Cursor, etc.), install the Firecrawl skill:

```
npx -y firecrawl-cli@latest init --all --browser
```

Each session runs in an isolated, disposable or persistent sandbox that scales without managing infrastructure.

## [​](https://docs.firecrawl.dev/features/browser\#quick-start)  Quick Start

Create a session, execute code, and close it:

Node

Python

## CLI

cURL

```
// npm install firecrawl
import { Firecrawl } from 'firecrawl';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

// 1. Launch a session
const session = await firecrawl.browser();
console.log(session.cdpUrl); // wss://cdp-proxy.firecrawl.dev/cdp/...

// 2. Execute code
const result = await firecrawl.browserExecute(session.id, {
  code: `
    await page.goto("https://news.ycombinator.com");
    const title = await page.title();
    console.log(title);
  `,
  language: "node",
});
console.log(result.result); // "Hacker News"

// 3. Close
await firecrawl.deleteBrowser(session.id);
```

```
# pip install firecrawl
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR-API-KEY")

# 1. Launch a session
session = app.browser()
print(session.cdp_url)  # wss://cdp-proxy.firecrawl.dev/cdp/...

# 2. Execute code
result = app.browser_execute(
    session.id,
    code='await page.goto("https://news.ycombinator.com")\ntitle = await page.title()\nprint(title)',
    language="python",
)
print(result.result)  # "Hacker News"

# 3. Close
app.delete_browser(session.id)
```

```
# Install the Firecrawl CLI
npm install -g firecrawl-cli

# Shorthand - auto-launches a session, no "execute" needed
firecrawl browser "open https://news.ycombinator.com"
firecrawl browser "snapshot"
firecrawl browser "scrape"

# Close when done
firecrawl browser close
```

```
# 1. Launch a session
curl -X POST "https://api.firecrawl.dev/v2/interact" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json"

# 2. Execute code
curl -X POST "https://api.firecrawl.dev/v2/interact/YOUR_SESSION_ID/execute" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "code": "await page.goto(\"https://news.ycombinator.com\")\ntitle = await page.title()\nprint(title)"
  }'

# 3. Close
curl -X DELETE "https://api.firecrawl.dev/v2/interact/YOUR_SESSION_ID" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY"
```

- **No Driver Installation** \- No Chromium binary, no `playwright install`, no driver compatibility issues
- **Python, JavaScript & Bash** \- Send code via API, CLI, or SDK and get results back. All three languages run remotely in the sandbox
- **agent-browser** \- Pre-installed CLI with 60+ commands. AI agents write simple bash commands instead of Playwright code
- **Playwright loaded** \- Playwright comes pre-installed in the sandbox. Agents can write Playwright code if they prefer.
- **CDP Access** \- Connect your own Playwright instance over WebSocket when you need full control
- **Live View** \- Watch sessions in real time via embeddable stream URL
- **Interactive Live View** \- Let users interact with the browser directly through an embeddable interactive stream

## [​](https://docs.firecrawl.dev/features/browser\#launch-a-session)  Launch a Session

Returns a session ID, CDP URL, and live view URL.

Node

Python

## CLI

cURL

```
import { Firecrawl } from 'firecrawl';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

const session = await firecrawl.browser({
  ttl: 120,
  activityTtl: 60,
});

console.log(session.id);
console.log(session.cdpUrl);      // wss://cdp-proxy.firecrawl.dev/cdp/...
console.log(session.liveViewUrl); // https://liveview.firecrawl.dev/...
```

```
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR-API-KEY")

session = app.browser(
    ttl=120,
    activity_ttl=60,
)

print(session.id)
print(session.cdp_url)        # wss://cdp-proxy.firecrawl.dev/cdp/...
print(session.live_view_url)  # https://liveview.firecrawl.dev/...
```

```
# Launch with live view and custom TTL
firecrawl browser launch-session --stream --ttl 120 --ttl-inactivity 60

# Launch and save session info to file
firecrawl browser launch-session -o session.json --json
```

```
curl -X POST "https://api.firecrawl.dev/v2/interact" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "ttl": 120,
    "activityTtl": 60
  }'
```

Response

```
{
  "success": true,
  "id": "${OBJECT_ID}",
  "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=${SECRET}",
  "liveViewUrl": "https://liveview.firecrawl.dev/...",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
  "expiresAt": "2025-01-15T10:40:00Z"
}
```

## [​](https://docs.firecrawl.dev/features/browser\#execute-code)  Execute Code

Run Python, JavaScript, or bash code in your session. Output is returned via `stdout`; for Node.js, the last expression value is also available in `result`.

Node

Python

## CLI

cURL

cURL (Bash / agent-browser)

```
import { Firecrawl } from 'firecrawl';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

const result = await firecrawl.browserExecute("YOUR_SESSION_ID", {
  code: 'await page.goto("https://example.com"); const title = await page.title(); console.log(title);',
  language: "node",
});

console.log(result);
```

```
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR-API-KEY")

result = app.browser_execute(
##     "YOUR_SESSION_ID",
    code='await page.goto("https://example.com")\ntitle = await page.title()\nprint(title)',
    language="python",
)

print(result)
```

```
# agent-browser commands (default - "agent-browser" is auto-prefixed)
firecrawl browser execute "open https://example.com"
firecrawl browser execute "snapshot"
firecrawl browser execute "scrape"

# Execute Playwright Python code
firecrawl browser execute --python 'await page.goto("https://example.com")
print(await page.title())'

# Execute Playwright JavaScript code
firecrawl browser execute --node 'await page.goto("https://example.com"); document.title'

# Execute arbitrary bash in the sandbox
firecrawl browser execute --bash 'ls /tmp'

# Target a specific session
firecrawl browser execute --session <id> "snapshot"
```

```
# Execute Playwright Python code
curl -X POST "https://api.firecrawl.dev/v2/interact/YOUR_SESSION_ID/execute" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "code": "await page.goto(\"https://example.com\")\ntitle = await page.title()\nprint(title)",
    "language": "python"
  }'

# Execute Playwright JavaScript code
curl -X POST "https://api.firecrawl.dev/v2/interact/YOUR_SESSION_ID/execute" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "code": "await page.goto(\"https://example.com\"); const title = await page.title(); console.log(title);",
    "language": "node"
  }'
```

```
# Navigate to a page
curl -X POST "https://api.firecrawl.dev/v2/interact/YOUR_SESSION_ID/execute" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "code": "agent-browser open https://example.com", "language": "bash" }'

# Get accessibility snapshot with @ref IDs
curl -X POST "https://api.firecrawl.dev/v2/interact/YOUR_SESSION_ID/execute" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "code": "agent-browser snapshot", "language": "bash" }'

# Interact using @ref IDs from the snapshot
curl -X POST "https://api.firecrawl.dev/v2/interact/YOUR_SESSION_ID/execute" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "code": "agent-browser click @e5", "language": "bash" }'

# Extract page content as markdown
curl -X POST "https://api.firecrawl.dev/v2/interact/YOUR_SESSION_ID/execute" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "code": "agent-browser scrape", "language": "bash" }'
```

Response

```
{
  "success": true,
  "stdout": "",
  "result": "Example Domain",
  "stderr": "",
  "exitCode": 0,
  "killed": false
}
```

### [​](https://docs.firecrawl.dev/features/browser\#handling-file-downloads)  Handling File Downloads

Files downloaded inside a session can be captured and returned as base64. Use Playwright’s download API via the execute endpoint:

Python

Node

```
import base64

async with page.expect_download() as download_info:
    await page.click('a#download-link')  # Click the element that triggers the download

download = download_info.value
path = await download.path()

# Optionally save to a known path
# await download.save_as('/tmp/myfile.pdf')

# Read and output file content as base64
with open(path, "rb") as f:
    content = base64.b64encode(f.read()).decode()
    print(content)
```

```
// Get the download URL from the link element
const href = await page.getAttribute('a#download-link', 'href');

// Fetch the file in the browser context and convert to base64
const b64 = await page.evaluate(async (url) => {
  const resp = await fetch(url);
  const blob = await resp.blob();
  return new Promise((resolve) => {
    const reader = new FileReader();
    reader.onloadend = () => resolve(reader.result.split(',')[1]);
    reader.readAsDataURL(blob);
  });
}, href);

process.stdout.write(b64);
```

The sandbox filesystem is ephemeral — downloaded files are lost when the session ends. To persist files, read their content within the session and save it to your own storage. Persistent profiles preserve browser state (cookies, localStorage) but not files on disk.

## [​](https://docs.firecrawl.dev/features/browser\#agent-browser-bash-mode)  agent-browser (Bash Mode)

[agent-browser](https://github.com/vercel-labs/agent-browser) is a headless browser CLI pre-installed in every sandbox. Instead of writing Playwright code, agents send simple bash commands. The CLI auto-injects `--cdp` so agent-browser connects to your active session automatically.

The `firecrawl browser` CLI examples below are for legacy Browser Sandbox sessions. For CLI/MCP agent workflows, prefer `firecrawl interact` or the MCP `firecrawl_interact` tool.

### [​](https://docs.firecrawl.dev/features/browser\#shorthand)  Shorthand

The fastest way to use browser. Both the shorthand and `execute` send commands to agent-browser automatically. The shorthand just skips `execute` and auto-launches a session if needed:

```
firecrawl browser "open https://example.com"
firecrawl browser "snapshot"
firecrawl browser "click @e5"
```

### [​](https://docs.firecrawl.dev/features/browser\#cli)  CLI

The explicit form uses `execute`. Commands are sent to agent-browser automatically — you don’t need to type `agent-browser` or use `--bash`:

Navigate & Snapshot

Interact

```
firecrawl browser execute "open https://example.com"
firecrawl browser execute "snapshot"
```

```
firecrawl browser execute "click @e5"
firecrawl browser execute "fill @e3 'search query'"
firecrawl browser execute "scrape"
```

### [​](https://docs.firecrawl.dev/features/browser\#api-&-sdk)  API & SDK

Use `language: "bash"` to run agent-browser commands via the API or SDKs:

cURL

Node

Python

```
curl -X POST "https://api.firecrawl.dev/v2/interact/YOUR_SESSION_ID/execute" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "code": "agent-browser snapshot",
    "language": "bash"
  }'
```

```
const result = await app.browserExecute(sessionId, {
  code: "agent-browser snapshot",
  language: "bash",
});
```

```
result = app.browser_execute(
    session_id,
    code="agent-browser snapshot",
    language="bash",
)
```

## [​](https://docs.firecrawl.dev/features/browser\#session-management)  Session Management

### [​](https://docs.firecrawl.dev/features/browser\#persistent-sessions)  Persistent Sessions

By default, each browser session starts with a clean slate. With `profile`, you can save and reuse browser state across sessions. This is useful for staying logged in and preserving preferences.To save or select a profile, use the `profile` parameter when creating a session.

Node

Python

cURL

## CLI

```
const session = await firecrawl.browser({
  ttl: 600,
  profile: {
    name: "my-profile",
    saveChanges: true,
  },
});
```

```
session = app.browser(
    ttl=600,
    profile={
        "name": "my-profile",
        "save_changes": True,
    },
)
```

```
curl -X POST "https://api.firecrawl.dev/v2/interact" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "ttl": 600,
    "profile": {
      "name": "my-profile",
      "saveChanges": true
    }
  }'
```

```
# Launch with a profile (saves changes by default)
firecrawl browser launch-session --profile my-profile

# Launch with a profile in read-only mode
firecrawl browser launch-session --profile my-profile --no-save-changes

# Shorthand: launch with profile + execute in one step
firecrawl browser --profile my-profile "open https://example.com"
```

| Parameter | Default | Description |
| --- | --- | --- |
| `name` | — | A name for the persistent profile. Sessions with the same name share storage. |
| `saveChanges` | `true` | When `true`, browser state is saved back to the profile on close. Set to `false` to load existing data without writing — useful when you need multiple concurrent readers. |

Only one session can save to a profile at a time. If another session is already saving, you’ll get a `409` error. You can still open the same profile with `saveChanges: false`, or try again later.

The browser session state only saves when the session is closed. So we recommend closing the browser session when you are done with it so it can be reused. Once a session is closed, its session ID is no longer valid — you cannot reuse it. Instead, create a new session with the same profile name and use the new session ID returned in the response. To save and close it:

Node

Python

## CLI

cURL

```
import { Firecrawl } from 'firecrawl';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

await firecrawl.deleteBrowser("YOUR_SESSION_ID");
```

```
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR-API-KEY")

app.delete_browser("YOUR_SESSION_ID")
```

```
# Close the active session
firecrawl browser close

# Close a specific session
firecrawl browser close --session <id>
```

```
curl -X DELETE "https://api.firecrawl.dev/v2/interact/YOUR_SESSION_ID" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY"
```

### [​](https://docs.firecrawl.dev/features/browser\#list-sessions)  List Sessions

Node

Python

## CLI

cURL

```
import { Firecrawl } from 'firecrawl';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

const { sessions } = await firecrawl.listBrowsers();
console.log(sessions);

// Filter by status
const { sessions: active } = await firecrawl.listBrowsers({ status: "active" });
console.log(active);
```

```
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR-API-KEY")

response = app.list_browsers()
print(response.sessions)
```

```
firecrawl browser list
firecrawl browser list active
```

```
curl -X GET "https://api.firecrawl.dev/v2/interact" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY"

# Filter by status
curl -X GET "https://api.firecrawl.dev/v2/interact?status=active" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY"
```

Response

```
{
  "success": true,
  "sessions": [\
    {\
      "id": "${OBJECT_ID}",\
      "status": "active",\
      "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=${SECRET}",\
      "liveViewUrl": "https://liveview.firecrawl.dev/...",\
      "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",\
      "createdAt": "2025-01-15T10:30:00Z",\
      "lastActivity": "2025-01-15T10:35:00Z"\
    }\
  ]
}
```

### [​](https://docs.firecrawl.dev/features/browser\#ttl-configuration)  TTL Configuration

Sessions have two TTL controls:

| Parameter | Default | Description |
| --- | --- | --- |
| `ttl` | 600s (10 min) | Maximum session lifetime (30-3600s) |
| `activityTtl` | 300s (5 min) | Auto-close after inactivity (10-3600s) |

### [​](https://docs.firecrawl.dev/features/browser\#close-a-session)  Close a Session

Node

Python

## CLI

cURL

```
import { Firecrawl } from 'firecrawl';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

await firecrawl.deleteBrowser("YOUR_SESSION_ID");
```

```
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR-API-KEY")

app.delete_browser("YOUR_SESSION_ID")
```

```
# Close the active session
firecrawl browser close

# Close a specific session
firecrawl browser close --session <id>
```

```
curl -X DELETE "https://api.firecrawl.dev/v2/interact/YOUR_SESSION_ID" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY"
```

## [​](https://docs.firecrawl.dev/features/browser\#live-view)  Live View

Every session returns a `liveViewUrl` in the response that you can embed to watch the browser in real time. Useful for debugging, demos, or building browser-powered UIs.

Response

```
{
  "success": true,
  "id": "${OBJECT_ID}",
  "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=${SECRET}",
  "liveViewUrl": "https://liveview.firecrawl.dev/...",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
  "expiresAt": "2025-01-15T10:40:00Z"
}
```

```
<iframe src="LIVE_VIEW_URL" width="100%" height="600" />
```

### [​](https://docs.firecrawl.dev/features/browser\#interactive-live-view)  Interactive Live View

The response also includes an `interactiveLiveViewUrl`. Unlike the standard live view which is view-only, the interactive live view allows users to click, type, and interact with the browser session directly through the embedded stream. This is useful for building user-facing browser UIs, collaborative debugging, or any scenario where the viewer needs to control the browser.

```
<iframe src="INTERACTIVE_LIVE_VIEW_URL" width="100%" height="600" />
```

## [​](https://docs.firecrawl.dev/features/browser\#connecting-via-cdp)  Connecting via CDP

Every session exposes a CDP WebSocket URL. The execute API and `--bash` flag cover most use cases, but if you need full local control you can connect directly.

TypeScript

Python

agent-browser

```
import { Firecrawl } from 'firecrawl';
import { chromium } from "playwright-core";

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });
const session = await firecrawl.browser();

const browser = await chromium.connectOverCDP(session.cdpUrl);
const context = browser.contexts()[0];
const page = context.pages()[0] || (await context.newPage());

await page.goto("https://example.com");
console.log(await page.title());

await browser.close();
await firecrawl.deleteBrowser(session.id);
```

```
from firecrawl import Firecrawl
from playwright.sync_api import sync_playwright

app = Firecrawl(api_key="fc-YOUR-API-KEY")
session = app.browser()

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(session.cdp_url)
    context = browser.contexts[0]
    page = context.pages[0] if context.pages else context.new_page()

    page.goto("https://example.com")
    print(page.title())

    browser.close()

app.delete_browser(session.id)
```

```
# Use the cdpUrl from the session response
## CDP_URL=YOUR_SESSION_CDP_URL

agent-browser open https://example.com --cdp "$CDP_URL"
agent-browser snapshot --cdp "$CDP_URL"
```

## [​](https://docs.firecrawl.dev/features/browser\#when-to-use-browser)  When to Use Browser

| Use Case | Right Tool |
| --- | --- |
| Extract content from a known URL | [Scrape](https://docs.firecrawl.dev/features/scrape) |
| Search the web and get results | [Search](https://docs.firecrawl.dev/features/search) |
| Navigate pagination, fill forms, click through flows | **Browser** |
| Multi-step workflows with interaction | **Browser** |
| Parallel browsing across many sites | **Browser** (each session is isolated) |

## [​](https://docs.firecrawl.dev/features/browser\#use-cases)  Use Cases

- **Competitive intelligence** \- Browse competitor sites, navigate search forms and filters, extract pricing and features into structured data
- **Knowledge base ingestion** \- Navigate help centers, docs, and support portals that require clicks, pagination, or authentication
- **Market research** \- Launch parallel browser sessions to build datasets from job boards, real estate listings, or legal databases

## [​](https://docs.firecrawl.dev/features/browser\#pricing)  Pricing

Pricing depends on how you drive the session: 7 credits per browser minute if the session uses a `prompt`, or 2 credits per browser minute if it does not (Playwright `code` only). Billing is per browser minute with a one-minute minimum.

## [​](https://docs.firecrawl.dev/features/browser\#rate-limits)  Rate limits

For the initial launch, we allow all plans up to have up to 20 concurrent browser sessions.

## [​](https://docs.firecrawl.dev/features/browser\#api-reference)  API Reference

- [Create Browser Session](https://docs.firecrawl.dev/api-reference/endpoint/browser-create)
- [Execute Browser Code](https://docs.firecrawl.dev/api-reference/endpoint/browser-execute)
- [List Browser Sessions](https://docs.firecrawl.dev/api-reference/endpoint/browser-list)
- [Delete Browser Session](https://docs.firecrawl.dev/api-reference/endpoint/browser-delete)

* * *

Have feedback or need help? Email [help@firecrawl.com](mailto:help@firecrawl.com) or reach out on [Discord](https://discord.gg/firecrawl).

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

[Suggest edits](https://github.com/firecrawl/firecrawl-docs/edit/main/features/browser.mdx) [Raise issue](https://github.com/firecrawl/firecrawl-docs/issues/new?title=Issue%20on%20docs&body=Path:%20/features/browser)

✕
