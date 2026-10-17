> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Tavily: переносимое руководство

**Статус на целевой машине: требует собственной проверки.** Этот документ не передаёт действующий доступ, лицензию, библиотеку или результат авторизации другого пользователя.

## Назначение

Веб-поиск, тематический поиск новостей и финансов, извлечение, карта и обход сайтов, углублённые исследования с опросом состояния и потоковой выдачей.

## Способы подключения

Официальный удалённый MCP либо отдельный полный переходник API; их наборы методов различаются.

Доступ: **Собственный API-ключ**. Официальная точка начала: [сайт/интерфейс поставщика](https://app.tavily.com/). Состав методов сверяется с текущим каталогом выбранной версии и правами собственного аккаунта.

## Последовательность настройки

1. Выбрать поддерживаемые ОС/архитектуру и способ подключения. Для собственного переходника установить его программу отдельно; Markdown-контракт сам её не создаёт.
2. Создать или выбрать собственный аккаунт/местный профиль. Выполнить новый вход, запросить свои права и сохранить реквизиты в защищённом месте.
3. Заполнить необходимые параметры из общего справочника. Для библиотеки, базы, проекта и рабочих пространств получить новые идентификаторы.
4. Установить адаптированный навык и выбранные методы; включать подключение после проверки. Платные уровни, внешние адресаты и публикация выбираются отдельно.
5. Выполнить ограниченный тест чтения, ошибок и, если нужна запись, версии/отсутствия дубля. Проверить используемые CLI, приложение и канал сообщений.
6. Сохранить собственный протокол с датой, версией и фактическим охватом. До этого состояние не объявляется проверенным.

## Ограничения и интерпретация

Search/Extract/Map/Crawl и Research различаются по объёму/расходу. Проверять failed_results, статус асинхронной задачи и библиографические поля.

Остатки, тарифы, письма поддержки и разрешения другой установки не применяются к этому аккаунту. Текущие квоты и условия определяются собственным интерфейсом поставщика. Данные, ключи и решения о переносе файлов оформляются отдельно от документации.

## Шаблоны и контракты

- [crawl.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Tavily/examples--crawl.json.md)
- [extract.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Tavily/examples--extract.json.md)
- [map.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Tavily/examples--map.json.md)
- [research-get-params.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Tavily/examples--research-get-params.json.md)
- [research-stream.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Tavily/examples--research-stream.json.md)
- [research.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Tavily/examples--research.json.md)
- [search.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Tavily/examples--search.json.md)
- [full-tool-catalog.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Tavily/full-tool-catalog.json.md)
- [tool-catalog.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Tavily/tool-catalog.json.md)
- [api-schemas.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Tavily/%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8--api-schemas.json.md)

## Сохранённая публичная справка

- [core-0](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0152-core-0.md)
- [core-1](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0153-core-1.md)
- [core-2](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0154-core-2.md)
- [core-3](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0155-core-3.md)
- [core-4](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0156-core-4.md)
- [doc-0](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0157-doc-0.md)
- [doc-1](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0158-doc-1.md)
- [doc-10](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0159-doc-10.md)
- [doc-11](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0160-doc-11.md)
- [doc-12](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0161-doc-12.md)
- [doc-13](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0162-doc-13.md)
- [doc-14](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0163-doc-14.md)
- [doc-15](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0164-doc-15.md)
- [doc-16](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0165-doc-16.md)
- [doc-17](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0166-doc-17.md)
- [doc-18](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0167-doc-18.md)
- [doc-19](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0168-doc-19.md)
- [doc-2](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0169-doc-2.md)
- [doc-20](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0170-doc-20.md)
- [doc-21](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0171-doc-21.md)
- [doc-22](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0172-doc-22.md)
- [doc-23](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0173-doc-23.md)
- [doc-3](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0174-doc-3.md)
- [doc-4](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0175-doc-4.md)
- [doc-5](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0176-doc-5.md)
- [doc-6](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0177-doc-6.md)
- [doc-7](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0178-doc-7.md)
- [doc-8](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0179-doc-8.md)
- [doc-9](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0180-doc-9.md)
- [feedback](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0181-feedback.md)
- [full-docs](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0182-full-docs.md)
- [mcp-readme](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0183-mcp-readme.md)
- [privacy-prose](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0184-privacy-prose.md)
- [privacy](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Tavily/0185-privacy.md)

[Оглавление](../README.md) · [Параметры целевой установки](../00-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%BF%D0%B5%D1%80%D0%B5%D0%BD%D0%BE%D1%81%D0%B0.md) · [Проверка после настройки](../06-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%BD%D0%B0-%D0%BD%D0%BE%D0%B2%D0%BE%D0%B9-%D0%BC%D0%B0%D1%88%D0%B8%D0%BD%D0%B5.md)
