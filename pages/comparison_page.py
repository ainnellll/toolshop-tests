from playwright.sync_api import Page


class ComparisonPage:
    def __init__(self, page: Page):
        self.page = page
        # название товара лежит в заголовке каждого столбца таблицы
        self.names = page.get_by_role("columnheader").get_by_test_id("product-name")

    def price_cell(self, price: str):
        return self.page.get_by_text(price, exact=True)