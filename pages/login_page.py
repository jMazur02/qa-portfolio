"""
Page Object Model dla strony logowania SauceDemo.

Wzorzec POM (Page Object Model) to standard w testowaniu automatycznym –
zamiast pisać selektory bezpośrednio w testach, opakowujemy je w klasę.
Dzięki temu gdy zmieni się UI aplikacji, poprawkę robimy w jednym miejscu.
"""

BASE_URL = "https://www.saucedemo.com"


class LoginPage:
    def __init__(self, page):
        self.page = page
        # Lokatory elementów na stronie logowania
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def navigate(self):
        """Otwiera stronę logowania."""
        self.page.goto(BASE_URL)

    def login(self, username: str, password: str):
        """Wypełnia formularz logowania i zatwierdza."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        """Zwraca tekst komunikatu błędu (jeśli widoczny)."""
        return self.error_message.inner_text()

    def is_error_visible(self) -> bool:
        """Sprawdza czy komunikat błędu jest widoczny."""
        return self.error_message.is_visible()
