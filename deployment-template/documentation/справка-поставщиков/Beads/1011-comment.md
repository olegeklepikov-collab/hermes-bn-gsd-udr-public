> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: comment

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: "bd comment"
description: "Add a comment to an issue."
---

{/* AUTO-GENERATED: do not edit manually */}

Generated from `bd help --doc comment`.

Add a comment to an issue.

Shorthand for 'bd comments add &lt;id&gt; "text"'.

Examples:
  bd comment bd-123 "Working on this now"
  bd comment bd-123 Working on this now
  echo "comment from pipe" | bd comment bd-123 --stdin
  bd comment bd-123 --file notes.txt

```
bd comment <id> [text...] [flags]
```

**Flags:**

```
      --file string   Read comment text from file
      --stdin         Read comment text from stdin
```
