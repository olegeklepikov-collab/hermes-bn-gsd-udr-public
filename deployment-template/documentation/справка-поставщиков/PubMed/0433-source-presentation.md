> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка PubMed: source-presentation

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Evidence and source presentation

Every externally sourced scientific claim needs a response that actually supports it; successful retrieval alone is not evidence.

- Add claim-adjacent Markdown links only for substantive external claims supported by the response, using a deterministic authoritative record URL whenever one exists.
- Keep successful connectivity, schema, service-metadata, identifier-resolution, empty-result, and checked-but-empty lookups exclusively in `checked_sources`. Failed lookups do not provide citations.
- Evidence-bearing `sources` entries must include `supports_claim=true` and `kind=evidence`. Orchestration and synthesis must propagate only downstream entries carrying both properties.
- Use explicit, validated DOI, PMID, and PMCID mappings from `source-links.json`; never invent a deep link for an unsupported source or identifier.
- Redact credentials, tokens, API keys, email, session identifiers, private search or patient terms, request-body values, URL userinfo, and fragments from all provenance URLs.
- Raw JSON, XML, FASTA, or text responses must remain byte-for-byte identical to the upstream payload. Save structured sources separately; never inject Markdown or source metadata into raw output.
