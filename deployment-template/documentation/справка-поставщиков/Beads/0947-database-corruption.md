> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: database-corruption

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: Database Corruption
description: Recover from Dolt database corruption
---

This runbook helps you recover from database corruption in Beads.

## Symptoms

- Error messages during `bd` commands
- "database is locked" errors that persist
- Missing issues that should exist
- Inconsistent database state

## Diagnosis

```bash
# Check database integrity
bd doctor

# Check Dolt server health
bd dolt show
```

## Solution

**Step 1:** Stop the Dolt server
```bash
bd dolt stop
```

**Step 2:** Back up current state
```bash
cp -r .beads .beads.backup
```

**Step 3:** Preview what doctor would fix
```bash
bd doctor --dry-run
```

**Step 4:** Rebuild database
```bash
bd doctor --fix
```

**Step 5:** Verify recovery
```bash
bd doctor
bd list
```

**Step 6:** Restart the Dolt server
```bash
dolt sql-server
```

## Prevention

- Let the Dolt server handle synchronization
- Use `bd dolt stop` before system shutdown
- Run `bd doctor` periodically to catch issues early
