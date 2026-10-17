> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Zotero: collections

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

# Collections and Tags<a href="#collections_and_tags" class="headerlink" title="Permanent link">#</a>

Items in Zotero libraries can be organized with **collections** and **tags**.

**Collections** allow hierarchical organization of items into groups and subgroups. The same item can belong to multiple collections and subcollections in your library at the same time. Collections are useful for filing items in meaningful groups (e.g., items for a particular project, from a specific source, on a specific topic, or for a particular course). You can import items directly to a specific collection or add them to collections after they are already in your library.

**Tags** (often called “keywords” in other contexts) allow for detailed characterization of an item. You can tag items based on their topics, methods, status, ratings, or even based on your own workflow (e.g., “to-read”). Items can have as many tags as you like, and you can filter your library (or a specific collection) to show items having a specific set of one or more tags.

Tags are portable, but collections are not. Copying items between Zotero libraries (My Library and group libraries) will transfer their tags, but not their collection placements. Both organizational methods have unique advantages and features. Experiment with both to see what works best for your own workflow.

## Collections<a href="#collections" class="headerlink" title="Permanent link">#</a>

### The Zotero Collections Model<a href="#the_zotero_collections_model" class="headerlink" title="Permanent link">#</a>

<img src="/support/_media/collections_tree.png" class="align-left" alt="collections_tree.png" />

It is important to understand that items can belong to multiple collections and subcollections. Adding an item to multiple collections **does not duplicate** the item. In this sense, collections are more like music playlists than folders in your computer filesystem. Just as a single song can be added to more than one playlist, a single item in a Zotero library can be added to multiple collections.

The library root — “My Library” for personal libraries or the group name for group libraries — always shows all items in the library, and items are duplicates only if they appear multiple times in that view.

### Creating Collections<a href="#creating_collections" class="headerlink" title="Permanent link">#</a>

<img src="/support/_media/collections_right_click.png" class="align-right" width="300" />

Click the “New Collection…” button (<img src="/support/_media/quick_start/add_collection.png" width="15" />) above the left pane in Zotero to add a new collection. You can also right-click on “My Library” or the name of a Group library and choose “New Collection…” to add a new collection. The new collection will appear as a folder under “My Library” or the selected Group library.

Subcollections can be created by dragging and dropping an existing collection onto another collection or by right-clicking a collection and choosing “New Subcollection…”. You can convert a subcollection into a top-level collection by dragging it to the library root (e.g., “My Library”).

You can drag collections between Zotero libraries in the left pane. If you have editing privileges for the destination library, the collection (and all of its items and subcollections) will be added to the destination library.

### Adding Items to Collections<a href="#adding_items_to_collections" class="headerlink" title="Permanent link">#</a>

New items are automatically saved into the collection selected at the time. When saving from the browser, you can choose a different collection from the popup after clicking the save button.

To add existing items in your library to a collection, select them in the center pane and drag them onto the collection in the left pane. By default, the items will be added to the new collection but won’t be removed from their original location.

To *move* items between collections, hold down Cmd (Mac) or Shift (Windows/Linux) when dragging items to the new collection. Remember that the “My Library” view always shows all items in your library, so you cannot “move” items out of this view. To see only items that do not belong to any collection in your library, open the [Unfiled Items](#unfiled_items) special collection.

### Renaming Collections<a href="#renaming_collections" class="headerlink" title="Permanent link">#</a>

Right-click on the collection and choose “Rename Collection…” to give a collection a new name. Collections are sorted alphabetically in your library. You can use punctuation marks to sort collections to the top of the list.

### Deleting Collections<a href="#deleting_collections" class="headerlink" title="Permanent link">#</a>

Right-click on the collection and choose “Delete Collection…” to remove a collection from your library. Deleting a collection **does not delete** the items in the collection. Items are still accessible by clicking on My Library or the Group library name.

Deleting a collection will also delete its subcollections (but not the items in them).

To delete both the collection and its items, right-click on the collection and choose “Delete Collection and Items…”.

### Removing Items from a Collection<a href="#removing_items_from_a_collection" class="headerlink" title="Permanent link">#</a>

<img src="/support/_media/remove_from_collection_contextmenu.png" class="align-right" width="200" alt="remove_from_collection_contextmenu.png" />

Select a collection in the left Zotero pane, then select the items in the center pane that you want to remove from the collection. Press the Delete key to remove the items from the collection. You can also right-click the selected items and choose “Remove Item(s) from Collection…”. This only removes the items from the selected collection, not from “My Library” or any other collections.

To *delete* an item in a collection, select the items in the collection, right-click on them, and choose “Move Item(s) to Trash…”. When “My Library” or a Group library name is selected in the left Zotero pane, pressing the Delete key will also move items to the trash. When a collection or subcollection is selected, press Cmd/Ctrl-Delete to move the items directly to the trash.

### Identifying Collections an Item is In<a href="#identifying_collections_an_item_is_in" class="headerlink" title="Permanent link">#</a>

See [How can I see what collections my item is in?](https://www.zotero.org/support/kb/collections_containing_an_item)

### Saved Searches<a href="#saved_searches" class="headerlink" title="Permanent link">#</a>

[Saved Searches](https://www.zotero.org/support/searching#saved_searches) are like smart collections. They automatically update to include all the items in your library that meet the search criteria. For example, you can create a “To Read” Saved Search with the criteria `Tag` `is not` `read`. Then, opening the Saved Search will show you all of the items in your library that you haven’t read yet (i.e., the ones without a “read” tag). To mark an item as read, add the “read” tag to it.

### Special Collections<a href="#special_collections" class="headerlink" title="Permanent link">#</a>

#### My Publications<a href="#my_publications" class="headerlink" title="Permanent link">#</a>

<img src="/support/_media/special_collections.png" class="align-right" alt="special_collections.png" />

The [My Publications](https://www.zotero.org/support/my_publications) special collection allows you to share your own research work (including items, notes, and attachment files) publicly with the world. Drag your publications to this collection to launch the My Publication wizard, which will allow you to select which notes, links, and files are shared.

#### Duplicate Items<a href="#duplicate_items" class="headerlink" title="Permanent link">#</a>

The [Duplicate Items](https://www.zotero.org/support/duplicate_detection) special collection shows items that Zotero has identified as potential duplicates. You can use this collection to review and merge duplicate items. For details on how duplicate detection works and how to merge duplicates, see [here](https://www.zotero.org/support/duplicate_detection).

#### Unfiled Items<a href="#unfiled_items" class="headerlink" title="Permanent link">#</a>

Items that are not in any collection can be found in the “Unfiled Items” special collection at the bottom of the collections list in the left Zotero pane. If the “Unfiled Items” collection is not visible, right-click on “My Library” or the Group library name and choose “Show Unfiled Items”.

#### Trash<a href="#trash" class="headerlink" title="Permanent link">#</a>

When you delete an item by pressing Delete (Cmd/Ctrl-Delete in a collection) or by right-clicking and choosing “Move Item(s) to Trash”, they are moved to the Trash special collection. By default, items remain in the Trash for 30 days (you can adjust this period in the [General pane](https://www.zotero.org/support/preferences/general) of Zotero preferences), after which they are deleted permanently. You can restore an item from the Trash to your library by selecting it in the Trash and clicking the “Restore to Library” button (or by right-clicking and choosing “Restore to Library”). You can delete an item permanently by clicking the “Delete Permanently…” button (or by right-clicking and choosing “Delete Item…”.

### Show Items from Subcollections<a href="#show_items_from_subcollections" class="headerlink" title="Permanent link">#</a>

By default, items added to a subcollection do not automatically appear in parent collections. This can be changed by toggling “Show Items from Subcollections” in the View menu. This setting is not currently available in the online library.

## Tags<a href="#tags" class="headerlink" title="Permanent link">#</a>

### The Tag Selector<a href="#the_tag_selector" class="headerlink" title="Permanent link">#</a>

<img src="/support/_media/tag_selector.png" class="align-left" width="200" alt="tag_selector.png" />

The tag selector is located at the bottom of the left Zotero pane. It shows all the tags that have been assigned to the items currently shown in the center pane (i.e., items in the currently selected collection that match the current search). To show all of the tags present in the library, click the multi-color button in the lower-right corner of the tag selection and choose “Display All Tags in This Library”. Tags not assigned to currently shown items are greyed out. You can filter items by their tags by clicking on one more tags in the tag selector. Only items that have all of the selected tags will be shown in the center pane. As you apply filters, the list of tags in the tag selector will be updated to show only the tags assigned to currently visible items. Clicking on a tag a again will deselect it. To deselect all tags at once, click the multi-color button and choose “Deselect All”.

<img src="/support/_media/tag_actions_menu.png" class="align-right" width="400" alt="tag_actions_menu.png" />

The filter box at the bottom of the tag selector can be used to search for tags. Type in the search box to see all tags that match. To go back to viewing all the tags in the collection, press the Escape key or click the “X” button on the right.

### Adding Tags to Items<a href="#adding_tags_to_items" class="headerlink" title="Permanent link">#</a>

To add a tag to an item, select the item in the center Zotero pane, and then click the Tags tab in the right-hand pane. Click the Add button, type the tag name, and type Enter/Return. You can rename a tag by clicking on it and typing the new name. Once you have added the tag it will also appear in the tag selector in the bottom left.

As you type, you will be shown a list of matching existing tags. You can choose a suggested tag using the up and down arrow keys and insert it by pressing Tab or Enter/Return.

You can also drag items to a tag in the tag selector in the bottom left to quickly add the tag to all of those items.

<img src="/support/_media/collections_and_tags/manually_adding.png" class="align-right" width="600" alt="Screenshot of adding a tag" />

### Removing Tags from Items<a href="#removing_tags_from_items" class="headerlink" title="Permanent link">#</a>

To remove a tag from an item, select the item in the items list, click the Tags tab in the right-hand pane, and click the “-” (minus) button next to the tag you want to remove.

You can also hold Cmd (Mac) or Shift (Windows/Linux) while dragging items to a tag in the tag selector in the bottom left to remove the tag from all of those items.

If you’ve [assigned a color](#colored_tags) to a tag, you can also remove the tag from all selected items by pressing the number key associated with that tag on your keyboard.

#### Bulk Editing Tags<a href="#bulk_editing_tags" class="headerlink" title="Permanent link">#</a>

<img src="/support/_media/tag_right_click.png" class="align-right" alt="tag_right_click.png" />

You can use the tag selector to globally rename and delete tags. To rename a tag across all items it is assigned to, right-click the tag in the tag selector and choose “Rename Tag…”. To delete a tag from all items, right-click the tag and choose “Delete Tag…”. You can merge tags by renaming one to have the same name as the other.

### Emoji Tags<a href="#emoji_tags" class="headerlink" title="Permanent link">#</a>

If you use an emoji in a tag, it will be displayed directly in the items list.

### Colored Tags<a href="#colored_tags" class="headerlink" title="Permanent link">#</a>

<img src="/support/_media/colored_tags.png" class="align-left" width="350" alt="colored_tags.png" />

Colored tags appear as small colored squares next to items’ titles in the center pane. Colored tags make it easy to quickly scan your library for tags that have a certain tag. Colored tags are shown at the top of the tag selector and are always visible, even if not assigned to any visible items.

Many people use colored tags for “to read” or “favorite” items.

You can assign a color to a tag by right-clicking on it and choosing “Assign Color…” In the popup window, select a color from the dropdown box and click “Set Color”. You can remove a color from a tag by right-clicking, choosing “Assign Color…”, and clicking “Remove Color”.

<img src="/support/_media/assign_colored_tag.png" class="align-center" width="375" alt="assign_colored_tag.png" />

Each colored tag is also assigned a number, corresponding to its position at the top of the tag selector. You can quickly add or remove a colored tag from selected items by typing the corresponding number key on your keyboard. You can change a colored tag’s number by right-clicking on it, choosing “Assign Color…”, and choosing a new position.

If you use an emoji in a colored tag, the emoji will be displayed directly in place of the colored square. The tag will otherwise behave like a colored tag, showing at the top of the tag selector and being assignable with a number key.

Up to 9 tags can be assigned colors and numbers. For further documentation see [Colored Tags](https://zotero-manual.github.io/tags/#colored-tags).

### Automatic Tags<a href="#automatic_tags" class="headerlink" title="Permanent link">#</a>

<img src="/support/_media/tag_actions_menu.png" class="align-right" width="400" alt="tag_actions_menu.png" />

When items are saved to a Zotero library <a href="/support/adding_items_to_zotero#web_translators" class="missing-link">from the web</a>, tags are sometimes automatically added to items. For example, OPAC library catalogs provide subject headings for their records, which are saved as Zotero tags. Automatic tags behave the same as manually added tags but are marked by a red icon in the “Tags” tab of the right-hand Zotero pane (versus the blue icon for regular tags).

Automatic tags can be hidden from the tag selector by clicking the multi-color button in the lower-right corner of the tag selector and unchecking “Show Automatic”. You can delete all automatic tags from a library by clicking “Delete Automatic Tags in This Library”. To prevent Zotero from adding automatic tags, uncheck “Automatically tag items with keywords and subject headings” in the [General](https://www.zotero.org/support/preferences/general) pane of Zotero preferences.

<div class="aside zotero-docs-toc">

<div class="zotero-docs-toc-title">

On this page

</div>

- [Collections and Tags](#collections_and_tags)
  - [Collections](#collections)
    - [The Zotero Collections Model](#the_zotero_collections_model)
    - [Creating Collections](#creating_collections)
    - [Adding Items to Collections](#adding_items_to_collections)
    - [Renaming Collections](#renaming_collections)
    - [Deleting Collections](#deleting_collections)
    - [Removing Items from a Collection](#removing_items_from_a_collection)
    - [Identifying Collections an Item is In](#identifying_collections_an_item_is_in)
    - [Saved Searches](#saved_searches)
    - [Special Collections](#special_collections)
      - [My Publications](#my_publications)
      - [Duplicate Items](#duplicate_items)
      - [Unfiled Items](#unfiled_items)
      - [Trash](#trash)
    - [Show Items from Subcollections](#show_items_from_subcollections)
  - [Tags](#tags)
    - [The Tag Selector](#the_tag_selector)
    - [Adding Tags to Items](#adding_tags_to_items)
    - [Removing Tags from Items](#removing_tags_from_items)
      - [Bulk Editing Tags](#bulk_editing_tags)
    - [Emoji Tags](#emoji_tags)
    - [Colored Tags](#colored_tags)
    - [Automatic Tags](#automatic_tags)

<div class="zotero-docs-page-meta">

<div class="zotero-docs-modified">

Last updated 2025-07-29

</div>

<a href="https://github.com/zotero/zotero-docs/edit/main/content/collections_and_tags.md" class="zotero-docs-edit"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgZmlsbD0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSI+PHBhdGggZD0iTTExLjAxMyAxLjQyN2ExLjc1IDEuNzUgMCAwIDEgMi40NzQgMGwxLjA4NiAxLjA4NmExLjc1IDEuNzUgMCAwIDEgMCAyLjQ3NGwtOC42MSA4LjYxYy0uMjEuMjEtLjQ3LjM2NC0uNzU2LjQ0NWwtMy4yNTEuOTNhLjc1Ljc1IDAgMCAxLS45MjctLjkyOGwuOTI5LTMuMjVjLjA4MS0uMjg2LjIzNS0uNTQ3LjQ0NS0uNzU4bDguNjEtOC42MVptLjE3NiA0LjgyM0w5Ljc1IDQuODFsLTYuMjg2IDYuMjg3YS4yNTMuMjUzIDAgMCAwLS4wNjQuMTA4bC0uNTU4IDEuOTUzIDEuOTUzLS41NThhLjI1My4yNTMgMCAwIDAgLjEwOC0uMDY0TDExLjE4OSA2LjI1Wm0yLjk1LTIuMTItMS4wODYtMS4wODZhLjI1LjI1IDAgMCAwLS4zNTQgMGwtMS4wMTIgMS4wMTIgMS40NCAxLjQ0IDEuMDEyLTEuMDEzYS4yNS4yNSAwIDAgMCAwLS4zNTNaIiAvPjwvc3ZnPg==" />Edit on GitHub</a>

</div>

</div>

</div>

</div>
