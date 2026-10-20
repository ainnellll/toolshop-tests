# Description: what I automated

Site under test: https://practicesoftwaretesting.com
Tools: Python, pytest, Playwright, Page Object pattern.

## Test cases automated
1. **Register a new customer**: a new account with a unique email and
   password is created, and the user is redirected to the login page.
2. **Log in (valid credentials)**: a freshly registered user reaches the account page.
3. **Log in (invalid credentials)**: an unknown user sees "Invalid email or password"
   and does not reach the account page.
4. **Buy a product**: first product is added to the cart, the cart shows the same
   product and quantity 1, checkout with cash on delivery ends with
   "Payment was successful".
5. **Compare two products**: two products from the catalogue are added to the site's
   comparison; the comparison page shows exactly those two names and prices.
6. **Reset password (known email)**: the form shows the confirmation message
   and no error.
7. **Reset password (unknown email)**: the form shows "The selected email is invalid."

## Not automated (and why)
(Своими словами: что вы осознанно не автоматизировали, например проверка
письма для сброса пароля, оплата картой, внешний вид страниц.)