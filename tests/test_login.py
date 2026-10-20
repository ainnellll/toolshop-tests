import re

from playwright.sync_api import Page, expect

from data.user_factory import unknown_user


def test_valid_credentials_open_the_account_page(
    registered_customer, login_page, page: Page
):
    login_page.open()
    login_page.sign_in(registered_customer)

    expect(page).to_have_url(re.compile(r"/account"))


def test_wrong_credentials_show_an_error(login_page, page: Page):
    login_page.open()
    login_page.sign_in(unknown_user())

    expect(login_page.error).to_contain_text("Invalid email or password")
    expect(page).not_to_have_url(re.compile(r"/account"))