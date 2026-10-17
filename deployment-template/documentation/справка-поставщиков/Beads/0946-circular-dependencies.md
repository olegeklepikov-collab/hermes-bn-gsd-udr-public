> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: circular-dependencies

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: Circular Dependencies
description: Detect and break dependency cycles
---

This runbook helps you detect and break circular dependency cycles in your issues.

## Symptoms

- "circular dependency detected" errors
- `bd blocked` shows unexpected results
- Issues that should be ready appear blocked

## Diagnosis

```bash
# Check for blocked issues
bd blocked

# View dependencies for a specific issue
bd show <issue-id>

# List all dependencies
bd dep tree
```

## Solution

**Step 1:** Identify the cycle
```bash
bd blocked --verbose
```

**Step 2:** Map the dependency chain
```bash
bd show <issue-a>
bd show <issue-b>
# Follow the chain until you return to <issue-a>
```

**Step 3:** Determine which dependency to remove
Consider: Which dependency is least critical to the workflow?

**Step 4:** Remove the problematic dependency
```bash
bd dep remove <dependent-issue> <blocking-issue>
```

**Step 5:** Verify the cycle is broken
```bash
bd blocked
bd ready
```

## Prevention

- Think "X needs Y" not "X before Y" when adding dependencies
- Use `bd blocked` after adding dependencies to check for cycles
- Keep dependency chains shallow when possible
