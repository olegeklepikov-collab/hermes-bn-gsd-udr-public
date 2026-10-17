> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Wolfram: api-agent-one

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


<div class="header">

<div class="inner">

# Wolfram Agent One API *Reference*

</div>

</div>

<div id="intro" class="section">

<div class="inner">

## All-in-one LLM + CAG universal agent

Agent One combines LLM responses with [Wolfram Foundation Tool computation and knowledge](https://www.wolfram.com/artificial-intelligence/foundation-tool/). Each request returns both the LLM-generated response and the computations that inform the response, giving an auditable record rather than a black-box result.

Designed as a drop-in endpoint that produces verifiable output.

The Wolfram Agent One API is compatible with the OpenAI Chat Completions API specification, making it easy to integrate into any LLM-based system.

<a href="mailto:partner-program@wolfram.com" class="button" data-walid="Agent-One-Access">Request API Access</a> <a href="https://agent-one-sandbox.wolfram.com/" class="button" data-walid="Agent-One-Demo">Demo Sandbox</a>

</div>

</div>

<div id="using-the-api" class="section">

<div class="inner">

## Using the API

### Basic Usage

<div>

A basic request to the API takes the following form:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="c2c/01.txt">

curl -X POST https://services.wolfram.com/api/agent-one/v1/chat/completions \\ -H "Content-Type: application/json" \\ -H "Authorization: YOUR-API-KEY" \\ -d '{ "messages":\[ { "role": "user", "content": "Hey there" } \] }'

</div>

which yields the following response:

    {
      "code":200,
      "success":true,
      "created":1764643853,
      "model":"AgentOne",
      "uuid":"${OBJECT_ID}",
      "choices":[
        {
          "finish_reason":"stop",
          "index":0,
          "message":{
            "role":"assistant",
            "annotations":[],
            "content":" <think>


    Considering Wolfram Language sources...Skipped Wolfram Language sources.
    Considering Wolfram|Alpha results...Skipped Wolfram|Alpha results.</think>Hello! How can I assist you today?"
          }
        }
      ],
      "object":"chat.completion"
    }

</div>

### Request Parameters

<div>

The following parameters can be passed in the body of an API request:

<div class="n-column-table">

<div class="row">

<div class="cell key">

`"messages"`

</div>

<div class="cell value">

required

</div>

<div class="cell description">

JSON containing a chat history

</div>

</div>

<div class="row">

<div class="cell key">

`"stream"`

</div>

<div class="cell value">

default: `false`

</div>

<div class="cell description">

whether to stream results

</div>

</div>

</div>

#### `messages` <span class="gray">(required)</span>

<div>

The required parameter `"messages"` should consist of a list of `"messages"` formatted as JSON. Each `"message"` contains a `"role"` and a `"content"` field. The `"role"` field may be either `"user"` or `"assistant"`. The `"content"` field can be any string. For example:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="c2c/02.txt">

curl -X POST https://services.wolfram.com/api/agent-one/v1/chat/completions \\ -H "Content-Type: application/json" \\ -H "Authorization: YOUR-API-KEY" \\ -d '{ "messages":\[ { "role": "user", "content": "reverse the letters in my next input and return the result only." }, { "role": "user", "content": "supercalifragilisticexpialidocious" } \] }'

</div>

results in:

    {
      "code":200,
      "success":true,
      "created":1764691103,
      "model":"AgentOne",
      "uuid":"${OBJECT_ID}",
      "choices":[
        {
          "finish_reason":"stop",
          "index":0,
          "message":{
            "role":"assistant",
            "annotations":[
              {
                "wolfram_tool_request":{
                  "RequestID":"__wl__None",
                  "RequestString":"/wl
                  StringReverse["supercalifragilisticexpialidocious"]",
                  "LLMPacletVersion":"2.2.4",
                  "ParameterValues":{
                   "code":"StringReverse["supercalifragilisticexpialidocious"]"
                  },
                  "Name":"wolfram_language_evaluator"
                },
                "type":"wolfram_tool_request"
              },
              {
                "wolfram_tool_response":{
                  "RequestID":"9sytu",
                  "string":"Out[1]= "suoicodilaipxecitsiligarfilacrepus"",
                  "Output":{
                    "Packets":[],
                    "String":"Out[1]= "suoicodilaipxecitsiligarfilacrepus"",
                    "Result":"__wl__HoldCompleteForm["suoicodilaipxecitsiligarfilacrepus"]"
                  },
                  "Request":{
                    "RequestID":"9sytu",
                    "RequestString":"/wl
                    StringReverse["supercalifragilisticexpialidocious"]",
                    "LLMPacletVersion":"2.2.4",
                    "ParameterValues":{
                      "code":"StringReverse["supercalifragilisticexpialidocious"]"
                    },
                    "Name":"wolfram_language_evaluator"
                  },
                  "LLMPacletVersion":"2.2.4",
                  "InterpretedParameterValues":{
                    "code":"StringReverse["supercalifragilisticexpialidocious"]"
                  },
                  "ResponseString":"Out[1]= "suoicodilaipxecitsiligarfilacrepus"",
                  "Tool":"wolfram_language_evaluator"
                },
                "type":"wolfram_tool_response"
              }
            ],
            "content":"<think>


    Considering Wolfram Language sources...
    https://reference.wolfram.com/language/ref/StringReverse#988
    https://reference.wolfram.com/language/ref/StringReverse#5240
    https://reference.wolfram.com/language/ref/StringReverse#231862319

    Considering Wolfram|Alpha results...
    Skipped Wolfram|Alpha results."</think>
    [![Wolfram Language 
    Evaluator](https://wolfr.am/1yhTgAPyp)](https://www.wolframcloud.com/obj/cag-admin/CAG/api/1.0/
    WolframLanguageEvaluatorResults?w=OEM6eJwNyzEKgDAMRmHQm4irkyfwCmYUhxJj%2BaGYkrTi8c36%2
    BN42LDTgoZWa4cm7vGIux%2BS9inEquC1lFHgDy1cR5VKGdp%2FOhUbtjebACtYLJaF%2BwmgeR052R2GTGvgH3dEnfg%3D%3D)


    "
          }
        }
      ],
      "object":"chat.completion"
    }

</div>

#### `stream` <span class="gray">(optional)</span>

<div>

By default, when you make a request to the Agent One API, it generates the entire output before sending it back in a single HTTP response. When generating long outputs, waiting for a response can take time. Streaming responses lets you start printing or processing the beginning of the model's output while it continues generating the full response. To stream completions, set the `"stream"` parameter to `true`:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="c2c/03.txt">

curl -X POST https://services.wolfram.com/api/agent-one/v1/chat/completions \\ -H "Content-Type: application/json" \\ -H "Authorization: YOUR-API-KEY" \\ -d '{ "messages":\[ { "role": "user", "content": "Show me a graph comparing the length of the genomes for humans, horses and dogs." } \], "stream": true }'

</div>

which gives:

``` custom-code-block-01

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692756,choices:[{index:0,delta:{role:assistant,content:<think>,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692760,choices:[{index:0,delta:{role:assistant,content:Considering Wolfram Language sources...,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692767,choices:[{index:0,delta:{role:assistant,content:https://resources.wolframcloud.com/FunctionRepository/resources/SpeciesGenomeSummary#309514857 https://reference.wolfram.com/language/ref/GenomeData#437251972 https://reference.wolfram.com/language/ref/GenomeData#14104375 https://reference.wolfram.com/language/ref/Histogram#462649515 https://reference.wolfram.com/language/ref/GenomeData#21466432,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692767,choices:[{index:0,delta:{role:assistant,content:Considering Wolfram|Alpha results...,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692770,choices:[{index:0,delta:{role:assistant,content:https://www.wolframalpha.com/input?i=genome+length+of+humans https://www.wolframalpha.com/input?i=genome+length+of+horses https://www.wolframalpha.com/input?i=genome+length+of+dogs https://www.wolframalpha.com/input?i=comparison+of+genome+lengths+for+human%2C+horse%2C+dog,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692772,choices:[{index:0,delta:{role:assistant,content:</think>,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692774,choices:[{index:0,delta:{role:assistant,content:,refusal:null,annotations:[{type:wolfram_tool_request,wolfram_tool_request:{Name:wolfram_language_evaluator,ParameterValues:{code:BarChart[{3.082, 2.367, 2.445}, ChartLabels -> {Human , Horse , Dog }, ChartStyle -> Pastel , AxesLabel -> {None, Genome Length (Gbp)},  PlotLabel -> Comparison of Genome Lengths ]},RequestString:/wl BarChart[{3.082, 2.367, 2.445}, ChartLabels -> {Human , Horse , Dog }, ChartStyle -> Pastel , AxesLabel -> {None, Genome Length (Gbp)}, PlotLabel -> Comparison of Genome Lengths ],RequestID:__wl__None,LLMPacletVersion:2.2.4}}]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692784,choices:[{index:0,delta:{role:assistant,content:[![Wolfram Language Evaluator](https://wolfr.am/1yhTgAPyp)](https://www.wolframcloud.com/obj/cag-admin/CAG/api/1.0/WolframLanguageEvaluatorResults?w=OEM6eJxVjNFqwjAYhZm78ymyXCk0rWvqUncxcA50IFPopXiRxr%2BtI8lfmpRuyF5tzzbbC2FX58D5zrccsWx0ttnv3atsVpVs%2FOHCw1kaByQO%2BZPoI0nmP8GYDOtW5qAdYS%2FkQjetkZYGhG6wcdCXNyzpDc38t4aepHvpPGh6HZZf4AbFYPhAC9fXGiwaIFuwpa%2FIZJ3X08Gy1%2BhvMF2hqWVzdmgJFuTfx9Ejy%2B6x9dnu4fBuZAnHSeV97Z6jqOu6sENdNNIoje0pVGgizD%2BjeQqCC3hkCoRgySzlbAELxXghU17EuZL8NP0DUzdYRQ%3D%3D),refusal:null,annotations:[{type:wolfram_tool_response,wolfram_tool_response:{Request:{Name:wolfram_language_evaluator,ParameterValues:{code:BarChart[{3.082, 2.367, 2.445},  ChartLabels -> {Human , Horse , Dog },  ChartStyle -> Pastel ,   AxesLabel -> {None, Genome Length (Gbp)},  PlotLabel -> Comparison of Genome Lengths ]},RequestString:/wl   BarChart[{3.082, 2.367, 2.445},  ChartLabels -> {Human , Horse , Dog },  ChartStyle -> Pastel ,  AxesLabel -> {None, Genome Length (Gbp)},  PlotLabel -> Comparison of Genome Lengths ],RequestID:2wrsg,LLMPacletVersion:2.2.4},Tool:wolfram_language_evaluator,InterpretedParameterValues:{code:BarChart[{3.082, 2.367, 2.445},  ChartLabels -> {Human , Horse , Dog },  ChartStyle -> Pastel ,  AxesLabel -> {None, Genome Length (Gbp)},PlotLabel -> Comparison of Genome Lengths ]},Output:{String:Out[1]= ![Image](https://www.wolframcloud.com/obj/${OBJECT_ID}),Result:__wl__HoldCompleteForm[Graphics[{{Opacity[0], Point[{{-0.4116533139111435, 0.}, {4.35360524399126, 0.}}]}, {{}, {Directive[RGBColor[1., 0.78, 0.2], EdgeForm[Directive[Thickness[Small], Opacity[0.6789999999999999], GrayLevel[0]]]], {{Directive[EdgeForm[Directive[Thickness[Small], Opacity[0.6789999999999999], GrayLevel[0]]], RGBColor[0.761959, 0.470832, 0.940597]], Tooltip[StatusArea[Charting`DelayedMouseEffect[Rectangle[{0.5487982520029133, 0.}, {1.4512017479970867, 3.082}, RoundingRadius  -> 0], {Style , EdgeForm[{GrayLevel[0.5], AbsoluteThickness[1.5], Opacity[0.66]}]}], 3.082], Style[3.082, {}]]}, {Directive[EdgeForm[Directive[Thickness[Small], Opacity[0.6789999999999999], GrayLevel[0]]], RGBColor[0.9584254999999999, 0.877884, 0.5906629999999999]], Tooltip[StatusArea[Charting`DelayedMouseEffect[Rectangle[{1.5487982520029133, 0.}, {2.4512017479970867, 2.367}, RoundingRadius  -> 0], {Style , EdgeForm[{GrayLevel[0.5], AbsoluteThickness[1.5], Opacity[0.66]}]}], 2.367], Style[2.367, {}]]}, {Directive[EdgeForm[Directive[Thickness[Small], Opacity[0.6789999999999999], GrayLevel[0]]], RGBColor[0.431296, 0.709773, 0.927077]], Tooltip[StatusArea[Charting`DelayedMouseEffect[Rectangle[{2.5487982520029133, 0.}, {3.4512017479970867, 2.445}, RoundingRadius  -> 0], {Style , EdgeForm[{GrayLevel[0.5], AbsoluteThickness[1.5], Opacity[0.66]}]}], 2.445], Style[2.445, {}]]}}}, {}, {}}, {}, {}, {}, {}, {Style[{Antialiasing -> False, {Directive[Thickness[Tiny]], {Line[{{-0.4116533139111435, 0.}, {4.430862345229425, 0.}}]}, Style[{}, GraphicsLabel ]}, Style[{{Directive[Thickness[Tiny]], Line[{{0.5487982520029133, 0.}, Offset[{-1.102182119232618*^-15, -6.}, {0.5487982520029133, 0.}]}], Line[{{3.4512017479970867, 0.}, Offset[{-1.102182119232618*^-15, -6.}, {3.4512017479970867, 0.}]}], {{}, {}, {}, {Line[{{1.4512017479970867, 0.}, Offset[{-7.347880794884119*^-16, -4.}, {1.4512017479970867, 0.}]}], Line[{{1.5487982520029133, 0.}, Offset[{-7.347880794884119*^-16, -4.}, {1.5487982520029133, 0.}]}], Line[{{2.4512017479970867, 0.}, Offset[{-7.347880794884119*^-16, -4.}, {2.4512017479970867, 0.}]}], Line[{{2.5487982520029133, 0.}, Offset[{-7.347880794884119*^-16, -4.}, {2.5487982520029133, 0.}]}]}, {}}}, Style[{Directive[Thickness[Tiny]], Directive[Thickness[Tiny]], Style[{Text[Human , Offset[{0, -2}, {1., 0.}], {0, 1}, {1, 0}], Text[Horse , Offset[{0, -2}, {2., 0.}], {0, 1}, {1, 0}], Text[Dog , Offset[{0, -2}, {3., 0.}], {0, 1}, {1, 0}]}, {}]}, GraphicsLabel ]}, GraphicsTicks ]}, GraphicsAxes ]}}, {DisplayFunction -> Identity, PlotInteractivity :> $PlotInteractivity, DefaultBaseStyle -> {PlotGraphics , Graphics }, AspectRatio -> GoldenRatio^(-1), Axes -> {False, True}, AxesLabel -> {None, HoldForm[Genome Length (Gbp)]}, AxesOrigin -> {-0.4116533139111435, 0.}, CoordinatesToolOptions -> {DisplayFunction  -> ({Identity[#1[[1]]], Identity[#1[[2]]]} & ), CopiedValueFunction  -> ({Identity[#1[[1]]], Identity[#1[[2]]]} & )}, FrameLabel -> {{None, None}, {None, None}}, FrameTicks -> {{Automatic, Automatic}, {Automatic, Automatic}}, GridLines -> {None, None}, GridLinesStyle -> Directive[GrayLevel[0.5, 0.4]], PlotLabel -> Comparison of Genome Lengths , PlotRange -> {{All, All}, {All, All}}, PlotRangePadding -> {{Scaled[0.02], Scaled[0.02]}, {Scaled[0.02], Scaled[0.05]}}, Ticks -> {None, Automatic}}]],Packets:[]},ResponseString:Out[1]= ![Image](https://www.wolframcloud.com/obj/${OBJECT_ID}),LLMPacletVersion:2.2.4,RequestID:2wrsg,string:Out[1]= ![Image](https://www.wolframcloud.com/obj/${OBJECT_ID})}}]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692794,choices:[{index:0,delta:{role:assistant,content:H,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692794,choices:[{index:0,delta:{role:assistant,content:ere's a b,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692794,choices:[{index:0,delta:{role:assistant,content:ar c,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692794,choices:[{index:0,delta:{role:assistant,content:har,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692794,choices:[{index:0,delta:{role:assistant,content:t com,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:paring the,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content: ge,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:nom,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:e ,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:lengt,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:h,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:s of humans, horses, and dogs:\n\n![Comparis,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:on of Genome,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content: Length,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:s](https://www.wolf,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:ra,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:mclo,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:ud.com/ob,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:j/58e737,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:e1-,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:ce77-4083-9,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:e9c,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:-3fa83f2bc,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:a3,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:d)\n\nAs,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content: s,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:hown ,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:in the chart,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content:,,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692795,choices:[{index:0,delta:{role:assistant,content: humans ha,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692796,choices:[{index:0,delta:{role:assistant,content:ve the largest genome with approximately 3.082 gigabase pairs (Gbp), followed by dogs with 2.445 Gbp, and horses with 2.367 Gbp.  ---  #### Wolfram Sources  * Wolfram\|Alpha:  [[1]](https://www.wolframalpha.com/input?i=genome+length+of+humans)  [[2]](https://www.wolframalpha.com/input?i=genome+length+of+horses)  [[3]](https://www.wolframalpha.com/input?i=genome+length+of+dogs)  [[4]](https://www.wolframalpha.com/input?i=comparison+of+genome+lengths+for+human%2C+horse%2C+dog)  [[5]](https://www.wolframalpha.com/input?i=compare+genome+lengths+of+human+horse+and+dog),refusal:null,annotations:[{type:sources,sources:[{ShortID:WA-1,Type:WolframAlpha,URI:https://www.wolframalpha.com/input?i=genome+length+of+humans},{ShortID:WA-2,Type:WolframAlpha,URI:https://www.wolframalpha.com/input?i=genome+length+of+horses},{ShortID:WA-3,Type:WolframAlpha,URI:https://www.wolframalpha.com/input?i=genome+length+of+dogs},{ShortID:WA-4,Type:WolframAlpha,URI:https://www.wolframalpha.com/input?i=comparison+of+genome+lengths+for+human%2C+horse%2C+dog},{ShortID:WA-5,Type:WolframAlpha,URI:https://www.wolframalpha.com/input?i=compare+genome+lengths+of+human+horse+and+dog}]}]},finish_reason:null}],usage:null}

data:{uuid:${OBJECT_ID},object:chat.completion.chunk,created:1764692796,choices:[{index:0,delta:{role:assistant,content:,refusal:null,annotations:[]},finish_reason:null}],usage:null}

data:[DONE]
```

### Managing Conversations

<div>

By using roles within the "`messages`" parameter, a multi-turn conversation can be carried out:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="c2c/04.txt">

curl -X POST https://services.wolfram.com/api/agent-one/v1/chat/completions \\ -H "Content-Type: application/json" \\ -H "Authorization: YOUR-API-KEY" \\ -d '{ "messages":\[ { "role":"user", "content":"knock knock." }, { "role":"assistant", "content":"Who is there?" }, { "role":"user", "content":"Orange" } \] }'

</div>

which yields the response:

    {
      "code":200,
      "success":true,
      "created":1764644221,
      "model":"AgentOne",
      "uuid":"${OBJECT_ID}",
      "choices":[
        {
          "finish_reason":"stop",
          "index":0,
          "message":{
            "role":"assistant",
            "annotations":[],
            "content":"<think>


    Considering Wolfram Language sources...Skipped Wolfram Language sources.

    Considering Wolfram|Alpha results...Skipped Wolfram|Alpha results.</think>Orange who?"
          }
        }
      ],
      "object":"chat.completion"
    }

</div>

### Response

<div>

The returned JSON contains the following fields:

`code` (integer) API status code (e.g. `200`, `400`, `403`, `501`, ...)

`success` (Boolean) `true` or `false` depending on whether the request completed successfully

`created` (integer) The Unix timestamp (in seconds) of when the chat completion was created

`model` (string) Indicates that the model used was `"AgentOne"`

`uuid` (string) A unique ID labeling the response

`choices` (JSON) A list of chat completion choices

`object` (string) The object type, which is always `"chat.completion"`

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

</div>

Use of these APIs is subject to the [API Terms of Use](https://products.wolframalpha.com/api/termsofuse) and [Commercial Terms of Use](https://products.wolframalpha.com/api/commercial-termsofuse).

</div>

</div>
