import pytest

pytestmark = pytest.mark.ui

class TestProduct:
  def test_open_product(self, logged_in_inventory_page, product_page, page):
    logged_in_inventory_page.open_product("Sauce Labs Backpack")
    assert product_page.get_product_name() == "Sauce Labs Backpack"

  def test_add_cart(self, logged_in_inventory_page, product_page):
    logged_in_inventory_page.open_product("Sauce Labs Backpack")

    product_page.add_to_cart()

    assert logged_in_inventory_page.get_cart_quantity() == 1

  def test_remove_cart(self, logged_in_inventory_page, product_page):
    logged_in_inventory_page.open_product("Sauce Labs Backpack")
    product_page.add_to_cart()
    product_page.remove_from_cart()

    assert logged_in_inventory_page.is_cart_empty()

  def test_voltar_para_lista_de_produtos(self, logged_in_inventory_page, product_page):
    logged_in_inventory_page.open_product("Sauce Labs Backpack")
    product_page.back_to_products()

    assert logged_in_inventory_page.is_inventory_visible()

