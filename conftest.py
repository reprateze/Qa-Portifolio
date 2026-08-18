import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

load_dotenv()

UI_BASE_URL = "https://www.saucedemo.com"
API_BASE_URL = "https://reqres.in/api"

STANDARD_USER = "standard_user"
STANDARD_PASSWORD = "secret_sauce"


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context(base_url=UI_BASE_URL)
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def api_base_url():
    return API_BASE_URL


@pytest.fixture
def api_headers():
    return {
        "x-api-key": os.getenv("REQRES_API_KEY"),
        "Content-Type": "application/json",
    }


# ---- Page Objects ----

@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


# ---- Estado pré-condicionado: usuário já logado ----

@pytest.fixture
def logged_in_inventory_page(login_page, inventory_page):
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)
    return inventory_page

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)