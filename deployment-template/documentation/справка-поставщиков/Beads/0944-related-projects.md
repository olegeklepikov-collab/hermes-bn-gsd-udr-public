> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: related-projects

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: Related Projects
description: Adjacent, independent projects that solve neighboring problems and compose well with beads
---

Adjacent or complementary tools that solve different problems in the
same neighborhood as Beads. These are not Beads integrations (see
Community Tools (локальный ресурс исходного примера не включён) for those) — they are
independent projects whose users may also find Beads useful, or vice
versa.

## Recall / knowledge graph

- **[scry](https://github.com/prmichaelsen/scry)** —
  ([scryspec.com](https://scryspec.com)) — marker-indexed knowledge
  and recall graph for AI coding agents. Files declare identity via
  inline `@scry.entry` markers; the index makes designs, lessons, and
  decisions reachable by meaning, tag, and seeded question rather than
  by path. Different job from Beads: where Beads is a task graph for
  *what to do next*, scry is a recall layer for *what was decided and
  why*. They compose — independently arrived at the same hash-based-ID
  convention (`bd-a1b2`, `~hash`) for the same reason: preventing
  collisions across multi-agent and multi-branch work.
