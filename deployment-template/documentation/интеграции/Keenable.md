> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Keenable: переносимое руководство

**Статус на целевой машине: требует собственной проверки.** Этот документ не передаёт действующий доступ, лицензию, библиотеку или результат авторизации другого пользователя.

## Назначение

Поиск и чтение веб-источников, создание таблиц по нескольким страницам, повторные SELECT-запросы и отчёты с происхождением данных.

## Способы подключения

Отдельные веб- и SELECT-интерфейсы, официальный CLI и API.

Доступ: **Собственный ключ; публичный режим — при наличии у поставщика**. Официальная точка начала: [сайт/интерфейс поставщика](https://app.keenable.ai/console/api-keys). Состав методов сверяется с текущим каталогом выбранной версии и правами собственного аккаунта.

## Последовательность настройки

1. Выбрать поддерживаемые ОС/архитектуру и способ подключения. Для собственного переходника установить его программу отдельно; Markdown-контракт сам её не создаёт.
2. Создать или выбрать собственный аккаунт/местный профиль. Выполнить новый вход, запросить свои права и сохранить реквизиты в защищённом месте.
3. Заполнить необходимые параметры из общего справочника. Для библиотеки, базы, проекта и рабочих пространств получить новые идентификаторы.
4. Установить адаптированный навык и выбранные методы; включать подключение после проверки. Платные уровни, внешние адресаты и публикация выбираются отдельно.
5. Выполнить ограниченный тест чтения, ошибок и, если нужна запись, версии/отсутствия дубля. Проверить используемые CLI, приложение и канал сообщений.
6. Сохранить собственный протокол с датой, версией и фактическим охватом. До этого состояние не объявляется проверенным.

## Ограничения и интерпретация

SELECT является производным извлечением; ячейки сверяются с оригиналом. Публикация отчёта и его удаление требуют отдельного определённого задания.

Остатки, тарифы, письма поддержки и разрешения другой установки не применяются к этому аккаунту. Текущие квоты и условия определяются собственным интерфейсом поставщика. Данные, ключи и решения о переносе файлов оформляются отдельно от документации.

## Шаблоны и контракты

- [batch.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Keenable/examples--batch.json.md)
- [fetch.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Keenable/examples--fetch.json.md)
- [mcp-fetch.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Keenable/examples--mcp-fetch.json.md)
- [mcp-search.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Keenable/examples--mcp-search.json.md)
- [overrides.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Keenable/examples--overrides.json.md)
- [report-revoke.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Keenable/examples--report-revoke.json.md)
- [report.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Keenable/examples--report.json.md)
- [search.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Keenable/examples--search.json.md)
- [select.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Keenable/examples--select.json.md)
- [api-schema.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Keenable/%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8--api-schema.json.md)
- [mcp-public-schema.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Keenable/%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8--mcp-public-schema.json.md)
- [mcp-select-schema.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Keenable/%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8--mcp-select-schema.json.md)
- [mcp-web-schema.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Keenable/%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8--mcp-web-schema.json.md)

## Сохранённая публичная справка

- [api-reference](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0186-api-reference.md)
- [api-reference](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0187-api-reference.md)
- [authentication](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0188-authentication.md)
- [authentication](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0189-authentication.md)
- [cli-md](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0194-cli-md.md)
- [cli-readme](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0195-cli-readme.md)
- [cli](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0197-cli.md)
- [cli](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0198-cli.md)
- [doc-0](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0199-doc-0.md)
- [doc-1](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0200-doc-1.md)
- [doc-2](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0201-doc-2.md)
- [doc-3](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0202-doc-3.md)
- [doc-4](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0203-doc-4.md)
- [doc-5](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0204-doc-5.md)
- [hermes](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0205-hermes.md)
- [index](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0206-index.md)
- [pay-per-request](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0207-pay-per-request.md)
- [privacy](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0208-privacy.md)
- [privacy](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0209-privacy.md)
- [rate-limits](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0210-rate-limits.md)
- [rate-limits](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0211-rate-limits.md)
- [select-md](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0212-select-md.md)
- [select](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0213-select.md)
- [terms](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0214-terms.md)
- [terms](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0215-terms.md)
- [time-machine](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0216-time-machine.md)
- [time-machine](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Keenable/0217-time-machine.md)

[Оглавление](../README.md) · [Параметры целевой установки](../00-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%BF%D0%B5%D1%80%D0%B5%D0%BD%D0%BE%D1%81%D0%B0.md) · [Проверка после настройки](../06-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%BD%D0%B0-%D0%BD%D0%BE%D0%B2%D0%BE%D0%B9-%D0%BC%D0%B0%D1%88%D0%B8%D0%BD%D0%B5.md)
