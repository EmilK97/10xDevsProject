Frontend - prosty frontend z wykorzystaniem stylów .css i JS.
- Zapewnie prostotę implementacji - nie potrzebujemy skomplikowanych rozwiązań jak React.
- Prosty JS oraz definiowanie stylów .css w pełni wystarczy dla elementow interaktywnych strony.

Backend - pisany w pythonie, za wykorzystaniem frameowrka Django.
- Zapewnia bazę danych SQLite
- Jest rozwiązaniem open source, które można hostować lokalnie lub na własnym serwerze
- Łatwo zaimplementować autentykację użytkowników

CI/CD i Hosting:
- Github Actions do tworzenia pipeline'ów CI/CD
- DigitalOcean do hostowania aplikacji za pośrednictwem obrazu docker

Testy i Zapewnienie Jakości:
- pytest jako główny framework testowy
- pytest-django do integracji z Django
- pytest-cov do analizy pokrycia kodu
- Factory Boy do generowania danych testowych
- Selenium WebDriver do testów UI
- Minimum 80% pokrycia kodu testami
- Automatyczne testy w pipeline CI/CD