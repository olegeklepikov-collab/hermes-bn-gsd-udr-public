> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: endpoints

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


<!DOCTYPE html><html lang="en" data-astro-cid-hkbrpulz><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="icon" type="image/png" href="/favicon.png"><link rel="apple-touch-icon" href="/favicon.png"><title>Endpoints Overview | OpenAlex Help Center</title><meta name="description" content="Every OpenAlex API endpoint at a glance — the entity list/single endpoints and the special-purpose ones — each linking to the entity page that documents its fields."><link rel="canonical" href="https://help.openalex.org/api/endpoints/"><link rel="alternate" type="text/plain" href="/llms.txt" title="llms.txt: index of every page, for AI agents"><link rel="stylesheet" href="/_astro/Base.BfIoc8yE.css"><style>.breadcrumbs[data-astro-cid-vx4iavld]{margin-bottom:.6rem}ol[data-astro-cid-vx4iavld]{color:var(--muted);flex-wrap:wrap;align-items:center;margin:0;padding:0;font-size:.82rem;list-style:none;display:flex}li[data-astro-cid-vx4iavld]{align-items:center;display:flex}.sep[data-astro-cid-vx4iavld]{color:var(--faint);flex:none;margin:0 .35rem}a[data-astro-cid-vx4iavld]{color:var(--muted)}a[data-astro-cid-vx4iavld]:hover{color:var(--accent);text-decoration:none}a[data-astro-cid-vx4iavld],span[data-astro-cid-vx4iavld]{align-items:center;gap:.3rem;display:inline-flex}.page-head[data-astro-cid-b2i3gsw2]{margin:0 0 2.25rem}.crumb-slot[data-astro-cid-b2i3gsw2]{align-items:center;height:1.66rem;display:flex}.crumb-slot[data-astro-cid-b2i3gsw2] .breadcrumbs{margin-bottom:0}.page-head[data-astro-cid-b2i3gsw2] h1[data-astro-cid-b2i3gsw2]{margin:0}.lede[data-astro-cid-b2i3gsw2]{color:var(--muted);margin:.5rem 0 0;font-size:.97rem;line-height:1.6}
aside[data-astro-cid-wv7whodv]{border-right:1px solid var(--line);background:#fafafa}nav[data-astro-cid-wv7whodv]{top:var(--nav-h);height:calc(100dvh - var(--nav-h));letter-spacing:.005em;scrollbar-width:thin;flex-direction:column;gap:2rem;padding:1.5rem 1rem 2.5rem 1.5rem;font-size:15px;display:flex;position:sticky;overflow-y:auto}.group[data-astro-cid-wv7whodv]{flex-direction:column;display:flex}.group-label[data-astro-cid-wv7whodv]{text-transform:uppercase;letter-spacing:.06em;color:var(--faint);margin-bottom:.45rem;font-size:.72rem;font-weight:700}a[data-astro-cid-wv7whodv]{color:var(--ink);border-radius:6px;align-items:center;gap:.5rem;margin-left:-.5rem;padding:.22rem .5rem;line-height:1.4;display:flex}a[data-astro-cid-wv7whodv]:hover{background:var(--panel-strong);color:var(--ink);text-decoration:none}a[data-astro-cid-wv7whodv][aria-current=page]{background:var(--line);color:var(--ink);font-weight:550}a[data-astro-cid-wv7whodv][aria-current=page]:hover{color:var(--ink)}summary[data-astro-cid-wv7whodv]{color:var(--ink);cursor:pointer;user-select:none;border-radius:6px;justify-content:space-between;align-items:center;gap:.5rem;margin-left:-.5rem;padding:.22rem .5rem;line-height:1.4;list-style:none;display:flex}summary[data-astro-cid-wv7whodv]::-webkit-details-marker{display:none}summary[data-astro-cid-wv7whodv]:hover{background:var(--panel-strong);color:var(--ink)}.chev[data-astro-cid-wv7whodv]{color:var(--faint);flex:none;transition:transform .15s}details[data-astro-cid-wv7whodv][open]>summary[data-astro-cid-wv7whodv] .chev[data-astro-cid-wv7whodv]{transform:rotate(90deg)}.children[data-astro-cid-wv7whodv]{border-left:1px solid var(--line);flex-direction:column;margin-left:.55rem;padding-left:.55rem;display:flex}@media (width<=900px){aside[data-astro-cid-wv7whodv]{display:none}}.shell[data-astro-cid-b4hyvnpz]{grid-template-columns:var(--sidebar-w) minmax(0, 1fr);min-height:calc(100dvh - var(--nav-h));display:grid}.content[data-astro-cid-b4hyvnpz]{min-width:0;padding:1.5rem 2rem 5rem}.columns[data-astro-cid-b4hyvnpz]{grid-template-columns:minmax(0,46rem) 13rem;justify-content:center;gap:3.5rem;display:grid}.rail-col[data-astro-cid-b4hyvnpz]{font-size:.84rem}@media (width<=1180px){.columns[data-astro-cid-b4hyvnpz]{grid-template-columns:minmax(0,46rem)}.rail-col[data-astro-cid-b4hyvnpz]{display:none}}@media (width<=900px){.shell[data-astro-cid-b4hyvnpz]{grid-template-columns:1fr}.content[data-astro-cid-b4hyvnpz]{padding:2rem 1.25rem 4rem}}
.entity-meta[data-astro-cid-yi3odb5r]{width:fit-content;max-width:100%;font-family:var(--font-mono);grid-template-columns:max-content minmax(0,1fr);gap:0 1ch;margin:-1.75rem 0 2.25rem;font-size:.8rem;line-height:1.7;display:grid}.group[data-astro-cid-yi3odb5r]{display:contents}.label[data-astro-cid-yi3odb5r]{color:var(--muted);font-family:var(--font-body)}.entity-meta[data-astro-cid-yi3odb5r] a[data-astro-cid-yi3odb5r]{color:var(--ink)}.entity-meta[data-astro-cid-yi3odb5r] a[data-astro-cid-yi3odb5r]:hover{color:var(--ink);text-decoration:underline}.updated[data-astro-cid-wytylmfw]{color:var(--faint);margin:0;font-size:.82rem}article[data-astro-cid-tlodkskj].prose{max-width:none}.tut-tags[data-astro-cid-tlodkskj]{flex-wrap:wrap;gap:.4rem;margin-top:.7rem;display:flex}.tag[data-astro-cid-tlodkskj]{color:var(--muted);border:1px solid var(--line);white-space:nowrap;background:0 0;border-radius:4px;padding:.05rem .5rem;font-size:.72rem;line-height:1.5}.rail[data-astro-cid-tlodkskj]{top:calc(var(--nav-h) + 1.5rem);position:sticky}.rail-head[data-astro-cid-tlodkskj]{letter-spacing:.06em;text-transform:uppercase;height:1.66rem;color:var(--faint);align-items:center;margin-bottom:.45rem;font-size:.72rem;font-weight:600;display:flex}.toc[data-astro-cid-tlodkskj]{flex-direction:column;gap:.35rem;display:flex}.toc[data-astro-cid-tlodkskj] a[data-astro-cid-tlodkskj]{color:var(--muted)}.toc[data-astro-cid-tlodkskj] a[data-astro-cid-tlodkskj]:hover{color:var(--ink);text-decoration:none}.article-foot[data-astro-cid-tlodkskj]{border-top:1px solid var(--line);flex-wrap:wrap;align-items:baseline;gap:.35rem 1rem;margin-top:3rem;padding-top:1.25rem;display:flex}.md-link[data-astro-cid-tlodkskj]{color:var(--muted);margin-left:auto;font-size:.82rem}.md-link[data-astro-cid-tlodkskj]:hover{color:var(--ink)}
</style></head><body data-astro-cid-hkbrpulz><header data-astro-cid-hkbrpulz><div class="topbar" data-astro-cid-hkbrpulz><a href="/" class="logo" aria-label="OpenAlex Help home" data-astro-cid-hkbrpulz><img src="/favicon.svg" alt="" height="22" data-astro-cid-hkbrpulz><span class="logo-name" data-astro-cid-hkbrpulz>OpenAlex</span><span class="logo-help" data-astro-cid-hkbrpulz>Help</span></a><div class="nav-right" data-astro-cid-hkbrpulz><button id="search-open" aria-label="Search" title="Search (⌘K)" data-astro-cid-ac66eqjo><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true" data-astro-cid-ac66eqjo><circle cx="11" cy="11" r="7" data-astro-cid-ac66eqjo></circle><path d="m20 20-3.5-3.5" data-astro-cid-ac66eqjo></path></svg><span class="search-label" data-astro-cid-ac66eqjo>Search help center…</span><kbd data-kbd-shortcut data-astro-cid-ac66eqjo>⌘K</kbd></button><script type="module">if(!/mac|iphone|ipad|ipod/i.test(navigator.platform||``)){for(let e of document.querySelectorAll(`[data-kbd-shortcut]`))e.textContent=`Ctrl K`;let e=document.getElementById(`search-open`);e&&(e.title=`Search (Ctrl K)`)}</script><dialog id="search-dialog" aria-label="Search the help center" data-astro-cid-ac66eqjo><div class="sd-head" data-astro-cid-ac66eqjo><svg class="sd-head-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true" data-astro-cid-ac66eqjo><circle cx="11" cy="11" r="7" data-astro-cid-ac66eqjo></circle><path d="m20 20-3.5-3.5" data-astro-cid-ac66eqjo></path></svg><input id="sd-input" type="search" placeholder="Search (eg: &quot;rate limit&quot;)" autocomplete="off" autocorrect="off" spellcheck="false" aria-controls="sd-body" data-astro-cid-ac66eqjo><button id="sd-clear" type="button" aria-label="Clear search" hidden data-astro-cid-ac66eqjo><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true" data-astro-cid-ac66eqjo><path d="M6 6l12 12M18 6L6 18" data-astro-cid-ac66eqjo></path></svg></button></div><div class="sd-body" id="sd-body" data-astro-cid-ac66eqjo></div><p class="sd-fallback" data-astro-cid-ac66eqjo>Search runs on the deployed site — it’s unavailable in local dev.</p></dialog><script type="module" src="/_astro/Search.astro_astro_type_script_index_1_lang.6CzpQ-18.js"></script><button class="menu-toggle" aria-label="Menu" aria-expanded="false" aria-controls="mobile-menu" data-astro-cid-hkbrpulz><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true" data-astro-cid-hkbrpulz><path d="M4 7h16M4 12h16M4 17h16" data-astro-cid-hkbrpulz></path></svg></button></div></div><div id="mobile-menu" hidden data-astro-cid-hkbrpulz><a href="/" data-astro-cid-hkbrpulz>Home</a><a href="/quickstart/" data-astro-cid-hkbrpulz>Start</a><a href="/how-to/ai-assistants/" data-astro-cid-hkbrpulz>AI</a><span class="menu-role" data-astro-cid-hkbrpulz>Learn</span><a href="/how-to/" data-astro-cid-hkbrpulz>How-to</a><a href="/tutorials/" data-astro-cid-hkbrpulz>Tutorials</a><span class="menu-role" data-astro-cid-hkbrpulz>Reference</span><a href="/access/" data-astro-cid-hkbrpulz>Access</a><a href="/data/" data-astro-cid-hkbrpulz>Data</a><a href="/api/" aria-current="page" data-astro-cid-hkbrpulz>API</a><a class="menu-site-link" href="https://openalex.org" target="_blank" rel="noopener" data-astro-cid-hkbrpulz>OpenAlex App <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14,3V5H17.59L7.76,14.83L9.17,16.24L19,6.41V10H21V3M19,19H5V5H12V3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V12H19V19Z"></path></svg></a></div></header><div class="layout" data-astro-cid-hkbrpulz><nav class="rail" aria-label="Primary" data-astro-cid-ekafmyw5><div class="rail-scroll" data-astro-cid-ekafmyw5><div class="sect" data-astro-cid-ekafmyw5><a href="/" class="item" data-tip-title="Home" data-tip-desc="Table of contents" data-astro-cid-ekafmyw5><span class="pill" data-astro-cid-ekafmyw5><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12,3L2,12H5V20H10V14H14V20H19V12H22L12,3M12,5.69L17,10.19V18H16V12H8V18H7V10.19L12,5.69Z"></path></svg></span><span class="label" data-astro-cid-ekafmyw5>Home</span></a><a href="/quickstart/" class="item" data-tip-title="Start" data-tip-desc="Five-minute intro tutorial" data-astro-cid-ekafmyw5><span class="pill" data-astro-cid-ekafmyw5><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.13 22.19L11.5 18.36C13.07 17.78 14.54 17 15.9 16.09L13.13 22.19M5.64 12.5L1.81 10.87L7.91 8.1C7 9.46 6.22 10.93 5.64 12.5M19.22 4C19.5 4 19.75 4 19.96 4.05C20.13 5.44 19.94 8.3 16.66 11.58C14.96 13.29 12.93 14.6 10.65 15.47L8.5 13.37C9.42 11.06 10.73 9.03 12.42 7.34C15.18 4.58 17.64 4 19.22 4M19.22 2C17.24 2 14.24 2.69 11 5.93C8.81 8.12 7.5 10.53 6.65 12.64C6.37 13.39 6.56 14.21 7.11 14.77L9.24 16.89C9.62 17.27 10.13 17.5 10.66 17.5C10.89 17.5 11.13 17.44 11.36 17.35C13.5 16.53 15.88 15.19 18.07 13C23.73 7.34 21.61 2.39 21.61 2.39S20.7 2 19.22 2M14.54 9.46C13.76 8.68 13.76 7.41 14.54 6.63S16.59 5.85 17.37 6.63C18.14 7.41 18.15 8.68 17.37 9.46C16.59 10.24 15.32 10.24 14.54 9.46M8.88 16.53L7.47 15.12L8.88 16.53M6.24 22L9.88 18.36C9.54 18.27 9.21 18.12 8.91 17.91L4.83 22H6.24M2 22H3.41L8.18 17.24L6.76 15.83L2 20.59V22M2 19.17L6.09 15.09C5.88 14.79 5.73 14.47 5.64 14.12L2 17.76V19.17Z"></path></svg></span><span class="label" data-astro-cid-ekafmyw5>Start</span></a><a href="/how-to/ai-assistants/" class="item" data-tip-title="AI" data-tip-desc="Use OpenAlex in Claude and other AI assistants" data-astro-cid-ekafmyw5><span class="pill" data-astro-cid-ekafmyw5><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M19,1L17.74,3.75L15,5L17.74,6.26L19,9L20.25,6.26L23,5L20.25,3.75M9,4L6.5,9.5L1,12L6.5,14.5L9,20L11.5,14.5L17,12L11.5,9.5M19,15L17.74,17.74L15,19L17.74,20.25L19,23L20.25,20.25L23,19L20.25,17.74"></path></svg></span><span class="label" data-astro-cid-ekafmyw5>AI</span></a></div><div class="divider" aria-hidden="true" data-astro-cid-ekafmyw5></div><div class="sect" data-astro-cid-ekafmyw5><a href="/how-to/" class="item" data-tip-title="How-to" data-tip-desc="Short, simple answers" data-astro-cid-ekafmyw5><span class="pill" data-astro-cid-ekafmyw5><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M11,18H13V16H11V18M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,6A4,4 0 0,0 8,10H10A2,2 0 0,1 12,8A2,2 0 0,1 14,10C14,12 11,11.75 11,15H13C13,12.75 16,12.5 16,10A4,4 0 0,0 12,6Z"></path></svg></span><span class="label" data-astro-cid-ekafmyw5>How-to</span></a><a href="/tutorials/" class="item" data-tip-title="Tutorials" data-tip-desc="Longer, step-by-step guides" data-astro-cid-ekafmyw5><span class="pill" data-astro-cid-ekafmyw5><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20,17A2,2 0 0,0 22,15V4A2,2 0 0,0 20,2H9.46C9.81,2.61 10,3.3 10,4H20V15H11V17M15,7V9H9V22H7V16H5V22H3V14H1.5V9A2,2 0 0,1 3.5,7H15M8,4A2,2 0 0,1 6,6A2,2 0 0,1 4,4A2,2 0 0,1 6,2A2,2 0 0,1 8,4Z"></path></svg></span><span class="label" data-astro-cid-ekafmyw5>Tutorials</span></a></div><div class="divider" aria-hidden="true" data-astro-cid-ekafmyw5></div><div class="sect" data-astro-cid-ekafmyw5><a href="/access/" class="item" data-tip-title="Access" data-tip-desc="Getting data in and out" data-astro-cid-ekafmyw5><span class="pill" data-astro-cid-ekafmyw5><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M2 12H4V17H20V12H22V17C22 18.11 21.11 19 20 19H4C2.9 19 2 18.11 2 17V12M12 15L17.55 9.54L16.13 8.13L13 11.25V2H11V11.25L7.88 8.13L6.46 9.55L12 15Z"></path></svg></span><span class="label" data-astro-cid-ekafmyw5>Access</span></a><a href="/data/" class="item" data-tip-title="Data" data-tip-desc="Contents and construction" data-astro-cid-ekafmyw5><span class="pill" data-astro-cid-ekafmyw5><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M11,13.5V21.5H3V13.5H11M9,15.5H5V19.5H9V15.5M12,2L17.5,11H6.5L12,2M12,5.86L10.08,9H13.92L12,5.86M17.5,13C20,13 22,15 22,17.5C22,20 20,22 17.5,22C15,22 13,20 13,17.5C13,15 15,13 17.5,13M17.5,15A2.5,2.5 0 0,0 15,17.5A2.5,2.5 0 0,0 17.5,20A2.5,2.5 0 0,0 20,17.5A2.5,2.5 0 0,0 17.5,15Z"></path></svg></span><span class="label" data-astro-cid-ekafmyw5>Data</span></a><a href="/api/" class="item" aria-current="page" data-tip-title="API" data-tip-desc="Automated access" data-astro-cid-ekafmyw5><span class="pill" data-astro-cid-ekafmyw5><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12,8A4,4 0 0,1 16,12A4,4 0 0,1 12,16A4,4 0 0,1 8,12A4,4 0 0,1 12,8M12,10A2,2 0 0,0 10,12A2,2 0 0,0 12,14A2,2 0 0,0 14,12A2,2 0 0,0 12,10M10,22C9.75,22 9.54,21.82 9.5,21.58L9.13,18.93C8.5,18.68 7.96,18.34 7.44,17.94L4.95,18.95C4.73,19.03 4.46,18.95 4.34,18.73L2.34,15.27C2.21,15.05 2.27,14.78 2.46,14.63L4.57,12.97L4.5,12L4.57,11L2.46,9.37C2.27,9.22 2.21,8.95 2.34,8.73L4.34,5.27C4.46,5.05 4.73,4.96 4.95,5.05L7.44,6.05C7.96,5.66 8.5,5.32 9.13,5.07L9.5,2.42C9.54,2.18 9.75,2 10,2H14C14.25,2 14.46,2.18 14.5,2.42L14.87,5.07C15.5,5.32 16.04,5.66 16.56,6.05L19.05,5.05C19.27,4.96 19.54,5.05 19.66,5.27L21.66,8.73C21.79,8.95 21.73,9.22 21.54,9.37L19.43,11L19.5,12L19.43,13L21.54,14.63C21.73,14.78 21.79,15.05 21.66,15.27L19.66,18.73C19.54,18.95 19.27,19.04 19.05,18.95L16.56,17.95C16.04,18.34 15.5,18.68 14.87,18.93L14.5,21.58C14.46,21.82 14.25,22 14,22H10M11.25,4L10.88,6.61C9.68,6.86 8.62,7.5 7.85,8.39L5.44,7.35L4.69,8.65L6.8,10.2C6.4,11.37 6.4,12.64 6.8,13.8L4.68,15.36L5.43,16.66L7.86,15.62C8.63,16.5 9.68,17.14 10.87,17.38L11.24,20H12.76L13.13,17.39C14.32,17.14 15.37,16.5 16.14,15.62L18.57,16.66L19.32,15.36L17.2,13.81C17.6,12.64 17.6,11.37 17.2,10.2L19.31,8.65L18.56,7.35L16.15,8.39C15.38,7.5 14.32,6.86 13.12,6.62L12.75,4H11.25Z"></path></svg></span><span class="label" data-astro-cid-ekafmyw5>API</span></a></div></div><div class="rail-foot" data-astro-cid-ekafmyw5><a href="https://openalex.org" class="item" data-tip-title="App" data-tip-desc="Jump to openalex.org" data-astro-cid-ekafmyw5><span class="pill" data-astro-cid-ekafmyw5><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14,3V5H17.59L7.76,14.83L9.17,16.24L19,6.41V10H21V3M19,19H5V5H12V3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V12H19V19Z"></path></svg></span><span class="label" data-astro-cid-ekafmyw5>App</span></a></div><div class="rail-tip" role="tooltip" hidden data-astro-cid-ekafmyw5><span class="rail-tip-desc" data-astro-cid-ekafmyw5></span></div></nav><script type="module">var e=document.querySelector(`.rail`),t=document.querySelector(`.rail-tip`);if(e&&t){let n=t.querySelector(`.rail-tip-desc`),r,i=()=>{clearTimeout(r),t.hidden=!0};for(let a of e.querySelectorAll(`[data-tip-title]`)){let e=()=>{clearTimeout(r),r=window.setTimeout(()=>{n.textContent=a.dataset.tipDesc??``,`tipExt`in a.dataset&&n.insertAdjacentHTML(`beforeend`,`<svg width="11" height="11" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14,3V5H17.59L7.76,14.83L9.17,16.24L19,6.41V10H21V3M19,19H5V5H12V3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V12H19V19Z"/></svg>`),t.hidden=!1;let e=a.getBoundingClientRect();t.style.left=`${e.right+8}px`;let r=Math.min(Math.max(8,e.top+e.height/2-t.offsetHeight/2),window.innerHeight-t.offsetHeight-8);t.style.top=`${r}px`},100)};a.addEventListener(`mouseenter`,e),a.addEventListener(`mouseleave`,i),a.addEventListener(`focus`,e),a.addEventListener(`blur`,i),a.addEventListener(`click`,i)}}</script><main class="wide" data-astro-cid-hkbrpulz><div class="shell" data-astro-cid-b4hyvnpz><aside data-astro-cid-wv7whodv><nav aria-label="Section pages" data-tab="api" data-astro-cid-wv7whodv><div class="group" data-astro-cid-wv7whodv><a href="/api/" data-astro-cid-wv7whodv>Overview</a><a href="/api/authentication/" data-astro-cid-wv7whodv>Authentication</a><a href="/api/errors/" data-astro-cid-wv7whodv>Error Handling</a><a href="/api/llm-quick-reference/" data-astro-cid-wv7whodv>LLM Quick Reference</a></div><div class="group" data-astro-cid-wv7whodv><span class="group-label" data-astro-cid-wv7whodv>Querying</span><a href="/api/filtering/" data-astro-cid-wv7whodv>Filter</a><a href="/api/searching/" data-astro-cid-wv7whodv>Search</a><a href="/api/semantic-search/" data-astro-cid-wv7whodv>Semantic Search</a><a href="/api/sorting/" data-astro-cid-wv7whodv>Sort</a><a href="/api/grouping/" data-astro-cid-wv7whodv>Group</a><a href="/api/paging/" data-astro-cid-wv7whodv>Page through Results</a><a href="/api/selecting-fields/" data-astro-cid-wv7whodv>Select Fields</a><a href="/api/get-single-entities/" data-astro-cid-wv7whodv>Get Singleton</a><a href="/api/autocomplete/" data-astro-cid-wv7whodv>Autocomplete</a><a href="/api/oql/" data-astro-cid-wv7whodv>OQL API</a></div><div class="group" data-astro-cid-wv7whodv><span class="group-label" data-astro-cid-wv7whodv>Endpoints</span><a href="/api/endpoints/" aria-current="page" data-astro-cid-wv7whodv>Overview</a></div><div class="group" data-astro-cid-wv7whodv><span class="group-label" data-astro-cid-wv7whodv>Curation &amp; special</span><a href="/api/author-curation/" data-astro-cid-wv7whodv>Author Curation</a><a href="/api/collections/" data-astro-cid-wv7whodv>Collections</a><a href="/api/alerts/" data-astro-cid-wv7whodv>Alerts and saved searches</a><a href="/api/tag-aboutness/" data-astro-cid-wv7whodv>Tag Aboutness</a></div><div class="group" data-astro-cid-wv7whodv><span class="group-label" data-astro-cid-wv7whodv>Reference</span><a href="/api/deprecations/" data-astro-cid-wv7whodv>Deprecations</a></div></nav></aside><!-- Sidebar scroll persistence (Cursor parity, oxjob #354): each full page load
     resets the nav's scroll, so save it to sessionStorage (per tab, like
     Cursor's docs-scroll-<section> keys) and restore on the next load. Must be
     is:inline and sit right after the <nav> markup: it then runs during HTML
     parse, after the blocking stylesheets but before first paint, so the
     restore never flickers. --><script>
  (() => {
    const nav = document.querySelector('aside > nav[data-tab]');
    if (!nav) return;
    const key = 'sidebar-scroll-' + nav.dataset.tab;
    let saved = null;
    try {
      saved = sessionStorage.getItem(key);
    } catch {}
    if (saved !== null) {
      nav.scrollTop = parseInt(saved, 10) || 0;
    } else {
      // First entry in this tab (deep link, new tab): show the reader where
      // they are instead of the top of the drawer.
      const active = nav.querySelector('a[aria-current="page"]');
      if (active) active.scrollIntoView({ block: 'nearest' });
    }
    nav.addEventListener(
      'scroll',
      () => {
        try {
          sessionStorage.setItem(key, String(nav.scrollTop));
        } catch {}
      },
      { passive: true }
    );
  })();
</script><div class="content" data-astro-cid-b4hyvnpz><div class="columns" data-astro-cid-b4hyvnpz><div class="main-col" data-astro-cid-b4hyvnpz><article class="prose" data-pagefind-body data-pagefind-meta="eyebrow:API › Endpoints" data-astro-cid-tlodkskj><header class="page-head" data-astro-cid-b2i3gsw2><div class="crumb-slot" data-astro-cid-b2i3gsw2><nav class="breadcrumbs" aria-label="Breadcrumb" data-pagefind-ignore data-astro-cid-vx4iavld><ol data-astro-cid-vx4iavld><li data-astro-cid-vx4iavld><a href="/api/" data-astro-cid-vx4iavld><svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12,8A4,4 0 0,1 16,12A4,4 0 0,1 12,16A4,4 0 0,1 8,12A4,4 0 0,1 12,8M12,10A2,2 0 0,0 10,12A2,2 0 0,0 12,14A2,2 0 0,0 14,12A2,2 0 0,0 12,10M10,22C9.75,22 9.54,21.82 9.5,21.58L9.13,18.93C8.5,18.68 7.96,18.34 7.44,17.94L4.95,18.95C4.73,19.03 4.46,18.95 4.34,18.73L2.34,15.27C2.21,15.05 2.27,14.78 2.46,14.63L4.57,12.97L4.5,12L4.57,11L2.46,9.37C2.27,9.22 2.21,8.95 2.34,8.73L4.34,5.27C4.46,5.05 4.73,4.96 4.95,5.05L7.44,6.05C7.96,5.66 8.5,5.32 9.13,5.07L9.5,2.42C9.54,2.18 9.75,2 10,2H14C14.25,2 14.46,2.18 14.5,2.42L14.87,5.07C15.5,5.32 16.04,5.66 16.56,6.05L19.05,5.05C19.27,4.96 19.54,5.05 19.66,5.27L21.66,8.73C21.79,8.95 21.73,9.22 21.54,9.37L19.43,11L19.5,12L19.43,13L21.54,14.63C21.73,14.78 21.79,15.05 21.66,15.27L19.66,18.73C19.54,18.95 19.27,19.04 19.05,18.95L16.56,17.95C16.04,18.34 15.5,18.68 14.87,18.93L14.5,21.58C14.46,21.82 14.25,22 14,22H10M11.25,4L10.88,6.61C9.68,6.86 8.62,7.5 7.85,8.39L5.44,7.35L4.69,8.65L6.8,10.2C6.4,11.37 6.4,12.64 6.8,13.8L4.68,15.36L5.43,16.66L7.86,15.62C8.63,16.5 9.68,17.14 10.87,17.38L11.24,20H12.76L13.13,17.39C14.32,17.14 15.37,16.5 16.14,15.62L18.57,16.66L19.32,15.36L17.2,13.81C17.6,12.64 17.6,11.37 17.2,10.2L19.31,8.65L18.56,7.35L16.15,8.39C15.38,7.5 14.32,6.86 13.12,6.62L12.75,4H11.25Z"></path></svg>API</a></li><li data-astro-cid-vx4iavld><svg class="sep" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" data-astro-cid-vx4iavld><polyline points="9 18 15 12 9 6" data-astro-cid-vx4iavld></polyline></svg><span data-astro-cid-vx4iavld>Endpoints</span></li></ol></nav></div><h1 data-astro-cid-b2i3gsw2>Endpoints Overview</h1></header><p>Every OpenAlex entity has a REST endpoint under <code>https://api.openalex.org/</code>. They all work the same way: request the plural path for a <strong>list</strong> (filter, search, sort, group, page), or add an ID for a <strong>single</strong> entity. The query mechanics are the same across every endpoint — see <a href="/api/filtering/">Filtering</a>, <a href="/api/searching/">Searching</a>, <a href="/api/sorting/">Sorting</a>, <a href="/api/grouping/">Grouping</a>, <a href="/api/paging/">Paging</a>, and <a href="/api/selecting-fields/">Selecting fields</a>.</p>
<p>This page is the index. What each entity <em>is</em>, and what every field on it <em>means</em>, lives on its <a href="/data/">Entities</a> page — follow the links.</p>
<h2 id="entity-endpoints">Entity endpoints</h2>













































<table><thead><tr><th>Endpoint</th><th>List / single</th><th>What it returns</th></tr></thead><tbody><tr><td><code>/works</code></td><td><code>/works</code> · <code>/works/W…</code></td><td><a href="/data/works/">Works</a> — scholarly documents</td></tr><tr><td><code>/authors</code></td><td><code>/authors</code> · <code>/authors/A…</code></td><td><a href="/data/authors/">Authors</a> — the people who create works</td></tr><tr><td><code>/sources</code></td><td><code>/sources</code> · <code>/sources/S…</code></td><td><a href="/data/sources/">Sources</a> — journals, conferences, repositories</td></tr><tr><td><code>/institutions</code></td><td><code>/institutions</code> · <code>/institutions/I…</code></td><td><a href="/data/institutions/">Institutions</a> — universities, companies, and more</td></tr><tr><td><code>/publishers</code></td><td><code>/publishers</code> · <code>/publishers/P…</code></td><td><a href="/data/publishers/">Publishers</a> — the organizations behind sources</td></tr><tr><td><code>/funders</code></td><td><code>/funders</code> · <code>/funders/F…</code></td><td><a href="/data/funders/">Funders</a> — research funders</td></tr><tr><td><code>/awards</code></td><td><code>/awards</code> · <code>/awards/G…</code></td><td><a href="/data/awards/">Awards</a> — specific grants</td></tr></tbody></table>
<h2 id="component-endpoints">Component endpoints</h2>
<p><a href="/data/component/">Component</a> entities are parts of a work. They have no minted OpenAlex ID, but two of them have their own list endpoints; locations are addressed by a namespaced id (<code>doi:…</code>, <code>pmh:…</code>, <code>pmid:…</code>, <code>mag:…</code>) rather than a letter-prefixed one.</p>




















<table><thead><tr><th>Endpoint</th><th>List / single</th><th>What it returns</th></tr></thead><tbody><tr><td><code>/locations</code></td><td><code>/locations</code> · <code>/locations/doi:…</code></td><td><a href="/data/locations/">Locations</a> — every harvested copy of a work, one row per copy</td></tr><tr><td><code>/raw-affiliation-strings</code></td><td><code>/raw-affiliation-strings</code></td><td><a href="/data/raw-affiliation-strings/">Raw affiliation strings</a> — distinct affiliation strings as printed</td></tr></tbody></table>
<h2 id="aboutness-endpoints">Aboutness endpoints</h2>









































<table><thead><tr><th>Endpoint</th><th>What it returns</th></tr></thead><tbody><tr><td><code>/topics</code></td><td><a href="/data/topics/">Topics</a> — ~4,500 fine-grained subjects</td></tr><tr><td><code>/subfields</code></td><td><a href="/data/subfields/">Subfields</a> — 252 mid-level subjects</td></tr><tr><td><code>/fields</code></td><td><a href="/data/fields/">Fields</a> — 26 broad disciplines</td></tr><tr><td><code>/domains</code></td><td><a href="/data/domains/">Domains</a> — the 4 top-level branches</td></tr><tr><td><code>/keywords</code></td><td><a href="/data/keywords/">Keywords</a> — short topic-derived phrases</td></tr><tr><td><code>/sdgs</code></td><td><a href="/data/sdgs/">SDGs</a> — the 17 UN Sustainable Development Goals</td></tr><tr><td><code>/study-designs</code></td><td><a href="/data/study-designs/">Study designs</a>: the 7 designs a work’s research can have (randomized controlled trial, systematic review, …)</td></tr><tr><td><code>/concepts</code></td><td><a href="/data/concepts/">Concepts</a> <em>(deprecated — use Topics)</em></td></tr></tbody></table>
<h2 id="vocabulary-endpoints">Vocabulary endpoints</h2>













































<table><thead><tr><th>Endpoint</th><th>What it returns</th></tr></thead><tbody><tr><td><code>/work-types</code></td><td><a href="/data/work-types/">Work types</a></td></tr><tr><td><code>/source-types</code></td><td><a href="/data/source-types/">Source types</a></td></tr><tr><td><code>/institution-types</code></td><td><a href="/data/institution-types/">Institution types</a></td></tr><tr><td><code>/countries</code></td><td><a href="/data/countries/">Countries</a></td></tr><tr><td><code>/continents</code></td><td><a href="/data/continents/">Continents</a></td></tr><tr><td><code>/languages</code></td><td><a href="/data/languages/">Languages</a></td></tr><tr><td><code>/licenses</code></td><td><a href="/data/licenses/">Licenses</a></td></tr><tr><td><code>/indexes</code></td><td><a href="/data/indexes/">Indexes</a></td></tr><tr><td><code>/source-lists</code></td><td><a href="/data/source-lists/">Source lists</a></td></tr></tbody></table>
<h2 id="special-purpose-endpoints">Special-purpose endpoints</h2>





























<table><thead><tr><th>Endpoint</th><th>What it does</th></tr></thead><tbody><tr><td><code>/autocomplete/{entity}</code></td><td>Fast type-ahead suggestions — see <a href="/api/autocomplete/">Autocomplete</a></td></tr><tr><td><code>/text</code></td><td>Tag arbitrary text with topics and keywords — see <a href="/api/tag-aboutness/">Tag Aboutness</a></td></tr><tr><td><code>/collections</code></td><td><a href="/data/collections/">Collections</a>: list the public ones (no key) and your own (filter, search, sort, group), create, read, share and change them and their members (no credits) — see <a href="/api/collections/">Collections API</a></td></tr><tr><td><code>/curations</code></td><td>Submit corrections <em>(on <code>user.openalex.org</code>)</em> — see <a href="/api/author-curation/">Author curation</a> and <a href="/data/curations/">Curations</a></td></tr><tr><td><code>/saved-searches</code></td><td>Save searches and set email alerts for new works (no credits) — see <a href="/api/alerts/">Alerts and saved searches</a></td></tr></tbody></table>
<h2 id="oql-and-oqo">OQL and OQO</h2>
<p>Beyond REST, OpenAlex answers the same queries through <a href="/access/oql/">OQL</a> (a readable query language) and its machine-readable twin <a href="/access/oqo-schema/">OQO</a>. Every query surface — REST, OQL, the web builder — transpiles to the same OQO under the hood; see <a href="/access/querying/">Querying</a>.</p><div class="article-foot" data-pagefind-ignore data-astro-cid-tlodkskj><p class="updated" data-astro-cid-wytylmfw>Last updated <time datetime="2026-10-03" data-localize-date data-astro-cid-wytylmfw>October 3, 2026</time></p><!-- is:inline and adjacent to the markup, so it runs during parse (before
     first paint) and the en-US fallback never flashes in a French browser. --><script>
  (() => {
    const el = document.querySelector('time[data-localize-date]');
    if (!el) return;
    const [y, m, d] = el.dateTime.split('-').map(Number);
    if (!y || !m || !d) return;
    // Build the date in LOCAL time. `new Date('2026-08-11')` parses as UTC
    // midnight, which renders as the 10th for every reader behind Greenwich.
    const local = new Date(y, m - 1, d);
    const locales = navigator.languages?.length ? navigator.languages : undefined;
    try {
      el.textContent = local.toLocaleDateString(locales, {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
      });
    } catch {
      // Bad Accept-Language → RangeError. Keep the server's en-US string.
    }
  })();
</script><a class="md-link" href="/api/endpoints.md" data-astro-cid-tlodkskj>View as Markdown</a></div></article></div><div class="rail-col" data-astro-cid-b4hyvnpz><div class="rail" data-astro-cid-tlodkskj><div class="rail-head" data-astro-cid-tlodkskj>On this page</div><nav class="toc" aria-label="On this page" data-astro-cid-tlodkskj><a href="#entity-endpoints" data-astro-cid-tlodkskj>Entity endpoints</a><a href="#component-endpoints" data-astro-cid-tlodkskj>Component endpoints</a><a href="#aboutness-endpoints" data-astro-cid-tlodkskj>Aboutness endpoints</a><a href="#vocabulary-endpoints" data-astro-cid-tlodkskj>Vocabulary endpoints</a><a href="#special-purpose-endpoints" data-astro-cid-tlodkskj>Special-purpose endpoints</a><a href="#oql-and-oqo" data-astro-cid-tlodkskj>OQL and OQO</a></nav></div></div></div></div></div></main></div><script type="module">var e=`<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>`;for(let t of document.querySelectorAll(`.prose h2[id], .prose h3[id], .prose h4[id]`)){let n=document.createElement(`a`);n.className=`h-anchor`,n.href=`#`+t.id,n.setAttribute(`aria-label`,`Link to this section`),n.innerHTML=e,t.appendChild(n),t.classList.add(`has-anchor`),t.addEventListener(`click`,e=>{e.target.closest(`a`)||(location.hash=t.id)})}var t=document.querySelector(`.menu-toggle`),n=document.getElementById(`mobile-menu`);t&&n&&(t.addEventListener(`click`,()=>{let e=n.classList.toggle(`open`);n.hidden=!1,t.setAttribute(`aria-expanded`,String(e))}),document.addEventListener(`keydown`,e=>{e.key===`Escape`&&n.classList.contains(`open`)&&(n.classList.remove(`open`),t.setAttribute(`aria-expanded`,`false`))}));</script></body></html>
