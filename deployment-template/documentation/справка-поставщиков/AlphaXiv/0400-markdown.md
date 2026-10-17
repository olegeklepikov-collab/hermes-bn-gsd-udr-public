> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка AlphaXiv: markdown

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


<div class="min-h-0 w-full flex-auto flex-col pl-(--assistant-room-left) pr-(--assistant-room-right) transition-[padding] duration-[var(--assistant-room-duration,300ms)] ease-[cubic-bezier(0.32,0.72,0,1)] sm:w-0" role="main">

<div class="mx-auto w-full max-w-[1150px] px-4 py-8 sm:px-10">

<div class="relative flex shrink-0 items-center w-max rounded-full p-1 bg-surface">

<a href="/docs/mcp" class="relative shrink-0 cursor-pointer rounded-full transition-[color] px-3 py-0.5 text-sm/6 font-normal text-text hover:text-custom-red" data-active="false">MCP Server</a><a href="/docs/markdown" class="bg-bg relative shrink-0 cursor-pointer rounded-full transition-[color] px-3 py-0.5 text-sm/6 font-normal text-custom-red active" data-active="true" data-status="active" aria-current="page">Blog formatting</a>

</div>

# Blog formatting

<div class="markdown-content blog-post [&_table]:w-full!">

Publishing markdown blogs can be done through the button on the homepage. This page describes the custom features we support for these blogs.

Standard Markdown is supported, plus tables, footnotes, highlighted code blocks, and inline and display math. See the <a href="https://www.markdownguide.org/basic-syntax/" target="_blank" rel="noopener noreferrer" data-state="closed">Markdown basic syntax reference<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLWV4dGVybmFsLWxpbmsgbWwtMC41IGlubGluZSBzaXplLTMuNSBhbGlnbi1iYXNlbGluZSIgYXJpYS1oaWRkZW49InRydWUiPjxwYXRoIGQ9Ik0xNSAzaDZ2NiIgLz48cGF0aCBkPSJNMTAgMTQgMjEgMyIgLz48cGF0aCBkPSJNMTggMTN2NmEyIDIgMCAwIDEtMiAySDVhMiAyIDAgMCAxLTItMlY4YTIgMiAwIDAgMSAyLTJoNiIgLz48L3N2Zz4=" class="lucide lucide-external-link ml-0.5 inline size-3.5 align-baseline" /></a>. A leading `# Title` becomes the blog's title and is removed from the body, which must not be empty; sections use `##`, and a later `#` heading is rejected. The byline and optional abstract come from the publication fields.

## ImageCaption

An image with a rich caption and the blog image viewer.

| Attribute | Required | Meaning                                              |
|-----------|----------|------------------------------------------------------|
| `src`     | Yes      | Path to the image inside the uploaded ZIP.           |
| `alt`     | No       | Text describing the image.                           |
| Children  | No       | Caption content; Markdown and supported inline HTML. |

<div class="group/code-block relative overflow-hidden rounded-lg border border-border/50">

<div class="flex items-center justify-between border-b border-border/50 bg-panel-alt/40 px-3 py-1.5">

<span class="text-xs font-medium text-muted select-none">HTML</span>

<div class="interactable-overlay bg-overlay">

</div>

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLWNvcHkgc2l6ZS0zLjUgdGV4dC1tdXRlZCIgYXJpYS1oaWRkZW49InRydWUiPjxyZWN0IHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgeD0iOCIgeT0iOCIgcng9IjIiIHJ5PSIyIiAvPjxwYXRoIGQ9Ik00IDE2Yy0xLjEgMC0yLS45LTItMlY0YzAtMS4xLjktMiAyLTJoMTBjMS4xIDAgMiAuOSAyIDIiIC8+PC9zdmc+" class="lucide lucide-copy size-3.5 text-muted" />

</div>

``` m-0!
<ImageCaption src="images/results.png" alt="Accuracy by method">
  <strong>Figure 1.</strong> Accuracy on the evaluation set.
</ImageCaption>
```

</div>

## Tabs · Tab

Switchable content panels. `Tabs` takes direct `Tab` children and opens the first panel initially.

| Element | Attribute | Required | Meaning                                     |
|---------|-----------|----------|---------------------------------------------|
| `Tabs`  | —         | —        | Container for the panels.                   |
| `Tab`   | `label`   | Yes      | Plain-text label shown in the tab row.      |
| `Tab`   | Children  | No       | Panel content; Markdown and supported HTML. |

<div class="group/code-block relative overflow-hidden rounded-lg border border-border/50">

<div class="flex items-center justify-between border-b border-border/50 bg-panel-alt/40 px-3 py-1.5">

<span class="text-xs font-medium text-muted select-none">HTML</span>

<div class="interactable-overlay bg-overlay">

</div>

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLWNvcHkgc2l6ZS0zLjUgdGV4dC1tdXRlZCIgYXJpYS1oaWRkZW49InRydWUiPjxyZWN0IHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgeD0iOCIgeT0iOCIgcng9IjIiIHJ5PSIyIiAvPjxwYXRoIGQ9Ik00IDE2Yy0xLjEgMC0yLS45LTItMlY0YzAtMS4xLjktMiAyLTJoMTBjMS4xIDAgMiAuOSAyIDIiIC8+PC9zdmc+" class="lucide lucide-copy size-3.5 text-muted" />

</div>

``` m-0!
<Tabs>
  <Tab label="Method">
    <p>The <strong>method</strong> and its assumptions.</p>
  </Tab>
  <Tab label="Results"> <p>The results and their interpretation.</p> </Tab>
</Tabs>
```

</div>

## HTML support

| Category | Elements |
|----|----|
| Structure | `p`, `br`, `hr`, `h2`–`h6`, `div`, `span`, `section` |
| Emphasis | `em`, `strong`, `b`, `i`, `s`, `del`, `sub`, `sup`, `kbd`, `mark` |
| Links and images | `a`, `img`, `figure`, `figcaption` |
| Code and quotations | `code`, `pre`, `blockquote` |
| Lists | `ul`, `ol`, `li` |
| Tables | `table`, `thead`, `tbody`, `tr`, `th`, `td` |

Use literal attribute values. Keep blank lines around Markdown nested in HTML. Component names are case-sensitive — `ImageCaption`, `Tabs`, `Tab` — and custom elements require explicit closing tags, even with no children.

The alphaXiv app reads posts as MDX, so uploads must also parse as MDX and render the same in both readers: self-close empty tags (`<br />`, `<img src="…" />`), escape a literal `{`, `}`, or `<` in text as `\{`, `\}`, or `\<`, keep every start tag on one line, fence every code block instead of indenting it, write links as `[text](https://www.alphaxiv.org/docs/url)` instead of `<url>`, and leave out HTML comments.

Scripts, iframes, inline SVG, forms, and unlisted components are rejected. Event handlers, inline styles, and unsupported attributes are removed. Imports and JavaScript expressions are never executed.

## Images and upload limits

Images must be bundled in a `.zip` alongside the Markdown file and referenced by relative path, such as `![Results](https://www.alphaxiv.org/docs/images/results.png)`.

| Resource | Limit                                        |
|----------|----------------------------------------------|
| Markdown | 1 MB                                         |
| ZIP      | 50 MB compressed and expanded; 200 entries   |
| Images   | 50 distinct sources; 10 MB each; 50 MB total |

Please <a href="/cdn-cgi/l/email-protection#9cfff3f2e8fdffe8dcfdf0ecf4fde4f5eab2f3eefb" target="_blank" rel="noopener noreferrer" data-state="closed"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLW1haWwgbXgtMC41IGlubGluZSBzaXplLTMuNSBhbGlnbi1taWRkbGUiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtMjIgNy04Ljk5MSA1LjcyN2EyIDIgMCAwIDEtMi4wMDkgMEwyIDciIC8+PHJlY3QgeD0iMiIgeT0iNCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjE2IiByeD0iMiIgLz48L3N2Zz4=" class="lucide lucide-mail mx-0.5 inline size-3.5 align-middle" />contact us</a> if you would like to publish a blog exceeding these limits.

</div>

</div>

</div>
