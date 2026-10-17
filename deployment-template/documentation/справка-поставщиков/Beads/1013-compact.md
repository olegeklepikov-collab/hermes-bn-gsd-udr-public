> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: compact

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: "bd compact"
description: "Squash Dolt commits older than N days into a single commit."
---

{/* AUTO-GENERATED: do not edit manually */}

Generated from `bd help --doc compact`.

Squash Dolt commits older than N days into a single commit.

Recent commits (within the retention window) are preserved via cherry-pick.
This reduces Dolt storage overhead from auto-commit history while keeping
recent change tracking intact.

For semantic issue compaction (summarizing closed issues), use 'bd admin compact'.
For full history squash, use 'bd flatten'.

How it works:
  1. Identifies commits older than --days threshold
  2. Creates a squashed base commit from all old history
  3. Cherry-picks recent commits on top
  4. Swaps main branch to the compacted version
  5. Runs Dolt GC to reclaim space

Examples:
  bd compact --dry-run               # Preview: show commit breakdown
  bd compact --force                 # Squash commits older than 30 days
  bd compact --days 7 --force        # Keep only last 7 days of history
  bd compact --days 90 --force       # Conservative: squash 90+ day old commits

```
bd compact [flags]
```

**Flags:**

```
      --days int   Keep commits newer than N days (default 30)
      --dry-run    Preview without making changes
  -f, --force      Confirm commit squash
```
