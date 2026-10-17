> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка ASReview: installation

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Installation

## Install ASReview LAB

ASReview LAB requires Python 3.10 or later. Detailed step-by-step instructions for installing Python and ASReview LAB are available for [Windows](https://asreview.ai/download) and [macOS/Linux](https://asreview.ai/download/) users.

To install ASReview LAB using Pip, run the following command in <span class="title-ref">CMD.exe</span> (Windows) or <span class="title-ref">Terminal</span> (macOS/Linux):

``` bash
pip install asreview
```

To start the application, use this command in <span class="title-ref">CMD.exe</span> or \`Terminal\`:

``` bash
asreview lab
```

The ASReview LAB application will open in your browser. For more options to start ASReview LAB, see `start`.

> [!NOTE]
> Refer to `troubleshooting` for solutions to common installation issues.

## Upgrade ASReview LAB

To upgrade ASReview LAB, run:

``` bash
pip install --upgrade asreview
```

## Uninstall ASReview LAB

To uninstall ASReview LAB, run:

``` bash
pip uninstall asreview
```

When prompted, enter `y` to confirm.

> [!WARNING]
> Uninstalling ASReview LAB does not delete your project files. These files are stored in the <span class="title-ref">.asreview</span> folder in your home directory.

## Server Installation

You can run ASReview LAB on a server or custom domain. Use the <span class="title-ref">ip</span> and <span class="title-ref">port</span> flags for configuration. ASReview LAB should only be used in closed networks.

``` bash
asreview lab --port 5555 --ip xxx.x.x.xx
```

> [!WARNING]
> For use in production, we recommend to follow the `../server/installation` instructions of ASReview LAB Server.

## Install with Docker

ASReview LAB is also available as a Docker container. Ensure Docker is installed on your machine.

To install and start ASReview LAB at <http://localhost:5000>, run:

``` bash
docker run -p 5000:5000 ghcr.io/asreview/asreview:latest lab
```

You can pass advanced command-line options as follows:

``` bash
docker run -p 9000:9000 ghcr.io/asreview/asreview lab --port 9000
```

> [!TIP]
> ASReview LAB is now installed. Open `http://localhost:5000` in your web browser to get started.

### Mount Local Volume

To mount the container to your local project folder (or any other folder), use the <span class="title-ref">-v</span> flag. Replace <span class="title-ref">path-to-your-folder</span> with the path to your local folder. When a project folder is specified, ASReview LAB will store and load all projects from this folder. Multiple containers can access the same folder.

``` bash
docker run -p 5000:5000 -v path-to-your-folder:/project_folder
ghcr.io/asreview/asreview lab
```

### Named Container

To simplify usage, create a named container:

``` bash
docker create --name asreview-lab -p 5000:5000 -v
path-to-your-folder:/project_folder ghcr.io/asreview/asreview lab
```

To start ASReview LAB, run:

``` bash
docker start asreview
```

To stop it, replace <span class="title-ref">start</span> with <span class="title-ref">stop</span>. You can check running containers with <span class="title-ref">docker ps</span>.

### Customize the Image

To add extensions or build the Docker image yourself, modify the [Dockerfile](https://github.com/asreview/asreview/blob/main/Dockerfile). After making changes, build and run the image with:

``` bash
docker build -t asreview/asreview:custom . docker run -p 5000:5000
ghcr.io/asreview/asreview:custom lab
```
