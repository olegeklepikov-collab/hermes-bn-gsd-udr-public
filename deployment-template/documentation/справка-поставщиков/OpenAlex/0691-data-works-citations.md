> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: data-works-citations

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Citations

Every work in OpenAlex knows which works it cites and which works cite it. This page covers how those links are built, and the citation metric derived from them.

> [!claude]
> You can ask Claude: *"Who cites W2741809807, what does it reference, and what's its FWCI?"* It lists the citing and referenced works and can summarize the follow-up work. (Citation totals across a set of works are website-only.) Set up once: [Using OpenAlex with an AI assistant](https://help.openalex.org/how-to/ai-assistants/).

## Citations and references

Every work carries a list of the works it cites ([`referenced_works`](https://help.openalex.org/data/works/attributes/#referenced_works)) and a count of the works that cite it ([`cited_by_count`](https://help.openalex.org/data/works/attributes/#cited_by_count)). Both are built from the same process: extracting each work's reference list, then matching those references to other works already in OpenAlex.

When OpenAlex creates a work record, it pulls the reference list from the record's source (Crossref, PubMed, and similar). When the work is open access, OpenAlex can also extract references directly from the PDF, which fills gaps for works whose source records omit references. Each extracted reference is then matched to an existing work — first by DOI (highly reliable) and, when no DOI is present, by other bibliographic metadata (less reliable). A successful match counts as a **reference** in the citing work and a **citation** of the cited work.

Because citations are built by matching, a work's `referenced_works` can be *shorter* than the reference list printed in its PDF. The common reasons: the cited work isn't in OpenAlex (references to unknown works are dropped); the source record's references differ from the final PDF; many Crossref records include no references at all; or a reference has no DOI and metadata matching failed.

## Field-Weighted Citation Impact

[`fwci`](https://help.openalex.org/data/works/attributes/#fwci) is a [snowball metric](https://arma.ac.uk/wp-content/uploads/2021/08/Snowball-Metrics-Recipe-Book-edition-2.pdf) normalizing a work's citations for its type, publication year, and [subfield](https://help.openalex.org/data/subfields/). The formula is `citations received / citations expected`: **1.0** is world average, **2.0** is twice expected, **0.5** is half.

- **Citations received** (numerator): citations in the publication year plus the three following years.
- **Citations expected** (denominator): the average of that same 4-year received count over every work with the same year, type, and subfield (articles split journals vs. conference proceedings). [Calculation code](https://github.com/ourresearch/openalex-databricks/tree/main/jobs/weekly_metric_creation).

FWCI follows the standard [recipe book](https://arma.ac.uk/wp-content/uploads/2021/08/Snowball-Metrics-Recipe-Book-edition-2.pdf), so the math matches other databases, but the *inputs* differ: OpenAlex is more comprehensive (many uncited works pull the expected value down, raising FWCI for cited works); we classify each work into a single subfield from its own text, not its journal; and our publication year is typically the first-online date. Not every work gets an FWCI — work types that aren't expected to accrue citations (e.g. [paratext](https://help.openalex.org/data/work-types/)) are omitted so they don't distort institutional averages. As of mid-2026 about 218M of 322M works (68%) carry one.
