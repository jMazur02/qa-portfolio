"""
Testy koszyka zakupów aplikacji SauceDemo.

Pokryte przypadki testowe:
- TC-007: Dodanie produktu do koszyka
- TC-008: Usunięcie produktu z koszyka
- TC-009: Licznik koszyka aktualizuje się poprawnie
- TC-010: Koszyk zachowuje zawartość po powrocie ze strony produktu
"""

import pytest
from pages.login_page import LoginPage
from conftest import VALID_USER, VALID_PASSWORD


class TestCart:

    @pytest.fixture(autouse=True)
    def login_before_each(self, page):
        """Loguje użytkownika przed każdym testem i resetuje stan koszyka."""
        login = LoginPage(page)
        login.navigate()
        login.login(VALID_USER, VALID_PASSWORD)
        assert "/inventory" in page.url

        # Reset koszyka: usuwamy wszystkie produkty które mogły zostać z poprzedniego testu
        # (sesja przeglądarki jest współdzielona, więc lokalny storage może zawierać resztki)
        page.evaluate("window.localStorage.clear()")
        page.reload()
        page.wait_for_url("**/inventory.html")

    def test_TC007_add_item_to_cart(self, page):
        """TC-007: Dodanie pierwszego produktu do koszyka."""
        # Klikamy przycisk "Add to cart" przy pierwszym produkcie
        page.locator(".btn_primary.btn_inventory").first.click()

        # Sprawdzamy czy licznik koszyka pokazuje "1"
        cart_badge = page.locator(".shopping_cart_badge")
        assert cart_badge.inner_text() == "1", (
            f"Licznik koszyka powinien wynosić 1, wynosi: {cart_badge.inner_text()}"
        )

    def test_TC008_remove_item_from_cart(self, page):
        """TC-008: Usunięcie produktu z koszyka."""
        # Najpierw dodajemy produkt
        page.locator(".btn_primary.btn_inventory").first.click()

        # Następnie usuwamy (przycisk zmienia się na "Remove")
        page.locator(".btn_secondary.btn_inventory").first.click()

        # Licznik koszyka powinien zniknąć (brak elementu = koszyk pusty)
        cart_badge = page.locator(".shopping_cart_badge")
        assert not cart_badge.is_visible(), "Licznik koszyka powinien zniknąć po usunięciu produktu"

    def test_TC009_cart_counter_updates(self, page):
        """TC-009: Licznik koszyka aktualizuje się po dodaniu wielu produktów."""
        add_buttons = page.locator(".btn_primary.btn_inventory")

        # Dodajemy dwa pierwsze produkty
        add_buttons.nth(0).click()
        add_buttons.nth(1).click()

        cart_badge = page.locator(".shopping_cart_badge")
        assert cart_badge.inner_text() == "2", (
            f"Licznik koszyka powinien wynosić 2, wynosi: {cart_badge.inner_text()}"
        )

    def test_TC010_cart_persists_on_navigation(self, page):
        """TC-010: Koszyk zachowuje zawartość po wejściu na stronę szczegółów produktu."""
        # Dodajemy produkt do koszyka
        page.locator(".btn_primary.btn_inventory").first.click()

        # Wchodzimy w szczegóły pierwszego produktu
        page.locator(".inventory_item_name").first.click()

        # Wracamy do listy produktów
        page.go_back()

        # Koszyk dalej powinien mieć 1 produkt
        cart_badge = page.locator(".shopping_cart_badge")
        assert cart_badge.inner_text() == "1", "Koszyk powinien zachować zawartość po nawigacji"
