> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: rules

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: "bd rules"
description: "Audit and compact Claude rules"
---

{/* AUTO-GENERATED: do not edit manually */}

Generated from `bd help --doc rules`.

Audit and compact Claude rules

```
bd rules [flags]
```

## bd rules audit

Scan rules for contradictions and merge opportunities

```
bd rules audit [flags]
```

**Flags:**

```
      --path string       Path to rules directory (default ".claude/rules/")
      --threshold float   Jaccard similarity threshold (default 0.6)
```

## bd rules compact

Merge related rules into composites

```
bd rules compact [flags]
```

**Flags:**

```
      --auto            Apply audit suggestions
      --dry-run         Preview without applying
      --group strings   Rule names to merge
      --path string     Path to rules directory (default ".claude/rules/")
```
