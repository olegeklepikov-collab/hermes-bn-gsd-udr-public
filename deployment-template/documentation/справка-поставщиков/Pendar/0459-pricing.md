> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Pendar: pricing

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


<div class="d-flex">

<div id="sidebar" class="sidebar">

<div class="sidebar-logo text-center mb-2">

<a href="/" class="sidebar-logo-link" title="Go to Home"><img src="/static/images/pendar_logo_no_background.a5c10d3a95dc.png" class="sidebar-logo-img" onerror="this.style.display=&#39;none&#39;; this.nextElementSibling.style.display=&#39;inline&#39;;" alt="Pendar Logo" /></a> <span class="version-text" style="display:none;">v1.6.0</span>

</div>

<div class="nav flex-column">

<div class="nav-item">

<a href="#" class="nav-link nav-disabled" data-tooltip="🔒 Please login or register to chat with agents"><span class="emoji-icon"> <img src="/static/icons/stars.91b8109955b4.svg" class="sidebar-svg-icon" /> </span> <span class="nav-text">Chat with agents</span></a>

</div>

<div class="nav-item">

<a href="#" class="nav-link nav-disabled" data-tooltip="🔒 Please login or register to access Library"><span class="emoji-icon"> <img src="/static/icons/library_sidenav.25f2561aa6fa.svg" class="sidebar-svg-icon" /> </span> <span class="nav-text">Library</span></a>

</div>

<div class="nav-item unified-chat-history-nav-item" style="display:none;">

<a href="#" id="sidebar-history-btn" class="nav-link" data-tooltip="Chat history" title="Open past chat conversations"><span class="emoji-icon"> <img src="/static/icons/history_sidenav.dcb5842ae81e.svg" class="sidebar-svg-icon" /> </span> <span class="nav-text">Chat history</span></a>

</div>

<div class="nav-item">

<a href="#" class="nav-link nav-disabled" data-tooltip="🔒 Please login or register to access Research Briefings"><span class="emoji-icon"> <img src="/static/icons/briefings.7215a5b9708c.svg" class="sidebar-svg-icon" /> </span> <span class="nav-text">Research Briefings</span></a>

</div>

<div class="nav-item">

<a href="/accounts/login/" class="nav-link" data-tooltip="Login"><span class="emoji-icon"> <img src="/static/icons/key.95f6973e1441.svg" class="sidebar-svg-icon" /> </span> <span class="nav-text">Login</span></a>

</div>

</div>

<div class="bottom-nav-section">

<div class="bottom-nav-separator">

</div>

<div class="bottom-nav-item">

<span class="emoji-icon"> <img src="/static/icons/help_sidenav.c7b2c7485bc3.svg" class="sidebar-svg-icon" /> </span> <span class="nav-text">Help</span>

</div>

<div class="bottom-nav-item">

<span class="emoji-icon"> <img src="/static/icons/toggle_sidenav.3a83705787dc.svg" class="sidebar-svg-icon" /> </span> <span class="nav-text">Toggle Sidebar</span>

</div>

</div>

</div>

<div id="help-chooser-modal" class="autosave-modal app-settings-modal-anchor help-chooser-modal" style="display:none;" role="dialog" aria-modal="true" aria-label="Help" aria-hidden="true">

<div id="help-chooser-backdrop" class="autosave-modal-backdrop">

</div>

<div id="help-chooser-body" class="autosave-modal-body app-settings-modal-body help-chooser-body">

<div class="autosave-modal-header autosave-modal-header--close-only">

×

</div>

<div class="help-chooser-actions">

<img src="/static/icons/ai_help.ded35de07c25.svg" class="help-chooser-action-icon" /> User guides

<a href="/support/" class="help-chooser-action" target="_blank" rel="noopener noreferrer"><img src="/static/icons/help.8d6fab740160.svg" class="help-chooser-action-icon" /> <span>Contact us</span></a> <a href="/feedback/" class="help-chooser-action" target="_blank" rel="noopener noreferrer"><img src="/static/icons/feedback_sidenav.fd0c3d021d3e.svg" class="help-chooser-action-icon" /> <span>Give us feedback</span></a>

</div>

</div>

</div>

<div id="help-modal" class="help-modal" style="display:none;" role="dialog" aria-modal="true" aria-labelledby="help-modal-title" aria-hidden="true">

<div class="help-modal-backdrop">

</div>

<div id="help-modal-dialog" class="help-modal-dialog">

<div class="help-modal-header">

<img src="/static/icons/help_modal_back.f705f8b57ed3.svg" class="help-modal-back-icon" />

## User guides

×

</div>

<div id="help-topic-body" class="help-topic-body is-empty">

<div id="help-topic-selector" class="help-topic-selector">

<div class="help-topic-pill-wrap">

<span class="help-topic-pill-size-anchor" aria-hidden="true"> <span class="help-topic-pill-size-icon"></span> What is Analyze Research Landscape? </span>

<img src="/static/icons/help_select.d513785092ed.svg" class="help-topic-pill-icon" data-role="pill-icon" /> <span class="help-topic-pill-label" data-role="pill-label">Select</span>

<div id="help-topic-menu" class="help-topic-menu" role="listbox" hidden="">

</div>

</div>

</div>

<div id="help-modal-panel" class="help-modal-panel" tabindex="0">

</div>

</div>

</div>

</div>

<div id="upgradeModal" class="upgrade-modal-overlay">

<div class="upgrade-modal">

×

### Not enough credits

Buy credits to keep going

<div class="upgrade-modal-buttons">

<a href="/pricing/" class="dashboard-btn upgrade-modal-dashboard-btn"><img src="/static/icons/credit_card.0bd296790b33.svg" class="dashboard-btn-subscription-icon" aria-hidden="true" width="20" height="20" /> Buy Credits</a>

</div>

</div>

</div>

<div id="mainContent" class="main-content">

<div class="content-container">

<div class="pricing-container">

<div class="pricing-header">

<div class="pricing-title-row">

<img src="/static/icons/credit-card-main-page.b4853c5481bb.svg" class="pricing-title-icon" />

# Buy Credit

</div>

Credits never expire and there are no recurring charges for credit packages

</div>

<div class="pricing-pack-row-heading">

<img src="/static/icons/individual.e955430f5f8a.svg" class="pricing-pack-row-icon pricing-pack-row-icon--individual" />

## Individual Packs

</div>

<div class="credit-pack-pills credit-pack-pills--individual">

<a href="/accounts/login/?pack=starter" class="dashboard-btn">250 credits for $10</a> <a href="/accounts/login/?pack=plus" class="dashboard-btn">500 credits for $20</a> <a href="/accounts/login/?pack=pro" class="dashboard-btn">1250 credits for $50</a>

</div>

<div class="pricing-pack-row-heading">

<img src="/static/icons/sharable.0495e9500633.svg" class="pricing-pack-row-icon pricing-pack-row-icon--sharable" />

## Sharable packs

</div>

Buy for yourself, or share one key with a team after you choose a pack.

<div class="credit-pack-pills credit-pack-pills--sharable">

<a href="/accounts/login/?pack=growth" class="dashboard-btn">2500 credits for $100</a> <a href="/accounts/login/?pack=team" class="dashboard-btn">12500 credits for $500</a> <a href="/accounts/login/?pack=lab" class="dashboard-btn">25000 credits for $1000</a> <a href="/accounts/login/" class="dashboard-btn">Custom</a>

</div>

<div class="section pricing-briefing-section">

<div class="pricing-pack-row-heading">

<img src="/static/icons/newsletter_monitor.b4f2f5899289.svg" class="pricing-pack-row-icon pricing-pack-row-icon--monitor" />

## Monitor research fields

</div>

Track progress in scientific fields by subscribing to agentic monitoring

<div class="briefing-subscribe-row">

<div class="briefing-subscribe-copy">

Subscribe for \$4/month to get 6

</div>

<a href="/accounts/login/?briefing=1" class="dashboard-btn briefing-subscribe-action-pill"><img src="/static/icons/briefings.7215a5b9708c.svg" class="btn-icon" aria-hidden="true" width="20" height="20" /> Subscribe</a>

</div>

</div>

<div class="pricing-card pricing-features-card">

<div class="tier-features">

### What do credits buy?

- <span class="feature-emoji"> <img src="/static/icons/paper_finder_home.9e3d9723861e.svg" class="feature-icon-img" /> </span> <span class="feature-name">Explore Literature</span> <span class="feature-limit"> 3 credits / run </span>
- <span class="feature-emoji"> <img src="/static/icons/deep_research_home.d47692291630.svg" class="feature-icon-img" /> </span> <span class="feature-name">Deep Research</span> <span class="feature-limit"> 12 credits / run </span>
- <span class="feature-emoji"> <img src="/static/icons/research_mapping_home.c0e8e6603991.svg" class="feature-icon-img" /> </span> <span class="feature-name">Analyze Research Landscape</span> <span class="feature-limit"> 7 credits / run </span>
- <span class="feature-emoji"> <img src="/static/icons/claim_validation_library.c269804b6d0a.svg" class="feature-icon-img" /> </span> <span class="feature-name">Validate a Claim</span> <span class="feature-limit"> 3 credits / run </span>
- <span class="feature-emoji"> <img src="/static/icons/ai-writer.e8ec46764bbb.svg" class="feature-icon-img" /> </span> <span class="feature-name">Writing Assistant</span> <span class="feature-limit"> 7 credits up to 15 papers, then +1 per 5 extra papers </span>
- <span class="feature-emoji"> <img src="/static/icons/pdf_upload.53264c52d4e0.svg" class="feature-icon-img" /> </span> <span class="feature-name">PDF Uploads</span> <span class="feature-limit"> 1 credit / run </span>
- <span class="feature-emoji"> <img src="/static/icons/graph_hopper.d2d8d11cedea.svg" class="feature-icon-img" /> </span> <span class="feature-name">Citation analytics</span> <span class="feature-limit"> 1 credit / 3 analyses </span>
- <span class="feature-emoji"> <img src="/static/icons/mcp_plugin.2b7b09f3914e.svg" class="feature-icon-img" /> </span> <span class="feature-name">Plugin calls</span> <span class="feature-limit"> 1 credit / call; bibliography audits 1 per 5 references </span>
- <span class="feature-emoji"> <img src="/static/icons/paper_library_home.24af6d90684f.svg" class="feature-icon-img" /> </span> <span class="feature-name">Paper Library Storage</span> <span class="feature-limit">Grows with your total purchases</span>

</div>

</div>

<div class="pricing-nav-buttons">

<a href="/accounts/login/" class="dashboard-btn"><em></em> Login</a>

</div>

</div>

</div>

</div>

</div>
