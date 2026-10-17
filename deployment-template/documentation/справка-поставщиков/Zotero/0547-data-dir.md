> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Zotero: data-dir

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

# The Zotero Data Directory<a href="#the_zotero_data_directory" class="headerlink" title="Permanent link">#</a>

## Locating Your Zotero Data<a href="#locating_your_zotero_data" class="headerlink" title="Permanent link">#</a>

The easiest and most reliable way to find your Zotero data is by clicking the “Show Data Directory” button in the [Advanced](https://www.zotero.org/support/preferences/advanced) tab of the [Zotero settings](https://www.zotero.org/support/preferences). This will reveal the folder on your computer that contains your Zotero database and attachment files.

### Default Locations<a href="#default_locations" class="headerlink" title="Permanent link">#</a>

Unless you have selected a custom data directory in the [Advanced](https://www.zotero.org/support/preferences/advanced) tab of the Zotero settings, your Zotero data is stored within the following OS-dependent directories:

|                          |                                               |
|--------------------------|-----------------------------------------------|
| **macOS**                | `${USER_HOME}/Zotero`                    |
| **Windows 7 and higher** | `${USER_HOME}\Zotero`                 |
| **Windows XP/2000**      | `${USER_HOME}\Zotero` |
| **Linux**                | `~/Zotero`                                    |

The “Show Data Directory” button will always reveal the data directory currently in use and is the recommended method for finding your data directory. If you’re unable to access the Zotero settings, a search for the file name ‘zotero.sqlite’ can also help you locate the Zotero data directory.

**Older Versions**

##### Zotero 4 for Firefox (2017 and earlier)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><strong>macOS</strong></td>
<td><code>${USER_HOME}/Library/Application Support/Firefox/Profiles/&lt;randomstring&gt;/zotero</code><br />
<span class="small">Note: The ${USER_HOME}/Library folder is hidden by default. To access it, click on your desktop, hold down the Option key, and click the Finder's Go menu, and then select Library from the menu.</span></td>
</tr>
<tr>
<td><strong>Windows 7 and higher</strong></td>
<td><code>${USER_HOME}\AppData\Roaming\Mozilla\Firefox\Profiles\&lt;randomstring&gt;\zotero</code></td>
</tr>
<tr>
<td><strong>Windows XP/2000</strong></td>
<td><code>${USER_HOME}\Application Data\Mozilla\Firefox\Profiles\&lt;randomstring&gt;\zotero</code></td>
</tr>
<tr>
<td><strong>Linux (most distributions)</strong></td>
<td><code>~/.mozilla/firefox/Profiles/&lt;randomstring&gt;/zotero</code></td>
</tr>
</tbody>
</table>

##### Zotero 4 Standalone (2017 and earlier)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><strong>macOS</strong></td>
<td><code>${USER_HOME}/Library/Application Support/Zotero/Profiles/&lt;randomstring&gt;/zotero</code><br />
<span class="small">Note: The ${USER_HOME}/Library folder is hidden by default. To access it, click on your desktop, hold down the Option key, and click the Finder's Go menu, and then select Library from the menu.</span></td>
</tr>
<tr>
<td><strong>Windows 7 and higher</strong></td>
<td><code>${USER_HOME}\AppData\Roaming\Zotero\Zotero\Profiles\&lt;randomstring&gt;\zotero</code></td>
</tr>
<tr>
<td><strong>Windows XP/2000</strong></td>
<td><code>${USER_HOME}\Application Data\Zotero\Profiles\&lt;randomstring&gt;\zotero</code></td>
</tr>
<tr>
<td><strong>Linux (most distributions)</strong></td>
<td><code>~/.zotero/Profiles/&lt;randomstring&gt;/zotero</code></td>
</tr>
</tbody>
</table>

## Data Directory Contents<a href="#data_directory_contents" class="headerlink" title="Permanent link">#</a>

The most important file in the data directory is the `zotero.sqlite` file, which is the database containing the majority of your data: item metadata, notes, tags, etc. When Zotero starts up, it reads the `zotero.sqlite` file in the active data directory.

The directory also contains a `storage` folder with 8-character subfolders (e.g., `N7SMB24A`) containing all of your file attachments, such as PDFs, web snapshots, audio files, or any other files you have imported. (Files that are [linked](https://www.zotero.org/support/attaching_files) are not copied into this subfolder.)

Your data directory will likely contain several other files and folders:

- `zotero.sqlite-wal` and `zotero.sqlite-shm` — temporary database files while Zotero is open. `zotero.sqlite-wal` is normally zeroed when Zotero closes. If Zotero doesn’t shut down cleanly, `zotero.sqlite-wal` may contain recent changes that Zotero will apply at the next startup, so you shouldn’t delete it, and you should keep it with zotero.sqlite when copying the database elsewhere.
- `zotero.sqlite.bak` and `zotero.sqlite.1.bak` — automatic backups of `zotero.sqlite`, made at most once a day by default. On most Mac systems, backups are cloned files (APFS copy-on-write) that don’t take up additional disk space except where the main database has changed.
- `fulltext.sqlite` — indexes of full-text content (attachments, notes, etc.) for faster searching. This file isn’t backed up, because it can be recreated automatically if necessary.
- Folders such as `locate`, `logs`, `pipes`, `styles`, and `translators` that are created automatically at Zotero startup

**Warning**: Before you copy, delete, or move any of these files, be sure that Zotero is closed. Failure to do so before moving these files can damage your data.

## Backing Up Your Zotero Data<a href="#backing_up_your_zotero_data" class="headerlink" title="Permanent link">#</a>

We strongly recommend that you regularly back up your Zotero data directory. While [syncing](https://www.zotero.org/support/sync) is a great way to make sure you can restore your libraries if something happens to your computer, it’s not a complete substitute for a proper backup: the Zotero servers only store the most recent version of your libraries, and it takes just a single (possibly automatic) sync to change the server copy (though some inadvertent changes can be restored from [Zotero’s automatic backups](#restoring_from_the_last_automatic_backup)).

Rather than backing up just your Zotero database, we recommend using a backup utility that automatically backs up your entire hard drive to an external device on a regular basis and keeps incremental backups so that you can restore to a given version. Most modern operating systems offer such functionality (e.g., Time Machine on Macs).

If you really want to back up your Zotero data specifically, [locate your Zotero data](https://www.zotero.org/support/zotero_data#locating_your_zotero_data), close Zotero, and copy your data directory (the *entire folder*, including `zotero.sqlite` and `storage` and the other subfolders) to a backup location, preferably on another storage device. As with all important data, it’s a good idea to back up your Zotero data frequently, which is why we recommend an automated full-system backup instead.

Note that if you’re using “download files as needed” for file syncing, your attachment files may not all exist locally and may not be included in a backup. Zotero Storage provides reliable storage of uploaded files, so you might choose to exclude the `storage` folder from your backup, but if you’d like a local backup of attachments as well, you would need to use “download files at sync time” on one computer and make a backup of the data directory from that computer.

**Warning**: You shouldn’t use export (e.g., to Zotero RDF, BibTeX, or RIS) as a backup method. Exporting and re-importing a library doesn’t produce an exact copy — it will reset Date Added/Modified times and break links to existing citations in word processor documents, along with other potential changes.

## Restoring Your Zotero Data From a Backup<a href="#restoring_your_zotero_data_from_a_backup" class="headerlink" title="Permanent link">#</a>

Between manual backups, automatic backups, and synced data, it’s often possible to restore a lost Zotero library or restore data that was accidentally deleted.

Before following these steps, be sure that [Zotero is looking in the right place for your data](#where_did_my_items_go).

### Restoring Your Zotero Data Using Zotero Syncing<a href="#restoring_your_zotero_data_using_zotero_syncing" class="headerlink" title="Permanent link">#</a>

If you were using Zotero syncing and have an empty local library, you can likely restore your data simply by syncing with your online library. After verifying that your library is correct on zotero.org, simply reenter your username and password in the Sync tab of the Zotero settings and click the Sync button in the toolbar. (Zotero only syncs explicit deletions, so just syncing an empty library won’t overwrite the server data **unless you deleted items manually**.)

If you have a local Zotero library that you want to overwrite, close Zotero and delete the old [Zotero data directory](#locating_your_zotero_data) before syncing. Syncing your database with a different Zotero account will also prompt you to remove the existing local database.

### Restoring Your Zotero Data From a Backup<a href="#restoring_your_zotero_data_from_a_backup_1" class="headerlink" title="Permanent link">#</a>

If you were not using Zotero syncing (or were but don’t want to perform a full sync) and have a backup of your Zotero data directory, you can restore your library by replacing your active data directory with your backed-up data directory.

Open the Advanced tab of the Zotero settings and make a note of the specified path under Data Directory Location. (By default, this will be “Zotero” within your home folder.) Click “Show Data Directory”, which should reveal your active data directory containing zotero.sqlite and possibly a ‘storage’ subdirectory. Close Zotero, change to the parent folder of the active data directory (Cmd-up-arrow on macOS, Alt-up-arrow on Windows), and rename the folder to “Zotero-Old”. Next, copy the data directory from your backup to the original location (e.g., “Zotero”).

When you reopen Zotero, you should see your restored Zotero data.

Once you’ve successfully restored your data, you can delete the “Zotero-Old” folder, but it’s a good idea to keep it for a while until you’re sure your data is correct.

Note that, if you were using Zotero syncing, any changes you made to your library since the backup and subsequently synced to your online library will be applied to your restored database as soon as you sync. If you don’t want that to happen, see the following section.

### Restoring Your Zotero Data From a Backup and Overwriting Synced Changes<a href="#restoring_your_zotero_data_from_a_backup_and_overwriting_synced_changes" class="headerlink" title="Permanent link">#</a>

If you or someone else made unwanted changes to your Zotero library and synced those changes to your online library, you may be able to restore data by using a local backup of your Zotero data directory.

1.  Temporarily disable auto-sync in the Sync tab of the Zotero settings.
2.  Follow the steps in the preceding section to restore from a backup of your Zotero data directory.
3.  Once you see your restored data, were you to sync again, the more recent data in the online library would replace the data you just restored, and you’ll need to take steps to prevent that:
    - If you’re trying to restore a small number of deleted items or notes, you can simply duplicate the items — by right-clicking and choosing “Duplicate Item(s)” — so that the new copies remain even after syncing. You could also make a local change (e.g., adding items to a collection) to trigger a conflict, and then choose the local versions when you sync.
    - If you’re trying to restore deleted collections, you can create duplicate collections and drag items from the old collections to the new ones. When you sync, the old collections will be deleted but the new ones will remain.
    - If many items were affected or collections were deleted, you can use [Replace Online Library](https://www.zotero.org/support/kb/sync_reset_options#replace_online_library) to force Zotero to upload the local version of the library, overwriting previously synced changes. Note that will delete any other changes you’ve made locally since the backup.

If you’re happy with the results, you can re-enable auto-sync and continue working.

### Restoring From the Last Automatic Backup<a href="#restoring_from_the_last_automatic_backup" class="headerlink" title="Permanent link">#</a>

If you make a critical mistake while using Zotero — for example, if you accidentally delete a large set of items — you may be able to revert to the last automatic backup. Note that automatic backups contain only data, not files.

1.  If you’re using syncing, temporarily disable auto-sync in the Sync tab of the Zotero settings.
2.  [Locate your Zotero data](https://www.zotero.org/support/zotero_data#locating_your_zotero_data) and make a backup copy of any zotero.sqlite.bak files. The timestamps of the files may help you determine which file would contain the data you’re trying to restore.
3.  Close Zotero. In your data directory, rename zotero.sqlite to zotero.sqlite.old, rename one of the original .bak files (based on the timestamp) to zotero.sqlite, and restart Zotero. You should now see the backed-up version of your library.
4.  If you were using syncing and the undesired changes were already synced, syncing again now would cause the more recent data in the online library to replace the data you just restored, and you’ll need to take steps to prevent that:
    - If you’re trying to restore deleted collections, you can create duplicate collections and drag items from the old collections to the new ones. When you sync, the old collections will be deleted but the new ones will remain.
    - If you’re trying to restore a small number of deleted items or notes, you can simply duplicate the items — by right-clicking and choosing “Duplicate Item(s)” — so that the new copies remain even after syncing.
    - If many items were affected or collections were deleted, you can use [Replace Online Library](https://www.zotero.org/support/kb/sync_reset_options#replace_online_library) to force Zotero to upload the local version of the library, overwriting previously synced changes.

If you’re happy with the results, you can re-enable auto-sync and continue working. Keep zotero.sqlite.old and your .bak file backups until you’re sure all your data is intact and in sync across all your computers.

### Restoring From the Last Upgrade Backup<a href="#restoring_from_the_last_upgrade_backup" class="headerlink" title="Permanent link">#</a>

When you upgrade to a major new version of Zotero, Zotero will automatically update your database to work with the new version. If you would like to revert to a previous version of Zotero at a later point, you will have to manually replace your database with the automatic backup Zotero made during the upgrade. In most cases this will be the highest-numbered “zotero.sqlite.\[num\].bak” file in your Zotero data directory.

It’s a good idea to make a backup of your entire Zotero data directory before making any changes.

If you have synced your data with the Zotero servers, reverting to a previous version is as simple as reinstalling the previous version, closing Zotero, replacing “zotero.sqlite” in your Zotero data directory with “zotero.sqlite.\[highest-number\].bak”, and restarting Zotero. (Note that if you try to open an upgraded database in an earlier version, Zotero will display an error. Just close Zotero and replace the .sqlite file.) Zotero will then sync from the online library any changes made since you last used the older database.

If you were not using syncing, you may wish to export to Zotero RDF any items added since the database upgrade and then reimport those into the earlier version. [Sorting](https://www.zotero.org/support/sorting) your library by Date Added may help you find such items.

To temporarily disable further updates, go to the Config Editor in the Advanced tab of the Zotero settings and set `app.update.auto` to false. Note that staying on an old version is not a long-term solution, as old versions are no longer supported and may stop syncing or receiving site-compatibility updates at any time. Be sure to post to the Zotero Forums and explain whatever is causing you to downgrade, and make a note to check back periodically to see whether it makes sense for you to re-enable automatic updates.

## Locating Missing Zotero Data<a href="#locating_missing_zotero_data" class="headerlink" title="Permanent link">#</a>

If you open Zotero to find your library blank or missing lots of data, there are a few main possibilities:

- If you were using a very old version of Zotero — from 2017 or earlier — without installing any updates and just upgraded to a newer version of Zotero, see [Missing Data After Zotero 5 Upgrade](https://www.zotero.org/support/kb/data_missing_after_zotero_5_upgrade). Zotero 5 was released many years ago, so this no longer applies to most people.
- If you’re using a different computer from the one where you created the missing data, and your data is also missing in your online library, your data simply hasn’t synced from the computer where you created it. See [Changes Not Syncing](https://www.zotero.org/support/kb/changes_not_syncing).
- If you know you’ve had the data on this computer previously, something may have happened to your previous Zotero database, or Zotero may be looking in the wrong place for your data. Read on for instructions.

To determine what happened to your data on this computer, first locate your current Zotero data directory by going to the [Advanced → Files and Folders](https://www.zotero.org/support/preferences/advanced) section of the Zotero settings and using the “Show Data Directory” button. Take note of the names, sizes, and dates of the files beginning with “zotero.sqlite” in this folder, which are your Zotero database (zotero.sqlite) and automatic database backups (\*.bak). An empty Zotero database will be either approximately 1 MB (~1,000 KB) or 5 MB.

If you see only 1 MB or 5 MB zotero.sqlite files, look in the ‘storage’ folder, if one exists, for folders with dates corresponding with your previous usage of Zotero.

- If you see folders in ‘storage’, this is likely the Zotero data directory you were using previously, but something happened to the zotero.sqlite database outside of Zotero — for example, you might have accidentally deleted zotero.sqlite using system tools while trying to clear disk space. In this case, you can restore your data through backups and/or Zotero syncing:
  1.  Look for larger zotero.sqlite.bak files in the data directory, or look for a larger zotero.sqlite file in any separate backups you have. (It’s not possible to restore your data from the ‘storage’ files alone.) When Zotero starts up, it reads the zotero.sqlite file in the active data directory, so you can try other copies of zotero.sqlite by copying them to that location and filename. Do not try to import an .sqlite file into Zotero via File → “Import…” — it won’t work.
  2.  Whether or not you have a backup, if you’ve been using Zotero syncing, you can sync to pull down all data in your [online library](https://www.zotero.org/mylibrary). If you do have a backup, all data more recent than the backup will be downloaded. If you only have an empty database, all data will be downloaded. In either case, you won’t overwrite data in the online library simply by syncing — syncing doesn’t work that way.
  3.  If you can’t find any other copies of zotero.sqlite and weren’t using Zotero syncing, you’ll unfortunately probably need to recreate your database from scratch. Close Zotero, move the Zotero data directory to your desktop as “Zotero Old”, and restart Zotero to create a new library. You can search for all PDFs within your “Zotero Old” folder and drag them to Zotero, and Zotero will attempt to [retrieve metadata](https://www.zotero.org/support/retrieve_pdf_metadata) for as many of them as possible. You can also extract data from any Word or LibreOffice documents you used with the Zotero word processor plugin by using [Reference Extractor](https://rintze.zelle.me/ref-extractor/), though note that any data you re-import this way won’t be linked to your existing documents.
- If this isn’t the location you were expecting to be using, or if you don’t see a ‘storage’ folder or it’s empty, you’ll need to locate your previous data directory on this computer. Once you find it, either select that data directory from the Zotero settings or, with Zotero closed, rename the current directory (e.g., to “Zotero-Old”) and move your desired Zotero directory to the specified location. If you’re not sure where your most recent Zotero data is located, look for versions of zotero.sqlite or zotero.sqlite.bak larger than 5 MB with appropriate modification times stored elsewhere on your computer and look at the dates of the folders within the ‘storage’ folder.
  - Unless you have a good reason to use a custom data directory location, we strongly recommend using the [default location](#default_locations) in your home directory.
  - When specifying a custom data directory location, keep in mind that Zotero doesn’t move or copy any data. You still need to copy your data into the specified location. Also, when pointing the data directory location to an existing folder, be sure to specify the folder containing zotero.sqlite and ‘storage’, not the ‘storage’ folder.

If you’ve gone through these steps and aren’t sure what to do, post to the Zotero Forums with the following info:

- The names, sizes, and dates of all files beginning with “zotero.sqlite” in your current data directory
- Whether there’s a ‘storage’ folder containing subfolders with dates corresponding to your previous usage of Zotero
- Whether your current data directory is in the default location (“Zotero” in your home folder)
- When you last used Zotero on this computer, and what happened on your computer since then
- What you’ve tried so far

<div class="aside zotero-docs-toc">

<div class="zotero-docs-toc-title">

On this page

</div>

- [The Zotero Data Directory](#the_zotero_data_directory)
  - [Locating Your Zotero Data](#locating_your_zotero_data)
    - [Default Locations](#default_locations)
  - [Data Directory Contents](#data_directory_contents)
  - [Backing Up Your Zotero Data](#backing_up_your_zotero_data)
  - [Restoring Your Zotero Data From a Backup](#restoring_your_zotero_data_from_a_backup)
    - [Restoring Your Zotero Data Using Zotero Syncing](#restoring_your_zotero_data_using_zotero_syncing)
    - [Restoring Your Zotero Data From a Backup](#restoring_your_zotero_data_from_a_backup_1)
    - [Restoring Your Zotero Data From a Backup and Overwriting Synced Changes](#restoring_your_zotero_data_from_a_backup_and_overwriting_synced_changes)
    - [Restoring From the Last Automatic Backup](#restoring_from_the_last_automatic_backup)
    - [Restoring From the Last Upgrade Backup](#restoring_from_the_last_upgrade_backup)
  - [Locating Missing Zotero Data](#locating_missing_zotero_data)

<div class="zotero-docs-page-meta">

<div class="zotero-docs-modified">

Last updated 2026-09-30

</div>

<a href="https://github.com/zotero/zotero-docs/edit/main/content/zotero_data.md" class="zotero-docs-edit"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgZmlsbD0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSI+PHBhdGggZD0iTTExLjAxMyAxLjQyN2ExLjc1IDEuNzUgMCAwIDEgMi40NzQgMGwxLjA4NiAxLjA4NmExLjc1IDEuNzUgMCAwIDEgMCAyLjQ3NGwtOC42MSA4LjYxYy0uMjEuMjEtLjQ3LjM2NC0uNzU2LjQ0NWwtMy4yNTEuOTNhLjc1Ljc1IDAgMCAxLS45MjctLjkyOGwuOTI5LTMuMjVjLjA4MS0uMjg2LjIzNS0uNTQ3LjQ0NS0uNzU4bDguNjEtOC42MVptLjE3NiA0LjgyM0w5Ljc1IDQuODFsLTYuMjg2IDYuMjg3YS4yNTMuMjUzIDAgMCAwLS4wNjQuMTA4bC0uNTU4IDEuOTUzIDEuOTUzLS41NThhLjI1My4yNTMgMCAwIDAgLjEwOC0uMDY0TDExLjE4OSA2LjI1Wm0yLjk1LTIuMTItMS4wODYtMS4wODZhLjI1LjI1IDAgMCAwLS4zNTQgMGwtMS4wMTIgMS4wMTIgMS40NCAxLjQ0IDEuMDEyLTEuMDEzYS4yNS4yNSAwIDAgMCAwLS4zNTNaIiAvPjwvc3ZnPg==" />Edit on GitHub</a>

</div>

</div>

</div>

</div>
