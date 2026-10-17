> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Keenable: time-machine

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


<div class="_Main_17wcw_63" role="main">

# Keenable Time Machine - Search the web as it existed then

<div class="_timemachine_15s6a_2">

Web pages change after they’re published, and search engines only ever serve the current version. That makes it hard to reconstruct what a query would have returned before a given event, or on a past date.

**Keenable Time Machine** reproduces the search results Keenable would have returned at a past moment. Add `query_time` to any Search API request to exclude pages acquired later and recompute freshness and ranking relative to that timestamp.

<div class="_tm-hero-req_15s6a_1344">

``` _tm-code_15s6a_283
{
  "query": "who will win the 2026 UEFA Champions League final?",
  "query_time": "2026-05-30T09:00:00Z"
}
```

</div>

<div class="_tm-ba_15s6a_1375">

<div class="_tm-ba-col_15s6a_1389 _tm-ba-bad_15s6a_1402">

<div class="_tm-ba-head_15s6a_1409">

<span class="_tm-ba-title-lbl_15s6a_1419">Current search</span><span class="_tm-ba-sub_15s6a_1427">today, no query_time</span>

</div>

1.  <span class="_tm-ba-rank_15s6a_1467">1</span><span class="_tm-ba-title_15s6a_1419">2026 UEFA Champions League final</span><span class="_tm-ba-meta_15s6a_1493"><span class="_tm-type_15s6a_1350 _tm-type-res_15s6a_1362">result</span><span class="_tm-ba-date_15s6a_1501">acquired Jul 22</span></span>
2.  <span class="_tm-ba-rank_15s6a_1467">2</span><span class="_tm-ba-title_15s6a_1419">2026 UEFA Champions League final - Wikiwand</span><span class="_tm-ba-meta_15s6a_1493"><span class="_tm-type_15s6a_1350 _tm-type-res_15s6a_1362">result</span><span class="_tm-ba-date_15s6a_1501">acquired Jul 14</span></span>
3.  <span class="_tm-ba-rank_15s6a_1467">3</span><span class="_tm-ba-title_15s6a_1419">2025–26 UEFA Champions League</span><span class="_tm-ba-meta_15s6a_1493"><span class="_tm-type_15s6a_1350 _tm-type-res_15s6a_1362">result</span><span class="_tm-ba-date_15s6a_1501">acquired Jun 17</span></span>
4.  <span class="_tm-ba-rank_15s6a_1467">4</span><span class="_tm-ba-title_15s6a_1419">Who Won the Champions League Final 2026?</span><span class="_tm-ba-meta_15s6a_1493"><span class="_tm-type_15s6a_1350 _tm-type-res_15s6a_1362">result</span><span class="_tm-ba-date_15s6a_1501">acquired May 31</span></span>
5.  <span class="_tm-ba-rank_15s6a_1467">5</span><span class="_tm-ba-title_15s6a_1419">Champions League 2025-26: PSG Crowned in Budapest \| Squawka</span><span class="_tm-ba-meta_15s6a_1493"><span class="_tm-type_15s6a_1350 _tm-type-res_15s6a_1362">result</span><span class="_tm-ba-date_15s6a_1501">acquired Jun 1</span></span>

<div class="_tm-ba-verdict_15s6a_1509">

Post-match pages fill the results, and the top hit already announces the winner.

</div>

</div>

<div class="_tm-ba-col_15s6a_1389 _tm-ba-good_15s6a_1405">

<div class="_tm-ba-head_15s6a_1409">

<span class="_tm-ba-title-lbl_15s6a_1419">Point-in-time search</span><span class="_tm-ba-sub_15s6a_1427">query_time = May 30, 09:00 UTC</span>

</div>

1.  <span class="_tm-ba-rank_15s6a_1467">1</span><span class="_tm-ba-title_15s6a_1419">PSG chases second title, Arsenal targets first in Champions League final tonight</span><span class="_tm-ba-meta_15s6a_1493"><span class="_tm-ba-date_15s6a_1501">acquired May 30</span></span>
2.  <span class="_tm-ba-rank_15s6a_1467">2</span><span class="_tm-ba-title_15s6a_1419">2026 UEFA Champions League final</span><span class="_tm-ba-meta_15s6a_1493"><span class="_tm-ba-date_15s6a_1501">acquired May 18</span></span>
3.  <span class="_tm-ba-rank_15s6a_1467">3</span><span class="_tm-ba-title_15s6a_1419">PSG vs Arsenal: UEFA Champions League final – 10 things to know \| Football News - News Beep</span><span class="_tm-ba-meta_15s6a_1493"><span class="_tm-ba-date_15s6a_1501">acquired May 29</span></span>
4.  <span class="_tm-ba-rank_15s6a_1467">4</span><span class="_tm-ba-title_15s6a_1419">When is Champions League final 2026? Date, kick-off time, TV channel and live stream as Arsenal play PSG in Budapest</span><span class="_tm-ba-meta_15s6a_1493"><span class="_tm-ba-date_15s6a_1501">acquired May 26</span></span>
5.  <span class="_tm-ba-rank_15s6a_1467">5</span><span class="_tm-ba-title_15s6a_1419">Arsenal Reach Champions League Final: North London News 2026</span><span class="_tm-ba-meta_15s6a_1493"><span class="_tm-ba-date_15s6a_1501">acquired May 18</span></span>

<div class="_tm-ba-verdict_15s6a_1509">

Every result was acquired before the match. No outcome has leaked in.

</div>

</div>

</div>

The only thing that changes is query_time. Rows acquired after the match are tinted red, those from before it green. Every response on this page is real, from `api.keenable.ai/v1/search`.

------------------------------------------------------------------------

<div class="section _tm-section_15s6a_121">

<div class="_tm-section-head_15s6a_131">

## The web keeps changing

<span class="_tm-kicker_15s6a_151">one query · 37 days · 50 query times</span>

</div>

The web changes every minute. Pages are published, edited, and re-crawled, and search engines re-index and re-rank on top of that, so the results for a fixed query keep shifting, and around an event they can turn over completely. Below is one query run at 50 query times across 37 days, from the semifinals to just after the final. Each dot is a top-10 result at its acquired time, coloured by finalist; the line is `query_time` advancing. Watch Arsenal appear first as they reach the final, then PSG, then the whole set flip to the result the moment the line crosses kick-off.

<div class="_tm-sweep_15s6a_634">

<div class="_tm-sweep-q_15s6a_644">

<span class="_tm-sweep-q-k_15s6a_656">Question</span><span class="_tm-sweep-q-v_15s6a_668">Who will win the 2026 UEFA Champions League final?</span>

</div>

<div class="_tm-sweep-legend_15s6a_677">

<span class="_tm-sweep-leg_15s6a_677"><span class="_tm-sweep-leg-line_15s6a_698"></span>query_time</span><span class="_tm-sweep-leg_15s6a_677"><span class="_tm-sweep-leg-dot_15s6a_707 _tm-sweep-leg-ars_15s6a_719"></span>Arsenal</span><span class="_tm-sweep-leg_15s6a_677"><span class="_tm-sweep-leg-dot_15s6a_707 _tm-sweep-leg-psg_15s6a_722"></span>PSG</span><span class="_tm-sweep-leg_15s6a_677"><span class="_tm-sweep-leg-dot_15s6a_707 _tm-sweep-leg-pred_15s6a_716"></span>other</span><span class="_tm-sweep-leg_15s6a_677"><span class="_tm-sweep-leg-dot_15s6a_707 _tm-sweep-leg-res_15s6a_725"></span>result</span><span class="_tm-sweep-leg-axis_15s6a_729">horizontal = acquired time · vertical = recency (newest at top)</span>

</div>

<div class="_tm-sweep-scroll_15s6a_743">

<div class="_tm-sweep-plot_15s6a_747">

<div class="_tm-sweep-match_15s6a_855" style="left: 84.2%;">

</div>

<span class="_tm-sweep-match-lbl_15s6a_867" style="left: 84.2%;">final · May 30</span>

<div class="_tm-sweep-dot_15s6a_766" style="left: 3%; top: 82.5px; opacity: 0.775;">

</div>

<div class="_tm-sweep-dot_15s6a_766" style="left: 3%; top: 124.5px; opacity: 0.595;">

</div>

<div class="_tm-sweep-dot_15s6a_766" style="left: 3%; top: 40.5px; opacity: 0.955;">

</div>

<div class="_tm-sweep-dot_15s6a_766" style="left: 3%; top: 61.5px; opacity: 0.865;">

</div>

<div class="_tm-sweep-dot_15s6a_766" style="left: 3%; top: 51px; opacity: 0.91;">

</div>

<div class="_tm-sweep-dot_15s6a_766 _tm-sweep-dot-psg_15s6a_796" style="left: 3%; top: 103.5px; opacity: 0.685;">

</div>

<div class="_tm-sweep-dot_15s6a_766 _tm-sweep-dot-top_15s6a_801" style="left: 3%; top: 30px; opacity: 1;">

</div>

<div class="_tm-sweep-dot_15s6a_766" style="left: 3%; top: 72px; opacity: 0.82;">

</div>

<div class="_tm-sweep-dot_15s6a_766" style="left: 3%; top: 93px; opacity: 0.73;">

</div>

<div class="_tm-sweep-dot_15s6a_766" style="left: 3%; top: 114px; opacity: 0.64;">

</div>

<div class="_tm-sweep-anchor_15s6a_813" style="left: 6.6%;">

</div>

<span class="_tm-sweep-qlabel_15s6a_826 _tm-sweep-qlabel-l_15s6a_846" style="left: 6.6%;">Apr 28, 12:14 UTC</span>

<div class="_tm-sweep-rail_15s6a_755">

</div>

<span class="_tm-sweep-day_15s6a_951" style="left: 7.8%;">Apr 29</span><span class="_tm-sweep-day_15s6a_951" style="left: 29.5%;">May 8</span><span class="_tm-sweep-day_15s6a_951" style="left: 48.7%;">May 16</span><span class="_tm-sweep-day_15s6a_951" style="left: 67.9%;">May 24</span><span class="_tm-sweep-day_15s6a_951" style="left: 87.2%;">Jun 1</span>

</div>

</div>

<div class="_tm-sweep-caption_15s6a_971">

<span class="_tm-sweep-cap-line_15s6a_976"><span class="_tm-sweep-cap-k_15s6a_987">query_time</span><span class="_tm-sweep-cap-v_15s6a_997">Apr 28, 12:14 UTC</span><span class="_tm-sweep-cap-sep_15s6a_1004">·</span><span class="_tm-sweep-cap-count_15s6a_1008">all 10 results are pre-match previews</span></span><span class="_tm-sweep-cap-top_15s6a_1018">most recent: <span class="_tm-sweep-cap-title_15s6a_1031">Official UEFA Champions League Podcast \| Escuchar p…</span></span>

</div>

<div class="_tm-sweep-controls_15s6a_1038">

❚❚ pause

<span class="_tm-sweep-frameidx_15s6a_1077">03 / 50</span>

</div>

<div class="_tm-sweep-events_15s6a_1088">

<div class="_tm-sweep-events-head_15s6a_1095">

the road to the final<span class="_tm-sweep-events-note_15s6a_1112">key events a model read out of the result snippets</span>

</div>

1.  <span class="_tm-sweep-ev-date_15s6a_1145">Apr 14</span><span class="_tm-sweep-ev-dot_15s6a_1153 _tm-sweep-ev-dot-psg_15s6a_1166"></span><span class="_tm-sweep-ev-label_15s6a_1173">PSG beat Liverpool 2-0 at Anfield (4-0 agg)</span>
2.  <span class="_tm-sweep-ev-date_15s6a_1145">Apr 15</span><span class="_tm-sweep-ev-dot_15s6a_1153"></span><span class="_tm-sweep-ev-label_15s6a_1173">Atletico Madrid beat Barcelona 3-2 agg to reach semis</span>
3.  <span class="_tm-sweep-ev-date_15s6a_1145">Apr 15</span><span class="_tm-sweep-ev-dot_15s6a_1153"></span><span class="_tm-sweep-ev-label_15s6a_1173">Bayern Munich beat Real Madrid 6-4 agg to reach semis</span>
4.  <span class="_tm-sweep-ev-date_15s6a_1145">Apr 16</span><span class="_tm-sweep-ev-dot_15s6a_1153 _tm-sweep-ev-dot-ars_15s6a_1163"></span><span class="_tm-sweep-ev-label_15s6a_1173">Arsenal beat Sporting 1-0 agg to reach semis</span>
5.  <span class="_tm-sweep-ev-date_15s6a_1145">Apr 28</span><span class="_tm-sweep-ev-dot_15s6a_1153 _tm-sweep-ev-dot-psg_15s6a_1166"></span><span class="_tm-sweep-ev-label_15s6a_1173">PSG beat Bayern 5-4 in semi-final first leg</span>
6.  <span class="_tm-sweep-ev-date_15s6a_1145">Apr 29</span><span class="_tm-sweep-ev-dot_15s6a_1153"></span><span class="_tm-sweep-ev-label_15s6a_1173">Arsenal vs Atletico Madrid semi-final first leg (1-1)</span>
7.  <span class="_tm-sweep-ev-date_15s6a_1145">May 5</span><span class="_tm-sweep-ev-dot_15s6a_1153 _tm-sweep-ev-dot-ars_15s6a_1163"></span><span class="_tm-sweep-ev-label_15s6a_1173">Arsenal beat Atletico Madrid 1-0 (2-1 agg) to reach final</span>
8.  <span class="_tm-sweep-ev-date_15s6a_1145">May 6</span><span class="_tm-sweep-ev-dot_15s6a_1153 _tm-sweep-ev-dot-psg_15s6a_1166"></span><span class="_tm-sweep-ev-label_15s6a_1173">PSG draw 1-1 with Bayern (6-5 agg) to reach final</span>
9.  <span class="_tm-sweep-ev-date_15s6a_1145">May 30</span><span class="_tm-sweep-ev-dot_15s6a_1153"></span><span class="_tm-sweep-ev-label_15s6a_1173">2026 UEFA Champions League Final: PSG vs Arsenal</span>
10. <span class="_tm-sweep-ev-date_15s6a_1145">May 30</span><span class="_tm-sweep-ev-dot_15s6a_1153 _tm-sweep-ev-dot-ars_15s6a_1163 _tm-sweep-ev-dot-res_15s6a_1169"></span><span class="_tm-sweep-ev-label_15s6a_1173">Kai Havertz scores to give Arsenal 1-0 lead</span>
11. <span class="_tm-sweep-ev-date_15s6a_1145">May 30</span><span class="_tm-sweep-ev-dot_15s6a_1153 _tm-sweep-ev-dot-psg_15s6a_1166 _tm-sweep-ev-dot-res_15s6a_1169"></span><span class="_tm-sweep-ev-label_15s6a_1173">Ousmane Dembele penalty equalizes 1-1 for PSG</span>
12. <span class="_tm-sweep-ev-date_15s6a_1145">May 30</span><span class="_tm-sweep-ev-dot_15s6a_1153 _tm-sweep-ev-dot-psg_15s6a_1166 _tm-sweep-ev-dot-res_15s6a_1169"></span><span class="_tm-sweep-ev-label_15s6a_1173">PSG win 4-3 on penalties after 1-1 draw (AET)</span>

</div>

</div>

Over these 50 query times the top result changed 21 times, and 129 different pages passed through the top 10. That is a single query across 37 days.

</div>

------------------------------------------------------------------------

<div class="section _tm-section_15s6a_121">

<div class="_tm-section-head_15s6a_131">

## Only the acquired date is always there

<span class="_tm-kicker_15s6a_151">acquired_at · published_at · query_time</span>

</div>

In search, “when” is ambiguous. Every result carries an acquired date, the moment Keenable crawled that version of the page. Many also carry a published date, but that one is declared by the publisher, so it is often missing and, when present, can disagree with the crawl by months. A query can name a third date: the moment you want to search as of.

### Where the dates come from

- **Acquired time** (`acquired_at`): stamped by Keenable’s crawler when it fetched that version of the page. Always present, and it reflects when the content entered the index.
- **Published time** (`published_at`): pulled from the page’s own metadata (`og:article:published_time`, JSON-LD `datePublished`, meta date tags) when it exists. It is whatever the publisher declared: unverified, often absent, and easily left stale on a page that keeps changing.
- **Query time** (`query_time`): the moment you search as of. It excludes pages acquired later and anchors every ranking signal to that instant.

<div class="_tm-leakage_15s6a_396">

<div class="_tm-leakage-head_15s6a_406">

When published_at lies

</div>

Here is a real result for this query, and it is a full match report. Its `published_at` is stamped 15:09 UTC on May 30, before the 18:00 CEST kick-off, so a `published_before` filter set to the match keeps it. But Keenable crawled the page at 19:56, once the final was over, and the copy it stored already names the winner and the score. The declared time is before the match; the snapshot behind it is not.

``` _tm-leakage-code_15s6a_456
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
```

The published date is whatever the source declared, so a page can carry a timestamp from before the match while the copy behind it was crawled after. The result above does exactly that: stamped 15:09, before kick-off, but crawled at 19:56 with “PSG won the shootout 4-3” in the body. A page first published before the match and updated once it was over, a live blog or a fixtures table, passes a `published_before` filter the same way while holding the score.

In a forecasting eval this breaks the result. The model is meant to predict the final; if the pages it retrieves already report the score, you are grading reading comprehension and calling it prediction. RL environments have the same gap. A tool call that returns pages crawled after the episode’s cutoff leaks the future the agent was supposed to work out, and because a live index keeps moving, the same task can return different documents from one run to the next, so the policy learns behaviour that only pays off because the environment keeps shifting under it.

`query_time` gates on acquired time instead, so a page is in scope only if Keenable had stored it by the query time, and the ranking is recomputed as of that moment. The declared publication date never enters the decision.

</div>

### The three filters

The same query at the same moment, filtered three ways. Each column is a real response; `published_before` and `acquired_before` scope the documents, but only `query_time` also rewinds the ranking, so the order matches what the index would have produced then.

<div class="_tm-compare_15s6a_1525">

<div class="_tm-cmp-col_15s6a_1539">

<div class="_tm-cmp-head_15s6a_1552">

<span class="_tm-cmp-name_15s6a_1560">Publication-date filter</span>`published_before`

</div>

<div class="_tm-cmp-verdict_15s6a_1576 _tm-cmp-verdict-bad_15s6a_1586">

Unverified dates

</div>

Gates on the publisher’s declared date, which is unverified. Several results were crawled after the final (flagged), so the copy can postdate the anchor.

<div class="_tm-cmp-items_15s6a_1605">

<div class="_tm-cmp-item_15s6a_1605 _tm-cmp-item-ok_15s6a_1629">

<div class="_tm-cmp-titlerow_15s6a_1634">

<a href="https://en.wikipedia.org/wiki/2026_UEFA_Champions_League_final" class="_tm-cmp-title_15s6a_1634" rel="noreferrer" target="_blank" title="https://en.wikipedia.org/wiki/2026_UEFA_Champions_League_final">2026 UEFA Champions League final</a><span class="_tm-cmp-flag_15s6a_1705">✓</span>

</div>

<div class="_tm-cmp-url_15s6a_1660">

en.wikipedia.org/wiki/2026_UEFA_Champions_League_final

</div>

<div class="_tm-cmp-sub_15s6a_1675">

<span class="_tm-type_15s6a_1350 _tm-type-pred_15s6a_1368">preview</span><span class="_tm-cmp-dates_15s6a_1685"><span class="_tm-cmp-dk_15s6a_1693">pub</span> May 13<span class="_tm-cmp-dk_15s6a_1693">acq</span> May 18</span>

</div>

</div>

<div class="_tm-cmp-item_15s6a_1605 _tm-cmp-item-ok_15s6a_1629">

<div class="_tm-cmp-titlerow_15s6a_1634">

<a href="https://fifaworldcupnews.com/2026-uefa-champions-league-final" class="_tm-cmp-title_15s6a_1634" rel="noreferrer" target="_blank" title="https://fifaworldcupnews.com/2026-uefa-champions-league-final">2026 UEFA Champions League Final Date, Venue &amp; How to Watch</a><span class="_tm-cmp-flag_15s6a_1705">✓</span>

</div>

<div class="_tm-cmp-url_15s6a_1660">

fifaworldcupnews.com/2026-uefa-champions-league-final

</div>

<div class="_tm-cmp-sub_15s6a_1675">

<span class="_tm-type_15s6a_1350 _tm-type-pred_15s6a_1368">preview</span><span class="_tm-cmp-dates_15s6a_1685"><span class="_tm-cmp-dk_15s6a_1693">pub</span> May 6<span class="_tm-cmp-dk_15s6a_1693">acq</span> May 17</span>

</div>

</div>

<div class="_tm-cmp-item_15s6a_1605 _tm-cmp-item-ok_15s6a_1629">

<div class="_tm-cmp-titlerow_15s6a_1634">

<a href="https://aol.co.uk/articles/know-2026-champions-league-final-103409476.html" class="_tm-cmp-title_15s6a_1634" rel="noreferrer" target="_blank" title="https://aol.co.uk/articles/know-2026-champions-league-final-103409476.html">What to know about the 2026 Champions League final</a><span class="_tm-cmp-flag_15s6a_1705">✓</span>

</div>

<div class="_tm-cmp-url_15s6a_1660">

aol.co.uk/articles/know-2026-champions-league-final-103409476.html

</div>

<div class="_tm-cmp-sub_15s6a_1675">

<span class="_tm-type_15s6a_1350 _tm-type-pred_15s6a_1368">preview</span><span class="_tm-cmp-dates_15s6a_1685"><span class="_tm-cmp-dk_15s6a_1693">pub</span> May 6<span class="_tm-cmp-dk_15s6a_1693">acq</span> May 8</span>

</div>

</div>

<div class="_tm-cmp-item_15s6a_1605 _tm-cmp-item-bad_15s6a_1625">

<div class="_tm-cmp-titlerow_15s6a_1634">

<a href="https://sports.yahoo.com/news/arsenals-record-uefa-champions-league-110600359.html" class="_tm-cmp-title_15s6a_1634" rel="noreferrer" target="_blank" title="https://sports.yahoo.com/news/arsenals-record-uefa-champions-league-110600359.html">What is Arsenal's record in UEFA Champions League knockouts? Gunners into first final for two decades</a><span class="_tm-cmp-flag_15s6a_1705">✗ +42d</span>

</div>

<div class="_tm-cmp-url_15s6a_1660">

sports.yahoo.com/news/arsenals-record-uefa-champions-league-110600359.html

</div>

<div class="_tm-cmp-sub_15s6a_1675">

<span class="_tm-type_15s6a_1350 _tm-type-pred_15s6a_1368">preview</span><span class="_tm-cmp-dates_15s6a_1685"><span class="_tm-cmp-dk_15s6a_1693">pub</span> May 5<span class="_tm-cmp-dk_15s6a_1693">acq</span> Jul 11</span>

</div>

</div>

<div class="_tm-cmp-item_15s6a_1605 _tm-cmp-item-ok_15s6a_1629">

<div class="_tm-cmp-titlerow_15s6a_1634">

<a href="https://newsbeep.com/563207" class="_tm-cmp-title_15s6a_1634" rel="noreferrer" target="_blank" title="https://newsbeep.com/563207">PSG vs Arsenal: UEFA Champions League final – 10 things to know | Football News - News Beep</a><span class="_tm-cmp-flag_15s6a_1705">✓</span>

</div>

<div class="_tm-cmp-url_15s6a_1660">

newsbeep.com/563207

</div>

<div class="_tm-cmp-sub_15s6a_1675">

<span class="_tm-type_15s6a_1350 _tm-type-pred_15s6a_1368">preview</span><span class="_tm-cmp-dates_15s6a_1685"><span class="_tm-cmp-dk_15s6a_1693">pub</span> May 29<span class="_tm-cmp-dk_15s6a_1693">acq</span> May 29</span>

</div>

</div>

</div>

Inspect response

<div class="_tm-serp_15s6a_1181">

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">01</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">en.wikipedia.org</span>

</div>

<a href="https://en.wikipedia.org/wiki/2026_UEFA_Champions_League_final" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">2026 UEFA Champions League final</a>

It will be played at the Puskás Aréna in Budapest, Hungary, on 30 May 2026 between French club Paris Saint-Germain, the defending champions, and English club Arsenal. This will be the first…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 13, 2026 · 18:40</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 18, 2026 · 05:40</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">02</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">fifaworldcupnews.com</span>

</div>

<a href="https://fifaworldcupnews.com/2026-uefa-champions-league-final" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">2026 UEFA Champions League Final Date, Venue &amp; How to Watch</a>

The 2026 UEFA Champions League Final between PSG vs Arsenal will be scheduled on Saturday, May 30, 2026, at 18:00 CEST at the Puskás Aréna in Budapest, Hungary. Arsenal has secured the firs…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 6, 2026 · 21:33</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 17, 2026 · 10:01</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">03</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">aol.co.uk</span>

</div>

<a href="https://aol.co.uk/articles/know-2026-champions-league-final-103409476.html" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">What to know about the 2026 Champions League final</a>

Paris Saint-Germain will take on Arsenal in the 2026 Champions League final. PSG eliminated Bayern Munich in the semifinals following a 1-1 draw on Wednesday to book its place in the showpi…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 6, 2026 · 10:34</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 8, 2026 · 16:07</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">04</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">sports.yahoo.com</span>

</div>

<a href="https://sports.yahoo.com/news/arsenals-record-uefa-champions-league-110600359.html" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">What is Arsenal's record in UEFA Champions League knockouts? Gunners into first final for two decades</a>

Arsenal have reached their second Champions League final and a first for 20 years. Bukayo Saka’s goal was enough to seal a 1-0 win on the night and a 2-1 aggregate victory over Atletico Mad…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 5, 2026 · 21:16</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-flag_15s6a_1299"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">Jul 11, 2026 · 00:52</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">05</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">newsbeep.com</span>

</div>

<a href="https://newsbeep.com/563207" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">PSG vs Arsenal: UEFA Champions League final – 10 things to know | Football News - News Beep</a>

This year’s final will be contested by English Premier League club Arsenal, who overcame Atletico Madrid in the semifinals, and French giants Paris Saint-Germain, who defeated Bayern Munich…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 29, 2026 · 00:43</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 29, 2026 · 01:27</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">06</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">en.thairath.co.th</span>

</div>

<a href="https://en.thairath.co.th/sport/eurofootball/uefa/2931097" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">No Hesitation: Harry Kane Predicts UCL Champion After Finalists Revealed, Explains Why (Video)</a>

On 7 May 2026 GMT+7, Harry Kane, striker for Bayern Munich, German Bundesliga champions, gave an interview after the 2025-26 UEFA Champions League semifinal second leg, which ended in a 1-1…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 7, 2026 · 01:48</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 14, 2026 · 03:37</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">07</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">news.net</span>

</div>

<a href="https://news.net/news/what-to-know-about-the-2026-champions-league-final" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">What to know about the 2026 Champions League final - News.net</a>

Paris Saint-Germain will take on Arsenal in the 2026 Champions League final. PSG eliminated Bayern Munich in the semifinals following a 1-1 draw on Wednesday to book its place in the showpi…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 6, 2026 · 22:20</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-flag_15s6a_1299"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">Jun 20, 2026 · 06:04</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">08</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">chron.com</span>

</div>

<a href="https://chron.com/sports/article/what-to-know-about-the-2026-champions-league-final-22246423.php" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">What to know about the 2026 Champions League final</a>

Paris Saint-Germain will take on Arsenal in the 2026 Champions League final. PSG eliminated Bayern Munich in the semifinals following a 1-1 draw on Wednesday to book its place in the showpi…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 7, 2026 · 08:41</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-flag_15s6a_1299"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 31, 2026 · 08:06</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">09</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">uefa.com</span>

</div>

<a href="https://uefa.com/uefachampionsleague/news/029a-1df98e9a78ca-1acaca3c53b0-1000--2026-uefa-champions-league-final-where-is-it-who-is-involv?:~:text=Sevilla%20claimed%20a%20record%20seventh_of%20Europe&#39;s%20premier%20club%20competition." class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">2026 UEFA Champions League final: Where is it, who is involved, how to watch | UEFA Champions League | UEFA.com</a>

Paris Saint-Germain will face Arsenal in the 2026 Champions League final. Holders Paris are bidding to become only the second club in the Champions League era to successfully defend their t…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 11, 2026 · 20:30</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 24, 2026 · 19:54</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">10</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">uefa.com</span>

</div>

<a href="https://uefa.com/uefachampionsleague/news/02a5-20901454177c-738c0ac757df-1000--champions-league-final-meet-the-teams" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">Champions League final: Meet the teams | UEFA Champions League | UEFA.com</a>

Champions League final \*\*Paris Saint-Germain vs Arsenal \*\*Saturday 30 May, 18:00 CET Arsenal (ENG) League phase: W8 D0 L0 F23 A4 (1st place) Round of 16: 3-1agg vs Leverkusen Paris (FRA) Le…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 11, 2026 · 11:18</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 12, 2026 · 17:43</span></span>

</div>

</div>

</div>

<div class="_tm-serp-total_15s6a_1334">

showing top 10 of 10 results · live from api.keenable.ai/v1/search

</div>

</div>

</div>

<div class="_tm-cmp-col_15s6a_1539">

<div class="_tm-cmp-head_15s6a_1552">

<span class="_tm-cmp-name_15s6a_1560">Acquisition-date filter</span>`acquired_before`

</div>

<div class="_tm-cmp-verdict_15s6a_1576 _tm-cmp-verdict-warn_15s6a_1589">

Historical corpus, current ranking

</div>

Restricts the corpus to what was indexed by the anchor, but ranks it with today’s freshness signals.

<div class="_tm-cmp-items_15s6a_1605">

<div class="_tm-cmp-item_15s6a_1605 _tm-cmp-item-ok_15s6a_1629">

<div class="_tm-cmp-titlerow_15s6a_1634">

<a href="https://en.wikipedia.org/wiki/2026_UEFA_Champions_League_final" class="_tm-cmp-title_15s6a_1634" rel="noreferrer" target="_blank" title="https://en.wikipedia.org/wiki/2026_UEFA_Champions_League_final">2026 UEFA Champions League final</a><span class="_tm-cmp-flag_15s6a_1705">✓</span>

</div>

<div class="_tm-cmp-url_15s6a_1660">

en.wikipedia.org/wiki/2026_UEFA_Champions_League_final

</div>

<div class="_tm-cmp-sub_15s6a_1675">

<span class="_tm-type_15s6a_1350 _tm-type-pred_15s6a_1368">preview</span><span class="_tm-cmp-dates_15s6a_1685"><span class="_tm-cmp-dk_15s6a_1693">pub</span> May 13<span class="_tm-cmp-dk_15s6a_1693">acq</span> May 18</span>

</div>

</div>

<div class="_tm-cmp-item_15s6a_1605 _tm-cmp-item-ok_15s6a_1629">

<div class="_tm-cmp-titlerow_15s6a_1634">

<a href="https://fifaworldcupnews.com/2026-uefa-champions-league-final" class="_tm-cmp-title_15s6a_1634" rel="noreferrer" target="_blank" title="https://fifaworldcupnews.com/2026-uefa-champions-league-final">2026 UEFA Champions League Final Date, Venue &amp; How to Watch</a><span class="_tm-cmp-flag_15s6a_1705">✓</span>

</div>

<div class="_tm-cmp-url_15s6a_1660">

fifaworldcupnews.com/2026-uefa-champions-league-final

</div>

<div class="_tm-cmp-sub_15s6a_1675">

<span class="_tm-type_15s6a_1350 _tm-type-pred_15s6a_1368">preview</span><span class="_tm-cmp-dates_15s6a_1685"><span class="_tm-cmp-dk_15s6a_1693">pub</span> May 6<span class="_tm-cmp-dk_15s6a_1693">acq</span> May 17</span>

</div>

</div>

<div class="_tm-cmp-item_15s6a_1605 _tm-cmp-item-ok_15s6a_1629">

<div class="_tm-cmp-titlerow_15s6a_1634">

<a href="https://aol.co.uk/articles/know-2026-champions-league-final-103409476.html" class="_tm-cmp-title_15s6a_1634" rel="noreferrer" target="_blank" title="https://aol.co.uk/articles/know-2026-champions-league-final-103409476.html">What to know about the 2026 Champions League final</a><span class="_tm-cmp-flag_15s6a_1705">✓</span>

</div>

<div class="_tm-cmp-url_15s6a_1660">

aol.co.uk/articles/know-2026-champions-league-final-103409476.html

</div>

<div class="_tm-cmp-sub_15s6a_1675">

<span class="_tm-type_15s6a_1350 _tm-type-pred_15s6a_1368">preview</span><span class="_tm-cmp-dates_15s6a_1685"><span class="_tm-cmp-dk_15s6a_1693">pub</span> May 6<span class="_tm-cmp-dk_15s6a_1693">acq</span> May 8</span>

</div>

</div>

<div class="_tm-cmp-item_15s6a_1605 _tm-cmp-item-ok_15s6a_1629">

<div class="_tm-cmp-titlerow_15s6a_1634">

<a href="https://newsbeep.com/563207" class="_tm-cmp-title_15s6a_1634" rel="noreferrer" target="_blank" title="https://newsbeep.com/563207">PSG vs Arsenal: UEFA Champions League final – 10 things to know | Football News - News Beep</a><span class="_tm-cmp-flag_15s6a_1705">✓</span>

</div>

<div class="_tm-cmp-url_15s6a_1660">

newsbeep.com/563207

</div>

<div class="_tm-cmp-sub_15s6a_1675">

<span class="_tm-type_15s6a_1350 _tm-type-pred_15s6a_1368">preview</span><span class="_tm-cmp-dates_15s6a_1685"><span class="_tm-cmp-dk_15s6a_1693">pub</span> May 29<span class="_tm-cmp-dk_15s6a_1693">acq</span> May 29</span>

</div>

</div>

<div class="_tm-cmp-item_15s6a_1605 _tm-cmp-item-ok_15s6a_1629">

<div class="_tm-cmp-titlerow_15s6a_1634">

<a href="https://en.thairath.co.th/sport/eurofootball/uefa/2931097" class="_tm-cmp-title_15s6a_1634" rel="noreferrer" target="_blank" title="https://en.thairath.co.th/sport/eurofootball/uefa/2931097">No Hesitation: Harry Kane Predicts UCL Champion After Finalists Revealed, Explains Why (Video)</a><span class="_tm-cmp-flag_15s6a_1705">✓</span>

</div>

<div class="_tm-cmp-url_15s6a_1660">

en.thairath.co.th/sport/eurofootball/uefa/2931097

</div>

<div class="_tm-cmp-sub_15s6a_1675">

<span class="_tm-type_15s6a_1350 _tm-type-pred_15s6a_1368">preview</span><span class="_tm-cmp-dates_15s6a_1685"><span class="_tm-cmp-dk_15s6a_1693">pub</span> May 7<span class="_tm-cmp-dk_15s6a_1693">acq</span> May 14</span>

</div>

</div>

</div>

Inspect response

<div class="_tm-serp_15s6a_1181">

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">01</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">en.wikipedia.org</span>

</div>

<a href="https://en.wikipedia.org/wiki/2026_UEFA_Champions_League_final" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">2026 UEFA Champions League final</a>

It will be played at the Puskás Aréna in Budapest, Hungary, on 30 May 2026 between French club Paris Saint-Germain, the defending champions, and English club Arsenal. This will be the first…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 13, 2026 · 18:40</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 18, 2026 · 05:40</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">02</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">fifaworldcupnews.com</span>

</div>

<a href="https://fifaworldcupnews.com/2026-uefa-champions-league-final" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">2026 UEFA Champions League Final Date, Venue &amp; How to Watch</a>

The 2026 UEFA Champions League Final between PSG vs Arsenal will be scheduled on Saturday, May 30, 2026, at 18:00 CEST at the Puskás Aréna in Budapest, Hungary. Arsenal has secured the firs…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 6, 2026 · 21:33</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 17, 2026 · 10:01</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">03</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">aol.co.uk</span>

</div>

<a href="https://aol.co.uk/articles/know-2026-champions-league-final-103409476.html" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">What to know about the 2026 Champions League final</a>

Paris Saint-Germain will take on Arsenal in the 2026 Champions League final. PSG eliminated Bayern Munich in the semifinals following a 1-1 draw on Wednesday to book its place in the showpi…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 6, 2026 · 10:34</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 8, 2026 · 16:07</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">04</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">newsbeep.com</span>

</div>

<a href="https://newsbeep.com/563207" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">PSG vs Arsenal: UEFA Champions League final – 10 things to know | Football News - News Beep</a>

This year’s final will be contested by English Premier League club Arsenal, who overcame Atletico Madrid in the semifinals, and French giants Paris Saint-Germain, who defeated Bayern Munich…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 29, 2026 · 00:43</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 29, 2026 · 01:27</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">05</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">en.thairath.co.th</span>

</div>

<a href="https://en.thairath.co.th/sport/eurofootball/uefa/2931097" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">No Hesitation: Harry Kane Predicts UCL Champion After Finalists Revealed, Explains Why (Video)</a>

On 7 May 2026 GMT+7, Harry Kane, striker for Bayern Munich, German Bundesliga champions, gave an interview after the 2025-26 UEFA Champions League semifinal second leg, which ended in a 1-1…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 7, 2026 · 01:48</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 14, 2026 · 03:37</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">06</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">uefa.com</span>

</div>

<a href="https://uefa.com/uefachampionsleague/news/02a5-20901454177c-738c0ac757df-1000--champions-league-final-meet-the-teams" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">Champions League final: Meet the teams | UEFA Champions League | UEFA.com</a>

Champions League final \*\*Paris Saint-Germain vs Arsenal \*\*Saturday 30 May, 18:00 CET Arsenal (ENG) League phase: W8 D0 L0 F23 A4 (1st place) Round of 16: 3-1agg vs Leverkusen Paris (FRA) Le…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 11, 2026 · 11:18</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 12, 2026 · 17:43</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">07</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">apnews.com</span>

</div>

<a href="https://apnews.com/article/champions-league-final-2026-kick-off-time-venue-841b3d49efddf8256a4fe696e97a7714" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">What to know about the 2026 Champions League final</a>

Paris Saint-Germain will take on Arsenal in the 2026 Champions League final. PSG eliminated Bayern Munich in the semifinals following a 1-1 draw on Wednesday to book its place in the showpi…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 6, 2026 · 10:34</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 12, 2026 · 19:40</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">08</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">uefa.com</span>

</div>

<a href="https://uefa.com/uefachampionsleague/news/029a-1df98e9a78ca-1acaca3c53b0-1000--2026-uefa-champions-league-final-where-is-it-who-is-involv?:~:text=Sevilla%20claimed%20a%20record%20seventh_of%20Europe&#39;s%20premier%20club%20competition." class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">2026 UEFA Champions League final: Where is it, who is involved, how to watch | UEFA Champions League | UEFA.com</a>

Paris Saint-Germain will face Arsenal in the 2026 Champions League final. Holders Paris are bidding to become only the second club in the Champions League era to successfully defend their t…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 11, 2026 · 20:30</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 24, 2026 · 19:54</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">09</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">legit.ng</span>

</div>

<a href="https://legit.ng/sports/football/1705737-supercomputer-predicts-uefa-champions-league-winner-real-madrid-sporting-exit" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">Supercomputer Predicts UEFA Champions League Winner After Real Madrid &amp; Sporting Lisbon Exit</a>

The Opta supercomputer has predicted the winner of the 2025/26 UEFA Champions League following the completion of the quarter-final fixtures on Wednesday, April 15. Four clubs, Atletico Madr…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">Apr 16, 2026 · 08:03</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 16, 2026 · 21:54</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">10</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">football.fandom.com</span>

</div>

<a href="https://football.fandom.com/wiki/2026_UEFA_Champions_League_Final" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">2026 UEFA Champions League Final</a>

It will be played at the Puskás Aréna in Budapest, Hungary, on 30 May 2026 between Paris Saint-Germain and English club Arsenal. Play-offs Bye Chelsea 8–2 5–2 (H) 3–0 (A) Round of 16 Bayer…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">n/a</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 23, 2026 · 20:32</span></span>

</div>

</div>

</div>

<div class="_tm-serp-total_15s6a_1334">

showing top 10 of 10 results · live from api.keenable.ai/v1/search

</div>

</div>

</div>

<div class="_tm-cmp-col_15s6a_1539">

<div class="_tm-cmp-head_15s6a_1552">

<span class="_tm-cmp-name_15s6a_1560">Query-time search</span>`query_time`

</div>

<div class="_tm-cmp-verdict_15s6a_1576 _tm-cmp-verdict-good_15s6a_1592">

Historical corpus and ranking

</div>

Restricts the corpus and ranks it as of the query time, so both the set and the order match.

<div class="_tm-cmp-items_15s6a_1605">

<div class="_tm-cmp-item_15s6a_1605 _tm-cmp-item-ok_15s6a_1629">

<div class="_tm-cmp-titlerow_15s6a_1634">

<a href="https://turkiyetoday.com/sports/psg-chase-second-title-arsenal-target-first-in-champions-league-final-tonight-3220905" class="_tm-cmp-title_15s6a_1634" rel="noreferrer" target="_blank" title="https://turkiyetoday.com/sports/psg-chase-second-title-arsenal-target-first-in-champions-league-final-tonight-3220905">PSG chases second title, Arsenal targets first in Champions League final tonight</a><span class="_tm-cmp-flag_15s6a_1705">✓</span>

</div>

<div class="_tm-cmp-url_15s6a_1660">

turkiyetoday.com/sports/psg-chase-second-title-arsenal-target-first-in-champions-league-final-tonight-3220905

</div>

<div class="_tm-cmp-sub_15s6a_1675">

<span class="_tm-type_15s6a_1350 _tm-type-pred_15s6a_1368">preview</span><span class="_tm-cmp-dates_15s6a_1685"><span class="_tm-cmp-dk_15s6a_1693">pub</span> May 30<span class="_tm-cmp-dk_15s6a_1693">acq</span> May 30</span>

</div>

</div>

<div class="_tm-cmp-item_15s6a_1605 _tm-cmp-item-ok_15s6a_1629">

<div class="_tm-cmp-titlerow_15s6a_1634">

<a href="https://en.wikipedia.org/wiki/2026_UEFA_Champions_League_final" class="_tm-cmp-title_15s6a_1634" rel="noreferrer" target="_blank" title="https://en.wikipedia.org/wiki/2026_UEFA_Champions_League_final">2026 UEFA Champions League final</a><span class="_tm-cmp-flag_15s6a_1705">✓</span>

</div>

<div class="_tm-cmp-url_15s6a_1660">

en.wikipedia.org/wiki/2026_UEFA_Champions_League_final

</div>

<div class="_tm-cmp-sub_15s6a_1675">

<span class="_tm-type_15s6a_1350 _tm-type-pred_15s6a_1368">preview</span><span class="_tm-cmp-dates_15s6a_1685"><span class="_tm-cmp-dk_15s6a_1693">pub</span> May 13<span class="_tm-cmp-dk_15s6a_1693">acq</span> May 18</span>

</div>

</div>

<div class="_tm-cmp-item_15s6a_1605 _tm-cmp-item-ok_15s6a_1629">

<div class="_tm-cmp-titlerow_15s6a_1634">

<a href="https://newsbeep.com/563207" class="_tm-cmp-title_15s6a_1634" rel="noreferrer" target="_blank" title="https://newsbeep.com/563207">PSG vs Arsenal: UEFA Champions League final – 10 things to know | Football News - News Beep</a><span class="_tm-cmp-flag_15s6a_1705">✓</span>

</div>

<div class="_tm-cmp-url_15s6a_1660">

newsbeep.com/563207

</div>

<div class="_tm-cmp-sub_15s6a_1675">

<span class="_tm-type_15s6a_1350 _tm-type-pred_15s6a_1368">preview</span><span class="_tm-cmp-dates_15s6a_1685"><span class="_tm-cmp-dk_15s6a_1693">pub</span> May 29<span class="_tm-cmp-dk_15s6a_1693">acq</span> May 29</span>

</div>

</div>

<div class="_tm-cmp-item_15s6a_1605 _tm-cmp-item-ok_15s6a_1629">

<div class="_tm-cmp-titlerow_15s6a_1634">

<a href="https://thesun.co.uk/sport/39019265/champions-league-final-arsenal-psg-time-team-news-live-stream" class="_tm-cmp-title_15s6a_1634" rel="noreferrer" target="_blank" title="https://thesun.co.uk/sport/39019265/champions-league-final-arsenal-psg-time-team-news-live-stream">When is Champions League final 2026? Date, kick-off time, TV channel and live stream as Arsenal play PSG in Budapest</a><span class="_tm-cmp-flag_15s6a_1705">✓</span>

</div>

<div class="_tm-cmp-url_15s6a_1660">

thesun.co.uk/sport/39019265/champions-league-final-arsenal-psg-time-team-news-live-stream

</div>

<div class="_tm-cmp-sub_15s6a_1675">

<span class="_tm-type_15s6a_1350 _tm-type-pred_15s6a_1368">preview</span><span class="_tm-cmp-dates_15s6a_1685"><span class="_tm-cmp-dk_15s6a_1693">pub</span> May 26<span class="_tm-cmp-dk_15s6a_1693">acq</span> May 26</span>

</div>

</div>

<div class="_tm-cmp-item_15s6a_1605 _tm-cmp-item-ok_15s6a_1629">

<div class="_tm-cmp-titlerow_15s6a_1634">

<a href="https://northlondonnews.co.uk/sports/arsenal-fc/saka-sends-arsenal-to-champions-league-final-north-london-news-2026" class="_tm-cmp-title_15s6a_1634" rel="noreferrer" target="_blank" title="https://northlondonnews.co.uk/sports/arsenal-fc/saka-sends-arsenal-to-champions-league-final-north-london-news-2026">Arsenal Reach Champions League Final: North London News 2026</a><span class="_tm-cmp-flag_15s6a_1705">✓</span>

</div>

<div class="_tm-cmp-url_15s6a_1660">

northlondonnews.co.uk/sports/arsenal-fc/saka-sends-arsenal-to-champions-league-final-north-london-news-2026

</div>

<div class="_tm-cmp-sub_15s6a_1675">

<span class="_tm-type_15s6a_1350 _tm-type-pred_15s6a_1368">preview</span><span class="_tm-cmp-dates_15s6a_1685"><span class="_tm-cmp-dk_15s6a_1693">pub</span> May 14<span class="_tm-cmp-dk_15s6a_1693">acq</span> May 18</span>

</div>

</div>

</div>

Inspect response

<div class="_tm-serp_15s6a_1181">

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">01</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">turkiyetoday.com</span>

</div>

<a href="https://turkiyetoday.com/sports/psg-chase-second-title-arsenal-target-first-in-champions-league-final-tonight-3220905" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">PSG chases second title, Arsenal targets first in Champions League final tonight</a>

The UEFA Champions League title will be decided on Saturday night at the Puskas Arena, where reigning champions Paris Saint-Germain faces Premier League winners Arsenal in a final that brin…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 30, 2026 · 01:11</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 30, 2026 · 01:23</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">02</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">en.wikipedia.org</span>

</div>

<a href="https://en.wikipedia.org/wiki/2026_UEFA_Champions_League_final" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">2026 UEFA Champions League final</a>

It will be played at the Puskás Aréna in Budapest, Hungary, on 30 May 2026 between French club Paris Saint-Germain, the defending champions, and English club Arsenal. This will be the first…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 13, 2026 · 18:40</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 18, 2026 · 05:40</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">03</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">newsbeep.com</span>

</div>

<a href="https://newsbeep.com/563207" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">PSG vs Arsenal: UEFA Champions League final – 10 things to know | Football News - News Beep</a>

This year’s final will be contested by English Premier League club Arsenal, who overcame Atletico Madrid in the semifinals, and French giants Paris Saint-Germain, who defeated Bayern Munich…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 29, 2026 · 00:43</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 29, 2026 · 01:27</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">04</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">thesun.co.uk</span>

</div>

<a href="https://thesun.co.uk/sport/39019265/champions-league-final-arsenal-psg-time-team-news-live-stream" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">When is Champions League final 2026? Date, kick-off time, TV channel and live stream as Arsenal play PSG in Budapest</a>

Arsenal are looking to win the Champions League for the first time in the club’s history after knocking out Spanish giants Atletico Madrid in the semi-finals. The Champions League final wil…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 26, 2026 · 20:33</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 26, 2026 · 20:45</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">05</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">northlondonnews.co.uk</span>

</div>

<a href="https://northlondonnews.co.uk/sports/arsenal-fc/saka-sends-arsenal-to-champions-league-final-north-london-news-2026" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">Arsenal Reach Champions League Final: North London News 2026</a>

Arsenal secured their place in the UEFA Champions League final for the first time in 20 years with a 1-0 victory over Atletico Madrid. Bukayo Saka scored the decisive goal in the 44th minut…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 14, 2026 · 09:10</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 18, 2026 · 02:31</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">06</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">rmoutlook.com</span>

</div>

<a href="https://rmoutlook.com/soccer/champions-league-final-how-psg-and-arsenal-got-there-12346204" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">Champions League final: How PSG and Arsenal got there</a>

Champions League final: How PSG and Arsenal got there BUDAPEST, Hungary (AP) — How Paris Saint-Germain and Arsenal reached the Champions League final: PSG League stage: 11th place Playoffs:…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 29, 2026 · 06:56</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 29, 2026 · 07:11</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">07</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">talksport.com</span>

</div>

<a href="https://talksport.com/football/3512372/champions-league-winner-odds-liverpool-psg-free-bets" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">Champions League final odds: PSG edge Arsenal as favourites for European crown</a>

The two 2026 Champions League finalists have been confirmed with defending champions PSG, reaching their second consecutive final, coming up against an Arsenal side who haven’t reached the…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 7, 2026 · 09:19</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 26, 2026 · 13:03</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">08</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">thenewcitizen.ng</span>

</div>

<a href="https://thenewcitizen.ng/saka-fires-arsenal-into-first-champions-league-final-in-20-years" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">Saka Fires Arsenal Into First Champions League Final In 20 Years</a>

Arsenal reached the Champions League final for the first time in 20 years as Bukayo Saka sealed a 1-0 win against Atletico Madrid on Tuesday. n second-placed Manchester City drew at Everton…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 6, 2026 · 06:23</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 21, 2026 · 17:45</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">09</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">metrodailyng.com</span>

</div>

<a href="https://metrodailyng.com/saka-fires-arsenal-into-first-champions-league-final-in-20-years" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">Saka Fires Arsenal Into First Champions League Final In 20 Years</a>

Arsenal reached the Champions League final for the first time in 20 years as Bukayo Saka sealed a 1-0 win against Atletico Madrid on Tuesday. will be crowned champions if they win their las…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 6, 2026 · 05:58</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 22, 2026 · 01:16</span></span>

</div>

</div>

</div>

<div class="_tm-serp-row_15s6a_1190">

<span class="_tm-serp-rank_15s6a_1204">10</span>

<div class="_tm-serp-main_15s6a_1215">

<div class="_tm-serp-head_15s6a_1219">

<span class="_tm-serp-host_15s6a_1228">uefa.com</span>

</div>

<a href="https://uefa.com/uefachampionsleague/news/02a5-20901454177c-738c0ac757df-1000--champions-league-final-meet-the-teams" class="_tm-serp-title_15s6a_1235" rel="noreferrer" target="_blank">Champions League final: Meet the teams | UEFA Champions League | UEFA.com</a>

Champions League final \*\*Paris Saint-Germain vs Arsenal \*\*Saturday 30 May, 18:00 CET Arsenal (ENG) League phase: W8 D0 L0 F23 A4 (1st place) Round of 16: 3-1agg vs Leverkusen Paris (FRA) Le…

<div class="_tm-serp-dates_15s6a_1262">

<span class="_tm-serp-date_15s6a_1262 tm-serp-date-pub"><span class="_tm-serp-date-k_15s6a_1284">published</span><span class="_tm-serp-date-v_15s6a_1293">May 11, 2026 · 11:18</span></span><span class="_tm-serp-date_15s6a_1262 tm-serp-date-acq _tm-serp-date-ok_15s6a_1309"><span class="_tm-serp-date-k_15s6a_1284">acquired</span><span class="_tm-serp-date-v_15s6a_1293">May 12, 2026 · 17:43</span></span>

</div>

</div>

</div>

<div class="_tm-serp-total_15s6a_1334">

showing top 10 of 10 results · live from api.keenable.ai/v1/search

</div>

</div>

</div>

</div>

</div>

------------------------------------------------------------------------

<div class="section _tm-section_15s6a_121">

<div class="_tm-section-head_15s6a_131">

## How often results leak the future

<span class="_tm-kicker_15s6a_151">measured · 400 forecasting questions</span>

</div>

We took a real forecasting benchmark, 400 questions, and searched each one at its historical date through Exa, a web-search API that supports `published_at` filtering, set to return only pages published before that date. Then a detector read every result and flagged any page whose content reports something from after the question. 5,555 of 14,541 returned pages did.

<div class="_tm-prev-stats_15s6a_486">

<div class="_tm-prev-stat_15s6a_486">

<span class="_tm-prev-stat-num_15s6a_515">38%</span><span class="_tm-prev-stat-lbl_15s6a_526">of returned results carried information from after the question date</span>

</div>

<div class="_tm-prev-stat_15s6a_486">

<span class="_tm-prev-stat-num_15s6a_515">88%</span><span class="_tm-prev-stat-lbl_15s6a_526">of the 1,470 retrievals contained at least one leak</span>

</div>

<div class="_tm-prev-stat_15s6a_486">

<span class="_tm-prev-stat-num_15s6a_515">77%</span><span class="_tm-prev-stat-lbl_15s6a_526">had a leak inside the top five results a model reads</span>

</div>

</div>

A `published_before` filter can’t catch this. 78% of the leaking pages have no publication date at all, and the filter returned them anyway; of the ones that do carry a date, it is often years stale, a page stamped 2019 serving live 2026 market data, while the content behind the URL keeps refreshing. The leaks spread across 4,339 different pages and nearly every question in the set, and they cluster on sources that are live by design.

<div class="_tm-prev-sites_15s6a_533">

<div class="_tm-prev-site_15s6a_533">

<span class="_tm-prev-site-host_15s6a_551">forecast.weather.gov</span><span class="_tm-prev-site-track_15s6a_562"><span class="_tm-prev-site-fill_15s6a_572" style="width: 100%;"></span></span><span class="_tm-prev-site-n_15s6a_581">547</span><span class="_tm-prev-site-kind_15s6a_591">live weather forecast</span>

</div>

<div class="_tm-prev-site_15s6a_533">

<span class="_tm-prev-site-host_15s6a_551">espn.com</span><span class="_tm-prev-site-track_15s6a_562"><span class="_tm-prev-site-fill_15s6a_572" style="width: 19%;"></span></span><span class="_tm-prev-site-n_15s6a_581">106</span><span class="_tm-prev-site-kind_15s6a_591">live sports scores</span>

</div>

<div class="_tm-prev-site_15s6a_533">

<span class="_tm-prev-site-host_15s6a_551">kworb.net</span><span class="_tm-prev-site-track_15s6a_562"><span class="_tm-prev-site-fill_15s6a_572" style="width: 14%;"></span></span><span class="_tm-prev-site-n_15s6a_581">76</span><span class="_tm-prev-site-kind_15s6a_591">streaming charts</span>

</div>

<div class="_tm-prev-site_15s6a_533">

<span class="_tm-prev-site-host_15s6a_551">basketball-reference.com</span><span class="_tm-prev-site-track_15s6a_562"><span class="_tm-prev-site-fill_15s6a_572" style="width: 13%;"></span></span><span class="_tm-prev-site-n_15s6a_581">73</span><span class="_tm-prev-site-kind_15s6a_591">live sports stats</span>

</div>

<div class="_tm-prev-site_15s6a_533">

<span class="_tm-prev-site-host_15s6a_551">polymarket.com</span><span class="_tm-prev-site-track_15s6a_562"><span class="_tm-prev-site-fill_15s6a_572" style="width: 10%;"></span></span><span class="_tm-prev-site-n_15s6a_581">56</span><span class="_tm-prev-site-kind_15s6a_591">prediction market</span>

</div>

<div class="_tm-prev-site_15s6a_533">

<span class="_tm-prev-site-host_15s6a_551">finviz.com</span><span class="_tm-prev-site-track_15s6a_562"><span class="_tm-prev-site-fill_15s6a_572" style="width: 8%;"></span></span><span class="_tm-prev-site-n_15s6a_581">41</span><span class="_tm-prev-site-kind_15s6a_591">live market data</span>

</div>

</div>

Gating on acquired time removes the whole class of failure: a page counts only if Keenable had already crawled it at the question’s moment, so an always-current page with no date, or one refreshed after the fact, is simply out of scope.

</div>

------------------------------------------------------------------------

<div class="section _tm-section_15s6a_121">

<div class="_tm-section-head_15s6a_131">

## Search API

<span class="_tm-kicker_15s6a_151">endpoint · auth · parameters</span>

</div>

### Request

<div class="_tm-code-block_15s6a_313">

``` _tm-code_15s6a_283
curl -s https://api.keenable.ai/v1/search \
  -H "X-API-Key: $KEENABLE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query":      "who will win the 2026 UEFA Champions League final?",
    "mode":       "realtime",
    "query_time": "2026-05-30T09:00:00Z"
  }'
```

</div>

`POST https://api.keenable.ai/v1/search`. Authenticate with your key in the `X-API-Key` header; quota is tracked per key.

### Parameters

<div class="_tm-table-wrap_15s6a_340">

| Parameter | Type | Description |
|----|----|----|
| `query` | string, required | The search query. Natural language or keyword. |
| `mode` | "realtime" | Retrieval mode. "realtime" returns fresh, low-latency results. |
| `published_after` | ISO 8601 \| YYYY-MM-DD \| relative | Exclude results published before this value. Gates on published time. |
| `published_before` | ISO 8601 \| YYYY-MM-DD \| relative | Exclude results published after this value. Gates on published time. |
| `acquired_after` | ISO 8601 \| YYYY-MM-DD \| relative | Exclude results acquired before this value. Supports relative values like "7d" or "24h". |
| `acquired_before` | ISO 8601 \| YYYY-MM-DD \| relative | Exclude results acquired after this value. |
| `query_time` | ISO 8601 datetime | Snapshot the index: only pages acquired on or before this moment are eligible, and every ranking signal is computed relative to it. |

</div>

### Examples

Each temporal filter is a field you add to the request body, alongside `query` and `mode`. Combine the `published_*` or `acquired_*` pair to bound a window from both sides.

<div class="_tm-table-wrap_15s6a_340">

| Add to the request body | Result |
|----|----|
| `"published_after": "2026-05-10"` | Only pages published on or after this date. |
| `"published_before": "2026-05-30T09:00:00Z"` | Only pages published on or before this moment. |
| `"acquired_after": "7d"` | Only pages acquired in the last seven days (relative value). |
| `"acquired_before": "2026-05-30T09:00:00Z"` | Only pages acquired on or before this moment. |
| `"query_time": "2026-05-30T09:00:00Z"` | Snapshot the index and rewind the ranking to this moment. |

</div>

Date fields accept ISO 8601 (`2026-01-01T00:00:00Z`), plain `YYYY-MM-DD`, or a relative value like `7d`. Relative values are not supported for `query_time`. Full reference: <a href="https://api.keenable.ai/docs/" rel="noreferrer" target="_blank">interactive docs</a> · <a href="https://api.keenable.ai/openapi.json" rel="noreferrer" target="_blank">OpenAPI spec</a>.

</div>

keenable.ai

</div>

</div>
