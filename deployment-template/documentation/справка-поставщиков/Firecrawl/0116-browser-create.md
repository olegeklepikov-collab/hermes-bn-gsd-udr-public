> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Firecrawl: browser-create

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


https://docs.firecrawl.dev/api-reference/endpoint/browser-create

> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.firecrawl.dev/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.firecrawl.dev/api-reference/endpoint/browser-create#content-area)

Create an interact session

cURL

```
curl --request POST \
  --url https://api.firecrawl.dev/v2/interact \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "ttl": 300,
  "activityTtl": 1805,
  "streamWebView": true
}
'
```

```
import requests

url = "https://api.firecrawl.dev/v2/interact"

payload = {
    "ttl": 300,
    "activityTtl": 1805,
    "streamWebView": True
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: JSON.stringify({ttl: 300, activityTtl: 1805, streamWebView: true})
};

fetch('https://api.firecrawl.dev/v2/interact', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [\
  CURLOPT_URL => "https://api.firecrawl.dev/v2/interact",\
  CURLOPT_RETURNTRANSFER => true,\
##   CURLOPT_ENCODING => "",\
##   CURLOPT_MAXREDIRS => 10,\
##   CURLOPT_TIMEOUT => 30,\
##   CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,\
##   CURLOPT_CUSTOMREQUEST => "POST",\
  CURLOPT_POSTFIELDS => json_encode([\
    'ttl' => 300,\
    'activityTtl' => 1805,\
    'streamWebView' => true\
  ]),\
##   CURLOPT_HTTPHEADER => [\
    "Authorization: Bearer <token>",\
    "Content-Type: application/json"\
  ],\
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```

```
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.firecrawl.dev/v2/interact"

	payload := strings.NewReader("{\n  \"ttl\": 300,\n  \"activityTtl\": 1805,\n  \"streamWebView\": true\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.post("https://api.firecrawl.dev/v2/interact")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"ttl\": 300,\n  \"activityTtl\": 1805,\n  \"streamWebView\": true\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.firecrawl.dev/v2/interact")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"ttl\": 300,\n  \"activityTtl\": 1805,\n  \"streamWebView\": true\n}"

response = http.request(request)
puts response.read_body
```

200

402

```
{
  "success": true,
  "id": "<string>",
  "cdpUrl": "<string>",
  "liveViewUrl": "<string>",
  "interactiveLiveViewUrl": "<string>",
  "expiresAt": "2023-11-07T05:31:56Z"
}
```

```
{
  "error": "Payment required to access this resource."
}
```

## POST

/

interact

Try it

Create an interact session

cURL

```
curl --request POST \
  --url https://api.firecrawl.dev/v2/interact \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "ttl": 300,
  "activityTtl": 1805,
  "streamWebView": true
}
'
```

```
import requests

url = "https://api.firecrawl.dev/v2/interact"

payload = {
    "ttl": 300,
    "activityTtl": 1805,
    "streamWebView": True
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: JSON.stringify({ttl: 300, activityTtl: 1805, streamWebView: true})
};

fetch('https://api.firecrawl.dev/v2/interact', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [\
  CURLOPT_URL => "https://api.firecrawl.dev/v2/interact",\
  CURLOPT_RETURNTRANSFER => true,\
##   CURLOPT_ENCODING => "",\
##   CURLOPT_MAXREDIRS => 10,\
##   CURLOPT_TIMEOUT => 30,\
##   CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,\
##   CURLOPT_CUSTOMREQUEST => "POST",\
  CURLOPT_POSTFIELDS => json_encode([\
    'ttl' => 300,\
    'activityTtl' => 1805,\
    'streamWebView' => true\
  ]),\
##   CURLOPT_HTTPHEADER => [\
    "Authorization: Bearer <token>",\
    "Content-Type: application/json"\
  ],\
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```

```
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.firecrawl.dev/v2/interact"

	payload := strings.NewReader("{\n  \"ttl\": 300,\n  \"activityTtl\": 1805,\n  \"streamWebView\": true\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.post("https://api.firecrawl.dev/v2/interact")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"ttl\": 300,\n  \"activityTtl\": 1805,\n  \"streamWebView\": true\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.firecrawl.dev/v2/interact")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"ttl\": 300,\n  \"activityTtl\": 1805,\n  \"streamWebView\": true\n}"

response = http.request(request)
puts response.read_body
```

200

402

```
{
  "success": true,
  "id": "<string>",
  "cdpUrl": "<string>",
  "liveViewUrl": "<string>",
  "interactiveLiveViewUrl": "<string>",
  "expiresAt": "2023-11-07T05:31:56Z"
}
```

```
{
  "error": "Payment required to access this resource."
}
```

## [​](https://docs.firecrawl.dev/api-reference/endpoint/browser-create\#headers)  Headers

| Header | Value |
| --- | --- |
| `Authorization` | `Bearer <API_KEY>` |
| `Content-Type` | `application/json` |

## [​](https://docs.firecrawl.dev/api-reference/endpoint/browser-create\#request-body)  Request Body

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `ttl` | number | No | 600 | Total session lifetime in seconds (30-3600) |
| `activityTtl` | number | No | 300 | Seconds of inactivity before session is destroyed (10-3600) |
| `profile` | object | No | — | Enable persistent storage across sessions. See below. |
| `profile.name` | string | Yes\* | — | Name for the profile (1-128 chars). Sessions with the same name share storage. |
| `profile.saveChanges` | boolean | No | `true` | When `true`, browser state is saved back to the profile on close. Set to `false` to load existing data without writing. Only one saver is allowed at a time. |

## [​](https://docs.firecrawl.dev/api-reference/endpoint/browser-create\#response)  Response

| Field | Type | Description |
| --- | --- | --- |
| `success` | boolean | Whether the session was created |
| `id` | string | Unique session identifier |
| `cdpUrl` | string | WebSocket URL for CDP connections |
| `liveViewUrl` | string | URL to watch the session in real time |
| `interactiveLiveViewUrl` | string | URL to interact with the session in real time (click, type, scroll) |
| `expiresAt` | string | When the session will expire based on TTL |

### [​](https://docs.firecrawl.dev/api-reference/endpoint/browser-create\#example-request)  Example Request

```
curl -X POST "https://api.firecrawl.dev/v2/interact" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "ttl": 120
  }'
```

### [​](https://docs.firecrawl.dev/api-reference/endpoint/browser-create\#example-response)  Example Response

```
{
  "success": true,
  "id": "${OBJECT_ID}",
  "cdpUrl": "wss://cdp-proxy.firecrawl.dev/cdp/${OBJECT_ID}",
  "liveViewUrl": "https://liveview.firecrawl.dev/${OBJECT_ID}",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/${OBJECT_ID}?interactive=true"
}
```

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

[​](https://docs.firecrawl.dev/api-reference/endpoint/browser-create#authorization-authorization)

Authorization

string

header

required

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Body

application/json

[​](https://docs.firecrawl.dev/api-reference/endpoint/browser-create#body-ttl)

ttl

integer

default:300

Total time-to-live in seconds for the interact session

Required range: `30 <= x <= 3600`

[​](https://docs.firecrawl.dev/api-reference/endpoint/browser-create#body-activity-ttl)

activityTtl

integer

Time in seconds before the session is destroyed due to inactivity

Required range: `10 <= x <= 3600`

[​](https://docs.firecrawl.dev/api-reference/endpoint/browser-create#body-stream-web-view)

streamWebView

boolean

default:true

Whether to stream a live view of the browser

[​](https://docs.firecrawl.dev/api-reference/endpoint/browser-create#body-profile)

profile

object

Enable persistent storage across interact sessions. Data saved in one session can be loaded in a later session using the same name.

Showchild attributes

#### Response

200

application/json

Interact session created successfully

[​](https://docs.firecrawl.dev/api-reference/endpoint/browser-create#response-success)

success

boolean

[​](https://docs.firecrawl.dev/api-reference/endpoint/browser-create#response-id)

id

string

The unique session identifier

[​](https://docs.firecrawl.dev/api-reference/endpoint/browser-create#response-cdp-url)

cdpUrl

string

WebSocket URL for Chrome DevTools Protocol access

[​](https://docs.firecrawl.dev/api-reference/endpoint/browser-create#response-live-view-url)

liveViewUrl

string

URL to view the interact session in real time

[​](https://docs.firecrawl.dev/api-reference/endpoint/browser-create#response-interactive-live-view-url)

interactiveLiveViewUrl

string

URL to interact with the interact session in real time (click, type, scroll)

[​](https://docs.firecrawl.dev/api-reference/endpoint/browser-create#response-expires-at)

expiresAt

string<date-time>

When the session will expire based on TTL

[Suggest edits](https://github.com/firecrawl/firecrawl-docs/edit/main/api-reference/endpoint/browser-create.mdx) [Raise issue](https://github.com/firecrawl/firecrawl-docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/endpoint/browser-create)
