"""
Testy modułu logowania aplikacji SauceDemo.

Pokryte przypadki testowe:
- TC-001: Poprawne logowanie
- TC-002: Błędne hasło
- TC-003: Puste pole użytkownika
- TC-004: Puste pole hasła
- TC-005: Zablokowane konto
- TC-006: Weryfikacja tytułu strony po zalogowaniu
"""

import pytest
from pages.login_page import LoginPage
from conftest import VALID_USER, VALID_PASSWORD, LOCKED_USER, WRONG_PASSWORD


class TestLogin:

    def test_TC001_successful_login(self, page):
        """TC-001: Poprawne logowanie z prawidłowymi danymi."""
        login = LoginPage(page)
        login.navigate()
        login.login(VALID_USER, VALID_PASSWORD)

        # Po zalogowaniu powinna pojawić się strona z produktami
        assert "/inventory" in page.url, (
            f"Oczekiwano przekierowania na /inventory, otrzymano: {page.url}"
        )

    def test_TC002_wrong_password(self, page):
        """TC-002: Logowanie z błędnym hasłem – oczekiwany komunikat błędu."""
        login = LoginPage(page)
        login.navigate()
        login.login(VALID_USER, WRONG_PASSWORD)

        assert login.is_error_visible(), "Komunikat błędu powinien być widoczny"
        assert "Username and password do not match" in login.get_error_message()

    def test_TC003_empty_username(self, page):
        """TC-003: Próba logowania z pustym polem nazwy użytkownika."""
        login = LoginPage(page)
        login.navigate()
        login.login("", VALID_PASSWORD)

        assert login.is_error_visible(), "Komunikat błędu powinien być widoczny"
        assert "Username is required" in login.get_error_message()

    def test_TC004_empty_password(self, page):
        """TC-004: Próba logowania z pustym polem hasła."""
        login = LoginPage(page)
        login.navigate()
        login.login(VALID_USER, "")

        assert login.is_error_visible(), "Komunikat błędu powinien być widoczny"
        assert "Password is required" in login.get_error_message()

    def test_TC005_locked_out_user(self, page):
        """TC-005: Konto zablokowane – weryfikacja odpowiedniego komunikatu."""
        login = LoginPage(page)
        login.navigate()
        login.login(LOCKED_USER, VALID_PASSWORD)

        assert login.is_error_visible(), "Komunikat błędu powinien być widoczny"
        assert "locked out" in login.get_error_message().lower()

    def test_TC006_page_title_after_login(self, page):
        """TC-006: Weryfikacja tytułu strony po pomyślnym zalogowaniu."""
        login = LoginPage(page)
        login.navigate()
        login.login(VALID_USER, VALID_PASSWORD)

        title = page.title()
        assert "Swag Labs" in title, f"Oczekiwano 'Swag Labs' w tytule, otrzymano: {title}"
