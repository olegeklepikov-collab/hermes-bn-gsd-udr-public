> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Wolfram: api-hints

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


Wolfram Language Hints API: Reference
## WOLFRAM
Products
Wolfram|One
The definitive Wolfram Language and notebook experience
Mathematica
The original technical computing environment
System Modeler
Multidomain modeling and simulation of complex systems
Compute Services
Use with Mathematica and Wolfram|One
AI Access
Use with Mathematica and Wolfram|One
Finance Platform
Wolfram|Alpha Notebook Edition
Application Server
Enterprise Private Cloud
Wolfram Engine
Wolfram Player
Wolfram Cloud App
Wolfram Player App
More mobile apps
Wolfram|Alpha
Wolfram|Alpha Website
Wolfram|Alpha APIs
AI Products
Wolfram AI Ecosystem
Wolfram Foundation Tool
Wolfram Cloud MCP
Wolfram Local MCP
Agent One API
CAG Component APIs
Core Technologies of Wolfram Products
Wolfram Language
Computable Data
Wolfram Notebooks
Linguistic Understanding
Additional Deployment Options
Wolfram Cloud
Wolfram Web Engine
wolframscript
WSTPServer
Group & Organizational Licensing
All Products
Consulting & Solutions
We deliver solutions for the AI era—combining symbolic computation, data-driven insights and deep technical expertise
Wolfram Consulting
Data Science, Finance & Business
Artificial Intelligence
Data Science
Healthcare
Real Estate
Engineering
Civil Engineering
Automotive Engineering
Sustainable Energy
Science & Technology
AgTech
Biosciences
Environmental Science
Food Science
Quantum Computation
Social and Behavioral Sciences
More Wolfram Solutions
Technology for Education
Research Universities
Colleges & Teaching Universities
High Schools
Resources for Students
Education Initiatives
Next-Gen EdTech
Computer-Based Math
More Solutions for Education
Contact Us
Learning
& Support
Get Started
Wolfram Language Introduction
Fast Intro for Programmers
Fast Intro for Math Students
Wolfram Language Documentation
More Learning
Highlighted Core Areas
Demonstrations
YouTube
Daily Study Groups
Wolfram Schools and Programs
Books
Grow Your Skills
Wolfram U
Courses in computing, science, life and more
Community
Learn, solve problems and share ideas.
Blog
News, views and insights from Wolfram
Resources for
Software Developers
Tech Support
Contact Us
Support FAQs
Support FAQs
Contact Us
Company
About Wolfram
Career Center
All Sites & Resources
Connect & Follow
Contact Us
Work with Us
Student Ambassador Initiative
Wolfram for Startups
Student Opportunities
Jobs Using Wolfram Language
Educational Programs for Adults
Summer School
Winter School
Educational Programs for Youth
Middle School Camp
High School Research Program
Computational Adventures
Read
Stephen Wolfram's Writings
Wolfram Blog
Wolfram Tech | Books
Wolfram Media
Complex Systems
Educational Resources
Wolfram MathWorld
Wolfram in STEM
Wolfram Challenges
Wolfram Problem Generator
Wolfram Initiatives
Wolfram Science
Wolfram Foundation
History of Mathematics Project
Events
Stephen Wolfram Livestreams
Online & In-Person Events
Contact Us
Connect & Follow
For AIs
Wolfram Cloud
Your Account
Your Account
User Portal
Wolfram Cloud
Search
Close
Navigation Menu
Products
Wolfram|One
Mathematica
System Modeler
Compute Services
Use with Mathematica and Wolfram|One
AI Access
Use with Mathematica and Wolfram|One
Finance Platform
Wolfram|Alpha Notebook Edition
Application Server
Enterprise Private Cloud
Wolfram Engine
Wolfram Player
Wolfram Cloud App
Wolfram Player App
More mobile apps
Wolfram|Alpha
Wolfram|Alpha Website
Wolfram|Alpha APIs
AI Products
Wolfram AI Ecosystem
Wolfram Foundation Tool
Wolfram Cloud MCP
Wolfram Local MCP
Agent One API
CAG Component APIs
Core Technologies
Wolfram Language
Computable Data
Wolfram Notebooks
Linguistic Understanding
Additional Deployment Options
Wolfram Cloud
Wolfram Web Engine
wolframscript
WSTPServer
Group &
Organizational Licensing
All Products
Consulting & Solutions
Wolfram Consulting
Data Science, Finance & Business
Artificial Intelligence
Data Science
Healthcare
Real Estate
Engineering
Civil Engineering
Automotive Engineering
Sustainable Energy
Science & Technology
AgTech
Biosciences
Environmental Science
Food Science
Quantum Computation
Social and Behavioral Sciences
More Wolfram Solutions
Technology for Education
Research Universities
Colleges & Teaching Universities
High Schools
Resources for Students
Education Initiatives
Next-Gen EdTech
Computer-Based Math
More Solutions for Education
Contact Us
Learning & Support
Get Started
Wolfram Language Introduction
Fast Intro for Programmers
Fast Intro for Math Students
Wolfram Language Documentation
Grow Your Skills
Wolfram U
Courses in computing, science, life and more
Community
Learn, solve problems and share ideas.
Blog
News, views and insights from Wolfram
Resources for
Software Developers
Tech Support
Contact Us
Support FAQs
More Learning
Highlighted Core Areas
Demonstrations
YouTube
Daily Study Groups
Wolfram Schools and Programs
Books
Support FAQs
Contact Us
Company
About Wolfram
Career Center
All Sites & Resources
Connect & Follow
Contact Us
Work with Us
Student Ambassador Initiative
Wolfram for Startups
Student Opportunities
Jobs Using Wolfram Language
Educational Programs for Adults
Summer School
Winter School
Educational Programs for Youth
Middle School Camp
High School Research Program
Computational Adventures
Read
Stephen Wolfram's Writings
Wolfram Blog
Wolfram Tech | Books
Wolfram Media
Complex Systems
Educational Resources
Wolfram MathWorld
Wolfram in STEM
Wolfram Challenges
Wolfram Problem Generator
Wolfram Initiatives
Wolfram Science
Wolfram Foundation
History of Mathematics Project
Events
Stephen Wolfram Livestreams
Online & In-Person Events
Contact Us
Connect & Follow
For AIs
Wolfram Cloud
Your Account
User Portal
Enable JavaScript to interact with content and submit forms on Wolfram websites.
Learn how
Wolfram APIs
Overview
Wolfram Agent
One API
Wolfram|Alpha
Context API
Wolfram|Alpha
Results API
Wolfram Language
Computation API
Wolfram Language
Hints API
Wolfram|Alpha APIs
Overview
Documentation
Wolfram Agent
One API
Wolfram|Alpha
Context API
Wolfram|Alpha
Results API
Wolfram Language
Computation API
Wolfram Language
Hints API
Wolfram|Alpha APIs
More
Overview
Wolfram Agent
One API
Wolfram|Alpha
Context API
Wolfram|Alpha
Results API
Wolfram Language
Computation API
Wolfram Language
Hints API
Wolfram|Alpha APIs
Wolfram Language Hints API
Reference
Find Wolfram Language code samples relevant to a given query or task
The Wolfram Language Hints API searches Wolfram Language reference materials for code samples relevant to a given input. The response is formatted as text appropriate for use as part of an LLM prompt.
Request API Access
Using the API
Basic Usage
A basic request to the API takes the following form:
curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageHints \
-H "Content-Type: application/json" \
-H "Authorization: YOUR-API-KEY" \
-d '{
"context": "Draw a pentagram"
}'
which yields the following response:
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
Request Parameters
The following parameters can be passed in the body of an API request:
"context"
required
query for which to provide context
"count"
default:
5
maximum number of results to generate
context
(required)
The required parameter
"context"
specifies the message or messages for which additional prompting is generated.
"context"
accepts the following forms:
"query"
plaintext query suitable for an LLM
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
a list of JSON message objects
curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageHints \
-H "Content-Type: application/json" \
-H "Authorization: YOUR-API-KEY" \
-d '{
"context": "What'\''s the 123456789th prime?"
}'
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
count
(optional)
Use the optional
"count"
parameter to specify an upper bound on the number of related queries to generate. (The default value of
"count"
is
5
.)
curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageHints \
-H "Content-Type: application/json" \
-H "Authorization: YOUR-API-KEY" \
-d '{
"context": "Compare the Eiffel Tower to the pyramids at Giza",
"count": 2
}'
Response
The returned JSON contains the following fields:
result
(string)
A collection of Wolfram Language documentation code samples that typically includes related descriptive text and one or more input-output pairs
code
(integer)
API status code (e.g.
200
,
400
,
403
,
501
, ...)
success
(Boolean)
true
or
false
depending on whether the request completed successfully
uuid
(string)
A unique ID labeling the response
Status Codes
HTTP Status
200
This status indicates a success.
HTTP Status
400
This status indicates that the API did not find an input parameter while parsing. In most cases, this can be fixed by checking that you have used the correct syntax for including the input parameter.
HTTP Status
403
This status is returned when a request contains a missing or invalid API key in the authorization header. Double-check that your AppID is typed correctly and is using the correct syntax.
HTTP Status
501
This status is returned if a given input value cannot be interpreted by this API. This is commonly caused by input that is misspelled, poorly formatted or otherwise unintelligible. Because this API is designed to return results for use in LLMs, the body of the
501
message may contain suggested inputs. You may occasionally receive this status when requesting information on topics that are restricted or not covered.
Use of these APIs  is subject to the
API Terms of Use
and
Commercial Terms of Use
.
Contact Us
Download Page as PDF
-->
Products
Wolfram|One
Mathematica
AI Access
Compute Services
System Modeler
Wolfram|Alpha Notebook Edition
Wolfram|Alpha Pro
Mobile Apps
Wolfram Engine
Wolfram Player
Volume & Site Licensing
Server Deployment Options
Consulting
Wolfram Consulting
Repositories
Data Repository
Function Repository
Community Paclet Repository
Neural Net Repository
Prompt Repository
Wolfram Language Example Repository
Notebook Archive
Wolfram GitHub
Learning
Wolfram U
Wolfram Language Documentation
Webinars & Training
Educational Programs
Wolfram Language Introduction
Fast Introduction for Programmers
Fast Introduction for Math Students
Books
Wolfram Community
Wolfram Blog
Public Resources
Wolfram|Alpha
Wolfram Problem Generator
Wolfram Challenges
Computer-Based Math
Computational Thinking
Computational Adventures
Demonstrations Project
Wolfram Data Drop
MathWorld
Wolfram Science
Wolfram Media Publishing
Customer Resources
Store
Product Downloads
User Portal
Your Account
Organization Access
Support FAQ
Contact Support
Company
About Wolfram
Careers
Contact
Events
Wolfram Community
Wolfram Blog
Facebook
## X
Twitch
LinkedIn
YouTube
Wolfram
Legal
&
Privacy Policy
WolframAlpha.com
|
WolframCloud.com
Facebook
## X
Twitch
LinkedIn
YouTube
Wolfram
©
2026
Wolfram
©
2026
Wolfram
|
Legal
&
Privacy Policy
|
English
English
