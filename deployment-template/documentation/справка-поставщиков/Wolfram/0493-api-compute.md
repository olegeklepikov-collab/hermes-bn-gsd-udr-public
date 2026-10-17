> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Wolfram: api-compute

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


<div class="header">

<div class="inner">

# Wolfram Language Computation API *Reference*

</div>

</div>

<div id="intro" class="section">

<div class="inner">

## An evaluator for Wolfram Language inputs

The Wolfram Language Computation API evaluates Wolfram Language code to give reliable, computationally driven results suitable for use by an LLM.

<a href="mailto:partner-program@wolfram.com" class="button" data-walid="WL-Computation-Access">Request API Access</a>

</div>

</div>

<div id="using-the-api" class="section">

<div class="inner">

## Using the API

### Basic Usage

<div>

A basic request to the API takes the following form:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="c2c/01.txt">

curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageCompute \\ -H "Content-Type: application/json" \\ -H "Authorization: YOUR-API-KEY" \\ -d '{ "code": "Sin\[Pi\]" }'

</div>

which yields the following response:

<div>

     "{
        "result":"Out[1]=0",
        "code":200,
        "success":true,
        "uuid":"${OBJECT_ID}"
    }"

</div>

</div>

### Request Parameters

<div>

The following parameters can be passed in the body of an API request:

<div class="n-column-table">

<div class="row">

<div class="cell key">

`"code"`

</div>

<div class="cell value">

required

</div>

<div class="cell description">

Wolfram Language code to evaluate

</div>

</div>

<div class="row">

<div class="cell key">

`"line"`

</div>

<div class="cell value">

default: `1`

</div>

<div class="cell description">

label for output

</div>

</div>

<div class="row">

<div class="cell key">

`"maxChars"`

</div>

<div class="cell value">

default: `10000`

</div>

<div class="cell description">

maximum characters of output to return

</div>

</div>

<div class="row">

<div class="cell key">

`"timeConstraint"`

</div>

<div class="cell value">

default: `60`

</div>

<div class="cell description">

maximum allowed evaluation time in seconds

</div>

</div>

</div>

#### `code` <span class="gray">(required)</span>

<div>

The code to be evaluated is passed to the API using the `"code"` parameter:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="c2c/02.txt">

curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageCompute \\ -H "Content-Type: application/json" \\ -H "Authorization: YOUR-API-KEY" \\ -d '{ "code": "TrigExpand@Sin\[2x\]" }'

</div>

    "{
      "result":"Out[1]= 2*Cos[x]*Sin[x]",
      "code":200,
      "success":true,
      "uuid":"${OBJECT_ID}"
    }"

Images and graphics are returned via a Markdown image URL:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="c2c/03.txt">

curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageCompute \\ -H "Content-Type: application/json" \\ -H "Authorization: YOUR-API-KEY" \\ -d '{ "code": "Graphics\[{Red, Circle\[\]}\]" }'

</div>

    "{
      "result":"Out1]=![Image (пример адреса или протокола; задаётся в целевой среде)",
      "code":200,
      "success":true,
      "uuid":"${OBJECT_ID}"
    }"

View the image:

<img src="img/output-image.png" width="210" />

The free-form prompt character, <span class="black-square-eq">`=`</span>, can be used to represent `ctrl-=` in inputs to retrieve curated data through natural language:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="c2c/04.txt">

curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageCompute \\ -H "Content-Type: application/json" \\ -H "Authorization: YOUR-API-KEY" \\ -d '{ "code": "\\\[FreeformPrompt\]\[\\France population\\\]" }'

</div>

    "{
      "result":"During evaluation of In[1]:= [INFO] Interpreted "France population" as: Entity["Country", "France"][EntityProperty["Country", "Population"]]
    Out[1]= Quantity[66438822, "People"]",
      "code":200,
      "success":true,
      "uuid":"${OBJECT_ID}"
    }"

</div>

#### `line` <span class="gray">(optional)</span>

<div>

The integer appearing in the output label can be overridden with the `"line"` parameter:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="c2c/05.txt">

curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageCompute \\ -H "Content-Type: application/json" \\ -H "Authorization: YOUR-API-KEY" \\ -d '{ "code": "Integrate\[x, {x, 0, 1}\]", "line": "50" }'

</div>

    "{
      "result":"Out[50]= 1/2",
      "code":200,
      "success":true,
      "uuid":"${OBJECT_ID}"
    }"

</div>

#### `maxChars` <span class="gray">(optional)</span>

<div>

The size of the output can be limited using the `"maxChars"` parameter:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="c2c/06.txt">

curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageCompute \\ -H "Content-Type: application/json" \\ -H "Authorization: YOUR-API-KEY" \\ -d '{ "code": "ExampleData\[{\\Text\\, \\AliceInWonderland\\}\]", "maxChars": 1000 }'

</div>

Elision markers `<<` and `>>` indicate where the output was shortened and by how much:

    {
      result:"Out[1]= I--DOWN THE RABBIT-HOLE 
      Alice was beginning to get very tired of sitting by her sister on the bank,
     
    >    and of having nothing to do. Once or twice she had peeped into 
    the book her sister was
     
    >    reading, but it had no pictures or conversations in it, "and 
    what is the use of a book,"
     
    >    thought Alice, "without pictures or conversations?" So she was 
    considering in her own mind (as
     
    >    well as she could, for the day made her feel very sleepy and 
    stupid), whether the pleasure of
     
    >    making a daisy-chain would be worth the trouble of getting up 
    and picking the daisies, when
     
    >    suddenly <<50875>>ve had such a curious dream!" said Alice. And 
    she told her sister, as well
     
    >    as she could remember them, all these strange adventures of hers 
    that you have just been
     
    >    reading about. Alice got up and ran off, thinking while she ran, 
    as well she might, what a
     
    >    wonderful dream it had been.",
      "code":200,
      "success":true,
      "uuid":"${OBJECT_ID}"
    }

</div>

#### `timeConstraint` <span class="gray">(optional)</span>

<div>

Evaluation time can be limited using the `"timeConstraint"` parameter:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="c2c/07.txt">

curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageCompute \\ -H "Content-Type: application/json" \\ -H "Authorization: YOUR-API-KEY" \\ -d '{ "code": "Pause\[60\]", "timeConstraint": "10" }'

</div>

When the time constraint is exceeded, `"result"` is a `Failure` expression:

    {
      "result":"Failure["EvaluationTimeExceeded", 
      <|"MessageTemplate" -> "Evaluation exceeded the `1` second time limit.", 
      "MessageParameters" -> {10}|>]",
      "code":200,
      "success":true,
      "uuid":"${OBJECT_ID}"
    }

</div>

### Response

<div>

The returned JSON contains the following fields:

- `result` (string) The result of evaluating the Wolfram Language expression passed in via the `"code"` body parameter
- `code` (integer) API status code (e.g. `200`, `400`, `403`, `501`, ...)
- `success` (Boolean) `true` or `false` depending on whether the request completed successfully
- `uuid` (string) A unique ID labeling the response

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

</div>
