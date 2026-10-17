> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: index

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: Introduction
description: Dependency-aware, Dolt-backed issue tracker built for AI coding agents that survive context loss
---

**Beads** (`bd`) is a Dolt-powered issue tracker designed for AI-supervised coding workflows.

These docs are for the 1.3.0 release of beads — see the v1.3.0 release notes](https://github.com/gastownhall/beads/releases/tag/v1.3.0). Upgrading from 1.2.2 or earlier crosses a schema migration; read [Upgrading (локальный ресурс исходного примера не включён) first.

## Why Beads?

Traditional issue trackers (Jira, GitHub Issues) weren't designed for AI agents. Beads was built from the ground up for:

- **AI-native workflows** - Hash-based IDs prevent collisions when multiple agents work concurrently
- **Dolt-backed storage** - Issues stored in a version-controlled SQL database, enabling collaboration via Dolt-native replication
- **Dependency-aware execution** - `bd ready` shows only unblocked work
- **Formula system** - Declarative templates for repeatable workflows
- **Multi-agent coordination** - Routing, gates, and molecules for complex workflows

## Quick Start

```bash
# Install via Homebrew (macOS/Linux)
brew install beads

# Or quick install (macOS/Linux/FreeBSD)
curl -fsSL https://raw.githubusercontent.com/gastownhall/beads/main/scripts/install.sh | bash

# Initialize in your project
cd your-project
bd init --quiet

# Create your first issue
bd create "Set up database" -p 1 -t task

# See ready work
bd ready
```

## Core Concepts

The whole model on one page: How Beads Works (локальный ресурс исходного примера не включён).

| Concept | Description |
|---------|-------------|
| **Beads (issues)** (локальный ресурс исходного примера не включён) | Work items with priorities, types, labels, and dependencies |
| **Dependencies** (локальный ресурс исходного примера не включён) | `blocks`, `parent-child`, `discovered-from`, `related` |
| **Sync** (локальный ресурс исходного примера не включён) | Dolt push/pull over your git remote — no server to run |
| **Formulas** (локальный ресурс исходного примера не включён) | Declarative workflow templates (TOML or JSON) |
| **Molecules** (локальный ресурс исходного примера не включён) | Work graphs instantiated from formulas |
| **Gates** (локальный ресурс исходного примера не включён) | Async coordination primitives (human, timer, GitHub) |

## For AI Agents

Beads is optimized for AI coding agents:

```bash
# Always use --json for programmatic access
bd list --json
bd show bd-42 --json

# Track discovered work during implementation
bd create "Found bug in auth" --description="Details..." \
  --deps discovered-from:bd-100 --json

# Push changes at end of session
bd dolt push
```

See the Claude Code integration (локальный ресурс исходного примера не включён) for detailed agent instructions.

## Architecture

```
Dolt DB (.beads/embeddeddolt/ in embedded mode,
         .beads/dolt/ in server mode; gitignored)
    ↕ dolt commit
Local Dolt history
    ↕ dolt push/pull
Remote Dolt repository (shared across machines)
```

The magic is automatic synchronization via Dolt's version-controlled database with built-in replication.

## Next Steps

- Installation (локальный ресурс исходного примера не включён) - Get bd installed
- Quick Start (локальный ресурс исходного примера не включён) - Create your first issues
- How Beads Works (локальный ресурс исходного примера не включён) - The concept model on one page
- CLI Reference (локальный ресурс исходного примера не включён) - All available commands
- Workflows (локальный ресурс исходного примера не включён) - Formulas, molecules, and gates
