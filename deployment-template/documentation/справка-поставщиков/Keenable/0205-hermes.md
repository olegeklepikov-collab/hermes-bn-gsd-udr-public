> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Keenable: hermes

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.keenable.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Hermes Agent

> Keenable is built into Hermes Agent as a web backend for web_search and web_extract, and works without a key.

*Built-in web backend*

Keenable ships inside [Hermes Agent](https://hermes-agent.nousresearch.com/) as a bundled web backend. It serves both of Hermes's web tools, `web_search` and `web_extract`, with no plugin to install and no account to create.

→ [View the provider on GitHub](https://github.com/NousResearch/hermes-agent/tree/main/plugins/web/keenable)

A fresh install with no web credentials already reaches Keenable some of the time: Hermes rotates keyless requests across the public free tiers of Exa, Parallel, Firecrawl and Keenable, and moves to the next vendor when one is rate-limited. With a Nous Portal sign-in, including the desktop app's free guest tier, `web_search` goes to Nous's managed search instead. Select Keenable and every call goes to Keenable, so results stay consistent from one run to the next, with or without a key.

## Install

### Install Hermes Agent

On Linux, macOS, WSL2 or Termux:

```bash theme={"system"}
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

On native Windows, in PowerShell:

```powershell theme={"system"}
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

Nothing Keenable-specific to install: the backend is part of Hermes itself.

### Select Keenable

Run `hermes tools` and pick **Keenable · Free (keyless)** for web search and extract, or set it directly:

```bash theme={"system"}
hermes config set web.backend keenable
```

A backend you select always wins over the rotation and over the managed search. To use Keenable for only one of the two tools, set `web.search_backend` or `web.extract_backend` instead of `web.backend`.

### Add an API key (optional)

```bash theme={"system"}
hermes config set KEENABLE_API_KEY keen_<your_key>
```

Hermes keeps the key in `~/.hermes/.env` and sends it to Keenable's authenticated endpoint. On an install where no backend was ever selected, the key alone is enough for Hermes to pick Keenable, unless a Tavily, Perplexity, Exa or Parallel key is set too. Create one in the console](https://app.keenable.ai/console); see [Authentication (локальный ресурс исходного примера не включён). In `hermes tools`, **Keenable · Paid (API key)** pins the keyed path, so a missing key fails with an error instead of dropping to the free tier, while **Free (keyless)** stays keyless even after you add a key.

### Check it

```bash theme={"system"}
hermes doctor
hermes config get web.backend
```

`hermes doctor` reports whether `web_search` and `web_extract` are ready. Then start `hermes` and ask something that needs the web.

<Note>
  Set `KEENABLE_API_KEY` to authenticate — this removes the hourly request cap. Without a key, calls run on the shared public tier at lower rate limits (локальный ресурс исходного примера не включён).
</Note>

## The `hermes-keenable-web` plugin

Before Keenable was bundled, this page pointed to a standalone PyPI plugin, `hermes-keenable-web`. The built-in backend replaces it. If you installed the plugin, uninstall it from the environment Hermes runs in (`pip uninstall hermes-keenable-web`), or delete `~/.hermes/plugins/web/keenable/` if you copied it there by hand: it registers under the same name, `keenable`, and takes the built-in backend's place.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
