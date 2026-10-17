> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Crossref: metadata-plus

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

<div class="col-lg-10 col-lg-offset-1 col-md-10 col-md-offset-1">

# Metadata Plus

</div>

</div>

</div>

</div>

<div class="container xxx">

<div class="row">

<div class="col-md-10 col-md-offset-1">

<div class="breadcrumb-wrap" role="navigation" aria-label="breadcrumbs navigation">

- [Home](https://www.crossref.org/)\>
- [Find a service](https://www.crossref.org/services/)\>
- [Metadata Retrieval](https://www.crossref.org/services/metadata-retrieval/)\>
- Metadata Plus

</div>

</div>

</div>

<div class="row">

<div class="col-md-10 col-md-offset-1">

<div class="snippet">

> #### Metadata Plus gives you enhanced access to all our supported APIs, guarantees service levels and support, and additional features such as snapshots and priority service/rate limits.

To use Metadata Plus, an optional paid-for service, you do not need to be a member. In addition to enhanced access to all our supported APIs ([OAI-PMH and REST APIs](https://www.crossref.org/documentation/retrieve-metadata/)) and metadata in XML and JSON, Metadata Plus provides you with:

- a service level agreement guaranteeing you extra service and support, giving you a consistent and predictable experience
- additional features such as snapshots and priority service/rate limits.

Metadata Plus users may use either or both of the included API interfaces:

- OAI-PMH: this API retrieves metadata in XML using the <a href="http://www.openarchives.org/OAI/openarchivesprotocol.html" target="_blank">Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH)</a> version 2 repository framework
- REST API: this API searches and filters metadata, is generally RESTFUL, and returns results in JSON. Learn more in our <a href="https://api.crossref.org/swagger-ui/index.html" target="_blank">REST API documentation</a>.

## Description of Service <a href="#00343" id="00343"><em></em></a>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th width="33%">Feature</th>
<th width="33%">Defined as</th>
<th width="33%">Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Snapshots</td>
<td>User-requested full-file downloads.<br />
<br />
Data may be requested in JSON and XML via an interface separate from each API.<br />
<br />
Pre-generated reports available via machine request and human user interface.</td>
<td>Filters based on commonly used data are in *under consideration*:<br />
+ ISSN<br />
+ Month and year<br />
+ Publisher<br />
+ Journal title</td>
</tr>
<tr>
<td>Priority Service/Rate Limits</td>
<td>Plus users will be prioritized via isolated resources.<br />
<br />
Minimum number of queries per second per IP address.</td>
<td>Rate limiting of the API is primarily on a per IP basis. If a method allows, for example, for 150 requests per rate limit window, then it allows 150 requests per IP. This number can depend on the system state and may need to change. If it does, Crossref will publish it in the response headers.</td>
</tr>
</tbody>
</table>

In the exceptional event that a release is not backwards-compatible, Crossref will provide extensive lead time to communicate the changes, as part of our proactive support for Plus users.

## How Metadata Plus works <a href="#00341" id="00341"><em></em></a>

Start by [contacting us about Metadata Plus access](mailto:plus@crossref.org). Plus subscribers can [create their own API keys](https://www.crossref.org/documentation/metadata-plus/metadata-plus-keys/) to use either or both the OAI-PMH and the REST API. Learn more in our extensive documentation for both the [REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api) and [OAI-PMH](https://www.crossref.org/documentation/retrieve-metadata/oai-pmh) interfaces.

## Service level agreement (SLA) <a href="#00342" id="00342"><em></em></a>

Crossref will maintain an aggregated, average uptime for all of the interfaces that together comprise the Crossref Metadata Service of 99.5%, reported on a monthly basis. Crossref will provide technical support to Subscriber through Crossref’s existing support channels as requested by Subscriber, and will provide a response within one (1) business day to support requests received during normal working hours in the United States and the United Kingdom. “Business days” do not include weekends or legal holidays in the United States and the United Kingdom. “Response” means that support requests will be acknowledged. The time required for resolution will depend upon the nature of the request.

## Agreement and fees for Metadata Plus <a href="#00254" id="00254"><em></em></a>

Learn more about the [Metadata Plus service terms](https://www.crossref.org/services/metadata-retrieval/metadata-plus/terms/), and [fees and pricing tiers](https://www.crossref.org/fees/#metadata-plus-subscriber-fees) for Metadata Plus.

<span id="snippet-end"></span>

</div>

## Getting started with Metadata Plus <a href="#00671" id="00671"><em></em></a>

Learn more about [Metadata Plus in our documentation](https://www.crossref.org/education/metadata-plus/metadata-plus-snapshots/).

------------------------------------------------------------------------

</div>

</div>

<div class="row">

<div class="col-md-10 col-md-offset-1">

</div>

</div>

<div class="row infoline">

<div class="col-md-10 col-md-offset-1">

Page maintainer: Martyn Rittman\
Last updated: 2020-April-08

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
