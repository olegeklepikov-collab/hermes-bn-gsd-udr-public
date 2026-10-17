> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: index

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: Multi-Agent
description: Coordinate beads across multiple agents and repositories with routing, cross-repo dependencies, and work handoff
---

Beads supports coordination between multiple AI agents and repositories.

## Overview

Multi-agent features enable:
- **Routing** - Automatic issue routing to correct repositories
- **Cross-repo dependencies** - Dependencies across repository boundaries
- **Agent coordination** - Work assignment and handoff between agents

## Key Concepts

### Routing

Routing decides which repository a new bead lands in, based on your role
(contributor vs maintainer) and the `routing.*` config keys — an explicit
`--repo` flag always wins. See Multi-Repo Routing (локальный ресурс исходного примера не включён)
for the decision flow and configuration reference.

### Work Assignment

Assign or atomically claim work:

```bash
bd assign bd-42 agent-1        # shorthand for bd update bd-42 --assignee agent-1
bd update bd-42 --claim        # atomically set assignee + in_progress
bd ready --claim --json        # claim the first ready match
```

### Cross-repo Dependencies

Track dependencies across repositories:

```bash
bd dep add bd-42 external:other-repo:api-ready
```

## Architecture

```
┌─────────────────┐
│   Main Repo     │
│   (coordinator) │
└────────┬────────┘
         │ routes
    ┌────┴────┐
    │         │
┌───▼───┐ ┌───▼───┐
│Frontend│ │Backend│
│ Repo   │ │ Repo  │
└────────┘ └────────┘
```

## Getting Started

1. **Single repo**: Standard beads workflow
2. **Multi-repo**: Configure routes and cross-repo deps
3. **Multi-agent**: Add work assignment and handoff

## Pages in this section

- Routing (локальный ресурс исходного примера не включён) — automatic issue routing across
  repositories and `BEADS_DIR` resolution.
- Coordination (локальный ресурс исходного примера не включён) — work assignment and handoff
  patterns between agents.
- Federation (локальный ресурс исходного примера не включён) — peer-to-peer sharing of beads
  across repos and organizations.
- Bucket Federation Quickstart (локальный ресурс исходного примера не включён) — federate
  two machines through a GCS or S3 bucket, with no server to run.
- Multi-Repo Migration (локальный ресурс исходного примера не включён) — moving an
  existing single-repo setup to multi-repo routing.
