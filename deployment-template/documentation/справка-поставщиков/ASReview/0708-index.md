> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка ASReview: index

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
myst:
  html_meta:
    "description lang=en": |
      Top-level documentation for pydata-sphinx theme, with links to the rest
      of the site..
html_theme.sidebar_secondary.remove: true
---

# The ASReview LAB documentation

Join the movement towards fast, open, and transparent systematic reviews.

```{gallery-grid}
:grid-columns: 1 2 2 3

- header: "{fas}`bolt;pst-color-primary` Fast screening"
  content: "Powerful and customizable AI to screen large volumes of text, achieving up to 95% time savings."
  link: "https://doi.org/10.1038/s42256-020-00287-7"
- header: "{fas}`eye;pst-color-primary` Transparant and reproducible"
  content: "Engage in a fully open and transparent interaction with the AI where you are the oracle."
  link: "https://osf.io/preprints/psyarxiv/g93zf"
- header: "{fas}`circle-half-stroke;pst-color-primary` Customizable interface"
  content: "Customize your review environment, offering light and dark modes, adding tags and AI-aided highlighting."
- header: "{fas}`lightbulb;pst-color-primary` Simulate and validate"
  content: "Utilize the robust simulation tool to predict AI performance and validate your, another reviewer’s or LLM findings"
  link: "lab/simulation_overview.html"
- header: "{fas}`microchip;pst-color-primary` CLI and API"
  content: "Access extensive command-line options and API integration for advanced customization."
  link: "technical/index.html"
- header: "{fas}`users;pst-color-primary` Community"
  content: "Join a community where open discussions and shared insights contribute to the continuous improvement."
  link: "https://github.com/asreview/asreview/discussions"
```

## ASReview LAB explained in 2 minutes

```{youtube} k-a2SCq-LtA
:align: center
```

## User guide


```{toctree}
:maxdepth: 2

lab/index
```

## Server guide

All documentation for the ASReview LAB Server

```{toctree}
:maxdepth: 2

server/index
```

## Technical guide

All technical documentation and reources

```{toctree}
:maxdepth: 2

technical/index
```
