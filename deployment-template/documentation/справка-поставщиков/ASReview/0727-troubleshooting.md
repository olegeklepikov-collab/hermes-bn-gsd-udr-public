> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка ASReview: troubleshooting

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Troubleshooting

ASReview LAB is advanced machine learning software. In some situations, you might encounter unexpected behavior. See below for solutions to common problems.

## Unknown Command "pip"

The command line returns one of the following messages:

``` bash
-bash: pip: No such file or directory
```

``` bash
'pip' is not recognized as an internal or external command, operable program or batch file.
```

First, check if Python is installed by using the following command:

``` bash
python --version
```

If this doesn't return a version number, then Python is either not installed or not correctly installed.

Most likely, the environment variables aren't configured correctly. Follow the step-by-step installation instructions on the ASReview website ([Windows](https://asreview.ai/download/) and [MacOS](https://asreview.ai/download/)).

However, there is a simple way to resolve incorrect environment variables by adding <span class="title-ref">python -m</span> in front of the command. For example:

``` bash
python -m pip install asreview
```

## Unknown command "asreview"

In some situations, the entry point "asreview" can not be found after installation. First check whether the package is correctly installed. Do this with the command <span class="title-ref">python -m asreview -h</span>. If this shows a decryption of the program, use <span class="title-ref">python -m</span> in front of all your commands. For example:

``` bash
python -m asreview lab
```

## Build dependencies error

The command line returns the following message:

``` bash
"Installing build dependencies ... error"
```

This error typically happens when the version of your Python installation has been released very recently. Because of this, the dependencies of ASReview are not compatible with your Python installation yet. It is advised to install the second most recent version of Python instead. Detailed step-by-step instructions to install Python (and ASReview LAB) are available for [Windows](https://asreview.ai/download/) and [MacOS](https://asreview.ai/download/) users.
