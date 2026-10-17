> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: status

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: "bd status"
description: "Show a quick snapshot of the issue database state and statistics."
---

{/* AUTO-GENERATED: do not edit manually */}

Generated from `bd help --doc status`.

Show a quick snapshot of the issue database state and statistics.

This command provides a summary of issue counts by state (open, in_progress,
blocked, closed), ready work, extended statistics (pinned issues,
average lead time), and recent activity over the last 24 hours from git history.

Similar to how 'git status' shows working tree state, 'bd status' gives you
a quick overview of your issue database without needing multiple queries.

Use cases:
  - Quick project health check
  - Onboarding for new contributors
  - Integration with shell prompts or CI/CD
  - Daily standup reference

Examples:
  bd status                    # Show summary with activity
  bd status --no-activity      # Skip git activity (faster)
  bd status --json             # JSON format output
  bd status --assigned         # Show issues assigned to current user
  bd stats                     # Alias for bd status

```
bd status [flags]
```

**Aliases:** stats

**Flags:**

```
      --all           Show all issues (default behavior)
      --assigned      Show issues assigned to current user
      --no-activity   Skip git activity tracking (faster)
```
