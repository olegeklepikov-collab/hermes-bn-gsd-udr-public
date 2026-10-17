> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: data-raw-affiliation-strings

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Raw affiliation strings

A **raw affiliation string** (RAS) is the exact affiliation text an author printed on a work, before OpenAlex matches it to an [institution](https://help.openalex.org/data/institutions/) — free text like `"Impactstory, Sanford, NC, USA"` or `"Massachusetts Institute of Technology"`, often messy and inconsistent. It's the raw input to institution disambiguation: the thing OpenAlex parses to figure out *which organizations* an author was affiliated with. Raw affiliation strings are a [component](https://help.openalex.org/data/component/) entity — they don't get their own OpenAlex ID. They live inside an [authorship](https://help.openalex.org/data/authorships/), in its [`raw_affiliation_strings`](https://help.openalex.org/data/authorships/#raw_affiliation_strings) list and its [`affiliations`](https://help.openalex.org/data/authorships/#affiliations) mapping. They can also be queried in two other ways: a bespoke `raw_affiliation_strings.search` filter on [works](https://help.openalex.org/data/works/), and a standalone [`/raw-affiliation-strings`](https://api.openalex.org/raw-affiliation-strings) list endpoint that pages over the distinct strings themselves.

## About

OpenAlex preserves the affiliation text exactly as it arrived on the source record, then parses each string to extract the institutions it names — so both `"MIT, Boston, USA"` and `"Massachusetts Institute of Technology"` resolve to the same institution ([ror.org/042nb2s44](https://ror.org/042nb2s44)).

### How matching works

Since 28 September 2026, strings are matched by the [OpenAlex affiliation matcher](https://github.com/ourresearch/openalex-affiliation-matcher), version 3.0. For each string it finds about 18 candidate institutions, scores each one with a small model, and then chooses the set: none, one or several, using [ROR](https://ror.org/)'s parent, child and related links. It names exactly the right institutions for 89% of a random sample of OpenAlex strings, up from 73% for the previous version, and every new string is matched the night it arrives. The method, benchmarks, code and test sets are all in [the repository](https://github.com/ourresearch/openalex-affiliation-matcher). We keep improving it in numbered releases, so institution counts keep changing, mostly upward.

The result is stored on the authorship as the [`affiliations`](https://help.openalex.org/data/authorships/#affiliations) mapping: each raw string paired with the institution IDs it produced. Country is assigned through the same matching — from the matched ROR record's metadata, or, when nothing matches but the address still names a country, directly from the string.

### Complex and layered systems

Some national research systems are layered — a French *unité mixte de recherche* (UMR) may belong to several parent organizations at once. OpenAlex handles these through ROR lineage: when a sub-unit has its own ROR record, the raw string matches to it, and lineage lets users roll the report up to the parent universities. The limiting factor is ROR coverage; where a sub-unit has no ROR record, a string can only match its parent.

### Failure modes

The matcher can still miss or mis-assign institutions, most often organizations with no ROR record. A raw string can also resolve to no institution at all while still yielding a country. Because the raw string is preserved verbatim, you can always see the original text even when matching fell short, and member institutions can review and correct their own affiliation matches with the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/); those corrections override the matcher. Known issues are listed in [the repository](https://github.com/ourresearch/openalex-affiliation-matcher#known-issues); the earlier versions live in [openalex-institution-parsing](https://github.com/ourresearch/openalex-institution-parsing).

## Attributes

A raw affiliation string is essentially a string plus its matched-institution mapping, both of which live on the [authorship](https://help.openalex.org/data/authorships/). Being a component entity, it carries none of the [common attributes](https://help.openalex.org/data/common-attributes/) and has no OpenAlex ID.

### `raw_affiliation_strings`
*List of strings.* On an authorship, the exact affiliation text this author printed, one string per affiliation — e.g. `["Impactstory, Sanford, NC, USA"]`. The unparsed input to institution matching.

### `affiliations`
*List of objects.* On an authorship, the mapping from each raw string to the institutions it matched. Each element has:

- **`raw_affiliation_string`** *(String)* — one raw affiliation string, verbatim.
- **`institution_ids`** *(List)* — the OpenAlex [institution](https://help.openalex.org/data/institutions/) IDs that string resolved to (empty if nothing matched).

```json
"affiliations": [
  {
    "raw_affiliation_string": "Impactstory, Sanford, NC, USA",
    "institution_ids": [
      "https://openalex.org/I4200000001",
      "https://openalex.org/I4210166736"
    ]
  }
]
```

This is the authoritative record of *which printed string produced which institutions* — the flattened [`institutions`](https://help.openalex.org/data/authorships/#institutions) list on the authorship loses that per-string provenance.

## In the API

Raw affiliation strings are a [component](https://help.openalex.org/data/component/) entity — they carry no OpenAlex ID and you'll usually meet them as fields on an [authorship](https://help.openalex.org/data/authorships/) (select [`authorships`](https://help.openalex.org/data/works/attributes/#authorships) on a work). There are three ways to reach them:

- **The standalone list endpoint** at [`api.openalex.org/raw-affiliation-strings`](https://api.openalex.org/raw-affiliation-strings) pages over the *distinct* strings themselves, rather than through works. Each row is a raw string plus its `works_count`, the institution IDs it resolved to (`institution_ids_final`, and any curated `institution_ids_override`), and its `countries` — handy for auditing how a given affiliation string is being matched across the whole corpus.
- **Search the raw text** with the `raw_affiliation_strings.search` filter on [works](https://help.openalex.org/data/works/): `filter=raw_affiliation_strings.search:impactstory` returns works whose authors printed that affiliation text — matching on the *raw string*, before institution disambiguation. Useful for finding an organization's works when its name never resolved cleanly to a ROR-backed institution. Unlike most `.search` filters, this one is **unstemmed** (it matches the printed tokens literally), so [wildcards](https://help.openalex.org/api/searching/#wildcards) work here: `filter=raw_affiliation_strings.search.exact:impactstor*` — the `.search.exact` spelling is the sanctioned wildcard target and searches the same text. [Proximity](https://help.openalex.org/api/searching/#proximity-search) works too, including with wildcard operands, e.g. `raw_affiliation_strings.search.exact:"process*"~50~"material*"` for the two terms within 50 words of each other in the affiliation text; in [OQL](https://help.openalex.org/access/oql/) that's `raw affiliation has (within 50 ("process*", "material*"))`.
- **Filter on the resolved mapping** with `authorships.affiliations.institution_ids`, which filters works on the institution IDs a raw string produced.

See [Filtering](https://help.openalex.org/api/filtering/) for filter syntax and [Searching](https://help.openalex.org/api/searching/) for how `.search` behaves. To filter on the resolved institution itself (rather than the raw text), use `authorships.institutions.id` on [works](https://help.openalex.org/data/works/).
