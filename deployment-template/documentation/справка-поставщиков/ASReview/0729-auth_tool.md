> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка ASReview: auth_tool

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Auth-Tool

The <span class="title-ref">auth-tool</span> is a command-line utility provided by ASReview to manage user authentication and project linking in an authenticated environment. It allows administrators to create databases, manage user accounts, list projects, and migrate projects from unauthenticated to authenticated modes.

## Features of Auth-Tool

- Create and manage authentication databases.
- Add user accounts interactively or in bulk.
- List users and projects in the database.
- Migrate projects to authenticated environments.

## Creating the Authentication Database

To create a database for authentication, use the <span class="title-ref">create-db</span> command:

``` bash
asreview auth-tool create-db --db-uri=sqlite:////path/example.sqlite
```

If the <span class="title-ref">--db-uri</span> option is not provided, the tool will use the default database URI configured in the ASReview folder.

## Adding User Accounts

You can add user accounts interactively or in bulk using a JSON string.

**Interactive Mode:**

Run the following command:

``` bash
asreview auth-tool add-users --db-uri=sqlite:////path/example.sqlite
```

The tool will prompt you to add user details such as email, name, affiliation (optional), and password.

**Bulk Mode:**

Use the <span class="title-ref">--json</span> option to add multiple users at once:

``` bash
asreview auth-tool add-users \
        --db-uri=sqlite:////path/example.sqlite \ -j "[{\"email\":
        \"name@email.org\", \"name\": \"Name of User\", \"affiliation\":
        \"Some Place\", \"password\": \"1234@ABcd\"}]"
```

The JSON string should contain a list of dictionaries with the following keys: <span class="title-ref">email</span>, <span class="title-ref">name</span>, <span class="title-ref">affiliation</span>, and <span class="title-ref">password</span>.

## Listing Projects

To list all projects in the database, use the <span class="title-ref">list-projects</span> command:

``` bash
asreview auth-tool list-projects
```

To get the output in JSON format, use the <span class="title-ref">--json</span> flag:

``` bash
asreview auth-tool list-projects --json
```

The JSON output can be used to bulk insert or link projects to users.

## Listing Users

To list all users in the database, use the <span class="title-ref">list-users</span> command:

``` bash
asreview auth-tool list-users
```

## Migrating Projects to Authenticated Mode

If you are switching from unauthenticated to authenticated mode, you need to migrate existing projects.

**Interactive Migration:**

Run the following command:

``` bash
asreview auth-tool link-projects --db-uri=sqlite:////path/example.sqlite
```

The tool will prompt you to assign a user ID to each project.

**Bulk Migration:**

Use the JSON output from the <span class="title-ref">list-projects</span> command, add user IDs to each project, and run:

``` bash
asreview auth-tool link-projects \
        --db-uri=sqlite:////path/example.sqlite \ --json "[{\"folder\":
        \"project-id\", \"version\": \"1.3\", \"project_id\":
        \"project-id\", \"name\": \"project 1\", \"authors\":
        \"Authors\", \"created\": \"2023-04-12 21:23:28.625859\",
        \"owner_id\": 15}]"
```
