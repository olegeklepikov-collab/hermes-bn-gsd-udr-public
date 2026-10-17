> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Crossref: public-data-2026

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

<div class="col-md-11 col-md-offset-1">

<div class="page-banner-titleline">

# Blog

</div>

</div>

</div>

</div>

</div>

<div class="container">

<div class="row">

<div class="col-md-11 col-md-offset-1">

<div class="breadcrumb-wrap" role="navigation" aria-label="breadcrumbs navigation">

- [Home](https://www.crossref.org/)\>
- [Blog](https://www.crossref.org/blog/)\>
- 2026 public data file now available

</div>

<div class="doi-wrap">

<img src="/img/crossref-logo-icon-only.svg" class="site-logo" height="15" alt="Crossref logo icon" /><https://doi.org/10.64000/7s70g-drz77>

</div>

</div>

</div>

<div class="row">

<div class="col-md-8 col-md-offset-1 content-column">

** 3 minute read.**

## 2026 public data file now available

<div class="details-wrapper clearfix">

<div class="details">

<div class="img">

<img src="https://www.crossref.org//images/staff/martyn-rittman.jpg" width="57" height="57" alt="Martyn Rittman" />

</div>

[Martyn Rittman](https://www.crossref.org/authors/martyn-rittman), [Carlos del Ojo Elías](https://www.crossref.org/authors/carlos-del-ojo-el%C3%ADas), [Luis Montilla](https://www.crossref.org/authors/luis-montilla) – 2026 March 17

In <span class="category-link">[Metadata Retrieval](https://www.crossref.org/categories/metadata-retrieval)</span><span class="category-link">[Metadata](https://www.crossref.org/categories/metadata)</span><span class="category-link">[APIs](https://www.crossref.org/categories/apis)</span>

</div>

</div>

Once a year we release all metadata records for content registered with Crossref in a public data file. This year’s version, containing nearly 180 million records, is now available. It includes metadata associated with all Crossref-registered DOIs in JSON-lines format.

All our metadata is openly available via our REST API at all time and this file provides the same information all in one place for those who find that format useful for their tools and analysis. You can access the file via Academic Torrents at <a href="https://doi.org/10.13003/nggf-vt1j" target="_blank">https://doi.org/10.13003/nggf-vt1j</a> or <a href="https://www.crossref.org/documentation/retrieve-metadata/bulk-downloads/#00818" target="_blank">directly from AWS</a>. For further guidance and tips, <a href="https://www.crossref.org/documentation/retrieve-metadata/bulk-downloads/" target="_blank">see our documentation</a>. The complete, compressed files are 208 GB.

Our metadata has several sources:

- Primarily, it comes from records deposited by over 24,000 members spread across over 160 countries. This year, we are pleased to have added a number of new countries by expanding our <a href="https://www.crossref.org/gem/" target="_blank">GEM program</a>, which supports participation in the Crossref community from those in the most economically disadvantaged regions.
- Second, we enrich the data by adding automated matches, for example by adding DOIs to deposited references, and organisation identifiers to funders. We are undertaking a renewal of our matching processes, starting later this year with matching funders to ROR identifiers.
- Finally, we use selected third party sources to enrich the metadata. Currently we include retractions from the Retraction Watch database.

Most of the data can be freely reused and is not subject to copyright. Some limitations are applied to abstracts. See <a href="https://www.crossref.org/documentation/retrieve-metadata/#73020" target="_blank">our documentation</a> for more details about licensing.

## Why do we do this?

The community is key to everything we do. Without the thousands of members depositing metadata, we would have nothing to share. And without countless organisations and individuals making use of the metadata, it would have no impact or value. Our mission is to serve our community, and making metadata publicly and openly available is one of our key values. The public data file is just one of a number of ways in which we enable <a href="https://www.crossref.org/documentation/retrieve-metadata/" target="_blank">metadata retrieval</a>.

Over the last year, there have been over 600 downloads of the public data file. In addition, we see around 2 billion hits to our public APIs each month. We are always excited to hear about the diverse and interesting ways in which metadata can be used.

## What’s different this year?

Thanks to the rich metadata, the records deposited with Crossref are interconnected with many types of relationships between works, people, and organisations, that tell the story of the research endeavor. The latest public data file reflects the current status of the research nexus as we know it and we’re delighted to share it with the community.

This year’s dataset contains 12.7 million new records (a 7.6% increase since last year). Across the board, we’re also seeing richer metadata records, with more abstracts (up 15%), ORCID identifiers for authors (up 20%), ROR identifiers for organisations (up 250%), and links to grant identifiers for funding (reaching 50,000 records).

Research integrity is a current theme in our community. We can see that members increasingly look to leverage metadata in service of asserting trust in their works. An additional 27% more records have Crossmark enabled, meaning that the member responsible is open about research integrity practices, and committed to communicating corrections, retractions, and other post-publication changes. In addition, this year’s snapshot contains retractions from the Retraction Watch database. If you have any questions or feedback about the public data file, or would like to discuss how you can use it, head over to our <a href="https://community.crossref.org/" target="_blank">community forum</a> and join the conversation.

<div>

<div class="related-reading">

### Related reading

<div class="pub-card-grid">

<div class="card">

<div class="card-body">

Blog

#### 2025 public data file now available

<a href="/blog/2025-public-data-file-now-available/" class="card-link">Read more →</a>

</div>

</div>

<div class="card">

<div class="card-body">

Blog

#### Announcing changes to REST API rate limits

<a href="/blog/announcing-changes-to-rest-api-rate-limits/" class="card-link">Read more →</a>

</div>

</div>

<div class="card">

<div class="card-body">

Blog

#### 2024 public data file now available, featuring new experimental formats

<a href="/blog/2024-public-data-file-now-available-featuring-new-experimental-formats/" class="card-link">Read more →</a>

</div>

</div>

</div>

</div>

</div>

<div id="discourse-comments">

</div>

</div>

<div class="col-md-2">

<div class="blogsearchouter">

</div>

<div class="blog-box">

<a href="/blog/index.xml" class="topic-rss"><em></em> RSS feed</a>

</div>

<div class="section">

<div class="blog-box">

## Recent blog posts

<div class="item">

[How Grobid uses Crossref metadata to enrich bibliographic information](https://www.crossref.org/blog/how-grobid-uses-crossref-metadata-to-enrich-bibliographic-information/)

2026 October 06

</div>

<div class="item">

[2026 board election slate](https://www.crossref.org/blog/2026-board-election-slate/)

2026 September 21

</div>

<div class="item">

[July 2026 board meeting summary](https://www.crossref.org/blog/july-2026-board-meeting-summary/)

2026 September 17

</div>

<div class="item">

[Improving how funding connects to research outputs](https://www.crossref.org/blog/improving-how-funding-connects-to-research-outputs/)

2026 September 15

</div>

<div class="section">

<div class="blog-box">

## Topics

<div class="topic-cloud">

<a href="/categories/metadata" class="label label-default topic-pill">Metadata<span class="topic-count">(173)</span></a> <a href="/categories/community" class="label label-default topic-pill">Community<span class="topic-count">(147)</span></a> <a href="/categories/identifiers" class="label label-default topic-pill">Identifiers<span class="topic-count">(103)</span></a> <a href="/categories/meetings" class="label label-default topic-pill">Meetings<span class="topic-count">(76)</span></a> <a href="/categories/member-briefing" class="label label-default topic-pill">Member Briefing<span class="topic-count">(72)</span></a> <a href="/categories/collaboration" class="label label-default topic-pill">Collaboration<span class="topic-count">(66)</span></a> <a href="/categories/linking" class="label label-default topic-pill">Linking<span class="topic-count">(51)</span></a> <a href="/categories/content-registration" class="label label-default topic-pill">Content Registration<span class="topic-count">(49)</span></a> <a href="/categories/apis" class="label label-default topic-pill">APIs<span class="topic-count">(47)</span></a> <a href="/categories/research-nexus" class="label label-default topic-pill">Research Nexus<span class="topic-count">(44)</span></a> <a href="/categories/citation" class="label label-default topic-pill">Citation<span class="topic-count">(43)</span></a> <a href="/categories/governance" class="label label-default topic-pill">Governance<span class="topic-count">(37)</span></a> <a href="/categories/event-data" class="label label-default topic-pill">Event Data<span class="topic-count">(34)</span></a> <a href="/categories/rd" class="label label-default topic-pill">R&amp;D<span class="topic-count">(34)</span></a> <a href="/categories/board" class="label label-default topic-pill">Board<span class="topic-count">(33)</span></a> <a href="/categories/dois" class="label label-default topic-pill">DOIs<span class="topic-count">(33)</span></a> <a href="/categories/annual-meeting" class="label label-default topic-pill">Annual Meeting<span class="topic-count">(29)</span></a> <a href="/categories/interoperability" class="label label-default topic-pill">Interoperability<span class="topic-count">(27)</span></a> <a href="/categories/membership" class="label label-default topic-pill">Membership<span class="topic-count">(27)</span></a> <a href="/categories/datacite" class="label label-default topic-pill">DataCite<span class="topic-count">(26)</span></a> <a href="/categories/data" class="label label-default topic-pill">Data<span class="topic-count">(25)</span></a> <a href="/categories/elections" class="label label-default topic-pill">Elections<span class="topic-count">(25)</span></a> <a href="/categories/persistence" class="label label-default topic-pill">Persistence<span class="topic-count">(25)</span></a> <a href="/categories/research-funders" class="label label-default topic-pill">Research Funders<span class="topic-count">(24)</span></a> <a href="/categories/orcid" class="label label-default topic-pill">ORCID<span class="topic-count">(23)</span></a> <a href="/categories/search" class="label label-default topic-pill">Search<span class="topic-count">(23)</span></a> <a href="/categories/publishing" class="label label-default topic-pill">Publishing<span class="topic-count">(21)</span></a> <a href="/categories/staff" class="label label-default topic-pill">Staff<span class="topic-count">(21)</span></a> <a href="/categories/grant-linking-system" class="label label-default topic-pill">Grant Linking System<span class="topic-count">(20)</span></a> <a href="/categories/api-case-study" class="label label-default topic-pill">API Case Study<span class="topic-count">(18)</span></a> <a href="/categories/standards" class="label label-default topic-pill">Standards<span class="topic-count">(18)</span></a> <a href="/categories/strategy" class="label label-default topic-pill">Strategy<span class="topic-count">(18)</span></a> <a href="/categories/infrastructure" class="label label-default topic-pill">Infrastructure<span class="topic-count">(17)</span></a> <a href="/categories/linked-data" class="label label-default topic-pill">Linked Data<span class="topic-count">(16)</span></a> <a href="/categories/preprints" class="label label-default topic-pill">Preprints<span class="topic-count">(16)</span></a> <a href="/categories/research-integrity" class="label label-default topic-pill">Research Integrity<span class="topic-count">(16)</span></a> <a href="/categories/metadata-matching" class="label label-default topic-pill">Metadata Matching<span class="topic-count">(15)</span></a> <a href="/categories/schema" class="label label-default topic-pill">Schema<span class="topic-count">(15)</span></a> <a href="/categories/crossmark" class="label label-default topic-pill">Crossmark<span class="topic-count">(14)</span></a> <a href="/categories/wikipedia" class="label label-default topic-pill">Wikipedia<span class="topic-count">(14)</span></a> <a href="/categories/xmp" class="label label-default topic-pill">XMP<span class="topic-count">(14)</span></a> <a href="/categories/handle" class="label label-default topic-pill">Handle<span class="topic-count">(12)</span></a> <a href="/categories/news-release" class="label label-default topic-pill">News Release<span class="topic-count">(12)</span></a> <a href="/categories/sustainability" class="label label-default topic-pill">Sustainability<span class="topic-count">(12)</span></a> <a href="/categories/ror" class="label label-default topic-pill">ROR<span class="topic-count">(11)</span></a> <a href="/categories/rss" class="label label-default topic-pill">RSS<span class="topic-count">(11)</span></a> <a href="/categories/citation-formats" class="label label-default topic-pill">Citation Formats<span class="topic-count">(10)</span></a> <a href="/categories/metadata-manager" class="label label-default topic-pill">Metadata Manager<span class="topic-count">(10)</span></a>

</div>

</div>

<div class="blog-box">

## Archives

<div class="topic-cloud">

<a href="/archives/2026" class="label label-default topic-pill">2026<span class="topic-count">(45)</span></a> <a href="/archives/2025" class="label label-default topic-pill">2025<span class="topic-count">(51)</span></a> <a href="/archives/2024" class="label label-default topic-pill">2024<span class="topic-count">(37)</span></a> <a href="/archives/2023" class="label label-default topic-pill">2023<span class="topic-count">(31)</span></a> <a href="/archives/2022" class="label label-default topic-pill">2022<span class="topic-count">(31)</span></a> <a href="/archives/2021" class="label label-default topic-pill">2021<span class="topic-count">(25)</span></a> <a href="/archives/2020" class="label label-default topic-pill">2020<span class="topic-count">(34)</span></a> <a href="/archives/2019" class="label label-default topic-pill">2019<span class="topic-count">(37)</span></a> <a href="/archives/2018" class="label label-default topic-pill">2018<span class="topic-count">(55)</span></a> <a href="/archives/2017" class="label label-default topic-pill">2017<span class="topic-count">(41)</span></a> <a href="/archives/2016" class="label label-default topic-pill">2016<span class="topic-count">(50)</span></a> <a href="/archives/2015" class="label label-default topic-pill">2015<span class="topic-count">(23)</span></a> <a href="/archives/2014" class="label label-default topic-pill">2014<span class="topic-count">(4)</span></a> <a href="/archives/2013" class="label label-default topic-pill">2013<span class="topic-count">(2)</span></a> <a href="/archives/2012" class="label label-default topic-pill">2012<span class="topic-count">(5)</span></a> <a href="/archives/2011" class="label label-default topic-pill">2011<span class="topic-count">(6)</span></a> <a href="/archives/2010" class="label label-default topic-pill">2010<span class="topic-count">(9)</span></a> <a href="/archives/2009" class="label label-default topic-pill">2009<span class="topic-count">(34)</span></a> <a href="/archives/2008" class="label label-default topic-pill">2008<span class="topic-count">(56)</span></a> <a href="/archives/2007" class="label label-default topic-pill">2007<span class="topic-count">(91)</span></a> <a href="/archives/2006" class="label label-default topic-pill">2006<span class="topic-count">(21)</span></a>

</div>

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

</div>

</div>

</div>

</div>
