import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage

load_dotenv()

UI_BASE_URL = "https://www.saucedemo.com"
API_BASE_URL = "https://reqres.in/api"

STANDARD_USER = "problem_user"
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

@pytest.fixture
def product_page(page):
    return ProductPage(page)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page is not None:
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot_path = f"reports/screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)

            if "pytest_html" in item.config.pluginmanager.list_name_plugin():
                extra = getattr(report, "extra", [])
                from pytest_html import extras
                extra.append(extras.image(screenshot_path))
                report.extra = extra