import re

from playwright.sync_api import Page, expect


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        # у каждой карточки товара своё уникальное имя: product-<длинный номер>
        self.cards = page.get_by_test_id(re.compile(r"^product-[0-9A-Z]{10,}$"))
        self.name = page.get_by_test_id("product-name")
        self.add_to_cart_button = page.get_by_test_id("add-to-cart")
        self.cart_icon = page.get_by_test_id("nav-cart")

    def open_home(self):
        self.page.goto("/")
        expect(self.cards.first).to_be_visible()

    def open_first_product(self):
        self.cards.first.click()
        expect(self.name).to_be_visible()

    def read_name(self) -> str:
        return self.name.inner_text().strip()

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def open_cart(self):
        self.cart_icon.click()