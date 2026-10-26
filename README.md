# QA Portfolio – Playwright + Python

Projekt testowy przygotowany jako część portfolio QA. Zawiera testy manualne (udokumentowane jako przypadki testowe) oraz testy automatyczne napisane w Playwright + Python.

## Testowana aplikacja

**SauceDemo** (`https://www.saucedemo.com`) – publiczna aplikacja demo e-commerce, stworzona specjalnie do celów testowych przez Sauce Labs. Idealnie nadaje się do prezentacji umiejętności QA, ponieważ zawiera celowo wbudowane błędy i różne typy kont użytkowników.

## Struktura projektu

```
qa-portfolio/
├── tests/
│   ├── test_login.py          # Testy logowania (pozytywne i negatywne)
│   ├── test_cart.py           # Testy koszyka zakupów
│   └── test_checkout.py       # Testy procesu zakupu
├── pages/
│   └── login_page.py          # Page Object Model – strona logowania
├── test_cases/
│   └── TC_LOGIN.md            # Ręcznie napisane przypadki testowe (format Jira-like)
├── bug_reports/
│   └── BUG_001.md             # Przykładowy raport błędu
├── conftest.py                # Konfiguracja Playwright (fixtures)
├── pytest.ini                 # Konfiguracja pytest
└── requirements.txt           # Zależności projektu
```

## Technologie

- **Python 3.10+**
- **Playwright** – automatyzacja przeglądarki
- **pytest** – framework testowy
- **pytest-html** – generowanie raportów HTML

## Uruchomienie

```bash
# 1. Instalacja zależności
pip install -r requirements.txt

# 2. Instalacja przeglądarek Playwright
playwright install chromium

# 3. Uruchomienie wszystkich testów
pytest

# 4. Uruchomienie z raportem HTML
pytest --html=report.html --self-contained-html

# 5. Uruchomienie w trybie "headful" (widoczna przeglądarka)
pytest --headed
```

## Wyniki

Testy pokrywają następujące obszary:
- ✅ Logowanie poprawne / niepoprawne (6 przypadków testowych)
- ✅ Dodawanie i usuwanie produktów z koszyka (4 przypadki)
- ✅ Pełny flow zakupu (checkout end-to-end) (3 przypadki)
- ✅ Testowanie REST API (Postman – kolekcja w katalogu `/postman`)
