from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.continue_after_sign_in_button = page.get_by_test_id("proceed-2")
        self.country = page.get_by_test_id("country")
        self.postal_code = page.get_by_test_id("postal_code")
        self.house_number = page.get_by_test_id("house_number")
        self.street = page.get_by_test_id("street")
        self.city = page.get_by_test_id("city")
        self.state = page.get_by_test_id("state")
        self.continue_after_billing_button = page.get_by_test_id("proceed-3")
        self.payment_method = page.get_by_test_id("payment-method")
        self.confirm = page.get_by_test_id("finish")
        self.payment_success = page.get_by_text("Payment was successful")

    def continue_after_sign_in(self):
        self.continue_after_sign_in_button.click()

    def fill_billing_address(self, address: dict):
        self.country.select_option(address["country"])
        self.postal_code.fill(address["postal_code"])
        self.house_number.fill(address["house_number"])
        self.street.fill(address["street"])
        self.city.fill(address["city"])
        self.state.fill(address["state"])
        self.continue_after_billing_button.click()

    def pay_cash_on_delivery(self):
        self.payment_method.select_option("cash-on-delivery")
        self.confirm.click()