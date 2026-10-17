> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: defer

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: "bd defer"
description: "Defer issues to put them on ice for later."
---

{/* AUTO-GENERATED: do not edit manually */}

Generated from `bd help --doc defer`.

Defer issues to put them on ice for later.

Deferred issues are deliberately set aside - not blocked by anything specific,
just postponed for future consideration. Unlike blocked issues, there's no
dependency keeping them from being worked. Unlike closed issues, they will
be revisited.

Deferred issues don't show in 'bd ready' but remain visible in 'bd list'.

Examples:
  bd defer bd-abc                  # Defer a single issue (status-based)
  bd defer bd-abc --until=tomorrow # Defer until specific time
  bd defer bd-abc --reason="waiting on API access"
  bd defer bd-abc bd-def           # Defer multiple issues

```
bd defer [id...] [flags]
```

**Flags:**

```
      --reason string   Record why this issue is being deferred (appended to notes)
      --until string    Defer until specific time (e.g., +1h, tomorrow, next monday)
```
