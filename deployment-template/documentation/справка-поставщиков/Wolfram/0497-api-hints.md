> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Wolfram: api-hints

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


<div class="header">

<div class="inner">

# Wolfram Language Hints API *Reference*

</div>

</div>

<div id="intro" class="section">

<div class="inner">

## Find Wolfram Language code samples relevant to a given query or task

The Wolfram Language Hints API searches Wolfram Language reference materials for code samples relevant to a given input. The response is formatted as text appropriate for use as part of an LLM prompt.

<a href="mailto:partner-program@wolfram.com" class="button" data-walid="WL-Hints-Access">Request API Access</a>

</div>

</div>

<div id="using-the-api" class="section">

<div class="inner">

## Using the API

### Basic Usage

<div>

A basic request to the API takes the following form:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="c2c/01.txt">

curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageHints \\ -H "Content-Type: application/json" \\ -H "Authorization: YOUR-API-KEY" \\ -d '{ "context": "Draw a pentagram" }'

</div>

which yields the following response:

<div>

    {
      "result":"IMPORTANT: Here are some Wolfram documentation snippets that you should use to respond.

    ======

    <result url='https://reference.wolfram.com/language/ref/GraphData#1002612349'>

    # GraphData > Examples > Scope > Detailed 
    Properties > Annotatable Properties Related to Graph Output > 18

    Return the name of the ordinary line graph of the pentagram configuration:

    ```wl
    In[1]:= GraphData["PentagramConfigurationGraph", "OrdinaryLineGraph", "Name"]

    Out[1]= "PetersenGraph"
    ```

    Return the ordinary line graph of the pentagram configuration:

    ```wl
    In[2]:= GraphData["PentagramConfigurationGraph", "OrdinaryLineGraph", "Graph"]

    Out[2]= Image[...]
    ```

    Compute by finding the extraordinary lines of the pentagram configuration:

    ```wl
    In[3]:= config = GraphData["PentagramConfigurationGraph", "Graph", "Labeled"]

    Out[3]= Image[...]

    In[4]:=
    v = GraphEmbedding[config];
    configurationlines = ResourceFunction["FindExtraordinaryLines"][v]

    Out[4]= {}
    ```

    Complement with all possible pairs of points to get the ordinary lines:

    ```wl
    In[5]:= ordinarylines = Complement[Subsets[VertexList[config], 
    {2}], Flatten[Subsets[#, {2}]& /@ configurationlines, 1]]

    Out[5]= {{1, 2}, {1, 3}, {1, 4}, {1, 5}, {1, 6}, {1, 7}, {1, 8}, {1, 9}, {1, 10}, {2, 3}, {2, 4}, 
    {2, 5}, {2, 6}, {2, 7}, {2, 8}, {2, 9}, {2, 10}, {3, 4}, {3, 5}, {3, 6}, {3, 7}, {3, 8}, {3,
    9}, {3, 10}, {4, 5}, {4, 6}, {4, 7}, {4, 8}, {4, 9}, {4, 10}, {5, 6}, {5, 7}, {5, 8}, {5, 9}, 
    {5, 10}, {6, 7}, {6, 8}, {6, 9}, {6, 10}, {7, 8}, {7, 9}, {7, 10}, {8, 9}, {8, 10}, {9, 10}}

    In[6]:= connectedpts = Union@Flatten[ordinarylines];
    ```

    Build the ordinary line graph:

    ```wl
    In[7]:= Graph[connectedpts, UndirectedEdge@@@ordinarylines, VertexCoordinates -> v[[connectedpts]]]

    Out[7]= Image[...]
    ```

    Identify using ``ToEntity`` :

    ```wl
    In[8]:= ToEntity[%]

    Out[8]= Entity["Graph", {"Complete", 10}]
    ```

    </result>

    <result url='https://resources.wolframcloud.com/FunctionRepository/resources/TurtleArt#809943932'>

    # WFR > TurtleArt > Examples > Neat Examples > Neonsqi

    Draw [neonsqi](https://turtleart.org/programming/book1/code.html?6) :

    ```wl
    In[1]:=
    Module[{sqi}, 
        sqi[] := Module[{box1 = 0}, 
        ResourceFunction["TurtleArt"]["SetXY"][0, 0];
        ResourceFunction["TurtleArt"]["SetHeading"][0];
        Do[
        ResourceFunction["TurtleArt"]["Forward"][box1];
        ResourceFunction["TurtleArt"]["Right"][89];
        box1 += 10
        , 
        80
        ]
        ];
        
        ResourceFunction["TurtleArt"]["Clean"][];
        ResourceFunction["TurtleArt"]["SetPensize"][100];
        ResourceFunction["TurtleArt"]["SetColor"][10];
        ResourceFunction["TurtleArt"]["SetShade"][100];
        
        Do[
        sqi[];
        ResourceFunction["TurtleArt"]["SetShade"][ResourceFunction["TurtleArt"]@"Shade" - 8];
        ResourceFunction["TurtleArt"]["SetPensize"][ResourceFunction["TurtleArt"]@"Pensize" - 1]
        , 
        100
        ];
        
        ResourceFunction["TurtleArt"]["Draw"][]
        ]

    Out[1]= !(*GraphicsBox[«7»])
    ```

    </result>

    <result url='https://resources.wolframcloud.com/FunctionRepository/resources/DrawSketch#91293614'>

    # WFR > DrawSketch > Examples > Neat Examples

    Create a function which displays an animation showing the object being drawn from the sequence of pen strokes chosen by the network:

    ```wl
    In[1]:=
    animateSketch[obj_] := DynamicModule[{lines, plotRange}, lines = DeleteCases[drawSketch[obj], {}];
        plotRange = Map[MinMax, 1.05 * {lines[[All, All, 1]], lines[[All, All, 2]]}];
        Animate[Graphics[Line@lines[[1 ;; i]], PlotRange -> plotRange], {i, 1, Length[lines], 1}, AnimationRepetitions -> 1]]

    In[2]:= animateSketch["Bird"]

    Out[2]= Image[...]
    ```

    </result>",
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

query for which to provide context

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

maximum number of results to generate

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
          "role" : "assistant",
            "content" : "API RESPONSE"
        },
        {
          "role" : "user",
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

curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageHints \\ -H "Content-Type: application/json" \\ -H "Authorization: YOUR-API-KEY" \\ -d '{ "context": "What'\\'s the 123456789th prime?" }'

</div>

    {
      "result":"IMPORTANT: Here are some Wolfram documentation snippets that you should use to respond.

    ======

    <result url='https://reference.wolfram.com/language/ref/Prime#25932'>

    # Prime

    Prime[n] gives the n$$^{\\text{th}}$$prime number $$p_n$$.

    ## Details

    * ``Prime`` is also known as prime number sequence.

    * Integer mathematical function, suitable for both symbolic and numerical manipulation.

    * $$p_n$$ is the smallest positive integer greater than $$p_{n-1}$$, which cannot be divided by any integer greater than 1 and smaller than itself. The first prime $$p_1$$ is the integer 2.

    * $$p_n$$ is asymptotically equivalent to $$n \\log (n)$$ as $$n\\to \\infty$$.

    cell image (пример адреса или протокола; задаётся в целевой среде)

    ### Basic Examples

    Compute the $$100^{\\text{th}}$$ prime:

    ```wl\nIn[1]:= Prime[100]

    Out[1]= 541\n```

    </result>

    <result url='https://reference.wolfram.com/language/ref/Prime#877499005'>

    # Prime > Examples > Scope > Numerical Evaluation

    ``Prime`` works over positive integers:

    ```wl\nIn[1]:= Prime[10]

    Out[1]= 29\n```

    </result>

    <result url='https://reference.wolfram.com/language/ref/NextPrime#383220371'>

    # NextPrime > Examples > Properties & Relations > 3

    Compute the $$n^{\\text{th}}$$ prime using ``NextPrime`` :

    ```wl\nIn[1]:= NextPrime[1, 39]

    Out[1]= 167

    In[2]:= Prime[39]

    Out[2]= 167\n```

    </result>",
      "code": 200,
      "success": true,
      "uuid": "${OBJECT_ID}"
    }

</div>

#### `count` <span class="gray">(optional)</span>

<div>

Use the optional `"count"` parameter to specify an upper bound on the number of related queries to generate. (The default value of `"count"` is `5`.)

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="c2c/03.txt">

curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageHints \\ -H "Content-Type: application/json" \\ -H "Authorization: YOUR-API-KEY" \\ -d '{ "context": "Compare the Eiffel Tower to the pyramids at Giza", "count": 2 }'

</div>

### Response

<div>

The returned JSON contains the following fields:

- `result` (string) A collection of Wolfram Language documentation code samples that typically includes related descriptive text and one or more input-output pairs
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

<div id="footer-placeholder">

</div>

<div id="footer">

<div class="footer-buttons">

<div class="flex justify-content-c align-items-c">

<div>

<a href="mailto:partner-program@wolfram.com" class="button">Contact Us</a>

</div>

</div>

</div>

</div>

<div id="_footer-top">

<div>

- Products

- <a href="https://www.wolfram.com/wolfram-one/?source=footer" data-walid="GUIFooter">Wolfram|One</a>

- <a href="https://www.wolfram.com/mathematica/?source=footer" data-walid="GUIFooter">Mathematica</a>

- <a href="https://www.wolfram.com/ai-access/?source=footer" data-walid="GUIFooter">AI Access</a>

- <a href="https://www.wolfram.com/compute-services/?source=footer" data-walid="GUIFooter">Compute Services</a>

- <a href="https://www.wolfram.com/system-modeler/?source=footer" data-walid="GUIFooter">System Modeler</a>

- 

  ------------------------------------------------------------------------

- <a href="https://www.wolfram.com/wolfram-alpha-notebook-edition/?source=footer" data-walid="GUIFooter">Wolfram|Alpha Notebook Edition</a>

- <a href="https://www.wolframalpha.com/pro/?source=footer" data-walid="GUIFooter">Wolfram|Alpha Pro</a>

- <a href="https://www.wolfram.com/products/?source=footer#mobile-apps" data-walid="GUIFooter">Mobile Apps</a>

- 

  ------------------------------------------------------------------------

- <a href="https://www.wolfram.com/engine/?source=footer" data-walid="GUIFooter">Wolfram Engine</a>

- <a href="https://www.wolfram.com/player/?source=footer" data-walid="GUIFooter">Wolfram Player</a>

- 

  ------------------------------------------------------------------------

- <a href="https://www.wolfram.com/group-organization-licensing/?source=footer" data-walid="GUIFooter">Volume &amp; Site Licensing</a>

- <a href="https://www.wolfram.com/server-deployment-options/?source=footer" data-walid="GUIFooter">Server Deployment Options</a>

</div>

<div>

- Consulting
- <a href="https://consulting.wolfram.com/?source=footer" data-walid="GUIFooter">Wolfram Consulting</a>

<!-- -->

- Repositories

- <a href="https://datarepository.wolframcloud.com/?source=footer" data-walid="GUIFooter">Data Repository</a>

- <a href="https://resources.wolframcloud.com/FunctionRepository/?source=footer" data-walid="GUIFooter">Function Repository</a>

- <a href="https://resources.wolframcloud.com/PacletRepository/?source=footer" data-walid="GUIFooter">Community Paclet Repository</a>

- <a href="https://resources.wolframcloud.com/NeuralNetRepository/?source=footer" data-walid="GUIFooter">Neural Net Repository</a>

- <a href="https://resources.wolframcloud.com/PromptRepository/?source=footer" data-walid="GUIFooter">Prompt Repository</a>

- 

  ------------------------------------------------------------------------

- <a href="https://resources.wolframcloud.com/ExampleRepository/?source=footer" data-walid="GUIFooter">Wolfram Language Example Repository</a>

- <a href="https://notebookarchive.org/?source=footer" data-walid="GUIFooter">Notebook Archive</a>

- <a href="https://github.com/wolframresearch/?source=footer" data-walid="GUIFooter" target="_blank">Wolfram GitHub</a>

</div>

<div>

- Learning

- <a href="https://www.wolfram.com/wolfram-u/?source=footer" data-walid="GUIFooter">Wolfram U</a>

- <a href="https://reference.wolfram.com/language/?source=footer" data-walid="GUIFooter">Wolfram Language Documentation</a>

- <a href="https://events.wolfram.com/?source=footer" data-walid="GUIFooter">Webinars &amp; Training</a>

- <a href="https://education.wolfram.com/programs/?source=footer" data-walid="GUIFooter">Educational Programs</a>

- 

  ------------------------------------------------------------------------

- <a href="https://www.wolfram.com/language/elementary-introduction/3rd-ed/?source=footer" data-walid="GUIFooter">Wolfram Language Introduction</a>

- <a href="https://www.wolfram.com/language/fast-introduction-for-programmers/?source=footer" data-walid="GUIFooter">Fast Introduction for Programmers</a>

- <a href="https://www.wolfram.com/language/fast-introduction-for-math-students/?source=footer" data-walid="GUIFooter">Fast Introduction for Math Students</a>

- <a href="https://www.wolfram-media.com/?source=footer" data-walid="GUIFooter">Books</a>

- 

  ------------------------------------------------------------------------

- <a href="https://community.wolfram.com/?source=footer" data-walid="GUIFooter">Wolfram Community</a>

- <a href="https://blog.wolfram.com/?source=footer" data-walid="GUIFooter">Wolfram Blog</a>

</div>

<div>

- Public Resources

- <a href="https://www.wolframalpha.com/?source=footer" data-walid="GUIFooter">Wolfram|Alpha</a>

- <a href="https://www.wolframalpha.com/pro/problem-generator/?source=footer" data-walid="GUIFooter">Wolfram Problem Generator</a>

- <a href="https://challenges.wolframcloud.com/?source=footer" data-walid="GUIFooter">Wolfram Challenges</a>

- 

  ------------------------------------------------------------------------

- <a href="https://www.computerbasedmath.org/?source=footer" data-walid="GUIFooter">Computer-Based Math</a>

- <a href="https://www.wolfram.com/resources/computational-thinking/?source=footer" data-walid="GUIFooter">Computational Thinking</a>

- <a href="https://www.computationinitiative.org/computational-adventures/?source=footer" data-walid="GUIFooter">Computational Adventures</a>

- 

  ------------------------------------------------------------------------

- <a href="https://demonstrations.wolfram.com/?source=footer" data-walid="GUIFooter">Demonstrations Project</a>

- <a href="https://datadrop.wolframcloud.com/?source=footer" data-walid="GUIFooter">Wolfram Data Drop</a>

- <a href="https://mathworld.wolfram.com/?source=footer" data-walid="GUIFooter" target="_blank">MathWorld</a>

- <a href="https://www.wolframscience.com/?source=footer" data-walid="GUIFooter">Wolfram Science</a>

- <a href="https://www.wolfram-media.com/?source=footer" data-walid="GUIFooter">Wolfram Media Publishing</a>

</div>

<div>

- Customer Resources

- <a href="https://www.wolfram.com/get-products-services/?source=footer" data-walid="GUIFooter">Store</a>

- <a href="https://www.wolfram.com/download-center/?source=footer" data-walid="GUIFooter">Product Downloads</a>

- <a href="https://user.wolfram.com/portal/?source=footer" data-walid="GUIFooter">User Portal</a>

- <a href="https://account.wolfram.com/?source=footer" data-walid="GUIFooter">Your Account</a>

- <a href="https://www.wolfram.com/siteinfo/?source=footer" data-walid="GUIFooter">Organization Access</a>

- 

  ------------------------------------------------------------------------

- <a href="https://support.wolfram.com/?source=footer" data-walid="GUIFooter">Support FAQ</a>

- <a href="https://www.wolfram.com/support/contact/?source=footer" data-walid="GUIFooter">Contact Support</a>

<!-- -->

- Company
- <a href="https://www.wolfram.com/company/?source=footer" data-walid="GUIFooter">About Wolfram</a>
- <a href="https://www.wolfram.com/company/careers/?source=footer" data-walid="GUIFooter">Careers</a>
- <a href="https://www.wolfram.com/company/contact/?source=footer" data-walid="GUIFooter">Contact</a>
- <a href="https://company.wolfram.com/events/?source=footer" data-walid="GUIFooter">Events</a>

</div>

<div id="_footer-mobile" class="_page-width padding-bt-2 text-align-c hide show__900">

<div id="_footer-mobile-community" class="flex gap-3 justify-content-c">

<a href="https://community.wolfram.com/?source=footer" data-walid="GUIFooter">Wolfram Community</a> <a href="https://blog.wolfram.com/?source=footer" data-walid="GUIFooter">Wolfram Blog</a>

</div>

<div id="_footer-mobile-social" class="flex justify-content-c margin-1">

<a href="https://www.facebook.com/wolframresearch?source=footer" data-walid="GUIFooter" target="_blank"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci1mYWNlYm9vayI+PHVzZSBocmVmPSIjX2Zvb3Rlci1mYWNlYm9vayIgLz48dGl0bGU+RmFjZWJvb2s8L3RpdGxlPjwvc3ZnPg==" class="_icon _footer-facebook" /></a> <a href="https://x.com/WolframResearch?source=footer" data-walid="GUIFooter" target="_blank"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci10d2l0dGVyIj48dXNlIGhyZWY9IiNfZm9vdGVyLXR3aXR0ZXIiIC8+PHRpdGxlPlg8L3RpdGxlPjwvc3ZnPg==" class="_icon _footer-twitter" /></a> <a href="https://twitch.tv/wolfram?source=footer" data-walid="GUIFooter" target="_blank"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci10d2l0Y2giPjx1c2UgaHJlZj0iI19mb290ZXItdHdpdGNoIiAvPjx0aXRsZT5Ud2l0Y2g8L3RpdGxlPjwvc3ZnPg==" class="_icon _footer-twitch" /></a> <a href="https://www.linkedin.com/company/wolfram-research/?source=footer" data-walid="GUIFooter" target="_blank"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci1saW5rZWRpbiI+PHVzZSBocmVmPSIjX2Zvb3Rlci1saW5rZWRpbiIgLz48dGl0bGU+TGlua2VkSW48L3RpdGxlPjwvc3ZnPg==" class="_icon _footer-linkedin" /></a> <a href="https://www.youtube.com/user/wolframresearch?source=footer" data-walid="GUIFooter" target="_blank"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci15b3V0dWJlIj48dXNlIGhyZWY9IiNfZm9vdGVyLXlvdXR1YmUiIC8+PHRpdGxlPllvdVR1YmU8L3RpdGxlPjwvc3ZnPg==" class="_icon _footer-youtube" /></a> <a href="https://www.wolfram.com/?source=footer" data-walid="GUIFooter"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci1zcGlrZXkiPjx1c2UgaHJlZj0iI19mb290ZXItc3Bpa2V5IiAvPjx0aXRsZT5Xb2xmcmFtPC90aXRsZT48L3N2Zz4=" class="_icon _footer-spikey" /></a>

</div>

<div id="_footer-mobile-legal">

<a href="https://www.wolfram.com/legal/?source=footer" data-walid="GUIFooter">Legal</a> & <a href="https://www.wolfram.com/legal/privacy/wolfram/?source=footer" data-walid="GUIFooter">Privacy Policy</a>\
<a href="https://www.wolframalpha.com/?source=footer" data-walid="GUIFooter">WolframAlpha.com</a> <span class="_separator">\|</span> <a href="https://www.wolframcloud.com/?source=footer" data-walid="GUIFooter">WolframCloud.com</a>

</div>

</div>

</div>

<div id="_footer-bottom" class="_page-width-no-padding">

<div id="_footer-bottom-grid">

<div id="_footer-social">

<div class="flex hide__900">

<a href="https://www.facebook.com/wolframresearch?source=footer" data-walid="GUIFooter" target="_blank"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci1mYWNlYm9vayI+PHVzZSBocmVmPSIjX2Zvb3Rlci1mYWNlYm9vayIgLz48dGl0bGU+RmFjZWJvb2s8L3RpdGxlPjwvc3ZnPg==" class="_icon _footer-facebook" /></a> <a href="https://x.com/WolframResearch?source=footer" data-walid="GUIFooter" target="_blank"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci10d2l0dGVyIj48dXNlIGhyZWY9IiNfZm9vdGVyLXR3aXR0ZXIiIC8+PHRpdGxlPlg8L3RpdGxlPjwvc3ZnPg==" class="_icon _footer-twitter" /></a> <a href="https://twitch.tv/wolfram?source=footer" data-walid="GUIFooter" target="_blank"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci10d2l0Y2giPjx1c2UgaHJlZj0iI19mb290ZXItdHdpdGNoIiAvPjx0aXRsZT5Ud2l0Y2g8L3RpdGxlPjwvc3ZnPg==" class="_icon _footer-twitch" /></a> <a href="https://www.linkedin.com/company/wolfram-research/?source=footer" data-walid="GUIFooter" target="_blank"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci1saW5rZWRpbiI+PHVzZSBocmVmPSIjX2Zvb3Rlci1saW5rZWRpbiIgLz48dGl0bGU+TGlua2VkSW48L3RpdGxlPjwvc3ZnPg==" class="_icon _footer-linkedin" /></a> <a href="https://www.youtube.com/user/wolframresearch?source=footer" data-walid="GUIFooter" target="_blank"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci15b3V0dWJlIj48dXNlIGhyZWY9IiNfZm9vdGVyLXlvdXR1YmUiIC8+PHRpdGxlPllvdVR1YmU8L3RpdGxlPjwvc3ZnPg==" class="_icon _footer-youtube" /></a> <a href="https://www.wolfram.com/?source=footer" data-walid="GUIFooter"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci1zcGlrZXkiPjx1c2UgaHJlZj0iI19mb290ZXItc3Bpa2V5IiAvPjx0aXRsZT5Xb2xmcmFtPC90aXRsZT48L3N2Zz4=" class="_icon _footer-spikey" /></a>

</div>

<div class="hide show__900">

© <span id="_footer-year">2026</span> <a href="https://www.wolfram.com/?source=footer" data-walid="GUIFooter">Wolfram</a>

</div>

</div>

<div id="_footer-language" class="text-align-r">

<div class="display-ib hide__900">

© <span id="_footer-year">2026</span> <a href="https://www.wolfram.com/?source=footer" data-walid="GUIFooter">Wolfram</a> <span class="_separator">\|</span> <a href="https://www.wolfram.com/legal/?source=footer" data-walid="GUIFooter">Legal</a> & <a href="https://www.wolfram.com/legal/privacy/wolfram/?source=footer" data-walid="GUIFooter">Privacy Policy</a> <span class="_separator">\|</span>

</div>

<div class="display-ib">

<div id="_language-picker">

<div class="_current-language">

<img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci1nbG9iZSI+PHVzZSBocmVmPSIjX2Zvb3Rlci1nbG9iZSIgLz48L3N2Zz4=" class="_icon _footer-globe" /> English

</div>

<div class="_dropdown">

- <a href="/apis/documentation/cag/wolfram-language-hints-api/index.php.en?source=footer" data-walid="GUIFooter"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iX2ljb24gX2Zvb3Rlci1jaGVjayI+PHVzZSBocmVmPSIjX2Zvb3Rlci1jaGVjayIgLz48L3N2Zz4=" class="_icon _footer-check" />English</a>

</div>

</div>

</div>

</div>

</div>

</div>

<div id="IPstripe-wrap">

</div>

</div>

</div>

</div>

</div>
