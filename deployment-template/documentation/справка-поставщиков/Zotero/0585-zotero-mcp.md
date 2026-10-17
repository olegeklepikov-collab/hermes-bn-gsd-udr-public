> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Zotero: zotero-mcp

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Zotero MCP: Chat with your Research Library—Local or Web—in Claude, ChatGPT, and more.
**Zotero MCP** connects your [Zotero](https://www.zotero.org/) research library with [ChatGPT](https://openai.com), [Claude](https://www.anthropic.com/claude), and other AI assistants (e.g., [Cherry Studio](https://cherry-ai.com/), [Chorus](https://chorus.sh), [Cursor](https://www.cursor.com/)) via the [Model Context Protocol](https://modelcontextprotocol.io/introduction). Search your library, read and annotate papers, add and organize items, and find research by meaning.
> **AI agents:** read [docs/for-agents.md](https://github.com/54yyyu/zotero-mcp/blob/main/docs/for-agents.md) first. It covers which route to use, setup, and the commands in one place.
## ✨ What it does
- 🔍 **Search** by title, author, tag, collection, full text, or meaning ([semantic search](https://github.com/54yyyu/zotero-mcp/blob/main/docs/semantic-search.md) with local, OpenAI, Gemini, or Ollama embeddings)
- 📚 **Read** metadata, BibTeX, full text, and page ranges of PDFs, with page images where text extraction garbles math, figures, and tables
- 📝 **Annotate**: highlights and area boxes placed on the exact words, figure, table, or equation; notes; PDF annotation extraction
- ✏️ **Write**: add papers by DOI, URL, ISBN, BibTeX, or file (with open-access PDFs), manage collections and tags, merge duplicates
- 💻 **Local or web**: in local mode reads come straight from `zotero.sqlite`; writes go to the running Zotero 10+ or through the web API
- 🪶 **Two ways in**: an MCP server for chat apps, or `zotero-cli` plus an agent skill for coding agents
- 📊 **Scite** citation tallies and retraction alerts (optional)
## 🚀 Quick start
**1. Install** (Python 3.10+):
```bash
uv tool install zotero-mcp-server     # or: pip install zotero-mcp-server
```
> **New to the command line?** Try the community-built [Zotero MCP Setup](https://github.com/ehawkin/zotero-mcp-setup): a macOS GUI installer, one-click scripts for Mac and Windows, and a step-by-step guide.
**2. Enable Zotero's local API**: in Zotero 7+, open **Settings → Advanced** and tick *Allow other applications on this computer to communicate with Zotero*.
**3. Connect your assistant**:
```bash
zotero-mcp setup      # auto-configures Claude Desktop
```
or add the server by hand (Claude Desktop: `claude_desktop_config.json`; Claude Code: `~/.claude.json`):
```json
{
"mcpServers": {
"zotero": {
"command": "zotero-mcp",
"env": { "ZOTERO_LOCAL": "true" }
}
}
}
```
**4. Writes (optional)**: on Zotero 10+, run `zotero-mcp authorize-local` once and choose **Always Allow**. On older Zotero, add `ZOTERO_API_KEY` and `ZOTERO_LIBRARY_ID` to write through the web API.
Then ask things like *"Find papers in my library on attention mechanisms"*, *"Summarize the key findings of this paper"*, or *"Highlight the main claims of this PDF"*.
ChatGPT, Cherry Studio, Chorus, Autohand, and other clients: see [Getting started](https://github.com/54yyyu/zotero-mcp/blob/main/docs/getting-started.md).
### Optional extras
The base install covers search, reading, annotations, and writes. Heavier features are extras:
| Extra | What it adds | Install command |
|-------|-------------|-----------------|
| `semantic` | Semantic search via ChromaDB, sentence-transformers, OpenAI/Gemini embeddings | `pip install "zotero-mcp-server[semantic]"` |
| `pdf` | PDF outlines, page layout and page images (PyMuPDF), EPUB annotations | `pip install "zotero-mcp-server[pdf]"` |
| `scite` | [Scite](https://scite.ai) citation tallies and retraction alerts (no account needed) | `pip install "zotero-mcp-server[scite]"` |
| `all` | Everything above | `pip install "zotero-mcp-server[all]"` |
Update any time with `zotero-mcp update`.
## 🪶 MCP server or agent skill?
If your agent has a shell (Claude Code, Cursor, Codex, Windsurf, Gemini CLI, Amp, OpenCode …), one command teaches it to drive `zotero-cli`:
```bash
zotero-mcp install-skill
```
An MCP server sends every tool's schema on every request, before you type anything. The skill costs 98 tokens until the agent decides it is relevant:
| Route | In context | Paid |
|---|---:|---|
| MCP server, default profile (38 tools) | **13,448** | every request |
| Agent skill, frontmatter only | **98** | always |
| Agent skill, body loaded | 1,368 | when it fires |
Use the MCP server when your client speaks MCP but has no shell (Claude Desktop, ChatGPT); use the skill when it has a shell. Both share one config. Details: [CLI and agent skill](https://github.com/54yyyu/zotero-mcp/blob/main/docs/cli.md).
## 📖 Documentation
| Guide | What's in it |
|---|---|
| [Getting started](https://github.com/54yyyu/zotero-mcp/blob/main/docs/getting-started.md) | Connecting Claude Desktop and Claude Code, ChatGPT, Cherry Studio, Chorus, Autohand, and other MCP clients |
| [Configuration](https://github.com/54yyyu/zotero-mcp/blob/main/docs/configuration.md) | Environment variables, local writes, web and hybrid modes, the SQLite read backend, global search, text extraction, command-line options |
| [Semantic search](https://github.com/54yyyu/zotero-mcp/blob/main/docs/semantic-search.md) | Embedding models, building and updating the index |
| [Tools](https://github.com/54yyyu/zotero-mcp/blob/main/docs/tools.md) | Every MCP tool, tool groups (`ZOTERO_MCP_TOOLSETS`), related items, PDF annotation extraction |
| [CLI and agent skill](https://github.com/54yyyu/zotero-mcp/blob/main/docs/cli.md) | `zotero-cli` command reference, `--json` output, `install-skill` |
| [Docker](https://github.com/54yyyu/zotero-mcp/blob/main/docs/docker-images.md) | Container images and runtime modes |
| [Troubleshooting](https://github.com/54yyyu/zotero-mcp/blob/main/docs/troubleshooting.md) | Common problems and fixes |
| [For AI agents](https://github.com/54yyyu/zotero-mcp/blob/main/docs/for-agents.md) | One guide for an agent setting up or using Zotero MCP |
Website: [stevenyuyy.com/zotero-mcp](https://stevenyuyy.com/zotero-mcp/) · [Changelog](https://github.com/54yyyu/zotero-mcp/blob/main/CHANGELOG.md)
## 🤝 Contributing
Issues and pull requests are welcome. Run the tests with `uv run pytest tests/`. A live integration test plan, meant to be run by Claude against a real library, is in [docs/integration-test-plan.md](https://github.com/54yyyu/zotero-mcp/blob/main/docs/integration-test-plan.md).
## ☕ Support
Zotero MCP is free and MIT-licensed.
If it saves you or your lab time, sponsoring helps cover the unglamorous parts: Windows and WSL2 edge
cases, Zotero schema changes, group-library support, and the embedding/search infrastructure.
**Labs and institutions:** the $50 and $200 tiers are meant to be expensable, and include priority
triage on the issues affecting your workflow.
## Contributors
Thanks to everyone who has contributed code, fixes, and ideas to Zotero MCP.
## 📄 License
## MIT
