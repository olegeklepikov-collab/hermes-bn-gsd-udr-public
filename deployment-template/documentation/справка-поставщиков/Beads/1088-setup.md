> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: setup

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: "bd setup"
description: "Setup integration files for AI editors and coding assistants."
---

{/* AUTO-GENERATED: do not edit manually */}

Generated from `bd help --doc setup`.

Setup integration files for AI editors and coding assistants.

Recipes define where beads workflow instructions are written. Built-in recipes
include cursor, claude, copilot, gemini, aider, factory, codex, mux, opencode, junie, windsurf, cody, and kilocode.

Examples:
  bd setup cursor          # Install Cursor IDE integration
  bd setup codex           # Install Codex skill + AGENTS.md guidance + native hooks
  bd setup codex --global  # Install global Codex skill + guidance + native hooks
  bd setup copilot         # Install Copilot CLI plugin + repository instructions
  bd setup mux --project   # Install Mux workspace layer (.mux/AGENTS.md)
  bd setup mux --global    # Install Mux global layer (~/.mux/AGENTS.md)
  bd setup mux --project --global  # Install both Mux layers
  bd setup --list          # Show all available recipes
  bd setup --print         # Print the template to stdout
  bd setup -o rules.md     # Write template to custom path
  bd setup --add myeditor .myeditor/rules.md  # Add custom recipe

Use 'bd setup &lt;recipe&gt; --check' to verify installation status.
Use 'bd setup &lt;recipe&gt; --remove' to uninstall.

```
bd setup [recipe] [flags]
```

**Flags:**

```
      --add string      Add a custom recipe with given name
      --check           Check if integration is installed
      --global          Install globally (claude/codex/mux; writes to ~/.claude/settings.json, $CODEX_HOME/AGENTS.md or ~/.codex/AGENTS.md, or ~/.mux/AGENTS.md)
      --list            List all available recipes
  -o, --output string   Write template to custom path
      --print           Print the template to stdout
      --project         Install for this project only (gemini/mux)
      --remove          Remove the integration
      --stealth         Use stealth mode (claude/gemini)
```
