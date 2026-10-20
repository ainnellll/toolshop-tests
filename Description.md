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

I automated the happy paths and the main error cases of the five required
scenarios. I deliberately left the following out.

### Things a machine cannot judge well
- **Visual appearance and layout** (colours, spacing, how pages look).
  A test can check that an element exists, not that it looks right.
  A human reviewer is better for this.
- **Quality of texts and translations.** For example, the reset-password page shows
  the technical key `page.forgot-password.confirm` instead of a readable sentence.
  My test only checks that this confirmation is shown; whether the wording
  is good needs a person.

### Things I cannot reach from the browser
- **The reset-password email and the link inside it.** The test only checks the
  message on the screen. Opening a real mailbox is outside this project.
- **"Sign in with Google".** It depends on a third-party service and a real
  Google account, so it is not stable or safe to automate here.

### Things I chose not to automate for safety or cost
- **Payment by credit card, bank transfer, buy-now-pay-later and gift card.**
  I only automated cash on delivery. Card payments need extra data, and real
  card details must never be stored in code in a public repository.
- **Account locking after repeated failed logins.** I noticed the site locks an
  account after several wrong attempts. Testing it would deliberately break
  an account, so I did not automate it.
- **Using the shared demo accounts (customer@ and customer2@).** They are shared by
  everyone, and their state changes (an account was locked, and later a password
  stopped working). My tests create their own user instead.

### Things outside the five required scenarios
- Registration with invalid data (wrong date format, weak or leaked password,
  empty required fields). I only automated a successful registration.
- Product search, filters, sorting and favourites.
- Buying several items, changing quantity, out-of-stock products.
- Other browsers and mobile screen sizes (tests run in Chromium only).
- Performance and load testing.

### Known limitation
Each test registers a new user on the public site and I do not delete these
users afterwards, so test accounts accumulate on the demo site.