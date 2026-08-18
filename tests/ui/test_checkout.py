import pytest

pytestmark = pytest.mark.ui


class TestCheckout:
    def test_checkout_completo(self, logged_in_inventory_page, cart_page, checkout_page):
        logged_in_inventory_page.add_backpack_to_cart()
        logged_in_inventory_page.open_cart()

        cart_page.go_to_checkout()

        checkout_page.fill_checkout_info("Jon", "Morgan", "12345")
        checkout_page.continue_checkout()
        checkout_page.finish_checkout()

        assert checkout_page.is_order_complete()
        assert checkout_page.get_message() == "Thank you for your order!"

    def test_checkout_cancel(self, logged_in_inventory_page, cart_page, checkout_page):
        logged_in_inventory_page.add_backpack_to_cart()
        logged_in_inventory_page.open_cart()

        cart_page.go_to_checkout()
        checkout_page.fill_checkout_info("Jon", "Morgan", "12345")
        checkout_page.cancel_checkout()

        assert "cart.html" in checkout_page.page.url

    def test_erro_firtname(self, logged_in_inventory_page, cart_page, checkout_page):
        logged_in_inventory_page.add_backpack_to_cart()
        logged_in_inventory_page.open_cart()
        
        cart_page.go_to_checkout()
        checkout_page.fill_checkout_info("", "Morgan", "12345")
        checkout_page.continue_checkout()

        assert "Error: First Name is required" == checkout_page.get_error_message()

    def test_checkout_sem_last_name(self, logged_in_inventory_page, cart_page, checkout_page):
        logged_in_inventory_page.add_backpack_to_cart()
        logged_in_inventory_page.open_cart()
        cart_page.go_to_checkout()

        checkout_page.fill_checkout_info("John", "", "12345")
        checkout_page.continue_checkout()

        assert "Error: Last Name is required" in checkout_page.get_error_message()

    def test_checkout_sem_postal_code(self, logged_in_inventory_page, cart_page, checkout_page):
        logged_in_inventory_page.add_backpack_to_cart()
        logged_in_inventory_page.open_cart()
        cart_page.go_to_checkout()

        checkout_page.fill_checkout_info("John", "Doe", "")
        checkout_page.continue_checkout()

        assert "Error: Postal Code is required" in checkout_page.get_error_message()
    
    def test_checkout_resumo_valores(self, logged_in_inventory_page, cart_page, checkout_page):
        logged_in_inventory_page.add_backpack_to_cart()
        logged_in_inventory_page.add_bike_light_to_cart()
        logged_in_inventory_page.open_cart()
        cart_page.go_to_checkout()

        checkout_page.fill_checkout_info("John", "Doe", "12345")
        checkout_page.continue_checkout()

        subtotal = checkout_page.get_subtotal()
        tax = checkout_page.get_tax()
        total = checkout_page.get_total()

        assert round(subtotal + tax, 2) == round(total, 2)

    def test_cancelar_checkout_volta_para_carrinho(self, logged_in_inventory_page, cart_page, checkout_page, page):
        logged_in_inventory_page.add_backpack_to_cart()
        logged_in_inventory_page.open_cart()
        cart_page.go_to_checkout()

        checkout_page.cancel_checkout()

        assert "cart.html" in page.url

    def test_voltar_para_produtos_apos_pedido(self, logged_in_inventory_page, cart_page, checkout_page):
        logged_in_inventory_page.add_backpack_to_cart()
        logged_in_inventory_page.open_cart()
        cart_page.go_to_checkout()

        checkout_page.fill_checkout_info("John", "Doe", "12345")
        checkout_page.continue_checkout()
        checkout_page.finish_checkout()
        checkout_page.back_to_products()

        assert logged_in_inventory_page.is_inventory_visible()