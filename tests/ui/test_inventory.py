import pytest

pytestmark = pytest.mark.ui


class TestInventory:

    def test_acessar_lista_de_produtos(self, logged_in_inventory_page):
        assert logged_in_inventory_page.is_inventory_visible()

    def test_adicionar_produto_ao_carrinho(self, logged_in_inventory_page):
        logged_in_inventory_page.add_backpack_to_cart()

        assert logged_in_inventory_page.get_cart_quantity() == 1

    def test_adicionar_multiplos_produtos_ao_carrinho(self, logged_in_inventory_page):
        logged_in_inventory_page.add_backpack_to_cart()
        logged_in_inventory_page.add_bike_light_to_cart()
        logged_in_inventory_page.add_bolt_t_shirt_to_cart()

        assert logged_in_inventory_page.get_cart_quantity() == 3

    def test_remover_backpack(self, logged_in_inventory_page):
        logged_in_inventory_page.add_backpack_to_cart()
        logged_in_inventory_page.remove_backpack()

        assert logged_in_inventory_page.is_cart_empty()

    def test_ordenar_produtos_por_nome(self, logged_in_inventory_page):
        logged_in_inventory_page.sort_products_by_name()

        assert logged_in_inventory_page.get_first_product() == "Test.allTheThings() T-Shirt (Red)"

    def test_ordenar_produtos_menor_maior(self, logged_in_inventory_page):
        logged_in_inventory_page.sort_by_lowhigh()

        prices = logged_in_inventory_page.get_product_prices()

        assert prices == sorted(prices)

    def test_ordenar_produtos_maior_menor(self, logged_in_inventory_page):
        logged_in_inventory_page.sort_products_by_price_high_to_low()

        prices = logged_in_inventory_page.get_product_prices()

        assert prices == sorted(prices, reverse=True)