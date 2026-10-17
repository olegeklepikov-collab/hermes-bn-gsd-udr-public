> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Crossref: переносимое руководство

**Статус на целевой машине: требует собственной проверки.** Этот документ не передаёт действующий доступ, лицензию, библиотеку или результат авторизации другого пользователя.

## Назначение

Проверка DOI и библиографии, поиск метаданных, авторов/фондов/организаций, связей, лицензий и изменений; форматы цитирования и ограниченные дополнительные интерфейсы.

## Способы подключения

Официальные REST/XML/OpenURL/OAI и выбранный переходник.

Доступ: **Собственный технический контакт для Polite; дополнительные права при необходимости**. Официальная точка начала: [сайт/интерфейс поставщика](https://www.crossref.org/documentation/retrieve-metadata/rest-api/). Состав методов сверяется с текущим каталогом выбранной версии и правами собственного аккаунта.

## Последовательность настройки

1. Выбрать поддерживаемые ОС/архитектуру и способ подключения. Для собственного переходника установить его программу отдельно; Markdown-контракт сам её не создаёт.
2. Создать или выбрать собственный аккаунт/местный профиль. Выполнить новый вход, запросить свои права и сохранить реквизиты в защищённом месте.
3. Заполнить необходимые параметры из общего справочника. Для библиотеки, базы, проекта и рабочих пространств получить новые идентификаторы.
4. Установить адаптированный навык и выбранные методы; включать подключение после проверки. Платные уровни, внешние адресаты и публикация выбираются отдельно.
5. Выполнить ограниченный тест чтения, ошибок и, если нужна запись, версии/отсутствия дубля. Проверить используемые CLI, приложение и канал сообщений.
6. Сохранить собственный протокол с датой, версией и фактическим охватом. До этого состояние не объявляется проверенным.

## Ограничения и интерпретация

Метаданные, optional abstract и ссылки не являются полным текстом. Проверять пропущенные поля, даты online/print и частичные ошибки пакетов.

Остатки, тарифы, письма поддержки и разрешения другой установки не применяются к этому аккаунту. Текущие квоты и условия определяются собственным интерфейсом поставщика. Данные, ключи и решения о переносе файлов оформляются отдельно от документации.

## Шаблоны и контракты

- [data-citations-openapi.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Crossref/config--data-citations-openapi.json.md)
- [openapi.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Crossref/config--openapi.json.md)
- [profiles.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Crossref/config--profiles.json.md)
- [tool-catalog.json](../%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D1%8B/Crossref/config--tool-catalog.json.md)

## Сохранённая публичная справка

- [README](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0586-README.md)
- [access](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0587-access.md)
- [access](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0588-access.md)
- [content-negotiation](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0589-content-negotiation.md)
- [content-negotiation](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0590-content-negotiation.md)
- [data-citations-announcement](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0591-data-citations-announcement.md)
- [data-citations-announcement](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0592-data-citations-announcement.md)
- [data-citations](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0593-data-citations.md)
- [data-citations](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0594-data-citations.md)
- [datacitations-swagger](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0595-datacitations-swagger.md)
- [datacitations-swagger](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0596-datacitations-swagger.md)
- [funder-ror](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0597-funder-ror.md)
- [funder-ror](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0598-funder-ror.md)
- [metadata-plus](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0599-metadata-plus.md)
- [oai](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0600-oai.md)
- [openurl](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0601-openurl.md)
- [openurl](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0602-openurl.md)
- [public-data-2026](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0603-public-data-2026.md)
- [public-data-2026](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0604-public-data-2026.md)
- [rate-limits](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0605-rate-limits.md)
- [rate-limits](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0606-rate-limits.md)
- [rest-api](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0607-rest-api.md)
- [rest](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0608-rest.md)
- [rest](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0609-rest.md)
- [retraction-watch](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0610-retraction-watch.md)
- [retraction-watch](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0611-retraction-watch.md)
- [swagger-ui](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0613-swagger-ui.md)
- [tips](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0614-tips.md)
- [tips](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0615-tips.md)
- [xml](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0616-xml.md)
- [xml](../%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/Crossref/0617-xml.md)

[Оглавление](../README.md) · [Параметры целевой установки](../00-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%BF%D0%B5%D1%80%D0%B5%D0%BD%D0%BE%D1%81%D0%B0.md) · [Проверка после настройки](../06-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%BD%D0%B0-%D0%BD%D0%BE%D0%B2%D0%BE%D0%B9-%D0%BC%D0%B0%D1%88%D0%B8%D0%BD%D0%B5.md)
