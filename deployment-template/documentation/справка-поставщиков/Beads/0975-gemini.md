> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Beads: gemini

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: Gemini CLI
description: Set up beads for Gemini CLI with SessionStart hooks that run bd prime and GEMINI.md workflow guidance
---

Use Beads with Gemini CLI through SessionStart hooks and `GEMINI.md` guidance.

```bash
bd setup gemini
bd setup gemini --check
```

By default, setup installs global hooks in `~/.gemini/settings.json`. For project-local hooks, use:

```bash
bd setup gemini --project
```

The hook runs `bd prime --hook-json` so Gemini receives compact Beads workflow context at session start. The setup also writes Beads guidance to `GEMINI.md`.

## Stealth Mode

For CI or other environments where setup should avoid git operations:

```bash
bd setup gemini --stealth
bd setup gemini --project --stealth
```

## Remove

```bash
bd setup gemini --remove
bd setup gemini --project --remove
```
