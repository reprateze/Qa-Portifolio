from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"
    INVENTORY_LIST = ".inventory_list"

    def login(self, username: str, password: str):
        self.goto("/")
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.page.inner_text(self.ERROR_MESSAGE)

    def is_logged_in(self) -> bool:
        return self.page.is_visible(self.INVENTORY_LIST)
