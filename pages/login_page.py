from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email = page.get_by_test_id("email")
        self.password = page.get_by_test_id("password")
        self.submit = page.get_by_test_id("login-submit")
        self.error = page.get_by_test_id("login-error")

    def open(self):
        self.page.goto("/auth/login")
        self.page.wait_for_load_state("networkidle")
        expect(self.submit).to_be_enabled()

    def sign_in(self, user: dict):
        self.email.fill(user["email"])
        self.password.fill(user["password"])
        self.submit.click()