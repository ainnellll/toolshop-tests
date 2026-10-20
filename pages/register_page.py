from playwright.sync_api import Page, expect


class RegisterPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.get_by_test_id("first-name")
        self.last_name = page.get_by_test_id("last-name")
        self.dob = page.get_by_test_id("dob")
        self.country = page.get_by_test_id("country")
        self.postal_code = page.get_by_test_id("postal_code")
        self.house_number = page.get_by_test_id("house_number")
        self.street = page.get_by_test_id("street")
        self.city = page.get_by_test_id("city")
        self.state = page.get_by_test_id("state")
        self.phone = page.get_by_test_id("phone")
        self.email = page.get_by_test_id("email")
        self.password = page.get_by_test_id("password")
        self.submit = page.get_by_test_id("register-submit")

    def open(self):
        self.page.goto("/auth/register")
        self.page.wait_for_load_state("networkidle")
        expect(self.submit).to_be_enabled()

    def register(self, user: dict):
        self.first_name.fill(user["first_name"])
        self.last_name.fill(user["last_name"])
        self.dob.fill(user["dob"])
        self.country.select_option(user["country"])
        self.postal_code.fill(user["postal_code"])
        self.house_number.fill(user["house_number"])
        self.street.fill(user["street"])
        self.city.fill(user["city"])
        self.state.fill(user["state"])
        self.phone.fill(user["phone"])
        self.email.fill(user["email"])
        self.password.fill(user["password"])
        self.submit.click()