from playwright.sync_api import expect


def test_known_email_shows_a_confirmation(registered_customer, forgot_password_page):
    forgot_password_page.open()
    forgot_password_page.request_reset(registered_customer["email"])

    # сайт показывает подтверждение (и не показывает ошибку)
    expect(forgot_password_page.form).to_contain_text("forgot-password.confirm")
    expect(forgot_password_page.invalid_email_error).to_have_count(0)


def test_unknown_email_shows_an_error(forgot_password_page):
    forgot_password_page.open()
    forgot_password_page.request_reset("nobody-reset@example.com")

    expect(forgot_password_page.invalid_email_error).to_be_visible()