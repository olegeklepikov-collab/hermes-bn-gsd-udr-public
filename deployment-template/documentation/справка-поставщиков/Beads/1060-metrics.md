> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: metrics

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: "bd metrics"
description: "Show whether anonymous usage metrics are on, see exactly what is sent, and"
---

{/* AUTO-GENERATED: do not edit manually */}

Generated from `bd help --doc metrics`.

Show whether anonymous usage metrics are on, see exactly what is sent, and
turn them on or off.

bd shares anonymous usage metrics to learn how people actually use it — just
which commands get run, plus the bd version and OS platform. That's how we decide
what to polish next. We never collect your issues, paths, remotes, identity, or
any user-supplied text.

  bd metrics            show the current status and what is collected
  bd metrics on         turn metrics on
  bd metrics off        turn metrics off
  bd metrics example    show real examples of the events bd sends

```
bd metrics [flags]
```

## bd metrics example

Show real examples of the anonymous metrics bd sends

```
bd metrics example [flags]
```

## bd metrics off

Turn anonymous usage metrics off

```
bd metrics off [flags]
```

## bd metrics on

Turn anonymous usage metrics on

```
bd metrics on [flags]
```
