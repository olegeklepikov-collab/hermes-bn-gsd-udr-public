> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Crossref: content-negotiation

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


<div id="nav2019" class="nav-container nav-container--hidden">

<div class="menu-wrap">

- <div class="nav-burger">

  </div>

- Menu

</div>

<div class="social-icons">

<a href="https://bsky.app/profile/crossref.bsky.social" aria-label="Bluesky" title="Bluesky"><em></em></a> <a href="https://mastodon.online/@crossref" rel="me" aria-label="Mastodon" title="Mastodon"><em></em></a> <a href="https://www.linkedin.com/company/crossref" aria-label="LinkedIn" title="LinkedIn"><em></em></a> <a href="https://www.youtube.com/c/CrossrefVideos" aria-label="YouTube" title="YouTube"><em></em></a> <a href="https://gitlab.com/crossref" aria-label="GitLab" title="GitLab"><em></em></a> <a href="https://community.crossref.org/" aria-label="Community forum" title="Community forum"><em></em></a>

</div>

<div class="nav-wrapper dark-grey">

<div class="nav-outer-flex">

<div class="nav-flex">

<div class="nav-col first-col order-1 mobile-home-btn">

- <a href="/" class="home-nav normal"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibmF2LWljb24iIHZpZXdib3g9IjAgMCA1MCA1MCI+PHBhdGggY2xhc3M9ImhvbWUiIGQ9Ik0xLjMgMTcuMSAyNS4yLjBsMjMuNSAxNy4xVjUwSDMxLjZWMzIuOUgxOC4yTDE4LjQgNTBIMS4zVjE3LjF6IiAvPjwvc3ZnPg==" class="nav-icon" /> <span>Home</span></a>

</div>

<div class="nav-col first-col order-2">

- <a href="/" class="home-nav normal"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibmF2LWljb24iIHZpZXdib3g9IjAgMCA1MCA1MCI+PHBhdGggY2xhc3M9ImhvbWUiIGQ9Ik0xLjMgMTcuMSAyNS4yLjBsMjMuNSAxNy4xVjUwSDMxLjZWMzIuOUgxOC4yTDE4LjQgNTBIMS4zVjE3LjF6IiAvPjwvc3ZnPg==" class="nav-icon" /> <span>Home</span></a>
- <a href="/membership/" class="apply-nav reverse"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibmF2LWljb24iIHZpZXdib3g9IjAgMCA1MCA1MCI+PHBhdGggY2xhc3M9ImFwcGx5IiBkPSJNMjAuNCAyMS4xdjQuMUw3LjIgMTkuOHYtNC4xbDEzLjIgNS40ek03LjIgMjkuM2wxMy4yIDUuM3YtNC4xTDcuMiAyNS4ydjQuMXpNNDIuOCAxNS43IDI5LjYgMjF2NC4xbDEzLjItNS4zVjE1Ljd6bTAgMTMuNnYtNC4xbC0xMy4yIDUuM3Y0LjFsMTMuMi01LjN6TTQ1LjEgNy45bC0xOC41IDcuNnYyNy4xTDQ1LjEgMzVWNy45ek00LjkgMzVsMTguOSA3LjdWMTUuNkw0LjkgNy45VjM1ek00OC43IDIuNWMuNi40IDEgMS4xIDEgMS45djMyLjFjMCAuOS0uNiAxLjgtMS41IDIuMWwtMjIuNCA5cy0uMS4wLS4xLjBjLS4zLjEtLjUuMi0uOC4ycy0uNS0uMS0uOC0uMkgyNGwtMjIuNC05Yy0uOS0uNC0xLjQtMS4yLTEuNC0yLjFWNC40YzAtLjguNC0xLjUgMS0xLjlDMiAyLjEgMi44IDIgMy41IDIuM0wyNSAxMC45bDIxLjUtOC42QzQ3LjIgMiA0OCAyLjEgNDguNyAyLjUiIC8+PC9zdmc+" class="nav-icon" /> <span>Join</span></a>
- <a href="/members-area/" class="members-nav normal"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibmF2LWljb24iIHZpZXdib3g9IjAgMCA1MCA1MCI+PHBhdGggY2xhc3M9Im1lbWJlcnMiIGQ9Ik0zMS4xIDI3LjFjLS4zLjAtLjYuMC0uOS4xLTEuNi41LTMuNC45LTUuMi45cy0zLjYtLjMtNS4yLS45Yy0uMy0uMS0uNi0uMS0uOS0uMS03LjkuMC0xNC4zIDguNC0xNC4yIDE2LjMuMCAzLjMgMi44IDYgNi4xIDZoMjguNGMzLjMuMCA2LjEtMi43IDYuMS02QzQ1LjQgMzUuNSAzOSAyNy4xIDMxLjEgMjcuMXpNMjUgMjVjNi43LjAgMTIuMi01LjUgMTIuMi0xMi4yUzMxLjcuNiAyNSAuNiAxMi44IDYuMSAxMi44IDEyLjggMTguMyAyNSAyNSAyNXoiIC8+PC9zdmc+" class="nav-icon" /> <span>Members</span></a>
- <a href="/documentation/" class="documentation-nav reverse"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibmF2LWljb24iIHZpZXdib3g9IjAgMCA1MCA1MCI+PHBhdGggY2xhc3M9InN1cHBvcnQiIGQ9Ik0xNi4zIDMzLjRjLS4yLjAtLjQuMC0uNS4xLTEgLjMtMi4xLjUtMy4yLjVzLTIuMi0uMi0zLjItLjVjLS4yLS4xLS40LS4xLS41LS4xLTQuOC4wLTguNyAzLjktOC43IDguNy4wIDIgMS43IDMuNyAzLjcgMy43aDE3LjNjMiAwIDMuNy0xLjYgMy43LTMuN0MyNSAzNy4zIDIxLjEgMzMuNCAxNi4zIDMzLjR6bS0zLjctMi41YzQuMS4wIDcuNC0zLjMgNy40LTcuNHMtMy4zLTcuNC03LjQtNy40LTcuNCAzLjMtNy40IDcuNCAzLjMgNy40IDcuNCA3LjR6TTQ2IDYuMkgxNi4zYy0yIDAtMy43IDEuNy0zLjcgMy44djMuNmMxLjguMCAzLjUuNSA0LjkgMS40di0zLjloMjcuMnYyMi4zaC00Ljl2LTQuOWgtOS45djQuOUgyNGMxLjUgMS4zIDIuNiAzIDMuMSA0LjlINDZjMiAwIDMuNy0xLjcgMy43LTMuOFYxMGMwLTIuMS0xLjYtMy44LTMuNy0zLjh6IiAvPjwvc3ZnPg==" class="nav-icon" /> <span>Documentation</span></a>
- <a href="https://community.crossref.org" class="forum-nav normal"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibmF2LWljb24iIHZpZXdib3g9IjAgMCA1MCA1MCI+PHBhdGggY2xhc3M9ImZvcnVtIiBkPSJNNDYuMTgxIDM2LjE4OUM0OC41NjggMzMuODYgNTAgMzAuOTM4IDUwIDI3Ljc1YzAtNi44NzUtNi42NDEtMTIuNTU1LTE1LjI5NS0xMy41Ny0yLjczNS00Ljk1LTkuMTU4LTguNDMtMTYuNjQ5LTguNDNDOC4wODIgNS43NS4wIDExLjkwMy4wIDE5LjVjMCAzLjE4IDEuNDMyIDYuMTAyIDMuODE5IDguNDM5QzIuNDkxIDMwLjU3Ny41ODIgMzIuNjIzLjU0NyAzMi42NTcuMCAzMy4yMzMtLjE1NiAzNC4wNzUuMTY1IDM0LjgwNS40NzcgMzUuNTM2IDEuMjA3IDM2LjAwOSAyLjAwNSAzNi4wMDljNC42NDQuMCA4LjM5NC0xLjczNiAxMC44NjgtMy4zMzVDMTMuNjcyIDMyLjg1NSAxNC40OTcgMzIuOTkyIDE1LjMzOSAzMy4wOTVjMi43MjUgNC45MzMgOS4xMjMgOC40MDUgMTYuNjA1IDguNDA1QzMzLjc1IDQxLjUgMzUuNDg2IDQxLjI5NCAzNy4xMzUgNDAuOTE2IDM5LjYwOSA0Mi41MDUgNDMuMzUxIDQ0LjI1IDQ4LjAwMyA0NC4yNSA0OC44MDIgNDQuMjUgNDkuNTIzIDQzLjc3NyA0OS44NDQgNDMuMDQ3IDUwLjE1NiA0Mi4zMTYgNTAuMDA5IDQxLjQ3NCA0OS40NjIgNDAuODk4IDQ5LjQyNyA0MC44NzMgNDcuNTA5IDM4LjgyNyA0Ni4xODEgMzYuMTg5ek0xMi4wODMgMjguMjU3IDEwLjU5OSAyOS4yMTFjLTEuMjI0Ljc4Mi0yLjQ3NCAxLjQwMS0zLjc0MSAxLjgzOS4yMzQtLjQwNC40NjgtLjgzNC42OTQtMS4yNzJsMS4zNDYtMi42NzNMNi43NDUgMjVjLTEuMTcyLTEuMTUyLTIuNTc4LTMuMDM0LTIuNTc4LTUuNS4wLTUuMjE2IDYuMzYzLTkuNjI1IDEzLjg4OS05LjYyNVMzMS45NDQgMTQuMjg0IDMxLjk0NCAxOS41cy02LjM2MiA5LjYyNS0xMy44ODggOS42MjVDMTYuNjIzIDI5LjEyNSAxNS4xOTEgMjguOTYyIDEzLjgwMiAyOC42NDRMMTIuMDgzIDI4LjI1N3pNNDMuMjU1IDMzLjI1IDQxLjExMSAzNS4zNDdsMS4zNDYgMi42NzNDNDIuNjgyIDM4LjQ1OCA0Mi45MTcgMzguODg4IDQzLjE1MSAzOS4yOTEgNDEuODg0IDM4Ljg1MyA0MC42MzQgMzguMjM0IDM5LjQxIDM3LjQ1MkwzNy45MjUgMzYuNDk4IDM2LjE5OCAzNi44OTRDMzQuODA5IDM3LjIxMiAzMy4zNzcgMzcuMzc1IDMxLjk0NCAzNy4zNzVjLTQuNjg3LjAtOC44NzEtMS43MjctMTEuMzk3LTQuMjcxQzI5LjM0IDMyLjE3NiAzNi4xMTEgMjYuNDUyIDM2LjExMSAxOS41IDM2LjExMSAxOS4yMDggMzYuMDc2IDE4LjkyNCAzNi4wNSAxOC42NDFjNS41OTEgMS4yNDYgOS43ODMgNC44ODEgOS43ODMgOS4xMDkuMCAyLjQ2Ni0xLjQwNiA0LjM0OC0yLjU3OCA1LjV6IiAvPjwvc3ZnPg==" class="nav-icon" /> <span>Forum</span></a>
- <a href="/blog/" class="blog-nav normal"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibmF2LWljb24iIHZpZXdib3g9IjAgMCA1MCA1MCI+PHBhdGggY2xhc3M9ImJsb2ciIGQ9Ik0xMC41IDMzLjdjLTMuNC4wLTYuMiAyLjgtNi4yIDYuMi4wIDMuNCAyLjggNi4xIDYuMiA2LjFzNi4yLTIuOCA2LjItNi4xQzE2LjYgMzYuNCAxMy45IDMzLjcgMTAuNSAzMy43ek01IDE4Yy0uNC4wLS42LjMtLjYuNnY3LjhjMCAuNC4zLjYuNi42IDEwIDAgMTguMiA4LjIgMTguMiAxOC4yLjAuMy4zLjYuNi42aDcuOC4wYy40LjAuNi0uMy42LS42VjQ1QzMyLjEgMzAuMiAxOS45IDE4IDUgMTh6TTQ1LjggNDUuMUM0NS43IDIyLjcgMjcuNCA0LjUgNSA0LjVjLS40LjAtLjYuMy0uNi42djhjMCAuNC4zLjYuNi42IDE3LjQuMCAzMS41IDE0LjEgMzEuNSAzMS41LjAuMy4zLjYuNi42aDggMGMuMy4wLjYtLjMuNi0uNkw0NS44IDQ1LjF6IiAvPjwvc3ZnPg==" class="nav-icon" /> <span>Blog</span></a>
- <a href="/contact/" class="contact-nav normal"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibmF2LWljb24iIHZpZXdib3g9IjAgMCA1MCA1MCI+PHBhdGggY2xhc3M9ImNvbnRhY3QiIGQ9Ik00My45IDYuMkg2LjFjLTMuMi4wLTUuOSAyLjUtNS45IDUuN3YyNi40YzAgMy4xIDIuNiA1LjcgNS45IDUuN2gzNy44YzMuMi4wIDUuOS0yLjUgNS45LTUuN1YxMS44QzQ5LjggOC43IDQ3LjIgNi4yIDQzLjkgNi4yem0wIDMyLjdINi4xYy0uNS4wLS45LS4zLS45LS43VjE1LjNsMTcuMSAxNC41Yy40LjMgMi44IDIgNS40LjBsMTcuMS0xNC41djIyLjlDNDQuOCAzOC41IDQ0LjQgMzguOSA0My45IDM4Ljl6TTI1IDI1LjMgOC40IDExLjFoMzMuM0wyNSAyNS4zeiIgLz48L3N2Zz4=" class="nav-icon" /> <span>Contact</span></a>

</div>

<div class="nav-col mobile order-3">

## Get involved

<div class="plus-wrapper">

<div class="plus go-yellow">

</div>

<div class="minus go-yellow minus-1">

</div>

</div>

- <div class="child-mobile-arrow">

  </div>

- [Overview](https://www.crossref.org/community/)

- [Become a member](https://www.crossref.org/membership/)

- [Events](https://www.crossref.org/events/)

- [Service providers](https://www.crossref.org/community/service-providers/)

- [Special programs](https://www.crossref.org/community/special-programs/)

- [Working for you](https://www.crossref.org/community/working-for-you/)

- [Data citation](https://www.crossref.org/community/data-citation/)

- [Sponsors program](https://www.crossref.org/community/sponsors/)

- [Ambassadors](https://www.crossref.org/community/ambassadors/)

- [Working groups](https://www.crossref.org/working-groups/)

- [Code of conduct](https://www.crossref.org/code-of-conduct/)

- [Fees](https://www.crossref.org/fees/)

- [API Learning Hub](https://www.crossref.org/learning/)

</div>

<div class="nav-col mobile order-3">

## Find a service

<div class="plus-wrapper">

<div class="plus go-yellow">

</div>

<div class="minus go-yellow minus-1">

</div>

</div>

- <div class="child-mobile-arrow">

  </div>

- [Overview](https://www.crossref.org/services/)

- [Content Registration](https://www.crossref.org/services/content-registration/)

- [Metadata Retrieval](https://www.crossref.org/services/metadata-retrieval/)

- [Metadata Plus](https://www.crossref.org/services/metadata-retrieval/metadata-plus/)

- [Grant Linking System (GLS)](https://www.crossref.org/services/grant-linking-system/)

- [Research Organization Registry (ROR)](https://www.crossref.org/services/ror/)

- [Open Funder Registry (OFR)](https://www.crossref.org/services/funder-registry/)

- [Support for Reference Linking](https://www.crossref.org/services/reference-linking/)

- [Similarity Check](https://www.crossref.org/services/similarity-check/)

- [Cited-by](https://www.crossref.org/services/cited-by/)

- [Crossmark](https://www.crossref.org/services/crossmark/)

</div>

<div class="nav-col mobile order-3">

## Documentation

<div class="plus-wrapper">

<div class="plus go-yellow">

</div>

<div class="minus go-yellow minus-1">

</div>

</div>

- <div class="child-mobile-arrow">

  </div>

- [Overview](https://www.crossref.org/documentation/)

- [Setting up as a member](https://www.crossref.org/documentation/member-setup/)

- [The Research Nexus](https://www.crossref.org/documentation/research-nexus/)

- [Metadata principles and practices](https://www.crossref.org/documentation/principles-practices/)

- [Register and maintain your records](https://www.crossref.org/documentation/register-maintain-records/)

- [Schema library](https://www.crossref.org/documentation/schema-library/)

- [Reports](https://www.crossref.org/documentation/reports/)

- [Crossmark](https://www.crossref.org/documentation/crossmark/)

- [Cited-by](https://www.crossref.org/documentation/cited-by/)

- [Similarity Check](https://www.crossref.org/documentation/similarity-check/)

- [Metadata Retrieval](https://www.crossref.org/documentation/retrieve-metadata/)

</div>

<div class="nav-col mobile order-3">

## About us

<div class="plus-wrapper">

<div class="plus go-yellow">

</div>

<div class="minus go-yellow minus-1">

</div>

</div>

- <div class="child-mobile-arrow">

  </div>

- [Overview](https://www.crossref.org/about/)

- [Operations & sustainability](https://www.crossref.org/operations-and-sustainability/)

- [Board & governance](https://www.crossref.org/board-and-governance/)

- [Publications](https://www.crossref.org/publications/)

- [Strategic agenda and roadmap](https://www.crossref.org/strategy/)

- [Our truths](https://www.crossref.org/truths/)

- [Our people](https://www.crossref.org/people/)

- [Organisation chart](https://www.crossref.org/people/org-chart/)

- [Jobs](https://www.crossref.org/jobs/)

</div>

</div>

<div class="nav-flex posts">

<div class="nav-col">

<span class="latest-posts light-grey-text">Latest blog posts</span>

</div>

<div class="nav-col nav2019__post">

<img src="https://www.crossref.org//images/staff/luis-montilla-thumb.jpg" class="profile-pic" width="57" height="57" alt="Luis Montilla" />

<div class="nav2019__post-text">

##### 2026 October 06

### [How Grobid uses Crossref metadata to enrich bibliographic information](https://www.crossref.org/blog/how-grobid-uses-crossref-metadata-to-enrich-bibliographic-information/)

Crossref members register around 37,000 records daily. All this metadata is openly shared with the global scholarly community through our free APIs. We receive over two billion calls to our API each month, signalling its use by hundreds of tools and services worldwide, supporting the discovery and assessment of scholarly metadata. As part of a new series in our blog, we will spotlight the diversity of tools and integrations that rely on Crossref metadata to serve the scholarly community. In this initial post, we chat to Luca Foppiano, the developer and maintainer of Grobid1, to learn about how Grobid uses Crossref metadata to improve the extraction and enrichment of bibliographic information from scholarly PDFs.

</div>

<a href="/blog/how-grobid-uses-crossref-metadata-to-enrich-bibliographic-information/" class="nav2019__post-readmore">...Find out more</a>

</div>

<div class="nav-col nav2019__post">

<img src="https://www.crossref.org//images/staff/lucy-ofiesh.jpg" class="profile-pic" width="57" height="57" alt="Lucy Ofiesh" />

<div class="nav2019__post-text">

##### 2026 September 21

### [2026 board election slate](https://www.crossref.org/blog/2026-board-election-slate/)

On behalf of the Nominating Committee, I’m pleased to share the slate of candidates for the 2026 board election. Every active member organisation is invited to submit a ballot to elect the incoming board class.

</div>

<a href="/blog/2026-board-election-slate/" class="nav2019__post-readmore">...Find out more</a>

</div>

<div class="nav-col nav2019__post">

<img src="https://www.crossref.org//images/staff/lucy-ofiesh.jpg" class="profile-pic" width="57" height="57" alt="Lucy Ofiesh" />

<div class="nav2019__post-text">

##### 2026 September 17

### [July 2026 board meeting summary](https://www.crossref.org/blog/july-2026-board-meeting-summary/)

We’re providing a summary of the board’s July 2026 meeting. The July board meeting is our only in-person meeting. The board gathers for two days of strategic thinking and long-range planning, as well as conducting annual board business. This year, we focused on allocating surplus funds we have on hand to invest in a three-year project to redesign the content system. In a related discussion, we decided to lower content registration fees starting in 2027 because we’ve had a demonstrated history of generating surpluses, exceeding what we need to run Crossref. We also discussed the board structure, as part of our regular review of stakeholder governance. And we conducted annual board business, such as approving the audited financial statements and reviewed our risk register and mitigation plans.

The [resolutions are available](https://www.crossref.org/board-and-governance) on the dedicated section of our website, which also lists the members of the Board and offers further information about our governance.

We also managed to squeeze in watching a World Cup game over dinner.

</div>

<a href="/blog/july-2026-board-meeting-summary/" class="nav2019__post-readmore">...Find out more</a>

</div>

<div class="nav-col nav2019__post">

<img src="https://www.crossref.org//images/staff/martyn-rittman.jpg" class="profile-pic" width="57" height="57" alt="Martyn Rittman" />

<div class="nav2019__post-text">

##### 2026 September 15

### [Improving how funding connects to research outputs](https://www.crossref.org/blog/improving-how-funding-connects-to-research-outputs/)

Starting today, funder names deposited in Crossref metadata without an identifier will be matched to ROR IDs, to support an open and connected [Research Nexus](https://www.crossref.org/documentation/research-nexus/). Funding information is an increasingly important part of the scholarly record. The improved matching strategy supports researchers, funders, institutions, and meta-researchers, who rely on that information to understand how research is supported and what outcomes that support produces.

</div>

<a href="/blog/improving-how-funding-connects-to-research-outputs/" class="nav2019__post-readmore">...Find out more</a>

</div>

</div>

<div class="footer-colours">

</div>

</div>

</div>

<div class="logo">

<a href="https://www.crossref.org/" class="crossref-brand"><img src="https://www.crossref.org//img/crossref-logo-reverse.svg" class="site-logo" alt="Crossref logo" /></a>

</div>

</div>

<div class="site-header">

<div class="container-fluid site-header-inner">

<div class="menu-wrap">

- <div class="nav-burger">

  </div>

- Menu

</div>

<div class="social-icons">

<a href="https://bsky.app/profile/crossref.bsky.social" aria-label="Bluesky" title="Bluesky"><em></em></a> <a href="https://mastodon.online/@crossref" rel="me" aria-label="Mastodon" title="Mastodon"><em></em></a> <a href="https://www.linkedin.com/company/crossref" aria-label="LinkedIn" title="LinkedIn"><em></em></a> <a href="https://www.youtube.com/c/CrossrefVideos" aria-label="YouTube" title="YouTube"><em></em></a> <a href="https://gitlab.com/crossref" aria-label="GitLab" title="GitLab"><em></em></a> <a href="https://community.crossref.org/" aria-label="Community forum" title="Community forum"><em></em></a>

</div>

<div class="search-icon">

<a href="#" class="search-trigger">search</a>

</div>

<div class="hcwh-box-top">

</div>

<div class="logo">

<a href="https://www.crossref.org/" class="crossref-brand"><img src="https://assets.crossref.org/logo/crossref-logo-200.svg" class="site-logo" alt="Crossref logo" /></a>

</div>

</div>

</div>

<div class="header intro-header short">

<div class="container short">

<div class="row">

<div class="col-md-10 col-md-offset-1">

# Documentation

</div>

</div>

</div>

</div>

<div class="container">

<div class="row">

<div class="col-md-8 col-md-offset-1">

<div class="breadcrumb-wrap" role="navigation" aria-label="breadcrumbs navigation">

- [Home](https://www.crossref.org/)\>
- [Documentation](https://www.crossref.org/documentation/)\>
- [Metadata Retrieval](https://www.crossref.org/documentation/retrieve-metadata/)\>
- Content negotiation

</div>

</div>

<div class="col-md-2">

<div class="documentationsearchouter">

</div>

</div>

</div>

<div class="row">

<div id="documentation-nav-burger" class="col-md-12" style="display:none">

<div class="nav-burger">

</div>

<div class="nav-label">

Documentation Menu

</div>

</div>

</div>

<div id="documentation-content" class="row">

<div id="menu" class="col-md-3 col-md-offset-1 hidden-print">

<div id="v-tab">

<a href="/documentation/" class="nav-item nav-link">Documentation</a> <a href="/documentation/member-setup/" class="nav-item nav-link">Setting up as a member</a> <a href="/documentation/member-setup/account-credentials/" class="nav-item nav-link indent" style="display:none">Your Crossref account credentials</a> <a href="/documentation/member-setup/constructing-your-dois/" class="nav-item nav-link indent" style="display:none">Constructing your DOIs</a> <a href="/documentation/member-setup/constructing-your-dois/the-structure-of-a-doi/" class="nav-item nav-link doubleindent" style="display:none">DOIs for different levels</a> <a href="/documentation/member-setup/constructing-your-dois/suffixes-containing-special-characters/" class="nav-item nav-link doubleindent" style="display:none">Suffixes containing special characters</a> <a href="/documentation/member-setup/constructing-your-dois/suggested-doi-registration-workflow-including-suffix-generator/" class="nav-item nav-link doubleindent" style="display:none">Suggested DOI registration workflow, including suffix generator</a> <a href="/documentation/member-setup/constructing-your-dois/dois-and-dspace-repositories/" class="nav-item nav-link doubleindent" style="display:none">DOIs and DSpace repositories</a> <a href="/documentation/member-setup/creating-a-landing-page/" class="nav-item nav-link indent" style="display:none">Creating a landing page</a> <a href="/documentation/member-setup/working-with-a-service-provider/" class="nav-item nav-link indent" style="display:none">Working with a service provider</a> <a href="/documentation/member-setup/working-with-a-service-provider/hosting-platforms/" class="nav-item nav-link doubleindent" style="display:none">Hosting platforms</a> <a href="/documentation/member-setup/working-with-a-service-provider/manuscript-submission-systems/" class="nav-item nav-link doubleindent" style="display:none">Manuscript submission systems</a> <a href="/documentation/member-setup/working-with-a-service-provider/planning-a-platform-migration/" class="nav-item nav-link doubleindent" style="display:none">Planning a platform migration</a> <a href="/documentation/member-setup/working-with-a-service-provider/checklist-for-platform-migration/" class="nav-item nav-link doubleindent" style="display:none">Checklist for platform migration</a> <a href="/documentation/member-setup/leveling-up/" class="nav-item nav-link indent" style="display:none">Leveling up as a member</a> <a href="/documentation/research-nexus/" class="nav-item nav-link">The Research Nexus</a> <a href="/documentation/research-nexus/books-and-chapters/" class="nav-item nav-link indent" style="display:none">Introduction to books and chapters</a> <a href="/documentation/research-nexus/conference-proceedings/" class="nav-item nav-link indent" style="display:none">Introduction to conference proceedings</a> <a href="/documentation/research-nexus/datasets/" class="nav-item nav-link indent" style="display:none">Introduction to datasets</a> <a href="/documentation/research-nexus/dissertations/" class="nav-item nav-link indent" style="display:none">Introduction to dissertations</a> <a href="/documentation/research-nexus/grants/" class="nav-item nav-link indent" style="display:none">Introduction to grants</a> <a href="/documentation/research-nexus/journals-and-articles/" class="nav-item nav-link indent" style="display:none">Introduction to journals and articles</a> <a href="/documentation/research-nexus/peer-reviews/" class="nav-item nav-link indent" style="display:none">Introduction to peer reviews</a> <a href="/documentation/research-nexus/pending-publications/" class="nav-item nav-link indent" style="display:none">Introduction to pending publications</a> <a href="/documentation/research-nexus/posted-content-includes-preprints/" class="nav-item nav-link indent" style="display:none">Introduction to posted content (includes preprints)</a> <a href="/documentation/research-nexus/reports-and-working-papers/" class="nav-item nav-link indent" style="display:none">Introduction to reports and working papers</a> <a href="/documentation/research-nexus/standards/" class="nav-item nav-link indent" style="display:none">Introduction to standards</a> <a href="/documentation/principles-practices/" class="nav-item nav-link">Metadata principles and practices</a> <a href="/documentation/principles-practices/best-practices/" class="nav-item nav-link indent" style="display:none">Metadata best practices</a> <a href="/documentation/principles-practices/best-practices/abstracts/" class="nav-item nav-link doubleindent" style="display:none">Abstracts</a> <a href="/documentation/principles-practices/best-practices/bibliographic/" class="nav-item nav-link doubleindent" style="display:none">Bibliographic metadata</a> <a href="/documentation/principles-practices/best-practices/funding/" class="nav-item nav-link doubleindent" style="display:none">Funding metadata</a> <a href="/documentation/principles-practices/best-practices/license/" class="nav-item nav-link doubleindent" style="display:none">License metadata</a> <a href="/documentation/principles-practices/best-practices/multi-language/" class="nav-item nav-link doubleindent" style="display:none">Multi-language material and translations</a> <a href="/documentation/principles-practices/best-practices/references/" class="nav-item nav-link doubleindent" style="display:none">References</a> <a href="/documentation/principles-practices/best-practices/relationships/" class="nav-item nav-link doubleindent" style="display:none">Relationship metadata</a> <a href="/documentation/principles-practices/best-practices/versioning/" class="nav-item nav-link doubleindent" style="display:none">Version control, corrections, and retractions</a> <a href="/documentation/principles-practices/books-and-chapters/" class="nav-item nav-link indent" style="display:none">Books and chapters</a> <a href="/documentation/principles-practices/conference-proceedings/" class="nav-item nav-link indent" style="display:none">Conference proceedings and papers</a> <a href="/documentation/principles-practices/datasets/" class="nav-item nav-link indent" style="display:none">Datasets</a> <a href="/documentation/principles-practices/dissertations/" class="nav-item nav-link indent" style="display:none">Dissertations</a> <a href="/documentation/principles-practices/grants/" class="nav-item nav-link indent" style="display:none">Grants</a> <a href="/documentation/principles-practices/journals/" class="nav-item nav-link indent" style="display:none">Journals and articles</a> <a href="/documentation/principles-practices/peer-review/" class="nav-item nav-link indent" style="display:none">Peer review</a> <a href="/documentation/principles-practices/posted-content/" class="nav-item nav-link indent" style="display:none">Posted content</a> <a href="/documentation/principles-practices/reports/" class="nav-item nav-link indent" style="display:none">Reports and working papers</a> <a href="/documentation/principles-practices/standards/" class="nav-item nav-link indent" style="display:none">Standards</a> <a href="/documentation/register-maintain-records/" class="nav-item nav-link">Register and maintain your records</a> <a href="/documentation/register-maintain-records/choose-content-registration-method/" class="nav-item nav-link indent" style="display:none">Choosing a content registration method</a> <a href="/documentation/register-maintain-records/ojs-plugin/" class="nav-item nav-link indent" style="display:none">OJS platform</a> <a href="/documentation/register-maintain-records/ojs-plugin/ojs-3.5/" class="nav-item nav-link doubleindent" style="display:none">OJS 3.5</a> <a href="/documentation/register-maintain-records/ojs-plugin/ojs-3.4/" class="nav-item nav-link doubleindent" style="display:none">OJS 3.4</a> <a href="/documentation/register-maintain-records/ojs-plugin/ojs-3.3/" class="nav-item nav-link doubleindent" style="display:none">OJS 3.3</a> <a href="/documentation/register-maintain-records/web-deposit-form/" class="nav-item nav-link indent" style="display:none">Web deposit form</a> <a href="/documentation/register-maintain-records/metadata-manager/" class="nav-item nav-link indent" style="display:none">Metadata Manager</a> <a href="/documentation/register-maintain-records/direct-deposit-xml/" class="nav-item nav-link indent" style="display:none">Direct deposit of XML</a> <a href="/documentation/register-maintain-records/direct-deposit-xml/admin-tool/" class="nav-item nav-link doubleindent" style="display:none">Upload XML files using our admin tool</a> <a href="/documentation/register-maintain-records/direct-deposit-xml/https-post/" class="nav-item nav-link doubleindent" style="display:none">XML deposit using HTTPS POST</a> <a href="/documentation/register-maintain-records/direct-deposit-xml/https-post-using-java-program/" class="nav-item nav-link doubleindent" style="display:none">POSTing files using our upload tool</a> <a href="/documentation/register-maintain-records/direct-deposit-xml/testing-your-xml/" class="nav-item nav-link doubleindent" style="display:none">Testing your XML</a> <a href="/documentation/register-maintain-records/direct-deposit-xml/jats-xml/" class="nav-item nav-link doubleindent" style="display:none">Using JATS XML</a> <a href="/documentation/register-maintain-records/verify-your-registration/" class="nav-item nav-link indent" style="display:none">Verify your registration</a> <a href="/documentation/register-maintain-records/verify-your-registration/submission-queue-and-log/" class="nav-item nav-link doubleindent" style="display:none">Submission queue and log</a> <a href="/documentation/register-maintain-records/verify-your-registration/interpret-submission-logs/" class="nav-item nav-link doubleindent" style="display:none">Interpret submission logs</a> <a href="/documentation/register-maintain-records/verify-your-registration/troubleshooting-submissions/" class="nav-item nav-link doubleindent" style="display:none">Troubleshooting submissions</a> <a href="/documentation/register-maintain-records/verify-your-registration/notification-callback-service/" class="nav-item nav-link doubleindent" style="display:none">Notification callback service</a> <a href="/documentation/register-maintain-records/creating-and-managing-dois/" class="nav-item nav-link indent" style="display:none">Creating and managing DOIs</a> <a href="/documentation/register-maintain-records/creating-and-managing-dois/changing-or-deleting-dois/" class="nav-item nav-link doubleindent" style="display:none">Changing or deleting DOIs</a> <a href="/documentation/register-maintain-records/creating-and-managing-dois/transferring-responsibility-for-dois/" class="nav-item nav-link doubleindent" style="display:none">Transferring responsibility for titles and DOIs</a> <a href="/documentation/register-maintain-records/creating-and-managing-dois/prefix-transfers-other-ra/" class="nav-item nav-link doubleindent" style="display:none">Transferring prefixes between different Registration Agencies</a> <a href="/documentation/register-maintain-records/creating-and-managing-dois/multiple-resolution/" class="nav-item nav-link doubleindent" style="display:none">Multiple resolution</a> <a href="/documentation/register-maintain-records/maintaining-your-metadata/" class="nav-item nav-link indent" style="display:none">Maintaining your metadata</a> <a href="/documentation/register-maintain-records/maintaining-your-metadata/updating-your-metadata/" class="nav-item nav-link doubleindent" style="display:none">Updating your metadata</a> <a href="/documentation/register-maintain-records/maintaining-your-metadata/add-references/" class="nav-item nav-link doubleindent" style="display:none">Adding references to your metadata record</a> <a href="/documentation/register-maintain-records/maintaining-your-metadata/resource-only-deposit/" class="nav-item nav-link doubleindent" style="display:none">Resource-only deposit</a> <a href="/documentation/register-maintain-records/maintaining-your-metadata/registering-updates/" class="nav-item nav-link doubleindent" style="display:none">Registering updates</a> <a href="/documentation/register-maintain-records/maintaining-your-metadata/metadata-removal-markup-guide/" class="nav-item nav-link doubleindent" style="display:none">Metadata removal markup guide</a> <a href="/documentation/register-maintain-records/maintaining-your-metadata/updating-after-title-transfer/" class="nav-item nav-link doubleindent" style="display:none">Updating metadata for inherited DOIs after a title transfer</a> <a href="/documentation/schema-library/" class="nav-item nav-link">Schema library</a> <a href="/documentation/schema-library/required-recommended-elements/" class="nav-item nav-link indent" style="display:none">Required, recommended, and optional metadata</a> <a href="/documentation/schema-library/markup-guide-metadata-segments/" class="nav-item nav-link indent" style="display:none">Markup guides for metadata segments</a> <a href="/documentation/schema-library/markup-guide-metadata-segments/abstracts/" class="nav-item nav-link doubleindent" style="display:none">Abstracts</a> <a href="/documentation/schema-library/markup-guide-metadata-segments/affiliations/" class="nav-item nav-link doubleindent" style="display:none">Affiliations and ROR</a> <a href="/documentation/schema-library/markup-guide-metadata-segments/archive-locations/" class="nav-item nav-link doubleindent" style="display:none">Archive locations</a> <a href="/documentation/schema-library/markup-guide-metadata-segments/article-ids/" class="nav-item nav-link doubleindent" style="display:none">Article numbers or IDs</a> <a href="/documentation/schema-library/markup-guide-metadata-segments/contributors/" class="nav-item nav-link doubleindent" style="display:none">Contributors</a> <a href="/documentation/schema-library/markup-guide-metadata-segments/data-citation/" class="nav-item nav-link doubleindent" style="display:none">Data and software citation deposit guide</a> <a href="/documentation/schema-library/markup-guide-metadata-segments/face-markup/" class="nav-item nav-link doubleindent" style="display:none">Face markup</a> <a href="/documentation/schema-library/markup-guide-metadata-segments/full-text-urls/" class="nav-item nav-link doubleindent" style="display:none">Resource and full-text URLs</a> <a href="/documentation/schema-library/markup-guide-metadata-segments/funding-information/" class="nav-item nav-link doubleindent" style="display:none">Funding information</a> <a href="/documentation/schema-library/markup-guide-metadata-segments/issn-isbn/" class="nav-item nav-link doubleindent" style="display:none">ISSNs and ISBNs</a> <a href="/documentation/schema-library/markup-guide-metadata-segments/license-information/" class="nav-item nav-link doubleindent" style="display:none">License information</a> <a href="/documentation/schema-library/markup-guide-metadata-segments/mathml/" class="nav-item nav-link doubleindent" style="display:none">MathML</a> <a href="/documentation/schema-library/markup-guide-metadata-segments/multi-language/" class="nav-item nav-link doubleindent" style="display:none">Translated and multi-language materials</a> <a href="/documentation/schema-library/markup-guide-metadata-segments/references/" class="nav-item nav-link doubleindent" style="display:none">References</a> <a href="/documentation/schema-library/markup-guide-metadata-segments/relationships/" class="nav-item nav-link doubleindent" style="display:none">Relationships</a> <a href="/documentation/schema-library/markup-guide-metadata-segments/titles/" class="nav-item nav-link doubleindent" style="display:none">Titles</a> <a href="/documentation/schema-library/markup-guide-record-types/" class="nav-item nav-link indent" style="display:none">Markup guides for record types</a> <a href="/documentation/schema-library/markup-guide-record-types/books-and-chapters/" class="nav-item nav-link doubleindent" style="display:none">Books and chapters markup guide</a> <a href="/documentation/schema-library/markup-guide-record-types/components/" class="nav-item nav-link doubleindent" style="display:none">Components</a> <a href="/documentation/schema-library/markup-guide-record-types/conference-proceedings/" class="nav-item nav-link doubleindent" style="display:none">Conference proceedings markup guide</a> <a href="/documentation/schema-library/markup-guide-record-types/datasets/" class="nav-item nav-link doubleindent" style="display:none">Datasets markup guide</a> <a href="/documentation/schema-library/markup-guide-record-types/dissertations/" class="nav-item nav-link doubleindent" style="display:none">Dissertations markup guide</a> <a href="/documentation/schema-library/markup-guide-record-types/grants/" class="nav-item nav-link doubleindent" style="display:none">Grants markup guide</a> <a href="/documentation/schema-library/markup-guide-record-types/journals-and-articles/" class="nav-item nav-link doubleindent" style="display:none">Journals and articles markup guide</a> <a href="/documentation/schema-library/markup-guide-record-types/peer-reviews/" class="nav-item nav-link doubleindent" style="display:none">Peer reviews markup guide</a> <a href="/documentation/schema-library/markup-guide-record-types/pending-publications/" class="nav-item nav-link doubleindent" style="display:none">Pending publications markup guide</a> <a href="/documentation/schema-library/markup-guide-record-types/posted-content-includes-preprints/" class="nav-item nav-link doubleindent" style="display:none">Posted content (includes preprints) markup guide</a> <a href="/documentation/schema-library/markup-guide-record-types/reports-and-working-papers/" class="nav-item nav-link doubleindent" style="display:none">Reports and working papers markup guide</a> <a href="/documentation/schema-library/markup-guide-record-types/standards/" class="nav-item nav-link doubleindent" style="display:none">Standards markup guide</a> <a href="/documentation/schema-library/xsd-schema-quick-reference/" class="nav-item nav-link indent" style="display:none">XSD schema quick reference</a> <a href="/documentation/schema-library/schema-versions/" class="nav-item nav-link indent" style="display:none">Schema versions</a> <a href="/documentation/schema-library/metadata-deposit-schema-5-5-0/" class="nav-item nav-link indent" style="display:none">Metadata deposit schema 5.5.0</a> <a href="/documentation/schema-library/metadata-deposit-schema-5-4-0/" class="nav-item nav-link indent" style="display:none">Metadata deposit schema 5.4.0</a> <a href="/documentation/schema-library/grants-schema/" class="nav-item nav-link indent" style="display:none">Grants schema</a> <a href="/documentation/schema-library/resource-only-deposit-schema-5-4-0/" class="nav-item nav-link indent" style="display:none">Resource-only deposit schema 5.4.0</a> <a href="/documentation/schema-library/schema-deprecation-guide/" class="nav-item nav-link indent" style="display:none">Schema deprecation guide</a> <a href="/documentation/schema-library/metadata-deposit-schema/" class="nav-item nav-link indent" style="display:none">Metadata deposit schema</a> <a href="/documentation/reports/" class="nav-item nav-link">Reports</a> <a href="/documentation/reports/browsable-title-list/" class="nav-item nav-link indent" style="display:none">Browsable title list</a> <a href="/documentation/reports/conflict-report/" class="nav-item nav-link indent" style="display:none">Conflict report</a> <a href="/documentation/reports/depositor-report/" class="nav-item nav-link indent" style="display:none">Depositor report</a> <a href="/documentation/reports/doi-crawler-report/" class="nav-item nav-link indent" style="display:none">DOI crawler report</a> <a href="/documentation/reports/doi-error-report/" class="nav-item nav-link indent" style="display:none">DOI error report</a> <a href="/documentation/reports/field-or-missing-metadata-report/" class="nav-item nav-link indent" style="display:none">Field or missing metadata report</a> <a href="/documentation/reports/missed-conflict-report/" class="nav-item nav-link indent" style="display:none">Missed conflict report</a> <a href="/documentation/reports/participation-reports/" class="nav-item nav-link indent" style="display:none">Participation Reports</a> <a href="/documentation/reports/resolution-report/" class="nav-item nav-link indent" style="display:none">Resolution report</a> <a href="/documentation/reports/schematron-report/" class="nav-item nav-link indent" style="display:none">Schematron report</a> <a href="/documentation/reference-linking/" class="nav-item nav-link">Reference Linking</a> <a href="/documentation/reference-linking/how-do-i-create-reference-links/" class="nav-item nav-link indent" style="display:none">How do I find and create reference links?</a> <a href="/documentation/crossmark/" class="nav-item nav-link">Crossmark</a> <a href="/documentation/crossmark/participating-in-crossmark/" class="nav-item nav-link indent" style="display:none">Participating in Crossmark</a> <a href="/documentation/crossmark/crossmark-policy-page/" class="nav-item nav-link indent" style="display:none">Update policy page</a> <a href="/documentation/crossmark/crossmark-button-guidelines/" class="nav-item nav-link indent" style="display:none">Crossmark button guidelines</a> <a href="/documentation/crossmark/linked-clinical-trials/" class="nav-item nav-link indent" style="display:none">Linked clinical trials</a> <a href="/documentation/crossmark/crossmark-and-transferring-responsibility-for-dois/" class="nav-item nav-link indent" style="display:none">Crossmark and transferring responsibility for DOIs</a> <a href="/documentation/crossmark/crossmark-terms/" class="nav-item nav-link indent" style="display:none">Crossmark terms</a> <a href="/documentation/cited-by/" class="nav-item nav-link">Cited-by</a> <a href="/documentation/cited-by/cited-by-participation/" class="nav-item nav-link indent" style="display:none">How to participate in Cited-by</a> <a href="/documentation/cited-by/retrieve-citations/" class="nav-item nav-link indent" style="display:none">Retrieve citations using Cited-by</a> <a href="/documentation/funder-registry/" class="nav-item nav-link">Open Funder Registry</a> <a href="/documentation/funder-registry/accessing-the-funder-registry/" class="nav-item nav-link indent" style="display:none">Accessing the Open Funder Registry</a> <a href="/documentation/funder-registry/funding-data-overview/" class="nav-item nav-link indent" style="display:none">Funding data overview</a> <a href="/documentation/funder-registry/updating-funding-deposits-with-new-registry-info/" class="nav-item nav-link indent" style="display:none">Updating funding deposits with new registry info</a> <a href="/documentation/funder-registry/funder-data-via-the-api/" class="nav-item nav-link indent" style="display:none">Funder data via the API</a> <a href="/documentation/similarity-check/" class="nav-item nav-link">Similarity Check</a> <a href="/documentation/similarity-check/participate/" class="nav-item nav-link indent" style="display:none">How to participate in Similarity Check</a> <a href="/documentation/similarity-check/participate/eligibility/" class="nav-item nav-link doubleindent" style="display:none">Checking your eligibility and applying</a> <a href="/documentation/similarity-check/participate/urls-for-new-deposits/" class="nav-item nav-link doubleindent" style="display:none">Adding full-text URLs to new deposits</a> <a href="/documentation/similarity-check/participate/urls-for-existing-deposits/" class="nav-item nav-link doubleindent" style="display:none">Adding full-text URLs to existing deposits</a> <a href="/documentation/similarity-check/ithenticate-account-setup/" class="nav-item nav-link indent" style="display:none">Setting up your iThenticate v1 account (admins only)</a> <a href="/documentation/similarity-check/ithenticate-account-setup/administrator-checklist/" class="nav-item nav-link doubleindent" style="display:none">Administrator checklist</a> <a href="/documentation/similarity-check/ithenticate-account-setup/settings/" class="nav-item nav-link doubleindent" style="display:none">Admin settings</a> <a href="/documentation/similarity-check/ithenticate-account-setup/account-info/" class="nav-item nav-link doubleindent" style="display:none">Account information</a> <a href="/documentation/similarity-check/ithenticate-account-setup/manage-users/" class="nav-item nav-link doubleindent" style="display:none">Manage users</a> <a href="/documentation/similarity-check/ithenticatev2-account-setup/" class="nav-item nav-link indent" style="display:none">Setting up your iThenticate 2.0 account for use directly in the browser (admins only)</a> <a href="/documentation/similarity-check/ithenticatev2-account-setup/administrator-checklist/" class="nav-item nav-link doubleindent" style="display:none">Administrator checklist</a> <a href="/documentation/similarity-check/ithenticatev2-account-setup/exclusions/" class="nav-item nav-link doubleindent" style="display:none">Exclusions</a> <a href="/documentation/similarity-check/ithenticatev2-account-setup/private-repository/" class="nav-item nav-link doubleindent" style="display:none">Private repository</a> <a href="/documentation/similarity-check/ithenticatev2-account-setup/manage-users/" class="nav-item nav-link doubleindent" style="display:none">Manage users and folders</a> <a href="/documentation/similarity-check/ithenticatev2-mts-account-setup/" class="nav-item nav-link indent" style="display:none">Setting up your iThenticate 2.0 account MTS integration (admins only)</a> <a href="/documentation/similarity-check/ithenticatev2-mts-account-setup/administrator-checklist/" class="nav-item nav-link doubleindent" style="display:none">Administrator checklist</a> <a href="/documentation/similarity-check/ithenticatev2-mts-account-setup/api-key/" class="nav-item nav-link doubleindent" style="display:none">Setting up your MTS integration with an API key</a> <a href="/documentation/similarity-check/ithenticatev2-mts-account-setup/exclusions/" class="nav-item nav-link doubleindent" style="display:none">Exclusions</a> <a href="/documentation/similarity-check/ithenticatev2-mts-account-setup/private-repository/" class="nav-item nav-link doubleindent" style="display:none">Private repository</a> <a href="/documentation/similarity-check/ithenticatev2-mts-account-setup/manage-users/" class="nav-item nav-link doubleindent" style="display:none">Manage users and folders</a> <a href="/documentation/similarity-check/ithenticate-account-use/" class="nav-item nav-link indent" style="display:none">Using your iThenticate account</a> <a href="/documentation/similarity-check/ithenticate-account-use/folders/" class="nav-item nav-link doubleindent" style="display:none">Folders</a> <a href="/documentation/similarity-check/ithenticate-account-use/documents-overview/" class="nav-item nav-link doubleindent" style="display:none">Documents overview</a> <a href="/documentation/similarity-check/ithenticate-account-use/documents-submit/" class="nav-item nav-link doubleindent" style="display:none">Submit a document</a> <a href="/documentation/similarity-check/ithenticate-account-use/similarity-report-create/" class="nav-item nav-link doubleindent" style="display:none">Creating and finding your Similarity Report</a> <a href="/documentation/similarity-check/ithenticate-account-use/similarity-report-use/" class="nav-item nav-link doubleindent" style="display:none">Working with your Similarity Report</a> <a href="/documentation/similarity-check/ithenticate-account-use/doc-to-doc-comparison/" class="nav-item nav-link doubleindent" style="display:none">Doc-to-doc comparison</a> <a href="/documentation/similarity-check/ithenticate-account-use/account-info/" class="nav-item nav-link doubleindent" style="display:none">Your Similarity Check user account</a> <a href="/documentation/similarity-check/ithenticate-account-use/settings/" class="nav-item nav-link doubleindent" style="display:none">Settings</a> <a href="/documentation/similarity-check/similarity-report-understand/" class="nav-item nav-link indent" style="display:none">Understanding your Similarity Report</a> <a href="/documentation/similarity-check/upgrading/" class="nav-item nav-link indent" style="display:none">Upgrading from iThenticate v1 to iThenticate 2.0</a> <a href="/documentation/similarity-check/upgrading/v1-or-v2/" class="nav-item nav-link doubleindent" style="display:none">iThenticate v1 or iThenticate 2.0?</a> <a href="/documentation/similarity-check/upgrading/faqs/" class="nav-item nav-link doubleindent" style="display:none">Upgrade FAQs</a> <a href="/documentation/similarity-check/get-help/" class="nav-item nav-link indent" style="display:none">Get help with Similarity Check</a> <a href="/documentation/similarity-check/similarity-check-portuguese/" class="nav-item nav-link indent" style="display:none">Similarity Check (Português Brasileiro)</a> <a href="/documentation/similarity-check/similarity-check-portuguese/administrator-checklist-portuguese/" class="nav-item nav-link doubleindent" style="display:none">Lista de verificação do(a) administrador(a)</a> <a href="/documentation/similarity-check/similarity-check-romanian/" class="nav-item nav-link indent" style="display:none">Similarity Check (Româna)</a> <a href="/documentation/similarity-check/similarity-check-romanian/administrator-checklist-romanian/" class="nav-item nav-link doubleindent" style="display:none">Listă de verificare pentru administrator</a> <a href="/documentation/similarity-check/similarity-check-spanish/" class="nav-item nav-link indent" style="display:none">Similarity Check (Español)</a> <a href="/documentation/similarity-check/similarity-check-spanish/administrator-checklist-spanish/" class="nav-item nav-link doubleindent" style="display:none">Lista de comprobación para administradores</a> <a href="/documentation/retrieve-metadata/" class="nav-item nav-link">Metadata Retrieval</a> <a href="/documentation/retrieve-metadata/rest-api/" class="nav-item nav-link indent">REST API</a> <a href="/documentation/retrieve-metadata/rest-api/access-and-authentication/" class="nav-item nav-link doubleindent" style="display:none">Access and authentication</a> <a href="/documentation/retrieve-metadata/rest-api/rest-api-filters/" class="nav-item nav-link doubleindent" style="display:none">REST API filters</a> <a href="/documentation/retrieve-metadata/rest-api/tips-for-using-the-crossref-rest-api/" class="nav-item nav-link doubleindent" style="display:none">Tips and tricks</a> <a href="/documentation/retrieve-metadata/xml-api/" class="nav-item nav-link indent">XML API</a> <a href="/documentation/retrieve-metadata/xml-api/query-schema/" class="nav-item nav-link doubleindent" style="display:none">Query schema</a> <a href="/documentation/retrieve-metadata/xml-api/xml-query-examples/" class="nav-item nav-link doubleindent" style="display:none">Query examples</a> <a href="/documentation/retrieve-metadata/bulk-downloads/" class="nav-item nav-link indent">Public data files and snapshots</a> <a href="/documentation/retrieve-metadata/data-citations/" class="nav-item nav-link indent">Data citations</a> <a href="/documentation/retrieve-metadata/oai-pmh/" class="nav-item nav-link indent">OAI-PMH</a> <a href="/documentation/retrieve-metadata/openurl/" class="nav-item nav-link indent">OpenURL</a> <a href="/documentation/retrieve-metadata/dois-openurl-and-link-resolvers/" class="nav-item nav-link indent">DOIs, OpenURL, and link resolvers</a> <a href="/documentation/retrieve-metadata/retraction-watch/" class="nav-item nav-link indent">Retraction Watch</a> <a href="/documentation/retrieve-metadata/simple-text-query/" class="nav-item nav-link indent">Simple Text Query</a> <a href="/documentation/retrieve-metadata/content-negotiation/" class="nav-item nav-link active indent">Content negotiation</a> <a href="/documentation/retrieve-metadata/retrieving-identifiers-for-deposited-references/" class="nav-item nav-link indent">Matched references</a> <a href="/documentation/retrieve-metadata/text-and-data-mining/" class="nav-item nav-link indent">Accessing full texts</a> <a href="/documentation/retrieve-metadata/api-versioning/" class="nav-item nav-link indent">API Versions</a> <a href="/documentation/retrieve-metadata/xml-output-formats/" class="nav-item nav-link indent">XML output formats</a> <a href="/documentation/retrieve-metadata/xml-output-formats/unixsd-query-output-format/" class="nav-item nav-link doubleindent" style="display:none">UNIXSD query output format</a> <a href="/documentation/retrieve-metadata/xml-output-formats/unixref-query-output-format/" class="nav-item nav-link doubleindent" style="display:none">UNIXREF query output format</a> <a href="/documentation/retrieve-metadata/xml-output-formats/xsd-xml-query-output-format/" class="nav-item nav-link doubleindent" style="display:none">XSD XML query output format</a> <a href="/documentation/metadata-plus/" class="nav-item nav-link">Metadata Plus</a> <a href="/documentation/metadata-plus/metadata-plus-keys/" class="nav-item nav-link indent" style="display:none">Metadata Plus keys</a> <a href="/documentation/metadata-plus/metadata-plus-snapshots/" class="nav-item nav-link indent" style="display:none">Metadata Plus snapshots</a>

<div id="documentation-sticky">

<span class="nav-item nav-link new-arrow" onclick="window.scrollTo(0,0)">Back to top <img src="/img/white-up-arrow.svg" class="up-arrow" alt="up arrow" /></span>

<div class="questions-btn">

Questions?\
[Visit forum](https://community.crossref.org) or [contact us](https://www.crossref.org/contact/)

</div>

</div>

</div>

</div>

<div id="content" class="col-md-7">

## Content negotiation[](https://www.crossref.org/documentation/retrieve-metadata/content-negotiation/)

<div class="row">

<div class="nav-buttons">

<span class="btn btn-primary btnPrevious"></span><span class="btn btn-primary btnNext"></span>

</div>

</div>

Through content negotiation you can request a single metadata record in a specified format. It is a service offered by several DOI registrations agencies (currently Crossref, <a href="https://datacite.org/" target="_blank">DataCite</a>, and <a href="https://www.medra.org/" target="_blank">mEDRA</a>) through the <a href="https://citation.doi.org/docs.html" target="_blank">DOI Foundation</a>. It means that you don’t need to know where a DOI is registered in order to retrieve its associated metadata.

## How to use content negotiation

Content negotiation is an API request where the format of the metadata returned is specified in the `Accept` header, for example (using <a href="https://curl.se/" target="_blank">cURL</a> in a terminal):

`curl -LH "Accept: application/rdf+xml" "https://doi.org/10.1126/science.1157784"`

At Crossref, the following formats are available:

| Format | Accept header value |
|----|----|
| Resource Description Framework (RDF) | application/rdf+xml |
| Terse RDF Triple Language (Turtle) | text/turtle |
| Citation style language (CSL) | application/vnd.citationstyles.csl+json |
| Formatted citation | text/x-bibliography |
| Research Information Systems (RIS) | application/x-research-info-systems |
| BibTeX citation | application/x-bibtex |
| Crossref Deposit XML (UNIXREF) | application/vnd.crossref.unixref+xml |
| Crossref Output XML (UNIXSD) | application/vnd.crossref.unixsd+xml |

The formatted citation format uses two additional headers to define the citation style and locale. Here is an example query: `curl -LH "Accept: text/x-bibliography; style=bibtex; locale=en-US" "https://doi.org/10.1126/science.169.3946.635"`

We use formatting styles from the <a href="https://citationstyles.org/" target="_blank">CSL</a> repository and are currently using <a href="https://github.com/citation-style-language/styles/tree/76e6bef63e85dd10fbf6e5b304dd99781de94252" target="_blank">this version</a>. We maintain an artifact in the API with <a href="https://api.crossref.org/v1/styles" target="_blank">the list of available citation styles</a>.

## How does it work?

The DOI foundation runs an API that accepts content negotiation requests. It determines which registration agency holds the metadata and redirects the request (which is why `-L` is included in the examples above, to ensure that redirects are followed).

At Crossref, requests are handled by the transform route of the REST API, so

`curl -LH "Accept: application/rdf+xml" "https://api.crossref.org/v1/works/10.1126/science.1157784/transform"`

and

`curl -LH "Accept: application/rdf+xml" "https://doi.org/10.1126/science.1157784"`

give the same result. Using 10.23719/1531731, however, will not return a result in the first case because the DOI is registered with DataCite and not Crossref.

## Advantages and limitations

Content negotiation is useful if you want to retrieve metadata in a commonly used format, such as BibTeX or RIS. It is also convenient for compiling references in a bibliography in accordance with a publisher style. The other big advantage of content negotiation is that it can retrieve metadata from several DOI registration agencies.

Note that content negotiation maps from multiple schema to multiple schema, which may use different field names and vocabularies and the mapping is not always direct. Sometimes several types are matched to a single field, or differ between registration agencies. For example, the Crossref types `book`, `edited-book`, and `monograph` map to the single RIS type `book`.

Only one record at a time is returned by content negotiation. For filtering and queries that return multiple metadata records, use the <a href="https://www.crossref.org/documentation/retrieve-metadata/rest-api/" target="_blank">REST API</a>.

There are some known bugs with content negotiation, they are <a href="https://crossref.atlassian.net/browse/CR-855" target="_blank">listed on Jira</a>.

<div class="row">

<div class="nav-buttons">

<span class="btn btn-primary btnPrevious"></span><span class="btn btn-primary btnNext"></span>

</div>

</div>

</div>

</div>

<div class="row infoline">

<div class="col-md-10 col-md-offset-1">

Page maintainer: Martyn Rittman\
Last updated: 2025-March-17

</div>

</div>

</div>

<div class="container">

<div class="row">

<div class="home-slot col-md-3 col-md-offset-1">

<img src="https://www.crossref.org/img/crossref-love-metadata.svg" class="strap-logo" alt="I love metadata" />

</div>

<div class="home-slot home-slot-col2 col-md-3">

Join the community

</div>

<div class="home-slot col-md-3 strap">

Get email updates

</div>

</div>

</div>

<div class="container">

<div class="row">

<div class="home-slot col-md-3 col-md-offset-1">

[Membership](https://www.crossref.org/membership/ "Membership")\
[Governance](https://www.crossref.org/board-and-governance/ "Governance")\
[Sustainability](https://www.crossref.org/operations-and-sustainability/ "Sustainability")\
[Services](https://www.crossref.org/services/ "Services")\

</div>

<div class="home-slot home-slot-col2 col-md-3">

[Documentation](https://www.crossref.org/documentation/ "Documentation")\
<a href="https://status.crossref.org/" target="_blank" title="Status page">Status page</a>\
[API Learning Hub](https://www.crossref.org/learning/ "API Learning Hub")\
<a href="https://community.crossref.org/" target="_blank" title="Community forum">Community forum</a>\

</div>

<div class="home-slot col-md-3">

[Join](https://www.crossref.org/membership/ "Join")\
[Contact](https://www.crossref.org/contact/ "Contact")\
[Jobs](https://www.crossref.org/jobs/ "Jobs")\
[Blog](https://www.crossref.org/blog/ "Blog")\

</div>

</div>

</div>

<div class="container">

<div class="row">

<div class="col-md-3 vbf-social">

<div class="social-icons">

<a href="https://bsky.app/profile/crossref.bsky.social" aria-label="Bluesky" title="Bluesky"><em></em></a> <a href="https://mastodon.online/@crossref" rel="me" aria-label="Mastodon" title="Mastodon"><em></em></a> <a href="https://www.linkedin.com/company/crossref" aria-label="LinkedIn" title="LinkedIn"><em></em></a> <a href="https://www.youtube.com/c/CrossrefVideos" aria-label="YouTube" title="YouTube"><em></em></a> <a href="https://gitlab.com/crossref" aria-label="GitLab" title="GitLab"><em></em></a> <a href="https://community.crossref.org/" aria-label="Community forum" title="Community forum"><em></em></a>

</div>

</div>

<div class="col-md-6">

<img src="/images/footer/cc.svg" class="footer-svg cc" /><img src="/images/footer/by.svg" class="footer-svg by" /> The content of this site is licensed under a <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" title="Creative Commons">Creative Commons Attribution 4.0 International License</a>

</div>

<div class="col-md-3 vbf-legal">

[Accessibility](https://www.crossref.org//operations-and-sustainability/accessibility) [Privacy](https://www.crossref.org//operations-and-sustainability/privacy)

</div>

</div>

</div>

<embed src="https://crossref.matomo.cloud/piwik.php?idsite=1&amp;rec=1" style="border:0" />
