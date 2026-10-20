import re

import pytest
from playwright.sync_api import expect

from data.user_factory import new_customer
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.comparison_page import ComparisonPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
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


@pytest.fixture
def product_page(page):
    return ProductPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)


@pytest.fixture
def comparison_page(page):
    return ComparisonPage(page)


@pytest.fixture
def forgot_password_page(page):
    return ForgotPasswordPage(page)


@pytest.fixture
def registered_customer(page, register_page):
    """Создаёт нового пользователя для одного теста и отдаёт его данные."""
    user = new_customer()
    register_page.open()
    register_page.register(user)
    expect(page).to_have_url(re.compile(r"/auth/login"))
    return user