> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: restore

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: "bd restore"
description: "Restore the pre-compaction content of a compacted issue."
---

{/* AUTO-GENERATED: do not edit manually */}

Generated from `bd help --doc restore`.

Restore the pre-compaction content of a compacted issue.

When an issue is compacted, its description/design/notes/acceptance criteria
are summarized and the originals are archived to a compaction snapshot. This
command recovers that original content.

By default it is read-only: it displays the archived content without modifying
the database. Pass --apply to write the original content back into the issue
and step its compaction level back down.

If no archived snapshot exists (e.g. the issue was compacted by an older bd
before snapshot archiving), restore falls back to a best-effort reconstruction
from Dolt version history, which can only be displayed, not applied.

```
bd restore <issue-id> [flags]
```

**Flags:**

```
      --apply   Write the restored content back into the issue (default: display only)
      --json    Output restore results in JSON format
```
