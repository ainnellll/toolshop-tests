from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.item_names = page.get_by_test_id("product-title")
        self.quantity = page.get_by_test_id("product-quantity")
        self.proceed = page.get_by_test_id("proceed-1")

    def proceed_to_checkout(self):
        self.proceed.click()