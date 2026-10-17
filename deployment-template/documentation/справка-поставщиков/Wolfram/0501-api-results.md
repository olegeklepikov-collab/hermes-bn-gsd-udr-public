> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Wolfram: api-results

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


<div class="header">

<div class="inner">

# Wolfram\|Alpha Results API *Reference*

</div>

</div>

<div id="intro" class="section">

<div class="inner">

## Enhance your LLM prompts with results from the Wolfram\|Alpha knowledge engine

The Wolfram\|Alpha Results API assists users in generating prompts for LLMs by retrieving related facts, data and other content from Wolfram\|Alpha. This is the [Wolfram\|Alpha LLM API](https://products.wolframalpha.com/llm-api/documentation) customized for easy integration with the other [Wolfram APIs](https://www.wolfram.com/apis/documentation/).

<a href="mailto:partner-program@wolfram.com" class="button" data-walid="WA-Results-Access">Request API Access</a>

</div>

</div>

<div id="using-the-api" class="section">

<div class="inner">

## Using the API

### Basic Usage

<div>

A basic request to the API takes the following form:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="c2c/01.txt">

curl -X GET https://services.wolfram.com/api/cag/v1/WolframAlphaResult?input=properties+of+diamond \\ -H "Authorization: YOUR-API-KEY"

</div>

which yields the following response:

<div>

    Query:
    "properties of diamond"

    Assumption:
    Assuming "diamond" is a mineral
    To use as a material set assumption=*C.diamond-_*Material-
    To use as a class of materials set assumption=*C.diamond-_*MaterialClass-
    To use as referring to famous gems set assumption=*C.diamond-_*FamousGemClass-
    To use as a lamina set assumption=*C.diamond-_*Lamina-
    To use as a geometric object set assumption=*C.diamond-_*Geometry-
    To use as a surname set assumption=*C.diamond-_*Surname-
    To use as a glacier set assumption=*C.diamond-_*Glacier-
    To use as an administrative division set assumption=*C.diamond-_*AdministrativeDivision-
    To use as referring to consumer product brands set assumption=*C.diamond-_*ConsumerProductBrands-

    Input interpretation:
    diamond (mineral)

    Image:
    image: https://public6.wolframalpha.com/files/PNG_x6jy7gel1l.png
    Wolfram Language code: Entity["Mineral", "Diamond"][EntityProperty["Mineral", "Image"]]

    General properties:
    formula | C

    Basic properties:
    density | 3.515 g/cm^3
    transparency | transparent | subtransparent | translucent
    luster | adamantine | greasy
    Mohs hardness | 10
    tenacity | brittle
    streak | colorless
    magnetism | nonmagnetic
    color | colorless | white | gray | black | blue
    fracture | conchoidal
    molar mass | 12.01 g/mol (grams per mole)

    Mineral identifiers:
    Strunz ID | I/B.02-40
    Dana ID | 1.3.6.1

    Crystallographic properties:
    crystal system | cubic
    crystal class | 4/m-32/m
    unit cell volume | 45.38 Å^3 (cubic ångströms)
    d-spacing | 2.06 Å (ångströms) | 1.261 Å (ångströms) | 1.075 Å (ångströms)
    intensity | 100% | 25% | 16%
    molecules per unit cell | 8 molecules per cell
    refractive indices | 2.418 | 0 | 0 | 0 | 0 | 0
    dispersion | strong
    unit cell lengths | 3.567 Å (ångströms) | 3.567 Å (ångströms) | 3.567 Å (ångströms)
    unit cell angles | 90° (degrees) | 90° (degrees) | 90° (degrees)

    Wolfram|Alpha website result for "properties of diamond":
    https://www.wolframalpha.com/input?i=properties+of+diamond

</div>

</div>

### Request Parameters

<div>

All requests must include an `"input"` parameter. Queries must be URL encoded (e.g. spaces represented as `"%20"` and backslashes represented as `"%5c"`). For mathematical queries, the API will also accept input formatted using presentation LaTeX or MathML.

You can add URL-encoded parameters to customize output. Since the output for this API is intended for consumption by LLMs, only basic parameters are available. Many parameters from our [Full Results API](https://products.wolframalpha.com/api/documentation) are also available for use here:

- `"assumption"`
- `"ip"`
- `"latlong"`
- `"location"`
- `"scantimeout"`
- `"units"`
- `"width"`
- `"maxwidth"`
- `"plotwidth"`
- `"mag"`
- `"formattimeout"`
- `"parsetimeout"`
- `"totaltimeout"`
- `"id"`

For information on how to use these API parameters, view the [Full Results API documentation](https://products.wolframalpha.com/api/documentation?scrollTo=parameter-reference).

</div>

### Status Codes

<div id="status-codes">

HTTP Status `200`

This status indicates a success.

HTTP Status `400`

This status indicates that the API did not find an input parameter while parsing. In most cases, this can be fixed by checking that you have used the correct syntax for including the input parameter.

HTTP Status `403`

This status is returned when a request contains a missing or invalid API key in the authorization header. Double-check that your AppID is typed correctly and is using the correct syntax.

HTTP Status `501`

This status is returned if a given input value cannot be interpreted by this API. This is commonly caused by input that is misspelled, poorly formatted or otherwise unintelligible. Because this API is designed to return results for use in LLMs, the body of the `501` message may contain suggested inputs. You may occasionally receive this status when requesting information on topics that are restricted or not covered.

</div>

Use of these APIs is subject to the [API Terms of Use](https://products.wolframalpha.com/api/termsofuse) and [Commercial Terms of Use](https://products.wolframalpha.com/api/commercial-termsofuse).

</div>

</div>
