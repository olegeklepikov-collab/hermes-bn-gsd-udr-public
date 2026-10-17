> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Zotero: basics

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

# Zotero Web API Documentation<a href="#zotero_web_api_documentation" class="headerlink" title="Permanent link">#</a>

This page documents read requests available in the [Zotero Web API](https://www.zotero.org/support/dev/web_api/v3), providing read-only access to online Zotero libraries. The Zotero desktop client exposes the same endpoints as a [local API](https://www.zotero.org/support/dev/web_api/v3/local_api) that serves data from the local database, which is useful for code running on the user’s computer.

## Base URL<a href="#base_url" class="headerlink" title="Permanent link">#</a>

The base URL for all API requests is

<div class="codehilite">

    https://api.zotero.org

</div>

All requests must use HTTPS. (The local API uses `http://localhost:23119/api/` instead; see [Local API](https://www.zotero.org/support/dev/web_api/v3/local_api).)

## API Versioning<a href="#api_versioning" class="headerlink" title="Permanent link">#</a>

Multiple versions of the API are available, and production code should always request a specific version. This page documents API version 3, which is currently the default and recommended version.

Clients can request a specific version in one of two ways:

1.  Via the `Zotero-API-Version` HTTP header (`Zotero-API-Version: 3`)
2.  Via the `v` query parameter (`v=3`)

Use of the `Zotero-API-Version` header is recommended for production code. The `v` parameter can be used for easier debugging and sharing of API requests or in clients that can’t pass arbitrary HTTP headers.

The API version of a response will be returned in the `Zotero-API-Version` response header.

### Version Transitions<a href="#version_transitions" class="headerlink" title="Permanent link">#</a>

At most times, API changes are made in a backwards-compatible manner. Occasionally, however, backwards-incompatible changes may need to be made. When this occurs, a new API version will be made available without changing the default version for clients that don’t request a specific version. After a transition period, the new API version will become the default. If an API version is discontinued, clients requesting the discontinued version will receive the oldest available version. Announcements regarding API version transitions will always be made ahead of time on [zotero-dev](https://groups.google.com/group/zotero-dev).

## Authentication<a href="#authentication" class="headerlink" title="Permanent link">#</a>

Authentication is not required for read access to public libraries.

Accessing non-public libraries requires use of an API key. Third-party developers should [use OAuth to establish credentials](https://www.zotero.org/support/dev/web_api/v3/oauth) or instruct their users to create dedicated keys for use with their services. End users can create API keys via [their Zotero account settings](https://www.zotero.org/settings/keys/new).

API keys can be included in requests in one of three ways:

1.  As an HTTP header in the form `Zotero-API-Key: ${API_KEY}`
2.  As an HTTP header in the form `Authorization: Bearer [СЕКРЕТ УДАЛЁН]`
3.  As a URL query parameter, in the form `key=${ZOTERO_API_KEY}` (not recommended)

Use of an HTTP header is recommended, as it allows use of URLs returned from the API (e.g., for pagination) without modification.

`Authorization: Bearer` is also the authentication mechanism for OAuth 2.0. While Zotero currently supports only OAuth 1.0a, when support for OAuth 2.0 is added, clients will no longer need to extract the API key from the OAuth response and pass it to the API separately.

The [local API](https://www.zotero.org/support/dev/web_api/v3/local_api) does not use authentication for read requests. Write requests (Zotero 10+) require a local API key, which is unrelated to a zotero.org API key and is granted by the user at runtime; see [Authorizing Writes](https://www.zotero.org/support/dev/web_api/v3/local_api#authorizing_writes).

## Local API<a href="#local_api" class="headerlink" title="Permanent link">#</a>

The Zotero desktop client exposes a local implementation of this API on `localhost:23119` under `/api/`, serving data from the user’s local database. See [Local API](https://www.zotero.org/support/dev/web_api/v3/local_api) for details. The sections below note where local API behavior diverges from the Web API.

## Resources<a href="#resources" class="headerlink" title="Permanent link">#</a>

### User and Group Library URLs<a href="#user_and_group_library_urls" class="headerlink" title="Permanent link">#</a>

Requests for data in a specific library begin with `/users/<userID>` or `/groups/<groupID>`, referred to below as \<userOrGroupPrefix\>. User IDs are different from usernames and can be found on the [API Keys](https://www.zotero.org/settings/keys) page and in OAuth responses. Group IDs are different from group names and can be retrieved from `/users/<userID>/groups`.

#### Collections<a href="#collections" class="headerlink" title="Permanent link">#</a>

| URI | Description |
|----|----|
| \<userOrGroupPrefix\>/collections | Collections in the library |
| \<userOrGroupPrefix\>/collections/top | Top-level collections in the library |
| \<userOrGroupPrefix\>/collections/\<collectionKey\> | A specific collection in the library |
| \<userOrGroupPrefix\>/collections/\<collectionKey\>/collections | Subcollections within a specific collection in the library |

#### Items<a href="#items" class="headerlink" title="Permanent link">#</a>

| URI | Description |
|----|----|
| \<userOrGroupPrefix\>/items | All items in the library, excluding trashed items |
| \<userOrGroupPrefix\>/items/top | Top-level items in the library, excluding trashed items |
| \<userOrGroupPrefix\>/items/trash | Items in the trash |
| \<userOrGroupPrefix\>/items/\<itemKey\> | A specific item in the library |
| \<userOrGroupPrefix\>/items/\<itemKey\>/children | Child items under a specific item |
| \<userOrGroupPrefix\>/publications/items | Items in My Publications |
| \<userOrGroupPrefix\>/collections/\<collectionKey\>/items | Items within a specific collection in the library |
| \<userOrGroupPrefix\>/collections/\<collectionKey\>/items/top | Top-level items within a specific collection in the library |

#### Searches<a href="#searches" class="headerlink" title="Permanent link">#</a>

(Note: Only search metadata is currently available, not search results.)

| URI | Description |
|----|----|
| \<userOrGroupPrefix\>/searches | All saved searches in the library |
| \<userOrGroupPrefix\>/searches/\<searchKey\> | A specific saved search in the library |

#### Tags<a href="#tags" class="headerlink" title="Permanent link">#</a>

| URI | Description |
|----|----|
| \<userOrGroupPrefix\>/tags | All tags in the library |
| \<userOrGroupPrefix\>/tags/ | Tags of all types matching a specific name |
| \<userOrGroupPrefix\>/items/\<itemKey\>/tags | Tags associated with a specific item |
| \<userOrGroupPrefix\>/collections/\<collectionKey\>/tags | Tags within a specific collection in the library |
| \<userOrGroupPrefix\>/items/tags | All tags in the library, with the ability to filter based on the items |
| \<userOrGroupPrefix\>/items/top/tags | Tags assigned to top-level items |
| \<userOrGroupPrefix\>/items/trash/tags | Tags assigned to items in the trash |
| \<userOrGroupPrefix\>/collections/\<collectionKey\>/items/tags | Tags assigned to items in a given collection |
| \<userOrGroupPrefix\>/collections/\<collectionKey\>/items/top/tags | Tags assigned to top-level items in a given collection |
| \<userOrGroupPrefix\>/publications/items/tags | Tags assigned to items in My Publications |

### Other URLs<a href="#other_urls" class="headerlink" title="Permanent link">#</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>URI</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>/keys/&lt;key&gt;</td>
<td>The user id and privileges of the given API key.<br />
Use the <code>DELETE</code> HTTP method to delete the key. This should generally be done only by a client that created the key originally using <a href="/dev/web_api/v3/OAuth">OAuth</a>.</td>
</tr>
<tr class="even">
<td>/users/&lt;userID&gt;/groups</td>
<td>The set of groups the current API key has access to, including public groups the key owner belongs to even if the key doesn't have explicit permissions for them.</td>
</tr>
</tbody>
</table>

## Read Requests<a href="#read_requests" class="headerlink" title="Permanent link">#</a>

The following parameters affect the format of data returned from read requests. All parameters are optional.

### General Parameters<a href="#general_parameters" class="headerlink" title="Permanent link">#</a>

The following parameters are valid for all read requests:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Values</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>format</code></td>
<td><code>atom</code>, <code>bib</code>, <code>json</code>, <code>keys</code>, <code>versions</code>, <a href="#export_formats">export format</a></td>
<td><code>json</code> (or <code>atom</code> if the <code>Accept</code> header includes <code>application/atom+xml</code>)</td>
<td><code>atom</code> will return an Atom feed suitable for use in feed readers or feed-reading libraries.<br />
<code>bib</code>, valid only for item requests, will return a formatted bibliography as XHTML. <code>bib</code> mode is currently limited to a maximum of 150 items.<br />
<code>json</code> will return a JSON array for multi-object requests and a single JSON object for single-object requests.<br />
<code>keys</code>, valid for multi-object requests, will return a newline-separated list of object keys. <code>keys</code> mode has no default or maximum limit.<br />
<code>versions</code>, valid for multi-object collection, item, and search requests, will return a JSON object with Zotero object keys as keys and object versions as values. Like <code>keys</code>, <code>versions</code> mode has no default or maximum limit.<br />
Export formats, valid only for item requests, produce output in the specified format.</td>
</tr>
</tbody>
</table>

The [local API](https://www.zotero.org/support/dev/web_api/v3/local_api) does not support `format=atom`; requests using it return `501 Not Implemented`. All other formats are supported.

### Parameters for “format=json”<a href="#parameters_for_formatjson" class="headerlink" title="Permanent link">#</a>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Values</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>include</code></td>
<td><code>bib</code>, <code>citation</code>, <code>data</code>, <a href="#export_formats">export format</a><br />
Multiple formats can be specified by using a comma as the delimiter (<code>include=data,bib</code>).</td>
<td><code>data</code></td>
<td>Formats to include in the response:<br />
<code>bib</code>, valid only for item requests, will return a formatted reference for each item.<br />
<code>citation</code>, valid only for item requests, will return a formatted citation for each item.<br />
<code>data</code> (the default) will include all writeable fields in JSON format, suitable for modifying and sending back to the API.<br />
Export formats, valid only for item requests, will return data in the specified format for each item.</td>
</tr>
</tbody>
</table>

### Parameters for “format=atom”<a href="#parameters_for_formatatom" class="headerlink" title="Permanent link">#</a>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Values</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>content</code></td>
<td><code>bib</code>, <code>citation</code>, <code>html</code>, <code>json</code>, <a href="#export_formats">export formats</a>, <code>none</code><br />
Multiple formats can be specified by using a comma as the delimiter (<code>content=json,bib</code>).</td>
<td><code>html</code></td>
<td>The format of the Atom response's <code>&lt;content&gt;</code> node:<br />
<code>html</code> (the default) will return an XHTML representation of each object, useful for display in feed readers and for parsing by XML tools.<br />
<code>json</code>, currently valid only for item and collection requests, will return a JSON representation of all the item's fields.<br />
<code>bib</code>, valid only for item requests, will return a formatted reference for each item.<br />
<code>citation</code>, valid only for item requests, will return a formatted citation for each item.<br />
Export formats, valid only for item requests, will return data in the specified format for each item.<br />
If additional data is not required, use <code>none</code> to decrease the response size.<br />
If multiple formats are requested, <code>&lt;content&gt;</code> will contain multiple <code>&lt;zapi:subcontent&gt;</code> elements (in the http://zotero.org/ns/api namespace), each with a <code>zapi:type</code> attribute matching one of the specified content parameters.</td>
</tr>
</tbody>
</table>

The Atom parameters above do not apply to the [local API](https://www.zotero.org/support/dev/web_api/v3/local_api), which does not produce Atom output.

### Parameters for “format=bib”, “include/content=bib”, “include/content=citation”<a href="#parameters_for_formatbib_includecontentbib_includecontentcitation" class="headerlink" title="Permanent link">#</a>

| Parameter | Values | Default | Description |
|----|----|----|----|
| `style` | string | `chicago-note-bibliography` | Citation style to use for formatted references. Can be either the file name (without the .csl extension) of one of the styles in the [Zotero Style Repository](https://www.zotero.org/styles/) (e.g., `apa`) or the URL of a remote CSL file. |
| `linkwrap` | boolean | `0` | Set to `1` to return URLs and DOIs as links |
| `locale` | string | `en-US` | Bibliography locale. See the [available CSL locales](https://github.com/citation-style-language/locales). Note that some styles use a fixed locale and cannot be localized. |

Note the difference between `format=bib` and `include=bib`/`content=bib`. `format=bib` returns a formatted bibliography as XHTML, sorted according to the rules of the selected style. `include=bib` (valid only for `format=json` (the default format mode) and `format=atom`) returns an individual formatted reference within the JSON `data` block or Atom \<content\> block for each item, with the results or feed sorted according to the query parameters. `format=bib` processes the entire feed you are requesting without regard for any limit arguments, so it is generally a good idea to use it only with collections or tags.

### Item Export Formats<a href="#item_export_formats" class="headerlink" title="Permanent link">#</a>

The following bibliographic data formats can be used as `format`, `include`, and `content` parameters for items requests:

| Parameter | Description |
|----|----|
| `bibtex` | BibTeX |
| `biblatex` | BibLaTeX |
| `bookmarks` | Netscape Bookmark File Format |
| `coins` | COinS |
| `csljson` | [Citation Style Language data format](https://github.com/citation-style-language/schema/blob/master/csl-data.json) |
| `csv` | CSV |
| `mods` | MODS |
| `refer` | Refer/BibIX |
| `rdf_bibliontology` | [Bibliographic Ontology](http://bibliontology.com/) RDF |
| `rdf_dc` | Unqualified Dublin Core RDF |
| `rdf_zotero` | Zotero RDF |
| `ris` | RIS |
| `tei` | Text Encoding Initiative (TEI) |
| `wikipedia` | Wikipedia Citation Templates |

## Searching<a href="#searching" class="headerlink" title="Permanent link">#</a>

### Search Parameters<a href="#search_parameters" class="headerlink" title="Permanent link">#</a>

| Parameter | Values | Default | Description |
|----|----|----|----|
| `itemKey` | string | null | A comma-separated list of item keys. Valid only for item requests. Up to 50 items can be specified in a single request. |
| `itemType` | [search syntax](#search_syntax) | null | Item type search |
| `q` | string | null | Quick search. Searches titles and individual creator fields by default. Use the `qmode` parameter to change the mode. Currently supports phrase searching only. |
| `since` | integer | `0` | Return only objects modified after the specified library version, returned in a previous `Last-Modified-Version` header. See [Syncing](https://www.zotero.org/support/dev/web_api/v3/syncing) for more info. |
| `tag` | [search syntax](#search_syntax) | null | Tag search |

The [local API](https://www.zotero.org/support/dev/web_api/v3/local_api) accepts the same search parameters but uses Zotero’s local quicksearch implementation, so the set of items returned by a given `q` value may not match the Web API exactly.

### Search Parameters (Items Endpoints)<a href="#search_parameters_items_endpoints" class="headerlink" title="Permanent link">#</a>

| Parameter | Values | Default | Description |
|----|----|----|----|
| `includeTrashed` | `0`, `1` | `0` (except in `/trash`) | Include items in the trash |
| `qmode` | `titleCreatorYear`, `everything` | `titleCreatorYear` | Quick search mode. To include full-text content, use `everything`. Searching of other fields will be possible in the future. |

### Search Parameters (Tags Endpoints)<a href="#search_parameters_tags_endpoints" class="headerlink" title="Permanent link">#</a>

| Parameter | Values | Default | Description |
|----|----|----|----|
| `qmode` | `contains`, `startsWith` | `contains` | Quick search mode. To perform a left-bound search, use `startsWith`. |

### Search Parameters (Tags-Within-Items Endpoints)<a href="#search_parameters_tags-within-items_endpoints" class="headerlink" title="Permanent link">#</a>

These parameters can be used to search against items when returning tags within items. In such cases, the main parameters (`q`, `qmode`, `tag`) apply to the tags themselves, as the primary objects of the request.

| Parameter | Values | Default | Description |
|----|----|----|----|
| `itemQ` | string | null | Same as `q` in an `items` request |
| `itemQMode` | `contains`, `startsWith` | `contains` | Same as `qmode` in an `items` request |
| `itemTag` | [search syntax](#search_syntax) | null | Same as `tag` in an `items` request |

### Search Syntax<a href="#search_syntax" class="headerlink" title="Permanent link">#</a>

`itemType` and `tag` parameters support Boolean searches:

Examples:

- `itemType=book`
- `itemType=book || journalArticle` (OR)
- `itemType=-attachment` (NOT)
- `tag=foo`
- `tag=foo bar` (tag with space)
- `tag=foo&tag=bar` (AND)
- `tag=foo bar || bar` (OR)
- `tag=-foo` (NOT)
- `tag=\-foo` (literal first-character hyphen)

Be sure to URL-encode search strings if required by your client or library.

## Sorting and Pagination<a href="#sorting_and_pagination" class="headerlink" title="Permanent link">#</a>

### Sorting and Pagination Parameters<a href="#sorting_and_pagination_parameters" class="headerlink" title="Permanent link">#</a>

The following parameters are valid only for multi-object read requests such as `<userOrGroupPrefix>/items`, with the exception of `format=bib` requests, which do not support sorting or pagination.

| Parameter | Values | Default | Description |
|----|----|----|----|
| `sort` | `dateAdded`, `dateModified`, `title`, `creator`, `itemType`, `date`, `publisher`, `publicationTitle`, `journalAbbreviation`, `language`, `accessDate`, `libraryCatalog`, `callNumber`, `rights`, `addedBy`, `numItems` (tags) | `dateModified` (`dateAdded` for Atom) | The name of the field by which entries are sorted |
| `direction` | `asc`, `desc` | varies by `sort` | The sorting direction of the field specified in the `sort` parameter |
| `limit` | integer 1-100\* | `25` | The maximum number of results to return with a single request. Required for export formats. |
| `start` | integer | `0` | The index of the first result. Combine with the limit parameter to select a slice of the available results. |

The [local API](https://www.zotero.org/support/dev/web_api/v3/local_api) does not impose a default or maximum `limit`. If `limit` is omitted, all matching objects are returned in one response. Pagination parameters and `Link` headers still work for clients that want them.

#### Total Results<a href="#total_results" class="headerlink" title="Permanent link">#</a>

Responses for multi-object read requests will include a custom HTTP header, `Total-Results`, that provides the total number of results matched by the request. In the Web API, the actual number of results provided in a given response will be no more than 100.

#### Link Header<a href="#link_header" class="headerlink" title="Permanent link">#</a>

When the total number of results matched by a read request is greater than the current limit, the API will include pagination links in the HTTP `Link` header. Possible values are `rel=first`, `rel=prev`, `rel=next`, and `rel=last`. For some requests, the header may also include a `rel=alternate` link for the relevant page on the Zotero website.

<div class="codehilite">

    GET https://api.zotero.org/users/${LIBRARY_ID}/items?limit=30

    Link: <https://api.zotero.org/users/${LIBRARY_ID}/items?limit=30&start=30>; rel="next",
     <https://api.zotero.org/users/${LIBRARY_ID}/items?limit=30&start=5040>; rel="last",
     <https://www.zotero.org/users/${LIBRARY_ID}/items>; rel="alternate"

</div>

(Newlines are inserted here for clarity.)

## Caching<a href="#caching" class="headerlink" title="Permanent link">#</a>

For efficient usage of the API, clients should make conditional GET requests whenever possible. Multi-object requests (e.g., `/users/${LIBRARY_ID}/items`) return a `Last-Modified-Version` header with the current library version. If a `If-Modified-Since-Version: <libraryVersion>` header is passed with a subsequent multi-object read request and data has not changed in the library since the specified version, the API will return `304 Not Modified` instead of `200`. (Single-object conditional requests are not currently supported, but will be supported in the future.)

While a conditional GET request that returns a `304` should be fast, some clients may wish or need to perform additional caching on their own, using stored data for a period of time before making subsequent conditional requests to the Zotero API. This makes particular sense when the underlying Zotero data is known not to change frequently or when the data will be accessed frequently. For example, a website that displayed a bibliography from a Zotero collection might cache the returned bibliography for an hour, after which time it would make another conditional request to the Zotero API. If the API returned a `304`, the website would continue to display the cached bibliography for another hour before retrying. This would prevent the website from making a request to the Zotero API every time a user loaded a page.

In addition to making conditional requests, clients downloading data for entire Zotero libraries should use `?since=` to request only objects that have changed since the last time data was downloaded.

See [Syncing](https://www.zotero.org/support/dev/web_api/v3/syncing) for more information on library and object versioning.

Conditional requests work the same way against the [local API](https://www.zotero.org/support/dev/web_api/v3/local_api), but local responses are already inexpensive to produce, so aggressive caching on the client side is less important. The `?since=` parameter is also supported and is the preferred way to fetch only changed objects from a large local library. Note that in Zotero 10+, local versions are unrelated to the versions in this API, so clients must partition cached data by server ID. See [Object Versions](https://www.zotero.org/support/dev/web_api/v3/local_api#object_versions).

## Rate Limiting<a href="#rate_limiting" class="headerlink" title="Permanent link">#</a>

Clients accessing the Zotero API should be prepared to handle two forms of rate limiting: backoff requests and hard limiting.

### Backoff<a href="#backoff" class="headerlink" title="Permanent link">#</a>

If the API servers are overloaded, the API may include a `Backoff: <seconds>` HTTP header in responses, indicating that the client should perform the minimum number of requests necessary to maintain data consistency and then refrain from making further requests for the number of seconds indicated. `Backoff` can be included in any response, including successful ones.

### 429 Too Many Requests<a href="#429_too_many_requests" class="headerlink" title="Permanent link">#</a>

If a client has made too many requests within a given time period or is making too many concurrent requests, the API may return `429 Too Many Requests`, potentially with a `Retry-After: <seconds>` header. Clients receiving a `429` should wait at least the number of seconds indicated in the header before making further requests, or to perform an exponential backoff if `Retry-After` isn’t provided. They should also reduce their overall request rate and/or concurrency to avoid repeatedly getting 429s, which may result in stricter throttling or temporary blocks.

For clients repeatedly hitting rate limits, the best solution is often to use a different request flow, such as using [batched writes](https://www.zotero.org/support/dev/web_api/v3/write_requests#updating_multiple_objects) rather individually updating a large number of objects. Clients should also generally make no more than 4 concurrent requests.

`Retry-After` can also be included with `503 Service Unavailable` responses when the server is undergoing maintenance.

## Example GET Requests and Responses<a href="#example_get_requests_and_responses" class="headerlink" title="Permanent link">#</a>

Several examples of read request URLs and their responses:

<table>
<thead>
<tr>
<th colspan="2">Multi-object JSON response: top-level items in a collection</th>
</tr>
</thead>
<tbody>
<tr>
<td>Request</td>
<td>https://api.zotero.org/users/${LIBRARY_ID}/collections/9KH9TNSJ/items/top?v=3</td>
</tr>
<tr>
<td>Response</td>
<td>https://gist.github.com/6eeace93a5c29775d39c</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th colspan="2">Single-object JSON response: individual item</th>
</tr>
</thead>
<tbody>
<tr>
<td>Request</td>
<td>https://api.zotero.org/users/${LIBRARY_ID}/items/X42A7DEE?v=3</td>
</tr>
<tr>
<td>Response</td>
<td>https://gist.github.com/f1030b9609aadc51ddec</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th colspan="2">Multi-object JSON response: collections for a user</th>
</tr>
</thead>
<tbody>
<tr>
<td>Request</td>
<td>https://api.zotero.org/users/${LIBRARY_ID}/collections?v=3</td>
</tr>
<tr>
<td>Response</td>
<td>https://gist.github.com/0bc17ca64ee7d3bc9063</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th colspan="2">Atom feed: items in a library</th>
</tr>
</thead>
<tbody>
<tr>
<td>Request</td>
<td>https://api.zotero.org/users/${LIBRARY_ID}/items?format=atom&amp;v=3</td>
</tr>
<tr>
<td>Response</td>
<td>https://gist.github.com/24172188ea79efa210b5</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th colspan="2">Formatted bibliography: items in a collection</th>
</tr>
</thead>
<tbody>
<tr>
<td>Request</td>
<td>https://api.zotero.org/users/${LIBRARY_ID}/collections/9KH9TNSJ/items?format=bib</td>
</tr>
<tr>
<td>Response</td>
<td>https://gist.github.com/77bc2413cce4c219f862</td>
</tr>
</tbody>
</table>

The [local API](https://www.zotero.org/support/dev/web_api/v3/local_api) does not currently apply rate limiting.

## HTTP Status Codes<a href="#http_status_codes" class="headerlink" title="Permanent link">#</a>

Successful GET requests will return a `200 OK` status code.

[Conditional GET requests](#caching) may return `304 Not Modified`.

For any read or write request, the server may return a `400 Bad Request`, `404 Not Found`, or `405 Method Not Allowed` for an invalid request and `500 Internal Server Error` or `503 Service Unavailable` for a server-related issue. [Authentication](#authentication) errors (e.g., invalid API key or insufficient privileges) will return a `403 Forbidden`.

Passing an `Expect` header, which is unsupported, will result in a `417 Expectation Failed` response.

[Library/object versioning](https://www.zotero.org/support/dev/web_api/v3/syncing#version_numbers) or <a href="/support/dev/web_api/v3/write_requests#zotero_write_token" class="missing-link">Zotero-Write-Token</a> errors will result in `412 Precondition Failed` or `428 Precondition Required`.

`429 Too Many Requests` indicates that the client has been [rate-limited](#rate_limiting).

The [local API](https://www.zotero.org/support/dev/web_api/v3/local_api) returns `403 Forbidden` when the local API preference is not enabled and `501 Not Implemented` when a request asks for something it does not support (Atom output, or an API version other than 3 on an endpoint other than `/api/`). It returns `401 Unauthorized` for a write request without a valid [local API key](https://www.zotero.org/support/dev/web_api/v3/local_api#authorizing_writes), and `412` or `428` for [`Zotero-Server-ID`](https://www.zotero.org/support/dev/web_api/v3/local_api#server_id) errors in addition to the versioning errors above.

## Additional API Documentation<a href="#additional_api_documentation" class="headerlink" title="Permanent link">#</a>

- [Local API](https://www.zotero.org/support/dev/web_api/v3/local_api)
- [Write Requests](https://www.zotero.org/support/dev/web_api/v3/write_requests)
- [File Uploads](https://www.zotero.org/support/dev/web_api/v3/file_upload)
- [Syncing](https://www.zotero.org/support/dev/web_api/v3/syncing)
- [OAuth Authentication](https://www.zotero.org/support/dev/web_api/v3/oauth)
- [Changes from API Version 2](https://www.zotero.org/support/dev/web_api/v3/changes_from_v2)

<div class="aside zotero-docs-toc">

<div class="zotero-docs-toc-title">

On this page

</div>

- [Zotero Web API Documentation](#zotero_web_api_documentation)
  - [Base URL](#base_url)
  - [API Versioning](#api_versioning)
    - [Version Transitions](#version_transitions)
  - [Authentication](#authentication)
  - [Local API](#local_api)
  - [Resources](#resources)
    - [User and Group Library URLs](#user_and_group_library_urls)
      - [Collections](#collections)
      - [Items](#items)
      - [Searches](#searches)
      - [Tags](#tags)
    - [Other URLs](#other_urls)
  - [Read Requests](#read_requests)
    - [General Parameters](#general_parameters)
    - [Parameters for “format=json”](#parameters_for_formatjson)
    - [Parameters for “format=atom”](#parameters_for_formatatom)
    - [Parameters for “format=bib”, “include/content=bib”, “include/content=citation”](#parameters_for_formatbib_includecontentbib_includecontentcitation)
    - [Item Export Formats](#item_export_formats)
  - [Searching](#searching)
    - [Search Parameters](#search_parameters)
    - [Search Parameters (Items Endpoints)](#search_parameters_items_endpoints)
    - [Search Parameters (Tags Endpoints)](#search_parameters_tags_endpoints)
    - [Search Parameters (Tags-Within-Items Endpoints)](#search_parameters_tags-within-items_endpoints)
    - [Search Syntax](#search_syntax)
  - [Sorting and Pagination](#sorting_and_pagination)
    - [Sorting and Pagination Parameters](#sorting_and_pagination_parameters)
      - [Total Results](#total_results)
      - [Link Header](#link_header)
  - [Caching](#caching)
  - [Rate Limiting](#rate_limiting)
    - [Backoff](#backoff)
    - [429 Too Many Requests](#429_too_many_requests)
  - [Example GET Requests and Responses](#example_get_requests_and_responses)
  - [HTTP Status Codes](#http_status_codes)
  - [Additional API Documentation](#additional_api_documentation)

<div class="zotero-docs-page-meta">

<div class="zotero-docs-modified">

Last updated 2026-07-29

</div>

<a href="https://github.com/zotero/zotero-docs/edit/main/content/dev/web_api/v3/basics.md" class="zotero-docs-edit"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgZmlsbD0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSI+PHBhdGggZD0iTTExLjAxMyAxLjQyN2ExLjc1IDEuNzUgMCAwIDEgMi40NzQgMGwxLjA4NiAxLjA4NmExLjc1IDEuNzUgMCAwIDEgMCAyLjQ3NGwtOC42MSA4LjYxYy0uMjEuMjEtLjQ3LjM2NC0uNzU2LjQ0NWwtMy4yNTEuOTNhLjc1Ljc1IDAgMCAxLS45MjctLjkyOGwuOTI5LTMuMjVjLjA4MS0uMjg2LjIzNS0uNTQ3LjQ0NS0uNzU4bDguNjEtOC42MVptLjE3NiA0LjgyM0w5Ljc1IDQuODFsLTYuMjg2IDYuMjg3YS4yNTMuMjUzIDAgMCAwLS4wNjQuMTA4bC0uNTU4IDEuOTUzIDEuOTUzLS41NThhLjI1My4yNTMgMCAwIDAgLjEwOC0uMDY0TDExLjE4OSA2LjI1Wm0yLjk1LTIuMTItMS4wODYtMS4wODZhLjI1LjI1IDAgMCAwLS4zNTQgMGwtMS4wMTIgMS4wMTIgMS40NCAxLjQ0IDEuMDEyLTEuMDEzYS4yNS4yNSAwIDAgMCAwLS4zNTNaIiAvPjwvc3ZnPg==" />Edit on GitHub</a>

</div>

</div>

</div>

</div>
