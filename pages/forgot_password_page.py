from playwright.sync_api import Page, expect


class ForgotPasswordPage:
    def __init__(self, page: Page):
        self.page = page
        self.link = page.get_by_test_id("forgot-password-link")
        self.email = page.get_by_test_id("email")
        self.submit = page.get_by_test_id("forgot-password-submit")
        self.form = page.get_by_test_id("forgot-password-form")
        self.invalid_email_error = page.get_by_text("The selected email is invalid.")

    def open(self):
        self.page.goto("/auth/login")
        self.page.wait_for_load_state("networkidle")
        expect(self.link).to_be_enabled()
        self.link.click()
        expect(self.form).to_be_visible()

    def request_reset(self, email: str):
        self.email.fill(email)
        self.submit.click()