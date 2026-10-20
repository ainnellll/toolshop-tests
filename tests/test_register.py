import re

from playwright.sync_api import Page, expect

from data.user_factory import new_customer


def test_new_customer_can_register(register_page, page: Page):
    register_page.open()
    register_page.register(new_customer())

    
    expect(page).to_have_url(re.compile(r"/auth/login"))