> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Zotero: multiple-profiles

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

# How can I use multiple profiles in Zotero?<a href="#how_can_i_use_multiple_profiles_in_zotero" class="headerlink" title="Permanent link">#</a>

Zotero allows you to create multiple profiles, each with its own settings and associated [data directory](https://www.zotero.org/support/zotero_data). This is an advanced configuration and not recommended for most users, but if you’re familiar with using multiple profiles in Firefox, Zotero works the same way and supports the same command-line flags.

A default profile is created when you first start Zotero. To create an additional profile, start Zotero from the command line and pass the `-P` flag to open the Profile Manager:

### macOS<a href="#macos" class="headerlink" title="Permanent link">#</a>

- Open Terminal via Spotlight or /Applications/Utilities.
- Paste `/Applications/Zotero.app/Contents/MacOS/zotero -P` into the Terminal window.
- Press Return

### Windows<a href="#windows" class="headerlink" title="Permanent link">#</a>

- Open the Run dialog (Search/Cortana → type “Run” → Run (Windows 10) or Start → Run (Windows 7)
- Paste `C:\\Program Files (x86)\\Zotero\\zotero.exe -P`
- Press Enter

### Linux<a href="#linux" class="headerlink" title="Permanent link">#</a>

- Start Zotero via the command line, adding the `-P` command-line flag.

The Profile Manager window should appear, allow you to select, create, and delete Zotero profiles.

When you create a new profile (e.g., “Work”), if there’s already a profile pointing to the default data directory location, Zotero will create a new data directory named after the new profile (e.g., “Zotero Work”) when you first start it. Your original data directory won’t be affected. \[**Note, June 2023:** This seems to currently not always happen. If you see your existing data directory in the new profile, create a new data directory manually and point the new profile to there from the Advanced → Files and Folders pane of the Zotero preferences.\]

You can open a specific profile from the command line with the `-p` flag (e.g., `-p Work`), which may be useful for creating shortcuts that automatically open a given profile. (On a Mac, you can save [an AppleScript with command-line flags embedded](https://superuser.com/a/116237) as an application in Script Editor.)

Additional configuration may be required when running [multiple instances](https://www.zotero.org/support/kb/multiple_instances) of Zotero at a time.

<div class="aside zotero-docs-toc">

<div class="zotero-docs-toc-title">

On this page

</div>

- [How can I use multiple profiles in Zotero?](#how_can_i_use_multiple_profiles_in_zotero)
  - [macOS](#macos)
  - [Windows](#windows)
  - [Linux](#linux)

<div class="zotero-docs-page-meta">

<div class="zotero-docs-modified">

Last updated 2023-06-13

</div>

<a href="https://github.com/zotero/zotero-docs/edit/main/content/kb/multiple_profiles.md" class="zotero-docs-edit"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgZmlsbD0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSI+PHBhdGggZD0iTTExLjAxMyAxLjQyN2ExLjc1IDEuNzUgMCAwIDEgMi40NzQgMGwxLjA4NiAxLjA4NmExLjc1IDEuNzUgMCAwIDEgMCAyLjQ3NGwtOC42MSA4LjYxYy0uMjEuMjEtLjQ3LjM2NC0uNzU2LjQ0NWwtMy4yNTEuOTNhLjc1Ljc1IDAgMCAxLS45MjctLjkyOGwuOTI5LTMuMjVjLjA4MS0uMjg2LjIzNS0uNTQ3LjQ0NS0uNzU4bDguNjEtOC42MVptLjE3NiA0LjgyM0w5Ljc1IDQuODFsLTYuMjg2IDYuMjg3YS4yNTMuMjUzIDAgMCAwLS4wNjQuMTA4bC0uNTU4IDEuOTUzIDEuOTUzLS41NThhLjI1My4yNTMgMCAwIDAgLjEwOC0uMDY0TDExLjE4OSA2LjI1Wm0yLjk1LTIuMTItMS4wODYtMS4wODZhLjI1LjI1IDAgMCAwLS4zNTQgMGwtMS4wMTIgMS4wMTIgMS40NCAxLjQ0IDEuMDEyLTEuMDEzYS4yNS4yNSAwIDAgMCAwLS4zNTNaIiAvPjwvc3ZnPg==" />Edit on GitHub</a>

</div>

</div>

</div>

</div>
