from playwright.sync_api import expect

from data.user_factory import BILLING_ADDRESS


def test_buy_a_product_with_cash_on_delivery(
    registered_customer, product_page, cart_page, login_page, checkout_page
):
    product_page.open_home()
    product_page.open_first_product()
    chosen_name = product_page.read_name()

    product_page.add_to_cart()
    product_page.open_cart()

    # в корзине именно тот товар и одна штука
    expect(cart_page.item_names).to_have_text([chosen_name])
    expect(cart_page.quantity).to_have_value("1")

    cart_page.proceed_to_checkout()
    login_page.sign_in(registered_customer)
    checkout_page.continue_after_sign_in()
    checkout_page.fill_billing_address(BILLING_ADDRESS)
    checkout_page.pay_cash_on_delivery()

    expect(checkout_page.payment_success).to_be_visible()