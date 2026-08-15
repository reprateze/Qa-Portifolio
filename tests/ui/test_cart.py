import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


pytestmark = pytest.mark.ui

class TestCart:

    def test_added_product_visibility_in_cart(self, page):
        login_page = LoginPage(page)
        Inventory_page = InventoryPage(page)
        cart_page = CartPage(page)

        login_page.login("standard_user", "secret_sauce")

        Inventory_page.add_backpack_to_cart()
        Inventory_page.open_cart()

        assert cart_page.get_product_name() == "Sauce Labs Backpack"

