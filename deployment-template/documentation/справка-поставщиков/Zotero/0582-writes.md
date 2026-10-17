> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Zotero: writes

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


<div class="zotero-docs-page">

<style>
  @font-face {
    font-family: 'Inter';
    font-weight: 400;
    font-display: swap;
    src: url('/support/_fonts/inter/Inter-Regular.woff2') format('woff2');
  }
  @font-face {
    font-family: 'Inter';
    font-weight: 500;
    font-display: swap;
    src: url('/support/_fonts/inter/Inter-Medium.woff2') format('woff2');
  }
  @font-face {
    font-family: 'Inter';
    font-weight: 600;
    font-display: swap;
    src: url('/support/_fonts/inter/Inter-SemiBold.woff2') format('woff2');
  }
  @font-face {
    font-family: 'Inter';
    font-weight: 700;
    font-display: swap;
    src: url('/support/_fonts/inter/Inter-Bold.woff2') format('woff2');
  }

  .zotero-docs {
    display: grid;
    grid-template-columns: 220px minmax(0, 720px) 200px;
    justify-content: center;
    gap: 2.5em;
    margin: 1.5em auto;
    padding: 0 1em;
    max-width: 1320px;
    box-sizing: border-box;
    font-family: Inter, sans-serif;
    font-size: 15px;
    line-height: 1.75;
    color: #222;
  }
  @media (max-width: 1240px) {
    .zotero-docs {
      grid-template-columns: 220px minmax(0, 1fr) 200px;
    }
  }
  @media (max-width: 1100px) {
    .zotero-docs {
      grid-template-columns: 220px minmax(0, 1fr);
    }
    .zotero-docs-toc { display: none; }
  }
  @media (max-width: 800px) {
    .zotero-docs {
      grid-template-columns: 1fr;
    }
  }

  /* ----- Content ----- */
  .zotero-docs-content {
    min-width: 0;
  }
  .zotero-docs-content h1,
  .zotero-docs-content h2,
  .zotero-docs-content h3,
  .zotero-docs-content h4,
  .zotero-docs-content h5,
  .zotero-docs-content h6 {
    font-family: inherit;
    font-weight: bold;
    margin: 0 0 0.6em;
    line-height: 1.3;
    clear: left;
  }
  .zotero-docs-content h1,
  .zotero-docs-content h2 { padding-top: 1.4em; }
  .zotero-docs-content h3,
  .zotero-docs-content h4 { padding-top: 0.8em; }
  .zotero-docs-content h5,
  .zotero-docs-content h6 { padding-top: 0.4em; }
  .zotero-docs-content > h1:first-child { padding-top: 0; }
  .zotero-docs-content :is(h1,h2,h3,h4,h5,h6) + :is(h1,h2,h3,h4,h5,h6) {
    padding-top: 0.5em;
  }
  .zotero-docs-content h1 {
    font-size: 200%;
    border-bottom: 1px solid #ddd;
    padding-bottom: 0.2em;
  }
  .zotero-docs-content h2 {
    font-size: 155%;
    border-bottom: 1px solid #eee;
    padding-bottom: 0.15em;
  }
  .zotero-docs-content h3 { font-size: 125%; }
  .zotero-docs-content h4 { font-size: 110%; }
  .zotero-docs-content h5 { font-size: 100%; color: #555; }
  .zotero-docs-content h6 {
    font-size: 88%; color: #555;
    text-transform: uppercase; letter-spacing: 0.04em;
  }
  .zotero-docs-content p,
  .zotero-docs-content ul,
  .zotero-docs-content ol {
    margin: 0 0 1.3em;
  }
  /* Default list items get minimal spacing; this covers both tight lists and
     loose lists whose items happen to be a single short paragraph. */
  .zotero-docs-content li { margin: 0.25em 0; }
  /* Genuinely multi-block items (e.g., a paragraph followed by another
     paragraph or a nested list) get more breathing room. */
  .zotero-docs-content li:has(> p + *) { margin: 0.7em 0; }
  .zotero-docs-content li > ul,
  .zotero-docs-content li > ol { margin: 0.2em 0 0.4em; }
  .zotero-docs-content code,
  .zotero-docs-content pre {
    font-family: Consolas, "Liberation Mono", Courier, monospace;
    font-size: 100%;
  }
  .zotero-docs-content code {
    background: #f0f4f8;
    color: inherit;
    padding: 0.1em 0.35em;
    border: 1px solid #dde2e8;
    border-radius: 3px;
  }
  .zotero-docs-content table code {
    background: none;
    border: none;
    padding: 0;
  }
  /* Multi-line inline code (from flattened Dokuwiki `<code>` blocks inside
     table cells) preserves newlines via `
` entities. */
  .zotero-docs-content code.multiline {
    display: block;
    white-space: pre;
    margin: 0.3em 0;
    padding: 0.5em 0.7em;
    background: #f0f4f8;
    border: 1px solid #dde2e8;
    border-radius: 3px;
    font-size: 100%;
  }
  .zotero-docs-content pre {
    background: #f6f8fa;
    padding: 0.8em 1em;
    border: 1px solid #dde2e8;
    border-radius: 4px;
    overflow-x: auto;
  }
  /* Syntax highlighting (Pygments "vs" theme) */
  .zotero-docs-content .codehilite { background: transparent; }
  .zotero-docs-content .codehilite .hll { background-color: #ffc; }
  .zotero-docs-content .codehilite .c,
  .zotero-docs-content .codehilite .ch,
  .zotero-docs-content .codehilite .cm,
  .zotero-docs-content .codehilite .cpf,
  .zotero-docs-content .codehilite .c1,
  .zotero-docs-content .codehilite .cs { color: #008000; }
  .zotero-docs-content .codehilite .k,
  .zotero-docs-content .codehilite .kc,
  .zotero-docs-content .codehilite .kd,
  .zotero-docs-content .codehilite .kn,
  .zotero-docs-content .codehilite .kp,
  .zotero-docs-content .codehilite .kr,
  .zotero-docs-content .codehilite .cp,
  .zotero-docs-content .codehilite .ow { color: #00F; }
  .zotero-docs-content .codehilite .kt,
  .zotero-docs-content .codehilite .nc { color: #2B91AF; }
  .zotero-docs-content .codehilite .s,
  .zotero-docs-content .codehilite .sa,
  .zotero-docs-content .codehilite .sb,
  .zotero-docs-content .codehilite .sc,
  .zotero-docs-content .codehilite .dl,
  .zotero-docs-content .codehilite .sd,
  .zotero-docs-content .codehilite .s2,
  .zotero-docs-content .codehilite .se,
  .zotero-docs-content .codehilite .sh,
  .zotero-docs-content .codehilite .si,
  .zotero-docs-content .codehilite .sx,
  .zotero-docs-content .codehilite .sr,
  .zotero-docs-content .codehilite .s1,
  .zotero-docs-content .codehilite .ss { color: #A31515; }
  .zotero-docs-content pre code {
    background: none;
    border: none;
    padding: 0;
    border-radius: 0;
  }
  .zotero-docs-content table {
    border-collapse: collapse;
    margin: 0 0 1.1em;
    font-size: 95%;
    width: 100%;
  }
  .zotero-docs-content table th,
  .zotero-docs-content table td {
    border: 1px solid #ddd;
    padding: 0.45em 0.7em;
    text-align: left;
    vertical-align: top;
  }
  .zotero-docs-content table th {
    background: #f3f3f3;
    font-weight: 600;
  }
  .zotero-docs-content table tr:nth-child(2n) td {
    background: #fafafa;
  }
  .zotero-docs-content img {
    max-width: 100%;
    height: auto;
  }
  .zotero-docs-content img.align-left {
    float: left; margin: 0 1em 0.5em 0;
  }
  .zotero-docs-content img.align-right {
    float: right; margin: 0 0 0.5em 1em;
  }
  .zotero-docs-content img.align-center {
    display: block; margin: 0.5em auto;
  }
  .zotero-docs-content a {
    text-decoration: underline;
    text-decoration-color: rgba(0, 102, 204, 0.4);
    text-underline-offset: 2px;
    transition: text-decoration-color 0.15s;
  }
  .zotero-docs-content a:hover {
    text-decoration-color: currentColor;
  }
  .zotero-docs-content a.missing-link {
    color: #006;
    text-decoration-style: dashed;
  }
  .zotero-docs-content a[href^="http"]:not([href*=".zotero.org"]):not([href*="//zotero.org"])::after {
    content: "";
    display: inline-block;
    width: 0.85em;
    height: 0.85em;
    margin-left: 0.25em;
    vertical-align: -1px;
    background-color: currentColor;
    opacity: 0.8;
    -webkit-mask-image: url("data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 24 24" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>");
    mask-image: url("data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 24 24" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>");
    -webkit-mask-repeat: no-repeat;
    mask-repeat: no-repeat;
    -webkit-mask-size: contain;
    mask-size: contain;
  }
  .zotero-docs-content .headerlink {
    color: #aaa; text-decoration: none; margin-left: 0.25em;
    opacity: 0; transition: opacity 0.15s, color 0.15s;
  }
  .zotero-docs-content :hover > .headerlink,
  .zotero-docs-content .headerlink:focus { opacity: 1; }
  .zotero-docs-content .headerlink:hover { color: #555; }
  /* The top-level page heading already serves as the page title; suppress
     its permalink # — there's nothing useful to link to. */
  .zotero-docs-content > :is(h1, h2):first-child .headerlink {
    display: none;
  }

  /* ----- Left sidebar (global nav) ----- */
  .zotero-docs-nav {
    font-size: 0.9em;
    line-height: 1.45;
    position: sticky;
    top: 1em;
    max-height: calc(100vh - 2em);
    display: flex;
    flex-direction: column;
  }
  /* Search box stays fixed at the top of the sidebar; the nav list scrolls
     within its own space. The search dropdown can overflow the nav freely
     because the nav container itself doesn't clip. */
  .zotero-docs-nav > ul {
    overflow-y: auto;
    flex: 1 1 auto;
    min-height: 0;
  }
  /* At narrow widths (e.g. high zoom), collapse the sidebar into normal
     page flow above the content: drop sticky positioning, the flex layout,
     and the inner ul's scrollbox. Must come AFTER the default nav rules so
     it wins on source order. DOM order is nav → article → aside, so it
     naturally lands above the content. */
  @media (max-width: 800px) {
    .zotero-docs-nav {
      position: static;
      max-height: none;
      overflow: visible;
      display: block;
      padding-bottom: 1em;
      border-bottom: 1px solid #ddd;
      margin-bottom: 1.5em;
    }
    .zotero-docs-nav > ul {
      overflow: visible;
      flex: none;
    }
  }
  .zotero-docs-search {
    position: relative;
    margin-bottom: 1em;
  }
  .zotero-docs-search input {
    width: 100%;
    padding: 0.45em 0.7em;
    font: inherit;
    font-size: 0.95em;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
  }
  .zotero-docs-search input:focus {
    outline: none;
    border-color: #1a3a6e;
  }
  .zotero-docs-search-results {
    position: absolute;
    top: calc(100% + 4px);
    left: 0;
    right: 0;
    background: #fff;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    max-height: 60vh;
    overflow-y: auto;
    z-index: 100;
    display: none;
  }
  .zotero-docs-search-results.open { display: block; }
  .zotero-docs-search-results article {
    display: block;
    padding: 0.5em 0.7em;
    margin: 0;
    border-bottom: 1px solid #f0f0f0;
  }
  .zotero-docs-search-results article:last-child { border-bottom: none; }
  .zotero-docs-search-results h3 {
    display: block;
    margin: 0 0 0.15em;
    padding: 0;
    font-size: 0.95em;
    font-weight: 600;
  }
  .zotero-docs-search-results h3 a {
    display: inline;
    padding: 0;
    margin: 0;
    text-indent: 0;
    text-decoration: none;
  }
  .zotero-docs-search-results h3 a:hover { text-decoration: underline; }
  .zotero-docs-search-results p {
    display: block;
    margin: 0;
    padding: 0;
  }
  .zotero-docs-search-context {
    color: #888;
    font-weight: 400;
  }
  .zotero-docs-search-results h3 a {
    color: #1a3a6e;
    text-decoration: none;
  }
  .zotero-docs-search-results h3 a:hover,
  .zotero-docs-search-results h3 a:focus {
    text-decoration: underline;
    outline: none;
  }
  .zotero-docs-search-results article:focus-within {
    background: #f5f8fc;
  }
  .zotero-docs-search-results p {
    margin: 0;
    font-size: 0.85em;
    color: #666;
    line-height: 1.4;
  }
  .zotero-docs-search-empty {
    padding: 0.7em;
    color: #888;
    font-size: 0.9em;
    font-style: italic;
  }
  .zotero-docs-nav ul {
    list-style: none; padding: 0; margin: 0;
  }
  .zotero-docs-nav ul ul {
    padding-left: 0.9em; margin: 0.1em 0 0.3em;
  }
  .zotero-docs-nav li { display: block; margin: 0.15em 0; }
  .zotero-docs-nav a {
    color: #444; text-decoration: none; display: block;
    padding: 0.15em 0.4em; border-radius: 3px;
  }
  .zotero-docs-nav a:hover { background: #f0f0f0; color: #000; }
  .zotero-docs-nav li.active > a {
    background: #e8eef5; color: #1a3a6e; font-weight: 600;
  }
  .zotero-docs-nav details {
    margin-top: 0.5em;
  }
  .zotero-docs-nav > ul > li {
    margin-top: 0.5em;
  }
  .zotero-docs-nav > ul > li > a,
  .zotero-docs-nav summary {
    list-style: none;
    cursor: pointer;
    padding: 0.25em 0.4em;
    font-weight: 600;
    color: #111;
    user-select: none;
  }
  .zotero-docs-nav summary::-webkit-details-marker { display: none; }
  /* Disclosure chevron drawn as a CSS border triangle so its geometric
     center matches the box center — rotating around the default origin
     keeps it visually anchored (a text ▸ glyph isn't centered in its
     em-box and drifts horizontally when rotated). */
  .zotero-docs-nav summary::before,
  .zotero-docs-nav > ul > li > a::before {
    content: "";
    display: inline-block;
    width: 0;
    height: 0;
    border: 4px solid transparent;
    border-left-color: #888;
    vertical-align: middle;
    margin-right: 0.25em;
    /* The triangle's apex is at the border-box center, so the default
       transform-origin would pivot at the pointy end. Move it to the
       visible triangle's bbox center (x=25% of the 8px-wide border box). */
    transform-origin: 25% 50%;
    transition: transform 0.12s ease;
  }
  .zotero-docs-nav > ul > li > a::before {
    visibility: hidden;
  }
  .zotero-docs-nav details[open] > summary::before {
    transform: rotate(90deg);
  }

  /* ----- Right sidebar (page TOC) ----- */
  .zotero-docs-toc {
    font-size: 0.85em;
    line-height: 1.45;
    position: sticky;
    top: 1em;
    max-height: calc(100vh - 2em);
    overflow-y: auto;
  }
  .zotero-docs-toc-title {
    font-size: 0.9em;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: #555;
    margin: 0 0 0.5em;
    padding-left: 0.4em;
  }
  .zotero-docs-page-meta {
    margin-top: 1.5em;
    padding: 1.2em 0.4em 0;
    border-top: 1px solid #eee;
    font-size: 0.85em;
    color: #555;
  }
  /* No TOC above? The meta block is the only child of the aside and
     doesn't need its separator line / top padding. */
  .zotero-docs-page-meta:first-child {
    margin-top: 0;
    padding-top: 0;
    border-top: none;
  }
  .zotero-docs-modified {
    margin-bottom: 0.6em;
  }
  .zotero-docs-edit {
    display: inline-flex;
    align-items: center;
    color: #555;
    text-decoration: none;
  }
  .zotero-docs-edit svg {
    margin-right: 0.6em;
  }
  .zotero-docs-edit:hover { color: #000; }
  .zotero-docs-toc ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  /* Outer ul draws the 2px guide line; nested ones just indent. The hover
     bar (a ::before on the hovered <a>) is offset back by the cumulative
     nested padding so it always lands on the outer guide line. */
  .zotero-docs-toc > ul {
    border-left: 2px solid #eee;
  }
  .zotero-docs-toc ul ul {
    padding-left: 0.8em;
  }
  .zotero-docs-toc li { display: block; margin: 0; }
  .zotero-docs-toc a {
    color: #555;
    text-decoration: none;
    display: block;
    padding: 0.15em 0.6em;
    position: relative;
  }
  .zotero-docs-toc a:hover {
    color: #000;
  }
  /* Scope to TOC entries (inside the ul) only — the Edit-on-GitHub link
     is a sibling anchor in the same aside but shouldn't get the bar. */
  .zotero-docs-toc ul a:hover::before {
    content: '';
    position: absolute;
    top: 0;
    bottom: 0;
    width: 2px;
    background: #aaa;
  }
  .zotero-docs-toc > ul > li > a:hover::before { left: -2px; }
  .zotero-docs-toc > ul > li > ul > li > a:hover::before { left: calc(-0.8em - 2px); }
  .zotero-docs-toc > ul > li > ul > li > ul > li > a:hover::before { left: calc(-1.6em - 2px); }
  .zotero-docs-toc > ul > li > ul > li > ul > li > ul > li > a:hover::before { left: calc(-2.4em - 2px); }
</style>

<div class="zotero-docs">

<div class="zotero-docs-search">

<div id="zotero-docs-search-results" class="zotero-docs-search-results">

</div>

</div>

- [Home](https://www.zotero.org/support/)
- Getting Started
  - [Installation](https://www.zotero.org/support/installation)
  - [Quick Start Guide](https://www.zotero.org/support/quick_start_guide)
  - [System Requirements](https://www.zotero.org/support/system_requirements)
  - [Frequently Asked Questions](https://www.zotero.org/support/frequently_asked_questions)
  - [Version History](https://www.zotero.org/support/changelog)
- Adding to Your Library
  - [Adding Items](https://www.zotero.org/support/adding_items_to_zotero)
  - [Adding Files](https://www.zotero.org/support/attaching_files)
  - [Feeds](https://www.zotero.org/support/feeds)
  - [Retrieve PDF Metadata](https://www.zotero.org/support/retrieve_pdf_metadata)
  - [Importing from Other Tools](https://www.zotero.org/support/moving_to_zotero)
- Organizing & Taking Notes
  - [Collections and Tags](https://www.zotero.org/support/collections_and_tags)
  - [Searching](https://www.zotero.org/support/searching)
  - [Sorting](https://www.zotero.org/support/sorting)
  - [PDF Reader](https://www.zotero.org/support/pdf_reader)
  - [Notes](https://www.zotero.org/support/notes)
  - [Related Items](https://www.zotero.org/support/related)
  - [Duplicate Detection](https://www.zotero.org/support/duplicate_detection)
- Citations & Bibliographies
  - [Creating Bibliographies](https://www.zotero.org/support/creating_bibliographies)
  - [Word Processor Integration](https://www.zotero.org/support/word_processor_integration)
  - [Citation Styles](https://www.zotero.org/support/styles)
  - [Reports](https://www.zotero.org/support/reports)
- Syncing & Collaboration
  - [Data and File Syncing](https://www.zotero.org/support/sync)
  - [Groups](https://www.zotero.org/support/groups)
  - [My Publications](https://www.zotero.org/support/my_publications)
- Preferences
  - [Preferences](https://www.zotero.org/support/preferences)
  - [Connector Preferences](https://www.zotero.org/support/connector_preferences)
  - [Languages](https://www.zotero.org/support/supported_languages)
- [Knowledge Base](https://www.zotero.org/support/kb)
- Troubleshooting
  - [Getting Help](https://www.zotero.org/support/getting_help)
  - [Library Data Issues](https://www.zotero.org/support/zotero_data)
  - [Web Saving Issues](https://www.zotero.org/support/troubleshooting_translator_issues)
  - [Word Processor Plugin Issues](https://www.zotero.org/support/word_processor_plugin_troubleshooting)
  - [Data Sync Issues](https://www.zotero.org/support/kb/changes_not_syncing)
  - [File Sync Issues](https://www.zotero.org/support/kb/files_not_syncing)
  - [File Handling Issues](https://www.zotero.org/support/kb/file_handling_issues)
- [Developers](https://www.zotero.org/support/dev)

# Zotero Web API Write Requests<a href="#zotero_web_api_write_requests" class="headerlink" title="Permanent link">#</a>

This page documents the write methods of the [Zotero Web API](https://www.zotero.org/support/dev/web_api/v3). See the [Basics](https://www.zotero.org/support/dev/web_api/v3/basics) page for basic information on accessing the API, including possible HTTP status codes not listed here.

An [API key](https://www.zotero.org/support/dev/web_api/v3/basics#authentication) with write access to a given library is necessary to use write methods.

In Zotero 10+, the [local API](https://www.zotero.org/support/dev/web_api/v3/local_api) supports the same write methods against the local database. Writes there use a local API key granted by the user at runtime and check preconditions against local object versions; see [Local API](https://www.zotero.org/support/dev/web_api/v3/local_api#write_requests) for the differences.

## JSON Object Data<a href="#json_object_data" class="headerlink" title="Permanent link">#</a>

By default, objects returned from the API in `format=json` mode include a `data` property containing “editable JSON” — that is, all the object fields that can be modified and sent back to the server:

<div class="codehilite">

    {
      "key": "${OBJECT_KEY}",
      "version": 1,
      "library": { ... },
      "links": { ... },
      "meta": { ... },
      "data": {
        "key": "${OBJECT_KEY}",
        "version": 1,
        "itemType": "webpage",
        "title": "Zotero Quick Start Guide",
        "creators": [
            {
                "creatorType": "author",
                "name": "Center for History and New Media"
            }
        ],
        "abstractNote": "",
        "websiteTitle": "Zotero",
        "websiteType": "",
        "date": "",
        "shortTitle": "",
        "url": "https://www.zotero.org/support/quick_start_guide",
        "accessDate": "2014-06-12T21:28:55Z",
        "language": "",
        "rights": "",
        "extra": "",
        "dateAdded": "2014-06-12T21:28:55Z",
        "dateModified": "2014-06-12T21:28:55Z",
        "tags": [],
        "collections": [],
        "relations": {}
      }
    }

</div>

There are two ways to make changes to the provided JSON:

### Programmatic Approach<a href="#programmatic_approach" class="headerlink" title="Permanent link">#</a>

For programmatic access to the API, the recommended approach is to extract the editable JSON from the `data` property, make changes as necesssary, and upload just the editable JSON back to the API. For new items, an [empty template](https://www.zotero.org/support/dev/web_api/v3/types_and_fields#getting_a_template_for_a_new_item) of the editable JSON can be retrieved from the API.

This approach reduces upload bandwidth by sending only the data that is actually processed by the server. (For an even more efficient upload, the HTTP `PATCH` method, discussed below, can be used to send only the fields that have changed.) The examples in this documentation assume programmatic access.

### REST Approach<a href="#rest_approach" class="headerlink" title="Permanent link">#</a>

For more casual access, the API supports standard REST behavior, allowing the entire downloaded JSON to be reuploaded. This allows edits to be performed without writing a single line of code:

<div class="codehilite">

    $ URL="https://api.zotero.org/users/${LIBRARY_ID}/items"
    $ API_KEY="${API_KEY}"
    $ curl -H "Zotero-API-Key: $API_KEY" $URL > items.json
    $ vi items.json  # edit the item data
    $ curl -H "Zotero-API-Key: $API_KEY" -d @items.json -v $URL

</div>

In this example, a JSON array of items is being saved to a text file, modified in a text editor, and then POSTed back to the same URL.

This approach allows a complicated task such as batch editing to be performed using only cURL and a text editor. Any objects modified in the text file will be updated on the server, while unmodified objects will be left unchanged.

A similar process can be used with PUT for individual objects:

<div class="codehilite">

    $ URL="https://api.zotero.org/users/${LIBRARY_ID}/items/ABCD2345"
    $ API_KEY="${API_KEY}"
    $ curl -H "Zotero-API-Key: $API_KEY" $URL > item.json
    $ vi items.json  # edit the item data
    $ curl -H "Zotero-API-Key: $API_KEY" -X PUT -d @item.json -v $URL

</div>

Note that when uploading full JSON, only the `data` property is processed. All other properties (`library`, `links`, `meta`, etc.) are ignored.

## Item Requests<a href="#item_requests" class="headerlink" title="Permanent link">#</a>

### Creating an Item<a href="#creating_an_item" class="headerlink" title="Permanent link">#</a>

When creating a new item, first get empty JSON for the item type with an [item template request](https://www.zotero.org/support/dev/web_api/v3/types_and_fields#getting_a_template_for_a_new_item) (or use a cached version of the template). Then modify it and resubmit it to the server in an array:

<div class="codehilite">

    POST <userOrGroupPrefix>/items
    Content-Type: application/json
    Zotero-Write-Token: <write token> or If-Unmodified-Since-Version: <last library version>

    [
      {
        "itemType" : "book",
        "title" : "My Book",
        "creators" : [
          {
            "creatorType":"author",
            "firstName" : "Sam",
            "lastName" : "McAuthor"
          },
          {
            "creatorType":"editor",
            "name" : "John T. Singlefield"
          }
        ],
        "tags" : [
          { "tag" : "awesome" },
          { "tag" : "rad", "type" : 1 }
        ],
        "collections" : [
          "BCDE3456", "CDEF4567"
        ],
        "relations" : {
          "owl:sameAs" : "http://zotero.org/groups/${GROUP_ID}/items/JKLM6543",
          "dc:relation" : "http://zotero.org/groups/${GROUP_ID}/items/PQRS6789",
          "dc:replaces" : "http://zotero.org/users/${LIBRARY_ID}/items/BCDE5432"
        }
      }
    ]

</div>

All properties other than `itemType`, `tags`, `collections`, and `relations` are optional.

<table>
<thead>
<tr>
<th colspan="2">Common responses</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>200 OK</code></td>
<td>The request completed. See the response JSON for status of individual writes.</td>
</tr>
<tr>
<td><code>400 Bad Request</code></td>
<td>Invalid type/field; unparseable JSON</td>
</tr>
<tr>
<td><code>409 Conflict</code></td>
<td>The target library is locked.</td>
</tr>
<tr>
<td><code>412 Precondition Failed</code></td>
<td>The version provided in <code>If-Unmodified-Since-Version</code> is out of date, or the provided <code>Zotero-Write-Token</code> has already been submitted.</td>
</tr>
<tr>
<td><code>413 Request Entity Too Large</code></td>
<td>Too many items submitted</td>
</tr>
</tbody>
</table>

`200 OK` response:

<div class="codehilite">

    {
      "success": {
        "0": "<itemKey>"
      },
      "unchanged": {},
      "failed": {},
      }
    }

</div>

See [Creating Multiple Objects](#creating_multiple_objects) for more information on the response format.

### Creating Multiple Items<a href="#creating_multiple_items" class="headerlink" title="Permanent link">#</a>

See [Creating Multiple Objects](#creating_multiple_objects).

### Updating an Existing Item<a href="#updating_an_existing_item" class="headerlink" title="Permanent link">#</a>

To update an existing item, first retrieve the current version of the item:

<div class="codehilite">

    GET <userOrGroupPrefix>/items/<itemKey>

</div>

The editable data, similar to the item data shown above in [Creating an Item](#creating_an_item), will be found in the `data` property in the response.

The API supports two ways of modifying item data: by uploading full item data (`PUT`) or by sending just the data that changed (`PATCH`).

#### Full-item updating (PUT)<a href="#full-item_updating_put" class="headerlink" title="Permanent link">#</a>

With `PUT`, you submit the item’s complete editable JSON to the server, typically by modifying the downloaded editable JSON — that is, the contents of the `data` property — directly and resubmitting it:

<div class="codehilite">

    PUT <userOrGroupPrefix>/items/<itemKey>
    Content-Type: application/json

    {
      "key": "${OBJECT_KEY}",
      "version": 1,
      "itemType" : "book",
      "title" : "My Amazing Book",
      "creators" : [
        {
          "creatorType":"author",
          "firstName" : "Sam",
          "lastName" : "McAuthor"
        },
        {
          "creatorType":"editor",
          "name" : "Jenny L. Singlefield"
        }
      ],
      "tags" : [
        { "tag" : "awesome" },
        { "tag" : "rad", "type" : 1 }
      ],
      "collections" : [
        "BCDE3456", "CDEF4567"
      ],
      "relations" : {
        "owl:sameAs" : "http://zotero.org/groups/${GROUP_ID}/items/JKLM6543",
        "dc:relation" : "http://zotero.org/groups/${GROUP_ID}/items/PQRS6789",
        "dc:replaces" : "http://zotero.org/users/${LIBRARY_ID}/items/BCDE5432"
      }
    }

</div>

All properties other than `itemType`, `tags`, `collections`, and `relations` are optional. Any existing fields not specified will be removed from the item. If `creators`, `tags`, `collections`, or `relations` are empty, any associated creators/tags/collections/relations will be removed from the item.

#### Partial-item updating (PATCH)<a href="#partial-item_updating_patch" class="headerlink" title="Permanent link">#</a>

With `PATCH`, you can submit just the properties that have actually changed, for a potentially much more efficient operation. Properties not included in the uploaded JSON are left untouched on the server. To clear a property, pass an empty string or an empty array as appropriate.

<div class="codehilite">

    PATCH <userOrGroupPrefix>/items/<itemKey>
    If-Unmodified-Since-Version: <last item version>

    {
      "date" : "2013"
      "collections" : [
        "BCDE3456", "CDEF4567"
      ]
    }

</div>

This would add a `date` field to the item and add it in the two specified collections if not already present. Array properties are interpreted as complete lists, so omitting a collection key would cause the item to be removed from that collection.

The `PATCH` behavior is also available when [modifying multiple items](https://www.zotero.org/support/dev/web_api/v3/write_requests#updating_multiple_objects) via `POST`.

#### Both PUT and PATCH<a href="#both_put_and_patch" class="headerlink" title="Permanent link">#</a>

Notes and attachments can be made child items by assigning the parent item’s key to the `parentItem` property. If parent and child items are created in the same `POST` request, the child items must appear after the parent item in the array of items, with a locally created [item key](#object_keys).

The item’s current version number is included in the `version` JSON property, as well as in the `Last-Modified-Version` header of single-item requests. `PUT` and `PATCH` requests must include the item’s current version number in either the `version` property or the `If-Unmodified-Since-Version` header. (`version` is included in responses from the API, so clients that simply modify the editable data do not need to bother with a version header.) If the item has been changed on the server since the item was retrieved, the write request will be rejected with a `412 Precondition Failed` error, and the most recent version of the item will have to be retrieved from the server before changes can be made. See [Version Numbers](https://www.zotero.org/support/dev/web_api/v3/syncing#version_numbers) for more on library and object versioning.

<table>
<thead>
<tr>
<th colspan="2">Common responses</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>204 No Content</code></td>
<td>The item was successfully updated.</td>
</tr>
<tr>
<td><code>400 Bad Request</code></td>
<td>Invalid type/field; unparseable JSON</td>
</tr>
<tr>
<td><code>409 Conflict</code></td>
<td>The target library is locked.</td>
</tr>
<tr>
<td><code>412 Precondition Failed</code></td>
<td>The item has changed since retrieval (i.e., the provided item version no longer matches).</td>
</tr>
</tbody>
</table>

### Updating Multiple Items<a href="#updating_multiple_items" class="headerlink" title="Permanent link">#</a>

See [Updating Multiple Objects](#updating_multiple_objects).

### Deleting an Item<a href="#deleting_an_item" class="headerlink" title="Permanent link">#</a>

<div class="codehilite">

    DELETE <userOrGroupPrefix>/items/<itemKey>
    If-Unmodified-Since-Version: <last item version>

</div>

<table>
<thead>
<tr>
<th colspan="2">Common responses</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>204 No Content</code></td>
<td>The item was deleted.</td>
</tr>
<tr>
<td><code>409 Conflict</code></td>
<td>The target library is locked.</td>
</tr>
<tr>
<td><code>412 Precondition Failed</code></td>
<td>The item has changed since retrieval (i.e., the provided item version no longer matches).</td>
</tr>
<tr>
<td><code>428 Precondition Required</code></td>
<td><code>If-Unmodified-Since-Version</code> was not provided.</td>
</tr>
</tbody>
</table>

### Deleting Multiple Items<a href="#deleting_multiple_items" class="headerlink" title="Permanent link">#</a>

Up to 50 items can be deleted in a single request.

<div class="codehilite">

    DELETE <userOrGroupPrefix>/items?itemKey=<key>,<key>,<key>
    If-Unmodified-Since-Version: <last library version>

    204 No Content
    Last-Modified-Version: <library version>

</div>

<table>
<thead>
<tr>
<th colspan="2">Common responses</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>204 No Content</code></td>
<td>The items were deleted.</td>
</tr>
<tr>
<td><code>409 Conflict</code></td>
<td>The target library is locked.</td>
</tr>
<tr>
<td><code>412 Precondition Failed</code></td>
<td>The library has changed since the specified version.</td>
</tr>
<tr>
<td><code>428 Precondition Required</code></td>
<td><code>If-Unmodified-Since-Version</code> was not provided.</td>
</tr>
</tbody>
</table>

## Collection Requests<a href="#collection_requests" class="headerlink" title="Permanent link">#</a>

### Creating a Collection<a href="#creating_a_collection" class="headerlink" title="Permanent link">#</a>

<div class="codehilite">

    POST <userOrGroupPrefix>/collections
    Content-Type: application/json
    Zotero-Write-Token: <write token> or If-Unmodified-Since-Version: <last library version>

    [
      {
        "name" : "My Collection",
        "parentCollection" : "QRST9876"
      }
    ]

</div>

<table>
<thead>
<tr>
<th colspan="2">Common responses</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>200 OK</code></td>
<td>The request completed without a general error. See the response JSON for status of individual writes.</td>
</tr>
<tr>
<td><code>409 Conflict</code></td>
<td>The target library is locked.</td>
</tr>
<tr>
<td><code>412 Precondition Failed</code></td>
<td>The version provided in <code>If-Unmodified-Since-Version</code> is out of date, or the provided <code>Zotero-Write-Token</code> has already been submitted.</td>
</tr>
</tbody>
</table>

### Updating an Existing Collection<a href="#updating_an_existing_collection" class="headerlink" title="Permanent link">#</a>

<div class="codehilite">

    GET <userOrGroupPrefix>/collections/<collectionKey>

</div>

Editable JSON will be found in the `data` property.

<div class="codehilite">

    PUT <userOrGroupPrefix>/collections/<collectionKey>
    Content-Type: application/json

    {
      "key" : "${OBJECT_KEY}",
      "version" : 156,
      "name" : "My Collection",
      "parentCollection" : false
    }

</div>

<table>
<thead>
<tr>
<th colspan="2">Common responses</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>200 OK</code></td>
<td>The collection was updated.</td>
</tr>
<tr>
<td><code>409 Conflict</code></td>
<td>The target library is locked.</td>
</tr>
<tr>
<td><code>412 Precondition Failed</code></td>
<td>The collection has changed since retrieval (i.e., the provided collection version no longer matches).</td>
</tr>
</tbody>
</table>

### Collection-Item Membership<a href="#collection-item_membership" class="headerlink" title="Permanent link">#</a>

Items can be added to or removed from collections via the `collections` property in the item JSON.

### Deleting a Collection<a href="#deleting_a_collection" class="headerlink" title="Permanent link">#</a>

<div class="codehilite">

    DELETE <userOrGroupPrefix>/collections/<collectionKey>
    If-Unmodified-Since-Version: <last collection version>

</div>

<table>
<thead>
<tr>
<th colspan="2">Common responses</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>204 No Content</code></td>
<td>The collection was deleted.</td>
</tr>
<tr>
<td><code>409 Conflict</code></td>
<td>The target library is locked.</td>
</tr>
<tr>
<td><code>412 Precondition Failed</code></td>
<td>The collection has changed since retrieval (i.e., the provided ETag no longer matches).</td>
</tr>
</tbody>
</table>

### Deleting Multiple Collections<a href="#deleting_multiple_collections" class="headerlink" title="Permanent link">#</a>

Up to 50 collections can be deleted in a single request.

<div class="codehilite">

    DELETE <userOrGroupPrefix>/collections?collectionKey=<collectionKey>,<collectionKey>,<collectionKey>
    If-Unmodified-Since-Version: <last library version>

    204 No Content
    Last-Modified-Version: <library version>

</div>

<table>
<thead>
<tr>
<th colspan="2">Common responses</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>204 No Content</code></td>
<td>The collections were deleted.</td>
</tr>
<tr>
<td><code>409 Conflict</code></td>
<td>The target library is locked.</td>
</tr>
<tr>
<td><code>412 Precondition Failed</code></td>
<td>The library has changed since the specified version.</td>
</tr>
</tbody>
</table>

## Saved Search Requests<a href="#saved_search_requests" class="headerlink" title="Permanent link">#</a>

### Creating a Search<a href="#creating_a_search" class="headerlink" title="Permanent link">#</a>

<div class="codehilite">

    POST <userOrGroupPrefix>/searches
    Content-Type: application/json
    Zotero-Write-Token: <write token> or If-Unmodified-Since-Version: <last library version>

    [
      {
        "name": "My Search",
        "conditions": [
          {
            "condition": "title",
            "operator": "contains",
            "value": "foo"
          },
          {
            "condition": "date",
            "operator": "isInTheLast",
            "value": "7 days"
          }
        ]
      }
    ]

</div>

<table>
<thead>
<tr>
<th colspan="2">Common responses</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>200 OK</code></td>
<td>The request completed without a general error. See the response JSON for status of individual writes.</td>
</tr>
<tr>
<td><code>409 Conflict</code></td>
<td>The target library is locked.</td>
</tr>
<tr>
<td><code>412 Precondition Failed</code></td>
<td>The version provided in <code>If-Unmodified-Since-Version</code> is out of date, or the provided <code>Zotero-Write-Token</code> has already been submitted.</td>
</tr>
</tbody>
</table>

### Deleting Multiple Searches<a href="#deleting_multiple_searches" class="headerlink" title="Permanent link">#</a>

Up to 50 searches can be deleted in a single request.

<div class="codehilite">

    DELETE <userOrGroupPrefix>/searches?searchKey=<searchKey>,<searchKey>,<searchKey>
    If-Unmodified-Since-Version: <last library version>

    204 No Content
    Last-Modified-Version: <library version>

</div>

<table>
<thead>
<tr>
<th colspan="2">Common responses</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>204 No Content</code></td>
<td>The searches were deleted.</td>
</tr>
<tr>
<td><code>409 Conflict</code></td>
<td>The target library is locked.</td>
</tr>
<tr>
<td><code>412 Precondition Failed</code></td>
<td>The library has changed since the specified version.</td>
</tr>
</tbody>
</table>

## Tag Requests<a href="#tag_requests" class="headerlink" title="Permanent link">#</a>

### Deleting Multiple Tags<a href="#deleting_multiple_tags" class="headerlink" title="Permanent link">#</a>

Up to 50 tags can be deleted in a single request.

<div class="codehilite">

    DELETE <userOrGroupPrefix>/tags?tag=<URL-encoded tag 1> || <URL-encoded tag 2> || <URL-encoded tag 3>
    If-Unmodified-Since-Version: <last library version>

    204 No Content
    Last-Modified-Version: <library version>

</div>

## Multi-Object Requests<a href="#multi-object_requests" class="headerlink" title="Permanent link">#</a>

### Creating Multiple Objects<a href="#creating_multiple_objects" class="headerlink" title="Permanent link">#</a>

Up to 50 collections, saved searches, or items can be created in a single request by including multiple objects in an array:

<div class="codehilite">

    POST <userOrGroupPrefix>/collections
    Content-Type: application/json
    Zotero-Write-Token: <write token> or If-Unmodified-Since-Version: <last library version>

    [
      {
        "name" : "My Collection",
        "parentCollection": "QRST9876"
      },
      {
        "name": "My Other Collection"
      }
    ]

</div>

For [syncing](https://www.zotero.org/support/dev/web_api/v3/syncing) objects with predetermined keys, an [object key](#object_keys) can also be provided with new objects.

`200` response:

<div class="codehilite">

    Content-Type: application/json
    Last-Modified-Version: <library version>

    {
      "successful": {
        "0": "<saved object>",
        "2": "<saved object>"
      },
      "unchanged": {
        "4": "<objectKey>"
      }
      "failed": {
        "1": {
          "key": "<objectKey>",
          "code": <HTTP response code>,
          "message": "<error message>"
        },
        "3": {
          "key": "<objectKey>",
          "code": <HTTP response code>,
          "message": "<error message>"
        },
      }
    }

</div>

The keys of the `successful`, `unchanged`, and `failed` objects are the numeric indexes of the Zotero objects in the uploaded array. The `Last-Modified-Version` is the version that has been assigned to any Zotero objects in the `successful` object — that is, objects that were modified in this request.

<table>
<thead>
<tr>
<th colspan="2">Common responses</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>200 OK</code></td>
<td>The objects were uploaded.</td>
</tr>
<tr>
<td><code>409 Conflict</code></td>
<td>The target library is locked.</td>
</tr>
<tr>
<td><code>412 Precondition Failed</code></td>
<td>The version provided in <code>If-Unmodified-Since-Version</code> is out of date, or the provided <code>Zotero-Write-Token</code> has already been submitted.</td>
</tr>
</tbody>
</table>

#### Updating Multiple Objects<a href="#updating_multiple_objects" class="headerlink" title="Permanent link">#</a>

Up to 50 collections, saved searches, or items can be updated in a single request.

Follow the instructions in [Creating Multiple Objects](#creating_multiple_objects), but include a `key` and `version` property in each object. If modifying editable JSON returned from the API, these properties will already exist and shouldn’t be modified. As an alternative to individual `version` properties, the last-known library version can be passed via the `If-Unmodified-Since-Version` HTTP Header.

Items can also include `dateAdded` and `dateModified` properties containing timestamps in [ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601) (e.g., “2014-06-10T13:52:43Z”). If `dateAdded` is included with an existing item, it must match the existing `dateAdded` value or else the API will return a 400 error. If a new `dateModified` time is not included with an update to existing item, the item’s `dateModified` value will be set to the current time. Editable JSON returned from the API includes `dateAdded` and `dateModified` in the correct format, so clients that are content with server-set modification times can simply ignore these properties.

<div class="codehilite">

    POST <userOrGroupPrefix>/collections
    Content-Type: application/json

    [
      {
        "key": "${OBJECT_KEY}",
        "version": 414,
        "name": "My Collection",
        "parentCollection": false
      },
      {
        "key": "${OBJECT_KEY}",
        "version": 416
        "name": "My Subcollection",
        "parentCollection": "BD85JEM4"
      }
    ]

</div>

The response is the same as that in [Creating Multiple Objects](#creating_multiple_objects).

Note that `POST` follows `PATCH` semantics, meaning that any properties not specified will be left untouched on the server. To erase an existing property, include it with an empty string or `false` as the value.

## Object Keys<a href="#object_keys" class="headerlink" title="Permanent link">#</a>

While the server will automatically generate valid keys for uploaded objects, in some situations, such as when [syncing](https://www.zotero.org/support/dev/web_api/v3/syncing) or creating a parent and child item in the same request, it may be desirable or necessary to create object keys locally.

Local object keys should conform to the pattern `/[23456789ABCDEFGHIJKLMNPQRSTUVWXYZ]{8}/`.

## Zotero-Write-Token<a href="#zotero-write-token" class="headerlink" title="Permanent link">#</a>

<div class="codehilite">

    Zotero-Write-Token: 19a4f01ad623aa7214f82347e3711f56

</div>

`Zotero-Write-Token` is an optional HTTP header, containing a client-generated random 32-character identifier string, that can be included with unversioned write requests to prevent them from being processed more than once (e.g., if a user clicks a form submit button twice). The Zotero server caches write tokens for successful requests for 12 hours, and subsequent requests from the same API key using the same write token will be rejected with a `412 Precondition Failed` status code. If a request fails, the write token will not be stored.

If using [versioned write requests](https://www.zotero.org/support/dev/web_api/v3/syncing#version_numbers) (i.e., those that include an `If-Unmodified-Since-Version` HTTP header or individual object `version` properties), `Zotero-Write-Token` is redundant and should be omitted.

In Zotero 10+, the [local API](https://www.zotero.org/support/dev/web_api/v3/local_api) also caches write tokens for 12 hours, but only in memory, so a token is forgotten if Zotero restarts.

## Examples<a href="#examples" class="headerlink" title="Permanent link">#</a>

See the [Syncing](https://www.zotero.org/support/dev/web_api/v3/syncing) page for an example workflow that puts together read and write methods for complete and efficient syncing of Zotero data via the API.

<div class="aside zotero-docs-toc">

<div class="zotero-docs-toc-title">

On this page

</div>

- [Zotero Web API Write Requests](#zotero_web_api_write_requests)
  - [JSON Object Data](#json_object_data)
    - [Programmatic Approach](#programmatic_approach)
    - [REST Approach](#rest_approach)
  - [Item Requests](#item_requests)
    - [Creating an Item](#creating_an_item)
    - [Creating Multiple Items](#creating_multiple_items)
    - [Updating an Existing Item](#updating_an_existing_item)
      - [Full-item updating (PUT)](#full-item_updating_put)
      - [Partial-item updating (PATCH)](#partial-item_updating_patch)
      - [Both PUT and PATCH](#both_put_and_patch)
    - [Updating Multiple Items](#updating_multiple_items)
    - [Deleting an Item](#deleting_an_item)
    - [Deleting Multiple Items](#deleting_multiple_items)
  - [Collection Requests](#collection_requests)
    - [Creating a Collection](#creating_a_collection)
    - [Updating an Existing Collection](#updating_an_existing_collection)
    - [Collection-Item Membership](#collection-item_membership)
    - [Deleting a Collection](#deleting_a_collection)
    - [Deleting Multiple Collections](#deleting_multiple_collections)
  - [Saved Search Requests](#saved_search_requests)
    - [Creating a Search](#creating_a_search)
    - [Deleting Multiple Searches](#deleting_multiple_searches)
  - [Tag Requests](#tag_requests)
    - [Deleting Multiple Tags](#deleting_multiple_tags)
  - [Multi-Object Requests](#multi-object_requests)
    - [Creating Multiple Objects](#creating_multiple_objects)
      - [Updating Multiple Objects](#updating_multiple_objects)
  - [Object Keys](#object_keys)
  - [Zotero-Write-Token](#zotero-write-token)
  - [Examples](#examples)

<div class="zotero-docs-page-meta">

<div class="zotero-docs-modified">

Last updated 2026-07-29

</div>

<a href="https://github.com/zotero/zotero-docs/edit/main/content/dev/web_api/v3/write_requests.md" class="zotero-docs-edit"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgZmlsbD0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSI+PHBhdGggZD0iTTExLjAxMyAxLjQyN2ExLjc1IDEuNzUgMCAwIDEgMi40NzQgMGwxLjA4NiAxLjA4NmExLjc1IDEuNzUgMCAwIDEgMCAyLjQ3NGwtOC42MSA4LjYxYy0uMjEuMjEtLjQ3LjM2NC0uNzU2LjQ0NWwtMy4yNTEuOTNhLjc1Ljc1IDAgMCAxLS45MjctLjkyOGwuOTI5LTMuMjVjLjA4MS0uMjg2LjIzNS0uNTQ3LjQ0NS0uNzU4bDguNjEtOC42MVptLjE3NiA0LjgyM0w5Ljc1IDQuODFsLTYuMjg2IDYuMjg3YS4yNTMuMjUzIDAgMCAwLS4wNjQuMTA4bC0uNTU4IDEuOTUzIDEuOTUzLS41NThhLjI1My4yNTMgMCAwIDAgLjEwOC0uMDY0TDExLjE4OSA2LjI1Wm0yLjk1LTIuMTItMS4wODYtMS4wODZhLjI1LjI1IDAgMCAwLS4zNTQgMGwtMS4wMTIgMS4wMTIgMS40NCAxLjQ0IDEuMDEyLTEuMDEzYS4yNS4yNSAwIDAgMCAwLS4zNTNaIiAvPjwvc3ZnPg==" />Edit on GitHub</a>

</div>

</div>

</div>

</div>
