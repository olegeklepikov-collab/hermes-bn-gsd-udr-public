> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: index

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: Reference
description: Lookup material — configuration, git integration, JSON contracts, observability, troubleshooting, and the FAQ.
---

Lookup material for beads: the pages here specify contracts and edge cases
rather than teach concepts (that's How Beads Works (локальный ресурс исходного примера не включён)).

## Pages in this section

- Configuration (локальный ресурс исходного примера не включён) — every config key, environment
  variable, default, and the precedence between them.
- Git Integration (локальный ресурс исходного примера не включён) — hooks, `refs/dolt/data`,
  role detection, and branchless (jujutsu) workflows.
- Git Worktrees Guide (локальный ресурс исходного примера не включён) — how beads behaves across
  worktrees sharing one repository.
- Protected Branches (локальный ресурс исходного примера не включён) — sync-branch mode for
  repos where direct pushes to main are blocked.
- Advanced Features (локальный ресурс исходного примера не включён) — rename, merge, compaction, and
  other power-user operations.
- JSON Output Schema Contract (локальный ресурс исходного примера не включён) — the stability
  contract behind every `--json` flag.
- Events Journal (локальный ресурс исходного примера не включён) — the durable, replayable record
  of committed mutations that external tooling tails, and its boundaries.
- Observability (OpenTelemetry) (локальный ресурс исходного примера не включён) — traces and
  metrics bd can emit, and how to point them at a collector.
- Troubleshooting (локальный ресурс исходного примера не включён) — symptom-first fixes for
  common failures (deeper runbooks live in Recovery (локальный ресурс исходного примера не включён)).
- Antivirus False Positives (локальный ресурс исходного примера не включён) — Windows AV heuristics
  and binary verification.
- FAQ (локальный ресурс исходного примера не включён) — beads vs other trackers, and the questions
  everyone asks in week one.
- CLI Reference (локальный ресурс исходного примера не включён) — the generated page-per-command
  reference, nested below as a collapsible group.
