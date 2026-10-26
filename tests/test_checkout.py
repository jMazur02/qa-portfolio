"""
Testy procesu zakupu (checkout) w aplikacji SauceDemo.

Pokryte przypadki testowe:
- TC-011: Pełny przepływ zakupu (end-to-end happy path)
- TC-012: Błąd przy pustych danych dostawy
- TC-013: Weryfikacja podsumowania zamówienia przed finalizacją
"""

import pytest
from pages.login_page import LoginPage
from conftest import VALID_USER, VALID_PASSWORD


class TestCheckout:

    @pytest.fixture(autouse=True)
    def setup_cart(self, page):
        """Loguje i dodaje produkt do koszyka przed każdym testem."""
        login = LoginPage(page)
        login.navigate()
        login.login(VALID_USER, VALID_PASSWORD)
        # Dodaj pierwszy produkt
        page.locator(".btn_primary.btn_inventory").first.click()
        # Przejdź do koszyka
        page.locator(".shopping_cart_link").click()

    def test_TC011_complete_checkout_flow(self, page):
        """TC-011: Pełny, pomyślny przepływ zakupu od koszyka do potwierdzenia."""
        # Krok 1: Rozpocznij zakup
        page.locator("[data-test='checkout']").click()
        assert "/checkout-step-one" in page.url

        # Krok 2: Wprowadź dane dostawy
        page.locator("[data-test='firstName']").fill("Jan")
        page.locator("[data-test='lastName']").fill("Kowalski")
        page.locator("[data-test='postalCode']").fill("20-001")
        page.locator("[data-test='continue']").click()

        # Krok 3: Potwierdź podsumowanie
        assert "/checkout-step-two" in page.url
        page.locator("[data-test='finish']").click()

        # Weryfikacja: strona potwierdzenia zamówienia
        assert "/checkout-complete" in page.url
        confirmation = page.locator(".complete-header")
        assert "Thank you" in confirmation.inner_text()

    def test_TC012_checkout_empty_first_name(self, page):
        """TC-012: Próba przejścia dalej przy pustym polu imienia."""
        page.locator("[data-test='checkout']").click()

        # Zostawiamy puste imię, wypełniamy resztę
        page.locator("[data-test='lastName']").fill("Kowalski")
        page.locator("[data-test='postalCode']").fill("20-001")
        page.locator("[data-test='continue']").click()

        error = page.locator("[data-test='error']")
        assert error.is_visible(), "Komunikat błędu powinien być widoczny"
        assert "First Name is required" in error.inner_text()

    def test_TC013_order_summary_contains_product(self, page):
        """TC-013: Podsumowanie zamówienia zawiera dodany produkt."""
        page.locator("[data-test='checkout']").click()

        page.locator("[data-test='firstName']").fill("Jan")
        page.locator("[data-test='lastName']").fill("Kowalski")
        page.locator("[data-test='postalCode']").fill("20-001")
        page.locator("[data-test='continue']").click()

        # Na stronie podsumowania powinien być przynajmniej jeden produkt
        items = page.locator(".cart_item")
        assert items.count() >= 1, "Podsumowanie powinno zawierać co najmniej jeden produkt"
