from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    CANCEL_BUTTON = "#cancel"
    ERROR_MESSAGE = "[data-test='error']"
    CHECKOUT_INFO = ".checkout_info"

    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    SUBTOTAL_LABEL = ".summary_subtotal_label"
    TAX_LABEL = ".summary_tax_label"
    TOTAL_LABEL = ".summary_total_label"
    FINISH_BUTTON = "#finish"

    COMPLETE_HEADER = ".complete-header"
    BACK_HOME_BUTTON = "#back-to-products"

    def is_checkout_visible(self) -> bool:
        return self.page.is_visible(self.CHECKOUT_INFO)

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.FIRST_NAME_INPUT, first_name)
        self.page.fill(self.LAST_NAME_INPUT, last_name)
        self.page.fill(self.POSTAL_CODE_INPUT, postal_code)

    def continue_checkout(self):
        self.page.click(self.CONTINUE_BUTTON)

    def cancel_checkout(self):
        self.page.click(self.CANCEL_BUTTON)

    def get_error_message(self) -> str:
        return self.page.inner_text(self.ERROR_MESSAGE)

    # ---- Step two ----

    def get_item_names(self) -> list[str]:
        return self.page.locator(self.ITEM_NAME).all_inner_texts()

    def get_subtotal(self) -> float:
        text = self.page.inner_text(self.SUBTOTAL_LABEL)
        return float(text.replace("Item total: $", ""))

    def get_tax(self) -> float:
        text = self.page.inner_text(self.TAX_LABEL)
        return float(text.replace("Tax: $", ""))

    def get_total(self) -> float:
        text = self.page.inner_text(self.TOTAL_LABEL)
        return float(text.replace("Total: $", ""))

    def finish_checkout(self):
        self.page.click(self.FINISH_BUTTON)

    def get_message(self) -> str:
        return self.page.inner_text(self.COMPLETE_HEADER)

    def is_order_complete(self) -> bool:
        return self.page.is_visible(self.COMPLETE_HEADER)

    def back_to_products(self):
        self.page.click(self.BACK_HOME_BUTTON)