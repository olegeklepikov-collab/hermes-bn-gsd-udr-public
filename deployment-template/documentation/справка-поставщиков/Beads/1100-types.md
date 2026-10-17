> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: types

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: "bd types"
description: "List all valid issue types that can be used with bd create --type."
---

{/* AUTO-GENERATED: do not edit manually */}

Generated from `bd help --doc types`.

List all valid issue types that can be used with bd create --type.

Core work types (bug, task, feature, chore, epic, decision) are always valid.
Additional types require configuration via types.custom in .beads/config.yaml.

Examples:
  bd types              # List all types with descriptions
  bd types --json       # Output as JSON


```
bd types [flags]
```
