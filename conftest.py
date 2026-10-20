import pytest

from pages.login_page import LoginPage
from pages.register_page import RegisterPage


@pytest.fixture(scope="session", autouse=True)
def set_test_id(playwright):
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def register_page(page):
    return RegisterPage(page)