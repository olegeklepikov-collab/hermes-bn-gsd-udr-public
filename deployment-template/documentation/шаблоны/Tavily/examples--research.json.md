> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Tavily: research.json

Это переносимый шаблон параметров. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "input": "Read the original Attention Is All You Need publication from 2017. Briefly identify its architecture and one methodological limitation. Use primary publication sources and APA citations. A short research note suffices.",
  "model": "pro",
  "citation_format": "apa",
  "output_length": "short",
  "include_domains": [
    "arxiv.org",
    "papers.neurips.cc"
  ],
  "exclude_domains": [
    "reddit.com",
    "quora.com"
  ]
}
```
