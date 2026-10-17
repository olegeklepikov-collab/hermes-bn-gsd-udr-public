> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: onboard

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: "bd onboard"
description: "Display a minimal snippet to add to your agent instructions file for bd integration."
---

{/* AUTO-GENERATED: do not edit manually */}

Generated from `bd help --doc onboard`.

Display a minimal snippet to add to your agent instructions file for bd integration.

By default, the agent instructions file is AGENTS.md. Use 'bd init --agents-file'
to configure a different filename (e.g. BEADS.md).

This outputs a small (~10 line) snippet that points to 'bd prime' for full
workflow context. This is the same minimal profile that 'bd init' generates
by default. This approach:

  • Keeps your agent file lean (doesn't bloat with instructions)
  • bd prime provides dynamic, always-current workflow details
  • Hooks auto-inject bd prime at session start

For agents or environments that do not auto-inject hook output, use
'bd init --agents-profile=full' to embed the complete command reference.

```
bd onboard [flags]
```
