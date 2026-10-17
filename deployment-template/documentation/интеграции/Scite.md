> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Scite: переносимое руководство

**Статус на целевой машине: требует собственной проверки.** Этот документ не передаёт действующий доступ, лицензию, библиотеку или результат авторизации другого пользователя.

## Назначение

Контексты и категории цитирований, поиск научных свидетельств, чтение разрешённого полного текста, библиотечные подборки, заметки и журнал использованных источников.

## Способы подключения

Официальный MCP; ключ не является обязательным при выбранном OAuth.

Доступ: **Новый OAuth-вход либо собственный ключ**. Официальная точка начала: [сайт/интерфейс поставщика](https://api.scite.ai/mcp). Состав методов сверяется с текущим каталогом выбранной версии и правами собственного аккаунта.

## Последовательность настройки

1. Выбрать поддерживаемые ОС/архитектуру и способ подключения. Для собственного переходника установить его программу отдельно; Markdown-контракт сам её не создаёт.
2. Создать или выбрать собственный аккаунт/местный профиль. Выполнить новый вход, запросить свои права и сохранить реквизиты в защищённом месте.
3. Заполнить необходимые параметры из общего справочника. Для библиотеки, базы, проекта и рабочих пространств получить новые идентификаторы.
4. Установить адаптированный навык и выбранные методы; включать подключение после проверки. Платные уровни, внешние адресаты и публикация выбираются отдельно.
5. Выполнить ограниченный тест чтения, ошибок и, если нужна запись, версии/отсутствия дубля. Проверить используемые CLI, приложение и канал сообщений.
6. Сохранить собственный протокол с датой, версией и фактическим охватом. До этого состояние не объявляется проверенным.

## Ограничения и интерпретация

Контекст и категория цитирования не равны истинности вывода. Возможны ограничения полного текста и экспорта; отмечать фактический охват сети.

Остатки, тарифы, письма поддержки и разрешения другой установки не применяются к этому аккаунту. Текущие квоты и условия определяются собственным интерфейсом поставщика. Данные, ключи и решения о переносе файлов оформляются отдельно от документации.

## Шаблоны и контракты

- [mcp-selected.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Scite/config--mcp-selected.json.md)
- [profiles.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Scite/config--profiles.json.md)
- [rest-openapi.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Scite/%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8--rest-openapi.json.md)

## Сохранённая публичная справка

- [api-docs](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0281-api-docs.md)
- [docs-index](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0282-docs-index.md)
- [index](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0283-index.md)
- [mcp-terms](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0284-mcp-terms.md)
- [pricing](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0285-pricing.md)
- [agents](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0286-agents.md)
- [authentication](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0287-authentication.md)
- [enterprise-access-and-sso](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0289-enterprise-access-and-sso.md)
- [errors-and-rate-limits](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0290-errors-and-rate-limits.md)
- [introduction](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0291-introduction.md)
- [pricing-and-plans](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0292-pricing-and-plans.md)
- [quickstart](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0293-quickstart.md)
- [get-scite-journal-index-for-issn](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0295-get-scite-journal-index-for-issn.md)
- [get-scite-journal-index-for-multiple-issns](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0296-get-scite-journal-index-for-multiple-issns.md)
- [get-smart-citation-tallies-for-a-journal](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0297-get-smart-citation-tallies-for-a-journal.md)
- [get-yearly-scite-index-for-a-journal](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0298-get-yearly-scite-index-for-a-journal.md)
- [get-assistant-task](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0299-get-assistant-task.md)
- [start-an-assistant-query](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0300-start-an-assistant-query.md)
- [get-510k-summary-pdf-detail](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0301-get-510k-summary-pdf-detail.md)
- [get-510k-summary-pdfs-facets](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0302-get-510k-summary-pdfs-facets.md)
- [get-510k-summary-pdfs-schema](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0303-get-510k-summary-pdfs-schema.md)
- [get-clinical-trial-detail](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0304-get-clinical-trial-detail.md)
- [get-clinical-trials-facets](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0305-get-clinical-trials-facets.md)
- [get-clinical-trials-schema](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0306-get-clinical-trials-schema.md)
- [get-device-510k-detail](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0307-get-device-510k-detail.md)
- [get-device-510k-facets](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0308-get-device-510k-facets.md)
- [get-device-510k-schema](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0309-get-device-510k-schema.md)
- [get-drug-detail](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0310-get-drug-detail.md)
- [get-drugs-facets](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0311-get-drugs-facets.md)
- [get-drugs-schema](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0312-get-drugs-schema.md)
- [get-faers-facets](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0313-get-faers-facets.md)
- [get-faers-report-detail](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0314-get-faers-report-detail.md)
- [get-faers-schema](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0315-get-faers-schema.md)
- [get-grant-detail](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0316-get-grant-detail.md)
- [get-grants-facets](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0317-get-grants-facets.md)
- [get-grants-schema](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0318-get-grants-schema.md)
- [get-maude-facets](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0319-get-maude-facets.md)
- [get-maude-report-detail](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0320-get-maude-report-detail.md)
- [get-maude-schema](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0321-get-maude-schema.md)
- [get-mhra-alert-detail](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0322-get-mhra-alert-detail.md)
- [get-mhra-facets](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0323-get-mhra-facets.md)
- [get-mhra-schema](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0324-get-mhra-schema.md)
- [get-patent-detail](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0325-get-patent-detail.md)
- [get-patent-facets](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0326-get-patent-facets.md)
- [get-patent-schema](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0327-get-patent-schema.md)
- [search-510k-summary-pdfs](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0328-search-510k-summary-pdfs.md)
- [search-clinical-trials](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0329-search-clinical-trials.md)
- [search-device-510k-clearances](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0330-search-device-510k-clearances.md)
- [search-faers-drug-adverse-event-reports](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0331-search-faers-drug-adverse-event-reports.md)
- [search-fda-drug-labels-orange-book-and-drugs@fda](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0332-search-fda-drug-labels-orange-book-and-drugs-fda.md)
- [search-grants](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0333-search-grants.md)
- [search-maude-adverse-event-reports](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0334-search-maude-adverse-event-reports.md)
- [search-mhra-alerts](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0335-search-mhra-alerts.md)
- [search-patents](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0336-search-patents.md)
- [get-aggregate-tally](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0337-get-aggregate-tally.md)
- [get-multiple-tallies-bulk-get-with-body-—-prefer-post](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0338-get-multiple-tallies-bulk-get-with-body---prefer-post.md)
- [get-multiple-tallies-bulk-post](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0339-get-multiple-tallies-bulk-post.md)
- [get-section-tallies](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0340-get-section-tallies.md)
- [get-section-tally](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0341-get-section-tally.md)
- [get-tally](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0342-get-tally.md)
- [get-multiple-papers-bulk-get-with-body-—-prefer-post](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0343-get-multiple-papers-bulk-get-with-body---prefer-post.md)
- [get-multiple-papers-bulk-post](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0344-get-multiple-papers-bulk-post.md)
- [get-papers-by-target](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0345-get-papers-by-target.md)
- [get-single-paper](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0346-get-single-paper.md)
- [resolve-pmid-to-doi](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0347-resolve-pmid-to-doi.md)
- [retrieve-aggregated-citation-statistics-for-an-author](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0348-retrieve-aggregated-citation-statistics-for-an-author.md)
- [retrieve-author-metadata-and-papers-by-author-slug](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0349-retrieve-author-metadata-and-papers-by-author-slug.md)
- [retrieve-distinct-references-from-a-publication](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0350-retrieve-distinct-references-from-a-publication.md)
- [retrieve-distinct-references-to-a-publication](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0351-retrieve-distinct-references-to-a-publication.md)
- [get-search-results-from-a-query](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0352-get-search-results-from-a-query.md)
- [get-recommended-papers-to-read-given-a-doi](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0353-get-recommended-papers-to-read-given-a-doi.md)
- [cancel-task](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0354-cancel-task.md)
- [get-result-url](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0355-get-result-url.md)
- [get-result](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0356-get-result.md)
- [post-reference-check](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0357-post-reference-check.md)
- [receive-citations-with-the-doi-as-a-source-paper](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0358-receive-citations-with-the-doi-as-a-source-paper.md)
- [receive-citations-with-the-doi-as-a-target-paper](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0359-receive-citations-with-the-doi-as-a-target-paper.md)
- [create-a-collection-from-a-list-of-dois-or-a-search-query](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0360-create-a-collection-from-a-list-of-dois-or-a-search-query.md)
- [delete-a-collection-by-slug](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0361-delete-a-collection-by-slug.md)
- [get-a-collection-by-slug](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0362-get-a-collection-by-slug.md)
- [update-a-collection-by-slug](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0363-update-a-collection-by-slug.md)
- [overview](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0364-overview.md)
- [prompts](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0365-prompts.md)
- [collections](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0366-collections.md)
- [evidence](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0367-evidence.md)
- [literature](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0368-literature.md)
- [overview](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0369-overview.md)
- [assistant](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0370-assistant.md)
- [collections](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0371-collections.md)
- [papers-and-authors](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0372-papers-and-authors.md)
- [reference-check](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0373-reference-check.md)
- [search](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0374-search.md)
- [smart-citations](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0375-smart-citations.md)
- [zotero-plugin](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0376-zotero-plugin.md)
- [adverse-events](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0377-adverse-events.md)
- [clinical-trials](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0378-clinical-trials.md)
- [devices](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0379-devices.md)
- [drugs](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0380-drugs.md)
- [grants](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0381-grants.md)
- [overview](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0382-overview.md)
- [patents](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0383-patents.md)
- [safety-alerts](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0384-safety-alerts.md)
- [citation-model](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0385-citation-model.md)
- [glossary](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Scite/0386-glossary.md)

[Оглавление](../README.md) · [Параметры целевой установки](../00-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%BF%D0%B5%D1%80%D0%B5%D0%BD%D0%BE%D1%81%D0%B0.md) · [Проверка после настройки](../06-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%BD%D0%B0-%D0%BD%D0%BE%D0%B2%D0%BE%D0%B9-%D0%BC%D0%B0%D1%88%D0%B8%D0%BD%D0%B5.md)
