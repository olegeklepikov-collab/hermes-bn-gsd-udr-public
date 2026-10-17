> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Wolfram: api-context

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


Wolfram|Alpha Context API: Reference
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
Wolfram|Alpha Context API
Reference
Augment LLM queries with related facts, figures, images and other content from Wolfram|Alpha
The Wolfram|Alpha Context API assists users by generating secondary Wolfram|Alpha queries that give factual context relevant to a given input. These queries and their results are then returned to the user in the form of plaintext that is appropriate for use as part of an LLM prompt.
Request API Access
Using the API
Basic Usage
A basic request to the API takes the following form:
curl -X POST https://services.wolfram.com/api/cag/v1/WolframAlphaContext \
-H "Content-Type: application/json" \
-H "Authorization: YOUR-API-KEY" \
-d '{
"context": "How long would it take a cheetah to round the bases in baseball?"
}'
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
"code"
:200,
"success"
:true,
"uuid"
:"${OBJECT_ID}"
}
Request Parameters
The following parameters can be passed in the body of an API request:
"context"
required
message to augment with Wolfram|Alpha knowledge
"count"
default:
5
number of related Wolfram|Alpha results to generate
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
"role" : "assistant"
"content" : "API RESPONSE"
},
{
"role" : "user"
"content" : "YOUR NEXT PROMPT"
}
]
}
a list of JSON message objects
curl -X POST https://services.wolfram.com/api/cag/v1/WolframAlphaContext \
-H "Content-Type: application/json" \
-H "Authorization: YOUR-API-KEY" \
-d '{
"context": "What'\''s the 123456789th prime?"
}'
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
# Density of primes
count
(optional)
Use the optional
"count"
parameter to specify an upper bound on the number of related queries to generate. (The default value of
"count"
is
5
.)
curl -X POST https://services.wolfram.com/api/cag/v1/WolframAlphaContext \
-H "Content-Type: application/json" \
-H "Authorization: YOUR-API-KEY" \
-d '{
"context": "Compare the Eiffel Tower to the pyramids at Giza",
"count": "2"
}'
Response
The returned JSON contains the following fields:
result
(string)
A plaintext summary of Wolfram|Alpha queries and results, with individual queries and their results delimited between
<result query=XXX>
and
</result>
tag pairs and returned in Markdown
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
