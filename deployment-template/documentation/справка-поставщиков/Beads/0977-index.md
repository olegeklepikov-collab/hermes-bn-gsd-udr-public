> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: index

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: Integrations
description: Browse every beads editor and agent integration, from bd setup recipes to MCP-based clients
---

Beads integration pages are based on two sources of support in the repository:

- Built-in `bd setup` recipes from `internal/recipes/recipes.go`
- First-party MCP integrations and editor guides already shipped in the repo

Run this command to see the built-in setup recipes supported by your installed `bd` binary:

```bash
bd setup --list
```

## Built-in Setup Recipes

| Recipe | Integration | Primary setup surface |
|--------|-------------|-----------------------|
| `aider` | Aider (локальный ресурс исходного примера не включён) | `.aider.conf.yml` and `.aider/` instructions |
| `claude` | Claude Code (локальный ресурс исходного примера не включён) | Claude hooks and `CLAUDE.md` |
| `codex` | Codex (локальный ресурс исходного примера не включён) | Beads skill, `AGENTS.md`, and Codex hooks |
| `cody` | Sourcegraph Cody (локальный ресурс исходного примера не включён) | `.cody/rules/beads.md` |
| `cursor` | Cursor (локальный ресурс исходного примера не включён) | `.cursor/rules/beads.mdc` + `.cursor/hooks.json` |
| `factory` | Factory.ai Droid (локальный ресурс исходного примера не включён) | `AGENTS.md` |
| `gemini` | Gemini CLI (локальный ресурс исходного примера не включён) | Gemini hooks and `GEMINI.md` |
| `junie` | Junie (локальный ресурс исходного примера не включён) | `.junie/guidelines.md` and MCP config |
| `kilocode` | Kilo Code (локальный ресурс исходного примера не включён) | `.kilocode/rules/beads.md` |
| `kiro` | Kiro CLI (локальный ресурс исходного примера не включён) | `.kiro/steering/beads.md` |
| `mux` | Mux (локальный ресурс исходного примера не включён) | `AGENTS.md`, optional `.mux/AGENTS.md`, and Mux hooks |
| `opencode` | OpenCode (локальный ресурс исходного примера не включён) | `AGENTS.md` |
| `windsurf` | Windsurf (локальный ресурс исходного примера не включён) | `.windsurf/rules/beads.md` |

## MCP-Based Integrations

These integrations use the Beads MCP server rather than a dedicated `bd setup` recipe:

- MCP Server (локальный ресурс исходного примера не включён) — the beads MCP server for any
  MCP-capable client.
- GitHub Copilot (локальный ресурс исходного примера не включён) — Copilot in VS Code via
  MCP.
- GitHub Copilot CLI (локальный ресурс исходного примера не включён) — the Copilot coding-agent
  CLI.

## Other Integration Surfaces

- Claude Code Plugin (локальный ресурс исходного примера не включён) — the packaged
  plugin with slash commands and MCP tools (`/plugin install beads`).
- Azure DevOps (локальный ресурс исходного примера не включён) — configuration reference for
  syncing beads with ADO work items.
