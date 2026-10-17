> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Zotero: better-bibtex

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


Better BibTeX for Zotero
Skip to main content
image/svg+xml
Better BibTeX for Zotero
Search
Home
Installation
Preferences
Exporting
Citation Keys
Support
Changelog
Sponsoring BBT
More
Download
Sponsorship
GitHub repo
automatic export
cache
citation keys
cite as you write
export
git
import
libreoffice
overleaf
scripting
word
Star
Re-do migration
Features
Facilities for generating citation keys
Conversion between formats and encodings
Facilities for exporting data from Zotero
Getting started
How does it work ?
Got problems? We got fixes!
Better BibTeX for Zotero
Better BibTeX for Zotero
Better BibTeX (BBT) is an extension for
Zotero
and (in principle)
Juris-M
that makes it easier to manage bibliographic data, especially for people authoring documents using text-based toolchains (e.g. based on
LaTeX
/
Markdown
).
Notice
With the advent of Zotero 8, items have a Zotero-native citation key field. This has replaced the BBT citation key field.
This has caused a few somewhat disruptive changes:
Zotero 7 is no longer supported
. BBT 8.0.25 still works on 7.0.32, but will not receive further updates.
Zotero will have moved all pinned keys out of the
extra
field into the native field
The concept of pinning keys is gone; keys are
always
pinned now. Zotero doesn’t have a place I can store whether a key is pinned or not.
The Zotero-native citation keys are stored in another place than the BBT citation keys. If you have no Zotero-native citation keys yet, BBT will silently migrate them to there. If you do have Zotero-native citation keys, and a migration would overwrite them, you will be offered a window with the choice on how to migrate your citation keys from the BBT storage to the Zotero storage.
Integrations that read the BBT database directly will have to read the Zotero database instead.
Upside to all of this is that keys will sync.
Re-do migration
If key migration appears to have failed, YOUR CITATION KEYS ARE SAFE
.
Make sure you are on the latest version. For the first 5 minutes after BBT start, the Help menu will have an option
Re-do BBT citation key migration
. Click that, generate a debug log from the Help menu, then open an issue on github noting the debug log ID.
Features
Facilities for generating citation keys
Automatically generate
citation keys
without key clashes! Generate citation keys that take into account existing keys in your library even when they are not part of the items you export. Prevent random breakage!
Generate citation keys based on contents of your items using
citekey formulas
.
Set your own, stable citation keys, drag and drop LaTeX citations, add other custom BibLaTeX fields.
Conversion between formats and encodings
Zotero does all its work in UTF-8 Unicode, which is absolutely the right thing to do. Unfortunately, for those shackled
to BibTeX and who cannot (yet) move to BibLaTeX, unicode is a major PITA. Also, Zotero supports some simple HTML markup
in your items that Bib(La)TeX won’t understand.
BBT will convert from/to HTML/LaTeX:
<i>...</i>
⇔
\emph{...}
/
\mkbibemph{...}
/
\textit{...}
<b>...</b>
⇔
\textbf{...}
<sup>...</sup>
⇔
\textsuperscript{...}
and
<sub>...</sub>
⇔
\textsubscript{...}
.
More can be added on request.
BBT contains a comprehensive list of LaTeX constructs, so stuff like
\"{o}
or
\"o
will be converted to their unicode equivalents on import (e.g.,
\"{o}
to
ö
), and their unicode equivalents back to
\"{o}
if you have that option enabled (but you don’t have to if you use BibLaTeX, which has fairly good Unicode support).
If you need literal LaTeX in your export: surround it with
<script>
…
</script>
(or
<pre>
…
</pre>
, which do the same) markers.
Facilities for exporting data from Zotero
Highly
customized exports
.
Fixes date field exports: export dates like ‘forthcoming’ as ‘forthcoming’ instead of empty, but normalize valid dates
to unambiguous international format.
Auto export
of collections or entire libraries when they change.
Pull export
from the embedded webserver.
Automatic
journal abbreviation
.
Getting started
To get started, read the
installation instructions
.
How does it work ?
At its core, BBT behaves like any Zotero import/export module; anywhere you can export or import bibliography items in Zotero,
you’ll find
Better X
listed among the choices.
If nothing else, you could keep your existing workflow as-is, and just enjoy the improved LaTeX ↔ unicode translation on import and export and more accurate field mapping.
Better BibTeX works from
BibTeXing
and
Tame the
BeaST
for BibTeX, and
The BibLaTeX Package
for BibLaTeX, but
since there isn’t really a definitive manual for either format that is universally followed by Bib(La)TeX
editors/processors, I’m pragmatic about implementing what works.
Got problems? We got fixes!
If you have any questions on BBT’s use, do not hesitate to
file a GitHub issue
and ask for help.
If you’re reporting a bug in BBT, please take a moment to glance through the
support request guidelines
; it will make sure I get your problem fixed as quick as possible.
Clear bug reports commonly have really short time-to-fix, so if you report something, stick around – it may be done as you wait.
The support request guidelines are very detailed, perhaps to the point of being off-putting, but please do not fret; these guidelines simply express my ideal bug submission.
I of course prefer very clearly documented issue reports over fuzzy ones, but I prefer fuzzy ones over missed ones.
