> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Keenable: rate-limits

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


<div id="content-container" class="lg:flex-1 lg:min-w-0" role="main">

<span id="background-color" class="fixed inset-0 bg-background-light dark:bg-background-dark -z-10 pointer-events-none"></span><span class="block absolute dark:hidden inset-0 overflow-hidden pointer-events-none"></span><span class="hidden absolute dark:block inset-0 overflow-hidden pointer-events-none"></span><style data-custom-css-index="0" data-custom-css-path="style.css">/* ==========================================================================
   Keenable web style (Guidelines v3.1), applied to the Mintlify `mint` theme.

   Source of truth: the design kit shipped as `design-docs.md` + the
   "Keenable Docs" mock-up. The short version:

     - Four colours only: White, Keenable Black #2A2A2A, Blue #005CFF,
       Orange #F25F34. Blue is the single working accent; orange is never
       used in product UI. No green/red statuses.
     - One typeface family: Stack Sans, for display and body alike.
       TASA Orbiter for utility labels only. System mono for code.
     - 0px corners everywhere. Circles and pills are the only exceptions.
     - No shadows outside overlays; surfaces are separated by hairlines.
     - Flat backgrounds only — no gradients, blur, or patterns.

   Mintlify exposes most of its theme through CSS variables (`--gray-*`,
   `--rounded-*`, `--tw-prose-*`, `--font-*`), so the bulk of this file is
   token rewiring rather than selector overrides. Mintlify injects this file
   last in the document, so plain `:root` declarations win — `!important` is
   reserved for beating Tailwind utilities and inline styles.
   ========================================================================== */

/* --------------------------------------------------------------------------
   1. Typefaces

   One family, two optical sizes. Google Fonts splits Stack Sans into Headline
   / Text / Notch; this site uses Headline for display (page title, h2-h4,
   card and step titles) and Text for running copy, which is what each face is
   cut for. See `DESIGN.md` -> Typography for the decision and its rationale.
   TASA Orbiter stays a utility face for labels, badges and eyebrows.

   docs.json names both families so Mintlify preloads them, but it only
   requests weights 400-800; the kit leans on Light (300) for body copy. TASA
   Orbiter is not declared in docs.json at all. All three are pulled in here.
   -------------------------------------------------------------------------- */
@import url("https://fonts.googleapis.com/css2?family=Stack+Sans+Headline:wght@300;400;500&family=Stack+Sans+Text:wght@300;400;500&family=TASA+Orbiter:wght@400;500&display=swap");

/* --------------------------------------------------------------------------
   2. Brand tokens (transcribed from the kit's tokens/colors.css)
   -------------------------------------------------------------------------- */
:root {
  --keenable-white: #ffffff;
  --keenable-black: #2a2a2a;
  --keenable-blue: #005cff;

  --blue-background-2: #f5faff;
  --blue-interactive-1: #eaf2ff;
  --blue-interactive-2: #daebff;
  --blue-border-1: #b2d3ff;
  --blue-border-3: #74a6ff;
  --blue-solid-1: #005cff;
  --blue-solid-2: #0151e2;
  --blue-accessible-1: #0a57e8;

  --neutral-background-2: #f9f9f9;
  --neutral-interactive-1: #f0f0f0;
  --neutral-interactive-2: #e8e8e8;
  --neutral-border-1: #d9d9d9;
  --neutral-border-3: #bbbbbb;
  --neutral-solid-1: #8d8d8d;
  --neutral-accessible-1: #646464;
  --neutral-accessible-2: #202020;

  /* Semantic aliases, prefixed so they never collide with Mintlify's own. */
  --k-text-primary: var(--keenable-black);
  --k-text-secondary: var(--neutral-accessible-1);
  --k-text-muted: var(--neutral-solid-1);
  --k-text-link: var(--blue-accessible-1);
  --k-text-link-hover: var(--blue-solid-2);
  --k-hairline: #dddddd;
  --k-border: var(--neutral-border-1);
  --k-border-accent: var(--blue-border-1);
  --k-surface: var(--keenable-white);
  --k-surface-sunken: var(--neutral-background-2);
  --k-surface-quiet: var(--neutral-interactive-1);
  --k-tint-blue: var(--blue-background-2);
  --k-tint-blue-strong: var(--blue-interactive-1);
  --k-accent: var(--keenable-blue);
  --k-accent-hover: var(--blue-solid-2);
  --k-code-bg: var(--keenable-black);
  --k-code-fg: #f5f5f5;
  --k-code-chrome: rgba(255, 255, 255, 0.55);
  --k-code-rule: rgba(255, 255, 255, 0.12);

  --k-font-display: "Stack Sans Headline", -apple-system, BlinkMacSystemFont,
    "Segoe UI", system-ui, sans-serif;
  --k-font-body: "Stack Sans Text", -apple-system, BlinkMacSystemFont,
    "Segoe UI", system-ui, sans-serif;
  --k-font-utility: "TASA Orbiter", -apple-system, BlinkMacSystemFont,
    "Segoe UI", system-ui, sans-serif;
  --k-font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;

  --k-ease: cubic-bezier(0.4, 0, 0.2, 1);
  --k-duration-fast: 120ms;
  --k-duration-base: 220ms;
}

/* The kit has no dark theme, only the "Keenable Black" inverse surface. This
   maps that inverse set onto Mintlify's dark mode. The accent lifts from
   #005CFF to --blue-border-3, which is the lightest blue that still reads as
   the brand accent and clears contrast on #2A2A2A. */
html.dark {
  --k-text-primary: #ffffff;
  --k-text-secondary: #aeafaa;
  --k-text-muted: #8b8d98;
  --k-text-link: var(--blue-border-3);
  --k-text-link-hover: #a3c4ff;
  --k-hairline: rgba(255, 255, 255, 0.2);
  --k-border: rgba(255, 255, 255, 0.25);
  --k-border-accent: var(--blue-border-3);
  --k-surface: var(--keenable-black);
  --k-surface-sunken: #333333;
  --k-surface-quiet: rgba(255, 255, 255, 0.08);
  --k-tint-blue: rgba(0, 92, 255, 0.12);
  --k-tint-blue-strong: rgba(0, 92, 255, 0.2);
  --k-accent: var(--blue-border-3);
  --k-accent-hover: #a3c4ff;
  --k-code-bg: var(--neutral-accessible-2);
}

/* --------------------------------------------------------------------------
   3. Mintlify theme wiring
   -------------------------------------------------------------------------- */

/* 3.1 Fonts. Mintlify feeds `--font-family-*-custom` into `body` and `h1-h6`,
   and `--font-weight-*` into every Tailwind weight utility. Headings resolve
   to Stack Sans Headline, body copy to Stack Sans Text. Capping the scale at
   500 keeps the whole site inside the kit's 300/400/500 range. */
:root {
  --font-family-headings-custom: var(--k-font-display);
  --font-family-body-custom: var(--k-font-body);
  --font-weight-body-custom: 300;
  --font-weight-headings-custom: 400;
  --font-weight-normal: 300;
  --font-weight-medium: 400;
  --font-weight-semibold: 500;
  --font-weight-bold: 500;
}

/* 3.2 Corners. Every Tailwind radius utility in the theme resolves through
   one of these variables, so zeroing them squares the entire UI in one move.
   `--rounded-full` is deliberately left alone: circles and pills stay. */
:root {
  --rounded: 0px;
  --rounded-sm: 0px;
  --rounded-md: 0px;
  --rounded-lg: 0px;
  --rounded-xl: 0px;
  --rounded-2xl: 0px;
  --rounded-3xl: 0px;
  --radius-xl: 0px;
  --button-border-radius: 0px;
  --accordion-radius: 0px;
  --cdt-radius: 0px;
  --frame-placeholder-border-radius: 0px;
  --rounded-search: 0px;
}

/* 3.3 Neutral ramp. Mintlify derives every `*-gray-*` utility from these
   triplets. Light mode follows the kit's neutral ladder; dark mode gets its
   own ramp because the theme reaches for the *same* step numbers on both
   sides (`dark:text-gray-400` is body copy, not muted text). */
:root {
  --gray-50: 252 252 252;
  --gray-100: 240 240 240;
  --gray-200: 217 217 217;
  --gray-300: 187 187 187;
  --gray-400: 141 141 141;
  --gray-500: 100 100 100;
  --gray-600: 74 74 74;
  --gray-700: 42 42 42;
  --gray-800: 42 42 42;
  --gray-900: 42 42 42;
  --gray-950: 32 32 32;
}

html.dark {
  --gray-50: 255 255 255;
  --gray-100: 245 245 245;
  --gray-200: 235 235 235;
  --gray-300: 214 214 214;
  --gray-400: 190 190 190;
  --gray-500: 150 150 150;
  --gray-600: 120 120 120;
  --gray-700: 90 90 90;
  --gray-800: 58 58 58;
  --gray-900: 46 46 46;
  --gray-950: 32 32 32;
}

/* 3.4 Prose palette. */
.prose {
  --tw-prose-body: var(--keenable-black);
  --tw-prose-headings: var(--keenable-black);
  --tw-prose-lead: var(--neutral-accessible-1);
  --tw-prose-links: var(--blue-accessible-1);
  --tw-prose-bold: var(--keenable-black);
  --tw-prose-counters: var(--neutral-solid-1);
  --tw-prose-bullets: var(--neutral-border-3);
  --tw-prose-hr: #dddddd;
  --tw-prose-quotes: var(--keenable-black);
  --tw-prose-quote-borders: var(--neutral-border-1);
  --tw-prose-captions: var(--neutral-solid-1);
  --tw-prose-code: var(--keenable-black);
  --tw-prose-pre-code: #f5f5f5;
  --tw-prose-pre-bg: var(--keenable-black);
  --tw-prose-th-borders: var(--neutral-border-1);
  --tw-prose-td-borders: #dddddd;

  --tw-prose-invert-body: #ffffff;
  --tw-prose-invert-headings: #ffffff;
  --tw-prose-invert-lead: #aeafaa;
  --tw-prose-invert-links: var(--blue-border-3);
  --tw-prose-invert-bold: #ffffff;
  --tw-prose-invert-counters: #8b8d98;
  --tw-prose-invert-bullets: rgba(255, 255, 255, 0.35);
  --tw-prose-invert-hr: rgba(255, 255, 255, 0.2);
  --tw-prose-invert-quotes: #ffffff;
  --tw-prose-invert-quote-borders: rgba(255, 255, 255, 0.25);
  --tw-prose-invert-captions: #8b8d98;
  --tw-prose-invert-code: #ffffff;
  --tw-prose-invert-pre-code: #f5f5f5;
  --tw-prose-invert-pre-bg: var(--neutral-accessible-2);
  --tw-prose-invert-th-borders: rgba(255, 255, 255, 0.25);
  --tw-prose-invert-td-borders: rgba(255, 255, 255, 0.15);
}

/* 3.5 Motion. */
:root {
  --default-transition-duration: var(--k-duration-fast);
  --default-transition-timing-function: var(--k-ease);
  --duration-short: var(--k-duration-fast);
  --duration-long: var(--k-duration-base);
  --timing: var(--k-ease);
}

/* --------------------------------------------------------------------------
   4. Page shell
   -------------------------------------------------------------------------- */

/* 4.1 Header: 60px tall, white, hairline underneath. The sidebar's sticky
   offset and viewport height both read `--mintlify-slot-header-height`, so
   setting it here keeps the two in sync. */
:root {
  --mintlify-slot-header-height: 60px;
}

#navbar .h-16 {
  height: 60px;
}

#navbar-transition {
  border-bottom-color: var(--k-hairline) !important;
  transition: none;
}

/* The wordmark ships as a 737x134 viewBox; 20px tall is the kit's header size. */
.nav-logo,
nav img.nav-logo,
header img.nav-logo {
  height: 20px !important;
  max-height: 20px !important;
  width: auto !important;
}

/* The mock-up puts the section name next to the wordmark, split off by a
   1x20px rule. Mintlify has no slot for it, so it is drawn on the logo link. */
#navbar a.select-none {
  display: inline-flex;
  align-items: center;
}

#navbar a.select-none::after {
  content: "Docs";
  margin-left: 16px;
  padding-left: 17px;
  border-left: 1px solid var(--k-hairline);
  font-size: 14px;
  font-weight: 300;
  letter-spacing: 0.01em;
  line-height: 20px;
  color: var(--k-text-secondary);
}

@media (max-width: 1023px) {
  #navbar a.select-none::after {
    content: none;
  }
}

/* Mintlify centres the search in its own third of the header; the mock-up
   parks it on the right, next to the nav links. Redistributing the three
   header groups moves it there without touching the markup. The fourth
   child is the mobile-only group and is left alone. */
#navbar .h-full.relative.flex-1 > div:first-child {
  flex: 0 0 auto;
}

#navbar .h-full.relative.flex-1 > div:nth-child(2) {
  flex: 1 1 auto;
  justify-content: flex-end;
}

#navbar .h-full.relative.flex-1 > div:nth-child(3) {
  flex: 0 0 auto;
  margin-left: 24px;
}

/* Header search: a 260px pill with an inset hairline, blue on hover. */
#search-bar-entry {
  border-radius: 9999px !important;
  width: 260px;
  font-size: 13px;
  font-weight: 300;
  --tw-ring-color: var(--k-border);
}

#search-bar-entry:hover {
  --tw-ring-color: var(--k-border-accent);
}

#search-bar-entry .flex-none {
  font-family: var(--k-font-utility);
  font-size: 11px;
  font-weight: 400;
  letter-spacing: -0.004em;
}

/* Header CTA ("Sign in"): the kit's primary button — solid blue, square. */
#topbar-cta-button a > span[class*="absolute"] {
  background-color: var(--keenable-blue) !important;
  border-radius: 0 !important;
  opacity: 1 !important;
}

#topbar-cta-button a:hover > span[class*="absolute"] {
  background-color: var(--blue-solid-2) !important;
}

#topbar-cta-button a span,
#topbar-cta-button a svg {
  color: #ffffff !important;
}

/* 4.2 Sidebar: a 264px rail with a hairline on the right, TASA group labels,
   blue active item. */
#sidebar {
  width: 264px;
  border-right: 1px solid var(--k-hairline);
}

#sidebar [data-component-part="scroll-area-viewport"] {
  padding-right: 20px;
}

/* Mintlify fades the top of the rail with a gradient; the kit allows none.
   The 32px spacer it sits on stays, and doubles as the rail's top padding. */
#sidebar [class*="bg-linear-to-b"] {
  background-image: none !important;
}

/* 26px between groups; the first one already has the spacer above it. */
#navigation-items > div {
  margin-top: 26px !important;
}

#navigation-items > div:first-child {
  margin-top: 0 !important;
}

#navigation-items .sidebar-group-header,
#navigation-items .sidebar-title {
  font-family: var(--k-font-utility);
  font-size: 11px !important;
  font-weight: 400 !important;
  letter-spacing: -0.004em;
  line-height: 1.55;
  color: var(--k-text-muted) !important;
}

#navigation-items .sidebar-group-header {
  padding-left: 0;
  margin-bottom: 8px !important;
}

/* The item's left padding is written as an inline style, hence !important. */
#navigation-items li > a {
  font-size: 14px;
  font-weight: 300;
  letter-spacing: 0.01em;
  line-height: 1.5;
  padding: 6px 12px !important;
  color: var(--k-text-primary);
  transition: background-color var(--k-duration-fast) var(--k-ease),
    color var(--k-duration-fast) var(--k-ease);
}

#navigation-items li > a:hover {
  background-color: var(--k-surface-quiet) !important;
  color: var(--k-text-primary);
}

#navigation-items li[data-active] > a {
  font-weight: 500;
  color: var(--k-text-link) !important;
  background-color: var(--k-tint-blue-strong) !important;
  text-shadow: none !important;
}

/* 4.3 "On this page": TASA label, 13px items, blue rule on hover. */
#table-of-contents h2,
#table-of-contents-content > :first-child {
  font-family: var(--k-font-utility);
  font-size: 11px !important;
  font-weight: 400 !important;
  letter-spacing: -0.004em;
  line-height: 1.55 !important;
  color: var(--k-text-muted) !important;
}

#table-of-contents .toc-item > a {
  font-size: 13px;
  font-weight: 300;
  line-height: 1.5;
  color: var(--k-text-secondary);
  border-left: 1px solid transparent;
  transition: color var(--k-duration-fast) var(--k-ease),
    border-color var(--k-duration-fast) var(--k-ease);
}

#table-of-contents .toc-item > a:hover,
#table-of-contents .toc-item[data-active] > a {
  color: var(--k-accent) !important;
  border-left-color: var(--k-accent);
}

/* 4.4 Previous / next footer links. */
[data-component-part="pagination-prev"],
[data-component-part="pagination-next"] {
  border-color: var(--k-border) !important;
}

[data-component-part="pagination-title"] {
  font-size: 15px;
  font-weight: 400;
  color: var(--k-text-link);
}

/* --------------------------------------------------------------------------
   5. Content typography

   The kit's scale: H1 40/0.9 @400, H2 24/1.1 @500, H3 17/1.3 @500,
   body 16/1.5 @300, all with +0.010em tracking on the display and body roles.
   Headings are Stack Sans Headline; every size below inherits Stack Sans Text
   from `--font-family-body-custom` unless it names `--k-font-display`.
   -------------------------------------------------------------------------- */
#page-title {
  font-family: var(--k-font-display);
  font-size: 2.5rem;
  line-height: 0.95;
  font-weight: 400;
  letter-spacing: 0.01em;
  color: var(--k-text-primary);
}

/* The section eyebrow above the title (docs.json -> styling.eyebrows). */
#header .eyebrow {
  font-family: var(--k-font-utility);
  font-size: 12px;
  font-weight: 400 !important;
  letter-spacing: -0.004em;
  line-height: 1.55;
  color: var(--k-text-muted) !important;
}

#header .prose,
#header .prose p {
  font-size: 16px;
  font-weight: 300;
  line-height: 1.5;
  letter-spacing: 0.01em;
  color: var(--k-text-secondary);
}

.mdx-content h2 {
  font-family: var(--k-font-display);
  font-size: 1.5rem;
  line-height: 1.1;
  font-weight: 500;
  letter-spacing: 0.01em;
  margin-top: 2.5rem;
  margin-bottom: 0.75rem;
}

.mdx-content h3 {
  font-family: var(--k-font-display);
  font-size: 1.0625rem;
  line-height: 1.3;
  font-weight: 500;
  letter-spacing: 0;
  margin-top: 1.75rem;
  margin-bottom: 0.5rem;
}

.mdx-content h4 {
  font-family: var(--k-font-display);
  font-size: 0.9375rem;
  line-height: 1.4;
  font-weight: 500;
}

.mdx-content p,
.mdx-content li,
.mdx-content dd,
.mdx-content dt,
.mdx-content blockquote,
.mdx-content span[data-as="p"] {
  font-size: 16px;
  font-weight: 300;
  line-height: 1.5;
  letter-spacing: 0.01em;
}

/* Links: brand blue, never underlined, one step darker on hover. */
.mdx-content a,
.mdx-content a.link,
#header a {
  color: var(--k-text-link);
  text-decoration: none !important;
  transition: color var(--k-duration-fast) var(--k-ease);
}

.mdx-content a:hover,
.mdx-content a.link:hover {
  color: var(--k-text-link-hover);
}

/* Horizontal rules are hairlines, not full-weight borders. */
.mdx-content hr {
  border-color: var(--k-hairline);
}

/* Mintlify pins `strong` to `rgb(var(--gray-900))` with no dark-mode
   counterpart, which would leave bold text unreadable on Keenable Black.
   The weight also comes down from 600 to the kit's 500 ceiling. */
.mdx-content strong,
.mdx-content b {
  font-weight: 500;
  color: var(--k-text-primary);
}

/* --------------------------------------------------------------------------
   6. Code

   docs.json pins `styling.codeblocks` to `dark`, so blocks stay on the
   Keenable Black surface in both themes. The overrides below repaint the
   surface (Shiki writes it as an inline style, hence `!important`) and drop
   the frame, since a dark block already separates itself from the page.
   -------------------------------------------------------------------------- */
[data-component-part="code-block-root"],
[data-component-part="code-block-root"] pre.shiki,
.mdx-content pre.shiki {
  background-color: var(--k-code-bg) !important;
  --shiki-dark-bg: var(--k-code-bg) !important;
}

[data-fade-overlay] {
  --fade-color-light: var(--k-code-bg) !important;
  --fade-color-dark: var(--k-code-bg) !important;
}

/* Keep the dark Shiki palette in light mode too. */
.shiki,
.shiki span {
  color: var(--shiki-dark) !important;
}

.mdx-content pre,
.mdx-content pre code,
[data-component-part="code-block-root"] .font-mono {
  font-family: var(--k-font-mono) !important;
  font-size: 13px !important;
  line-height: 1.7 !important;
}

/* CodeGroup. With `codeblocks: dark` the whole frame renders in the dark
   chrome, so the tab bar rides on the Keenable Black surface and is split
   from the code by the mock-up's 12%-white divider. */
.code-group {
  background-color: var(--k-code-bg) !important;
  border-color: transparent !important;
  padding: 0 !important;
}

.code-group [data-component-part="code-group-tab-bar"] {
  border-bottom: 1px solid var(--k-code-rule);
}

.code-group [role="tab"] {
  font-size: 13px;
  font-weight: 400;
  color: var(--k-code-chrome) !important;
}

.code-group [role="tab"][data-active] {
  color: #ffffff !important;
}

/* The 2px active-tab underline; `bg-primary` would be near-invisible here. */
.code-group [role="tab"] > div[class*="absolute"] {
  background-color: var(--blue-border-3) !important;
  border-radius: 0 !important;
}

.code-group [role="tab"] > div:first-child {
  padding: 4px 10px;
}

.code-group [role="tab"] > div:first-child:hover {
  background-color: rgba(255, 255, 255, 0.08) !important;
  color: #ffffff !important;
}

/* Inline code: flat neutral chip, no radius. */
.mdx-content :not(pre) > code {
  font-family: var(--k-font-mono) !important;
  font-size: 0.85em !important;
  font-weight: 400;
  padding: 1px 6px;
  border-radius: 0;
  background-color: var(--k-surface-quiet);
  color: var(--k-text-primary);
}

.mdx-content :not(pre) > code::before,
.mdx-content :not(pre) > code::after {
  content: none;
}

/* --------------------------------------------------------------------------
   7. Callouts

   The kit forbids the coloured left bar and the green/red status palette.
   Note / Tip / Info sit on the blue tint; Warning falls back to the neutral
   tint rather than yellow, which keeps it distinguishable without leaving
   the four-colour system.
   -------------------------------------------------------------------------- */
.mdx-content .callout {
  border-radius: 0 !important;
  padding: 16px 20px;
  background-color: var(--k-tint-blue) !important;
  border: 1px solid var(--k-border-accent) !important;
}

.mdx-content .callout[class*="yellow"],
.mdx-content .callout[class*="red"],
.mdx-content .callout[class*="orange"],
.mdx-content .callout[class*="green"] {
  background-color: var(--k-surface-sunken) !important;
  border-color: var(--k-border) !important;
}

.mdx-content .callout [data-component-part="callout-icon"] {
  color: var(--k-text-link) !important;
}

.mdx-content .callout[class*="yellow"] [data-component-part="callout-icon"],
.mdx-content .callout[class*="red"] [data-component-part="callout-icon"],
.mdx-content .callout[class*="orange"] [data-component-part="callout-icon"],
.mdx-content .callout[class*="green"] [data-component-part="callout-icon"] {
  color: var(--k-text-secondary) !important;
}

.mdx-content .callout p,
.mdx-content .callout li,
.mdx-content .callout span[data-as="p"] {
  font-size: 14px !important;
  font-weight: 300;
  line-height: 1.5 !important;
  color: var(--k-text-primary);
}

/* --------------------------------------------------------------------------
   8. Cards
   -------------------------------------------------------------------------- */
.mdx-content .card {
  border-radius: 0 !important;
  border: 1px solid var(--k-border) !important;
  background-color: var(--k-surface) !important;
  box-shadow: none !important;
  transition: border-color var(--k-duration-fast) var(--k-ease),
    background-color var(--k-duration-fast) var(--k-ease);
}

.mdx-content .card:hover {
  border-color: var(--k-border-accent) !important;
  background-color: var(--k-tint-blue) !important;
}

.mdx-content [data-component-part="card-content-container"] {
  padding: 24px;
}

.mdx-content [data-component-part="card-title"] {
  font-family: var(--k-font-display);
  font-size: 18px !important;
  font-weight: 500 !important;
  line-height: 1.2;
  color: var(--k-text-primary) !important;
}

.mdx-content [data-component-part="card-content"],
.mdx-content [data-component-part="card-content"] span[data-as="p"] {
  font-size: 14px !important;
  font-weight: 300;
  line-height: 1.5 !important;
  color: var(--k-text-secondary) !important;
}

/* --------------------------------------------------------------------------
   9. Tables
   -------------------------------------------------------------------------- */
/* Prose already draws the rules on `thead` and `tbody tr`; recolouring them
   there rather than adding borders to the cells avoids doubled lines. */
.mdx-content thead {
  border-bottom-color: var(--k-border);
}

.mdx-content tbody tr {
  border-bottom-color: var(--k-hairline);
}

.mdx-content thead th {
  font-family: var(--k-font-utility);
  font-size: 11px !important;
  font-weight: 400 !important;
  letter-spacing: -0.004em;
  line-height: 1.55 !important;
  color: var(--k-text-muted) !important;
  text-transform: none;
  padding: 8px 12px;
}

.mdx-content tbody td {
  font-size: 14px !important;
  font-weight: 300;
  line-height: 1.5 !important;
  padding: 13px 12px;
}

.mdx-content thead th:first-child,
.mdx-content tbody td:first-child {
  padding-left: 0;
}

/* --------------------------------------------------------------------------
   10. API reference

   Mintlify colour-codes HTTP methods (green GET, red DELETE) and hardcodes
   its own blue for POST. The kit allows no green or red, so the pills are
   remapped onto the two sanctioned badge treatments: blue for the methods
   that write, neutral grey for the safe ones.
   -------------------------------------------------------------------------- */
.method-nav-pill > span,
[class*="method"] > span[class*="bg-"] {
  font-family: var(--k-font-utility);
  font-weight: 400 !important;
  letter-spacing: -0.004em;
  border-radius: 0 !important;
  background-color: var(--k-tint-blue-strong) !important;
  color: var(--k-text-link) !important;
}

.method-nav-pill > span[class*="green"],
[class*="method"] > span[class*="green"] {
  background-color: var(--k-surface-quiet) !important;
  color: var(--k-text-secondary) !important;
}
.mdx-content .field {
  border-radius: 0 !important;
  border-color: var(--k-hairline) !important;
}

.mdx-content [data-component-part="field-name"] {
  font-family: var(--k-font-mono);
  font-size: 14px !important;
  font-weight: 400;
  color: var(--k-text-primary) !important;
}

.mdx-content [data-component-part="field-meta"],
.mdx-content [data-component-part="field-info-pill"],
.mdx-content [data-component-part="field-required-pill"] {
  font-family: var(--k-font-utility);
  font-size: 11px !important;
  letter-spacing: -0.004em;
  border-radius: 0 !important;
}

/* "required" ships red and the type pill ships stone; both are pulled back
   onto the kit's blue / neutral badge pair. */
.mdx-content [data-component-part="field-required-pill"] {
  background-color: var(--k-tint-blue-strong) !important;
  color: var(--k-text-link) !important;
}

.mdx-content [data-component-part="field-info-pill"] {
  background-color: var(--k-surface-quiet) !important;
  color: var(--k-text-secondary) !important;
}

.mdx-content [data-component-part="field-content"],
.mdx-content [data-component-part="field-content"] [data-as="p"] {
  font-size: 15px !important;
  font-weight: 300;
  line-height: 1.6 !important;
}

/* --------------------------------------------------------------------------
   11. Steps
   -------------------------------------------------------------------------- */
.mdx-content [data-component-part="step-number"] {
  border-radius: 9999px !important;
  font-family: var(--k-font-utility);
  font-size: 12px !important;
  background-color: var(--k-tint-blue-strong) !important;
  color: var(--k-text-link) !important;
}

.mdx-content [data-component-part="step-line"] {
  background-color: var(--k-hairline) !important;
}

.mdx-content [data-component-part="step-title"] {
  font-family: var(--k-font-display);
  font-size: 17px !important;
  font-weight: 500 !important;
  line-height: 1.3;
}

/* --------------------------------------------------------------------------
   12. Buttons

   Two recipes only. Primary is a solid blue rectangle; secondary is white
   with a neutral hairline that turns blue on hover.
   -------------------------------------------------------------------------- */
.tryit-button,
button.tryit-button,
.tryit-button.bg-\[\#3064E3\] {
  background-color: var(--keenable-blue) !important;
  color: #ffffff !important;
  border-radius: 0 !important;
  font-size: 14px !important;
  font-weight: 400 !important;
}

.tryit-button:hover,
button.tryit-button:hover {
  background-color: var(--blue-solid-2) !important;
}

/* MCP one-click install links (see mcp-server.mdx). */
.install-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin: 1.5rem 0;
}

.install-button,
main .install-button,
article .install-button {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 10px 18px;
  border: 1px solid var(--k-border);
  border-radius: 0;
  background-color: var(--k-surface);
  color: var(--k-text-primary) !important;
  font-size: 14px !important;
  font-weight: 400;
  line-height: 1;
  text-decoration: none !important;
  transition: border-color var(--k-duration-fast) var(--k-ease),
    background-color var(--k-duration-fast) var(--k-ease);
}

.install-button:hover {
  border-color: var(--k-border-accent);
  background-color: var(--k-tint-blue);
  transform: none;
}

.install-button svg {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
}

.install-button span[data-as="p"] {
  font-size: 14px !important;
  font-weight: 400 !important;
  line-height: 1 !important;
}

/* --------------------------------------------------------------------------
   13. Shadows

   The kit allows a shadow on overlays only (the search modal). Everything
   else is separated by a hairline.
   -------------------------------------------------------------------------- */
#navbar .shadow-xs,
#sidebar .shadow-xs,
#content-area .shadow-xs,
.mdx-content .shadow-xs,
.mdx-content .shadow-sm,
.mdx-content .shadow,
.mdx-content .shadow-md,
.mdx-content .shadow-lg {
  box-shadow: none !important;
}
</style>

<div class="flex flex-row-reverse gap-12 box-border w-full pt-[calc(10rem+var(--banner-height,2.5rem))] lg:pt-10">

<div id="content-side-layout" class="hidden xl:flex self-start sticky xl:flex-col max-w-[28rem] z-21 h-[calc(100vh-9.5rem)] top-[9.5rem] [[data-banner-state=visible]_&]:h-[calc(100vh-12rem)] [[data-banner-state=visible]_&]:top-[12rem]">

<div id="table-of-contents-layout" class="z-10 hidden xl:flex box-border max-h-full pl-10 w-[19rem]">

</div>

</div>

<div id="content-area" class="relative grow box-border flex-col w-full mx-auto px-1 lg:pl-[5.7rem] lg:-ml-12 xl:w-[calc(100%-28rem)] lg:max-w-[calc(var(--content-width,100vw)+5.95rem)]" data-empty-page-layout="">

<div id="header" class="header relative leading-none @container/page-header">

<div class="mt-0.5 space-y-2.5">

<div class="eyebrow h-5 text-primary dark:text-primary-light text-sm font-semibold">

Get started

</div>

<div class="flex flex-col sm:flex-row items-start sm:items-center relative gap-2 min-w-0">

# Rate limits

<div id="page-context-menu" class="items-center shrink-0 min-w-[156px] justify-end ml-auto hidden @[520px]/page-header:flex">

<div class="flex items-center gap-2 text-sm text-center font-medium">

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxOCIgaGVpZ2h0PSIxOCIgdmlld2JveD0iMCAwIDE4IDE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgYXJpYS1oaWRkZW49InRydWUiIGNsYXNzPSJzaXplLTQgc2hyaW5rLTAiPjxwYXRoIGQ9Ik0xNC4yNSA1LjI1SDcuMjVDNi4xNDU0MyA1LjI1IDUuMjUgNi4xNDU0MyA1LjI1IDcuMjVWMTQuMjVDNS4yNSAxNS4zNTQ2IDYuMTQ1NDMgMTYuMjUgNy4yNSAxNi4yNUgxNC4yNUMxNS4zNTQ2IDE2LjI1IDE2LjI1IDE1LjM1NDYgMTYuMjUgMTQuMjVWNy4yNUMxNi4yNSA2LjE0NTQzIDE1LjM1NDYgNS4yNSAxNC4yNSA1LjI1WiIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHdpZHRoPSIxLjUiIGxpbmVjYXA9InJvdW5kIiBsaW5lam9pbj0icm91bmQiIC8+PHBhdGggZD0iTTIuODAxMDMgMTEuOTk4TDEuNzcyMDMgNS4wNzM5N0MxLjYxMDAzIDMuOTgwOTcgMi4zNjQwMyAyLjk2Mzk3IDMuNDU2MDMgMi44MDE5N0wxMC4zOCAxLjc3Mjk3QzExLjMxMyAxLjYzMzk3IDEyLjE5IDIuMTYyOTcgMTIuNTI4IDMuMDAwOTciIHN0cm9rZT0iY3VycmVudENvbG9yIiB3aWR0aD0iMS41IiBsaW5lY2FwPSJyb3VuZCIgbGluZWpvaW49InJvdW5kIiAvPjwvc3ZnPg==" class="size-4 shrink-0" /><span class="grid"><span class="invisible col-start-1 row-start-1" aria-hidden="true">Copy page</span><span class="col-start-1 row-start-1">Copy page</span></span>

</div>

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxOCIgaGVpZ2h0PSIxOCIgdmlld2JveD0iMCAwIDE4IDE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGFyaWEtaGlkZGVuPSJ0cnVlIiBmb2N1c2FibGU9ImZhbHNlIiBjbGFzcz0ic2l6ZS0zIHRyYW5zaXRpb24tdHJhbnNmb3JtIHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXI6dGV4dC1ncmF5LTYwMCBkYXJrOnRleHQtZ3JheS02MDAgZGFyazpncm91cC1ob3Zlcjp0ZXh0LWdyYXktNDAwIHNocmluay0wIHJvdGF0ZS05MCI+PHBhdGggZD0iTTYuNSAyLjc1TDEyLjc1IDlMNi41IDE1LjI1IiBzdHJva2U9ImN1cnJlbnRDb2xvciIgd2lkdGg9IjEuNSIgbGluZWNhcD0icm91bmQiIGxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4=" class="size-3 transition-transform text-gray-400 group-hover:text-gray-600 dark:text-gray-600 dark:group-hover:text-gray-400 shrink-0 rotate-90" />

</div>

</div>

</div>

<div class="mt-2 text-lg prose prose-gray dark:prose-invert [&>*]:[overflow-wrap:anywhere]">

How fast you can call search and fetch — the per-second and hourly limits for authenticated and unauthenticated requests, and how they differ from the credit allowance.

</div>

<div id="page-context-menu" class="flex items-center shrink-0 min-w-[156px] mt-3 @[520px]/page-header:hidden">

<div class="flex items-center gap-2 text-sm text-center font-medium">

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxOCIgaGVpZ2h0PSIxOCIgdmlld2JveD0iMCAwIDE4IDE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgYXJpYS1oaWRkZW49InRydWUiIGNsYXNzPSJzaXplLTQgc2hyaW5rLTAiPjxwYXRoIGQ9Ik0xNC4yNSA1LjI1SDcuMjVDNi4xNDU0MyA1LjI1IDUuMjUgNi4xNDU0MyA1LjI1IDcuMjVWMTQuMjVDNS4yNSAxNS4zNTQ2IDYuMTQ1NDMgMTYuMjUgNy4yNSAxNi4yNUgxNC4yNUMxNS4zNTQ2IDE2LjI1IDE2LjI1IDE1LjM1NDYgMTYuMjUgMTQuMjVWNy4yNUMxNi4yNSA2LjE0NTQzIDE1LjM1NDYgNS4yNSAxNC4yNSA1LjI1WiIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHdpZHRoPSIxLjUiIGxpbmVjYXA9InJvdW5kIiBsaW5lam9pbj0icm91bmQiIC8+PHBhdGggZD0iTTIuODAxMDMgMTEuOTk4TDEuNzcyMDMgNS4wNzM5N0MxLjYxMDAzIDMuOTgwOTcgMi4zNjQwMyAyLjk2Mzk3IDMuNDU2MDMgMi44MDE5N0wxMC4zOCAxLjc3Mjk3QzExLjMxMyAxLjYzMzk3IDEyLjE5IDIuMTYyOTcgMTIuNTI4IDMuMDAwOTciIHN0cm9rZT0iY3VycmVudENvbG9yIiB3aWR0aD0iMS41IiBsaW5lY2FwPSJyb3VuZCIgbGluZWpvaW49InJvdW5kIiAvPjwvc3ZnPg==" class="size-4 shrink-0" /><span class="grid"><span class="invisible col-start-1 row-start-1" aria-hidden="true">Copy page</span><span class="col-start-1 row-start-1">Copy page</span></span>

</div>

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxOCIgaGVpZ2h0PSIxOCIgdmlld2JveD0iMCAwIDE4IDE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGFyaWEtaGlkZGVuPSJ0cnVlIiBmb2N1c2FibGU9ImZhbHNlIiBjbGFzcz0ic2l6ZS0zIHRyYW5zaXRpb24tdHJhbnNmb3JtIHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXI6dGV4dC1ncmF5LTYwMCBkYXJrOnRleHQtZ3JheS02MDAgZGFyazpncm91cC1ob3Zlcjp0ZXh0LWdyYXktNDAwIHNocmluay0wIHJvdGF0ZS05MCI+PHBhdGggZD0iTTYuNSAyLjc1TDEyLjc1IDlMNi41IDE1LjI1IiBzdHJva2U9ImN1cnJlbnRDb2xvciIgd2lkdGg9IjEuNSIgbGluZWNhcD0icm91bmQiIGxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4=" class="size-3 transition-transform text-gray-400 group-hover:text-gray-600 dark:text-gray-600 dark:group-hover:text-gray-400 shrink-0 rotate-90" />

</div>

</div>

<div id="content" class="mdx-content @container/columns-container relative mt-8 prose prose-gray dark:prose-invert [contain:inline-size] isolate empty:hidden mb-14" data-page-title="Rate limits" data-page-href="/rate-limits">

<span data-as="p">Keenable applies rate limits across search and fetch endpoints in accordance with the authentication status of the request. To learn more about authentication, see <a href="/authentication" class="link">authentication</a>.</span>

<div class="min-w-0 [--page-padding:20px] flex w-[calc(100%+(var(--page-padding)*2))] my-[1em] py-[1em] -mx-(--page-padding) max-w-none [contain:inline-size]" role="presentation" style="position:relative;--scroll-area-corner-height:0px;--scroll-area-corner-width:0px" data-component-part="scroll-area" data-table-wrapper="true">

<div class="size-full rounded-[inherit] [--scroll-area-fade-size:32px] overflow-y-hidden! base-ui-disable-scrollbar" role="region" data-id="base-ui-_R_pbb9qnpfb39p7b9snpfiutb_-viewport" tabindex="-1" style="overflow:scroll" data-component-part="scroll-area-viewport" aria-label="Scrollable table">

<div class="flex" role="presentation" style="min-width:fit-content" data-component-part="scroll-area-content">

<div class="px-(--page-padding) grow max-w-none table">

| Authentication status | Rate limit |
|----|----|
| Authenticated | 10 requests per second (per organization) |
| Unauthenticated | 1,000 requests per hour, max 10 requests per second (per IP) |
| <a href="/pay-per-request" class="link">Pay per request</a> (x402) | 50 paid requests per second per paying wallet, 100 requests per second per IP, no hourly cap |

</div>

</div>

</div>

</div>

<span data-as="p">A few things worth keeping in mind:</span>

- Rate limits on authenticated requests are applied on the organization-level.
- Authentication removes the hourly request cap; the per-second limit still applies.
- Higher per-second limits are available on some plans.
- The unauthenticated pool is shared per IP address, so its available headroom depends on other traffic from the same address.
- On the pay-per-request paths, the per-IP limit counts both the unpaid request that returns the offer and the paid retry, which is why it is twice the per-wallet limit.

<span data-as="p">To increase rate limits on the authenticated tier, please <a href="https://keenable.ai/contact" class="link" target="_blank" rel="noreferrer">talk to us</a>.</span> <span data-as="p">Rate limits cap how *fast* you can call the API. How *much* you can call it is a separate limit: authenticated usage draws on a free allowance of 100,000 requests a month — see <a href="/credits" class="link">credits</a>.</span>

</div>

<a href="/authentication" class="group flex items-center min-w-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary dark:focus-visible:outline-primary-light gap-3 rounded-sm pagination-prev" rel="prev" aria-label="Previous: Authentication" data-component-part="pagination-prev"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMyA2IiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1jb21wb25lbnQtcGFydD0icGFnaW5hdGlvbi1jaGV2cm9uIiBjbGFzcz0iaC0xLjUgc2hyaW5rLTAgc3Ryb2tlLWdyYXktNDAwIG92ZXJmbG93LXZpc2libGUgZ3JvdXAtaG92ZXI6c3Ryb2tlLWdyYXktNjAwIGRhcms6Z3JvdXAtaG92ZXI6c3Ryb2tlLWdyYXktMzAwIj48cGF0aCBkPSJNMyAwTDAgM0wzIDYiIGZpbGw9Im5vbmUiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPjwvc3ZnPg==" class="h-1.5 shrink-0 stroke-gray-400 overflow-visible group-hover:stroke-gray-600 dark:group-hover:stroke-gray-300" /></a>

<div class="truncate group-hover:text-gray-900 dark:group-hover:text-white" data-component-part="pagination-title">

Authentication

</div>

<a href="/credits" class="group flex items-center min-w-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary dark:focus-visible:outline-primary-light gap-3 rounded-sm ml-auto pagination-next" rel="next" aria-label="Next: Credits" data-component-part="pagination-next"></a>

<div class="truncate group-hover:text-gray-900 dark:group-hover:text-white" data-component-part="pagination-title">

Credits

</div>

<img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMyA2IiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1jb21wb25lbnQtcGFydD0icGFnaW5hdGlvbi1jaGV2cm9uIiBjbGFzcz0iaC0xLjUgc2hyaW5rLTAgc3Ryb2tlLWdyYXktNDAwIG92ZXJmbG93LXZpc2libGUgZ3JvdXAtaG92ZXI6c3Ryb2tlLWdyYXktNjAwIGRhcms6Z3JvdXAtaG92ZXI6c3Ryb2tlLWdyYXktMzAwIHJvdGF0ZS0xODAiPjxwYXRoIGQ9Ik0zIDBMMCAzTDMgNiIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+" class="h-1.5 shrink-0 stroke-gray-400 overflow-visible group-hover:stroke-gray-600 dark:group-hover:stroke-gray-300 rotate-180" />

<div class="left-0 right-0 sticky bottom-0 w-full overflow-hidden z-20 pointer-events-none print:hidden invisible" data-assistant-bar="" aria-hidden="true" data-inert="">

<div class="chat-assistant-floating-input w-full group/assistant-bar relative before:content-[""] before:absolute before:left-0 before:right-0 before:top-[calc(50%-0.5rem)] sm:before:top-[calc(50%-0.75rem)] before:h-[200px] before:bg-background-light dark:before:bg-background-dark translate-y-[100px] opacity-0">

<div class="relative pb-4 sm:pb-6">

<div class="flex flex-col w-full rounded-2xl pointer-events-auto bg-background-light dark:bg-background-dark border border-gray-200 dark:border-white/10 focus-within:border-primary dark:focus-within:border-primary-light transition-colors cursor-pointer">

<div class="relative flex items-end">

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxOCIgaGVpZ2h0PSIxOCIgdmlld2JveD0iMCAwIDE4IDE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGFyaWEtaGlkZGVuPSJ0cnVlIiBjbGFzcz0ic2l6ZS0yLjUgc2hyaW5rLTAgdGV4dC13aGl0ZSBkYXJrOnRleHQtd2hpdGUiPjxwYXRoIGQ9Ik05LjAgMS41NzU0TDguOTk5OSAxNi40MTcxIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgd2lkdGg9IjEuNSIgbGluZWNhcD0icm91bmQiIGxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi4yNTYzIDguMzE5TDguOTk5OSAxLjU3NTRMMTUuNzQzNSA4LjMxOTEiIHN0cm9rZT0iY3VycmVudENvbG9yIiB3aWR0aD0iMS41IiBsaW5lY2FwPSJyb3VuZCIgbGluZWpvaW49InJvdW5kIiAvPjwvc3ZnPg==" class="size-2.5 shrink-0 text-white dark:text-white" />

</div>

</div>

</div>

</div>

</div>

<div class="flex gap-6 flex-wrap">

<a href="https://x.com/keenableai" class="h-fit" target="_blank" rel="noopener noreferrer"><span class="sr-only">x</span><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZm9yY2VkLWNvbG9yczpmb3JjZWQtY29sb3ItYWRqdXN0LW5vbmUgZm9yY2VkLWNvbG9yczpiZy1bY29sb3I6Q2FudmFzVGV4dF0hIHctNSBoLTUgYmctZ3JheS00MDAgZGFyazpiZy1ncmF5LTUwMCBob3ZlcjpiZy1ncmF5LTUwMCBkYXJrOmhvdmVyOmJnLWdyYXktNDAwIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZm9jdXNhYmxlPSJmYWxzZSIgc3R5bGU9Ii13ZWJraXQtbWFzay1pbWFnZTp1cmwoJnF1b3Q7aHR0cHM6Ly9kM2drMmM1eGltMWplMi5jbG91ZGZyb250Lm5ldC9mb250YXdlc29tZS92Ny4yLjAvYnJhbmRzL3gtdHdpdHRlci5zdmcmcXVvdDspOy13ZWJraXQtbWFzay1yZXBlYXQ6bm8tcmVwZWF0Oy13ZWJraXQtbWFzay1wb3NpdGlvbjpjZW50ZXI7bWFzay1pbWFnZTp1cmwoJnF1b3Q7aHR0cHM6Ly9kM2drMmM1eGltMWplMi5jbG91ZGZyb250Lm5ldC9mb250YXdlc29tZS92Ny4yLjAvYnJhbmRzL3gtdHdpdHRlci5zdmcmcXVvdDspO21hc2stcmVwZWF0Om5vLXJlcGVhdDttYXNrLXBvc2l0aW9uOmNlbnRlciI+PC9zdmc+" class="forced-colors:forced-color-adjust-none forced-colors:bg-[color:CanvasText]! w-5 h-5 bg-gray-400 dark:bg-gray-500 hover:bg-gray-500 dark:hover:bg-gray-400" /></a>

</div>

<div class="flex items-center justify-between">

<div class="sm:flex">

<a href="https://www.mintlify.com?utm_campaign=poweredBy&amp;utm_medium=referral&amp;utm_source=keenableai" class="group flex items-baseline gap-1 text-sm text-gray-400 dark:text-gray-500 hover:text-gray-600 dark:hover:text-gray-300 text-nowrap" target="_blank" rel="noreferrer"><span>Powered by</span><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI3NCIgaGVpZ2h0PSIzNjciIHZpZXdib3g9IjAgMCAxMjc0IDM2NyIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iaC0zLjUgdy1hdXRvIHRyYW5zbGF0ZS15LTAuNzUiPjxwYXRoIGQ9Ik0xMTU0LjM4IDM2Ni4wMzhIMTA5Ny44NkwxMTM3LjY5IDI3Ni4xNEwxMDU4LjA0IDk3LjEwNDZIMTExNC45M0wxMTYxLjM1IDIwOS4zMzdDMTE2Mi45NyAyMTMuMjYgMTE2OC41MyAyMTMuMjUzIDExNzAuMTQgMjA5LjMyNUwxMjE2LjIxIDk3LjEwNDZIMTI3My40OUwxMTU0LjM4IDM2Ni4wMzhaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PHBhdGggZD0iTTk4Mi43MTQgMjg2Ljc2MVYxNDIuNjIySDk0NC40MDNWOTcuMTA0MUg5ODIuNzE0VjcyLjQ0ODhDOTgyLjcxNCA0OS45NDI5IDk4OS41NDIgMzIuMjQxNiAxMDAzLjIgMTkuMzQ1QzEwMTYuODUgNi40NDgzMiAxMDM0LjE3IDAgMTA1NS4xNiAwQzEwNjguMDYgMCAxMDc5LjA2IDEuMzkwODEgMTA4OC4xNiA0LjE3MjQ0VjUwLjA2OTNDMTA4Mi4wOSA0Ny43OTM0IDEwNzUuMDEgNDYuNjU1NSAxMDY2LjkyIDQ2LjY1NTVDMTA1NS41NCA0Ni42NTU1IDEwNDcuMzIgNDkuMTg0MyAxMDQyLjI3IDU0LjI0MThDMTAzNy4yMSA1OS4wNDY0IDEwMzQuNjggNjcuMjY0OCAxMDM0LjY4IDc4Ljg5NzFWOTcuMTA0MUgxMDg4LjE2VjE0Mi42MjJIMTAzNC42OFYyODYuNzYxSDk4Mi43MTRaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PHBhdGggZD0iTTg5Ny45MTYgNjYuMDAwNUM4ODkuMDY2IDY2LjAwMDUgODgxLjM1MyA2Mi44Mzk1IDg3NC43NzggNTYuNTE3NkM4NjguMjAzIDQ5Ljk0MjkgODY0LjkxNiA0Mi4xMDM3IDg2NC45MTYgMzMuMDAwMkM4NjQuOTE2IDIzLjg5NjcgODY4LjIwMyAxNi4xODQgODc0Ljc3OCA5Ljg2MjE1Qzg4MS4zNTMgMy4yODczOCA4ODkuMDY2IDAgODk3LjkxNiAwQzkwNy4yNzMgMCA5MTUuMTEyIDMuMjg3MzggOTIxLjQzNCA5Ljg2MjE1QzkyOC4wMDggMTYuMTg0IDkzMS4yOTYgMjMuODk2NyA5MzEuMjk2IDMzLjAwMDJDOTMxLjI5NiA0Mi4xMDM3IDkyOC4wMDggNDkuOTQyOSA5MjEuNDM0IDU2LjUxNzZDOTE1LjExMiA2Mi44Mzk1IDkwNy4yNzMgNjYuMDAwNSA4OTcuOTE2IDY2LjAwMDVaTTg3Mi4xMjMgMjg2Ljc2MVY5Ny4xMDQxSDkyNC4wODlWMjg2Ljc2MUg4NzIuMTIzWiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjxwYXRoIGQ9Ik03ODEuNjM4IDI4Ni43NjFWMi4yNzYwOUg4MzMuNjA0VjI4Ni43NjFINzgxLjYzOFoiIGZpbGw9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNNzIyLjkzNCAyODkuMDM3QzcwMS42OTMgMjg5LjAzNyA2ODQuMjQ0IDI4My4yMjEgNjcwLjU4OSAyNzEuNTg4QzY1Ny4xODcgMjU5LjcwMyA2NTAuNDg1IDI0Mi42MzQgNjUwLjQ4NSAyMjAuMzgxVjE0Mi42MjJINjEyLjE3NVY5Ny4xMDQ0SDY1MC40ODVWNDQuMzc5OUg3MDIuNDUxVjk3LjEwNDRINzU1LjkzNFYxNDIuNjIySDcwMi40NTFWMjEwLjE0QzcwMi40NTEgMjIxLjc3MiA3MDQuOTggMjMwLjExNyA3MTAuMDM4IDIzNS4xNzRDNzE1LjA5NSAyMzkuOTc5IDcyMy4zMTMgMjQyLjM4MSA3MzQuNjkzIDI0Mi4zODFDNzQyLjc4NSAyNDIuMzgxIDc0OS44NjUgMjQxLjI0MyA3NTUuOTM0IDIzOC45NjdWMjg0Ljg2NEM3NDYuODMxIDI4Ny42NDYgNzM1LjgzMSAyODkuMDM3IDcyMi45MzQgMjg5LjAzN1oiIGZpbGw9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNNDE3LjY3NCAyODYuNzYxVjk3LjEwNDFINDY5LjY0VjExMC45NjdDNDY5LjY0IDExMy4zMTEgNDcyLjgzIDExNC4zNDcgNDc0LjM4MiAxMTIuNTkxQzQ4NS45NjcgOTkuNDg0OCA1MDIuNDY3IDkyLjkzMTcgNTIzLjg4MSA5Mi45MzE3QzU0Ni42NCA5Mi45MzE3IDU2NC40NjggMTAwLjUxOCA1NzcuMzY1IDExNS42OUM1OTAuNTE0IDEzMC42MSA1OTcuMDg5IDE1MC41ODcgNTk3LjA4OSAxNzUuNjIyVjI4Ni43NjFINTQ1LjEyM1YxODQuMzQ2QzU0NS4xMjMgMTcwLjQzOCA1NDIuMjE1IDE1OS42OTEgNTM2LjM5OSAxNTIuMTA1QzUzMC41ODMgMTQ0LjI2NSA1MjIuMzY0IDE0MC4zNDYgNTExLjc0MyAxNDAuMzQ2QzQ5OS4xIDE0MC4zNDYgNDg4Ljg1OCAxNDQuODk4IDQ4MS4wMTkgMTU0LjAwMUM0NzMuNDMzIDE2My4xMDUgNDY5LjY0IDE3Ni41MDcgNDY5LjY0IDE5NC4yMDhWMjg2Ljc2MUg0MTcuNjc0WiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjxwYXRoIGQ9Ik0zNTIuOTgxIDY2LjAwMDVDMzQ0LjEzIDY2LjAwMDUgMzM2LjQxNyA2Mi44Mzk1IDMyOS44NDMgNTYuNTE3NkMzMjMuMjY4IDQ5Ljk0MjkgMzE5Ljk4IDQyLjEwMzcgMzE5Ljk4IDMzLjAwMDJDMzE5Ljk4IDIzLjg5NjcgMzIzLjI2OCAxNi4xODQgMzI5Ljg0MyA5Ljg2MjE1QzMzNi40MTcgMy4yODczOCAzNDQuMTMgMCAzNTIuOTgxIDBDMzYyLjMzNyAwIDM3MC4xNzYgMy4yODczOCAzNzYuNDk4IDkuODYyMTVDMzgzLjA3MyAxNi4xODQgMzg2LjM2IDIzLjg5NjcgMzg2LjM2IDMzLjAwMDJDMzg2LjM2IDQyLjEwMzcgMzgzLjA3MyA0OS45NDI5IDM3Ni40OTggNTYuNTE3NkMzNzAuMTc2IDYyLjgzOTUgMzYyLjMzNyA2Ni4wMDA1IDM1Mi45ODEgNjYuMDAwNVpNMzI3LjE4NyAyODYuNzYxVjk3LjEwNDFIMzc5LjE1M1YyODYuNzYxSDMyNy4xODdaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PHBhdGggZD0iTTIzOC45NjcgMjg2Ljc2MVYxODUuNDg0QzIzOC45NjcgMTU1LjM5MiAyMjkuMTA1IDE0MC4zNDYgMjA5LjM4MSAxNDAuMzQ2QzE5OC4wMDEgMTQwLjM0NiAxODguODk4IDE0NC42NDUgMTgyLjA3IDE1My4yNDJDMTc1LjQ5NSAxNjEuODQgMTcxLjk1NSAxNzQuNjEgMTcxLjQ0OSAxOTEuNTUzVjI4Ni43NjFIMTE5LjQ4NFYxODUuNDg0QzExOS40ODQgMTU1LjM5MiAxMDkuNjIxIDE0MC4zNDYgODkuODk3MiAxNDAuMzQ2Qzc4LjI2NDkgMTQwLjM0NiA2OS4wMzUgMTQ0Ljg5OCA2Mi4yMDczIDE1NC4wMDFDNTUuMzc5NyAxNjMuMTA1IDUxLjk2NTkgMTc2LjUwNyA1MS45NjU5IDE5NC4yMDhWMjg2Ljc2MUgwVjk3LjEwNDFINTEuOTY1OVYxMTEuMTAzQzUxLjk2NTkgMTEzLjQzNSA1NS4xMDE0IDExNC40NjIgNTYuNjMzIDExMi43MDRDNjguMTEzNiA5OS41MjIzIDgzLjM3NDEgOTIuOTMxNyAxMDIuNDE1IDkyLjkzMTdDMTI3LjQzNiA5Mi45MzE3IDE0Ni4yODMgMTAzLjI2MiAxNTguOTUzIDEyMy45MjNDMTU5Ljk1MyAxMjUuNTUzIDE2Mi40MTIgMTI1LjUyNyAxNjMuNDA2IDEyMy44OTRDMTY4Ljg4NCAxMTQuODkxIDE3Ni40OTYgMTA3LjczMSAxODYuMjQzIDEwMi40MTVDMTk3LjM2OSA5Ni4wOTI2IDIwOC42MjIgOTIuOTMxNyAyMjAuMDAyIDkyLjkzMTdDMjQyLjUwNyA5Mi45MzE3IDI1OS45NTYgMTAwLjM5MiAyNzIuMzQ3IDExNS4zMTFDMjg0LjczOCAxMzAuMjMxIDI5MC45MzMgMTUwLjcxNCAyOTAuOTMzIDE3Ni43NlYyODYuNzYxSDIzOC45NjdaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+" class="h-3.5 w-auto translate-y-0.75" /><span class="sr-only">This documentation is built and hosted on Mintlify, a developer documentation platform</span></a>

</div>

</div>

</div>

</div>

</div>
