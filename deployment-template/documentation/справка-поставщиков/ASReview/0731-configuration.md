> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка ASReview: configuration

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Server configuration

ASReview LAB offers a number of options to run the application on a server. It is possible to run the application on a server with or without authentication. The latter is the default option. This page describes how to configure the ASReview LAB application to run on a server with authentication enabled. With authentication enabled, users can run their projects in their own separate workspaces. Authentication requires the storage of user accounts and links these accounts to projects. Currently, we are using a SQLite database (asreview.development.sqlite or asreview.production.sqlite) in the ASReview projects folder to store that information.

## Getting started

To configure the authentication in more detail, we need to create a TOML file that contains all relevant authentication parameters. The parameters in that TOML file will override parameters that were passed in the CLI. Below is an example of a TOML file (extension <span class="title-ref">.toml</span>) that enables authentication and OAuth with GitHub, ORCID, and Google. It also enables email verification and allows users to create their own accounts. The email server is configured to confirm new accounts and to allow users to retrieve a new password if they forget it. The TOML file also contains the necessary parameters to run the application in a secure way (HTTPS).

``` toml
DISABLE_LOGIN = false LOGIN_DURATION = 31 SECRET_KEY = "<secret key>"
SECURITY_PASSWORD_SALT = "<salt>" SESSION_COOKIE_SECURE = true
REMEMBER_COOKIE_SECURE = true SESSION_COOKIE_SAMESITE = "Lax"
SQLALCHEMY_TRACK_MODIFICATIONS = true ALLOW_ACCOUNT_CREATION = true
EMAIL_VERIFICATION = false

MAIL_SERVER = "<smtp-server>" MAIL_PORT = 465 MAIL_USERNAME =
"<smtp-server-username>" MAIL_PASSWORD = "<smtp-server-password>"
MAIL_USE_TLS = false MAIL_USE_SSL = true MAIL_DEFAULT_SENDER = "<preferred
reply email address>"

[OAUTH]
        [OAUTH.GitHub] AUTHORIZATION_URL =
        "https://github.com/login/oauth/authorize" TOKEN_URL =
        "https://github.com/login/oauth/access_token" CLIENT_ID = "<GitHub
        client ID>" CLIENT_SECRET = "<GitHub client secret>" SCOPE = ""

        [OAUTH.Orcid] AUTHORIZATION_URL =
        "https://sandbox.orcid.org/oauth/authorize" TOKEN_URL =
        "https://sandbox.orcid.org/oauth/token" CLIENT_ID = "<Orcid client
        ID>" CLIENT_SECRET = "<Orcid client secret>"

        [OAUTH.Google] AUTHORIZATION_URL =
        "https://accounts.google.com/o/oauth2/auth" TOKEN_URL =
        "https://oauth2.googleapis.com/token" CLIENT_ID = "<Google client
        ID>" CLIENT_SECRET = "<Google client secret>" SCOPE = "profile
        email"
```

Not that the SCOPE parameter is missing for Orcid: to retrieve user data from Orcid, multiple calls have to be made with different scopes. Therefor the scopes are hard-coded.

Store the TOML file on the server and start the ASReview application from the CLI with the `--config-path` parameter:

``` bash
asreview lab --config-path=<path-to-TOML-config-file>
```

A number of the keys in the TOML file are standard Flask parameters. The keys that are specific for authenticating ASReview are summarized below:

- DISABLE_LOGIN: if set to `false` the application will start with authentication. If the SQLite database does not exist, one will be created during startup.
- LOGIN_DURATION: number of days that a user should remain logged in. Default: 31.
- SECRET_KEY: the secret key is a string that is used to encrypt cookies and is mandatory if authentication is required.
- SECURITY_PASSWORD_SALT: another string used to hash passwords, also mandatory if authentication is required.
- SESSION_COOKIE_SAMESITE: Restrict how cookies are sent with requests from external sites. In the example the value is set to "Lax" which is the recommended option. If backend and frontend are served on different domains set to the string "None".
- ALLOW_ACCOUNT_CREATION: enables account creation by users, either by front- or backend.
- EMAIL_VERIFICATION: used in conjunction with ALLOW_ACCOUNT_CREATION. If set to `true` the system sends a verification email after account creation. Only relevant if the account is \_\_not\_\_ created by OAuth. This parameter can be omitted if you don't want verification.
- [MAIL]()\<PAR\>: configuration parameters to setup the SMTP email server that is used for email verification. It also allows users to retrieve a new password after forgetting it. Don't forget to enter the reply address (MAIL_DEFAULT_SENDER) of your system emails. Remove these parameters if system emails for verification and password retrieval are unwanted.
- OAUTH: an authenticated ASReview application may integrate with the OAuth functionality of Github, Orcid and Google. Provide the necessary OAuth login credentails (for [Github](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app), [Orcid](https://info.orcid.org/documentation/api-tutorials/api-tutorial-get-and-authenticated-orcid-id/) en [Google](https://support.google.com/cloud/answer/15549257?hl=en)). Please note that the <span class="title-ref">AUTHORIZATION_URL</span> and <span class="title-ref">TOKEN_URL</span> of the Orcid entry are sandbox-urls, and thus not to be used in production. Omit this parameter if OAuth is unwanted.

The `SQLALCHEMY_DATABASE_URI` key is not included in the TOML file. This key is used to configure the database connection. The default value is `sqlite:///asreview.production.sqlite`. This means that the application will use the SQLite database in the ASReview projects folder. If you would like to use a different database, you can add the `SQLALCHEMY_DATABASE_URI` key to the TOML file.

## Full configuration

All ASReview LAB settings are prefixed with <span class="title-ref">ASREVIEW_LAB\_</span>. They include all settings from Flask configuration.

### ASReview LAB settings

<div class="option">

ASREVIEW_LAB_CONFIG_PATH

Path to ASReview LAB config TOML file with ASReview LAB configuration.

</div>

<div class="option">

ASREVIEW_LAB_SECRET_KEY

Secret key for ASReview LAB.

</div>

### Login configuration

<div class="option">

ASREVIEW_LAB_AUTHENTICATION

If false, login is disabled and no password is required to use ASReview LAB.

</div>

<div class="option">

ASREVIEW_LAB_SQLALCHEMY_DATABASE_URI

Database URI for ASReview LAB.

</div>

### Account creation configuration

<div class="option">

ASREVIEW_LAB_ALLOW_ACCOUNT_CREATION

If true, account creation is enabled.

</div>

<div class="option">

ASREVIEW_LAB_SECURITY_PASSWORD_SALT

Salt for password hashing.

</div>

<div class="option">

ASREVIEW_LAB_RE_CAPTCHA_V3

If true, reCAPTCHA v3 is enabled for account creation.

</div>

### OAuth configuration

<div class="option">

ASREVIEW_LAB_OAUTH

OAuth configuration for ASReview LAB. It is a dictionary with the following keys: <span class="title-ref">GitHub</span>, <span class="title-ref">Orcid</span>, and <span class="title-ref">Google</span>. Each of these keys is a dictionary with the following keys: <span class="title-ref">AUTHORIZATION_URL</span>, <span class="title-ref">TOKEN_URL</span>, <span class="title-ref">CLIENT_ID</span>, <span class="title-ref">CLIENT_SECRET</span>, and <span class="title-ref">SCOPE</span>.

</div>

### Remote user configuration

<div class="option">

ASREVIEW_LAB_REMOTE_USER

Remote user configuration for ASReview LAB. It is a dictionary with the following keys: <span class="title-ref">USER_IDENTIFIER_HEADER</span>, <span class="title-ref">USER_NAME_HEADER</span>, <span class="title-ref">USER_EMAIL_HEADER</span>, <span class="title-ref">USER_AFFILIATION_HEADER</span>, <span class="title-ref">DEFAULT_EMAIL</span>, <span class="title-ref">DEFAULT_AFFILIATION</span>, <span class="title-ref">REMOTE_AUTH_SECRET</span>.

</div>

### Cookie configuration

<div class="option">

[ASREVIEW_LAB_REMEMBER_COOKIE]()\*

Login-related cookie settings. Refer to Flask-Login documentation for details.

</div>

### Mail configuration

<div class="option">

ASREVIEW_LAB_EMAIL_VERIFICATION

If true, email verification is required for new accounts.

</div>

<div class="option">

[ASREVIEW_LAB_MAIL]()\*

Mail-related configuration. Refer to Flask-Mail documentation for details.

</div>

### CORS configuration

<div class="option">

[ASREVIEW_LAB_CORS]()\*

CORS configuration. Refer to Flask-CORS documentation for details, except <span class="title-ref">ASREVIEW_LAB_CORS_SUPPORTS_CREDENTIALS</span>, which is always true. <span class="title-ref">ASREVIEW_LAB_CORS_ORIGINS</span> is used to link backend to frontend on different host and port.

</div>

<div class="option">

ASREVIEW_LAB_POST_LOGOUT_URL

URL to which to redirec the user after they have signed out. Default is the standard login page <span class="title-ref">/signin</span>. It can be useful to set this to a custom path when using external users, with remote user auth or OAuth. In that case, you might want to redirect the user to an organizational page after logout. Note that this should be set to a valid URI, so <span class="title-ref">/custom_logout_page</span> and not <span class="title-ref">custom_logout_page</span>.

</div>
