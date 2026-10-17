> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: RECOVERY

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Recovery Playbooks

The recovery playbooks moved to [docs/recovery/](0949-index.md), rendered
on the docs site at
[https://beads.gascity.com/recovery/](https://beads.gascity.com/recovery/).

> **Why this file exists:** released `bd` binaries print URLs into this file —
> v1.1.0's Dolt merge-refusal guidance (`printAncestorPKMismatchGuidance`,
> `cmd/bd/dolt.go` at tag `v1.1.0`) prints `docs/RECOVERY.md#pk-fork-refused`.
> This stub keeps those printed links landing on a page that points at the
> live playbooks. Do not delete it while released binaries still print it; it
> is a deliberate exception to the no-pointer-stubs rule, registered in
> `test/docsync`.
