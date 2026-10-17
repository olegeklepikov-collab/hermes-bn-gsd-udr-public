> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: zotero-plugin

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Scite Zotero plugin

> Install Scite's free Zotero plugin to see Smart Citation tallies and open Scite Reports from your Zotero library.

The Scite Zotero plugin brings citation context into your Zotero library. It adds sortable columns for supporting, contrasting, and mentioning citations, along with total Smart Citations and distinct citing publications.

No Scite account or API key is required.

<CardGroup cols={2}>
  <Card title="Download the latest plugin" icon="download" href="https://github.com/scitedotai/scite-zotero-plugin/releases/latest">
    Download the `.xpi` file for Zotero 7 and 8.
  </Card>

  <Card title="View source and releases" icon="github" href="https://github.com/scitedotai/scite-zotero-plugin">
    Review the source code, release notes, and known issues on GitHub.
  </Card>
</CardGroup>

<Note>
  Version 2 of the plugin supports Zotero 7 and 8. If you still use Zotero 6, install the [legacy v1.11.6 release](https://github.com/scitedotai/scite-zotero-plugin/releases/tag/v1.11.6).
</Note>

## Install the plugin

<Steps>
  <Step title="Download the XPI file">
    Open the [latest release](https://github.com/scitedotai/scite-zotero-plugin/releases/latest). Under **Assets**, download the file whose name ends in `.xpi`.

    If Firefox tries to install the file as a browser extension, right-click the download link and choose **Save Link As…** instead.
  </Step>

  <Step title="Open the Zotero Plugins Manager">
    In the Zotero desktop app, select **Tools → Plugins**.
  </Step>

  <Step title="Install the XPI file">
    Drag the downloaded `.xpi` file into the Plugins Manager. You can also click the gear icon, choose **Install Plugin From File…**, and select the file.
  </Step>

  <Step title="Finish installation">
    Confirm the installation and restart Zotero if prompted. Future plugin releases install automatically through Zotero's plugin updater.
  </Step>
</Steps>

Zotero plugins can access your Zotero data and your computer. Only install plugins from developers you trust. See [Zotero's plugin documentation](https://www.zotero.org/support/plugins) for more information.

## Show the Scite columns

The plugin adds five optional columns to the center pane of your Zotero library:

| Column | What it shows |
| - | - |
| **Supporting** | Citation statements that provide supporting evidence for the paper |
| **Contrasting** | Citation statements that provide contrasting evidence or results |
| **Mentioning** | Citation statements that mention the paper without supporting or contrasting it |
| **Total Smart Citations** | All citation statements Scite has extracted for the paper |
| **Total Distinct Citing Publications** | Unique publications that cite the paper |

To show them, right-click any column header in your library and select the Scite columns you want. You can resize and sort each column like other Zotero columns.

<Tip>
  Sort by **Supporting** to find papers with supporting evidence, or by **Contrasting** to find results that later research has challenged.
</Tip>

Smart Citation totals count individual citation statements. A single publication can cite the same paper more than once, so **Total Smart Citations** can be higher than **Total Distinct Citing Publications**. Learn more in Smart Citations (локальный ресурс исходного примера не включён).

## Open a Scite Report

Select a paper in your Zotero library, then click **View Scite Report** in the item pane. The report opens in your browser and shows the citation statements behind the tallies.

You can also right-click a library item to refresh its Scite citation data.

## Troubleshooting

### The Scite columns are missing

Right-click a column header and make sure the Scite columns are enabled. If they are not listed, open **Tools → Plugins**, confirm that the Scite plugin is enabled, and restart Zotero.

### An item has blank or zero counts

Scite usually matches a Zotero item by its DOI. Check that the parent item—not only its PDF attachment—has a valid DOI in its metadata. A zero can also mean that Scite has not identified any citation statements for that paper.

After correcting the metadata, right-click the item and refresh its citation data.

### Zotero says the plugin is incompatible

Install the release that matches your Zotero version. Version 2 supports Zotero 7 and 8. Zotero 6 requires the [legacy release](https://github.com/scitedotai/scite-zotero-plugin/releases/tag/v1.11.6).

### Firefox says the XPI is corrupt

Firefox may mistake a Zotero `.xpi` for a Firefox extension. Right-click the download link, select **Save Link As…**, and then install the saved file from Zotero.

### Disable or remove the plugin

Open **Tools → Plugins**, find **Scite Zotero Plugin**, and choose **Disable** or **Remove**. Disabling the plugin does not remove items from your Zotero library.

## Related

* Smart Citations (локальный ресурс исходного примера не включён): understand supporting, contrasting, and mentioning citations
* Collections (локальный ресурс исходного примера не включён): import papers from Zotero into a Scite Collection and monitor them over time
* [Report an issue](https://github.com/scitedotai/scite-zotero-plugin/issues): check known problems or contact the plugin maintainers


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
