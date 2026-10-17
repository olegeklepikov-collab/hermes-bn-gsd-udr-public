> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Wolfram: wolfram-terms

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


<style>
    :root {
        --li-width-1:  16px;
        --li-offset-1: 20px;

        --li-width-2:  24px;
        --li-offset-2: 28px;

        --li-width-3:  32px;
        --li-offset-3: 36px;
    }

    .leftcolumn h3 { font-size: 13px; }
    .leftcolumn p { margin: 0; padding-bottom: 11px; }

    .leftcolumn ol { 
        counter-reset: item; 
        list-style: none; 
        padding-left: var(--li-offset-1);
    }
    .leftcolumn ol ol  { padding-left: var(--li-offset-2); }
    .leftcolumn ol ol ol  { padding-left: var(--li-offset-3); }

    .leftcolumn li { position: relative; }

    .leftcolumn li::before {
        content: counters(item, ".") " "; 
        counter-increment: item; 
        display: inline-block;
        font-family: Helvetica, Verdana, Arial, sans-serif;
        font-size: 13px;
        font-weight: bold;
        left: calc(var(--li-offset-1) * -1);
        position: absolute;
        text-align: right;
        width: var(--li-width-1);
    }
    .leftcolumn li li::before {  
        font-size: 11px;
        font-weight: normal;
        left: calc(var(--li-offset-2) * -1);
        top: 1px;
        width: var(--li-width-2);
    }
    .leftcolumn li li li::before {  
        left: calc(var(--li-offset-3) * -1);
        width: var(--li-width-3);
    }

html { scroll-padding-top: 4rem; }

</style>

<div id="gl-outer-wrapper" class="gl-en cf">

<div id="_header" class="header">

<div id="_header-grid" class="_page-width">

# <a href="https://www.wolfram.com/?source=nav" data-walid="GUIHeader"><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTc3IiBoZWlnaHQ9IjM3Ij48dXNlIGhyZWY9IiNfdG9wLWxvZ28iIC8+PHRpdGxlPldPTEZSQU08L3RpdGxlPjwvc3ZnPg==" /></a>

<div id="_nav-products" class="_each-link">

<a href="https://www.wolfram.com/products/?source=nav" class="_label" data-walid="GUIHeader"><span>Products</span></a>

<div class="_dropdown">

- <a href="https://www.wolfram.com/wolfram-one/?source=nav" data-walid="GUIHeader">Wolfram|One</a>
- <a href="https://www.wolfram.com/mathematica/?source=nav" data-walid="GUIHeader">Mathematica</a>
- <a href="https://www.wolfram.com/system-modeler/?source=nav" data-walid="GUIHeader">System Modeler</a>
- <a href="https://www.wolframalpha.com/?source=nav" data-walid="GUIHeader">Wolfram|Alpha</a>
- <a href="https://www.wolfram.com/ai-access/?source=nav" data-walid="GUIHeader">AI Access</a>
- <a href="https://www.wolfram.com/compute-services/?source=nav" data-walid="GUIHeader">Compute Services</a>
- <a href="https://www.wolfram.com/products/?source=nav" data-walid="GUIHeader">All Products</a>

</div>

</div>

<div id="_nav-consulting" class="_each-link">

<a href="https://www.wolfram.com/solutions/?source=nav" class="_label" data-walid="GUIHeader"><span>Consulting &amp; Solutions</span></a>

<div class="_dropdown">

- <a href="https://consulting.wolfram.com/?source=nav" data-walid="GUIHeader">Wolfram Consulting</a>
- <a href="https://www.wolfram.com/solutions/?source=nav" data-walid="GUIHeader">Industry Solutions</a>
- <a href="https://www.wolfram.com/education/?source=nav" data-walid="GUIHeader">Solutions for Education</a>

</div>

</div>

<div id="_nav-learning" class="_each-link">

<a href="https://www.wolfram.com/resources/?source=nav" class="_label" data-walid="GUIHeader"><span>Learning &amp; Support</span></a>

<div class="_dropdown">

- <a href="https://www.wolfram.com/wolfram-u/?source=nav" data-walid="GUIHeader">Wolfram U Courses</a>
- <a href="https://www.wolfram.com/language/?source=nav#learning-resources" data-walid="GUIHeader">Wolfram Language Resources</a>
- <a href="https://community.wolfram.com/?source=nav" data-walid="GUIHeader">Wolfram Community</a>
- <a href="https://support.wolfram.com/?source=nav" data-walid="GUIHeader">Support FAQs</a>
- <a href="https://www.wolfram.com/support/contact/?source=nav" data-walid="GUIHeader">Contact Support</a>

</div>

</div>

<div id="_nav-company" class="_each-link">

<a href="https://www.wolfram.com/company/?source=nav" class="_label" data-walid="GUIHeader"><span>Company</span></a>

<div class="_dropdown">

- <a href="https://www.wolfram.com/company/?source=nav" data-walid="GUIHeader">About Wolfram</a>
- <a href="https://www.wolfram.com/company/careers/?source=nav" data-walid="GUIHeader">Careers</a>
- <a href="https://events.wolfram.com/?source=nav" data-walid="GUIHeader">Events</a>
- <a href="https://education.wolfram.com/programs/?source=nav" data-walid="GUIHeader">Educational Programs</a>
- <a href="https://www.wolfram.com/resources/?source=nav#mobile-apps" data-walid="GUIHeader">All Sites and Resources</a>

</div>

</div>

<div id="_nav-alpha" class="_each-link">

<a href="https://www.wolfram.com/for-agents.md?source=nav" class="_label" data-walid="GUIHeader" target="_blank"><span>For AIs<img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOSIgaGVpZ2h0PSI5Ij48dXNlIGhyZWY9IiNfdG9wLXdhIiAvPjwvc3ZnPg==" /></span></a>

</div>

<div id="_nav-cloud" class="_each-link">

<a href="https://www.wolframcloud.com/?source=nav" class="_label" data-walid="GUIHeader" target="_blank"><span><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMjQiPjx1c2UgaHJlZj0iI190b3AtY2xvdWQiIC8+PHRpdGxlPldvbGZyYW0gQ2xvdWQ8L3RpdGxlPjwvc3ZnPg==" /></span></a>

</div>

<div id="_nav-user" class="_each-link">

<a href="https://account.wolfram.com/login/oauth2/sign-in/?source=nav" class="_label" data-walid="GUIHeader" target="_blank"><span><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjUiPjx1c2UgaHJlZj0iI190b3AtdXNlciIgLz48dGl0bGU+WW91ciBBY2NvdW50PC90aXRsZT48L3N2Zz4=" /></span></a>

<div class="_dropdown">

- <a href="https://account.wolfram.com/?source=nav" data-walid="GUIHeader" target="_blank">Your Account</a>
- <a href="https://user.wolfram.com/?source=nav" data-walid="GUIHeader" target="_blank">User Portal</a>

</div>

</div>

<div id="_nav-search" class="_each-link">

<a href="https://search.wolfram.com/?source=nav" class="_label" data-walid="GUIHeader" target="_blank"><span><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiPjx1c2UgaHJlZj0iI190b3Atc2VhcmNoIiAvPjx0aXRsZT5TZWFyY2g8L3RpdGxlPjwvc3ZnPg==" /></span></a>

<div class="_dropdown">

<div id="_search-wrapper">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiPjx1c2UgaHJlZj0iI19zZWFyY2gtbWFnbmlmaWVyIiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjx1c2UgaHJlZj0iI19zZWFyY2gteCIgLz48dGl0bGU+Q2xvc2U8L3RpdGxlPjwvc3ZnPg==)

</div>

</div>

</div>

</div>

</div>

<div>

<div>

<img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX25vc2NyaXB0LXdhcm5pbmciPjx1c2UgaHJlZj0iI19ub3NjcmlwdC13YXJuaW5nIiAvPjwvc3ZnPg==" class="_noscript-warning" />

</div>

<div>

Enable JavaScript to interact with content and submit forms on Wolfram websites. <a href="http://www.enable-javascript.com/" class="chevron-after" target="_blank" data-walid="GUIFooter">Learn how</a>

</div>

</div>

<div style="height: 0; width: 0; position: absolute; visibility: hidden; top: -999999999999px;">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgoKICAgICAgICAgICAgPGcgaWQ9Il90b3AtaWNvbnMiPgoKICAgICAgICAgICAgICAgIDxzeW1ib2wgaWQ9Il90b3AtbG9nbyIgdmlld2JveD0iMCAwIDE4MyAzOC45MiI+CiAgICAgICAgICAgICAgICAgICAgPGc+CiAgICAgICAgICAgICAgICAgICAgICAgIDxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik00Mi42Miw5LjYzaDQuODdsMi4yNSwxMi41MiwzLjMzLTEyLjUyaDQuMjNsMy45NiwxMi43OSwyLjM0LTEyLjc5aDQuNmwtMy45NiwxOC44M2gtNS4zMmwtMy41MS0xMS43MS0zLjYsMTEuNzFoLTUuNTlsLTMuNi0xOC44M1oiIC8+CiAgICAgICAgICAgICAgICAgICAgICAgIDxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0xODMsMjguNDZoLTQuODdsLTIuMjUtMTIuNjEtMy4zMywxMi42MWgtNC4yM2wtMy45Ni0xMi43OS0yLjM0LDEyLjc5aC00LjZsMy45Ni0xOC44M2g1LjMybDMuNTEsMTEuNzEsMy42LTExLjcxaDUuNTlsMy42LDE4LjgzWiIgLz4KICAgICAgICAgICAgICAgICAgICAgICAgPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTc4LjM5LDkuMjdjNi4xMywwLDkuMjgsMy42OSw5LjI4LDkuNzNzLTMuMjQsOS43My05LjI4LDkuNzMtOS4yOC0zLjc4LTkuMjgtOS43M2MwLTYuMDQsMy4xNS05LjczLDkuMjgtOS43M1ptMCwxNS43N2MyLjk3LDAsNC4yMy0yLjg4LDQuMjMtNi4wNHMtMS4xNy02LjA0LTQuMjMtNi4wNC00LjIzLDIuNy00LjIzLDYuMDRjLjA5LDMuMTUsMS4yNiw2LjA0LDQuMjMsNi4wNFoiIC8+CiAgICAgICAgICAgICAgICAgICAgICAgIDxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik05MC40Niw5LjYzaDQuOTZ2MTUuMDRoNy42NnYzLjY5aC0xMi42MVY5LjYzWiIgLz4KICAgICAgICAgICAgICAgICAgICAgICAgPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTEwNS4xNSw5LjYzaDEyLjQzdjMuNTFoLTcuNDh2NC4xNGg3LjEydjMuNTFoLTcuMTJ2Ny41N2gtNC45NnMwLTE4Ljc0LDAtMTguNzRaIiAvPgogICAgICAgICAgICAgICAgICAgICAgICA8cGF0aCBmaWxsPSIjZmZmIiBkPSJNMTIwLjIsOS42M2g4LjgzYzMuMzMsMCw1Ljk1LDEuNTMsNS45NSw0Ljc3LDAsMi41Mi0xLjE3LDQuMTQtMy42LDQuNzdoMGMxLjYyLC40NSwxLjcxLDEuODksMi42MSw0LjE0bDEuOCw1LjE0aC01LjE0bC0xLjA4LTMuNDJjLS45OS0zLjI0LTEuNjItNC4wNS0zLjUxLTQuMDVoLTEuMDh2Ny4zOWgtNC45NlY5LjYzaC4xOFptNC44Nyw3Ljg0aDEuMjZjMS42MiwwLDMuNi0uMDksMy42LTIuMTYsMC0xLjcxLTEuNzEtMi4wNy0zLjYtMi4wN2gtMS4yNnY0LjIzWiIgLz4KICAgICAgICAgICAgICAgICAgICAgICAgPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTE0My4zNSw5LjYzaDYuMDRsNy4xMiwxOC44M2gtNS40MWwtMS4zNS00LjA1aC02Ljk0bC0xLjQ0LDQuMDVoLTUuMDVsNy4wMy0xOC44M1ptMy4wNiwzLjg3aDBsLTIuNDMsNy4zOWg0LjY5bC0yLjI1LTcuMzlaIiAvPgogICAgICAgICAgICAgICAgICAgIDwvZz4KICAgICAgICAgICAgICAgICAgICA8cGF0aCBmaWxsPSIjZDEwIiBkPSJNMzEuODEsMTkuNDZsNS40MS02LjA0LTcuOTMtMS43MSwuODEtOC4wMi03LjM5LDMuMjRMMTguNjUsMGwtNC4wNSw2Ljk0TDcuMTIsMy42OWwuODEsOC4wMkwwLDEzLjQybDUuNDEsNi4wNEwwLDI1LjVsNy45MywxLjcxLS44MSw4LjAyLDcuMzktMy4yNCw0LjA1LDYuOTQsNC4wNS02Ljk0LDcuMzksMy4yNC0uODEtOC4wMiw3LjkzLTEuNzEtNS4zMi02LjA0Wm0xLjM1LDMuODdsLTMuNTEtMS4xNy0yLjQzLTMuMTUsMy4xNSwxLjE3LDIuNzksMy4xNVptLTExLjUzLDcuNDhsLTIuMjUsMy43OHYtMy45NmwyLjM0LTMuMzMtLjA5LDMuNTFabS01LjIzLTE5LjczbC0zLjc4LTEuMzUtMi4xNi0yLjk3LDMuOTYsMS43MSwxLjk4LDIuNjFabTYuNDktMi41MmwzLjk2LTEuNzEtMi4xNiwyLjk3LTMuNzgsMS4zNSwxLjk4LTIuNjFabTQuNzgsMy41MWwtMS44OSwyLjcsLjA5LTQuMTQsMi4yNS0zLjA2LS40NSw0LjVabS05LjAxLDE3LjAzbC0yLjk3LTQuMzIsMi45Ny00LjA1LDIuOTcsNC4wNS0yLjk3LDQuMzJabS01LjU5LTEyLjM0bC0uMTgtNS4yMyw0Ljk2LDEuOHY1LjE0bC00Ljc4LTEuNzFabTYuMzEtMy41MWw0Ljk2LTEuOC0uMTgsNS4zMi00Ljc4LDEuNjJ2LTUuMTRabS05LjgyLTEuMTdsLS40NS00LjQxLDIuMjUsMy4wNiwuMDksNC4xNC0xLjg5LTIuNzlabTcuODQsNy43NWwtMi45Nyw0LjA1LTUuMDUtMS41MywzLjI0LTQuMTQsNC43OCwxLjYyWm0tMS44OSw3LjQ4bDIuMzQsMy4zM3YzLjk2bC0yLjI1LTMuNzgtLjA5LTMuNTFabTQuMzItNy40OGw0Ljc4LTEuNjIsMy4yNCw0LjE0LTUuMDUsMS41My0yLjk3LTQuMDVabTE0LjQyLTUuNDFsLTMuNjksNC4xNC00LjQyLTEuNjIsMi42MS0zLjc4LDUuNSwxLjI2Wm0tMTIuNzktNi41OGwtMi43OSwzLjYtMi43OS0zLjYsMi43OS00Ljg2LDIuNzksNC44NlpNMi45NywxNC4zMmw1LjUtMS4xNywyLjYxLDMuNzgtNC40MiwxLjYyLTMuNjktNC4yM1ptMy45Niw1Ljc3bDMuMTUtMS4xNy0yLjUyLDMuMjQtMy42LDEuMjYsMi45Ny0zLjMzWm0tMi42MSw0Ljc3bDMuNjktMS4yNiwzLjk2LDEuMTctMy4yNCwuOTktNC40Mi0uOVptNS4xNCwyLjM0bDQuNTEtMS40NCwuMDksNC43Ny01LjE0LDIuMjUsLjU0LTUuNTlabTEzLjcsMy4zM2wuMDktNC43Nyw0LjUxLDEuNDQsLjU0LDUuNTktNS4xNC0yLjI1Wm01LjMyLTQuNjhsLTMuMzMtMS4wOCwzLjk2LTEuMTcsMy42OSwxLjI2LTQuMzIsLjk5WiIgLz4KICAgICAgICAgICAgICAgIDwvc3ltYm9sPgoKICAgICAgICAgICAgICAgIDxzeW1ib2wgaWQ9Il90b3Atd2EiIHZpZXdib3g9IjAgMCAxMy4xMjUgMTIiPgogICAgICAgICAgICAgICAgICAgIDxwYXRoIGZpbGw9IiNiMmIyYjIiIGQ9Ik03LjU5Ni4wODNjLS4yNC0uMjQtLjU1OS0uMjMzLS43OTIsMC0uMjc2LjI3Ni0uMjgzLjU5NC0uMDQyLjgzNGwyLjg4NSwyLjg4NS04LjYzOC0uMDA3Yy0uMzE4LjAwNy0uNTUyLjI0LS41NTkuNTU5LDAsLjM5Ni4yMzMuNjI5LjU1Mi42MzZsMTEuNTE3LjAwN0w3LjU5Ni4wODNaIiAvPgogICAgICAgICAgICAgICAgICAgIDxwYXRoIGZpbGw9IiNiMmIyYjIiIGQ9Ik01LjUwOCwxMS45NTVjLjI0LjI0LjU1OS4yMzMuNzkyLDAsLjI3Ni0uMjc2LjI4My0uNTk0LjA0Mi0uODM0bC0yLjg4NS0yLjg4NSw4LjYzOC4wMDdjLjMxOC0uMDA3LjU1Mi0uMjQuNTU5LS41NTksMC0uMzk2LS4yMzMtLjYyOS0uNTUyLS42MzZsLTExLjUxNy0uMDA3LDQuOTIzLDQuOTE0WiIgLz4KICAgICAgICAgICAgICAgIDwvc3ltYm9sPgoKICAgICAgICAgICAgICAgIDxzeW1ib2wgaWQ9Il90b3AtY2xvdWQiIHZpZXdib3g9IjAgMCAzMSAyNCI+CiAgICAgICAgICAgICAgICAgICAgPHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMTYuMjYsMjRjLTEuMTksMC0yLjM4LS4zMy0zLjU4LTEuMDktLjQzLS4zMy0uODctLjc2LTEuMTktMS4wOS0uMTEsMC0uMzMsLjExLS40MywuMTEtMy4zNiwuNDQtNi4xOC0xLjA5LTYuNjEtMy43MXYtLjQ0Yy0yLjcxLS45OC00LjQ0LTMuMzgtNC40NC02LjExLDAtMy42LDMuMDMtNi4zMyw2LjgzLTYuNjYsLjIyLTEuNjQsMS4wOC0yLjg0LDIuMjgtMy43MUMxMC41MSwuMjEsMTIuNDctLjMzLDE0LjQyLC4yMWMxLjA4LC4yMiwyLjA2LC42NSwzLjAzLDEuMiwxLjQxLS40NCwzLjAzLS40NCw0LjY2LDAsMS44NCwuNzYsMy4yNSwyLjE4LDQuMTIsNC4xNSwyLjcxLC4zMyw0Ljc3LDIuNCw0Ljc3LDUuMTMsMCwxLjItLjQzLDIuNC0xLjMsMy4yNywuNDMsLjk4LC43NiwxLjk2LC40MywzLjA2LS42NSwyLjk1LTQuMjMsNC42OS04LjEzLDMuODJoLS4yMmMtLjk4LDEuNjQtMi4zOCwyLjYyLTQuMTIsMi45NS0uNDMsLjExLS45OCwuMjItMS40MSwuMjJabS0zLjktNC40N2wuMzMsLjQ0Yy4zMywuNDQsLjc2LC44NywxLjE5LDEuMiwuOTgsLjc2LDIuMTcsLjk4LDMuMzYsLjc2LDEuMy0uMjIsMi42LTEuMiwzLjI1LTIuNjJsLjMzLS42NSwuNzYsLjExYy4yMiwuMTEsLjQzLC4xMSwuNzYsLjIyLDIuODIsLjY1LDUuNjQtLjQ0LDUuOTYtMi4yOSwuMjItLjg3LS4yMi0xLjc1LS42NS0yLjE4bC0uNDMtLjc2LC42NS0uNDRjLjc2LS42NSwxLjE5LTEuNjQsMS4xOS0yLjQsMC0xLjg1LTEuNjMtMy4yNy0zLjU4LTMuMjdoLS43NmwtLjExLS41NWMtLjQzLTIuMDctMS43My0zLjI3LTMuMjUtMy45My0xLjE5LS40NC0yLjYtLjMzLTMuNzksLjExbC0uNDMsLjIyLS40My0uMzNjLS43Ni0uNjUtMS43My0xLjA5LTIuNzEtMS4yLTEuNDEtLjIyLTIuOTMsMC00LjAxLC44Ny0uODcsLjc2LTEuNDEsMS44NS0xLjYzLDMuMTZsLS4xMSwuODdoLTEuMTljLTIuOTMsMC01LjMxLDIuMDctNS4zMSw0LjgsMCwyLjA3LDEuNjMsNC4wNCwzLjksNC40N2wuODcsLjIyLS4yMiwuODdjLS4xMSwuMjItLjExLC40NCwwLC42NSwuMjIsMS40MiwyLjI4LDIuNCw0LjQ0LDIuMDcsLjMzLDAsLjY1LS4xMSwuODctLjIybC43Ni0uMjJaIiAvPgogICAgICAgICAgICAgICAgICAgIDxwYXRoIGZpbGw9ImN1cnJlbnRDb2xvciIgZD0iTTE1LjYxLDE5LjkybC0xLjc1LTMtMy4wOCwxLjM0LC4zMS0zLjQxLTMuMzktLjcyLDIuMjYtMi41OS0yLjI2LTIuNDgsMy4zOS0uNzItLjMxLTMuNDEsMy4wOCwxLjM0LDEuNzUtMywxLjc1LDMsMy4wOC0xLjM0LS4zMSwzLjQxLDMuMzksLjcyLTIuMjYsMi41OSwyLjI2LDIuNTktMy4zOSwuNzIsLjMxLDMuNDEtMy4wOC0xLjM0LTEuNzUsMi45Wm0uNDEtMy43MnYuOTNsLjYyLS45M3YtLjgzbC0uNjIsLjgzWm0tMS41NC0uMWwuNjIsLjkzdi0uODNsLS42Mi0uODN2LjcyWm0zLjA4LS4yMWwxLjc1LC43Mi0uMjEtMS44Ni0xLjU0LS40MXYxLjU1Wm0tNS41NS0xLjE0bC0uMjEsMS44NiwxLjc1LS43MnYtMS42NmwtMS41NCwuNTJabTIuNDctMS4wM2wuOTIsMS40NSwuOTItMS4zNC0uOTItMS40NS0uOTIsMS4zNFptNC4zMiwwbC43MiwuMjEsMS4xMy0uMjEtLjgyLS4zMS0xLjAzLC4zMVptLTguMzIsMGwxLjEzLC4yMSwuNzItLjIxLTEuMDMtLjMxLS44MiwuMzFabTUuODYtMS45N2wuOTIsMS4zNCwxLjY0LS40MS0xLjAzLTEuMzQtMS41NCwuNDFabS00LjIxLC44M2wxLjY0LC40MSwuOTItMS4zNC0xLjY0LS42Mi0uOTIsMS41NVptNy45MS0uMWwuNzIsLjIxLS43Mi0uODMtLjcyLS4yMSwuNzIsLjgzWm0tOS4wNC0uNTJsLS43MiwuNzIsLjgyLS4yMSwuNjItLjcyLS43MiwuMjFabTcuOTEtMS41NWwxLjU0LC42MiwxLjIzLTEuMzQtMS45NS0uMzEtLjgyLDEuMDNabS05LjM1LS44M2wxLjIzLDEuMzQsMS41NC0uNjItLjkyLTEuMTQtMS44NSwuNDFabTYuNDctLjUydjEuNzZsMS42NC0uNjJ2LTEuNjZsLTEuNjQsLjUyWm0tMi41NywxLjI0bDEuNjQsLjYydi0xLjg2bC0xLjY0LS42MnYxLjg2Wm0tMS4zNC0xLjg2bC40MSwuNTJ2LTEuMDNsLS40MS0uNzJ2MS4yNFptNi41OC0uNDF2MS4wM2wuNDEtLjYyLC4xLTEuMTQtLjUxLC43MlptLTQuMDEtMS4yNGwuOTIsMS4xNCwuODItMS4xNC0uOTItMS42Ni0uODIsMS42NlptLTEuNDQsLjcybC45MiwuMzEtLjMxLS40MS0uOTItLjUyLC4zMSwuNjJabTQuMTEtLjMxbC0uMzEsLjQxLC45Mi0uMzEsLjUxLS41Mi0xLjEzLC40MVoiIC8+CiAgICAgICAgICAgICAgICA8L3N5bWJvbD4KCiAgICAgICAgICAgICAgICA8c3ltYm9sIGlkPSJfdG9wLXVzZXIiIHZpZXdib3g9IjAgMCAyMSAyNCI+CiAgICAgICAgICAgICAgICAgICAgPHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMTcuNzcsMTQuNzdjLS41OC0uMjMtMS4xNy0uNTgtMS44Ny0uNjktLjkzLS4zNS0xLjQtLjQ2LTEuNC0uNjksLjEyLS41OCwuNDctMS4yNywuNy0xLjczLC44Mi0xLjM4LDEuMjgtMi44OCwxLjQtNC41LDAtMS45Ni0uNy0zLjgxLTEuOTgtNS4zMUMxMy41NywuNywxMi4wNSwuMDEsMTAuNDIsLjAxYy0xLjg3LS4xMi0zLjYyLC42OS00Ljc5LDIuMDhzLTEuNzUsMy4yMy0xLjUyLDQuOTZjLjEyLDEuNzMsLjgyLDMuNDYsMS43NSw0Ljg0LC4zNSwuMzUsLjQ3LC45MiwuNTgsMS4zOCwwLC4yMy0uMzUsLjM1LTEuNCwuNjlsLTEuNzUsLjY5QzEuMDgsMTUuODEsLjM4LDE4LjQ2LC4wMywyMC40MmMtLjEyLC45MiwuMTIsMS44NSwuODIsMi41NCwuNTgsLjY5LDEuNTIsMS4wNCwyLjMzLDEuMDRoMTQuNTljLjkzLDAsMS44Ny0uNDYsMi40NS0xLjE1cy45My0xLjYxLC43LTIuNjVjLS4zNS0yLjY1LTEuNC00LjYxLTMuMTUtNS40MlptLjgyLDYuNjljLS4xMiwuMjMtLjM1LC4zNS0uNTgsLjM1SDMuM2MtLjIzLDAtLjQ3LS4xMi0uNTgtLjM1LS4yMy0uMjMtLjIzLS40Ni0uMjMtLjgxLC4xMi0xLjI3LC43LTMuMzQsMS45OC00LjA0LC40Ny0uMjMsLjkzLS40NiwxLjUyLS41OCwxLjI4LS40NiwyLjkyLTEuMDQsMi45Mi0zdi0uMTJjLS4xMi0uODEtLjQ3LTEuNzMtLjkzLTIuNDItLjgyLTEuMTUtMS4yOC0yLjU0LTEuNC00LjA0LS4xMi0xLjE1LC4yMy0yLjMxLC45My0zLjExLC44Mi0uOTIsMS45OC0xLjI3LDMuMTUtMS4yNywuOTMsMCwxLjc1LC40NiwyLjMzLDEuMTUsLjgyLC45MiwxLjQsMi4xOSwxLjQsMy40Ni0uMTIsMS4yNy0uNDcsMi41NC0xLjE3LDMuNjktLjQ3LC44MS0uODIsMS42MS0xLjA1LDIuNTR2LjIzYzAsMS45NiwxLjc1LDIuNTQsMy4wNCwzLC40NywuMTIsMS4wNSwuMzUsMS41MiwuNTgsMS40LC42OSwxLjg3LDIuNzcsMi4xLDMuOTIsMCwuMzUtLjEyLC42OS0uMjMsLjgxWiIgLz4KICAgICAgICAgICAgICAgIDwvc3ltYm9sPgoKICAgICAgICAgICAgICAgIDxzeW1ib2wgaWQ9Il90b3Atc2VhcmNoIiB2aWV3Ym94PSIwIDAgMjQgMjQiPgogICAgICAgICAgICAgICAgICAgIDxwYXRoIGZpbGw9ImN1cnJlbnRDb2xvciIgZD0iTTIzLjY2LDIxLjg1bC02LjQ2LTYuNDVjMy4yMy00LjE4LDIuNTEtMTAuMTUtMS42Ny0xMy40OUMxMS4zNC0xLjE5LDUuMjQtLjQ3LDIuMDEsMy43MVMtLjUsMTMuODUsMy42OSwxNy4yYzMuNDcsMi42Myw4LjI1LDIuNjMsMTEuNzIsMGw2LjQ2LDYuNDVjLjQ4LC40OCwxLjIsLjQ4LDEuNjcsMCwuNi0uNiwuNi0xLjMxLC4xMi0xLjc5Wk0yLjQ5LDkuNTZjMC0zLjk0LDMuMjMtNy4xNiw3LjE3LTcuMTZzNy4xNywzLjIyLDcuMTcsNy4xNi0zLjIzLDcuMTYtNy4xNyw3LjE2LTcuMTctMy4xLTcuMTctNy4xNloiIC8+CiAgICAgICAgICAgICAgICA8L3N5bWJvbD4KCiAgICAgICAgICAgIDwvZz4KCiAgICAgICAgICAgIDxnIGlkPSJfc2VhcmNoLWljb25zIj4KCiAgICAgICAgICAgICAgICA8c3ltYm9sIGlkPSJfc2VhcmNoLW1hZ25pZmllciIgdmlld2JveD0iMCAwIDI0IDI0Ij4KICAgICAgICAgICAgICAgICAgICA8cGF0aCBmaWxsPSIjYjViNWI1IiBkPSJNMjMuNjYsMjEuODVsLTYuNDYtNi40NWMzLjIzLTQuMTgsMi41MS0xMC4xNS0xLjY3LTEzLjQ5QzExLjM0LTEuMTksNS4yNC0uNDcsMi4wMSwzLjcxUy0uNSwxMy44NSwzLjY5LDE3LjJjMy40NywyLjYzLDguMjUsMi42MywxMS43MiwwbDYuNDYsNi40NWMuNDgsLjQ4LDEuMiwuNDgsMS42NywwLC42LS42LC42LTEuMzEsLjEyLTEuNzlaTTIuNDksOS41NmMwLTMuOTQsMy4yMy03LjE2LDcuMTctNy4xNnM3LjE3LDMuMjIsNy4xNyw3LjE2LTMuMjMsNy4xNi03LjE3LDcuMTYtNy4xNy0zLjEtNy4xNy03LjE2WiIgLz4KICAgICAgICAgICAgICAgIDwvc3ltYm9sPgoKICAgICAgICAgICAgICAgIDxzeW1ib2wgaWQ9Il9zZWFyY2gteCIgdmlld2JveD0iMCAwIDE0IDE0Ij4KICAgICAgICAgICAgICAgICAgICA8cGF0aCBmaWxsPSIjNWU1ZTVlIiBkPSJNMS45LDEzLjlsLTEuNC0xLjVMNS42LDdMMC41LDEuN2wxLjQtMS41TDcsNS41bDUuMS01LjRsMS40LDEuNUw4LjQsN2w1LjEsNS40bC0xLjQsMS41TDcsOC41TDEuOSwxMy45eiIgLz4KICAgICAgICAgICAgICAgIDwvc3ltYm9sPgoKICAgICAgICAgICAgPC9nPgoKICAgICAgICAgICAgPGcgaWQ9Il9ub3NjcmlwdC1pY29ucyI+CgogICAgICAgICAgICAgICAgPHN5bWJvbCBpZD0iX25vc2NyaXB0LXdhcm5pbmciIHZpZXdib3g9IjAgMCAyOC4yMSAyNSI+CiAgICAgICAgICAgICAgICAgICAgPHBhdGggZD0iTTI3LjkxLDIxLjdMMTYuMDEsMS4xYy0uODQtMS40Ny0yLjk2LTEuNDctMy44MSwwTC4zLDIxLjdjLS44NSwxLjQ3LC4yMSwzLjMsMS45LDMuM0gyNmMxLjY5LDAsMi43NS0xLjgzLDEuOTEtMy4zWk0xNS43NSw3LjQ0bC0uNDYsOS40MmgtMi4zN2wtLjQ4LTkuNDJoMy4zMVptLTEuNjUsMTQuMjVjLTEuMTIsMC0xLjg3LS44MS0xLjg3LTEuODlzLjc3LTEuODksMS44Ny0xLjg5LDEuODMsLjc5LDEuODUsMS44OWMwLDEuMDgtLjczLDEuODktMS44NSwxLjg5WiIgZmlsbD0iI2Y0NzgyMSIgLz4KICAgICAgICAgICAgICAgICAgICA8cG9seWdvbiBwb2ludHM9IjE1Ljc3IDcuNDcgMTUuMzEgMTYuODkgMTIuOTQgMTYuODkgMTIuNDYgNy40NyAxNS43NyA3LjQ3IiBmaWxsPSIjZmZmIj48L3BvbHlnb24+CiAgICAgICAgICAgICAgICAgICAgPHBhdGggZD0iTTE0LjEsMjEuNjljLTEuMTIsMC0xLjg3LS44MS0xLjg3LTEuODlzLjc3LTEuODksMS44Ny0xLjg5LDEuODMsLjc5LDEuODUsMS44OWMwLDEuMDgtLjczLDEuODktMS44NSwxLjg5WiIgZmlsbD0iI2ZmZiIgLz4KICAgICAgICAgICAgICAgIDwvc3ltYm9sPgoKICAgICAgICAgICAgPC9nPgoKICAgICAgICA8L3N2Zz4=)

</div>

<div id="gl-inner-wrapper">

<div id="wrapper">

<div class="leftcolumn">

<div class="header">

# LEGAL INFORMATION

</div>

# Wolfram Terms of Use

#### *Effective July 29, 2024*

These Terms of Use ("Terms") govern Your access to and use of Wolfram services, websites, applications, software, support, or any product owned or operated by Wolfram (collectively, "Services"). By accessing or using the Services, You agree to be bound by these Terms. If You do not agree to these Terms, do not use the Services. By using the Services, You affirm that You are of legal age to agree to the Terms or have obtained parental or guardian consent to enter into the Terms. We may update or modify these Terms of Use from time to time in the future. Any such updates or modifications shall be effective immediately upon their announcement. Please refer often to this document at [https://www.wolfram.com/legal/terms/wolfram](https://www.wolfram.com/legal/terms/wolfram/) for the latest information.

1.  <div id="user-agreement">

    ### User Agreement

    1.  <div id="choice-of-law">

        Choice of Law. Unless agreed otherwise, use of the Services and the Terms and all other aspects of their operation and functionality shall be governed by and construed under the laws of the State of Illinois, United States, without giving effect to its rules regarding conflicts of laws. If any provision of these Terms is found to be invalid by a court of competent jurisdiction, the invalidity of such provision shall not impair the validity of the remaining Terms. No waiver of any provision of the Terms shall be deemed a further waiver of any other provision thereof.

        </div>

    2.  <div id="additional-terms">

        If a Service requires you to agree to additional licensing terms or if other terms apply (collectively, "Additional Terms"), then those Additional Terms are also considered part of these Terms. If there is a conflict between Additional Terms and Terms, the Additional Terms will govern.

        </div>

    </div>

2.  <div id="use-of-services">

    ### Use of Services

    1.  <div id="license-grant">

        License Grant. Subject to Your compliance with all Terms, Wolfram grants You a non-sublicensable, non-transferable, non-exclusive, terminable, limited license to access and use Services made available to You and licensed properly from Wolfram.

        </div>

    2.  <span id="access">Access</span>
        1.  You may need a Wolfram ID to use the Services. You are responsible for the security of any passwords, tokens, or keys associated with Your account and for any use of that account. You agree to notify Wolfram immediately upon learning of any unauthorized use of Your password or account. Your use of the Services is subject to the Wolfram Privacy Policy, available at [https://www.wolfram.com/legal/privacy/wolfram](https://www.wolfram.com/legal/privacy/wolfram/), which is hereby incorporated by reference. Changes to the Privacy Policy may be made as stated in that policy. The registration and use of Your Wolfram ID is governed by the Wolfram ID Terms and Conditions of Use, available at <http://www.wolfram.com/legal/terms/wolfram-id-terms.html> and hereby incorporated by reference.

        2.  Wolfram may release new Services from time to time, which may be subject to Additional Terms. Your use of later-added features is contingent upon Your agreement with such Additional Terms. In addition, Wolfram may change, discontinue or deprecate any Service or portion thereof for any reason, at any time, with or without notice.

    3.  <div id="user-responsibilities">

        User Responsibilities. You are solely responsible for Your Applications and End Users and for ensuring that the Applications and End Users comply with these Terms and the Prohibited Use section, herein and in any other applicable Terms. Wolfram reserves the right to review the Applications and any End User information to ensure use is consistent with Our Terms. You will provide information or other materials related to the Applications as requested by Us to verify Your compliance.

        As it relates to Wolfram Services, You will protect the privacy and legal rights of Your End Users under all applicable laws and regulations. You agree to obtain and maintain any required consents from End Users to allow Your access, monitoring, use, and disclosure of End User data. Further, You will notify Your End Users that data provided as part of the Services may be made available to Wolfram as a condition of verifying Your compliance with the obligations set forth in these Terms. You agree that Your use of the Services, including any Applications, will comply with all United States or relevant jurisdiction export restrictions and embargoes. Upon learning that any Application or End User's use of an Application, or data contained therein, is Prohibited, You agree to immediately suspend the Application and remove applicable data or to suspend access to the End User (as may be applicable). Wolfram reserves the right, if You do not suspend or remove as specified within 24 hours, to disable the Services (as may be applicable) until such violation is corrected.

        </div>

    4.  <span id="prohibited-use">Prohibited Use</span>
        1.  You will not, and You will not allow Your End Users to (i) violate or encourage the violation of the legal or equitable rights of others; (ii) engage in, promote, or encourage illegality; (iii) conduct any unlawful, invasive, infringing, defamatory, or fraudulent activity; (iv) distribute viruses, worms, Trojan horses, corrupted files, hoaxes, or other items of a destructive or deceptive nature; (v) interfere with anyone's appropriate use of the Services; (vi) disable, interfere with, or circumvent any aspect of the Services; (vii) generate, distribute, publish, or facilitate spam; or (viii) use the Services to access any other Wolfram Service in a way that violates any applicable Terms or Additional Terms.

            Further, You will not, and will not allow third parties under Your control, including End Users, to (i) copy, modify, create a derivative work of, reverse engineer, decompile, translate, disassemble, or otherwise attempt to extract the source code of the Services or any component thereof, except to the extent such restriction is expressly prohibited by applicable law; (ii) use the Services for activities where the use or failure of the Services could lead to death, personal injury, or environmental damage, such as the operation of nuclear facilities, air traffic control, or life support systems; (iii) sublicense, resell, or distribute the Services or any component thereof separate from any integrated Application; (iv) use the Services to create, train, or improve (directly or indirectly) a substantially similar product or service; (v) create multiple Applications to simulate or act as a single Application or otherwise access the Services in a manner intended to avoid incurring fees; (vi) unless otherwise set forth in individual terms, use the Services to operate or enable any telecommunications service or in connection with any Application that allows End Users to place calls or to receive calls from any public switched telephone network; (vii) process or store any data that is prohibited by the International Traffic in Arms Regulations maintained by the US Department of State; or (viii) claim You are affiliated with or endorsed by Wolfram in any way.

            Upon learning that any Application or End User's use of a Service, or data contained therein, is Prohibited, You agree to immediately suspend the use of that Service and remove applicable data or to suspend access to the End User (as may be applicable). Wolfram reserves the right, if You do not suspend or remove as specified within 24 hours, to terminate the applicable End User's or End Users' access, disable the Application, and/or disable the Services (as may be applicable) until such violation is corrected.

            Unless otherwise specified in writing, Wolfram does not intend uses of the Services to create obligations under HIPAA and makes no representations that the Services satisfy HIPAA requirements. If You are (or become) a Covered Entity or Business Associate as defined in HIPAA, You agree not to use the Services for any purpose or in any manner involving Protected Health Information (as defined in HIPAA and HIPAA regulations) unless You have received prior written consent to such use from Wolfram.

            Wolfram may provide additional documentation for Your use of the Services. The documentation may specify restrictions on or requirements for how Applications may be built or the Services may be used, and You agree to comply with any such instructions.

            Wolfram responds to notices of alleged copyright infringement and terminates accounts of repeat infringers according to the process set out in the US Digital Millennium Copyright Act. You may notify Wolfram of suspected violations of Your copyrights or those of End Users by submitting a DMCA notice to <dmca@wolfram.com>.

            Any Applications that You provide to End Users must have material value independent of the Services.

            Neither You nor Your End Users may use the Services in any way prohibited by law, including United States embargoes and export restrictions.

        2.  These Terms prohibit the training of artificial intelligence ("AI") models using data from the Services. You shall not (i) use the Services to train, fine-tune, or update AI models, including but not limited to language models, image recognition models, and machine learning algorithms; (ii) use data from the Services to generate training datasets for AI models; or (iii) use AI models trained on data from the Services for any purpose, whether commercial or otherwise.

            The material provided by the Services is intended to be used by a human being in the form in which it is delivered. You are not allowed to systematically extract data from the results returned and build them into a new raw data table, source, language model, or AI system. Use of the Services to produce, cache, or otherwise store data in a manner that circumvents the intended usage of the Services, with the aim of accessing or retrieving information without directly using the Services, is not permitted. This includes but is not limited to preemptively gathering or storing data to avoid continuous use of the Services while retaining access to the data obtained.

            Scraping or bulk downloading of data from the Services is strictly prohibited. You shall not attempt to reverse-engineer or recreate the Services' data or algorithms. Additionally, the Services should not be used in conjunction with your AI-powered tools or services unless a separate licensing agreement is in place.

            Licensing Options: These are our general Terms of Use for Wolfram Services. For other potential uses, including those involving AI models or open-source distribution, alternative licensing models may be available. If you donâ€™t want to be bound by these Terms, please contact us for options that more closely align with your desired use.

    </div>

3.  ### Fees and Payments

    1.  <div id="payment-for-the-services">

        Payment for the Services, including any recurring or periodic charges, is set forth in Your Services order or Additional Terms, if applicable. Wolfram's measurement of Your use of the Services is final. Fees associated with your Wolfram Services are non-refundable. Your non-payment or late payment may result in interest charges at the rate of 1.5% per month (or the highest rate permitted by law) and/or the suspension of Your access to the Services. We may take steps to collect any unpaid fees, and You may be responsible for costs related to that collection.

        </div>

    2.  <div id="authorized-user">

        By providing payment information to Wolfram or to one of Our third-party payment processors, You are representing to Wolfram that You are the authorized user of the card or account associated with that payment, and You authorize Wolfram to charge Your provided payment medium or to process Your payment with the payment processor for any fees associated therewith. Additionally, You agree that Your continued use of the Services authorizes Wolfram to charge Your payment method in the amount of any applicable recurring payment. To avoid interruption of Your Service, we may participate in programs supported by Your payment provider to update Your payment information. You authorize Us or Our third-party payment processors to continue billing and charging Your account for amounts owed with the information that We obtain.

        </div>

    3.  <div id="taxes-and-third-party-fees">

        Taxes and Third-Party Fees. Wolfram may charge You applicable sales taxes in addition to any of Our fees or third-party fees.

        </div>

4.  <div id="intellectual-property">

    ### Intellectual Property

    1.  <div>

        Intellectual Property Rights are any and all rights existing from time to time under patent law, copyright law, trade secret law, trademark law, and unfair competition law; any and all other proprietary rights; and any and all applications, renewals, extensions, and restorations thereof.

        </div>

    2.  <div>

        Except as expressly set forth herein, no party is granted any rights, implied or otherwise, to another's content or their Intellectual Property. As between the parties, You own all Intellectual Property Rights in End User data. Wolfram owns all Intellectual Property rights in the Services.

        </div>

    3.  <div id="companys-ownership-of-the-products">

        Company's Ownership of the Products. Wolfram is the sole owner of the Services with the exception of the portions licensed by Wolfram from third-party owners, if any. Wolfram is the holder of the Intellectual Property Rights in the Services, including, without limitation, such aspects of the Software as its code, structure, sequence, organization, "look and feel", programming language, and compilations of command names, descriptors, and data. Use of the Services, unless pursuant to the terms of a license or as otherwise authorized by law, is an infringement of Intellectual Property Rights.

        </div>

    4.  <div id="user-content">

        User Content. When publishing academic research, the Services should be appropriately cited as a reference and/or described in a methods section. Notwithstanding the obligation to provide the acknowledgment stated above, no other right to use the names, marks, or other distinctions of the Services or Wolfram is granted.

        </div>

    </div>

5.  <div id="data-security-privacy">

    ### Data Security/Privacy

    1.  <div id="data-security">

        Data Security. Wolfram has implemented industry-standard systems and procedures to safeguard Your data. By using the Services, You agree to allow Wolfram to process and store Your Applications and data and that of Your End Users.

        </div>

    2.  <div id="data-retention-policy">

        Company's Data Retention Policy. Wolfram takes privacy and data protection seriously and is committed to safeguarding data You share with us. To learn more, please see Our [Privacy Policy](https://www.wolfram.com/legal/privacy/wolfram/).

        </div>

    </div>

6.  <div id="disclaimers-limited-liability">

    ### Disclaimers/Limited Liability

    1.  <div id="disclaimer-of-warranties">

        Disclaimer of Warranties. Except as expressly provided for herein, to the maximum extent permitted by applicable law, Wolfram and its suppliers do not make any warranty of any kind, whether express, implied, statutory, or otherwise, including without limitation warranties of merchantability, fitness for a particular use, and noninfringement. Wolfram and its suppliers are not responsible or liable for the deletion of or failure to store any End User data and other communications maintained or transmitted through use of the Services. You are solely responsible for securing and backing up Your data. Neither Wolfram nor its suppliers warrant that the operation of Our Services will be error free or uninterrupted.

        </div>

    2.  <div id="limitation-of-liability">

        Limitation of Liability. To the maximum extent permitted by applicable law, neither party, nor Wolfram suppliers, will be liable under these Terms for lost revenues or indirect, special, incidental, consequential, exemplary, or punitive damages, even if the party or supplier knew or should have known that such damages were possible and even if direct damages do not satisfy a remedy.

        To the maximum extent permitted by applicable law, neither party, nor Wolfram suppliers, may be held liable under these Terms for more than the amount paid by You to Wolfram during the 12 months prior to the event giving rise to liability.

        The above limitations of liability do not apply to breaches of confidentiality obligations, violations of a party's Intellectual Property Rights by the other party or a supplier, or indemnification obligations.

        </div>

    3.  <div id="indemnification">

        Indemnification. Unless prohibited by applicable law, You will indemnify, defend, and hold harmless Wolfram from and against all liabilities, damages, and costs (including settlement costs and reasonable attorneys' fees) arising out of a third-party claim (i) regarding Your Applications, End Users, or data; or (ii) regarding Your or Your End Users' use of the cloud where such use constitutes Prohibited Use as defined herein. Wolfram will indemnify, defend, and hold harmless You from and against all liabilities, damages, and costs (including settlement costs and reasonable attorneys' fees) arising out of a third-party claim that Wolfram technology used to provide the Services (excluding any free/open-source software) or any intellectual property infringes or misappropriates any patent, copyright, trade secret, or trademark of such third party. Notwithstanding the foregoing, in no event will Wolfram have any obligations or liability under this Section arising from (i) use of any Service or Intellectual Property in a modified, unauthorized, or unintended form or in combination with materials not furnished by Wolfram; (ii) Your violation of these Terms; (iii) use of non-current versions of the Services or Intellectual Property; and (iv) any End User data.

        If Wolfram reasonably believes the Services infringe a third party's Intellectual Property Rights, then Wolfram may, at its sole option and expense, (i) obtain the right for You to continue using the Services; (ii) provide a non-infringing, functionally equivalent replacement; or (iii) modify the Services so that they no longer infringe. If Wolfram does not believe the foregoing options are commercially reasonable, then Wolfram may suspend or terminate Your use of the impacted Services.

        As a condition to indemnification for a claim, the party seeking indemnification must promptly notify the other party of the claim in writing and cooperate with the other party in defending the claim. The indemnifying party has full control and authority over the defense, except that (i) any settlement requiring the party seeking indemnification to admit liability or to pay any money will require that party's prior written consent, with such consent not to be unreasonably withheld or delayed; and (ii) the other party may join in the defense with its own counsel at its own expense. Notwithstanding the foregoing, if the indemnified party settles without the prior written consent of the indemnifying party, the indemnifying party has no obligation of contribution. The indemnities above are the only remedy under these Terms for violation of a third party's Intellectual Property Rights.

        </div>

    </div>

7.  <div id="notice-assignment-etc">

    ### Notice, Assignment, Force Majeure, Partnership, etc.

    All notices must be in writing and addressed to the other party's legal department, corporate officer, or registered agent. The email address for notices being sent to Wolfram is <legal@wolfram.com>. Notice will be effective upon receipt of written or automated confirmation.

    Neither party will be liable for failure or delay in performance to the extent caused by circumstances beyond its reasonable control.

    These Terms do not create any agency, partnership, or joint venture between the parties.

    If any Term (or part of a Term) herein is invalid, illegal, or unenforceable, the rest of the Terms will remain in effect.

    No Third-Party Beneficiaries. These Terms do not confer any benefits on any third party unless it expressly states that it does.

    Conflicting Terms. If there is a conflict between the documents that make up Your Additional Terms and these Terms, the Additional Terms will control.

    Force Majeure. No party will be liable to the other for any failure or delay in performing any obligation (other than Your payment obligations to Wolfram) under the Terms if the failure or delay is due to unforeseen events, which occur after the effectiveness of the Terms and which are beyond reasonable control of the parties, such as strikes, war, terrorist acts, riots, natural disasters, or refusal of license by the government or other governmental agencies, in so far as such an event prevents or delays a party from fulfilling its obligations and cannot be avoided with reasonable cost or effort.

    </div>

</div>

<div class="rightcolumn">

<div class="sidebarTop">

Legal (локальный ресурс исходного примера не включён)

</div>

<div class="sidebar">

- Privacy Policies<span class="privacyArrow keyarrowDown keyarrowUp"></span>

- <div class="legalLinks">

  - Wolfram (локальный ресурс исходного примера не включён)
  - Wolfram\|Alpha (локальный ресурс исходного примера не включён)
  - Data Retention (локальный ресурс исходного примера не включён)
  - CCPA Addendum (локальный ресурс исходного примера не включён)

  </div>

<!-- -->

- Terms of Use<span class="termsArrow keyarrowDown keyarrowUp"></span>

- <div class="legalLinks">

  - Wolfram (локальный ресурс исходного примера не включён)
  - Wolfram Research (локальный ресурс исходного примера не включён)
  - [Wolfram\|Alpha](http://www.wolframalpha.com/termsofuse/)
  - [Wolfram\|Alpha Pro](https://www.wolframalpha.com/termsofuse/pro/)
  - [Wolfram\|Alpha API](https://products.wolframalpha.com/api/commercial-termsofuse)
  - Wolfram ID (локальный ресурс исходного примера не включён)
  - Wolfram Engine (локальный ресурс исходного примера не включён)
  - Wolfram Notebook (локальный ресурс исходного примера не включён)
  - Wolfram Enterprise Private Cloud (локальный ресурс исходного примера не включён)
  - Wolfram Application Server (локальный ресурс исходного примера не включён)
  - Wolfram Programming Lab (локальный ресурс исходного примера не включён)
  - [Wolfram Community](http://community.wolfram.com/tou)
  - Wolfram Connected Devices Project (локальный ресурс исходного примера не включён)
  - Wolfram Demonstrations Project (локальный ресурс исходного примера не включён)
  - Liveminting (локальный ресурс исходного примера не включён)
  - Mathworld (локальный ресурс исходного примера не включён)
  - WolframTones (локальный ресурс исходного примера не включён)
  - Wolfram Science (локальный ресурс исходного примера не включён)
  - Wolfram Research Screensavers and Wallpapers (локальный ресурс исходного примера не включён)
  - Wolfram User Portal (локальный ресурс исходного примера не включён)
  - Wolfram Chat (локальный ресурс исходного примера не включён)

  </div>

<!-- -->

- License Agreements<span class="licenseArrow keyarrowDown keyarrowUp"></span>

- <div class="legalLinks">

  - Wolfram Mathematica (локальный ресурс исходного примера не включён)
  - Wolfram System Modeler (локальный ресурс исходного примера не включён)
  - Wolfram System Modeler Library (локальный ресурс исходного примера не включён)
  - Wolfram Finance Platform (локальный ресурс исходного примера не включён)
  - Wolfram\|Alpha Notebook Edition (локальный ресурс исходного примера не включён)
  - Wolfram Raspberry Pi Bundle (локальный ресурс исходного примера не включён)
  - Wolfram Player (локальный ресурс исходного примера не включён)
  - webMathematica Professional (локальный ресурс исходного примера не включён)
  - webMathematica Amateur (локальный ресурс исходного примера не включён)
  - WolframTones (локальный ресурс исходного примера не включён)
  - MathLink (локальный ресурс исходного примера не включён)
  - J/Link (локальный ресурс исходного примера не включён)
  - Wolfram\|Alpha Toolbar (локальный ресурс исходного примера не включён)
  - Wolfram Application Pack (локальный ресурс исходного примера не включён)
  - Other (локальный ресурс исходного примера не включён)

  </div>

<!-- -->

- Publishing and Submissions<span class="licenseArrow keyarrowDown keyarrowUp"></span>

- <div class="legalLinks">

  - Wolfram Challenges (локальный ресурс исходного примера не включён)
  - Wolfram Competitions (локальный ресурс исходного примера не включён)
  - [Wolfram Data Repository](https://datarepository.wolframcloud.com/submission-agreement)
  - [Wolfram Demonstrations](http://demonstrations.wolfram.com/submissionpolicy.html)
  - [Wolfram Resource System](https://datarepository.wolframcloud.com/publisher-agreement)

  </div>

<!-- -->

- Terms of Service<span class="serviceArrow keyarrowDown keyarrowUp"></span>

- <div class="legalLinks">

  - Enterprise Support (локальный ресурс исходного примера не включён)
  - AI Access (локальный ресурс исходного примера не включён)
  - Professional Support (локальный ресурс исходного примера не включён)
  - Personal License Support (локальный ресурс исходного примера не включён)

  </div>

<!-- -->

- Accessibility<span class="accessArrow keyarrowDown keyarrowUp"></span>

- <div class="legalLinks">

  - Wolfram\|Alpha (локальный ресурс исходного примера не включён)
  - Wolfram Mathematica and Wolfram Player (локальный ресурс исходного примера не включён)
  - Wolfram System Modeler (локальный ресурс исходного примера не включён)
  - Quezzio (локальный ресурс исходного примера не включён)

  </div>

</div>

<div>

 (локальный ресурс исходного примера не включён)

</div>

</div>

</div>

<div id="_footer-top">

<div>

- Products

- [Wolfram\|One](https://www.wolfram.com/wolfram-one/?source=footer)

- [Mathematica](https://www.wolfram.com/mathematica/?source=footer)

- [AI Access](https://www.wolfram.com/ai-access/?source=footer)

- [Compute Services](https://www.wolfram.com/compute-services/?source=footer)

- [System Modeler](https://www.wolfram.com/system-modeler/?source=footer)

- 

  ------------------------------------------------------------------------

- [Wolfram\|Alpha Notebook Edition](https://www.wolfram.com/wolfram-alpha-notebook-edition/?source=footer)

- [Wolfram\|Alpha Pro](https://www.wolframalpha.com/pro/?source=footer)

- [Mobile Apps](https://www.wolfram.com/products/?source=footer#mobile-apps)

- 

  ------------------------------------------------------------------------

- [Wolfram Engine](https://www.wolfram.com/engine/?source=footer)

- [Wolfram Player](https://www.wolfram.com/player/?source=footer)

- 

  ------------------------------------------------------------------------

- [Volume & Site Licensing](https://www.wolfram.com/group-organization-licensing/?source=footer)

- [Server Deployment Options](https://www.wolfram.com/server-deployment-options/?source=footer)

</div>

<div>

- Consulting
- [Wolfram Consulting](https://consulting.wolfram.com/?source=footer)

<!-- -->

- Repositories

- [Data Repository](https://datarepository.wolframcloud.com/?source=footer)

- [Function Repository](https://resources.wolframcloud.com/FunctionRepository/?source=footer)

- [Community Paclet Repository](https://resources.wolframcloud.com/PacletRepository/?source=footer)

- [Neural Net Repository](https://resources.wolframcloud.com/NeuralNetRepository/?source=footer)

- [Prompt Repository](https://resources.wolframcloud.com/PromptRepository/?source=footer)

- 

  ------------------------------------------------------------------------

- [Wolfram Language Example Repository](https://resources.wolframcloud.com/ExampleRepository/?source=footer)

- [Notebook Archive](https://notebookarchive.org/?source=footer)

- <a href="https://github.com/wolframresearch/?source=footer" target="_blank">Wolfram GitHub</a>

</div>

<div>

- Learning

- [Wolfram U](https://www.wolfram.com/wolfram-u/?source=footer)

- [Wolfram Language Documentation](https://reference.wolfram.com/language/?source=footer)

- [Webinars & Training](https://events.wolfram.com/?source=footer)

- [Educational Programs](https://education.wolfram.com/programs/?source=footer)

- 

  ------------------------------------------------------------------------

- [Wolfram Language Introduction](https://www.wolfram.com/language/elementary-introduction/3rd-ed/?source=footer)

- [Fast Introduction for Programmers](https://www.wolfram.com/language/fast-introduction-for-programmers/?source=footer)

- [Fast Introduction for Math Students](https://www.wolfram.com/language/fast-introduction-for-math-students/?source=footer)

- [Books](https://www.wolfram.com/books/?source=footer)

- 

  ------------------------------------------------------------------------

- [Wolfram Community](https://community.wolfram.com/?source=footer)

- [Wolfram Blog](https://blog.wolfram.com/?source=footer)

</div>

<div>

- Public Resources

- [Wolfram\|Alpha](https://www.wolframalpha.com/?source=footer)

- [Wolfram Problem Generator](https://www.wolframalpha.com/pro/problem-generator/?source=footer)

- [Wolfram Challenges](https://challenges.wolframcloud.com/?source=footer)

- 

  ------------------------------------------------------------------------

- [Computer-Based Math](https://www.computerbasedmath.org/?source=footer)

- [Computational Thinking](https://www.wolfram.com/resources/computational-thinking/?source=footer)

- [Computational Adventures](https://www.computationinitiative.org/computational-adventures/?source=footer)

- 

  ------------------------------------------------------------------------

- [Demonstrations Project](https://demonstrations.wolfram.com/?source=footer)

- [Wolfram Data Drop](https://datadrop.wolframcloud.com/?source=footer)

- <a href="https://mathworld.wolfram.com/?source=footer" target="_blank">MathWorld</a>

- [Wolfram Science](https://www.wolframscience.com/?source=footer)

- [Wolfram Media Publishing](https://www.wolfram-media.com/?source=footer)

</div>

<div>

- Customer Resources

- [Store](https://www.wolfram.com/get-products-services/?source=footer)

- [Product Downloads](https://www.wolfram.com/download-center/?source=footer)

- [User Portal](https://user.wolfram.com/portal/?source=footer)

- [Your Account](https://account.wolfram.com/?source=footer)

- [Organization Access](https://www.wolfram.com/siteinfo/?source=footer)

- 

  ------------------------------------------------------------------------

- [Support FAQ](https://support.wolfram.com/?source=footer)

- [Contact Support](https://www.wolfram.com/support/contact/?source=footer)

<!-- -->

- Company
- [About Wolfram](https://www.wolfram.com/company/?source=footer)
- [Careers](https://www.wolfram.com/company/careers/?source=footer)
- [Contact](https://www.wolfram.com/company/contact/?source=footer)
- [Events](https://company.wolfram.com/events/?source=footer)

</div>

</div>

<div id="_footer-bottom" class="_page-width-no-padding">

<div class="flex">

<div id="_footer-social">

<div class="flex">

<a href="https://www.facebook.com/wolframresearch?source=footer" target="_blank"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci1mYWNlYm9vayI+PHVzZSBocmVmPSIjX2Zvb3Rlci1mYWNlYm9vayIgLz48dGl0bGU+RmFjZWJvb2s8L3RpdGxlPjwvc3ZnPg==" class="_icon _footer-facebook" /></a> <a href="https://x.com/WolframResearch?source=footer" target="_blank"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci10d2l0dGVyIj48dXNlIGhyZWY9IiNfZm9vdGVyLXR3aXR0ZXIiIC8+PHRpdGxlPlg8L3RpdGxlPjwvc3ZnPg==" class="_icon _footer-twitter" /></a> <a href="https://twitch.tv/wolfram?source=footer" target="_blank"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci10d2l0Y2giPjx1c2UgaHJlZj0iI19mb290ZXItdHdpdGNoIiAvPjx0aXRsZT5Ud2l0Y2g8L3RpdGxlPjwvc3ZnPg==" class="_icon _footer-twitch" /></a> <a href="https://www.linkedin.com/company/wolfram-research/?source=footer" target="_blank"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci1saW5rZWRpbiI+PHVzZSBocmVmPSIjX2Zvb3Rlci1saW5rZWRpbiIgLz48dGl0bGU+TGlua2VkSW48L3RpdGxlPjwvc3ZnPg==" class="_icon _footer-linkedin" /></a> <a href="https://www.youtube.com/user/wolframresearch?source=footer" target="_blank"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci15b3V0dWJlIj48dXNlIGhyZWY9IiNfZm9vdGVyLXlvdXR1YmUiIC8+PHRpdGxlPllvdVR1YmU8L3RpdGxlPjwvc3ZnPg==" class="_icon _footer-youtube" /></a> [<img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci1zcGlrZXkiPjx1c2UgaHJlZj0iI19mb290ZXItc3Bpa2V5IiAvPjx0aXRsZT5Xb2xmcmFtPC90aXRsZT48L3N2Zz4=" class="_icon _footer-spikey" />](https://www.wolfram.com/?source=footer)

</div>

</div>

<div id="_footer-language" class="text-align-r">

<div class="display-ib">

Â© <span id="_footer-year">2026</span> [Wolfram](https://www.wolfram.com/?source=footer) <span class="_separator">\|</span> [Legal](https://www.wolfram.com/legal/?source=footer) & [Privacy Policy](https://www.wolfram.com/legal/privacy/wolfram/?source=footer) <span class="_separator">\|</span>

</div>

<div class="display-ib">

<div id="_language-picker">

<div class="_current-language">

<img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci1nbG9iZSI+PHVzZSBocmVmPSIjX2Zvb3Rlci1nbG9iZSIgLz48L3N2Zz4=" class="_icon _footer-globe" /> English

</div>

<div class="_dropdown">

- <img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci1jaGVjayI+PHVzZSBocmVmPSIjX2Zvb3Rlci1jaGVjayIgLz48L3N2Zz4=" class="_icon _footer-check" />![en (локальный ресурс исходного примера не включён)]()

</div>

</div>

</div>

</div>

</div>

</div>

<div style="height: 0; width: 0; position: absolute; visibility: hidden; top: -999999999999px;">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogICAgPGcgaWQ9Il9mb290ZXItaWNvbnMiPgogICAgICAgIDxzeW1ib2wgaWQ9Il9mb290ZXItZmFjZWJvb2siIHZpZXdib3g9IjAgMCAxNSAxNSI+CiAgICAgICAgICAgIDxwYXRoIGZpbGw9ImN1cnJlbnRDb2xvciIgZD0iTTEzLjQsMEgxLjdDLjgsMCwwLC44LDAsMS43djExLjdjMCwuOS43LDEuNywxLjMsMS43aDExLjdjMS4zLDAsMi0uOCwyLTEuN1YxLjdjMC0uOS0uOC0xLjctMS43LTEuN1pNMTEuOCw5LjFoLTEuNnY1LjloLTIuNXYtNS45aC0xLjJ2LTIuMmgxLjJ2LTEuOWMwLTEuNy43LTIuNywyLjctMi43aDJ2Mi4xaC0xLjNjLS44LDAtLjguMy0uOC44djEuN2gxLjlsLS4yLDIuMmgwWiIgLz4KICAgICAgICA8L3N5bWJvbD4KICAgICAgICA8c3ltYm9sIGlkPSJfZm9vdGVyLXR3aXR0ZXIiIHZpZXdib3g9IjAgMCAxNSAxNSI+CiAgICAgICAgICAgIDxwb2x5Z29uIGZpbGw9ImN1cnJlbnRDb2xvciIgcG9pbnRzPSIzLjkgMy42IDEwLjEgMTEuNyAxMS4xIDExLjcgNC45IDMuNiAzLjkgMy42Ij48L3BvbHlnb24+CiAgICAgICAgICAgIDxwYXRoIGZpbGw9ImN1cnJlbnRDb2xvciIgZD0iTTEzLjQsMEgxLjdDLjgsMCwwLC44LDAsMS43djExLjdjMCwuOS43LDEuNywxLjcsMS43aDExLjdjLjksMCwxLjctLjgsMS43LTEuN1YxLjdjMC0uOS0uOC0xLjctMS43LTEuN1pNOS42LDEyLjdsLTIuNy0zLjUtMy4xLDMuNWgtMS43bDQtNC42TDEuOSwyLjZoMy41bDIuNCwzLjIsMi45LTMuMmgxLjdsLTMuOCw0LjMsNC40LDUuOHMtMy40LDAtMy40LDBaIiAvPgogICAgICAgIDwvc3ltYm9sPgogICAgICAgIDxzeW1ib2wgaWQ9Il9mb290ZXItdHdpdGNoIiB2aWV3Ym94PSIwIDAgMTUgMTUiPgogICAgICAgICAgICA8cmVjdCBmaWxsPSJjdXJyZW50Q29sb3IiIHg9IjkuMyIgeT0iNC45IiB3aWR0aD0iMS4zIiBoZWlnaHQ9IjQiIC8+CiAgICAgICAgICAgIDxyZWN0IGZpbGw9ImN1cnJlbnRDb2xvciIgeD0iNS43IiB5PSI0LjkiIHdpZHRoPSIxLjMiIGhlaWdodD0iNCIgLz4KICAgICAgICAgICAgPHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMTMuNCwwSDEuN0MuOCwwLDAsLjgsMCwxLjd2MTEuN2MwLC45LjcsMS43LDEuNywxLjdoMTEuN2MuOSwwLDEuNy0uOCwxLjctMS43VjEuN2MwLS45LS44LTEuNy0xLjctMS43Wk0xMi45LDkuNmwtMi4zLDIuM2gtMy42bC0yLDJ2LTJoLTNWMi4zaDEwLjl2Ny4yaDBaIiAvPgogICAgICAgIDwvc3ltYm9sPgogICAgICAgIDxzeW1ib2wgaWQ9Il9mb290ZXItbGlua2VkaW4iIHZpZXdib3g9IjAgMCAxNSAxNSI+CiAgICAgICAgICAgIDxwYXRoIGZpbGw9ImN1cnJlbnRDb2xvciIgZD0iTTEzLjMsMEgxLjdDLjgsMCwwLC44LDAsMS43djExLjdjMCwuOS44LDEuNywxLjcsMS43aDExLjdjLjksMCwxLjctLjgsMS43LTEuN1YxLjdjMC0uOS0uOC0xLjctMS43LTEuN1pNNC40LDEyLjloLTIuMnYtNy4yaDIuMnY3LjJoMFpNMy4zLDQuOGMtLjcsMC0xLjMtLjYtMS4zLTEuM3MuNi0xLjMsMS4zLTEuMywxLjMuNiwxLjMsMS4zLS42LDEuMy0xLjMsMS4zWk0xMi44LDEyLjloLTIuMnYtMy44YzAtMS0uNC0xLjYtMS4yLTEuNnMtMS40LjYtMS40LDEuNnYzLjhoLTIuMnYtNy4yaDIuMnYxcy42LTEuMiwyLjItMS4yLDIuNi45LDIuNiwyLjl2NC42aDBaIiAvPgogICAgICAgIDwvc3ltYm9sPgogICAgICAgIDxzeW1ib2wgaWQ9Il9mb290ZXIteW91dHViZSIgdmlld2JveD0iMCAwIDE1IDE1Ij4KICAgICAgICAgICAgPHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMTMuNCwwSDEuN0MuOCwwLDAsLjgsMCwxLjd2MTEuN2MwLC45LjcsMS43LDEuNywxLjdoMTEuN2MuOSwwLDEuNy0uOCwxLjctMS43VjEuN2MwLS45LS44LTEuNy0xLjctMS43Wk00LjIsMTEuNFYzLjVsNy40LDMuOS03LjQsNGgwWiIgLz4KICAgICAgICA8L3N5bWJvbD4KICAgICAgICA8c3ltYm9sIGlkPSJfZm9vdGVyLXNwaWtleSIgdmlld2JveD0iMCAwIDE1IDE1Ij4KICAgICAgICAgICAgPGcgZmlsbD0iY3VycmVudENvbG9yIj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0xMy4zLDBIMS43Qy44LDAsMCwuOCwwLDEuN3YxMS42YzAsLjkuOCwxLjcsMS43LDEuN2gxMS42Yy45LDAsMS43LS43LDEuNy0xLjdWMS43YzAtLjktLjgtMS43LTEuNy0xLjdaTTEzLjY2OSw5LjUwNWwtMi42MjQuNTcyLjI2NywyLjY3Mi0yLjQ1OC0xLjA4MS0xLjM1NCwyLjMxOC0xLjM1NS0yLjMxOC0yLjQ1OCwxLjA4LjI2Ni0yLjY3Mi0yLjYyMy0uNTcyLDEuNzg2LTIuMDA0LTEuNzg2LTIuMDA1LDIuNjI0LS41NzEtLjI2Ni0yLjY3MiwyLjQ1OCwxLjA4LDEuMzU0LTIuMzE4LDEuMzU0LDIuMzE4LDIuNDU5LTEuMDc5LS4yNjcsMi42NzEsMi42MjMuNTcyLTEuNzg2LDIuMDA0LDEuNzg2LDIuMDA0WiIgLz4KICAgICAgICAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iMTIuMTU0IDguNjg3IDExLjEzOCA4LjMzOSAxMC40MzEgNy40MiAxMS4zMiA3Ljc1IDEyLjE1NCA4LjY4NyI+PC9wb2x5Z29uPgogICAgICAgICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSI4LjQ0MiAxMS4yMTMgNy43OTQgMTIuMzIyIDcuNzk0IDExLjE5MiA4LjQ2NiAxMC4yMTIgOC40NDIgMTEuMjEzIj48L3BvbHlnb24+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBwb2ludHM9IjYuNjQ3IDQuNjY3IDUuNTQ1IDQuMjc1IDQuOTIzIDMuNDM1IDYuMDgyIDMuOTQ0IDYuNjQ3IDQuNjY3Ij48L3BvbHlnb24+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBwb2ludHM9IjguOTE5IDMuOTQ1IDEwLjA3OCAzLjQzNiA5LjQ1NSA0LjI3NSA4LjM1NCA0LjY2NyA4LjkxOSAzLjk0NSI+PC9wb2x5Z29uPgogICAgICAgICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSIxMC40NDQgNS4wNDkgOS44OTYgNS44MjggOS45MjggNC42MjMgMTAuNTc0IDMuNzUyIDEwLjQ0NCA1LjA0OSI+PC9wb2x5Z29uPgogICAgICAgICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSI3LjUgMTAuNTgzIDYuNTc3IDkuMjM1IDcuNTAxIDcuOTgzIDguNDIzIDkuMjM1IDcuNSAxMC41ODMiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iNS43MTEgNi41NzcgNS42NjYgNC45NDEgNy4yMDcgNS40ODggNy4yMDcgNy4wODEgNS43MTEgNi41NzciPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iNy43OTQgNS40ODggOS4zMzQgNC45NDEgOS4yODkgNi41NzcgNy43OTQgNy4wODEgNy43OTQgNS40ODgiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iNC41NTcgNS4wNDkgNC40MjggMy43NTMgNS4wNzIgNC42MjIgNS4xMDQgNS44MjcgNC41NTcgNS4wNDkiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iNy4wMjYgNy42MzkgNi4xMDQgOC44OSA0LjUzNCA4LjQyOCA1LjUyOSA3LjEzNCA3LjAyNiA3LjYzOSI+PC9wb2x5Z29uPgogICAgICAgICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSI2LjUzNCAxMC4yMTEgNy4yMDcgMTEuMTkyIDcuMjA3IDEyLjMyMiA2LjU1OCAxMS4yMTIgNi41MzQgMTAuMjExIj48L3BvbHlnb24+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBwb2ludHM9IjcuOTc0IDcuNjM5IDkuNDcxIDcuMTM0IDEwLjQ2NiA4LjQyOCA4Ljg5NiA4Ljg5IDcuOTc0IDcuNjM5Ij48L3BvbHlnb24+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBwb2ludHM9IjEyLjU2MyA1Ljg1NiAxMS40MDUgNy4xNTYgMTAuMDM1IDYuNjQ3IDEwLjg1NiA1LjQ4MyAxMi41NjMgNS44NTYiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iOC4zNzkgMy42ODEgNy41IDQuODA1IDYuNjIyIDMuNjgxIDcuNSAyLjE3NyA4LjM3OSAzLjY4MSI+PC9wb2x5Z29uPgogICAgICAgICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSIyLjQzNyA1Ljg1NSA0LjE0NSA1LjQ4MyA0Ljk2NSA2LjY0NyAzLjU5NyA3LjE1NSAyLjQzNyA1Ljg1NSI+PC9wb2x5Z29uPgogICAgICAgICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSIzLjY4MiA3Ljc0OSA0LjU2OSA3LjQyIDMuODYyIDguMzM5IDIuODQ2IDguNjg2IDMuNjgyIDcuNzQ5Ij48L3BvbHlnb24+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBwb2ludHM9IjIuOTc1IDkuMjYyIDQuMDQ3IDguODk2IDUuMjEyIDkuMjQgNC4yNTggOS41NDEgMi45NzUgOS4yNjIiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iNC41NDQgMTAuMDY2IDUuOTM0IDkuNjI3IDUuOTY5IDExLjEwNSA0LjM3MSAxMS44MDcgNC41NDQgMTAuMDY2Ij48L3BvbHlnb24+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBwb2ludHM9IjkuMDMxIDExLjEwNiA5LjA2NiA5LjYyOCAxMC40NTUgMTAuMDY3IDEwLjYyOSAxMS44MDggOS4wMzEgMTEuMTA2Ij48L3BvbHlnb24+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBwb2ludHM9IjEwLjc0MiA5LjU0MiA5Ljc4NyA5LjI0IDEwLjk1MyA4Ljg5NiAxMi4wMjYgOS4yNjMgMTAuNzQyIDkuNTQyIj48L3BvbHlnb24+CiAgICAgICAgICAgIDwvZz4KICAgICAgICA8L3N5bWJvbD4KICAgICAgICA8c3ltYm9sIGlkPSJfZm9vdGVyLWdsb2JlIiB2aWV3Ym94PSIwIDAgMjQgMjQiPgogICAgICAgICAgICA8cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxNy45M2MtMy45NS0uNDktNy0zLjg1LTctNy45MyAwLS42Mi4wOC0xLjIxLjIxLTEuNzlMOSAxNXYxYzAgMS4xLjkgMiAyIDJ2MS45M3ptNi45LTIuNTRjLS4yNi0uODEtMS0xLjM5LTEuOS0xLjM5aC0xdi0zYzAtLjU1LS40NS0xLTEtMUg4di0yaDJjLjU1IDAgMS0uNDUgMS0xVjdoMmMxLjEgMCAyLS45IDItMnYtLjQxYzIuOTMgMS4xOSA1IDQuMDYgNSA3LjQxIDAgMi4wOC0uOCAzLjk3LTIuMSA1LjM5eiIgLz4KICAgICAgICA8L3N5bWJvbD4KICAgICAgICA8c3ltYm9sIGlkPSJfZm9vdGVyLWNoZWNrIiB2aWV3Ym94PSIwIDAgMTMuNjkgMTEiPgogICAgICAgICAgICA8cG9seWdvbiBmaWxsPSJjdXJyZW50Q29sb3IiIHBvaW50cz0iMTMuNjkgMS42NiAxMi4wMyAwIDQuMzUgNy42OCAxLjY2IDQuOTUgMCA2LjYxIDQuMzUgMTEgMTMuNjkgMS42NiI+PC9wb2x5Z29uPgogICAgICAgIDwvc3ltYm9sPgogICAgPC9nPgo8L3N2Zz4=)

</div>

</div>

</div>

<span id="gl-footer-lang-message"></span> <span id="gl-footer-lang"></span><span id="gl-footer-lang-links">![ja (локальный ресурс исходного примера не включён)](https://www.wolfram.com/legal/terms/wolfram/index.html.ja?footer=lang) </span>

<div id="IPstripe-wrap">

</div>
