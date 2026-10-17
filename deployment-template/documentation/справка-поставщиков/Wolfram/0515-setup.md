> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Wolfram: setup

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


<div id="sub" class="header">

<div id="sub-content">

<div class="backlink">

<a href="https://support.wolfram.com/" class="dark-gray red-hover arrow-l-before">Back to Support</a>

</div>

# How can I connect Wolfram Cloud MCP to my AI application?

</div>

</div>

<div id="post" class="section">

<div id="post-content" class="post-75237 post type-post status-publish format-standard hentry category-uncategorized">

<div id="entry">

**[Wolfram Cloud MCP](https://www.wolfram.com/artificial-intelligence/mcp-service/)** enables MCP-compatible AI applications to access Wolfram\|Alpha, Wolfram Language and the Wolfram Knowledgebase using the Model Context Protocol (MCP).

Its server URL is:

    https://agenttools.wolfram.com/mcp

Wolfram Cloud MCP is free to use and does not require any authentication.

Most AI clients can connect to Wolfram Cloud MCP. Specific setup instructions for a variety of them are provided below.

## Selection of Supported Clients

This article provides setup steps for:

- [Antigravity](#antigravity)
- [ChatGPT on desktop](#chatgpt)
- [ChatGPT on web](#webchatgpt)
- [Claude on desktop](#claude-desktop)
- [Claude on web](#claude-web)
- [Cline](#cline)
- [Codex](#Codex)
- [Continue](#continue)
- [Cursor](#cursor)
- [LibreChat](#libre-chat)
- [OpenCode](#open-code)
- [Windsurf](#windsurf)
- [Zed](#zed)

If you do not see your client here, check your client’s documentation for directions on connecting to a remote MCP service.

## Antigravity

1.  Open **Antigravity**.
2.  Open the MCP store via the **“…”** drop-down at the top of the editor’s agent panel.
3.  Click **Manage MCP Servers**.
4.  Click **View raw config**.
5.  Modify the `mcp_config.json` with your custom MCP server configuration.

<!-- -->

    {
      "mcpServers": {
        "wolfram": {
          "serverUrl": "https://agenttools.wolfram.com/mcp",
          "headers": {
            "Content-Type": "application/json"
          },
          "disabled": false
        }
      }
    }

## ChatGPT on Desktop

1.  Open your **ChatGPT** app.
2.  Open **Apps**.
3.  Search for **Wolfram**.
4.  Click **Wolfram**.
5.  Click **Connect**.
6.  When prompted to add **Wolfram** to ChatGPT, click **Connect**.
7.  Verify that the Wolfram app is installed.\
    <img src="https://content.wolfram.com/sites/20/2026/06/ChatGPT_3nATsILpcq.png" class="alignnone size-full wp-image-74828" fetchpriority="high" decoding="async" srcset="https://content.wolfram.com/sites/20/2026/06/ChatGPT_3nATsILpcq.png 978w, https://content.wolfram.com/sites/20/2026/06/ChatGPT_3nATsILpcq-300x231.png 300w, https://content.wolfram.com/sites/20/2026/06/ChatGPT_3nATsILpcq-768x591.png 768w" sizes="(max-width: 978px) 100vw, 978px" width="978" height="752" />

## ChatGPT on Web

1.  In your browser, go to <a href="https://chatgpt.com/" target="_blank">ChatGPT</a>.
2.  Click <a href="https://chatgpt.com/apps/wolfram/asdk_app_69fe0bf66c8481919c513d799406436e" target="_blank">here</a> to open the **Wolfram** app page.
3.  Click **Connect**.
4.  When prompted to add **Wolfram** to ChatGPT, click **Connect**.
5.  Verify e.g. in **…** \> **Manage** that the Wolfram plugin app is installed.\
    <img src="https://content.wolfram.com/sites/20/2026/07/0OBjSTMZ9I.png" class="alignnone size-full wp-image-75147" decoding="async" srcset="https://content.wolfram.com/sites/20/2026/07/0OBjSTMZ9I.png 827w, https://content.wolfram.com/sites/20/2026/07/0OBjSTMZ9I-300x260.png 300w, https://content.wolfram.com/sites/20/2026/07/0OBjSTMZ9I-768x666.png 768w" sizes="(max-width: 827px) 100vw, 827px" width="827" height="717" />

## Claude on Desktop

1.  Open your **Claude** app.
2.  Click **Customize**.
3.  Click **Connectors**.
4.  Search for **Wolfram**.
5.  Click the **+** icon to add **Wolfram**.
6.  Verify that the Wolfram connector is installed and that all Wolfram tools are enabled.\
    <img src="https://content.wolfram.com/sites/20/2026/06/claude_i3EZbxzmJS.png" class="alignnone size-full wp-image-74824" decoding="async" srcset="https://content.wolfram.com/sites/20/2026/06/claude_i3EZbxzmJS.png 919w, https://content.wolfram.com/sites/20/2026/06/claude_i3EZbxzmJS-300x161.png 300w, https://content.wolfram.com/sites/20/2026/06/claude_i3EZbxzmJS-768x412.png 768w" sizes="(max-width: 919px) 100vw, 919px" width="919" height="493" />

## Claude on Web

1.  In your browser, go to <a href="https://claude.ai/" target="_blank">Claude</a>.
2.  Click <a href="https://claude.ai/directory/connectors/wolfram" target="_blank">here</a> to open the **Wolfram** connector page.
3.  Click **Connect** to add **Wolfram**.
4.  Verify that the Wolfram connector is installed.\
    <img src="https://content.wolfram.com/sites/20/2026/07/Claude-WEB.png" class="alignnone size-full wp-image-75148" loading="lazy" decoding="async" srcset="https://content.wolfram.com/sites/20/2026/07/Claude-WEB.png 953w, https://content.wolfram.com/sites/20/2026/07/Claude-WEB-300x212.png 300w, https://content.wolfram.com/sites/20/2026/07/Claude-WEB-768x542.png 768w" sizes="(max-width: 953px) 100vw, 953px" width="953" height="672" />

## Cline

1.  Open **Cline** in **VS Code**.
2.  Click **MCP Servers**.
3.  Select the **Remote Servers** tab.
4.  Click the **Edit Configuration** button.\
    <img src="https://content.wolfram.com/sites/20/2026/04/cline2026-04-30-220818.png" class="alignnone size-full wp-image-74465" loading="lazy" decoding="async" srcset="https://content.wolfram.com/sites/20/2026/04/cline2026-04-30-220818.png 376w, https://content.wolfram.com/sites/20/2026/04/cline2026-04-30-220818-187x300.png 187w" sizes="(max-width: 376px) 100vw, 376px" width="376" height="603" />
5.  Add the following configuration and save the file.

<!-- -->

    {
      "mcpServers": {
        "Wolfram": {
          "url": "https://agenttools.wolfram.com/mcp",
          "type": "streamableHttp",
          "disabled": false,
          "autoApprove": []
        }
      }
    }

## Codex

1.  Open **Codex** in **VS Code**.
2.  Go to **Settings**, then open the **MCP Settings** section.
3.  Add the following configuration and save the changes.

<img src="https://content.wolfram.com/sites/20/2026/02/codex.png" class="alignnone size-full wp-image-74190" loading="lazy" decoding="async" srcset="https://content.wolfram.com/sites/20/2026/02/codex.png 1245w, https://content.wolfram.com/sites/20/2026/02/codex-300x181.png 300w, https://content.wolfram.com/sites/20/2026/02/codex-768x463.png 768w, https://content.wolfram.com/sites/20/2026/02/codex-1024x617.png 1024w" sizes="(max-width: 1245px) 100vw, 1245px" width="1245" height="750" alt="Codex MCP configuration in VS Code" />

## Continue

1.  Open **Continue** in **VS Code**.
2.  Navigate to the `.continue/mcpServers` directory in your user home folder.
3.  Add the following configuration and save the YAML file.

<!-- -->

    name: Wolfram MCP
    version: 0.0.1
    schema: v1
    mcpServers:
      - name: Wolfram
        command: npx
        args:
          - "-y"
          - "mcp-remote@latest"
          - "https://agenttools.wolfram.com/mcp"

## Cursor

1.  Open **Cursor**.
2.  Click **Tools & MCP**.
3.  Click **New MCP Server**.
4.  Add the following configuration and save.

<!-- -->

    {
      "mcpServers": {
        "Wolfram": {
          "url": "https://agenttools.wolfram.com/mcp"
        }
      }
    }

## LibreChat

1.  Open **LibreChat**.

2.  Open **MCP Settings**.

3.  Click the **+** icon to add a new MCP server.

4.  Enter the following configuration details as shown.

        Name: Wolfram
        MCP Server URL: https://services.wolfram.com/api/mcp
        Transport: Streamable HTTPS
        Authentication: API Key
        API Key: <YOUR_WOLFRAM_MCP_SERVICE_API_KEY>
        Header Format: Bearer

    <img src="https://content.wolfram.com/sites/20/2026/02/newww.png" class="alignnone size-full wp-image-73688" loading="lazy" decoding="async" srcset="https://content.wolfram.com/sites/20/2026/02/newww.png 636w, https://content.wolfram.com/sites/20/2026/02/newww-266x300.png 266w" sizes="(max-width: 636px) 100vw, 636px" width="636" height="716" />

5.  Enable **I trust this application**.

6.  Click **Create** to save the configuration.

## OpenCode

1.  Navigate to `%USERPROFILE%\.config\opencode\opencode.jsonc`.

2.  Edit the configuration file.

3.  Add the following Wolfram MCP configuration.

        {
          "$schema": "https://opencode.ai/config.json",
          "mcp": {
            "wolfram": {
              "type": "remote",
              "url": "https://agenttools.wolfram.com/mcp",
              "enabled": true,
              "oauth": false
            }
          }
        }

4.  Save the file.

5.  Restart **OpenCode**.

6.  Verify that the server appears in the **MCP** tab under **Status**.

## Windsurf

1.  Open **Windsurf**.
2.  Navigate to `%USERPROFILE%\.codeium\windsurf\mcp_config.json`.
3.  Add the following configuration and save the file.

<!-- -->

    {
      "mcpServers": {
        "wolfram": {
          "command": "npx",
          "args": [
            "mcp-remote",
            "https://agenttools.wolfram.com/mcp"
          ]
        }
      }
    }

## Zed

1.  Open **Zed**.
2.  Open the **Agent Panel**.
3.  Click **MCP Servers**.
4.  Select **Add Custom Server…**.
5.  Add the following configuration and save the changes.

<!-- -->

    {
        "wolfram": {
          "enabled": true,
          "remote": false,
          "command": "C:\\Progra~1\\nodejs\\npx.cmd",
          "args": ["-y", "mcp-remote@latest", "https://agenttools.wolfram.com/mcp"],
        },
      }

</div>

</div>

</div>

<div id="helpful" class="section">

<div id="helpful-content">

<div class="isHelpfulTitle">

Is this article helpful?

</div>

<div id="yesButton" class="button">

Yes

</div>

<div id="noButton" class="button">

No

</div>

</div>

</div>

<div id="helpful-form" class="section">

<div id="helpful-form-content">

Any comments?

Thank you for your feedback.

<div id="submitComments" class="button">

Submit

</div>

</div>

</div>

<div id="backlink" class="section">

<div id="backlink-content">

<div class="backlink">

<a href="https://support.wolfram.com/" class="dark-gray red-hover arrow-l-before">Back to Support</a>

</div>

</div>

</div>

<div id="rec-related" class="section">

<div id="rec-related-content">

------------------------------------------------------------------------

## Related Articles

<div class="grid cols-1 width-full">

<div class="width-full">

<a href="https://support.wolfram.com/74994" class="dark-gray red-hover chevron-after">What are the Wolfram|Alpha Notebook Edition 14.3 system requirements?</a>

</div>

<div class="width-full">

<a href="https://support.wolfram.com/74996" class="dark-gray red-hover chevron-after">What are Finance Platform 14.3 system requirements?</a>

</div>

<div class="width-full">

<a href="https://support.wolfram.com/75023" class="dark-gray red-hover chevron-after">Why do I see a “Support Ending for Intel-based Apps” message when installing the Wolfram app on Apple silicon?</a>

</div>

</div>

</div>

</div>

<a href="#top" class="toplink" title="Top"></a>

<div id="language-picker" class="section">

<div id="language-picker-content">

Deutsch English Español Français 日本語 한국어 Português Русский 中文

</div>

</div>

<div id="contact-support" class="section">

<div id="contact-support-content">

<div id="contact-pad">

## Contact Support

Whether you have a question about billing, activation or something more technical, we are ready to help you.

<div class="grid cols-3 cols-1__600 width-full">

<div class="width-1-3 width-full__600">

<a href="//www.wolfram.com/support/contact/" class="cta-link mini-m contact-message red orange-hover"><span><img src="https://support.wolfram.com/wp-content/themes/support/img/contact-send-message.svg" width="20" height="20" /></span> <span class="chevron-after">Send us a message</span></a>

</div>

<div class="width-1-3 width-full__600">

<a href="//www.wolfram.com/support/contact/?topic=feedback" class="cta-link mini-m contact-feedback red orange-hover"><span><img src="https://support.wolfram.com/wp-content/themes/support/img/contact-feedback.svg" width="20" height="20" /></span> <span class="chevron-after">Product feedback</span></a>

</div>

<div id="call-us-head" class="width-1-3 width-full__600">

<span class="cta-link mini-m red orange-hover"> <img src="https://support.wolfram.com/wp-content/themes/support/img/contact-call-us.svg" width="20" height="20" /> <span class="chevron-after">Call us</span> </span>

</div>

</div>

</div>

<div id="call-us-content">

<div id="call-us-inner">

## 1-800-WOLFRAM <span class="small">(+1-217-398-0700 for international callers)</span>

<div class="grid cols-2 cols-1__600 width-full">

<div class="width-1-3 width-2-5__900 width-full__600">

## Customer Support

**Monday–Friday**\
8am–5pm US Central Time

- Product registration or activation
- Pre-sales information and ordering
- Help with installation and first launch

</div>

<div class="width-2-3 width-3-5__900 width-full__600">

## Advanced Technical Support <span class="small">*(for eligible customers)*</span>

**Monday–Thursday**\
8am–5pm US Central Time

**Friday**\
8:30–10am & 11am–5pm US Central Time

- Priority technical support
- Product assistance from Wolfram experts
- Help with Wolfram Language programming
- Advanced installation support

</div>

</div>

</div>

</div>

</div>

</div>
