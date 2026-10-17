> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Wolfram: api-compute

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


Wolfram Language Computation API: Reference
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
Wolfram Language Computation API
Reference
An evaluator for Wolfram Language inputs
The Wolfram Language Computation API evaluates Wolfram Language code to give reliable, computationally driven results suitable for use by an LLM.
Request API Access
Using the API
Basic Usage
A basic request to the API takes the following form:
curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageCompute \
-H "Content-Type: application/json" \
-H "Authorization: YOUR-API-KEY" \
-d '{
"code": "Sin[Pi]"
}'
which yields the following response:
"{
"result":"Out[1]=0",
"code":200,
"success":true,
"uuid":"${OBJECT_ID}"
}"
Request Parameters
The following parameters can be passed in the body of an API request:
"code"
required
Wolfram Language code to evaluate
"line"
default:
1
label for output
"maxChars"
default:
10000
maximum characters of output to return
"timeConstraint"
default:
60
maximum allowed evaluation time in seconds
code
(required)
The code to be evaluated is passed to the API using the
"code"
parameter:
curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageCompute \
-H "Content-Type: application/json" \
-H "Authorization: YOUR-API-KEY" \
-d '{
"code": "TrigExpand@Sin[2x]"
}'
"{
"result":"Out[1]= 2*Cos[x]*Sin[x]",
"code":200,
"success":true,
"uuid":"${OBJECT_ID}"
}"
Images and graphics are returned via a Markdown image URL:
curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageCompute \
-H "Content-Type: application/json" \
-H "Authorization: YOUR-API-KEY" \
-d '{
"code": "Graphics[{Red, Circle[]}]"
}'
"{
"result":"Out1]=![Image (пример адреса или протокола; задаётся в целевой среде)",
"code":200,
"success":true,
"uuid":"${OBJECT_ID}"
}"
View the image:
The free-form prompt character,
=
, can be used to represent
ctrl-=
in inputs to retrieve curated data through natural language:
curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageCompute \
-H "Content-Type: application/json" \
-H "Authorization: YOUR-API-KEY" \
-d '{
"code": "\\[FreeformPrompt][\"France population\"]"
}'
"{
"result":"During evaluation of In[1]:= [INFO] Interpreted "France population" as: Entity["Country", "France"][EntityProperty["Country", "Population"]]
Out[1]= Quantity[66438822, "People"]",
"code":200,
"success":true,
"uuid":"${OBJECT_ID}"
}"
line
(optional)
The integer appearing in the output label can be overridden with the
"line"
parameter:
curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageCompute \
-H "Content-Type: application/json" \
-H "Authorization: YOUR-API-KEY" \
-d '{
"code": "Integrate[x, {x, 0, 1}]", "line": "50"
}'
"{
"result":"Out[50]= 1/2",
"code":200,
"success":true,
"uuid":"${OBJECT_ID}"
}"
maxChars
(optional)
The size of the output can be limited using the
"maxChars"
parameter:
curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageCompute \
-H "Content-Type: application/json" \
-H "Authorization: YOUR-API-KEY" \
-d '{
"code": "ExampleData[{\"Text\", \"AliceInWonderland\"}]", "maxChars": 1000
}'
Elision markers
and
>>
indicate where the output was shortened and by how much:
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
>    suddenly
50875
>>
ve had such a curious dream!" said Alice. And
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
timeConstraint
(optional)
Evaluation time can be limited using the
"timeConstraint"
parameter:
curl -X POST https://services.wolfram.com/api/cag/v1/WolframLanguageCompute \
-H "Content-Type: application/json" \
-H "Authorization: YOUR-API-KEY" \
-d '{
"code": "Pause[60]", "timeConstraint": "10"
}'
When the time constraint is exceeded,
"result"
is a
Failure
expression:
{
"result":"Failure["EvaluationTimeExceeded",
"Evaluation exceeded the `1` second time limit.",
"MessageParameters" -> {10}|>]",
"code":200,
"success":true,
"uuid":"${OBJECT_ID}"
}
Response
The returned JSON contains the following fields:
result
(string)
The result of evaluating the Wolfram Language expression passed in via the
"code"
body parameter
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
