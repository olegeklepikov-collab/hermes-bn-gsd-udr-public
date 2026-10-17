> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Keenable: time-machine

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


https://keenable.ai/preview/time-machine

Time Machine - Search the web as it existed then
Keenable — Search for AI agents
Keenable provides low-latency web search and content access APIs built for AI agents. One API key works
                across the CLI, REST API, and MCP server.
Get started
Recommended: install the Keenable CLI. It handles account creation, authentication via device-code flow
                (opens browser or prints a link and code for remote setups), API key generation, and MCP configuration —
                no manual key copying. Run "keenable login" then "keenable configure-mcp --all".
Install: brew install keenableai/tap/keenable-cli
Documentation
All docs pages are available as clean markdown by appending .md to the URL (e.g. curl
                https://docs.keenable.ai/cli.md).
Quickstart
CLI reference
MCP server setup
Authentication
API — Search
API — Fetch
API — Feedback
llms.txt
Keenable Time Machine - Search the web as it existed then
Web pages change after they’re published, and search engines only ever serve the current version. That makes it hard to reconstruct what a query would have returned before a given event, or on a past date.
Keenable Time Machine
reproduces the search results Keenable would have returned at a past moment. Add
query_time
to any Search API request to exclude pages acquired later and recompute freshness and ranking relative to that timestamp.
{
  "query": "who will win the 2026 UEFA Champions League final?",
  "query_time": "2026-05-30T09:00:00Z"
}
Current search
today, no query_time
1
2026 UEFA Champions League final
result
acquired Jul 22
2
2026 UEFA Champions League final - Wikiwand
result
acquired Jul 14
3
2025–26 UEFA Champions League
result
acquired Jun 17
4
Who Won the Champions League Final 2026?
result
acquired May 31
5
Champions League 2025-26: PSG Crowned in Budapest | Squawka
result
acquired Jun 1
Post-match pages fill the results, and the top hit already announces the winner.
Point-in-time search
query_time = May 30, 09:00 UTC
1
PSG chases second title, Arsenal targets first in Champions League final tonight
acquired May 30
2
2026 UEFA Champions League final
acquired May 18
3
PSG vs Arsenal: UEFA Champions League final – 10 things to know | Football News - News Beep
acquired May 29
4
When is Champions League final 2026? Date, kick-off time, TV channel and live stream as Arsenal play PSG in Budapest
acquired May 26
5
Arsenal Reach Champions League Final: North London News 2026
acquired May 18
Every result was acquired before the match. No outcome has leaked in.
The only thing that changes is query_time. Rows acquired after the match are tinted red, those from before it green. Every response on this page is real, from
api.keenable.ai/v1/search
.
The web keeps changing
one query · 37 days · 50 query times
The web changes every minute. Pages are published, edited, and re-crawled, and search engines re-index and re-rank on top of that, so the results for a fixed query keep shifting, and around an event they can turn over completely. Below is one query run at 50 query times across 37 days, from the semifinals to just after the final. Each dot is a top-10 result at its acquired time, coloured by finalist; the line is
query_time
advancing. Watch Arsenal appear first as they reach the final, then PSG, then the whole set flip to the result the moment the line crosses kick-off.
Question
Who will win the 2026 UEFA Champions League final?
query_time
Arsenal
## PSG
other
result
horizontal = acquired time · vertical = recency (newest at top)
final · May 30
Apr 28, 12:14 UTC
Apr 29
May 8
May 16
May 24
Jun 1
query_time
Apr 28, 12:14 UTC
·
all 10 results are pre-match previews
most recent:
Official UEFA Champions League Podcast | Escuchar p…
❚❚ pause
03 / 50
the road to the final
key events a model read out of the result snippets
Apr 14
PSG beat Liverpool 2-0 at Anfield (4-0 agg)
Apr 15
Atletico Madrid beat Barcelona 3-2 agg to reach semis
Apr 15
Bayern Munich beat Real Madrid 6-4 agg to reach semis
Apr 16
Arsenal beat Sporting 1-0 agg to reach semis
Apr 28
PSG beat Bayern 5-4 in semi-final first leg
Apr 29
Arsenal vs Atletico Madrid semi-final first leg (1-1)
May 5
Arsenal beat Atletico Madrid 1-0 (2-1 agg) to reach final
May 6
PSG draw 1-1 with Bayern (6-5 agg) to reach final
May 30
2026 UEFA Champions League Final: PSG vs Arsenal
May 30
Kai Havertz scores to give Arsenal 1-0 lead
May 30
Ousmane Dembele penalty equalizes 1-1 for PSG
May 30
PSG win 4-3 on penalties after 1-1 draw (AET)
Over these 50 query times the top result changed 21 times, and 129 different pages passed through the top 10. That is a single query across 37 days.
Only the acquired date is always there
acquired_at · published_at · query_time
In search, “when” is ambiguous. Every result carries an acquired date, the moment Keenable crawled that version of the page. Many also carry a published date, but that one is declared by the publisher, so it is often missing and, when present, can disagree with the crawl by months. A query can name a third date: the moment you want to search as of.
Where the dates come from
Acquired time
(
acquired_at
): stamped by Keenable’s crawler when it fetched that version of the page. Always present, and it reflects when the content entered the index.
Published time
(
published_at
): pulled from the page’s own metadata (
og:article:published_time
## , JSON-LD
datePublished
, meta date tags) when it exists. It is whatever the publisher declared: unverified, often absent, and easily left stale on a page that keeps changing.
Query time
(
query_time
): the moment you search as of. It excludes pages acquired later and anchors every ranking signal to that instant.
When published_at lies
Here is a real result for this query, and it is a full match report. Its
published_at
is stamped 15:09 UTC on May 30, before the 18:00 CEST kick-off, so a
published_before
filter set to the match keeps it. But Keenable crawled the page at 19:56, once the final was over, and the copy it stored already names the winner and the score. The declared time is before the match; the snapshot behind it is not.
{
  "url":          "fox8live.com/2026/05/30/paris-saint-germain-tops-arsenal-shootout-...",
  "published_at": "2026-05-30T15:09:34Z",   // stamped before the 18:00 CEST kick-off
  "acquired_at":  "2026-05-30T19:56:24Z",   // but crawled after the final, once the result was out
  "snippet":      "Paris Saint-Germain defeated Arsenal in a dramatic penalty
                   shootout ... winning the shootout 4-3 ... for the second
                   year in a row."
  // The published time is before the match; the stored copy is the match report.
  // published_before trusts published_at and cannot tell the two apart.
}
The published date is whatever the source declared, so a page can carry a timestamp from before the match while the copy behind it was crawled after. The result above does exactly that: stamped 15:09, before kick-off, but crawled at 19:56 with “PSG won the shootout 4-3” in the body. A page first published before the match and updated once it was over, a live blog or a fixtures table, passes a
published_before
filter the same way while holding the score.
In a forecasting eval this breaks the result. The model is meant to predict the final; if the pages it retrieves already report the score, you are grading reading comprehension and calling it prediction. RL environments have the same gap. A tool call that returns pages crawled after the episode’s cutoff leaks the future the agent was supposed to work out, and because a live index keeps moving, the same task can return different documents from one run to the next, so the policy learns behaviour that only pays off because the environment keeps shifting under it.
query_time
gates on acquired time instead, so a page is in scope only if Keenable had stored it by the query time, and the ranking is recomputed as of that moment. The declared publication date never enters the decision.
The three filters
The same query at the same moment, filtered three ways. Each column is a real response;
published_before
and
acquired_before
scope the documents, but only
query_time
also rewinds the ranking, so the order matches what the index would have produced then.
Publication-date filter
published_before
Unverified dates
Gates on the publisher’s declared date, which is unverified. Several results were crawled after the final (flagged), so the copy can postdate the anchor.
2026 UEFA Champions League final
✓
en.wikipedia.org/wiki/2026_UEFA_Champions_League_final
preview
pub
May 13
acq
May 18
2026 UEFA Champions League Final Date, Venue & How to Watch
✓
fifaworldcupnews.com/2026-uefa-champions-league-final
preview
pub
May 6
acq
May 17
What to know about the 2026 Champions League final
✓
aol.co.uk/articles/know-2026-champions-league-final-103409476.html
preview
pub
May 6
acq
May 8
What is Arsenal's record in UEFA Champions League knockouts? Gunners into first final for two decades
✗ +42d
sports.yahoo.com/news/arsenals-record-uefa-champions-league-110600359.html
preview
pub
May 5
acq
Jul 11
PSG vs Arsenal: UEFA Champions League final – 10 things to know | Football News - News Beep
✓
newsbeep.com/563207
preview
pub
May 29
acq
May 29
Inspect response
01
en.wikipedia.org
2026 UEFA Champions League final
It will be played at the Puskás Aréna in Budapest, Hungary, on 30 May 2026 between French club Paris Saint-Germain, the defending champions, and English club Arsenal. This will be the first…
published
May 13, 2026 · 18:40
acquired
May 18, 2026 · 05:40
02
fifaworldcupnews.com
2026 UEFA Champions League Final Date, Venue & How to Watch
The 2026 UEFA Champions League Final between PSG vs Arsenal will be scheduled on Saturday, May 30, 2026, at 18:00 CEST at the Puskás Aréna in Budapest, Hungary. Arsenal has secured the firs…
published
May 6, 2026 · 21:33
acquired
May 17, 2026 · 10:01
03
aol.co.uk
What to know about the 2026 Champions League final
Paris Saint-Germain will take on Arsenal in the 2026 Champions League final. PSG eliminated Bayern Munich in the semifinals following a 1-1 draw on Wednesday to book its place in the showpi…
published
May 6, 2026 · 10:34
acquired
May 8, 2026 · 16:07
04
sports.yahoo.com
What is Arsenal's record in UEFA Champions League knockouts? Gunners into first final for two decades
Arsenal have reached their second Champions League final and a first for 20 years. Bukayo Saka’s goal was enough to seal a 1-0 win on the night and a 2-1 aggregate victory over Atletico Mad…
published
May 5, 2026 · 21:16
acquired
Jul 11, 2026 · 00:52
05
newsbeep.com
PSG vs Arsenal: UEFA Champions League final – 10 things to know | Football News - News Beep
This year’s final will be contested by English Premier League club Arsenal, who overcame Atletico Madrid in the semifinals, and French giants Paris Saint-Germain, who defeated Bayern Munich…
published
May 29, 2026 · 00:43
acquired
May 29, 2026 · 01:27
06
en.thairath.co.th
No Hesitation: Harry Kane Predicts UCL Champion After Finalists Revealed, Explains Why (Video)
On 7 May 2026 GMT+7, Harry Kane, striker for Bayern Munich, German Bundesliga champions, gave an interview after the 2025-26 UEFA Champions League semifinal second leg, which ended in a 1-1…
published
May 7, 2026 · 01:48
acquired
May 14, 2026 · 03:37
07
news.net
What to know about the 2026 Champions League final - News.net
Paris Saint-Germain will take on Arsenal in the 2026 Champions League final. PSG eliminated Bayern Munich in the semifinals following a 1-1 draw on Wednesday to book its place in the showpi…
published
May 6, 2026 · 22:20
acquired
Jun 20, 2026 · 06:04
08
chron.com
What to know about the 2026 Champions League final
Paris Saint-Germain will take on Arsenal in the 2026 Champions League final. PSG eliminated Bayern Munich in the semifinals following a 1-1 draw on Wednesday to book its place in the showpi…
published
May 7, 2026 · 08:41
acquired
May 31, 2026 · 08:06
09
uefa.com
2026 UEFA Champions League final: Where is it, who is involved, how to watch | UEFA Champions League | UEFA.com
Paris Saint-Germain will face Arsenal in the 2026 Champions League final. Holders Paris are bidding to become only the second club in the Champions League era to successfully defend their t…
published
May 11, 2026 · 20:30
acquired
May 24, 2026 · 19:54
10
uefa.com
Champions League final: Meet the teams | UEFA Champions League | UEFA.com
Champions League final **Paris Saint-Germain vs Arsenal **Saturday 30 May, 18:00 CET Arsenal (ENG) League phase: W8 D0 L0 F23 A4 (1st place) Round of 16: 3-1agg vs Leverkusen Paris (FRA) Le…
published
May 11, 2026 · 11:18
acquired
May 12, 2026 · 17:43
showing top 10 of 10 results · live from api.keenable.ai/v1/search
Acquisition-date filter
acquired_before
Historical corpus, current ranking
Restricts the corpus to what was indexed by the anchor, but ranks it with today’s freshness signals.
2026 UEFA Champions League final
✓
en.wikipedia.org/wiki/2026_UEFA_Champions_League_final
preview
pub
May 13
acq
May 18
2026 UEFA Champions League Final Date, Venue & How to Watch
✓
fifaworldcupnews.com/2026-uefa-champions-league-final
preview
pub
May 6
acq
May 17
What to know about the 2026 Champions League final
✓
aol.co.uk/articles/know-2026-champions-league-final-103409476.html
preview
pub
May 6
acq
May 8
PSG vs Arsenal: UEFA Champions League final – 10 things to know | Football News - News Beep
✓
newsbeep.com/563207
preview
pub
May 29
acq
May 29
No Hesitation: Harry Kane Predicts UCL Champion After Finalists Revealed, Explains Why (Video)
✓
en.thairath.co.th/sport/eurofootball/uefa/2931097
preview
pub
May 7
acq
May 14
Inspect response
01
en.wikipedia.org
2026 UEFA Champions League final
It will be played at the Puskás Aréna in Budapest, Hungary, on 30 May 2026 between French club Paris Saint-Germain, the defending champions, and English club Arsenal. This will be the first…
published
May 13, 2026 · 18:40
acquired
May 18, 2026 · 05:40
02
fifaworldcupnews.com
2026 UEFA Champions League Final Date, Venue & How to Watch
The 2026 UEFA Champions League Final between PSG vs Arsenal will be scheduled on Saturday, May 30, 2026, at 18:00 CEST at the Puskás Aréna in Budapest, Hungary. Arsenal has secured the firs…
published
May 6, 2026 · 21:33
acquired
May 17, 2026 · 10:01
03
aol.co.uk
What to know about the 2026 Champions League final
Paris Saint-Germain will take on Arsenal in the 2026 Champions League final. PSG eliminated Bayern Munich in the semifinals following a 1-1 draw on Wednesday to book its place in the showpi…
published
May 6, 2026 · 10:34
acquired
May 8, 2026 · 16:07
04
newsbeep.com
PSG vs Arsenal: UEFA Champions League final – 10 things to know | Football News - News Beep
This year’s final will be contested by English Premier League club Arsenal, who overcame Atletico Madrid in the semifinals, and French giants Paris Saint-Germain, who defeated Bayern Munich…
published
May 29, 2026 · 00:43
acquired
May 29, 2026 · 01:27
05
en.thairath.co.th
No Hesitation: Harry Kane Predicts UCL Champion After Finalists Revealed, Explains Why (Video)
On 7 May 2026 GMT+7, Harry Kane, striker for Bayern Munich, German Bundesliga champions, gave an interview after the 2025-26 UEFA Champions League semifinal second leg, which ended in a 1-1…
published
May 7, 2026 · 01:48
acquired
May 14, 2026 · 03:37
06
uefa.com
Champions League final: Meet the teams | UEFA Champions League | UEFA.com
Champions League final **Paris Saint-Germain vs Arsenal **Saturday 30 May, 18:00 CET Arsenal (ENG) League phase: W8 D0 L0 F23 A4 (1st place) Round of 16: 3-1agg vs Leverkusen Paris (FRA) Le…
published
May 11, 2026 · 11:18
acquired
May 12, 2026 · 17:43
07
apnews.com
What to know about the 2026 Champions League final
Paris Saint-Germain will take on Arsenal in the 2026 Champions League final. PSG eliminated Bayern Munich in the semifinals following a 1-1 draw on Wednesday to book its place in the showpi…
published
May 6, 2026 · 10:34
acquired
May 12, 2026 · 19:40
08
uefa.com
2026 UEFA Champions League final: Where is it, who is involved, how to watch | UEFA Champions League | UEFA.com
Paris Saint-Germain will face Arsenal in the 2026 Champions League final. Holders Paris are bidding to become only the second club in the Champions League era to successfully defend their t…
published
May 11, 2026 · 20:30
acquired
May 24, 2026 · 19:54
09
legit.ng
Supercomputer Predicts UEFA Champions League Winner After Real Madrid & Sporting Lisbon Exit
The Opta supercomputer has predicted the winner of the 2025/26 UEFA Champions League following the completion of the quarter-final fixtures on Wednesday, April 15. Four clubs, Atletico Madr…
published
Apr 16, 2026 · 08:03
acquired
May 16, 2026 · 21:54
10
football.fandom.com
2026 UEFA Champions League Final
It will be played at the Puskás Aréna in Budapest, Hungary, on 30 May 2026 between Paris Saint-Germain and English club Arsenal. Play-offs Bye Chelsea 8–2 5–2 (H) 3–0 (A) Round of 16 Bayer…
published
n/a
acquired
May 23, 2026 · 20:32
showing top 10 of 10 results · live from api.keenable.ai/v1/search
Query-time search
query_time
Historical corpus and ranking
Restricts the corpus and ranks it as of the query time, so both the set and the order match.
PSG chases second title, Arsenal targets first in Champions League final tonight
✓
turkiyetoday.com/sports/psg-chase-second-title-arsenal-target-first-in-champions-league-final-tonight-3220905
preview
pub
May 30
acq
May 30
2026 UEFA Champions League final
✓
en.wikipedia.org/wiki/2026_UEFA_Champions_League_final
preview
pub
May 13
acq
May 18
PSG vs Arsenal: UEFA Champions League final – 10 things to know | Football News - News Beep
✓
newsbeep.com/563207
preview
pub
May 29
acq
May 29
When is Champions League final 2026? Date, kick-off time, TV channel and live stream as Arsenal play PSG in Budapest
✓
thesun.co.uk/sport/39019265/champions-league-final-arsenal-psg-time-team-news-live-stream
preview
pub
May 26
acq
May 26
Arsenal Reach Champions League Final: North London News 2026
✓
northlondonnews.co.uk/sports/arsenal-fc/saka-sends-arsenal-to-champions-league-final-north-london-news-2026
preview
pub
May 14
acq
May 18
Inspect response
01
turkiyetoday.com
PSG chases second title, Arsenal targets first in Champions League final tonight
The UEFA Champions League title will be decided on Saturday night at the Puskas Arena, where reigning champions Paris Saint-Germain faces Premier League winners Arsenal in a final that brin…
published
May 30, 2026 · 01:11
acquired
May 30, 2026 · 01:23
02
en.wikipedia.org
2026 UEFA Champions League final
It will be played at the Puskás Aréna in Budapest, Hungary, on 30 May 2026 between French club Paris Saint-Germain, the defending champions, and English club Arsenal. This will be the first…
published
May 13, 2026 · 18:40
acquired
May 18, 2026 · 05:40
03
newsbeep.com
PSG vs Arsenal: UEFA Champions League final – 10 things to know | Football News - News Beep
This year’s final will be contested by English Premier League club Arsenal, who overcame Atletico Madrid in the semifinals, and French giants Paris Saint-Germain, who defeated Bayern Munich…
published
May 29, 2026 · 00:43
acquired
May 29, 2026 · 01:27
04
thesun.co.uk
When is Champions League final 2026? Date, kick-off time, TV channel and live stream as Arsenal play PSG in Budapest
Arsenal are looking to win the Champions League for the first time in the club’s history after knocking out Spanish giants Atletico Madrid in the semi-finals. The Champions League final wil…
published
May 26, 2026 · 20:33
acquired
May 26, 2026 · 20:45
05
northlondonnews.co.uk
Arsenal Reach Champions League Final: North London News 2026
Arsenal secured their place in the UEFA Champions League final for the first time in 20 years with a 1-0 victory over Atletico Madrid. Bukayo Saka scored the decisive goal in the 44th minut…
published
May 14, 2026 · 09:10
acquired
May 18, 2026 · 02:31
06
rmoutlook.com
Champions League final: How PSG and Arsenal got there
Champions League final: How PSG and Arsenal got there BUDAPEST, Hungary (AP) — How Paris Saint-Germain and Arsenal reached the Champions League final: PSG League stage: 11th place Playoffs:…
published
May 29, 2026 · 06:56
acquired
May 29, 2026 · 07:11
07
talksport.com
Champions League final odds: PSG edge Arsenal as favourites for European crown
The two 2026 Champions League finalists have been confirmed with defending champions PSG, reaching their second consecutive final, coming up against an Arsenal side who haven’t reached the…
published
May 7, 2026 · 09:19
acquired
May 26, 2026 · 13:03
08
thenewcitizen.ng
Saka Fires Arsenal Into First Champions League Final In 20 Years
Arsenal reached the Champions League final for the first time in 20 years as Bukayo Saka sealed a 1-0 win against Atletico Madrid on Tuesday. n second-placed Manchester City drew at Everton…
published
May 6, 2026 · 06:23
acquired
May 21, 2026 · 17:45
09
metrodailyng.com
Saka Fires Arsenal Into First Champions League Final In 20 Years
Arsenal reached the Champions League final for the first time in 20 years as Bukayo Saka sealed a 1-0 win against Atletico Madrid on Tuesday. will be crowned champions if they win their las…
published
May 6, 2026 · 05:58
acquired
May 22, 2026 · 01:16
10
uefa.com
Champions League final: Meet the teams | UEFA Champions League | UEFA.com
Champions League final **Paris Saint-Germain vs Arsenal **Saturday 30 May, 18:00 CET Arsenal (ENG) League phase: W8 D0 L0 F23 A4 (1st place) Round of 16: 3-1agg vs Leverkusen Paris (FRA) Le…
published
May 11, 2026 · 11:18
acquired
May 12, 2026 · 17:43
showing top 10 of 10 results · live from api.keenable.ai/v1/search
How often results leak the future
measured · 400 forecasting questions
We took a real forecasting benchmark, 400 questions, and searched each one at its historical date through Exa, a web-search API that supports
published_at
filtering, set to return only pages published before that date. Then a detector read every result and flagged any page whose content reports something from after the question. 5,555 of 14,541 returned pages did.
38%
of returned results carried information from after the question date
88%
of the 1,470 retrievals contained at least one leak
77%
had a leak inside the top five results a model reads
## A
published_before
filter can’t catch this. 78% of the leaking pages have no publication date at all, and the filter returned them anyway; of the ones that do carry a date, it is often years stale, a page stamped 2019 serving live 2026 market data, while the content behind the URL keeps refreshing. The leaks spread across 4,339 different pages and nearly every question in the set, and they cluster on sources that are live by design.
forecast.weather.gov
547
live weather forecast
espn.com
106
live sports scores
kworb.net
76
streaming charts
basketball-reference.com
73
live sports stats
polymarket.com
56
prediction market
finviz.com
41
live market data
Gating on acquired time removes the whole class of failure: a page counts only if Keenable had already crawled it at the question’s moment, so an always-current page with no date, or one refreshed after the fact, is simply out of scope.
Search API
endpoint · auth · parameters
Request
curl -s https://api.keenable.ai/v1/search \
  -H "X-API-Key: $KEENABLE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query":      "who will win the 2026 UEFA Champions League final?",
    "mode":       "realtime",
    "query_time": "2026-05-30T09:00:00Z"
  }'
POST https://api.keenable.ai/v1/search
. Authenticate with your key in the
X-API-Key
header; quota is tracked per key.
Parameters
Parameter
Type
Description
query
string, required
The search query. Natural language or keyword.
mode
"realtime"
Retrieval mode. "realtime" returns fresh, low-latency results.
published_after
ISO 8601 | YYYY-MM-DD | relative
Exclude results published before this value. Gates on published time.
published_before
ISO 8601 | YYYY-MM-DD | relative
Exclude results published after this value. Gates on published time.
acquired_after
ISO 8601 | YYYY-MM-DD | relative
Exclude results acquired before this value. Supports relative values like "7d" or "24h".
acquired_before
ISO 8601 | YYYY-MM-DD | relative
Exclude results acquired after this value.
query_time
ISO 8601 datetime
Snapshot the index: only pages acquired on or before this moment are eligible, and every ranking signal is computed relative to it.
Examples
Each temporal filter is a field you add to the request body, alongside
query
and
mode
. Combine the
published_*
or
acquired_*
pair to bound a window from both sides.
Add to the request body
Result
"published_after": "2026-05-10"
Only pages published on or after this date.
"published_before": "2026-05-30T09:00:00Z"
Only pages published on or before this moment.
"acquired_after": "7d"
Only pages acquired in the last seven days (relative value).
"acquired_before": "2026-05-30T09:00:00Z"
Only pages acquired on or before this moment.
"query_time": "2026-05-30T09:00:00Z"
Snapshot the index and rewind the ranking to this moment.
Date fields accept ISO 8601 (
## 2026-01-01T00:00:00Z
), plain
## YYYY-MM-DD
, or a relative value like
7d
. Relative values are not supported for
query_time
. Full reference:
interactive docs
·
OpenAPI spec
.
keenable.ai
