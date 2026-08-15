import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

UI_BASE_URL = "https://www.saucedemo.com"
API_BASE_URL = "https://reqres.in/api"


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