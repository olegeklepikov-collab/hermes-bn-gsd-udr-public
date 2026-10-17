> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# R: options.json

Это переносимый справочный контракт/каталог. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
[
  {
    "name": "R / Rscript",
    "use": "Местное выполнение скриптов и пакетные расчёты",
    "url": "https://www.r-project.org/"
  },
  {
    "name": "mcptools + btw, stdio MCP",
    "use": "Расчёты, объекты, документация и графика из Hermes",
    "url": "https://posit-dev.github.io/mcptools/articles/server.html"
  },
  {
    "name": "btw groups docs/env/sessioninfo/cran/run",
    "use": "14 исследовательских методов; другие группы рассмотрены отдельно",
    "url": "https://posit-dev.github.io/btw/reference/btw_tools.html"
  },
  {
    "name": "renv",
    "use": "Фиксация и восстановление библиотек проекта",
    "url": "https://rstudio.github.io/renv/articles/renv.html"
  },
  {
    "name": "R Markdown / knitr / Pandoc",
    "use": "Воспроизводимые самостоятельные HTML-отчёты",
    "url": "https://rmarkdown.rstudio.com/"
  },
  {
    "name": "RStudio / Positron + interactive R session",
    "use": "Общая интерактивная рабочая среда; отдельная настройка сеансов",
    "url": "https://posit-dev.github.io/mcptools/articles/server.html"
  },
  {
    "name": "HTTP MCP / Posit Connect",
    "use": "Сетевое и многопользовательское развёртывание с отдельным управлением доступом",
    "url": "https://github.com/posit-dev/mcptools"
  },
  {
    "name": "R as MCP client / ellmer / btw chat",
    "use": "Самостоятельное приложение R с языковой моделью; отдельное подключение провайдера",
    "url": "https://ellmer.tidyverse.org/"
  },
  {
    "name": "Quarto / Jupyter IRkernel",
    "use": "Многоформатные блокноты и публикации; добавляются по формату работы",
    "url": "https://quarto.org/"
  },
  {
    "name": "Shiny",
    "use": "Собственные интерактивные аналитические приложения",
    "url": "https://shiny.posit.co/"
  },
  {
    "name": "reticulate / Python interoperability",
    "use": "Программный обмен R/Python при отдельной задаче",
    "url": "https://rstudio.github.io/reticulate/"
  },
  {
    "name": "Specialized CRAN / Bioconductor / Stan / sf / Arrow",
    "use": "Специализированные исследования, MCMC, пространственные и крупные колоночные данные; не установлены в текущий набор",
    "url": "https://cran.r-project.org/web/views/"
  }
]
```
