from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEM = ".cart_item"
    PRODUCT_NAME = ".inventory_item_name"

    def cart_visible(self)-> bool:
        return self.page.cart_visible(self.CART_ITEM)

    def get_product_name(self) -> str:
        return self.page.locator(self.PRODUCT_NAME).first.inner_text()
    
