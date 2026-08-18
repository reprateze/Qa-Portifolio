from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEM = ".cart_item"
    PRODUCT_NAME = ".inventory_item_name"
    CONTINUE_SHOPPING = "#continue-shopping"
    CHECKOUT_BUTTON = "#checkout"

    def cart_visible(self) -> bool:
        return self.page.locator(self.CART_ITEM).first.is_visible()

    def get_product_name(self) -> str:
        return self.page.locator(self.PRODUCT_NAME).first.inner_text()

    def get_product_names(self) -> list[str]:
        return self.page.locator(self.PRODUCT_NAME).all_inner_texts()

    def remove_product(self, product_id: str):
        self.page.click(f"#remove-{product_id}")

    def is_backpack_visible(self) -> bool:
        return self.page.locator(self.PRODUCT_NAME).filter(
        has_text="Sauce Labs Backpack"
     ).is_visible()

    def continue_shopping(self):
        self.page.click(self.CONTINUE_SHOPPING)

    def go_to_checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)
    
    
