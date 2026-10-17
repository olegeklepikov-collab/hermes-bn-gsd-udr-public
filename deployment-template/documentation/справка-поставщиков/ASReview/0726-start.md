> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка ASReview: start

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Start ASReview LAB

After you install ASReview LAB, start the program via the command line to start using it.

``` bash
asreview lab
```

When you are using Windows, open <span class="title-ref">CMD.exe</span> and run the command. When you use MacOS or Linux, you can open <span class="title-ref">Terminal</span> and run the command.

Read the following sections for advanced options to start or configure ASReview LAB users.

## Command line arguments for starting ASReview LAB

ASReview LAB provides a powerful command line interface for running ASReview LAB with other options or even run tasks like simulations. For a list of available commands in ASReview LAB, type `asreview lab --help`.

`asreview lab` launches the ASReview LAB software (the frontend).

``` bash
asreview lab [options]
```

<div class="program">

asreview lab

</div>

<div class="option">

`-h, --help`  

Show help message and exit.

</div>

<div class="option">

`--host HOST`  

The host/IP address the server will listen on.

</div>

<div class="option">

`--port PORT`  

The port the server will listen on.

</div>

<div class="option">

`--enable-auth ENABLE_AUTH`  

Enable authentication. Deprecated.

</div>

<div class="option">

`--secret-key SECRET_KEY`  

Secret key for authentication. Deprecated.

</div>

<div class="option">

`--salt SALT`  

When using authentication, a salt code is needed for hasing passwords.

</div>

<div class="option">

`--config-path CONFIG_PATH`  

Path to a TOML file containing ASReview parameters.

</div>

<div class="option">

`--no-browser NO_BROWSER`  

Do not open ASReview LAB in a browser after startup.

</div>

<div class="option">

`--port-retries NUMBER_RETRIES`  

<!-- -->

The number of additional ports to try if the specified port is not  
available.

</div>

<div class="option">

`--certfile CERTFILE_FULL_PATH`  

The full path to an SSL/TLS certificate file.

</div>

<div class="option">

`--keyfile KEYFILE_FULL_PATH`  

The full path to a private key file for usage with SSL/TLS.

</div>

<div class="option">

`--skip-update-check`  

Skip checking for updates.

</div>

## Set environment variables

The following environment variables are available.

<div class="option">

ASREVIEW_PATH

The path to the folder with project. Default <span class="title-ref">~/.asreview</span>.

</div>

How you set environment variables depends on the operating system and the environment in which you deploy ASReview LAB.

In MacOS or Linux operating systems, you can set environment variables from the command line. For example:

``` bash
export ASREVIEW_PATH=~/.asreview
```

On Windows, you can use the following syntax:

``` bash
set ASREVIEW_PATH=~/.asreview
```

To check if you set an environment variable successfully, run the following on \*nix operating systems:

``` bash
echo $ASREVIEW_PATH
```

Or the following on Windows operating systems:

``` bash
echo %ASREVIEW_PATH%
```

## Run ASReview LAB on localhost with a different port

By default, ASReview LAB runs on port 5000. If that port is already in use or if you want to specify a different port, start ASReview LAB with the following command:

``` bash
asreview lab --port <port>
```

For example, start ASReview LAB on port 5001:

``` bash
asreview lab --port 5001
```

## Local server with authentication

> [!NOTE]
> For production use, it is recommended to use the Docker setup. See the `../server/overview` section for more information.

The most basic configuration of the ASReview LAB application with authentication is to run the application from the CLI with the `--enable-auth` flag. The application will start with authentication enabled and will create a SQLite database if it does not exist. The database will be stored in the ASReview projects folder. The database contains the user accounts and links them to projects.

Start the application with authentication enabled:

``` bash
asreview lab --enable-auth --secret-key=<secret key> --salt=<salt>
```

where `--enable-auth` forces the application to run in an authenticated mode, `<secret key>` is a string that is used for encrypting cookies and `<salt>` is a string that is used to hash passwords. The `--secret-key` and `--salt` parameters are mandatory if authentication is required.

To create user accounts, one can use the `add-users` command of the `auth-tool` sub command of the ASReview application:

``` bash
asreview auth-tool add-users
```

For more information about auth-tool and creating users, see the section [Create user accounts](#create-user-accounts-with-auth-tool) below.
