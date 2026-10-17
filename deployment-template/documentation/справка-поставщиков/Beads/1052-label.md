> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: label

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: "bd label"
description: "Manage issue labels"
---

{/* AUTO-GENERATED: do not edit manually */}

Generated from `bd help --doc label`.

Manage issue labels

```
bd label [flags]
```

## bd label add

Add a label to one or more issues

```
bd label add [issue-id...] [label] [flags]
```

## bd label list

List labels for an issue

```
bd label list [issue-id] [flags]
```

## bd label list-all

List all unique labels in the database

```
bd label list-all [flags]
```

## bd label propagate

Push a label from a parent down to all direct children that don't already have it. Useful for applying branch: labels across an epic's subtasks.

```
bd label propagate [parent-id] [label] [flags]
```

## bd label remove

Remove a label from one or more issues

```
bd label remove [issue-id...] [label] [flags]
```
