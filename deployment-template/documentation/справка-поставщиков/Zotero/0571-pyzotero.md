> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Zotero: pyzotero

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


<div class="document" role="main" itemscope="itemscope" itemtype="http://schema.org/Article">

<div itemprop="articleBody">

Pyzotero is a Python wrapper for the <a href="https://www.zotero.org/support/dev/web_api/v3/start" class="reference external">Zotero API (v3)</a>.

<div id="getting-started-short-version" class="section">

<span id="module-zotero"></span>

# Getting started (short version)<a href="#getting-started-short-version" class="headerlink" title="Link to this heading"></a>

1.  <span class="pre">`uv`</span>` `<span class="pre">`add`</span>` `<span class="pre">`pyzotero`</span> or <span class="pre">`pip`</span>` `<span class="pre">`install`</span>` `<span class="pre">`pyzotero`</span> or <span class="pre">`conda`</span>` `<span class="pre">`install`</span>` `<span class="pre">`conda-forge::pyzotero`</span>

2.  You’ll need the ID of the personal or group library you want to access:

> <div>
>
> - Your **personal library ID** is available <a href="https://www.zotero.org/settings/keys" class="reference external">here</a>, in the section <span class="pre">`Your`</span>` `<span class="pre">`userID`</span>` `<span class="pre">`for`</span>` `<span class="pre">`use`</span>` `<span class="pre">`in`</span>` `<span class="pre">`API`</span>` `<span class="pre">`calls`</span>
>
> - For **group libraries**, the ID can be found by opening the group’s page: <span class="pre">`https://www.zotero.org/groups/groupname`</span>, and hovering over the <span class="pre">`group`</span>` `<span class="pre">`settings`</span> link. The ID is the integer after <span class="pre">`/groups/`</span>
>
> </div>

3.  You’ll also need [^1] to get an **API key** from the Zotero <a href="https://www.zotero.org/settings/keys/new" class="reference external">site</a>

4.  Are you accessing your own Zotero library? Set\`\`library_type\`\` to <span class="pre">`'user'`</span>

5.  Are you accessing a shared group library? Set\`\`library_type\`\` to <span class="pre">`'group'`</span>

6.  Access to your local Zotero library is available: set <span class="pre">`local=True`</span>. Reads need no authentication; writes require a local API key and a recent Zotero version — see <a href="#localapi" class="reference internal"><span class="std std-ref">The Local Zotero API</span></a>

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>         from pyzotero import Zotero
>         zot = Zotero(library_id, library_type, api_key)
>         items = zot.top(limit=5)
>         # we've retrieved the latest five top-level items in our library
>         # we can print each item's item type and ID
>         for item in items:
>         print(f"Item: {item['data']['itemType']} | Key: {item['data']['key']}")
>
> </div>
>
> </div>
>
> </div>

Refer to the <a href="#read" class="reference internal"><span class="std std-ref">Errors</span></a> and <a href="#write" class="reference internal"><span class="std std-ref">Write API Methods</span></a>.

</div>

<div id="installation-testing-usage-longer-version" class="section">

# Installation, testing, usage (longer version)<a href="#installation-testing-usage-longer-version" class="headerlink" title="Link to this heading"></a>

<div id="installation" class="section">

<span id="id2"></span>

## Installation<a href="#installation" class="headerlink" title="Link to this heading"></a>

Using <a href="https://docs.astral.sh/uv/concepts/projects/dependencies/#adding-dependencies" class="reference external">uv</a>: <span class="pre">`uv`</span>` `<span class="pre">`add`</span>` `<span class="pre">`pyzotero`</span>

Using <a href="http://www.pip-installer.org/en/latest/index.html" class="reference external">pip</a>: <span class="pre">`pip`</span>` `<span class="pre">`install`</span>` `<span class="pre">`pyzotero`</span>

Using <a href="https://www.anaconda.com/distribution/" class="reference external">Anaconda</a>: <span class="pre">`conda`</span>` `<span class="pre">`install`</span>` `<span class="pre">`conda-forge::pyzotero`</span>

<div id="optional-command-line-interface" class="section">

### Optional: Command-Line Interface<a href="#optional-command-line-interface" class="headerlink" title="Link to this heading"></a>

Pyzotero includes an optional command-line interface for searching and querying your local Zotero library, and for managing its collections.

To install Pyzotero with the CLI:

- Using <a href="https://docs.astral.sh/uv/" class="reference external">uv</a>: <span class="pre">`uv`</span>` `<span class="pre">`add`</span>` `<span class="pre">`"pyzotero[cli]"`</span>

- Using <a href="http://www.pip-installer.org/en/latest/index.html" class="reference external">pip</a>: <span class="pre">`pip`</span>` `<span class="pre">`install`</span>` `<span class="pre">`"pyzotero[cli]"`</span>

If you just want to use the CLI without permanently installing Pyzotero:

- Using <a href="https://docs.astral.sh/uv/" class="reference external">uvx</a>: <span class="pre">`uvx`</span>` `<span class="pre">`--from`</span>` `<span class="pre">`"pyzotero[cli]"`</span>` `<span class="pre">`pyzotero`</span>` `<span class="pre">`search`</span>` `<span class="pre">`-q`</span>` `<span class="pre">`"your`</span>` `<span class="pre">`query"`</span>

- Using <a href="https://pipx.pypa.io/" class="reference external">pipx</a>: <span class="pre">`pipx`</span>` `<span class="pre">`run`</span>` `<span class="pre">`--spec`</span>` `<span class="pre">`"pyzotero[cli]"`</span>` `<span class="pre">`pyzotero`</span>` `<span class="pre">`search`</span>` `<span class="pre">`-q`</span>` `<span class="pre">`"your`</span>` `<span class="pre">`query"`</span>

See <a href="#cli-usage" class="reference internal"><span class="std std-ref">Command-Line Interface Usage</span></a> for usage details.

</div>

<div id="optional-mcp-server" class="section">

### Optional: MCP Server<a href="#optional-mcp-server" class="headerlink" title="Link to this heading"></a>

Pyzotero includes an optional <a href="https://modelcontextprotocol.io" class="reference external">MCP</a> server that exposes your local Zotero library and the Semantic Scholar integration.

To install Pyzotero with the MCP server:

- Using <a href="https://docs.astral.sh/uv/" class="reference external">uv</a>: <span class="pre">`uv`</span>` `<span class="pre">`add`</span>` `<span class="pre">`"pyzotero[mcp]"`</span>

- Using <a href="http://www.pip-installer.org/en/latest/index.html" class="reference external">pip</a>: <span class="pre">`pip`</span>` `<span class="pre">`install`</span>` `<span class="pre">`"pyzotero[mcp]"`</span>

- As a standalone tool: <span class="pre">`uv`</span>` `<span class="pre">`tool`</span>` `<span class="pre">`install`</span>` `<span class="pre">`"pyzotero[mcp]"`</span>

- CLI and MCP server together: <span class="pre">`uv`</span>` `<span class="pre">`tool`</span>` `<span class="pre">`install`</span>` `<span class="pre">`"pyzotero[cli,mcp]"`</span>

See <a href="#mcp-server" class="reference internal"><span class="std std-ref">MCP Server</span></a> for configuration and the list of tools.

From a local clone, if you wish to install Pyzotero from a specific branch:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     git clone git://github.com/urschrei/pyzotero.git
>     cd pyzotero
>     git checkout main
>     uv sync
>
> </div>
>
> </div>
>
> </div>

The Pyzotero source tarball is also available from <a href="http://pypi.python.org/pypi/Pyzotero" class="reference external">PyPI</a>

</div>

</div>

<div id="installing-development-versions" class="section">

## Installing development versions<a href="#installing-development-versions" class="headerlink" title="Link to this heading"></a>

Pyzotero remains in development as of 2025. Unstable development versions can be found on the <a href="https://github.com/urschrei/pyzotero/tree/main" class="reference external">Github main branch</a>, and installed directly from a checked-out <span class="pre">`main`</span> branch on a local clone, as in the example above: specify <span class="pre">`--dev`</span> (uv) / <span class="pre">`--group`</span>` `<span class="pre">`dev`</span> (pip).

</div>

<div id="testing" class="section">

## Testing<a href="#testing" class="headerlink" title="Link to this heading"></a>

Testing requires installation of the <span class="pre">`dev`</span> dependency group (see above).

Run <span class="pre">`pytest`</span>` `<span class="pre">`.`</span> from the top-level directory.

</div>

<div id="command-line-interface-usage" class="section">

<span id="cli-usage"></span>

## Command-Line Interface Usage<a href="#command-line-interface-usage" class="headerlink" title="Link to this heading"></a>

The Pyzotero CLI connects to your local Zotero installation and allows you to search your library, list collections, view item types, and manage collection membership.

<div id="basic-commands" class="section">

### Basic Commands<a href="#basic-commands" class="headerlink" title="Link to this heading"></a>

Search for top-level items:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero search -q "machine learning"
>
> </div>
>
> </div>
>
> </div>

Search with full-text mode:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero search -q "climate change" --fulltext
>
> </div>
>
> </div>
>
> </div>

Filter by item type:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero search -q "methodology" --itemtype book --itemtype journalArticle
>
> </div>
>
> </div>
>
> </div>

Search for top-level items within a collection:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero search --collection ABC123 -q "test"
>
> </div>
>
> </div>
>
> </div>

Output as JSON for machine processing:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero search -q "climate" --json
>
> </div>
>
> </div>
>
> </div>

Filter by tags (multiple tags use AND logic):

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero search -q "topic" --tag "climate" --tag "adaptation"
>
> </div>
>
> </div>
>
> </div>

Paginate results:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero search -q "topic" --limit 20 --offset 20 --json
>
> </div>
>
> </div>
>
> </div>

List all collections:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero listcollections
>
> </div>
>
> </div>
>
> </div>

List available item types:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero itemtypes
>
> </div>
>
> </div>
>
> </div>

List the fields and creator types that one item type accepts:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero listitemfields journalArticle
>
> </div>
>
> </div>
>
> </div>

</div>

<div id="item-and-attachment-commands" class="section">

### Item and Attachment Commands<a href="#item-and-attachment-commands" class="headerlink" title="Link to this heading"></a>

Get a single item by key:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero item ABC123 --json
>
> </div>
>
> </div>
>
> </div>

Get child items (attachments, notes) of an item:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero children ABC123 --json
>
> </div>
>
> </div>
>
> </div>

Get multiple items by key in a single call (up to 50):

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero subset ABC123 DEF456 GHI789 --json
>
> </div>
>
> </div>
>
> </div>

Get full-text content of an attachment:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero fulltext ABC123
>
> </div>
>
> </div>
>
> </div>

</div>

<div id="tag-commands" class="section">

### Tag Commands<a href="#tag-commands" class="headerlink" title="Link to this heading"></a>

List all tags in the library:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero tags
>
> </div>
>
> </div>
>
> </div>

List tags from a specific collection:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero tags --collection ABC123
>
> </div>
>
> </div>
>
> </div>

</div>

<div id="write-commands" class="section">

### Write Commands<a href="#write-commands" class="headerlink" title="Link to this heading"></a>

These commands write to your library, so they need a local API key. Run <span class="pre">`pyzotero`</span>` `<span class="pre">`authorize`</span> once and choose “Always Allow” in Zotero’s dialog. The key is stored in <span class="pre">`$XDG_CONFIG_HOME/pyzotero/local-api-key.json`</span> (<span class="pre">`~/.config/pyzotero/local-api-key.json`</span> if that variable is unset). Setting <span class="pre">`PYZOTERO_LOCAL_API_KEY`</span> in the environment takes precedence over the file.

Obtain and store a key:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero authorize --app-name "My tool"
>
> </div>
>
> </div>
>
> </div>

Create items from a JSON file, or from standard input:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero createitem item.json
>     cat items.json | pyzotero createitem -
>     pyzotero createitem items.json --collection FD9AUNP2 --tag "to read" --json
>
> </div>
>
> </div>
>
> </div>

The file contains one item object, or a list of them, in Zotero’s item-data format:

> <div>
>
> <div class="highlight-json notranslate">
>
> <div class="highlight">
>
>     [
>       {
>         "itemType": "book",
>         "title": "Frankenstein",
>         "creators": [{"creatorType": "author", "lastName": "Shelley", "firstName": "Mary"}],
>         "date": "1818"
>       }
>     ]
>
> </div>
>
> </div>
>
> </div>

<span class="pre">`--collection`</span> files every created item under one collection, and <span class="pre">`--tag`</span>, which you can repeat, tags every created item. Collections and tags that an item already has are kept. The item type and the field names of every item are checked against the library’s schema before anything is sent. <span class="pre">`pyzotero`</span>` `<span class="pre">`itemtypes`</span> lists the item types, and <span class="pre">`pyzotero`</span>` `<span class="pre">`listitemfields`</span>` `<span class="pre">`TYPE`</span> lists the fields of one type. Zotero accepts up to 50 items in one call.

Create a collection, at the top level or nested under <span class="pre">`--parent`</span>:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero createcollection "Frankenstein Cities" --parent FD9AUNP2
>
> </div>
>
> </div>
>
> </div>

Add items to a collection:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero addtocollection FD9AUNP2 ABC123 DEF456
>
> </div>
>
> </div>
>
> </div>

Remove items from a collection (the items themselves are unchanged):

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero removefromcollection FD9AUNP2 ABC123
>
> </div>
>
> </div>
>
> </div>

Move items from one collection to another:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero movetocollection --from FD9AUNP2 --to X7Y8Z9W0 ABC123 DEF456
>
> </div>
>
> </div>
>
> </div>

Each command accepts <span class="pre">`--json`</span> and reports the keys it touched. The membership commands change items one at a time. <span class="pre">`movetocollection`</span> changes each item in one request: its membership of other collections is kept. If Zotero rejects an item that <span class="pre">`createitem`</span> sends, the error gives its reason and names the items that were created.

</div>

<div id="doi-index" class="section">

### DOI Index<a href="#doi-index" class="headerlink" title="Link to this heading"></a>

Output the complete DOI-to-key mapping for caching:

> <div>
>
> <div class="highlight-bash notranslate">
>
> <div class="highlight">
>
>     pyzotero doiindex > doi_cache.json
>
> </div>
>
> </div>
>
> </div>

This returns a JSON mapping of normalised DOIs to item keys and original DOIs, allowing external tools to cache the index and avoid repeated full-library scans.

</div>

<div id="search-behaviour" class="section">

### Search Behaviour<a href="#search-behaviour" class="headerlink" title="Link to this heading"></a>

By default, <span class="pre">`pyzotero`</span>` `<span class="pre">`search`</span> searches only top-level item titles and metadata fields.

When the <span class="pre">`--fulltext`</span> flag is used, the search expands to include all full-text indexed content, including PDFs and other attachments. Since most full-text content comes from PDF attachments rather than top-level items, the CLI automatically retrieves the parent bibliographic items for any matching attachments. This ensures you receive useful bibliographic records (journal articles, books, etc.) rather than raw attachment items.

</div>

<div id="output-format" class="section">

### Output Format<a href="#output-format" class="headerlink" title="Link to this heading"></a>

By default, the CLI outputs human-readable text with all relevant metadata including:

- Title, authors, date, publication

- Volume, issue, DOI, URL

- PDF attachments (with local file paths)

Use the <span class="pre">`--json`</span> flag to output structured JSON suitable for consumption by other tools and agents.

</div>

</div>

<div id="mcp-server" class="section">

<span id="id7"></span>

## MCP Server<a href="#mcp-server" class="headerlink" title="Link to this heading"></a>

The <span class="pre">`pyzotero-mcp`</span> command starts an <a href="https://modelcontextprotocol.io" class="reference external">MCP</a> server over standard input and output. It exposes your local Zotero library, and the Semantic Scholar integration. This lets sandboxed applications use your library without access to the CLI. See <a href="#installation" class="reference internal"><span class="std std-ref">Installation</span></a> for how to install it.

The server is read-only unless it is started with <span class="pre">`--enable-writes`</span>.

<div id="claude-desktop-configuration" class="section">

### Claude Desktop Configuration<a href="#claude-desktop-configuration" class="headerlink" title="Link to this heading"></a>

Add one of the following to your Claude Desktop configuration file.

If <span class="pre">`pyzotero-mcp`</span> is installed:

> <div>
>
> <div class="highlight-json notranslate">
>
> <div class="highlight">
>
>     {
>       "mcpServers": {
>         "zotero": {
>           "command": "pyzotero-mcp"
>         }
>       }
>     }
>
> </div>
>
> </div>
>
> </div>

Or, without installing, using <span class="pre">`uvx`</span>:

> <div>
>
> <div class="highlight-json notranslate">
>
> <div class="highlight">
>
>     {
>       "mcpServers": {
>         "zotero": {
>           "command": "uvx",
>           "args": ["--from", "pyzotero[mcp]", "pyzotero-mcp"]
>         }
>       }
>     }
>
> </div>
>
> </div>
>
> </div>

</div>

<div id="zotero-library-tools" class="section">

### Zotero Library Tools<a href="#zotero-library-tools" class="headerlink" title="Link to this heading"></a>

| Tool | Description |
|----|----|
| <span class="pre">`search`</span> | Search the local Zotero library by query, item type, collection, tag, or full-text content |
| <span class="pre">`get_item`</span> | Get a single Zotero item by its key |
| <span class="pre">`get_children`</span> | Get the child items (attachments, notes) of a Zotero item |
| <span class="pre">`list_collections`</span> | List all collections in the library |
| <span class="pre">`list_tags`</span> | List all tags, optionally filtered by collection |
| <span class="pre">`get_fulltext`</span> | Get the full-text content of a PDF or other attachment |

</div>

<div id="semantic-scholar-tools" class="section">

### Semantic Scholar Tools<a href="#semantic-scholar-tools" class="headerlink" title="Link to this heading"></a>

| Tool | Description |
|----|----|
| <span class="pre">`find_related`</span> | Find semantically similar papers using SPECTER2 embeddings |
| <span class="pre">`get_citations`</span> | Find papers that cite a given paper |
| <span class="pre">`get_references`</span> | Find papers referenced by a given paper |
| <span class="pre">`search_semantic_scholar`</span> | Search across Semantic Scholar’s paper index |

Each Semantic Scholar tool accepts a <span class="pre">`check_library`</span> parameter, <span class="pre">`True`</span> by default, which annotates each result with whether the paper is already in your local Zotero library.

</div>

<div id="write-tools" class="section">

### Write Tools<a href="#write-tools" class="headerlink" title="Link to this heading"></a>

The write tools are opt-in. To enable them:

1.  Obtain a persistent local API key, choosing “Always Allow” in Zotero’s dialog:

    > <div>
    >
    > <div class="highlight-bash notranslate">
    >
    > <div class="highlight">
    >
    >     pyzotero authorize --app-name "Claude Desktop"
    >
    > </div>
    >
    > </div>
    >
    > </div>

    The key and the Zotero server ID are stored in <span class="pre">`$XDG_CONFIG_HOME/pyzotero/local-api-key.json`</span> (<span class="pre">`~/.config/pyzotero/local-api-key.json`</span> if that variable is unset), readable only by you. The server reads the key from that file.

2.  Add the <span class="pre">`--enable-writes`</span> flag to the server’s arguments:

    > <div>
    >
    > <div class="highlight-json notranslate">
    >
    > <div class="highlight">
    >
    >     {
    >       "mcpServers": {
    >         "zotero": {
    >           "command": "pyzotero-mcp",
    >           "args": ["--enable-writes"]
    >         }
    >       }
    >     }
    >
    > </div>
    >
    > </div>
    >
    > </div>

3.  Optional: to supply the key some other way, set <span class="pre">`PYZOTERO_LOCAL_API_KEY`</span> in the server’s <span class="pre">`env`</span> block, and <span class="pre">`PYZOTERO_LOCAL_SERVER_ID`</span> beside it to save one request at startup. The environment takes precedence over the key file. <span class="pre">`pyzotero`</span>` `<span class="pre">`authorize`</span>` `<span class="pre">`--no-store`</span> prints a key without writing the file.

With <span class="pre">`--enable-writes`</span>, the server registers these tools:

| Tool | Description |
|----|----|
| <span class="pre">`list_item_fields`</span> | List the fields and creator types valid for an item type |
| <span class="pre">`create_item`</span> | Create a new item |
| <span class="pre">`update_item`</span> | Update fields on an existing item |
| <span class="pre">`add_tags`</span> | Add tags to an existing item |
| <span class="pre">`create_collection`</span> | Create a collection, optionally nested |
| <span class="pre">`add_to_collection`</span> | File an existing item under a collection |
| <span class="pre">`remove_from_collection`</span> | Remove an item from a collection; the item itself is unchanged |
| <span class="pre">`move_to_collection`</span> | Move an item from one collection to another in one step |
| <span class="pre">`add_attachment`</span> | Attach a file on disk to an existing item |
| <span class="pre">`delete_item`</span> | Permanently delete an item. Requires <span class="pre">`--enable-deletes`</span> |

</div>

<div id="how-the-write-tools-behave" class="section">

### How the write tools behave<a href="#how-the-write-tools-behave" class="headerlink" title="Link to this heading"></a>

Without <span class="pre">`--enable-writes`</span>, the write tools are not merely disabled: they are never registered, so they do not appear in the model’s tool list at all, and content in your library cannot induce a call to one.

<span class="pre">`add_attachment`</span> requires an **absolute** path. The server runs as a subprocess of your MCP client, so its working directory is not yours, and a relative path would resolve somewhere unintended; relative paths are rejected. The file is copied into Zotero’s storage, and syncs with the library if sync is enabled. Attaching a file that is already attached to the item is reported as unchanged rather than duplicated.

<span class="pre">`delete_item`</span> is behind a second flag because deletion via the local API is irreversible: items are erased outright rather than moved to the trash, and the deletion propagates on sync. <span class="pre">`--enable-deletes`</span> implies <span class="pre">`--enable-writes`</span>.

</div>

</div>

<div id="building-documentation" class="section">

## Building Documentation<a href="#building-documentation" class="headerlink" title="Link to this heading"></a>

If you wish to build Pyzotero’s documentation for offline use, it can be built from the <span class="pre">`doc`</span> directory of a local git repo by running <span class="pre">`make`</span> followed by the desired output format(s) (<span class="pre">`html`</span>, <span class="pre">`epub`</span>, <span class="pre">`latexpdf`</span> etc.)

This functionality requires Sphinx. See the <a href="http://sphinx.pocoo.org/tutorial.html#running-the-build" class="reference external">Sphinx documentation</a> for full details.

</div>

<div id="reporting-issues" class="section">

## Reporting issues<a href="#reporting-issues" class="headerlink" title="Link to this heading"></a>

If you encounter an error while using Pyzotero, please open an issue on its <a href="https://github.com/urschrei/pyzotero/issues" class="reference external">Github issues page</a>.

</div>

</div>

<div id="general-usage" class="section">

# General Usage<a href="#general-usage" class="headerlink" title="Link to this heading"></a>

<div class="admonition important">

Important

A <span class="pre">`Zotero`</span> instance is bound to the library or group used to create it. Thus, if you create a <span class="pre">`Zotero`</span> instance with a <span class="pre">`library_id`</span> of <span class="pre">`67`</span> and a <span class="pre">`library_type`</span> of <span class="pre">`group`</span>, its item methods will only operate upon that group. Similarly, if you create a <span class="pre">`Zotero`</span> instance with your own <span class="pre">`library_id`</span> and a <span class="pre">`library_type`</span> of <span class="pre">`user`</span>, the instance will be bound to your Zotero library.

</div>

First, create a new Zotero instance:

> <div>
>
> <span class="property"><span class="k"><span class="pre">class</span></span><span class="w"> </span></span><span class="sig-prename descclassname"><span class="pre">zotero.</span></span><span class="sig-name descname"><span class="pre">Zotero</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">library_id</span></span>*, *<span class="n"><span class="pre">library_type</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">api_key</span></span>*, *<span class="n"><span class="pre">preserve_json_order</span></span>*, *<span class="n"><span class="pre">locale</span></span>*, *<span class="n"><span class="pre">local</span></span>*, *<span class="n"><span class="pre">client</span></span>*, *<span class="n"><span class="pre">upload_timeout</span></span>*, *<span class="n"><span class="pre">server_id</span></span>*, *<span class="n"><span class="pre">local_api_key</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero" class="headerlink" title="Link to this definition"></a>  
> Parameters<span class="colon">:</span>  
> - **library_id** (*str*) – a valid Zotero API user ID
>
> - **library_type** (*str*) – a valid Zotero API library type: **user** or **group**
>
> - **api_key** (*str*) – a valid Zotero API user key
>
> - **preserve_json_order** (*bool*) – Load JSON returns with OrderedDict to preserve their order
>
> - **locale** (*str*) – Set the <a href="https://www.zotero.org/support/dev/web_api/v3/types_and_fields#zotero_web_api_item_typefield_requests" class="reference external">locale</a>, allowing retrieval of localised item types, field types, and creator types. Defaults to “en-US”.
>
> - **local** (*str*) – use the local Zotero http server instead of the remote API. See <a href="#localapi" class="reference internal"><span class="std std-ref">The Local Zotero API</span></a>
>
> - **client** (*httpx2.Client*) – the HTTP client for API requests. If it is <span class="pre">`None`</span> (the default), Pyzotero creates a client with its default timeout. In local mode, that client ignores proxy settings from the environment. Pyzotero sends its default headers with each request: <span class="pre">`Authorization`</span> (if you supply <span class="pre">`api_key`</span>), <span class="pre">`Zotero-API-Version`</span> and <span class="pre">`User-Agent`</span>. They replace headers of the same name on the client. Pyzotero does not change a client that you supply, and the client keeps its own proxy settings. To use the local API when your environment sets a proxy, create the client with <span class="pre">`trust_env=False`</span>
>
> - **upload_timeout** (*int/float*) – timeout in seconds for file uploads to storage (default: 120). Increase this for very large files or slow connections.
>
> - **server_id** (*str*) – a local API server ID retained from a previous session. Only meaningful when <span class="pre">`local`</span> is <span class="pre">`True`</span>; see <a href="#localapi" class="reference internal"><span class="std std-ref">The Local Zotero API</span></a>
>
> - **local_api_key** (*str*) – a persistent local API key retained from a previous session, obtained from <a href="#zotero.Zotero.authorize_local" class="reference internal" title="zotero.Zotero.authorize_local"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.authorize_local()</code></span></a>. Only meaningful when <span class="pre">`local`</span> is <span class="pre">`True`</span>
>
> </div>

Example:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     from pyzotero import Zotero
>     zot = Zotero('123', 'user', 'ABC1234XYZ')
>     # we now have a Zotero object, zot, and access to all its methods
>     first_ten = zot.items(limit=10)
>     # a list containing dicts of the ten most recently modified library items
>
> </div>
>
> </div>
>
> </div>

<div id="errors" class="section">

<span id="read"></span>

## Errors<a href="#errors" class="headerlink" title="Link to this heading"></a>

Where possible, any <span class="pre">`ZoteroError`</span> which is raised will preserve the underlying error in its <span class="pre">`__cause__`</span> and <span class="pre">`__context__`</span> properties, should you wish to work with these directly.

The local API reuses several status codes for more than one condition, so Pyzotero inspects the response body and raises a more specific exception. Each subclasses the exception the status code alone would have produced, so existing handlers are unaffected:

> <div>
>
> - <span class="pre">`LocalAPIKeyRequiredError`</span> (401, subclasses <span class="pre">`UserNotAuthorisedError`</span>): no valid local API key. Call <a href="#zotero.Zotero.authorize_local" class="reference internal" title="zotero.Zotero.authorize_local"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.authorize_local()</code></span></a>.
>
> - <span class="pre">`LocalAPIDeniedError`</span> (403, subclasses <span class="pre">`UserNotAuthorisedError`</span>): the user denied an authorisation request.
>
> - <span class="pre">`ServerIDMismatchError`</span> (412, subclasses <span class="pre">`PreConditionFailedError`</span>): the request reached a different Zotero instance or database.
>
> - <span class="pre">`ServerIDRequiredError`</span> (428, subclasses <span class="pre">`PreConditionRequiredError`</span>): a local write carried no <span class="pre">`Zotero-Server-ID`</span> header.
>
> </div>

</div>

</div>

<div id="read-api-methods" class="section">

# Read API Methods<a href="#read-api-methods" class="headerlink" title="Link to this heading"></a>

<div class="admonition note">

Note

All search/request parameters inside square brackets are **optional**. Methods such as <a href="#zotero.Zotero.top" class="reference internal" title="zotero.Zotero.top"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.top()</code></span></a>, <a href="#zotero.Zotero.items" class="reference internal" title="zotero.Zotero.items"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.items()</code></span></a> etc. can be called with no additional parameters if you wish.

</div>

<div class="admonition tip">

Tip

The Read API returns 25 results by default (the API documentation claims 50). In the interests of usability, Pyzotero returns 100 items by default, by setting the API <span class="pre">`limit`</span> parameter to 100, unless it’s set by the user. If you wish to retrieve e.g. all top-level items without specifying a <span class="pre">`limit`</span> parameter, you’ll have to wrap your call with <a href="#zotero.Zotero.everything" class="reference internal" title="zotero.Zotero.everything"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.everything()</code></span></a>: <span class="pre">`results`</span>` `<span class="pre">`=`</span>` `<span class="pre">`zot.everything(zot.top())`</span>.

</div>

<div id="search-request-parameters-for-read-api-calls" class="section">

## Search / Request Parameters for Read API calls<a href="#search-request-parameters-for-read-api-calls" class="headerlink" title="Link to this heading"></a>

Additional parameters may be set on Read API methods **following any required parameters**, or set using the <a href="#zotero.Zotero.add_parameters" class="reference internal" title="zotero.Zotero.add_parameters"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.add_parameters()</code></span></a> method detailed below.

The following two examples produce the same result:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     # set parameters on the call itself
>     z = zot.top(limit=7, start=3)
>
>     # set parameters using explicit method
>     zot.add_parameters(limit=7, start=3)
>     z = zot.top()
>
> </div>
>
> </div>
>
> </div>

The following parameters are **optional**.

**You may also set a search term here, using the ‘itemType’, ‘q’, ‘qmode’, or ‘tag’ parameters**.

This area of the Zotero Read API is under development, and may change frequently. See <a href="https://www.zotero.org/support/dev/web_api/v3/basics#read_requests" class="reference external">the API documentation</a> for the most up-to-date details of search syntax usage and export format details.

> <div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">add_parameters</span></span><span class="sig-paren">(</span><span class="optional">\[</span>*<span class="n"><span class="pre">format</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">itemKey</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">itemType</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">q</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">qmode</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">since</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">tag</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sort</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">direction</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">limit</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">start</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">content</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">style</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="optional">\]</span><span class="optional">\]</span><span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.add_parameters" class="headerlink" title="Link to this definition"></a>  
> Parameters<span class="colon">:</span>  
> **format** (*str*) – “atom”, “bib”, “bibtex”, json”, “keys”, “versions”. Pyzotero retrieves and decodes JSON responses by default
>
> <div class="admonition attention">
>
> Attention
>
> Setting <span class="pre">`format='bib'`</span> will remove the <span class="pre">`limit`</span> parameter if it’s been set, as **the API does not allow a limit on bibliography output**; it instead enforces a limit of 150 items, and if the set of items you are trying to generate a bibliography for exceeds 150, an error will be raised.
>
> </div>
>
> Parameters<span class="colon">:</span>  
> **itemKey** (*str*) – A comma-separated list of item keys. Valid only for item requests. Up to 50 items can be specified in a single request
>
> Search parameters:
>
> Parameters<span class="colon">:</span>  
> - **itemType** (*str*) – item type search. See the <a href="https://www.zotero.org/support/dev/web_api/v3/basics#search_syntax" class="reference external">Search Syntax</a> for details
>
> - **q** (*str*) – Quick search. Searches titles and individual creator fields by default. Use the <span class="pre">`qmode`</span> parameter to change the mode. Currently supports phrase searching only
>
> - **qmode** (*str*) – Quick search mode. To include full-text content in the search, use <span class="pre">`everything`</span>. Defaults to <span class="pre">`titleCreatorYear`</span>. Searching of other fields will be possible in the future
>
> - **since** (*int*) – default <span class="pre">`0`</span>. Return only objects modified after the specified library version
>
> - **tag** (*str*) –
>
>   tag search. See the <a href="https://www.zotero.org/support/dev/web_api/v3/basics#search_syntax" class="reference external">Search Syntax</a> for details. More than one tag may be passed by passing a list of strings – These are treated as <span class="pre">`AND`</span> search terms, meaning only items which include all of the specified tags are returned. You can search for items matching any tag in a list by using <span class="pre">`OR`</span>: <span class="pre">`"tag1`</span>` `<span class="pre">`OR`</span>` `<span class="pre">`tag2"`</span>, and all items which exclude a tag: <span class="pre">`"-tag"`</span>.
>
> The following parameters can be used for search requests:
>
> Parameters<span class="colon">:</span>  
> - **sort** (*str*) – The name of the field by which entries are sorted: (<span class="pre">`dateAdded`</span>, <span class="pre">`dateModified`</span>, <span class="pre">`title`</span>, <span class="pre">`creator`</span>, <span class="pre">`type`</span>, <span class="pre">`date`</span>, <span class="pre">`publisher`</span>, <span class="pre">`publicationTitle`</span>, <span class="pre">`journalAbbreviation`</span>, <span class="pre">`language`</span>, <span class="pre">`accessDate`</span>, <span class="pre">`libraryCatalog`</span>, <span class="pre">`callNumber`</span>, <span class="pre">`rights`</span>, <span class="pre">`addedBy`</span>, <span class="pre">`numItems`</span>, <span class="pre">`tags`</span>)
>
> - **direction** (*str*) – <span class="pre">`asc`</span> or <span class="pre">`desc`</span>
>
> - **limit** (*int*) – 1 – 100 or None
>
> - **start** (*int*) – 1 – total number of items in your library or None
>
> If you wish to retrieve citation or bibliography entries, use the following parameters:
>
> Parameters<span class="colon">:</span>  
> - **content** (*str*) – ‘bib’, ‘html’, or one of the export formats (see below). If ‘bib’ is passed, you may **also** pass:
>
> - **style** (*str*) – Any valid CSL style in the Zotero style repository
>
> - **linkwrap** (*str*) – Set this to “1” to have URLs in bibliography entries (see below) wrapped in <span class="pre">`<a>`</span> tags.
>
> Return type<span class="colon">:</span>  
> list of HTML strings or None.
>
> </div>

<div class="admonition note">

Note

Any parameters you set will be valid **for the next call only**. Any parameters set using <span class="pre">`add_parameters()`</span> will be overridden by parameters you pass in the call itself.

</div>

A note on the <span class="pre">`content`</span> and <span class="pre">`style`</span> parameters:

Example:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     zot.add_parameters(content='bib', style='mla')
>
> </div>
>
> </div>
>
> </div>

If these are set, the return value is a list of UTF-8 formatted HTML <span class="pre">`div`</span> elements, each containing an item:

<span class="pre">`['<div`</span>` `<span class="pre">`class="csl-entry">(content)</div>']`</span>.

You may also set <span class="pre">`content='citation'`</span> if you wish to retrieve citations. Similar to <span class="pre">`bib`</span>, the result will be a list of one or more HTML <span class="pre">`span`</span> elements.

If you select one of the available <a href="https://www.zotero.org/support/dev/web_api/v3/basics#export_formats" class="reference external">export formats</a> as the <span class="pre">`content`</span> parameter, pyzotero will in most cases return a list of unicode strings in the format you specified. The exception is the <span class="pre">`csljson`</span> format, which is parsed into a list of dicts. Please note that you must provide a <span class="pre">`limit`</span> parameter if you specify one of these export formats. Multiple simultaneous retrieval of particular formats, e.g. <span class="pre">`content="json,coins"`</span> is not currently supported.

If you set <span class="pre">`format='keys'`</span>, a newline-delimited string containing item keys will be returned

If you set <span class="pre">`format='bibtex'`</span>, a <a href="https://bibtexparser.readthedocs.io/en/main/bibtexparser.html" class="reference external">bibtexparser</a> object containing citations will be returned. You can access the citations as a list of dicts using the <span class="pre">`.entries`</span> property. The bibtexparser object also implements a <a href="https://bibtexparser.readthedocs.io/en/main/customize.html#formatting-options-for-writing" class="reference external">dump method</a>, if you’d like to write your citations to a <span class="pre">`.bib`</span> file.

<span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">key_info</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#zotero.Zotero.key_info" class="headerlink" title="Link to this definition"></a>  
Returns info about the user and group library permissions associated with the current <span class="pre">`Zotero`</span> instance, based on the API key. Together with <a href="#zotero.Zotero.groups" class="reference internal" title="zotero.Zotero.groups"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.groups()</code></span></a>, this allows all accessible resources to be determined.

Return type<span class="colon">:</span>  
dict

</div>

<div id="retrieving-items" class="section">

## Retrieving Items<a href="#retrieving-items" class="headerlink" title="Link to this heading"></a>

<div class="admonition tip">

Tip

In contrast to the v1 API, a great deal of additional metadata is now returned. In most cases, simply accessing items by referring to their <span class="pre">`item['data']`</span> key will suffice.

</div>

The following methods will retrieve either user or group items, depending on the value (<span class="pre">`user`</span> or <span class="pre">`group`</span>) used to create the <span class="pre">`Zotero`</span> instance:

> <div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">items</span></span><span class="sig-paren">(</span><span class="optional">\[</span>*<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.items" class="headerlink" title="Link to this definition"></a>  
> Returns Zotero library items
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">settings</span></span><span class="sig-paren">(</span><span class="optional">\[</span>*<span class="n"><span class="pre">since</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.settings" class="headerlink" title="Link to this definition"></a>  
> Returns synced Zotero user library settings such as feeds and PDF reading progress. Use the optional <span class="pre">`since`</span> parameter to specify the retrieval of changes since a known previous library version.
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">count_items</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#zotero.Zotero.count_items" class="headerlink" title="Link to this definition"></a>  
> Returns a count of all items in a library / group
>
> Return type<span class="colon">:</span>  
> int
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">top</span></span><span class="sig-paren">(</span><span class="optional">\[</span>*<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.top" class="headerlink" title="Link to this definition"></a>  
> Returns top-level Zotero library items
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">publications</span></span><span class="sig-paren">(</span><span class="optional">\[</span>*<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.publications" class="headerlink" title="Link to this definition"></a>  
> Returns the publications from the “My Publications” collection of a user’s library. Only available on <span class="pre">`user`</span> libraries.
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">trash</span></span><span class="sig-paren">(</span><span class="optional">\[</span>*<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.trash" class="headerlink" title="Link to this definition"></a>  
> Returns library items from the library’s trash
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">deleted</span></span><span class="sig-paren">(</span><span class="optional">\[</span>*<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.deleted" class="headerlink" title="Link to this definition"></a>  
> Returns deleted collections, library items, tags, searches and settings (requires “since=” parameter)
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">item</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">itemID</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.item" class="headerlink" title="Link to this definition"></a>  
> Returns a specific item
>
> Parameters<span class="colon">:</span>  
> **itemID** (*str*) – a zotero item ID
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">children</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">itemID</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.children" class="headerlink" title="Link to this definition"></a>  
> Returns the child items of a specific item
>
> Parameters<span class="colon">:</span>  
> **itemID** (*str*) – a zotero item ID
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">collection_items</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">collectionID</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.collection_items" class="headerlink" title="Link to this definition"></a>  
> Returns items from the specified collection. This does not include items in sub-collections
>
> Parameters<span class="colon">:</span>  
> **collectionID** (*str*) – a Zotero collection ID
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">collection_items_top</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">collectionID</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.collection_items_top" class="headerlink" title="Link to this definition"></a>  
> Returns top-level items from the specified collection.
>
> Parameters<span class="colon">:</span>  
> **collectionID** (*str*) – a Zotero collection ID
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">get_subset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">itemIDs</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.get_subset" class="headerlink" title="Link to this definition"></a>  
> Retrieve an arbitrary set of non-adjacent items. Limited to 50 items per call.
>
> Parameters<span class="colon">:</span>  
> **itemIDs** (*list*) – a list of Zotero Item IDs
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> </div>

Example of returned item data:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     [{u'data': {u'ISBN': u'0810116820',
>                u'abstractNote': u'',
>                u'accessDate': u'',
>                u'archive': u'',
>                u'archiveLocation': u'',
>                u'callNumber': u'HIB 828.912 BEC:3g N9',
>                u'collections': [u'2UNGXMU9'],
>                u'creators': [{u'creatorType': u'author',
>                               u'firstName': u'Daniel',
>                               u'lastName': u'Katz'}],
>                u'date': u'1999',
>                u'dateAdded': u'2010-01-04T14:50:40Z',
>                u'dateModified': u'2014-08-06T11:28:41Z',
>                u'edition': u'',
>                u'extra': u'',
>                u'itemType': u'book',
>                u'key': u'${OBJECT_KEY}',
>                u'language': u'',
>                u'libraryCatalog': u'library.catalogue.tcd.ie Library Catalog',
>                u'numPages': u'',
>                u'numberOfVolumes': u'',
>                u'place': u'Evanston, Ill',
>                u'publisher': u'Northwestern University Press',
>                u'relations': {u'dc:replaces': u'http://zotero.org/users/${LIBRARY_ID}/items/9TXN8QUD'},
>                u'rights': u'',
>                u'series': u'',
>                u'seriesNumber': u'',
>                u'shortTitle': u'Saying I No More',
>                u'tags': [{u'tag': u'Beckett, Samuel', u'type': 1},
>                          {u'tag': u'Consciousness in literature', u'type': 1},
>                          {u'tag': u'English prose literature', u'type': 1},
>                          {u'tag': u'Ireland', u'type': 1},
>                          {u'tag': u'Irish authors', u'type': 1},
>                          {u'tag': u'Modernism (Literature)', u'type': 1},
>                          {u'tag': u'Prose', u'type': 1},
>                          {u'tag': u'Self in literature', u'type': 1},
>                          {u'tag': u'Subjectivity in literature', u'type': 1}],
>                u'title': u'Saying I No More: Subjectivity and Consciousness in The Prose of Samuel Beckett',
>                u'url': u'',
>                u'version': 792,
>                u'volume': u''},
>      u'key': u'${OBJECT_KEY}',
>      u'library': {u'id': 436,
>                   u'links': {u'alternate': {u'href': u'https://www.zotero.org/urschrei',
>                                             u'type': u'text/html'}},
>                   u'name': u'urschrei',
>                   u'type': u'user'},
>      u'links': {u'alternate': {u'href': u'https://www.zotero.org/urschrei/items/VDNIEAPH',
>                                u'type': u'text/html'},
>                 u'self': {u'href': u'https://api.zotero.org/users/${LIBRARY_ID}/items/VDNIEAPH',
>                           u'type': u'application/json'}},
>      u'meta': {u'creatorSummary': u'Katz',
>                u'numChildren': 0,
>                u'parsedDate': u'1999-00-00'},
>      u'version': 792}]
>
> </div>
>
> </div>
>
> </div>

See <a href="#hello-world" class="reference internal"><span class="std std-ref">‘Hello World’</span></a> example, above

</div>

<div id="retrieving-files" class="section">

## Retrieving Files<a href="#retrieving-files" class="headerlink" title="Link to this heading"></a>

> <div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">file</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">itemID</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.file" class="headerlink" title="Link to this definition"></a>  
> Returns the raw file content of an item. This can be dumped like so:
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     with open('article.pdf', 'wb') as f:
>       f.write(zot.file('BM8MZJBB'))
>
> </div>
>
> </div>
>
> Parameters<span class="colon">:</span>  
> **itemID** (*str*) – a zotero item ID
>
> Return type<span class="colon">:</span>  
> binary string
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">dump</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">itemID</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">filename</span></span>*, *<span class="n"><span class="pre">path</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.dump" class="headerlink" title="Link to this definition"></a>  
> A convenient wrapper around <a href="#zotero.Zotero.file" class="reference internal" title="zotero.Zotero.file"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.<span class="bu">file</span>()</code></span></a>. Writes an attachment to disk using the optional path and filename. If neither are supplied, the file is written to the current working directory, and a <a href="#zotero.Zotero.item" class="reference internal" title="zotero.Zotero.item"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.item()</code></span></a> call is first made to determine the attachment filename. No error checking is done regarding the path. If successful, the full path including the file name is returned.
>
> <div class="admonition note">
>
> Note
>
> HTML snapshots will be dumped as zip files. These will be named with their API item key, and a .zip extension.
>
> </div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     # write a file to the current working directory using the stored filename
>     zot.dump('BM8MZJBB')
>     # write the same file to a different path, with a new name
>     zot.dump('BM8MZJBB', 'article_1.pdf', '${USER_HOME}/pdfs')
>
> </div>
>
> </div>
>
> Parameters<span class="colon">:</span>  
> - **itemID** (*str*) – a zotero item ID
>
> - **filename** (*str*) – (optional) an alternate filename
>
> - **path** (*str*) – (optional) a valid path for the file
>
> Return type<span class="colon">:</span>  
> String
>
> </div>

File retrieval and dumping should work for most common document, audio and video file formats. If you encounter an error, <a href="https://github.com/urschrei/pyzotero/issues" class="reference external">please open an issue</a>.

</div>

<div id="retrieving-collections" class="section">

## Retrieving Collections<a href="#retrieving-collections" class="headerlink" title="Link to this heading"></a>

> <div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">collections</span></span><span class="sig-paren">(</span><span class="optional">\[</span>*<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.collections" class="headerlink" title="Link to this definition"></a>  
> Returns a library’s collections. **This includes subcollections**.
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">collections_top</span></span><span class="sig-paren">(</span><span class="optional">\[</span>*<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.collections_top" class="headerlink" title="Link to this definition"></a>  
> Returns a library’s top-level collections.
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">collection</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">collectionID</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.collection" class="headerlink" title="Link to this definition"></a>  
> Returns a specific collection
>
> Parameters<span class="colon">:</span>  
> **collectionID** (*str*) – a Zotero library collection ID
>
> Return type<span class="colon">:</span>  
> dict
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">collections_sub</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">collectionID</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.collections_sub" class="headerlink" title="Link to this definition"></a>  
> Returns the sub-collections of a specific collection
>
> Parameters<span class="colon">:</span>  
> **collectionID** (*str*) – a Zotero library collection ID
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">all_collections</span></span><span class="sig-paren">(</span><span class="optional">\[</span>*<span class="n"><span class="pre">collectionID</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.all_collections" class="headerlink" title="Link to this definition"></a>  
> Returns either all collections and sub-collections in a flat list, or, if a collection ID is specified, that collection and all of its sub-collections. This method can be called at any collection “depth”.
>
> Parameters<span class="colon">:</span>  
> **collectionID** (*str*) – a Zotero library collection ID (optional)
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> </div>

Example of returned collection data:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     [{u'data': {u'key': u'${OBJECT_KEY}',
>                 u'name': u'Critical GIS',
>                 u'parentCollection': False,
>                 u'relations': {},
>                 u'version': 778},
>       u'key': u'${OBJECT_KEY}',
>       u'library': {u'id': 436,
>                    u'links': {u'alternate': {u'href': u'https://www.zotero.org/urschrei',
>                                              u'type': u'text/html'}},
>                    u'name': u'urschrei',
>                    u'type': u'user'},
>       u'links': {u'alternate': {u'href': u'https://www.zotero.org/urschrei/collections/5TSDXJG6',
>                                 u'type': u'text/html'},
>                  u'self': {u'href': u'https://api.zotero.org/users/${LIBRARY_ID}/collections/5TSDXJG6',
>                            u'type': u'application/json'}},
>       u'meta': {u'numCollections': 0, u'numItems': 1},
>       u'version': 778}]
>
> </div>
>
> </div>
>
> </div>

</div>

<div id="retrieving-groups" class="section">

## Retrieving groups<a href="#retrieving-groups" class="headerlink" title="Link to this heading"></a>

> <div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">groups</span></span><span class="sig-paren">(</span><span class="optional">\[</span>*<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.groups" class="headerlink" title="Link to this definition"></a>  
> Retrieve the Zotero group data to which the current library_id and api_key has access
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> </div>

Example of returned group data:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     [{u'data': {u'description': u'',
>                 u'fileEditing': u'admins',
>                 u'hasImage': 1,
>                 u'id': 169947,
>                 u'libraryEditing': u'admins',
>                 u'libraryReading': u'members',
>                 u'members': [1177919, 1408658],
>                 u'name': u'smart_cities',
>                 u'owner': 436,
>                 u'type': u'Private',
>                 u'url': u'',
>                 u'version': 0},
>       u'id': 169947,
>       u'links': {u'alternate': {u'href': u'https://www.zotero.org/groups/${GROUP_ID}',
>                                 u'type': u'text/html'},
>                  u'self': {u'href': u'https://api.zotero.org/groups/${GROUP_ID}',
>                            u'type': u'application/json'}},
>       u'meta': {u'created': u'2013-05-22T11:22:46Z',
>                 u'lastModified': u'2013-05-22T11:26:50Z',
>                 u'numItems': 817},
>       u'version': 0}]
>
> </div>
>
> </div>
>
> </div>

</div>

<div id="retrieving-tags" class="section">

## Retrieving Tags<a href="#retrieving-tags" class="headerlink" title="Link to this heading"></a>

> <div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">tags</span></span><span class="sig-paren">(</span><span class="optional">\[</span>*<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.tags" class="headerlink" title="Link to this definition"></a>  
> Returns a library’s tags
>
> Return type<span class="colon">:</span>  
> list of strings
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">item_tags</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">itemID</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.item_tags" class="headerlink" title="Link to this definition"></a>  
> Returns tags from a specific item
>
> Parameters<span class="colon">:</span>  
> **itemID** (*str*) – a valid Zotero library Item ID
>
> Return type<span class="colon">:</span>  
> list of strings
>
> </div>

Example of returned tag data:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     ['Authority in literature', 'Errata']
>
> </div>
>
> </div>
>
> </div>

</div>

<div id="retrieving-version-information" class="section">

## Retrieving Version Information<a href="#retrieving-version-information" class="headerlink" title="Link to this heading"></a>

The <a href="https://www.zotero.org/support/dev/web_api/v3/syncing" class="reference external">Zotero API</a> recommends requesting version information for all (or all changed) items and collections when implementing syncing. The following convenience methods (which by default return an unlimited number of responses) simplify this process.

The return values of these methods associate each item / collection with the last version (or greater) at which the item / collection was modified. By passing the keyword argument <span class="pre">`since=versionNum`</span> only items / collections which have been modified since <span class="pre">`versionNum`</span> are included in the response. Thus, an application which previously sucessfully synced with the server at <span class="pre">`versionNum`</span> can use these methods to determine which items / collections need to be retrieved from the server.

> <div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">item_versions</span></span><span class="sig-paren">(</span><span class="optional">\[</span>*<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.item_versions" class="headerlink" title="Link to this definition"></a>  
> Returns a dict containing version information for items in the library
>
> Return type<span class="colon">:</span>  
> dict: string -\> integer
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">collection_versions</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">itemID</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.collection_versions" class="headerlink" title="Link to this definition"></a>  
> Returns a dict containing version information for collections in the library
>
> Return type<span class="colon">:</span>  
> dict: string -\> integer
>
> </div>

Example of returned version data:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     {'C9KW275P': 3915, 'IB489TKM': 4025 }
>
> </div>
>
> </div>
>
> </div>

</div>

<div id="fulltext-content" class="section">

## Full–Text Content<a href="#fulltext-content" class="headerlink" title="Link to this heading"></a>

These methods allow the retrieval of full–text content for given library items

> <div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">new_fulltext</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">since</span></span>*<span class="sig-paren">)</span><a href="#zotero.Zotero.new_fulltext" class="headerlink" title="Link to this definition"></a>  
>
> Returns a dict containing item keys and library versions newer than <span class="pre">`since`</span> (a library version string, e.g. <span class="pre">`"1085"`</span>)
>
> rtype<span class="colon">:</span>  
> dict: string -\> integer
>
> </div>

Example of returned data:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     {
>         u'229QED6I': 747,
>         u'22TGJFS2': 769,
>         u'23SZWREM': 764
>     }
>
> </div>
>
> </div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">fulltext_item</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">itemID</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.fulltext_item" class="headerlink" title="Link to this definition"></a>  
>
> Returns a dict containing full-text data for the given attachment item. <span class="pre">`indexedChars`</span> and <span class="pre">`totalChars`</span> are used for text documents, while <span class="pre">`indexedPages`</span> and <span class="pre">`totalPages`</span> are used for PDFs.
>
> </div>

Example of returned data:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     {
>     "content": "This is full-text content.",
>     "indexedPages": 50,
>     "totalPages": 50
>     }
>
> </div>
>
> </div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">set_fulltext</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">itemID</span></span>*, *<span class="n"><span class="pre">payload</span></span>*<span class="sig-paren">)</span><a href="#zotero.Zotero.set_fulltext" class="headerlink" title="Link to this definition"></a>  
>
> Set full-text data for an item
>
> rtype<span class="colon">:</span>  
> boolean
>
> <span class="pre">`itemID`</span> should correspond to an existing attachment item.
>
> <span class="pre">`payload`</span>: a dict containing three keys:
>
> > <div>
> >
> > <span class="pre">`content`</span>: the full-text content, and either
> >
> > For text documents, <span class="pre">`indexedChars`</span> and <span class="pre">`totalChars`</span> OR
> >
> > For PDFs, <span class="pre">`indexedPages`</span> and <span class="pre">`totalPages`</span>.
> >
> > </div>
>
> </div>

Example payload:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     {
>     "content": "This is full-text content.",
>     "indexedPages": 50,
>     "totalPages": 50
>     }
>
> </div>
>
> </div>
>
> </div>

</div>

<div id="the-follow-and-everything-methods" class="section">

## The <span class="pre">`follow()`</span>, and <span class="pre">`everything()`</span> methods<a href="#the-follow-and-everything-methods" class="headerlink" title="Link to this heading"></a>

These methods (currently experimental) aim to make Pyzotero a little more RESTful. Following any Read API call which can retrieve **multiple items**, calling <span class="pre">`follow()`</span> will repeat that call, but for the next *x* number of items, where *x* is either a number set by the user for the original call, or 50 by default. Each subsequent call to <span class="pre">`follow()`</span> will extend the offset.

<span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">follow</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#zotero.Zotero.follow" class="headerlink" title="Link to this definition"></a>  
Returns <span class="pre">`None`</span> once all available items have been retrieved.

Example:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     from pyzotero import Zotero
>     zot = Zotero(library_id, library_type, api_key)
>     # only retrieve a single item
>     # this will retrieve the most recently added/modified top-level item
>     first_item = zot.top(limit=1)
>     # now we can start retrieving subsequent items
>     next_item = zot.follow()
>     third_item = zot.follow()
>
> </div>
>
> </div>
>
> <span class="pre">`follow()`</span> can thus be used to page through an entire library:
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     items = zot.items()
>     while items:
>         for item in items:
>             # do stuff with the item
>             ...
>         items = zot.follow()
>
> </div>
>
> </div>
>
> </div>

<span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">everything</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#zotero.Zotero.everything" class="headerlink" title="Link to this definition"></a>  

Example:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     from pyzotero import Zotero
>     zot = Zotero(library_id, library_type, api_key)
>     # retrieve all top-level items
>     toplevel = zot.everything(zot.top())
>
> </div>
>
> </div>
>
> </div>

The <span class="pre">`everything()`</span> method should work with all Pyzotero Read API calls which can return multiple items, but has not yet been extensively tested. <a href="https://github.com/urschrei/pyzotero/issues" class="reference external">Feedback is welcomed</a>.

<div id="related-generator-methods" class="section">

### Related generator methods<a href="#related-generator-methods" class="headerlink" title="Link to this heading"></a>

The <a href="#zotero.Zotero.iterfollow" class="reference internal" title="zotero.Zotero.iterfollow"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.iterfollow()</code></span></a> and <a href="#zotero.Zotero.makeiter" class="reference internal" title="zotero.Zotero.makeiter"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.makeiter()</code></span></a> methods are available for users who prefer to work directly with generators:

<span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">iterfollow</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#zotero.Zotero.iterfollow" class="headerlink" title="Link to this definition"></a>  
Return type<span class="colon">:</span>  
a generator over the <a href="#zotero.Zotero.follow" class="reference internal" title="zotero.Zotero.follow"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">follow()</code></span></a> method.

Example:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     z = zot.top(limit=5)
>     lazy = zot.iterfollow()
>     next(lazy) # the next() call has returned the next five items
>
> </div>
>
> </div>
>
> </div>

<span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">makeiter</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">API</span> <span class="pre">call</span></span>*<span class="sig-paren">)</span><a href="#zotero.Zotero.makeiter" class="headerlink" title="Link to this definition"></a>  
Returns a generator over a Read API method

Parameters<span class="colon">:</span>  
**call** (*function API*) – a Pyzotero Read API method capable of returning multiple items

Return type<span class="colon">:</span>  
generator

Example:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     gen = zot.makeiter(zot.top(limit=5))
>     next(gen) # this will return the first five items
>     next(gen) # this will return the next five items
>
> </div>
>
> </div>
>
> </div>

<div class="admonition warning">

Warning

The <span class="pre">`follow()`</span>, <span class="pre">`everything()`</span> and <span class="pre">`makeiter()`</span> methods are only valid for methods which can return multiple library items. For instance, you cannot use <span class="pre">`follow()`</span> after an <span class="pre">`item()`</span> call. The generator methods will raise a <span class="pre">`StopIteration`</span> error when all available items retrievable by your chosen API call have been exhausted.

</div>

</div>

</div>

<div id="retrieving-item-counts" class="section">

## Retrieving item counts<a href="#retrieving-item-counts" class="headerlink" title="Link to this heading"></a>

If you wish to retrieve item counts for subsets of a library, you can use the following methods:

<span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">num_items</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#zotero.Zotero.num_items" class="headerlink" title="Link to this definition"></a>  
Returns the count of top-level items in the library

Return type<span class="colon">:</span>  
int

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">num_collectionitems</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">collectionID</span></span>*<span class="sig-paren">)</span><a href="#zotero.Zotero.num_collectionitems" class="headerlink" title="Link to this definition"></a>  
Returns the count of items in the specified collection

Return type<span class="colon">:</span>  
int

</div>

<div id="retrieving-last-modified-version" class="section">

## Retrieving last modified version<a href="#retrieving-last-modified-version" class="headerlink" title="Link to this heading"></a>

If you wish to retrieve the last modified version of a user or group library, you can use the following method:

<span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">last_modified_version</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#zotero.Zotero.last_modified_version" class="headerlink" title="Link to this definition"></a>  
Returns the last modified version of the library

Return type<span class="colon">:</span>  
int

</div>

</div>

<div id="the-local-zotero-api" class="section">

<span id="localapi"></span>

# The Local Zotero API<a href="#the-local-zotero-api" class="headerlink" title="Link to this heading"></a>

Setting <span class="pre">`local=True`</span> directs Pyzotero at the HTTP API served by a running Zotero installation (<span class="pre">`http://127.0.0.1:23119/api`</span>) instead of <span class="pre">`api.zotero.org`</span>. It must first be enabled in Zotero, under Settings \> Advanced \> “Allow other applications on this computer to communicate with Zotero”.

Read requests need no authentication. Write requests need two things: a server ID, which Pyzotero handles for you, and a local API key, which requires the user’s consent.

This section is organised in three parts: <a href="#localapi-explanation" class="reference internal"><span class="std std-ref">How local write access works</span></a> covers the concepts behind local write access, <a href="#localapi-howto" class="reference internal"><span class="std std-ref">How-to guides</span></a> gives step-by-step recipes for common tasks, and <a href="#localapi-reference" class="reference internal"><span class="std std-ref">Reference</span></a> describes the attribute, the method, and the behavioural differences from the web API.

<div id="how-local-write-access-works" class="section">

<span id="localapi-explanation"></span>

## How local write access works<a href="#how-local-write-access-works" class="headerlink" title="Link to this heading"></a>

<div id="server-ids" class="section">

### Server IDs<a href="#server-ids" class="headerlink" title="Link to this heading"></a>

Every local API response carries a <span class="pre">`Zotero-Server-ID`</span> header identifying the Zotero instance the data came from. It persists with the user’s database. Pyzotero caches it from the first local response and sends it back on subsequent requests, so that a request made against a different instance — or the same one after a database restore — is rejected with <span class="pre">`ServerIDMismatchError`</span> rather than silently mixing data. You never need to fetch the ID yourself: Pyzotero obtains it automatically before the first write. It matters to you only if your program persists data between runs, in which case see the warning below and <a href="#localapi-howto-persist" class="reference internal"><span class="std std-ref">How to keep write access across sessions</span></a>.

</div>

<div id="versions" class="section">

### Versions<a href="#versions" class="headerlink" title="Link to this heading"></a>

<div class="admonition warning">

Warning

Versions reported by the local API are scoped to a server ID. They bear **no relation** to web API versions, nor to versions from any other Zotero instance, and because local changes need no sync they are typically **lower** than the versions the local API reported before write support was added. Any program that persists objects or versions retrieved from the local API — for <span class="pre">`since=`</span> queries, or its own change tracking — must partition that data by <span class="pre">`server_id`</span>, and should discard data cached against a different one. A mismatch raises <span class="pre">`ServerIDMismatchError`</span>.

</div>

</div>

<div id="local-api-keys" class="section">

### Local API keys<a href="#local-api-keys" class="headerlink" title="Link to this heading"></a>

Local API keys are unrelated to zotero.org API keys: they are granted by the running Zotero application itself, and only with the user’s consent. Requesting one makes Zotero display a dialog offering three choices. “Allow” grants a **single-use** key: the first successful write consumes it, and the next write fails with <span class="pre">`LocalAPIKeyRequiredError`</span>. “Always Allow” grants a persistent key, which the caller may store and reuse across sessions. “Deny” raises <span class="pre">`LocalAPIDeniedError`</span>.

</div>

</div>

<div id="how-to-guides" class="section">

<span id="localapi-howto"></span>

## How-to guides<a href="#how-to-guides" class="headerlink" title="Link to this heading"></a>

<div id="how-to-make-your-first-local-write" class="section">

### How to make your first local write<a href="#how-to-make-your-first-local-write" class="headerlink" title="Link to this heading"></a>

1.  Create a client with <span class="pre">`local=True`</span>.

2.  Call <a href="#zotero.Zotero.authorize_local" class="reference internal" title="zotero.Zotero.authorize_local"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.authorize_local()</code></span></a> and approve the dialog Zotero displays.

3.  Call any write method.

<div class="highlight-python notranslate">

<div class="highlight">

    from pyzotero import Zotero

    zot = Zotero('0', 'user', local=True)
    zot.authorize_local('My Application')  # Zotero prompts the user
    zot.create_items([item])

</div>

</div>

</div>

<div id="how-to-keep-write-access-across-sessions" class="section">

<span id="localapi-howto-persist"></span>

### How to keep write access across sessions<a href="#how-to-keep-write-access-across-sessions" class="headerlink" title="Link to this heading"></a>

1.  Call <a href="#zotero.Zotero.authorize_local" class="reference internal" title="zotero.Zotero.authorize_local"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.authorize_local()</code></span></a> and have the user choose “Always Allow”.

2.  Check the <span class="pre">`remember`</span> flag on the returned dict: it is <span class="pre">`True`</span> only for a persistent key. Store the key together with <a href="#zotero.Zotero.server_id" class="reference internal" title="zotero.Zotero.server_id"><span class="pre"><code class="sourceCode python xref py py-attr docutils literal notranslate">Zotero.server_id</code></span></a>.

3.  On a later run, pass both back to the constructor.

<div class="highlight-python notranslate">

<div class="highlight">

    auth = zot.authorize_local('My Application')
    if auth['remember']:
        save_somewhere(zot.server_id, auth['key'])

    # on a later run
    zot = Zotero('0', 'user', local=True,
                 server_id=saved_server_id, local_api_key=saved_key)

</div>

</div>

</div>

<div id="how-to-recover-from-a-consumed-or-revoked-key" class="section">

### How to recover from a consumed or revoked key<a href="#how-to-recover-from-a-consumed-or-revoked-key" class="headerlink" title="Link to this heading"></a>

A single-use key is consumed by the first successful write, and the user can revoke a persistent key in Zotero’s settings. In both cases the next write raises <span class="pre">`LocalAPIKeyRequiredError`</span>. Catch it and re-authorise:

<div class="highlight-python notranslate">

<div class="highlight">

    from pyzotero import Zotero, LocalAPIKeyRequiredError

    try:
        zot.create_items([item])
    except LocalAPIKeyRequiredError:
        zot.authorize_local('My Application')
        zot.create_items([item])

</div>

</div>

</div>

<div id="how-to-add-a-file-attachment" class="section">

### How to add a file attachment<a href="#how-to-add-a-file-attachment" class="headerlink" title="Link to this heading"></a>

<a href="#zotero.Zotero.attachment_simple" class="reference internal" title="zotero.Zotero.attachment_simple"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.attachment_simple()</code></span></a> and <a href="#zotero.Zotero.attachment_both" class="reference internal" title="zotero.Zotero.attachment_both"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.attachment_both()</code></span></a> are unavailable in local mode (see <a href="#localapi-differences" class="reference internal"><span class="std std-ref">Differences from the web API</span></a>). Build the attachment dict yourself and pass it to <a href="#zotero.Zotero.upload_attachments" class="reference internal" title="zotero.Zotero.upload_attachments"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.upload_attachments()</code></span></a>, which works normally:

<div class="highlight-python notranslate">

<div class="highlight">

    attachment = {
        'itemType': 'attachment',
        'linkMode': 'imported_file',
        'title': 'paper.pdf',
        'filename': '/path/to/paper.pdf',
        'contentType': 'application/pdf',
        'charset': '',
        'note': '',
        'tags': [],
        'relations': {},
    }
    zot.upload_attachments([attachment], parent_item_key)

</div>

</div>

</div>

</div>

<div id="reference" class="section">

<span id="localapi-reference"></span>

## Reference<a href="#reference" class="headerlink" title="Link to this heading"></a>

> <div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">server_id</span></span><a href="#zotero.Zotero.server_id" class="headerlink" title="Link to this definition"></a>  
> The local API’s server ID, or <span class="pre">`None`</span> if it is not yet known. Readable and writable: a program can persist it alongside its own data and supply it on a later run via the <span class="pre">`server_id`</span> constructor argument. Pyzotero fetches it automatically before the first write if it is not already set.
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">authorize_local</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">app_name</span></span>*<span class="sig-paren">)</span><a href="#zotero.Zotero.authorize_local" class="headerlink" title="Link to this definition"></a>  
> Request a local API key. Zotero displays a dialog offering “Allow” (one-time access), “Always Allow” (persistent access) and “Deny”. On approval the key is stored on the instance as <span class="pre">`local_api_key`</span> and sent with subsequent local writes.
>
> Parameters<span class="colon">:</span>  
> **app_name** (*str*) – the caller’s display name, shown to the user in the dialog
>
> Return type<span class="colon">:</span>  
> dict containing a <span class="pre">`key`</span> string and a <span class="pre">`remember`</span> boolean
>
> <span class="pre">`remember`</span> is <span class="pre">`True`</span> only for a persistent key; a single-use key must be replaced by a further call once a write has consumed it.
>
> Raises <span class="pre">`LocalAPIDeniedError`</span> if the user denies the request. Zotero rate-limits this endpoint, so it must not be called in a retry loop.
>
> </div>

The exceptions specific to the local API — <span class="pre">`LocalAPIKeyRequiredError`</span>, <span class="pre">`LocalAPIDeniedError`</span>, <span class="pre">`ServerIDMismatchError`</span> and <span class="pre">`ServerIDRequiredError`</span> — are listed under <a href="#errors" class="reference internal">Errors</a>.

<div id="differences-from-the-web-api" class="section">

<span id="localapi-differences"></span>

### Differences from the web API<a href="#differences-from-the-web-api" class="headerlink" title="Link to this heading"></a>

- <a href="#zotero.Zotero.item_template" class="reference internal" title="zotero.Zotero.item_template"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.item_template()</code></span></a> is unavailable: the local API implements the item type and field endpoints, but not <span class="pre">`/items/new`</span>. Zotero may add it in future, in which case the method starts working with no change to Pyzotero. Build item dicts directly and pass them to <a href="#zotero.Zotero.create_items" class="reference internal" title="zotero.Zotero.create_items"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.create_items()</code></span></a>, using <a href="#zotero.Zotero.item_types" class="reference internal" title="zotero.Zotero.item_types"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.item_types()</code></span></a> and <a href="#zotero.Zotero.item_type_fields" class="reference internal" title="zotero.Zotero.item_type_fields"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.item_type_fields()</code></span></a> to discover the valid fields. Calling it in local mode raises <span class="pre">`CallDoesNotExistError`</span>.

- For the same reason <a href="#zotero.Zotero.attachment_simple" class="reference internal" title="zotero.Zotero.attachment_simple"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.attachment_simple()</code></span></a> and <a href="#zotero.Zotero.attachment_both" class="reference internal" title="zotero.Zotero.attachment_both"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.attachment_both()</code></span></a>, which build an attachment template internally, are unavailable. Use <a href="#zotero.Zotero.upload_attachments" class="reference internal" title="zotero.Zotero.upload_attachments"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.upload_attachments()</code></span></a> with a hand-built attachment dict instead: see <a href="#localapi-howto" class="reference internal"><span class="std std-ref">How-to guides</span></a>.

- Keyed writes require a concurrency precondition: either a <span class="pre">`version`</span> on each object, which objects retrieved from the API already carry, or an explicit <span class="pre">`last_modified`</span> argument. Payloads built by hand without either are rejected.

- Item type and field endpoints return names in the user’s locale; the <span class="pre">`locale`</span> parameter is ignored. <a href="#zotero.Zotero.creator_fields" class="reference internal" title="zotero.Zotero.creator_fields"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.creator_fields()</code></span></a> always returns English.

- Atom is not supported, and there are no rate limits on ordinary requests.

- Results are not paginated by default, so <a href="#zotero.Zotero.everything" class="reference internal" title="zotero.Zotero.everything"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.everything()</code></span></a> is rarely needed.

- Requests go to <span class="pre">`127.0.0.1`</span>, not <span class="pre">`localhost`</span>: Zotero listens on the IPv4 loopback address only. The default client ignores proxy settings from the environment (<span class="pre">`HTTP_PROXY`</span>, <span class="pre">`ALL_PROXY`</span> and the system proxy configuration).

For the full list, see the <a href="https://github.com/zotero/zotero/blob/main/chrome/content/zotero/xpcom/server/server_localAPI.js" class="reference external">local API documentation</a>.

</div>

</div>

</div>

<div id="write-api-methods" class="section">

<span id="write"></span>

# Write API Methods<a href="#write-api-methods" class="headerlink" title="Link to this heading"></a>

<div id="saved-searches" class="section">

## Saved Searches<a href="#saved-searches" class="headerlink" title="Link to this heading"></a>

Pyzotero allows you to retrieve, delete, or modify saved searches:

> <div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">searches</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#zotero.Zotero.searches" class="headerlink" title="Link to this definition"></a>  
> Retrieve all saved searches. Note that this retrieves saved search *metadata*, as opposed to *content*; saved searches cannot currently (January 2019) be run using the API.
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">saved_search</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">name</span></span>*, *<span class="n"><span class="pre">conditions</span></span>*<span class="sig-paren">)</span><a href="#zotero.Zotero.saved_search" class="headerlink" title="Link to this definition"></a>  
> Create a new saved search. conditions is a list of one or more dicts, each of which must contain the following three string keys: condition, operator, value. See the <a href="https://www.zotero.org/support/dev/web_api/v3/write_requests#saved_search_requests" class="reference external">documentation</a> for an example.
>
> Parameters<span class="colon">:</span>  
> - **name** (*str*) – the name of the search
>
> - **conditions** (*list*) – one or more dicts containing search conditions and operators
>
> Return type<span class="colon">:</span>  
> dict showing creation success status
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">delete_saved_search</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">search_keys</span></span>*<span class="sig-paren">)</span><a href="#zotero.Zotero.delete_saved_search" class="headerlink" title="Link to this definition"></a>  
> Delete one or more saved searches. search_keys is a list of one or more search keys. These can be retrievd using <a href="#zotero.Zotero.searches" class="reference internal" title="zotero.Zotero.searches"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.searches()</code></span></a>
>
> Parameters<span class="colon">:</span>  
> **search_keys** (*list*) – list of unique saved search keys
>
> Return type<span class="colon">:</span>  
> None
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">show_operators</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#zotero.Zotero.show_operators" class="headerlink" title="Link to this definition"></a>  
> Show available saved search operators
>
> Return type<span class="colon">:</span>  
> list
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">show_conditions</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#zotero.Zotero.show_conditions" class="headerlink" title="Link to this definition"></a>  
> Show available saved search conditions
>
> Return type<span class="colon">:</span>  
> list
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">show_condition_operators</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">condition</span></span>*<span class="sig-paren">)</span><a href="#zotero.Zotero.show_condition_operators" class="headerlink" title="Link to this definition"></a>  
> Show available operators for a given saved search condition
>
> Parameters<span class="colon">:</span>  
> **condition** (*str*) – a valid saved search condition
>
> Return type<span class="colon">:</span>  
> list
>
> </div>

</div>

<div id="item-methods" class="section">

## Item Methods<a href="#item-methods" class="headerlink" title="Link to this heading"></a>

> <div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">item_types</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#zotero.Zotero.item_types" class="headerlink" title="Link to this definition"></a>  
> Returns a dict containing all available item types
>
> Return type<span class="colon">:</span>  
> dict
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">item_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#zotero.Zotero.item_fields" class="headerlink" title="Link to this definition"></a>  
> Returns a dict of all available item fields
>
> Return type<span class="colon">:</span>  
> dict
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">item_creator_types</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">itemtype</span></span>*<span class="sig-paren">)</span><a href="#zotero.Zotero.item_creator_types" class="headerlink" title="Link to this definition"></a>  
> Returns a dict of all valid creator types for the specified item type
>
> Parameters<span class="colon">:</span>  
> **itemtype** (*str*) – a valid Zotero item type. A list of available item types can be obtained by the use of <a href="#zotero.Zotero.item_types" class="reference internal" title="zotero.Zotero.item_types"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">item_types()</code></span></a>
>
> Return type<span class="colon">:</span>  
> dict
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">creator_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#zotero.Zotero.creator_fields" class="headerlink" title="Link to this definition"></a>  
> Returns a dict containing all localised creator fields
>
> Return type<span class="colon">:</span>  
> dict
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">item_type_fields</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">itemtype</span></span>*<span class="sig-paren">)</span><a href="#zotero.Zotero.item_type_fields" class="headerlink" title="Link to this definition"></a>  
> Returns all valid fields for the specified item type
>
> Parameters<span class="colon">:</span>  
> **itemtype** (*str*) – a valid Zotero item type. A list of available item types can be obtained by the use of <a href="#zotero.Zotero.item_types" class="reference internal" title="zotero.Zotero.item_types"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">item_types()</code></span></a>
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">item_template</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">itemtype</span></span>*, *<span class="n"><span class="pre">linkmode</span></span>*<span class="sig-paren">)</span><a href="#zotero.Zotero.item_template" class="headerlink" title="Link to this definition"></a>  
> Returns an item creation template for the specified item type
>
> Parameters<span class="colon">:</span>  
> - **itemtype** (*str*) – a valid Zotero item type. A list of available item types can be obtained by the use of <a href="#zotero.Zotero.item_types" class="reference internal" title="zotero.Zotero.item_types"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">item_types()</code></span></a>
>
> - **linkmode** (*str*) – either None (default) or a valid Zotero linkMode value required when itemtype is attachment. A list of available link modes can be obtained by the use of <span class="pre">`item_attachment_link_modes()`</span>
>
> Return type<span class="colon">:</span>  
> dict
>
> </div>

<div id="creating-and-updating-items" class="section">

### Creating and Updating Items<a href="#creating-and-updating-items" class="headerlink" title="Link to this heading"></a>

> <div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">create_items</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">items</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">parentid</span></span>*, *<span class="n"><span class="pre">last_modified</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.create_items" class="headerlink" title="Link to this definition"></a>  
> Create Zotero library items
>
> Parameters<span class="colon">:</span>  
> - **items** (*list*) – one or more dicts containing item data
>
> - **parentid** (*str*) – A Parent item ID. This will cause the item(s) to become the child items of the given parent ID
>
> - **last_modified** (*str/int*) – If not None will set the value of the If-Unmodified-Since-Version header.
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> Returns a copy of the created item(s), if successful. Use of <a href="#zotero.Zotero.item_template" class="reference internal" title="zotero.Zotero.item_template"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">item_template()</code></span></a> is recommended in order to first obtain a dict with a structure which is known to be valid.
>
> Before calling this method, the use of <a href="#zotero.Zotero.check_items" class="reference internal" title="zotero.Zotero.check_items"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">check_items()</code></span></a> is encouraged, in order to confirm that the item to be created contains only valid fields.
>
> Note that if any items contain a key field matching an existing item on the server it will be updated (any properties not in the dict will be left unmodified).
>
> </div>

Example:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     template = zot.item_template('book')
>     template['creators'][0]['firstName'] = 'Monty'
>     template['creators'][0]['lastName'] = 'Cantsin'
>     template['title'] = 'Maris Kundzins: A Life'
>     resp = zot.create_items([template])
>
> </div>
>
> </div>
>
> </div>

If successful, <span class="pre">`resp`</span> will be a dict containing the creation status of each item:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     {'failed': {}, 'success': {'0': 'ABC123'}, 'unchanged': {}}
>
> </div>
>
> </div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">update_item</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">item</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">last_modified</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.update_item" class="headerlink" title="Link to this definition"></a>  
> Update an item in your library
>
> Parameters<span class="colon">:</span>  
> - **item** (*dict*) – a dict containing item data. Fields not in item will be left unmodified.
>
> - **last_modified** (*str/int*) – If not <span class="pre">`None`</span>, will set the value of the If-Unmodified-Since-Version header. If unspecified/None then If-Unmodified-Since-Version will be set to the version property of item.
>
> Return type<span class="colon">:</span>  
> Boolean
>
> Will return <span class="pre">`True`</span> if the request was successful, or will raise an error.
>
> </div>

Example:

> <div>
>
> > <div>
> >
> > <div class="highlight-python notranslate">
> >
> > <div class="highlight">
> >
> >     i = zot.items()
> >     # see above for example of returned item structure
> >     # modify the latest item which was added to your library
> >     i[0]['data']['title'] = 'The Sheltering Sky'
> >     i[0]['data']['creators'][0]['firstName'] = 'Paul'
> >     i[0]['data']['creators'][0]['lastName'] = 'Bowles'
> >     zot.update_item(i[0])
> >
> > </div>
> >
> > </div>
> >
> > </div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">update_items</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">items</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">last_modified</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.update_items" class="headerlink" title="Link to this definition"></a>  
> Update items in your library. The API only accepts 50 items per call, so longer updates are chunked
>
> Parameters<span class="colon">:</span>  
> - **items** (*list*) – a list of dicts containing Item data. Fields not in item will be left unmodified.
>
> - **last_modified** (*int*) – optional library version, sent as <span class="pre">`If-Unmodified-Since-Version`</span>. Only needed when the dicts carry no <span class="pre">`version`</span> of their own; the local API rejects keyed writes that have neither.
>
> Return type<span class="colon">:</span>  
> Boolean
>
> Will return <span class="pre">`True`</span> if the request was successful, or will raise an error.
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">check_items</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">items</span></span>*<span class="sig-paren">)</span><a href="#zotero.Zotero.check_items" class="headerlink" title="Link to this definition"></a>  
> Check whether items to be created on the server contain only valid keys. This method first creates a set of valid keys by calling <a href="#zotero.Zotero.item_fields" class="reference internal" title="zotero.Zotero.item_fields"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">item_fields()</code></span></a>, then compares the user-created dicts to it. If any keys in the user-created dicts are unknown, a <span class="pre">`InvalidItemFields`</span> exception is raised, detailing the invalid fields.
>
> <span class="pre">`deleted`</span> is a valid key: the API returns it on trashed objects, and accepts it on write.
>
> Parameters<span class="colon">:</span>  
> **items** (*list*) – one or more dicts containing item data
>
> Return type<span class="colon">:</span>  
> List. Each list item is a valid dict containing item data.
>
> </div>

</div>

<div id="uploading-files" class="section">

### Uploading files<a href="#uploading-files" class="headerlink" title="Link to this heading"></a>

> <div>
>
> <div class="admonition warning">
>
> Warning
>
> Attachment methods are in beta.
>
> </div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">attachment_simple</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">files</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">parentid</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.attachment_simple" class="headerlink" title="Link to this definition"></a>  
> Create one or more file attachment items.
>
> Parameters<span class="colon">:</span>  
> - **files** (*list*) – a list containing one or more file paths: <span class="pre">`['/path/to/file/file.pdf',`</span>` `<span class="pre">`…`</span>` `<span class="pre">`]`</span>
>
> - **parentid** (*string*) – a library Item ID. If this is specified, attachments will be created as child items of this ID.
>
> Return type<span class="colon">:</span>  
> Dict. Showing status of each requested upload.
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">attachment_both</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">files</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">parentid</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.attachment_both" class="headerlink" title="Link to this definition"></a>  
> Create one or more file attachment items, specifying names for uploaded files
>
> Parameters<span class="colon">:</span>  
> - **files** (*list*) – a list containing one or more lists or tuples in the following format: <span class="pre">`(file`</span>` `<span class="pre">`name,`</span>` `<span class="pre">`file`</span>` `<span class="pre">`path)`</span>
>
> - **parentid** (*string*) – a library Item ID. If this is specified, attachments will be created as child items of this ID.
>
> Return type<span class="colon">:</span>  
> Dict. Showing status of each requested upload.
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">upload_attachments</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attachments</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">parentid</span></span>*, *<span class="n"><span class="pre">basedir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.upload_attachments" class="headerlink" title="Link to this definition"></a>  
> Upload files to their corresponding attachments. If the attachments lack the <span class="pre">`key`</span> property they are assumed not to exist and will be created. The <span class="pre">`parentid`</span> parameter is **not compatible** with existing attachments. In order for uploads to succeed, the filename parameter of each attachment must resolve.
>
> This method is really only required in cases where a sync has been interrupted, leaving your library with attachment items that don’t have corresponding files attached. It *may* also work for uploading modified files, though **this is untested**.
>
> Parameters<span class="colon">:</span>  
> - **attachments** (*list*) – A list of dicts representing zotero imported files which may or may not already have their key fields filled in.
>
> - **parentid** (*string*) – a library Item ID. If this is specified and key fields are not included, attachments will be created as child items of this ID.
>
> - **basedir** (*string/path*) – A string or path object to which the filenames specified in attachments will be evaluated relative to. If unspecified the filenames are evaluated as they are.
>
> Return type<span class="colon">:</span>  
> Dict. Showing status of each requested upload.
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     # example of the return type
>     {
>         'success': [attach1, attach2...],
>         'failure': [attach3, attach4...],
>         'unchanged': [attach4, attach5...]
>     }
>
> </div>
>
> </div>
>
> <div class="admonition note">
>
> Note
>
> unlike the space-saving responses from the server, the return value here eschews the complex index / key lookup and simply passes back the <span class="pre">`imported_file`</span> item template populated with keys (if created successfully or passed in) corresponding to each result. This is the return type for all of these methods. Entries additionally carry the item’s current <span class="pre">`version`</span> (as reported by the server after the item’s final write step), so a follow-up <a href="#zotero.Zotero.update_item" class="reference internal" title="zotero.Zotero.update_item"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.update_item()</code></span></a> call can be made without refetching the item first.
>
> </div>
>
> <div class="admonition note">
>
> Note
>
> the <span class="pre">`filename`</span> you pass is used to locate the file on disk (relative to <span class="pre">`basedir`</span>, if given), so it may be a path. The API doesn’t accept a directory path in a stored-file item’s <span class="pre">`filename`</span> field, so only the basename is sent when the attachment item is created. Entries returned under <span class="pre">`failure`</span> because the server rejected the item at creation time contain the server’s reason under an <span class="pre">`error`</span> key, e.g. <span class="pre">`{'code':`</span>` `<span class="pre">`400,`</span>` `<span class="pre">`'message':`</span>` `<span class="pre">`'…'}`</span>.
>
> </div>
>
> </div>

</div>

<div id="deleting-items" class="section">

### Deleting items<a href="#deleting-items" class="headerlink" title="Link to this heading"></a>

> <div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">delete_item</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">item</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">last_modified</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.delete_item" class="headerlink" title="Link to this definition"></a>  
> Delete one or more items from your library
>
> Parameters<span class="colon">:</span>  
> - **item** (*list*) – a list of one or more dicts containing item data. You must first retrieve the item(s) you wish to delete, as <span class="pre">`version`</span> data is required.
>
> - **last_modified** (*str/int*) – If not <span class="pre">`None`</span>, will set the value of the If-Unmodified-Since-Version header.
>
> <div class="admonition note">
>
> Note
>
> <span class="pre">`delete_item()`</span> is permanent. To move an item to the trash instead, set <span class="pre">`deleted`</span> to <span class="pre">`1`</span> on it and pass it to <span class="pre">`update_item()`</span>. Setting <span class="pre">`deleted`</span> to <span class="pre">`0`</span> restores it.
>
> </div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     item = zot.item('ABC123')
>     item['data']['deleted'] = 1
>     zot.update_item(item['data'])
>
> </div>
>
> </div>
>
> </div>

</div>

<div id="deleting-tags" class="section">

### Deleting tags<a href="#deleting-tags" class="headerlink" title="Link to this heading"></a>

> <div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">delete_tags</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">tag_a</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">tag</span> <span class="pre">…</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.delete_tags" class="headerlink" title="Link to this definition"></a>  
> Delete one or more tags from your library
>
> Parameters<span class="colon">:</span>  
> **tag** (*string*) – the tag(s) you’d like to delete
>
> You may also pass a list using <span class="pre">`zot.delete_tags(*[tag_list])`</span>
>
> </div>

</div>

</div>

<div id="adding-tags" class="section">

## Adding tags<a href="#adding-tags" class="headerlink" title="Link to this heading"></a>

> <div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">add_tags</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">item</span></span>*, *<span class="n"><span class="pre">tag</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">tag</span> <span class="pre">…</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.add_tags" class="headerlink" title="Link to this definition"></a>  
> Add one or more tags to an item, and update it on the server
>
> Parameters<span class="colon">:</span>  
> - **item** (*dict*) – a dict containing item data
>
> - **tag** (*string*) – the tag(s) you’d like to add to the item
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> You may also pass a list using <span class="pre">`zot.add_tags(item,`</span>` `<span class="pre">`*[tag_list])`</span>
>
> </div>

Example:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     z = zot.top(limit=1)
>     # we've now retrieved the most recent top-level item
>     updated = zot.add_tags(z[0], 'tag1', 'tag2', 'tag3')
>     # updated now contains a representation of the updated server item
>
> </div>
>
> </div>
>
> </div>

</div>

<div id="collection-methods" class="section">

## Collection Methods<a href="#collection-methods" class="headerlink" title="Link to this heading"></a>

> <div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">create_collections</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dicts</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">last_modified</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.create_collections" class="headerlink" title="Link to this definition"></a>  
> Create a new collection in the Zotero library
>
> Parameters<span class="colon">:</span>  
> - **dicts** (*list*) – list of dicts each containing the key <span class="pre">`name`</span>, with each value being a new collection name you wish to create. Each dict may optionally contain a <span class="pre">`parentCollection`</span> key, the value of which is the ID of an existing collection. If this is set, the collection will be created as a child of that collection.
>
> - **last_modified** (*str/int*) – If not None will set the value of the If-Unmodified-Since-Version header.
>
> Return type<span class="colon">:</span>  
> list of dicts
>
> Return type<span class="colon">:</span>  
> Boolean
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">create_collection</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">dicts</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">last_modified</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.create_collection" class="headerlink" title="Link to this definition"></a>  
> Alias for <a href="#zotero.Zotero.create_collections" class="reference internal" title="zotero.Zotero.create_collections"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">Zotero.create_collections()</code></span></a> to preserve backward compatibility
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">addto_collection</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">collection</span></span>*, *<span class="n"><span class="pre">item</span></span>*<span class="sig-paren">)</span><a href="#zotero.Zotero.addto_collection" class="headerlink" title="Link to this definition"></a>  
> Add the specified item(s) to the specified collection
>
> Parameters<span class="colon">:</span>  
> - **collection** (*str*) – a collection key
>
> - **item** (*dict*) – an item dict retrieved using an API call
>
> Return type<span class="colon">:</span>  
> Boolean
>
> Collection keys can be obtained by a call to <a href="#zotero.Zotero.collections" class="reference internal" title="zotero.Zotero.collections"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">collections()</code></span></a> (see details above).
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">deletefrom_collection</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">collection</span></span>*, *<span class="n"><span class="pre">item</span></span>*<span class="sig-paren">)</span><a href="#zotero.Zotero.deletefrom_collection" class="headerlink" title="Link to this definition"></a>  
> Remove the specified item from the specified collection
>
> Parameters<span class="colon">:</span>  
> - **collection** (*str*) – a collection key
>
> - **item** (*dict*) – a dict containing item data
>
> Return type<span class="colon">:</span>  
> Boolean
>
> See the <a href="#zotero.Zotero.delete_item" class="reference internal" title="zotero.Zotero.delete_item"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">delete_item()</code></span></a> example for multiple-item removal.
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">moveto_collection</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">from_collection</span></span>*, *<span class="n"><span class="pre">to_collection</span></span>*, *<span class="n"><span class="pre">item</span></span>*<span class="sig-paren">)</span><a href="#zotero.Zotero.moveto_collection" class="headerlink" title="Link to this definition"></a>  
> Move the specified item from one collection to another, in a single request
>
> Parameters<span class="colon">:</span>  
> - **from_collection** (*str*) – the key of the collection to remove the item from
>
> - **to_collection** (*str*) – the key of the collection to add the item to
>
> - **item** (*dict*) – an item dict retrieved using an API call
>
> Return type<span class="colon">:</span>  
> Boolean
>
> The item’s membership of other collections is unchanged. If the item is not in <span class="pre">`from_collection`</span>, it is still added to <span class="pre">`to_collection`</span>. Calling <a href="#zotero.Zotero.deletefrom_collection" class="reference internal" title="zotero.Zotero.deletefrom_collection"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">deletefrom_collection()</code></span></a> followed by <a href="#zotero.Zotero.addto_collection" class="reference internal" title="zotero.Zotero.addto_collection"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">addto_collection()</code></span></a> does not work for this: the first call changes the item’s version, so the second call fails its version check.
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     item = zot.item("ITEMKEY")
>     zot.moveto_collection("OLDCOLL", "NEWCOLL", item)
>
> </div>
>
> </div>
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">update_collection</span></span><span class="sig-paren">(</span>*<span class="pre">collection</span> <span class="pre">,</span> <span class="pre">last_modified\]</span>*<span class="sig-paren">)</span><a href="#zotero.Zotero.update_collection" class="headerlink" title="Link to this definition"></a>  
> Update existing collection metadata (name etc.)
>
> Parameters<span class="colon">:</span>  
> **collection** (*dict*) – a dict containing collection data, previously retrieved using one of the Collections calls (e.g. <a href="#zotero.Zotero.collections" class="reference internal" title="zotero.Zotero.collections"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">collections()</code></span></a>)
>
> Return type<span class="colon">:</span>  
> Boolean
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">update_collections</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">collection_items</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">last_modified</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.update_collections" class="headerlink" title="Link to this definition"></a>  
> Update multiple existing collection metadata. The API only accepts 50 collections per call, so longer updates are chunked
>
> Parameters<span class="colon">:</span>  
> - **collection_items** (*list*) – a list of dicts containing Collection data. Fields not in collection_item will be left unmodified.
>
> - **last_modified** (*int*) – optional library version, sent as <span class="pre">`If-Unmodified-Since-Version`</span>. Only needed when the dicts carry no <span class="pre">`version`</span> of their own; the local API rejects keyed writes that have neither.
>
> Return type<span class="colon">:</span>  
> Boolean
>
> Will return <span class="pre">`True`</span> if the request was successful, or will raise an error.
>
> <!-- -->
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">collection_tags</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">collectionID</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">search/request</span> <span class="pre">parameters</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.collection_tags" class="headerlink" title="Link to this definition"></a>  
> Retrieve all tags for a given collection
>
> Parameters<span class="colon">:</span>  
> **collectionID** (*str*) – a collection ID
>
> Return type<span class="colon">:</span>  
> list of strings
>
> </div>

Examples:

> <div>
>
> <div class="highlight-python notranslate">
>
> <div class="highlight">
>
>     # get existing collections, which will return a list of dicts
>     c = zot.collections()
>     # rename the last collection created in the library
>     c[0]['name'] = 'Whither Digital Humanities?'
>     # update collection name on the server
>     zot.update_collection(c[0])
>
> </div>
>
> </div>
>
> <span class="sig-prename descclassname"><span class="pre">Zotero.</span></span><span class="sig-name descname"><span class="pre">delete_collection</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">collection</span></span>*<span class="optional">\[</span>, *<span class="n"><span class="pre">last_modified</span></span>*<span class="optional">\]</span><span class="sig-paren">)</span><a href="#zotero.Zotero.delete_collection" class="headerlink" title="Link to this definition"></a>  
> Delete a collection from the Zotero library
>
> Parameters<span class="colon">:</span>  
> - **collection** (*dict*) – a dict containing collection data, previously retrieved using one of the Collections calls (e.g. <a href="#zotero.Zotero.collections" class="reference internal" title="zotero.Zotero.collections"><span class="pre"><code class="sourceCode python xref py py-meth docutils literal notranslate">collections()</code></span></a>). Alternatively, you may pass a **list** of collection dicts.
>
> - **last_modified** (*str/int*) – If not None will set the value of the If-Unmodified-Since-Version header.
>
> Return type<span class="colon">:</span>  
> Boolean
>
> </div>

</div>

</div>

<div id="notes" class="section">

# Notes<a href="#notes" class="headerlink" title="Link to this heading"></a>

Most Read API methods return **lists** of **dicts** or, in the case of tag methods, **lists** of **strings**. Most Write API methods return either <span class="pre">`True`</span> if successful, or raise an error. See <span class="pre">`zotero_errors.py`</span> for a full listing of these.

<div class="admonition warning">

Warning

URL parameters will supersede API calls which should return e.g. a single item: <span class="pre">`https://api.zotero.org/users/${LIBRARY_ID}/items/ABC?start=50&limit=10`</span> will return 10 items beginning at position 50, even though <span class="pre">`ABC`</span> does not exist. Be aware of this, and don’t pass URL parameters which do not apply to a given API method.

</div>

</div>

<div id="license" class="section">

# License<a href="#license" class="headerlink" title="Link to this heading"></a>

Pyzotero is licensed under the <a href="https://opensource.org/license/blue-oak-model-license" class="reference external">Blue Oak Model Licence</a> license.

</div>

<div id="cat-picture" class="section">

# Cat Picture<a href="#cat-picture" class="headerlink" title="Link to this heading"></a>

This is The Grinch.

<figure id="id11" class="align-default">
<img src="_images/cat.png" alt="_images/cat.png" />
<figcaption><p><span class="caption-text"><em>Orangecat</em></span><a href="#id11" class="headerlink" title="Link to this image"></a></p></figcaption>
</figure>

<div class="aside footnote-list brackets">

<div id="id10" class="aside footnote brackets" role="doc-footnote">

<span class="label"><span class="fn-bracket">\[</span><a href="#id1" role="doc-backlink">*</a><span class="fn-bracket">\]</span></span>

This isn’t strictly true: you only need an API key for personal libraries and non-public group libraries.

</div>

</div>

</div>

</div>

</div>

[^1]:
