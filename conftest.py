import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser_context():
    """Uruchamia przeglądarkę raz dla całej sesji testowej."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        yield context
        browser.close()


@pytest.fixture(scope="function")
def page(browser_context):
    """Tworzy nową kartę przeglądarki dla każdego testu."""
    page = browser_context.new_page()
    yield page
    page.close()


# Stałe – dane testowe
BASE_URL = "https://www.saucedemo.com"
VALID_USER = "standard_user"
LOCKED_USER = "locked_out_user"
VALID_PASSWORD = "secret_sauce"
WRONG_PASSWORD = "wrong_password"
