> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: official-cli-download-help

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


Usage: openalex download [OPTIONS]

  Download OpenAlex work metadata and optionally content (PDFs/XML).

  By default, downloads JSON metadata for each work. Use --content to also
  download PDFs and/or TEI XML files.

  Examples:
    # Metadata only (default)
    openalex download --filter "topics.id:T10325" -o ./frogs

    # Metadata + PDFs   openalex download --filter "topics.id:T10325"
    --content pdf -o ./frogs

    # Metadata + PDFs + XML   openalex download --filter "topics.id:T10325"
    --content pdf,xml -o ./frogs

  Input modes:
    1. Filter mode: --filter "publication_year:2024,type:article"
    2. ID list: --ids "W2741809807,W3203546474"
    3. Stdin: echo "W2741809807" | openalex download --stdin

  DOIs are auto-detected and resolved: --ids "10.1038/nature12373"

Options:
  --api-key TEXT           OpenAlex API key (or set OPENALEX_API_KEY env var)
                           [required]
  -o, --output PATH        Output directory for downloaded files
  --storage [local|s3]     Storage backend
  --s3-bucket TEXT         S3 bucket name (required for S3 storage)
  --s3-prefix TEXT         S3 key prefix
  --filter TEXT            OpenAlex filter string (e.g.,
                           'publication_year:>2020,type:article')
  --content TEXT           Content types to download: pdf, xml, or both
                           (comma-separated). If omitted, only metadata is
                           downloaded.
  --nested                 Use nested folder structure (W##/##/filename).
                           Recommended for >10K files.
  --ids TEXT               Comma-separated list of work IDs or DOIs to
                           download
  --stdin                  Read work IDs or DOIs from stdin (one per line or
                           comma-separated)
  --workers INTEGER RANGE  Number of concurrent download workers  [1<=x<=200]
  --resume / --no-resume   Resume from checkpoint if available
  --fresh                  Ignore existing checkpoint and start fresh
  --sample INTEGER RANGE   Download a random sample of N works (max 10,000).
                           Uses the API's sample parameter.  [1<=x<=10000]
  --seed INTEGER           Seed for reproducible random samples (use with
                           --sample).
  -q, --quiet              Minimal output (log file only)
  -v, --verbose            Verbose debug output
  --help                   Show this message and exit.
