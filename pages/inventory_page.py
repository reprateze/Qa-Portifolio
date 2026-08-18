from pages.base_page import BasePage


class InventoryPage(BasePage):

    INVENTORY_LIST = ".inventory_list"

    ADD_BACKPACK = "#add-to-cart-sauce-labs-backpack"
    ADD_BIKE_LIGHT = "#add-to-cart-sauce-labs-bike-light"
    ADD_BOLT_T_SHIRT = "#add-to-cart-sauce-labs-bolt-t-shirt"

    REMOVE_BACKPACK = "#remove-sauce-labs-backpack"

    CART_LINK = ".shopping_cart_link"
    CART_BADGE = ".shopping_cart_badge"

    PRODUCT_SORT = ".product_sort_container"

    

    def is_inventory_visible(self) -> bool:
        return self.page.is_visible(self.INVENTORY_LIST)

    def add_backpack_to_cart(self):
        self.page.click(self.ADD_BACKPACK)

    def add_bike_light_to_cart(self):
        self.page.click(self.ADD_BIKE_LIGHT)

    def add_bolt_t_shirt_to_cart(self):
        self.page.click(self.ADD_BOLT_T_SHIRT)

    def remove_backpack(self):
        self.page.click(self.REMOVE_BACKPACK)

    def get_cart_quantity(self) -> int:
        return int(self.page.inner_text(self.CART_BADGE))

    def is_cart_empty(self) -> bool:
        return not self.page.is_visible(self.CART_BADGE)

    def open_cart(self):
        self.page.click(self.CART_LINK)

    def sort_products_by_name(self):
      self.page.select_option(self.PRODUCT_SORT, "za")

    def get_first_product(self) -> str:
        return self.page.locator(".inventory_item_name").first.inner_text()

    def sort_by_lowhigh(self):
        self.page.select_option(self.PRODUCT_SORT,"lohi")

    def get_product_prices(self) -> list[float]:
        texts = self.page.locator(".inventory_item_price").all_inner_texts()
        return [float(t.replace("$", "")) for t in texts]

    def sort_products_by_price_high_to_low(self):
        self.page.select_option(self.PRODUCT_SORT, "hilo")

    def open_product(self, product_name: str):
        self.page.click(f"text={product_name}")
