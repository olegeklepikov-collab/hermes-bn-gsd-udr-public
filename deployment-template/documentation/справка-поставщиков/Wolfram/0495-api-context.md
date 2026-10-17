> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Wolfram: api-context

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


<div class="header">

<div class="inner">

# Wolfram\|Alpha Context API *Reference*

</div>

</div>

<div id="intro" class="section">

<div class="inner">

## Augment LLM queries with related facts, figures, images and other content from Wolfram\|Alpha

The Wolfram\|Alpha Context API assists users by generating secondary Wolfram\|Alpha queries that give factual context relevant to a given input. These queries and their results are then returned to the user in the form of plaintext that is appropriate for use as part of an LLM prompt.

<a href="mailto:partner-program@wolfram.com" class="button" data-walid="WA-Context-Access">Request API Access</a>

</div>

</div>

<div id="using-the-api" class="section">

<div class="inner">

## Using the API

### Basic Usage

<div>

A basic request to the API takes the following form:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="c2c/01.txt">

curl -X POST https://services.wolfram.com/api/cag/v1/WolframAlphaContext \\ -H "Content-Type: application/json" \\ -H "Authorization: YOUR-API-KEY" \\ -d '{ "context": "How long would it take a cheetah to round the bases in baseball?" }'

</div>

which yields the following response:

    {
        "result":"IMPORTANT: The following information was automatically generated using Wolfram 
    Alpha and should be used to help answer the user's query using factual information.

    ======

    <result query='average speed of a cheetah' 
    url='https://www.wolframalpha.com/input?i=average+speed+of+a+cheetah'>

    # Input interpretation

    cheetah | maximum speed

    # Result

    75 mph (miles per hour)

    # Unit conversions

    120.7 km/h (kilometers per hour)

    33.53 m/s (meters per second)

    2012 m/min (meters per minute)

    2897 km/d (kilometers per day)

    65.17 kn (knots)

    # Corresponding quantity

    ![Image](https://public6.wolframalpha.com/files/GIF_1aoph4h7awc.gif)

    Time to travel 1 meter from t = d/v:
     | 30 ms (milliseconds)

    ![Image](https://public6.wolframalpha.com/files/GIF_1aopizdck34.gif)

    Time to travel 1 kilometer from t = d/v:
     | 30 seconds

    ![Image](https://public6.wolframalpha.com/files/GIF_1aoplblznlf.gif)

    Observed wind intensity from v = 0.836B^(3/2) m/s:
     | 12 Beaufort scale numbers

    # Scientific name

    Acinonyx jubatus

    # Human comparisons

    ![Image](https://public6.wolframalpha.com/files/GIF_1aopa6l9kkp.gif)

    corresponding human value | 28 mph (miles per hour)
    fraction of human value | 2.7

    # Comparison as speed

     ≈ 0.9 × record human-powered vehicle land speed ( 83.13 mph )

     ≈ 0.999993 × cheetah sprint speed ( ≈ 75 mph )

     ≈ 1.1 × speed of the fastest water animal (sailfish) ( ≈ 110 km/h )

    </result>

    <result query='length of a baseball diamond' 
    url='https://www.wolframalpha.com/input?i=length+of+a+baseball+diamond'>

    # Input interpretation

    base running distance for a home run in baseball

    # Result

    360 feet

    # Unit conversion

    0.06818 miles

    120 yards

    109.7 meters

    0.1097 km (kilometers)

    10973 cm (centimeters)

    # Corresponding quantity

    ![Image](https://public6.wolframalpha.com/files/GIF_1aopnf139nx.gif)

    Light travel time t in vacuum from t = x/c:
     | 366 ns (nanoseconds)

    ![Image](https://public6.wolframalpha.com/files/GIF_1aopptziveu.gif)

    Light travel time t in an optical fiber t = 1.48x/c:
     | 542 ns (nanoseconds)

    ![Image](https://public6.wolframalpha.com/files/GIF_1aopsst9hk3.gif)

    Sound travel time t from t = x/v:
     | 320 ms (milliseconds)
     | (assuming speed of sound ≈ 340 m/s)

    # Comparison as length

     = length of an American football field (including end zones) ( 360 ft )

     ≈ 1.2 × length of an American football field (excluding end zones) ( 100 yd )

     ≈ 1.4 × length of a standard Manhattan city block ( 264 ft )

    </result>

    <result query='time to run 90 meters at 28 mph (average cheetah speed)' 
    url='https://www.wolframalpha.com/input?i=time+to+run+90+meters+at+28+mph+%28average+cheetah+speed%29'>

    No Results Found

    </result>

    <result query='cheetah sprint time for 100 meters' 
    url='https://www.wolframalpha.com/input?i=cheetah+sprint+time+for+100+meters'>

    No Results Found

    </result>

    <result query='time taken by a cheetah to cover 360 feet' 
    url='https://www.wolframalpha.com/input?i=time+taken+by+a+cheetah+to+cover+360+feet'>

    No Results Found

    </result>

    ======

    You can use any Markdown links from these results in your response to show images, formatted expressions, etc. to the user.

    If you use any information from these results, you should cite the relevant URL with a Markdown link in your response.",
        "code":200,
        "success":true,
        "uuid":"${OBJECT_ID}"
    }

</div>

### Request Parameters

<div>

The following parameters can be passed in the body of an API request:

<div class="n-column-table">

<div class="row">

<div class="cell key">

`"context"`

</div>

<div class="cell value">

required

</div>

<div class="cell description">

message to augment with Wolfram\|Alpha knowledge

</div>

</div>

<div class="row">

<div class="cell key">

`"count"`

</div>

<div class="cell value">

default: `5`

</div>

<div class="cell description">

number of related Wolfram\|Alpha results to generate

</div>

</div>

</div>

#### `context` <span class="gray">(required)</span>

<div>

The required parameter `"context"` specifies the message or messages for which additional prompting is generated. `"context"` accepts the following forms:

<div class="n-column-table two-column margin-b-3">

<div class="row">

<div class="cell key">

`"query"`

</div>

<div class="cell value">

plaintext query suitable for an LLM

</div>

</div>

<div class="row">

<div class="cell key">

    {
        "context" : [
            {
                    "role" : "user",
                    "content" : "YOUR PROMPT"
                },
            {
                    "role" : "assistant"
                    "content" : "API RESPONSE"
                },
            {
                    "role" : "user"
                    "content" : "YOUR NEXT PROMPT"
                }
        ]
     }

</div>

<div class="cell value">

a list of JSON message objects

</div>

</div>

</div>

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="c2c/02.txt">

curl -X POST https://services.wolfram.com/api/cag/v1/WolframAlphaContext \\ -H "Content-Type: application/json" \\ -H "Authorization: YOUR-API-KEY" \\ -d '{ "context": "What'\\'s the 123456789th prime?" }'

</div>

    {
        "result":"IMPORTANT: The following information was automatically generated using Wolfram Alpha and should be used to help answer the user's query using factual information.

    ======

    <result query='123456789th prime number' url='https://www.wolframalpha.com/input?i=123456789th+prime+number'>

    # Input

    p_123456789

    # Result

    2543568463

    # Scientific notation

    2.543568463 * 10^9

    # Number line

    ![Number line](https://public6.wolframalpha.com/files/GIF_15vcqcuhd89.gif)

    # Number name

    2 billion 543 million 568 thousand 463

    # Number length

    10 decimal digits

    # Residues modulo small integers

    ![Image](https://public6.wolframalpha.com/files/GIF_15vctx718z0.gif)

    m | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
    2543568463 mod m | 1 | 1 | 3 | 3 | 1 | 2 | 7 | 1

    # Property

    2543568463 is a number that cannot be written as a sum of 3 squares.

    2543568463 is the 123456789th prime number.

    2543568463 is an odd number.

    # Density of primes <= 2543568463

    0.0485368

    # Comparison

    ≈ 0.32 × the number of people alive today (≈ 7.8×10^9)

    # Series representation

    p_123456789 = 2 + sum_(k=2)^floor(2 + 246913578 log(123456789))(1 - floor(π(k)/123456789))

    p_123456789 = 1 + sum_(k=1)^(2^123456789) 
    floor(3^(2/123456789) 13717421^(1/123456789) (1/(1 + π(k)))^(1/123456789))

    p_123456789 = sum_(k=0)^15241578750190521 g(1 - g(-123456789 + sum_(j=0)^k r((g(-1 
    + j)!)^2, j))) for (g(m) = m θ(m) and δ_(0, b) (a - a mod b) + a mod b = r(a, b))

    # Neighboring primes

    p_123456788 = 2543568457 | p_123456790 = 2543568479

    </result>

    ======

    You can use any Markdown links from these results in your response to show images, formatted expressions, etc. to the user.

    If you use any information from these results, you should cite the relevant URL with a Markdown link in your response.",
        "code":200,
        "success":true,
        "uuid":"${OBJECT_ID}"
    }

</div>

#### `count` <span class="gray">(optional)</span>

<div>

Use the optional `"count"` parameter to specify an upper bound on the number of related queries to generate. (The default value of `"count"` is `5`.)

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="c2c/03.txt">

curl -X POST https://services.wolfram.com/api/cag/v1/WolframAlphaContext \\ -H "Content-Type: application/json" \\ -H "Authorization: YOUR-API-KEY" \\ -d '{ "context": "Compare the Eiffel Tower to the pyramids at Giza", "count": "2" }'

</div>

</div>

### Response

<div>

The returned JSON contains the following fields:

- `result` (string) A plaintext summary of Wolfram\|Alpha queries and results, with individual queries and their results delimited between `<result query=XXX>` and `</result>` tag pairs and returned in Markdown
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

</div>

Use of these APIs is subject to the [API Terms of Use](https://products.wolframalpha.com/api/termsofuse) and [Commercial Terms of Use](https://products.wolframalpha.com/api/commercial-termsofuse).

</div>

</div>
