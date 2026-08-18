import pytest

pytestmark = pytest.mark.ui


class TestCart:

    def test_added_product_visibility_in_cart(self, logged_in_inventory_page, cart_page):
        logged_in_inventory_page.add_backpack_to_cart()
        logged_in_inventory_page.open_cart()

        assert cart_page.get_product_name() == "Sauce Labs Backpack"

    def test_multiplos_produtos_no_carrinho(self, logged_in_inventory_page, cart_page):
        logged_in_inventory_page.add_backpack_to_cart()
        logged_in_inventory_page.add_bike_light_to_cart()
        logged_in_inventory_page.add_bolt_t_shirt_to_cart()

        logged_in_inventory_page.open_cart()

        products = cart_page.get_product_names()

        expected_products = [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
        ]
        assert products == expected_products

    def test_remover_backpack(self, logged_in_inventory_page, cart_page):
        logged_in_inventory_page.add_backpack_to_cart()
        logged_in_inventory_page.add_bike_light_to_cart()
        logged_in_inventory_page.add_bolt_t_shirt_to_cart()

        logged_in_inventory_page.open_cart()

        cart_page.remove_product("sauce-labs-backpack")

        assert not cart_page.is_backpack_visible()

    def test_remover_produto_mantem_outros_no_carrinho(self, logged_in_inventory_page, cart_page):
        logged_in_inventory_page.add_backpack_to_cart()
        logged_in_inventory_page.add_bike_light_to_cart()
        logged_in_inventory_page.open_cart()

        cart_page.remove_product("sauce-labs-backpack")

        assert cart_page.get_product_names() == ["Sauce Labs Bike Light"]

    def test_empty_cart(self, logged_in_inventory_page, cart_page):
        logged_in_inventory_page.open_cart()

        assert cart_page.get_product_names() == []

    def test_continue_Shopping(self, logged_in_inventory_page, cart_page):
        logged_in_inventory_page.open_cart()
        cart_page.continue_shopping()

        assert logged_in_inventory_page.is_inventory_visible()

    def test_go_to_checkout(self, logged_in_inventory_page, cart_page, page):
        logged_in_inventory_page.add_backpack_to_cart()
        logged_in_inventory_page.open_cart()
        cart_page.go_to_checkout()

        assert "checkout-step-one" in page.url
