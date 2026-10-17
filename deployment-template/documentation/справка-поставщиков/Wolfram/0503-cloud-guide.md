> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Wolfram: cloud-guide

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


<div class="page-width">

<div class="page-padding">

<div class="section">

<div id="view">

# Connecting to Wolfram Cloud MCP

Server URL:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/server-url.txt">

``` text
https://agenttools.wolfram.com/mcp
```

</div>

This guide covers how to connect various LLM applications and IDEs to [Wolfram Cloud MCP](https://www.wolfram.com/artificial-intelligence/mcp/cloud/) using the Streamable HTTP transport (the current recommended standard). SSE (server-sent events) transport is deprecated in the MCP specification but noted where still relevant.

For information on how to connect to Wolfram Local MCP instead, go [here](https://www.wolfram.com/artificial-intelligence/mcp/local/wolfram-mcp-local/).

------------------------------------------------------------------------

## Table of Contents

- [ChatGPT (Web)](#chatgpt-web-)
- [Claude.ai (Web/Desktop/Mobile)](#claude-ai-web-desktop-mobile-)
- [Claude Desktop—Local Config Method](#claude-desktop-local-config-method)
- [Claude Code (CLI)](#claude-code-cli-)
- [Anthropic API (Direct Integration)](#anthropic-api-direct-integration-)
- [Cursor IDE](#cursor-ide)
- [VS Code with GitHub Copilot](#vs-code-with-github-copilot)
- [GitHub Copilot CLI](#github-copilot-cli)
- [Other Available Registries](#other-available-registries)
- [Troubleshooting](#troubleshooting)

------------------------------------------------------------------------

## ChatGPT (Web)

Wolfram is available as an app in the <a href="https://chatgpt.com/apps" target="_blank">ChatGPT App Directory</a>.

### Steps Using Official App

1.  Open the <a href="https://chatgpt.com/apps/wolfram/asdk_app_69fe0bf66c8481919c513d799406436e" target="_blank">Wolfram app</a> page.
2.  If prompted, sign in to your ChatGPT account.
3.  Review the app information, capabilities and permissions.
4.  Click **Connect**.
5.  Once connected, the app should appear in your available apps list.

### Verify the Connection

1.  Open a new ChatGPT conversation.
2.  Click the **+** button (or use the Apps menu, depending on your interface).
3.  Locate and select **Wolfram** from your available apps.
4.  Alternatively, if your ChatGPT interface supports app mentions, invoke the app directly in a prompt.

#### Example Prompts

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/example-prompts-solve-and-graph-equation.txt">

``` text
Use Wolfram to solve and graph x^2 - 5x + 6 = 0.
```

</div>

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/example-prompts-satellite-orbital-period.txt">

``` text
Use Wolfram to calculate the orbital period of a satellite 400 km above Earth.
```

</div>

### Managing the Connection

1.  Open **Settings** in ChatGPT.
2.  Navigate to **Apps**.
3.  Locate **Wolfram** in your connected apps list.
4.  From there you can:
    - Review permissions
    - Reconnect the app
    - Disconnect the app

------------------------------------------------------------------------

## Claude.ai (Web/Desktop/Mobile)

Wolfram Cloud MCP is available as a <a href="https://claude.com/connectors/wolfram" target="_blank">connector</a>, or remote MCP servers can be configured as **custom connectors** brokered through your Anthropic account. The connection originates from Anthropic's cloud infrastructure, so the server must be publicly reachable.

### Steps Using Official Connector

1.  Visit the Wolfram official <a href="https://claude.com/connectors/wolfram" target="_blank">Claude connector</a> OR navigate to **<a href="https://claude.ai/customize/connectors" target="_blank">claude.ai/customize/connectors</a>** and search for **Wolfram** in the connector directory.
2.  Click the link under "Used in" to add to Claude.
3.  Click **Connect**.
4.  Once connected, the Wolfram connector will appear in your connector list.
5.  If you'd like to modify the tool's permissions, click the **+** button at the lower left of the chat interface, select **Connectors**, then **Manage connectors**. We recommend always allowing `WolframAlpha` and `WolframContext` tools, but setting `WolframLanguageEvaluator` as "Needs Approval." Without modifying permissions, you may need to approve requests more frequently.

#### Enabling the Connector in a Conversation

After connecting, enable Wolfram for a specific conversation:

1.  Click the **+** button at the lower left of the chat interface.
2.  Select **Connectors**.
3.  Toggle **Wolfram** on.

### Steps Using Custom Connector

1.  Open <a href="https://claude.ai" target="_blank">claude.ai</a> and click your account menu in the lower-left corner.
2.  Go to **Settings → Connectors**.
3.  Click **Add custom connector**.
4.  In the dialog, enter:
    - **Name:** `Wolfram`
    - **URL:** `https://agenttools.wolfram.com/mcp`
5.  Click **Add**.
6.  Once connected, the connector will appear in your Connectors list and be available in conversations.

**Note:** Remote connectors in Claude.ai are brokered through Anthropic's servers, not your local machine. Local MCP servers configured via `claude_desktop_config.json` are a separate mechanism. Learn more about Wolfram Local MCP [here](https://www.wolfram.com/artificial-intelligence/mcp/local/).

------------------------------------------------------------------------

## Claude Desktop—Local Config Method

For servers not yet in the Extensions directory, you can manually configure Claude Desktop via its JSON config file.

**Config file locations:**

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

### Option A—Direct URL (Streamable HTTP, Recommended)

Open **Settings → Developer → Edit Config** and add the following:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/option-a-direct-url-streamable-http-recommended.txt">

``` json
{
  "mcpServers": {
    "wolfram": {
      "url": "https://agenttools.wolfram.com/mcp"
    }
  }
}
```

</div>

### Option B—via `mcp-remote` Proxy (Older Claude Desktop Versions)

If your version of Claude Desktop doesn't support direct URL connections, use the `mcp-remote` npm package as a proxy. Requires Node.js.

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/option-b-via-mcp-remote-proxy-older-claude-desktop-versions.txt">

``` json
{
  "mcpServers": {
    "wolfram": {
      "command": "npx",
      "args": ["mcp-remote", "https://agenttools.wolfram.com/mcp"]
    }
  }
}
```

</div>

After editing the config, restart Claude Desktop. Wolfram tools will appear in your conversations.

### Organization-Level Tool Control (Team and Enterprise Only)

Owners can disable specific Wolfram tools across the organization:

1.  Navigate to **<a href="https://claude.ai/admin-settings/connectors" target="_blank">Organization settings &gt; Connectors</a>**.
2.  Locate the **Wolfram** connector.
3.  Click the connector to expand its settings.
4.  Disable any tool calls you do not want members to invoke—for example, tools that write data or take external actions.

**Note:** When using Claude's `Research` (Advanced Research) feature with Wolfram connected, Claude may invoke Wolfram tools automatically without per-call approval. Disable write-capable tools before using `Research` if you want to restrict this behavior.

------------------------------------------------------------------------

## Claude Code (CLI)

Claude Code supports remote MCP servers natively via its `claude mcp add` command. HTTP transport is the recommended option for remote servers.

### Add the Server (Streamable HTTP)

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/add-the-server-streamable-http.txt">

``` bash
claude mcp add --transport http wolfram https://agenttools.wolfram.com/mcp
```

</div>

### Verify the Connection

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/verify-the-connection-Claude-Code-CLI.txt">

``` bash
claude mcp list
# or inside a session:
/mcp
```

</div>

### Scoping Options

| Scope | Flag | Description |
|----|----|----|
| Local (default) | *(none)* | Available only in the current project |
| Global | `--scope global` | Available across all projects |
| Project (shared) | `--scope project` | Stored in `.mcp.json`, committable to version control |

### Manual `.mcp.json` Configuration *(Team Sharing)*

Create or edit `.mcp.json` in your project root:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/manual-mcp-json-configuration-team-sharing.txt">

``` json
{
  "mcpServers": {
    "wolfram": {
      "type": "streamable-http",
      "url": "https://agenttools.wolfram.com/mcp"
    }
  }
}
```

</div>

**Note:** `streamable-http` is accepted as an alias for `http` in JSON configs, for compatibility with server documentation that uses the MCP spec name.

If the server disconnects mid-session, Claude Code will automatically attempt to reconnect with exponential backoff (up to 5 attempts).

#### Allowlisting Specific Tools (HTTP Server)

In `.mcp.json` or `~/.claude.json`, use the `tool_configuration` field to restrict which tools are available:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/allowlisting-specific-tools-http-server.txt">

``` json
{
  "mcpServers": {
    "wolfram": {
      "type": "http",
      "url": "https://agenttools.wolfram.com/mcp",
      "tool_configuration": {
        "enabled": true,
        "allowed_tools": ["WolframAlpha", "WolframLanguageEvaluator", "WolframContext"]
      }
    }
  }
}
```

</div>

#### Denylisting Specific Tools

To allow all tools *except* specific ones, use `denied_tools`:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/denylisting-specific-tools.txt">

``` json
{
  "mcpServers": {
    "wolfram": {
      "type": "http",
      "url": "https://agenttools.wolfram.com/mcp",
        "tool_configuration": {
        "enabled": true,
        "denied_tools": ["WriteNotebook", "SubmitPaclet"]
      }
    }
  }
}
```

</div>

#### Global Permission Deny via Settings

To prevent Claude Code from ever calling a specific tool from any MCP server—including Wolfram—add it to the `deny` list in `.claude/settings.json` or `~/.claude/settings.json`:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/global-permission-deny-via-settings.txt">

``` json
{
  "permissions": {
    "deny": ["mcp__wolfram__WriteNotebook", "mcp__wolfram__SubmitPaclet"]
  }
}
```

</div>

#### Disabling Tool Search for Wolfram (Always-Load Mode)

By default, Claude Code defers loading MCP tool schemas until needed. To force Wolfram tools to always be available at session start:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/disabling-tool-search-for-wolfram-always-load-mode.txt">

``` json
{
  "mcpServers": {
    "wolfram": {
      "type": "http",
      "url": "https://agenttools.wolfram.com/mcp",
      "alwaysLoad": true
    }
  }
}
```

</div>

------------------------------------------------------------------------

## Anthropic API (Direct Integration)

You can connect to the Wolfram MCP server directly from the Anthropic Messages API using the `mcp_servers` parameter. This requires the beta header `mcp-client-2025-11-20`.

**Note:** Only MCP tool calls are supported via this method. MCP prompts and resources require a client-side SDK connection.

**Python Example**

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/python-example.txt">

``` python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "What is the integral of x^2 from 0 to 5?"}
    ],
    mcp_servers=[
        {
            "type": "url",
            "url": "https://agenttools.wolfram.com/mcp",
            "name": "wolfram",
        }
    ],
    tools=[
        {
            "type": "mcp_toolset",
            "mcp_server_name": "wolfram"
        }
    ],
    betas=["mcp-client-2025-11-20"],
)

print(response)
```

</div>

**JavaScript/TypeScript Example**

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/javascript-typescript-example.txt">

``` javascript
const Anthropic = require("@anthropic-ai/sdk");

const client = new Anthropic.Anthropic();

const response = await client.beta.messages.create({
  model: "claude-sonnet-4-6",
  max_tokens: 1000,
  messages: [
    { role: "user", content: "What is the integral of x^2 from 0 to 5?" }
  ],
  mcp_servers: [
    {
      type: "url",
      url: "https://agenttools.wolfram.com/mcp",
      name: "wolfram",
    }
  ],
  tools: [
    {
      type: "mcp_toolset",
      mcp_server_name: "wolfram"
    }
  ],
  betas: ["mcp-client-2025-11-20"],
});

console.log(response);
```

</div>

**Restricting Available Tools**

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/restricting-available-tools.txt">

``` json
{
  "tools": [
    {
      "type": "mcp_toolset",
      "mcp_server_name": "wolfram",
      "default_config": { "enabled": false },
      "configs": {
        "WolframAlpha": { "enabled": true },
        "WolframLanguageEvaluator": { "enabled": true }
      }
    }
  ]
}
```

</div>

------------------------------------------------------------------------

## Cursor IDE

Cursor supports remote MCP servers via Streamable HTTP. Configuration can be global or project level.

### Option A—Settings UI (Recommended)

1.  In the side panel, click **Customize** → **MCPs**.
2.  Choose **+New**.
3.  Add this to the list of MCP servers:
    - **Name:** `wolfram`
    - **URL:** `https://agenttools.wolfram.com/mcp`

### Option B—Manual JSON Config

- **Global:** `~/.cursor/mcp.json`
- **Project-level:** `.cursor/mcp.json` in your project root (commit to share with team)

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/option-b-manual-json-config.txt">

``` json
{
  "mcpServers": {
    "wolfram": {
      "url": "https://agenttools.wolfram.com/mcp"
    }
  }
}
```

</div>

### Option C—via `mcp-remote` Proxy (Older Cursor Versions)

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/option-c-via-mcp-remote-proxy-older-cursor-versions.txt">

``` json
{
  "mcpServers": {
    "wolfram": {
      "command": "npx",
      "args": ["mcp-remote", "https://agenttools.wolfram.com/mcp"]
    }
  }
}
```

</div>

After saving, reload the Cursor window or restart the IDE. Wolfram tools will appear in the agent's tool list.

**Tip:** Cursor reads the root key as `"mcpServers"`. Do not use `"servers"`—that is VS Code's key.

------------------------------------------------------------------------

## VS Code with GitHub Copilot

VS Code uses a different config key from Cursor (`"servers"` instead of `"mcpServers"`). MCP tools only work in **Agent mode** in Copilot Chat.

### Prerequisites

- VS Code 1.99 or later
- GitHub Copilot extension installed
- Copilot Chat open in **Agent mode** (select "Agent" from the mode drop-down)

### Option A—Command Palette (Recommended)

1.  Open the Command Palette (`Cmd/Ctrl+Shift+P`).
2.  Run **MCP: Add Server…**.
3.  Select **HTTP** as the server type.
4.  Paste `https://agenttools.wolfram.com/mcp` and press Enter.
5.  Give it the name `wolfram` and choose **Global** (all workspaces) or **Workspace** (current project only).

### Option B—Manual `mcp.json` Config

- **Global:** Run `MCP: Open User Configuration` from the Command Palette.
- **Workspace:** Create `.vscode/mcp.json` in your project root.

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/option-b-manual-mcp-json-config.txt">

``` json
{
  "servers": {
    "wolfram": {
      "type": "http",
      "url": "https://agenttools.wolfram.com/mcp"
    }
  }
}
```

</div>

A **Start** button will appear in the `mcp.json` file. Click it to activate the server and discover its tools.

- **Important:** VS Code uses `"servers"` as the root key, not `"mcpServers"`. Copying a Cursor or Claude Desktop config without changing this key is the most common setup mistake.

------------------------------------------------------------------------

## GitHub Copilot CLI

### Option A—Interactive `/mcp add`

In a Copilot CLI session, run:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/option-a-interactive-mcp-add.txt">

    /mcp add

</div>

When prompted:

- Choose **HTTP** as the server type.
- Enter the URL: `https://agenttools.wolfram.com/mcp`
- Enter the name: `wolfram`

### Option B—Edit Config File Directly

- **Global:** `~/.copilot/mcp-config.json`
- **Project:** `.mcp/copilot/mcp.json`

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/option-b-edit-config-file-directly.txt">

``` json
{
  "mcpServers": {
    "wolfram": {
      "type": "http",
      "url": "https://agenttools.wolfram.com/mcp"
    }
  }
}
```

</div>

Save the file and restart Copilot CLI for changes to take effect.

#### Managing Servers

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/cloud/c2c/managing-servers.txt">

    /mcp show              # list all configured servers
    /mcp show wolfram      # details + available tools
    /mcp disable wolfram   # disable without removing
    /mcp enable wolfram    # re-enable
    /mcp delete wolfram    # remove

</div>

------------------------------------------------------------------------

## Other Available Registries

Wolfram Cloud MCP is available through many other registries including:

- <a href="https://smithery.ai/servers/wolframmcp/Wolfram" target="_blank">Smithery.ai</a>
- <a href="https://www.mcpinstall.com/mcp-server/10040-mcpserver" target="_blank">MCP Install</a>
- <a href="https://mcprepository.com/wolframresearch/agenttools" target="_blank">MCP Repository</a>

------------------------------------------------------------------------

## Troubleshooting

### Server Not Connecting

- Confirm the URL is reachable: `curl https://agenttools.wolfram.com/mcp`
- Ensure your network allows outbound HTTPS on port 443.

### Tools Not Appearing

- Make sure you're using **Agent mode** in VS Code Copilot Chat (tools are invisible in Ask or Edit modes).
- In Claude Code, run `/mcp` inside a session to see server status.
- Validate your JSON config with a linter—a single misplaced comma will silently break the file.

### Wrong Config Key

- Claude Desktop and Cursor use `"mcpServers"` as the root key.
- VS Code uses `"servers"` as the root key.
- Mixing these up is the most common cross-client copy-paste mistake.

### SSE vs. HTTP Transport

- SSE (server-sent events) transport is deprecated in the MCP specification. Prefer `http`/`streamable-http` for all new configurations.
- If a client requires SSE, use the URL as is; many servers accept both transports at the same endpoint.

### Connecting to Local Wolfram Desktop

- For users wanting to connect to their **local** Wolfram Desktop, Mathematica or Wolfram Engine application, learn more about Wolfram Local MCP [here](https://www.wolfram.com/artificial-intelligence/mcp/local/).

------------------------------------------------------------------------

*Source: [Wolfram Cloud MCP](https://www.wolfram.com/artificial-intelligence/mcp/cloud/) — © 2026 Wolfram Research*

</div>

</div>

</div>

</div>
