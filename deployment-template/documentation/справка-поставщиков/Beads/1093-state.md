> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: state

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: "bd state"
description: "Query the current value of a state dimension from an issue's labels."
---

{/* AUTO-GENERATED: do not edit manually */}

Generated from `bd help --doc state`.

Query the current value of a state dimension from an issue's labels.

State labels follow the convention &lt;dimension&gt;:&lt;value&gt;, for example:
  patrol:active
  mode:degraded
  health:healthy

This command extracts the value for a given dimension.

Examples:
  bd state witness-abc patrol     # Output: active
  bd state witness-abc mode       # Output: normal
  bd state witness-abc health     # Output: healthy

```
bd state <issue-id> <dimension> [flags]
```

## bd state list

List all state labels (dimension:value format) on an issue.

This filters labels to only show those following the state convention.

Example:
  bd state list witness-abc
  # Output:
  #   patrol: active
  #   mode: normal
  #   health: healthy

```
bd state list <issue-id> [flags]
```
