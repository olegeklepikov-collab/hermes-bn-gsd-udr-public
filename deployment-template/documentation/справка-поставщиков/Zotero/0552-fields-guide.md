> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Zotero: fields-guide

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

# Zotero Item Types and Fields<a href="#zotero_item_types_and_fields" class="headerlink" title="Permanent link">#</a>

This page provides general descriptions of Zotero item types and fields. It can be helpful when entering item data into Zotero manually. The page also provides guidance on ways to store information for unusual item types.

## Item Types<a href="#item_types" class="headerlink" title="Permanent link">#</a>

Item types in Zotero should be regarded as flexible, broad categories. Item types are generally determined based on how items should be cited. See descriptions of Zotero’s item types below. If you are citing an unusual item type that does not perfectly fit one of the supported categories, choose an item type that is reasonably close with an adequate selection of fields (e.g., `Book`, `Report`, or `Manuscript` can be made to fit most unusual item types well).

You can store more specific information about the type of item (e.g., a novel versus a biography book) in the Type, Format, or Extra fields or using [tags](https://www.zotero.org/support/collections_and_tags#tags).

| Item Type | Description |
|----|----|
| Artwork | A piece of artwork (e.g., an oil painting, photograph, or sculpture). Also use this item type for other types of images or visual items (e.g., scientific figures). |
| Audio Recording | Any form of audio recording, including music, spoken word, sound effects, archival recordings, or audio-based scientific figures. |
| Bill | A proposed piece of legislation. |
| Blog Post | An article or entry posted to a personal blog website. For online articles published as part of a larger online publication (e.g., [NYT Blogs](http://www.nytimes.com/interactive/blogs/directory.html)), using `Magazine Article` or `Newspaper Article` generally yields better results. |
| Book | A book or similar published item. For government documents, technical reports, manuals, etc., use `Report` instead. This item type can also be adapted to fit many types of unusual items. |
| Book Section | A section of a book. Usually chapters, but also forewords, prefaces, introductions, appendices, afterwords, comments, etc. |
| Case | A legal case, either published or unpublished. |
| Conference Paper | A paper presented at a conference and subsequently published in a formal conference proceedings publication (e.g., as a book, report, or issue of a journal). For conference papers that have not been published in a proceedings, use `Presentation`. |
| Dataset | A collection of data. |
| Dictionary Entry | An entry published as part of a dictionary. |
| Document | A generic document item. This item type has a poor selection of fields and poor support in citation styles, so it should generally be avoided. |
| E-mail | A message sent via email. This type could also be used for other forms of personal communication. |
| Encyclopedia Article | An article or chapter published as part of an encyclopedia. |
| Film | A film or motion picture. Generally, use this type for artistically-oriented films (including fictional, non-fictional, and documentary films). For other types of video items, use `Video Recording`. |
| Forum Post | A post on an online discussion forum. Also use this type for items such as Facebook posts or tweets. |
| Hearing | A formal hearing or meeting report by a legislative body. |
| Instant Message | A message sent via an instant message or chat service. This type could also be used for other forms of personal communication. |
| Interview | An interview with a person, including recordings, transcripts, or other records of the interview. |
| Journal Article | An article published in a scholarly journal (either print or online). |
| Letter | A letter sent between persons or organizations. This type could also be used for other forms of personal communication. |
| Magazine Article | An article published in a non-scholarly, popular, or trade magazine (either print or online). |
| Manuscript | An unpublished manuscript. Use this type for both historical documents and modern unpublished work (e.g., unpublished manuscripts, manuscripts submitted for publication, working papers that are not widely available). Can also be used for other forms of historical or archival documents. This item type can also be adapted to fit many types of unusual items. |
| Map | A map. Also use this type for geographic models. |
| Newspaper Article | An article published in a newspaper (either print or online). |
| Patent | A patent awarded for an invention. |
| Podcast | A [podcast](https://en.wikipedia.org/wiki/Podcast) (an episode of an audio or video program distributed online, often via subscription). |
| Preprint | A version of a scholarly or scientific paper that precedes formal peer review and publication in a peer-reviewed scholarly or scientific journal. The preprint may be available, often as a non-typeset version available for free, before or after a paper is published in a journal, through institutional repositories or preprint servers. This item type can also be used for working papers. |
| Presentation | A presentation made as part of a conference, meeting, symposium, lecture, etc. This item type refers to the presentation itself, not a written version published as part of a conference proceedings (use `Conference Paper` for such published versions). |
| Radio Broadcast | An audio broadcast, such as a radio news show, an episode of a radio entertainment series, or similar. Includes broadcasts from online radio stations and audio broadcasts archived online (cf. `Podcast`). |
| Report | A report published by an organization, institution, government department, or similar entity. Also used for working papers and preprints distributed through institutional repositories or preprint servers. This item type can also be adapted to fit many types of unusual items. |
| Software | A piece of software, an app, or another computer program. |
| Standard | A published document describing a standard, or a similar set of industrial or governmental specifications. |
| Statute | A law or other piece of enacted legislation. |
| Thesis | A thesis submitted as part of a student applying for a degree (either published or unpublished). |
| TV Broadcast | An episode of a television series. |
| Video Recording | A video recording. Use this type for general video items that do not fit into one of the more specific video item types (e.g., Film, TV Broadcast), such as YouTube videos or video-based scientific figures. |
| Webpage | An online page of a website. When possible, use one of the more specific item types above (e.g., Magazine Article, Blog Post, Report). |
|  |  |
| Attachment | A standalone attachment file (e.g., a PDF, JPEG, DOCX, PPTX, XLSX, or ODT file). Standalone attachment files have limited functionality in Zotero (e.g., they cannot be properly searched or cited). Always [attach files to proper Zotero items](https://www.zotero.org/support/attaching_files#child_versus_standalone_attachment_files). |
| Note | A standalone note. Notes can be used for organizing and annotating in Zotero. If you cite a standalone note, Zotero will use the first 120 characters as the item title (and will treat the note as an author-less and date-less item). Citing notes is not a reliable way to add standalone commentary to a bibliography or reference list. |

For additional legal and historical item types, see [Legal Citations](https://www.zotero.org/support/kb/legal_citations).

## Item Fields<a href="#item_fields" class="headerlink" title="Permanent link">#</a>

Fields included for various item types in Zotero are described below. Fields are organized into categories based on the kinds of items they are most typically associated with. Some fields (e.g., Volume, Series) may also be present for other types of items. Specific meanings of fields for particular item types are noted where necessary.

Fields marked with an asterisk (\*) cannot be used in citations

### General Fields<a href="#general_fields" class="headerlink" title="Permanent link">#</a>

The following fields exist across multiple item types and have the same purpose for all (or nearly all) types.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Item Type</td>
<td>The broad type of item. Item types are generally determined based on how items should be cited. See descriptions of Zotero’s item types above. You can store more specific information about the type of item (e.g., a novel versus a biography book) in the Type, Format, or Extra fields or using <a href="/support/collections_and_tags#tags">tags</a>.</td>
</tr>
<tr class="even">
<td>Creators</td>
<td>The individuals or entities creating or associated with a work. An item can have multiple creators of numerous different kinds. See the list of creator types below.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>The principal title of an item. Should be entered in <a href="/support/kb/sentence_casing">sentence case</a>.</td>
</tr>
<tr class="even">
<td>Abstract</td>
<td>Short description of the work</td>
</tr>
<tr class="odd">
<td>Date</td>
<td>Date of publication. Use "Accessed" for the date an electronic resource was accessed.</td>
</tr>
<tr class="even">
<td>Short Title</td>
<td>Short form of the title, often without the subtitle. Used mostly in footnote styles for subsequent citations</td>
</tr>
<tr class="odd">
<td>Language</td>
<td>The language of publication for an item. We recommend storing these as two letter <a href="http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes">ISO language codes</a> followed by two letter <a href="http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO country codes</a> (e.g., en-US for American English, or de-DE for German).<br />
The Language field is used to determine whether <a href="/support/kb/preventing_title_casing_for_non-english_titles">English Title Casing rules</a> should be applied when formatting item titles. If the stored item data is in English (e.g., for translated titles), enter en-US or en-UK, even if the item content is in another language.</td>
</tr>
</tbody>
</table>

### Fields for Books and Periodicals<a href="#fields_for_books_and_periodicals" class="headerlink" title="Permanent link">#</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Publication</td>
<td>The title of the periodical (journal, magazine, newspaper, etc.) containing the cited item</td>
</tr>
<tr class="even">
<td>Book Title<br />
Dictionary Title<br />
Encyclopedia Title</td>
<td>The title of the book, encyclopedia, or dictionary that a chapter, entry, or other book section is published in.</td>
</tr>
<tr class="odd">
<td>Volume</td>
<td>The volume of a (typically multi-volume) publication an article or chapter is published in. For numeric volumes, enter only a number. If the volume should be cited with a volume title, include the title in this field (e.g,. "2: Organizational Psychology").</td>
</tr>
<tr class="even">
<td>Issue</td>
<td>The issue number of a periodical. Typically, issues start at 1 at the beginning of each year/volume. If a periodical has only a volume number and no issue number, leave this field blank.</td>
</tr>
<tr class="odd">
<td>Pages</td>
<td>The page range of an item that is part of a larger publication. Also to be used for locators or article numbers in e-journals and ebooks.</td>
</tr>
<tr class="even">
<td>Edition</td>
<td>The edition of a work. Where numeric, enter as simple Arabic numeral (i.e., "2" rather than "second").</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Series</td>
<td>Name of a series that contains multiple publications or presentations (e.g., "Cambridge Studies in Comparative Politics", "Special issue on Advances in Personality Assessment").</td>
</tr>
<tr class="odd">
<td>Series Number</td>
<td>The number of an item in a series.</td>
</tr>
<tr class="even">
<td>Series Title</td>
<td>Title of a series of articles <em>within</em> one issue of a journal (e.g., a special section or "From the Cover"). "Section Title" would likely be a more appropriate label. See <a href="http://dtd.nlm.nih.gov/publishing/tag-library/2.2/n-ihv0.html">here</a> for an explanation. For citation purposes, this field is currently equivalent to "Series" and is erroneously used instead of series in some item types (e.g., Audio Recording, Map).</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td># of Volumes</td>
<td>The number of volumes in a collective work.</td>
</tr>
<tr class="odd">
<td># of Pages</td>
<td>The number of pages in a book.</td>
</tr>
<tr class="even">
<td>Section</td>
<td>Section of a newspaper.</td>
</tr>
<tr class="odd">
<td>Place</td>
<td>The place of publication for an item.</td>
</tr>
<tr class="even">
<td>Publisher</td>
<td>The publisher of an item.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Journal Abbr</td>
<td>The abbreviated title of a journal. When using the Zotero Word or LibreOffice plugins, Zotero can automatically abbreviate titles using the MEDLINE list. Use this field to enter abbreviations using other systems or for generating bibliographies outside of a word processor.</td>
</tr>
<tr class="odd">
<td>ISBN</td>
<td>The <a href="http://en.wikipedia.org/wiki/ISBN">International Standard Book Number</a> of a book or other publication.</td>
</tr>
<tr class="even">
<td>ISSN</td>
<td>The <a href="http://en.wikipedia.org/wiki/ISSN">International Standard Serial Number</a> of a periodical or series publication.</td>
</tr>
</tbody>
</table>

### Fields Related to When and How Items Were Accessed<a href="#fields_related_to_when_and_how_items_were_accessed" class="headerlink" title="Permanent link">#</a>

| Field | Description |
|----|----|
| Accessed | Date an electronic resource was accessed. Typically filled automatically. You can enter “today,” “yesterday,” and “tomorrow” to quickly enter the corresponding date. |
| DOI | The [Digital Object Identifier](http://en.wikipedia.org/wiki/Digital_object_identifier) of an item. For items other than journal articles, the DOI can be stored in Extra. See [Citing Fields from Extra](#citing_fields_from_extra) below. |
| URL | URL (web-address) where the full item was accessed. Do not use this field for links to catalog records (e.g., libraries or Google Books) or abstracts—these should be instead added as links. |
|  |  |
| Archive | Mainly for archival resources, the archive where an item was found. Also used for repositories, such as government report databases, institutional repositories, or subject repositories. |
| Loc. in Archive | The location of an item in an archive, such as a box and folder number or other relevant location information from the finding aid. Include the subcollection/call number, box number, and folder number together in this field. For additional tips on citing archival sources in Zotero, see [here](https://web.archive.org/web/20150220133939/http://guides.library.harvard.edu/content.php?pid=535700&sid=4445138). |
|  |  |
| Library Catalog | The catalog or database an item was imported from. This field is used, for example, in the MLA citation style. Uses of this field are broader than actual library catalogs. |
| Call Number | The call number of an item in a library. For citing archival sources, also include the Call Number in `Loc. in Archive` (if applicable). |

### Fields for Reports and Theses<a href="#fields_for_reports_and_theses" class="headerlink" title="Permanent link">#</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Type<br />
Report Type</td>
<td>The type of report (e.g., "Technical report", "CPTO Technical Brief") or thesis (e.g., "Doctoral dissertation", "Ph.D. thesis", "Master thesis"; the word 'thesis' or 'dissertation' should be included where applicable).</td>
</tr>
<tr class="even">
<td>Report Number</td>
<td>The number of a report. Do not include the words "Number", "No.", "Nº", "№", or similar; these will be added automatically by the citation style.</td>
</tr>
<tr class="odd">
<td>Institution<br />
University</td>
<td>The institution publishing a report or the university granting the degree for a thesis.</td>
</tr>
</tbody>
</table>

### Fields for Presentations and Performances<a href="#fields_for_presentations_and_performances" class="headerlink" title="Permanent link">#</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Proceedings Title</td>
<td>The title of the conference proceedings where a conference paper was published.</td>
</tr>
<tr class="even">
<td>Conference Name<br />
Meeting Name</td>
<td>The name of the conference or meeting where a conference paper or presentation was presented.</td>
</tr>
<tr class="odd">
<td>Place</td>
<td>For Presentations, the place where the meeting was held or the presentation was made. For Conference Papers (published in a conference proceedings), use this field for the place where the proceedings was published. If separate locations are needed for the publication place and the location of the conference, leave this field blank and add <code>Event Place</code> and <code>Publisher Place</code> fields to Extra (see <a href="#citing_fields_from_extra">Citing Fields from Extra</a> below).</td>
</tr>
<tr class="even">
<td>Type</td>
<td>The type or format of presentation (e.g., "Poster", "Symposium", "Invited address").</td>
</tr>
</tbody>
</table>

### Fields for Recordings and Broadcasts<a href="#fields_for_recordings_and_broadcasts" class="headerlink" title="Permanent link">#</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Format<br />
File Type</td>
<td>The format of an audio or video recording (e.g. "DVD," "CD," "MP3," etc.).</td>
</tr>
<tr class="even">
<td>Running Time</td>
<td>The running time of any type of recording. Enter with the unit (e.g., 120 mins).</td>
</tr>
<tr class="odd">
<td>Program Title</td>
<td>The title of a radio or TV show of which an episode is part (e.g., "This American Life" or "60 Minutes").</td>
</tr>
<tr class="even">
<td>Episode Number</td>
<td>The episode number of a podcast or TV/radio broadcast.</td>
</tr>
<tr class="odd">
<td>Network</td>
<td>The network broadcasting a TV or radio show.</td>
</tr>
<tr class="even">
<td>Label</td>
<td>The recording label distributing an audio recording in a market.</td>
</tr>
<tr class="odd">
<td>Distributor</td>
<td>The organization distributing a film in a market.</td>
</tr>
<tr class="even">
<td>Studio</td>
<td>The studio producing a video recording.</td>
</tr>
<tr class="odd">
<td>Genre</td>
<td>The genre of film (e.g., "horror").</td>
</tr>
</tbody>
</table>

### Fields for Images, Artwork, and Maps<a href="#fields_for_images_artwork_and_maps" class="headerlink" title="Permanent link">#</a>

|  |  |
|----|----|
| Medium | The type of artwork or figure or the medium it was created with (e.g., "Watercolor painting", "Wood sculpture", "X-ray Crystallograph", "Scatterplot"). |
| Artwork Size | The dimensions of the artwork or figure. |
| Scale | The scale of a map or model. |
| Type | For maps, a description of the specific type or genre of map. |

### Fields for Primary Sources and Personal Communications<a href="#fields_for_primary_sources_and_personal_communications" class="headerlink" title="Permanent link">#</a>

|  |  |
|----|----|
| Medium | For interviews, the format in which an interview was recorded (e.g., "Audio Recording", "Video Recording", "Transcript"). |
| Type | For letters, a description of the specific type or purpose of letter (e.g., "Private correspondence). For manuscripts, a description of the type or status of the manuscript (e.g., "Unpublished manuscript", "Manuscript submitted for publication", "Working paper"). |
| Subject | The title of an email. |

### Fields for Websites<a href="#fields_for_websites" class="headerlink" title="Permanent link">#</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Website Title<br />
Blog Title</td>
<td>The title of the blog or website containing a post or specific web page.</td>
</tr>
<tr class="even">
<td>Forum/Listserv Title</td>
<td>The forum or listserv where a post was made.</td>
</tr>
<tr class="odd">
<td>Website Type</td>
<td>Rarely used. Describes the genre of a webpage such as "personal blog" or "intranet".</td>
</tr>
<tr class="even">
<td>Post Type</td>
<td>A description of the specific type of forum post (e.g., "Tweet" or "Facebook comment").</td>
</tr>
</tbody>
</table>

### Fields for Software<a href="#fields_for_software" class="headerlink" title="Permanent link">#</a>

|  |  |
|----|----|
| Version | The version of a computer program. |
| System | The operating system or platform a computer program is written for. |
| Company | The organization publishing a computer program. |
| Language | The programming language a computer program is written in. *Note that* Computer Program *uses the* `Language` *field differently than other items.* |

### Additional Fields<a href="#additional_fields" class="headerlink" title="Permanent link">#</a>

|  |  |
|----|----|
| Rights\\ | The copyright terms, license, or release status for an item. |
| Date Added | The date and time an item was added in Zotero. This field is filled automatically. |
| Date Modified | The date and time an item was last modified in Zotero. This field is filled and updated automatically. |
| Extra | Free field for storing additional information. You can also store additional variables not included in an item’s fields that can be used when making citations and bibliographies . See [Citing Fields from Extra](#citing_fields_from_extra) below. |

### Fields for Legal Items<a href="#fields_for_legal_items" class="headerlink" title="Permanent link">#</a>

For additional and more flexible support for citing legal materials, see [Legal Citations](https://www.zotero.org/support/kb/legal_citations).

##### Legislation and hearings<a href="#legislation_and_hearings" class="headerlink" title="Permanent link">#</a>

|  |  |
|----|----|
| Name of Act | The full title of a statute. |
| Bill Number | The identification number assigned to a proposed piece of legislation. |
| Code | The name of the code in which a bill or statute is published. |
| Code Volume | The volume number of the code containing a bill or statute. |
| Code Number | The identification number assigned to a piece of legislation in the code in which it is published. |
| Public Law Number | The identification number assigned to an enacted piece of legislation. See [here](https://www.loc.gov/law/help/statutes.php) for more details. |
| Date Enacted | The date a statute was enacted. |
| Section | The section of a bill or statute being cited. |
| Committee | The committee holding a hearing. |
| Document Number | The document identification number assigned to a published transcript or record of a committee hearing. |
| Code Pages | The pages in the code volume containing a bill or statute. |
| Legislative Body\\ | The legislative body (parliament, senate, etc.) debating a bill, holding a hearing, or passing legislation. |
| Session | The session of a legislative body in which a bill was introduced, statute was passed, or hearing was held. |
| History | Resources related to the procedural history of a bill or statute. |

##### Legal cases<a href="#legal_cases" class="headerlink" title="Permanent link">#</a>

|  |  |
|----|----|
| History | Resources related to the procedural history of a legal case. |
| Case Name | The title of a legal case. |
| Court | The court where a legal case was argued. |
| Date Decided | The date a legal case was decided. |
| Docket Number | The docket number assigned to a to-be-heard legal case. |
| Reporter | The reporter in which a legal case is published. |
| Reporter Volume | The volume number of the reporter in which a legal case is published. |
| First Page | The first page of the reporter volume on which a case appears. |

##### Patents<a href="#patents" class="headerlink" title="Permanent link">#</a>

|  |  |
|----|----|
| Country | The country issuing a patent. |
| Assignee | The entity to which a ownership rights for a patent are assigned. |
| Issuing Authority | The authority or office reviewing the application and issuing the patent. |
| Patent Number | The identification number assigned to a patent. |
| Filing Date | The date on which a patent application was filed. |
| Issue Date | The date on which a patent is formally issued. |
| Application Number | The identification number assigned to a patent application. |
| Priority Numbers | The international application number of a patent used for priority rights claims. |
| References | Resources related to the history of a patent. |
| Legal Status | The legal status of a patent or application. |

## Item Creators<a href="#item_creators" class="headerlink" title="Permanent link">#</a>

Creator types marked with an asterisk (\*) cannot be used in citations.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Author</td>
<td>The principal author or creator of a work. Enter authors (and other creators) in the order that they should be cited.<br />
Enter names of persons in two-field (Last/Family, First/Given) mode. Enter names of institutions or organizations in one-field mode.</td>
</tr>
<tr class="even">
<td>Editor</td>
<td>The editor of an item or the broader publication an item is part of (e.g., book, journal). If a distinction is drawn between the textual editor and the managing editor/publishing editor/editorial director (<em>Directeur de la Publication</em> in French), use <code>editor</code> for the textual editor and enter <code>Editorial Director</code> in Extra. See <a href="#citing_fields_from_extra">Citing Fields from Extra</a> below.</td>
</tr>
<tr class="odd">
<td>Series Editor</td>
<td>The overseeing editor of a series of items.</td>
</tr>
<tr class="even">
<td>Translator</td>
<td>The translator of an item. If the same person is both the editor and translator of a work, enter their name as both an Editor and a Translator in separate fields.</td>
</tr>
<tr class="odd">
<td>Contributor*</td>
<td>Other individuals or entities associated with a work that should not be included in citations (e.g., individuals listed after "with" on a book's cover). Used as the <code>author</code> for Hearing items.</td>
</tr>
<tr class="even">
<td>Reviewed Author</td>
<td>The name of the author whose work is being reviewed.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Artist</td>
<td>The creator of a piece of artwork or a figure. The <code>author</code> for Artwork items.</td>
</tr>
<tr class="odd">
<td>Performer</td>
<td>The individual performing on an audio recording. The <code>author</code> for Audio Recording items.</td>
</tr>
<tr class="even">
<td>Composer</td>
<td>The composer of the music on an audio recording.</td>
</tr>
<tr class="odd">
<td>Words By*</td>
<td>The individual who wrote the words in an audio recording (e.g., the lyricist or speechwriter).</td>
</tr>
<tr class="even">
<td>Cast Member*</td>
<td>A member of the cast of a broadcast or performance.</td>
</tr>
<tr class="odd">
<td>Director</td>
<td>The director of a broadcast or recording. The <code>author</code> for Film Recording, Video Recording, Radio Broadcast, and TV Broadcast items.</td>
</tr>
<tr class="even">
<td>Producer*</td>
<td>A producer for a film, recording, or broadcast.</td>
</tr>
<tr class="odd">
<td>Scriptwriter*</td>
<td>The person writing the script for a film or broadcast.</td>
</tr>
<tr class="even">
<td>Podcaster</td>
<td>The host of a podcast. The <code>author</code> for Podcast items.</td>
</tr>
<tr class="odd">
<td>Guest*</td>
<td>A guest on a podcast, radio broadcast, or TV broadcast.</td>
</tr>
<tr class="even">
<td>Cartographer</td>
<td>The principal creator of a map. The <code>author</code> for Map item.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Programmer</td>
<td>The programmer for a computer program. The <code>author</code> for Computer Program items.</td>
</tr>
<tr class="odd">
<td>Presenter</td>
<td>The person giving a presentation. The <code>author</code> for Presentation items.</td>
</tr>
<tr class="even">
<td>Interview With</td>
<td>The person being interviewed. The <code>author</code> for Interview items.</td>
</tr>
<tr class="odd">
<td>Interviewer</td>
<td>The person asking questions during an interview.</td>
</tr>
<tr class="even">
<td>Commenter*</td>
<td>An individual commenting on a blog post.</td>
</tr>
<tr class="odd">
<td>Recipient</td>
<td>The person receiving a letter, email, or message.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Sponsor</td>
<td>The principal author of a bill or piece of legislation. The <code>author</code> for Bill and Legislation items.</td>
</tr>
<tr class="even">
<td>Cosponsor*</td>
<td>Cosponsors or endorsers of a bill or piece of legislation.</td>
</tr>
<tr class="odd">
<td>Counsel*</td>
<td>The counsel arguing a legal case.</td>
</tr>
<tr class="even">
<td>Inventor</td>
<td>The creator of an invention. The <code>author</code> for Patent items.</td>
</tr>
<tr class="odd">
<td>Attorney/Agent*</td>
<td>The attorney or agent representing an inventor when filing a patent.</td>
</tr>
</tbody>
</table>

### Role Labels for Media Creators<a href="#role_labels_for_media_creators" class="headerlink" title="Permanent link">#</a>

For citations to films, recordings, and broadcasts, Zotero currently has limited to support for labeling producers, scriptwriters, and some other Creator roles.

To label directors, leave the main Zotero field blank (or enter the names as Contributor) and enter the director names using `Director` in Extra. See [Citing Fields from Extra](#citing_fields_from_extra) below.

All Creator roles (Director, Producer, Scriptwriter, etc.) can also be labelled by entering the names using the default `author` role for the item (*Performer* for Audio Recording, *Podcaster* for Podcast, and *Director* for Film, Radio Broadcast, TV Broadcast, and Video Recording) and adding the appropriate labels in parentheses after the authors’ first names or last names as appropriate for your citation style—e.g., MacNaughton \|\| Ian (Producer) for APA style. Note that the labels will be rendered verbatim in citations; enter abbreviated terms (e.g., “Prod.”) here as needed.

If the style uses initials for author first/given names, rather than full names (e.g., APA style), if the label contains multiple words (e.g., “Executive Producer” or “Writer & Director”), Zotero will abbreviate the words of the label after the first. To avoid this, type a “Word Joiner” character (Unicode U+2060, printed here between quotes: “⁠”) on either side of each space in the label.

See also [Media Creator Roles](https://www.zotero.org/support/kb/media_creator_roles)

## Additional Item Types and Fields<a href="#additional_item_types_and_fields" class="headerlink" title="Permanent link">#</a>

### Citeable Item Types not Included in Zotero<a href="#citeable_item_types_not_included_in_zotero" class="headerlink" title="Permanent link">#</a>

These item types are not yet formally supported in Zotero. For citation purposes, you can convert an item of a different type to one of these types by entering them in the [Extra field](#citing_fields_from_extra) in the following format:

<div class="codehilite">

    Type: CSL Type

</div>

For example:

<div class="codehilite">

    Type: review-book

</div>

| Item Type | CSL Type | Description |
|----|----|----|
| Figure | `figure` | A figure included in a scientific or academic work. |
| Musical Score | `musical_score` | The written score for a musical work. |
| Pamphlet | `pamphlet` | An informally-published work. Typically smaller and less technical than a Report. |
| Book Review | `review-book` | A review of a book. Enter these as Journal, Magazine, or Newspaper Article, depending on where they were published, by providing a “Reviewed Author” creator. |
| Treaty | `treaty` | A legal treaty between two nations. |

### Citeable Fields not Included in Zotero<a href="#citeable_fields_not_included_in_zotero" class="headerlink" title="Permanent link">#</a>

These item fields are not yet formally supported in Zotero. For citation purposes, you can convert an item of a different type to one of these types by entering them in the [Extra field](#citing_fields_from_extra) in this format:

<div class="codehilite">

    CSL Variable: Value

</div>

For example:

<div class="codehilite">

    PMID: 123456
    Status: in press
    Original Date: 1886-04-01
    Director: Kubrick || Stanley

</div>

| Field | CSL Variable | Description |
|----|----|----|
| PMID | `PMID` | The [PubMed identifier](http://en.wikipedia.org/wiki/PMID#PubMed_identifier). |
| PMCID | `PMCID` | The [PubMed Central identifier](https://en.wikipedia.org/wiki/PubMed_Central#PMCID). |
| Status | `Status` | The publication status of an item (e.g., “forthcoming”, “in press”, “advance online publication”). |
| Submitted Date | `Submitted` | The date an item was submitted for publication. |
| Reviewed Title | `Reviewed Title` | The title of a reviewed work. |
| Chapter Number | `Chapter Number` | The number of the chapter within a book. |
| Archive Place | `Archive Place` | The geographic location of an archive. |
| Event Date | `Event Date` | The date an event took place. Enter in ISO format (year-month-day). |
| Event Place | `Event Place` | The geographic location of an event. |
| Original Date | `Original Date` | The original date an item was published. Enter in ISO format (year-month-day). |
| Original Title | `Original Title` | The original title of a work (e.g., the untranslated title). |
| Original Publisher | `Original Publisher` | The publisher of the original version of an item (e.g., the untranslated version). |
| Original Publisher Place | `Original Publisher Place` | The geographic location of the publisher of the original version of an item (e.g., the untranslated version). |
| Original Author | `Original Author` | A type of Creator. The original creator of a work. |
| Director | `Director` | A type of Creator. The director of a film, recording, or broadcast. In Zotero, “Director” is mapped to CSL author. If you need special labels for directors—”(Dir.)”, enter the `Director` label in Extra. |
| Editorial Director | `Editorial Director` | A type of Creator. The managing editor of a publication (“Directeur de la Publication” in French). |
| Illustrator | `Illustrator` | A type of Creator. The illustrator of a work. |

### Citing Fields from Extra<a href="#citing_fields_from_extra" class="headerlink" title="Permanent link">#</a>

If a Zotero item type is missing fields that are needed for citations, it is possible to add these fields to the Extra field.

Enter each variable on a separate line at the top of the Extra field in the following format:

<div class="codehilite">

    CSL Variable: Value

</div>

For example:

<div class="codehilite">

    DOI: 10.1128/AEM.02591-07
    Original Date: 1824
    PMCID: PMC3531190

</div>

With the exception of Item Type (CSL `Type`) and Date variables (CSL `Issued`, etc.), variables entered in Extra will not override corresponding values entered in proper Zotero fields.

#### Dates<a href="#dates" class="headerlink" title="Permanent link">#</a>

Dates entered in Extra will override the date entered in Zotero’s Date field. Dates must be entered in ISO format (year-month-day). Date ranges can be entered in this format:

<div class="codehilite">

    Issued: 2001-12-15/2001-12-31

</div>

#### Names<a href="#names" class="headerlink" title="Permanent link">#</a>

For Creator variables, separate two-field names entered in Extra with two vertical bar characters (‘\|\|’), like this:

<div class="codehilite">

    Editorial Director: De Gaulle || Charles

</div>

<div class="aside zotero-docs-toc">

<div class="zotero-docs-toc-title">

On this page

</div>

- [Zotero Item Types and Fields](#zotero_item_types_and_fields)
  - [Item Types](#item_types)
  - [Item Fields](#item_fields)
    - [General Fields](#general_fields)
    - [Fields for Books and Periodicals](#fields_for_books_and_periodicals)
    - [Fields Related to When and How Items Were Accessed](#fields_related_to_when_and_how_items_were_accessed)
    - [Fields for Reports and Theses](#fields_for_reports_and_theses)
    - [Fields for Presentations and Performances](#fields_for_presentations_and_performances)
    - [Fields for Recordings and Broadcasts](#fields_for_recordings_and_broadcasts)
    - [Fields for Images, Artwork, and Maps](#fields_for_images_artwork_and_maps)
    - [Fields for Primary Sources and Personal Communications](#fields_for_primary_sources_and_personal_communications)
    - [Fields for Websites](#fields_for_websites)
    - [Fields for Software](#fields_for_software)
    - [Additional Fields](#additional_fields)
    - [Fields for Legal Items](#fields_for_legal_items)
      - [Legislation and hearings](#legislation_and_hearings)
      - [Legal cases](#legal_cases)
      - [Patents](#patents)
  - [Item Creators](#item_creators)
    - [Role Labels for Media Creators](#role_labels_for_media_creators)
  - [Additional Item Types and Fields](#additional_item_types_and_fields)
    - [Citeable Item Types not Included in Zotero](#citeable_item_types_not_included_in_zotero)
    - [Citeable Fields not Included in Zotero](#citeable_fields_not_included_in_zotero)
    - [Citing Fields from Extra](#citing_fields_from_extra)
      - [Dates](#dates)
      - [Names](#names)

<div class="zotero-docs-page-meta">

<div class="zotero-docs-modified">

Last updated 2026-05-18

</div>

<a href="https://github.com/zotero/zotero-docs/edit/main/content/kb/item_types_and_fields.md" class="zotero-docs-edit"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgZmlsbD0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSI+PHBhdGggZD0iTTExLjAxMyAxLjQyN2ExLjc1IDEuNzUgMCAwIDEgMi40NzQgMGwxLjA4NiAxLjA4NmExLjc1IDEuNzUgMCAwIDEgMCAyLjQ3NGwtOC42MSA4LjYxYy0uMjEuMjEtLjQ3LjM2NC0uNzU2LjQ0NWwtMy4yNTEuOTNhLjc1Ljc1IDAgMCAxLS45MjctLjkyOGwuOTI5LTMuMjVjLjA4MS0uMjg2LjIzNS0uNTQ3LjQ0NS0uNzU4bDguNjEtOC42MVptLjE3NiA0LjgyM0w5Ljc1IDQuODFsLTYuMjg2IDYuMjg3YS4yNTMuMjUzIDAgMCAwLS4wNjQuMTA4bC0uNTU4IDEuOTUzIDEuOTUzLS41NThhLjI1My4yNTMgMCAwIDAgLjEwOC0uMDY0TDExLjE4OSA2LjI1Wm0yLjk1LTIuMTItMS4wODYtMS4wODZhLjI1LjI1IDAgMCAwLS4zNTQgMGwtMS4wMTIgMS4wMTIgMS40NCAxLjQ0IDEuMDEyLTEuMDEzYS4yNS4yNSAwIDAgMCAwLS4zNTNaIiAvPjwvc3ZnPg==" />Edit on GitHub</a>

</div>

</div>

</div>

</div>
