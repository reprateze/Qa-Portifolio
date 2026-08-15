import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

pytestmark = pytest.mark.ui


class TestInventory:

    def test_acessar_lista_de_produtos(self, page):
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.login("standard_user", "secret_sauce")

        assert inventory_page.is_inventory_visible()

    def test_adicionar_produto_ao_carrinho(self, page):
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.login("standard_user", "secret_sauce")

        inventory_page.add_backpack_to_cart()

        assert inventory_page.get_cart_quantity() == 1

    def test_adicionar_multiplos_produtos_ao_carrinho(self, page):
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.login("standard_user", "secret_sauce")

        inventory_page.add_backpack_to_cart()
        inventory_page.add_bike_light_to_cart()
        inventory_page.add_bolt_t_shirt_to_cart()

        assert inventory_page.get_cart_quantity() == 3

    def test_remover_Backpack(self, page):
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.login("standard_user", "secret_sauce")

        inventory_page.add_backpack_to_cart()
        inventory_page.remove_backpack()

        assert inventory_page.is_cart_empty()

    def test_OrderList(self, page):
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)
        
        login_page.login("standard_user", "secret_sauce")

        inventory_page.sort_products_by_name()

        assert inventory_page.get_first_product() == "Test.allTheThings() T-Shirt (Red)"

    def test_Orderlist_LowHigh(self,page):
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)
                
        login_page.login("standard_user", "secret_sauce")

        inventory_page.sort_by_lowhigh()

        prices = inventory_page.get_product_prices()

        assert prices == sorted(prices)

    def test_ordenar_produtos_preco_maior_menor(self, page):
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.login("standard_user", "secret_sauce")

        inventory_page.sort_products_by_price_high_to_low()

        prices = inventory_page.get_product_prices()

        assert prices == sorted(prices, reverse=True)
      

       