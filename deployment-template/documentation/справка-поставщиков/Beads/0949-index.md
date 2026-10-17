> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: index

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: Recovery Overview
description: Diagnose and resolve common Beads issues
---

This section provides step-by-step recovery procedures for common Beads issues. Each runbook follows a consistent format: Symptoms, Diagnosis, Solution (5 steps max), and Prevention.

## Common Issues

| Issue | Symptoms | Runbook |
|-------|----------|---------|
| Schema Version Mismatch | `bd` refuses with `schema version mismatch: database is at vNN, binary knows up to vNN` | Accidental v1.2.1 Release (локальный ресурс исходного примера не включён) |
| Init Safety Refusals | `bd init` or `bd dolt` refuses with a pattern code like `pk-fork-refused` | Recovery Playbooks (локальный ресурс исходного примера не включён) |
| Database Corruption | Database errors, missing data | Database Corruption (локальный ресурс исходного примера не включён) |
| Merge Conflicts | Dolt conflicts during sync | Merge Conflicts (локальный ресурс исходного примера не включён) |
| Circular Dependencies | Cycle detection errors | Circular Dependencies (локальный ресурс исходного примера не включён) |
| Sync Failures | `bd dolt push`/`bd dolt pull` errors | Sync Failures (локальный ресурс исходного примера не включён) |
| History Bloat | Store grows unbounded; `dolt gc` reclaims nothing | History Bloat (локальный ресурс исходного примера не включён) |
| Removing beads | Uninstall bd or strip beads from a repo | Uninstalling (локальный ресурс исходного примера не включён) |

## Quick Diagnostic

Before diving into specific runbooks, try these quick checks:

```bash
# Check Beads status
bd status

# Verify Dolt server is running
bd doctor

# Check for blocked issues
bd blocked
```

<Tip>
Most issues can be diagnosed with `bd status`. Start there before following specific runbooks.
</Tip>

## Getting Help

If these runbooks don't resolve your issue:

1. Check the FAQ (локальный ресурс исходного примера не включён)
2. Search [existing issues](https://github.com/gastownhall/beads/issues)
3. Open a new issue with diagnostic output
