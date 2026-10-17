> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Crossref: datacitations-swagger

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


OpenAPI UI (Powered by Quarkus 3.24.3)
window.onload = function() {
                
                // If Url is relative, append the host and port
                var oar = "/beta/datacitations/swagger/oauth2-redirect.html";
                if(oar.startsWith("/")){
                    oar = window.location.protocol + "//" + window.location.host + oar;   
                }
                
                var ui = SwaggerUIBundle({
                            url: '/beta/datacitations/openapi',
                            dom_id: '#swagger-ui',
                            deepLinking: true,
                            presets: [SwaggerUIBundle.presets.apis,SwaggerUIStandalonePreset],
                            plugins: [SwaggerUIBundle.plugins.DownloadUrl],
                            layout: 'StandaloneLayout',
                            oauth2RedirectUrl: oar,
                          })
                
            }
function waitForSwaggerUI() {
                var linkElement = document.getElementsByClassName("link")[0];

                if (linkElement !== undefined) {
                    clearInterval(checkInterval); 
                    const urlParams = new URLSearchParams(window.location.search);
                    const embed = urlParams.get('embed');
                    
                    if(!embed){
                        linkElement.innerHTML = "<a id='swaggerUiLogoLink' href='/beta/datacitations/swagger'><img src='logo.png' alt='OpenAPI UI (Powered by Quarkus 3.24.3)' height='44' align='middle'></a><a id='swaggerUiTitleLink' href='/beta/datacitations/swagger'></a>";
                    }else{
                        linkElement.style.display = 'none';
                        var downloadElement = document.getElementsByClassName("download-url-input")[0];
                        if (downloadElement !== undefined) {
                            downloadElement.style.width = "100%";
                        }
                    }
                }
            }
            var checkInterval = setInterval(waitForSwaggerUI, 100);
