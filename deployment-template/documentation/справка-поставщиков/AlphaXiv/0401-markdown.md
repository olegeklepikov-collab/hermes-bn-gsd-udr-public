> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка AlphaXiv: markdown

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


Blog formatting | alphaXiv
alphaXiv
Explore
Researchers
Sign In
MCP Server
Autoresearch
Browser Extension
Light themeDark themeBlogSend Feedback?MCP ServerBlog formatting
Blog formatting
Publishing markdown blogs can be done through the button on the homepage. This
page describes the custom features we support for these blogs.
Standard Markdown is supported, plus tables, footnotes, highlighted code blocks, and inline and display math. See the Markdown basic syntax reference. A leading # Title becomes the blog's title and is removed from the body, which must not be empty; sections use ##, and a later # heading is rejected. The byline and optional abstract come from the publication fields.
ImageCaption
An image with a rich caption and the blog image viewer.AttributeRequiredMeaningsrcYesPath to the image inside the uploaded ZIP.altNoText describing the image.ChildrenNoCaption content; Markdown and supported inline HTML.HTML
<ImageCaption src="images/results.png" alt="Accuracy by method">
<strong>Figure 1.</strong> Accuracy on the evaluation set.
</ImageCaption>
Tabs · Tab
Switchable content panels. Tabs takes direct Tab children and opens the first panel initially.ElementAttributeRequiredMeaningTabs——Container for the panels.TablabelYesPlain-text label shown in the tab row.TabChildrenNoPanel content; Markdown and supported HTML.HTML
<Tabs>
<Tab label="Method">
<p>The <strong>method</strong> and its assumptions.</p>
</Tab>
<Tab label="Results"> <p>The results and their interpretation.</p> </Tab>
</Tabs>
HTML supportCategoryElementsStructurep, br, hr, h2–h6, div, span, sectionEmphasisem, strong, b, i, s, del, sub, sup, kbd, markLinks and imagesa, img, figure, figcaptionCode and quotationscode, pre, blockquoteListsul, ol, liTablestable, thead, tbody, tr, th, td
Use literal attribute values. Keep blank lines around Markdown nested in HTML. Component names are case-sensitive — ImageCaption, Tabs, Tab — and custom elements require explicit closing tags, even with no children.
The alphaXiv app reads posts as MDX, so uploads must also parse as MDX and render the same in both readers: self-close empty tags (<br />, <img src="…" />), escape a literal {, }, or < in text as \{, \}, or \<, keep every start tag on one line, fence every code block instead of indenting it, write links as text (локальный ресурс исходного примера не включён) instead of <url>, and leave out HTML comments.
Scripts, iframes, inline SVG, forms, and unlisted components are rejected. Event handlers, inline styles, and unsupported attributes are removed. Imports and JavaScript expressions are never executed.
Images and upload limits
Images must be bundled in a .zip alongside the Markdown file and referenced by relative path, such as Results (локальный ресурс исходного примера не включён).ResourceLimitMarkdown1 MBZIP50 MB compressed and expanded; 200 entriesImages50 distinct sources; 10 MB each; 50 MB total
Please contact us if you would like to publish a blog exceeding these limits.Sign in
Assistant
