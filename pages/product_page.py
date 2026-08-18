from pages.base_page import BasePage

class ProductPage(BasePage):
    PRODUCT_NAME = ".inventory_details_name"
    PRODUCT_DESC = ".inventory_details_desc"
    PRODUCT_PRICE = ".inventory_details_price"
    ADD_TO_CART_BUTTON = "button[id^='add-to-cart']"
    REMOVE_BUTTON = "button[id^='remove']"
    BACK_BUTTON = "#back-to-products"

    def get_product_name(self) -> str:
        return self.page.inner_text((self.PRODUCT_NAME))

    def add_to_cart(self):
        return self.page.click(self.ADD_TO_CART_BUTTON)

    def remove_from_cart(self):
        return self.page.click(self.REMOVE_BUTTON)

    def back_to_products(self):
        return self.page.click(self.BACK_BUTTON)

    def is_add_to_cart_visible(self) -> bool:
        return self.page.is_visible(self.ADD_TO_CART_BUTTON)

    def get_product_name(self) -> str:
            return self.page.inner_text((self.PRODUCT_NAME))