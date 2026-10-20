# Overview: how I checked and corrected the AI output

## What the AI gave me:
advice, guesses about why the tests initially ran separately and then failed together. why 1–2 tests worked at first and then failed because the system temporarily blocked the shared account.

## Decisions I made myself:
- In the purchase test, I didn’t use the specific product number from the codegen record (it may change), but instead took the first product on the page and saved its name. A typo in the file name card_page.py instead of cart_page.py caused Mobilenoter Android to fail.
- The site rejected the password from the leaked password database; the password is now generated randomly.
- Initially, I used ready‑made customer and customer2 accounts. They are shared by everyone, and the password reset test changed the password, which caused the login and purchase tests to fail. I replaced the shared accounts with a registered_customer fixture that registers a new user for each test. Now the tests are independent and can be run in any order and in parallel.
- I didn’t use hardcoded product identifiers from codegen, as they may change.
- I’ve never used `wait_for_timeout`; I used assertions that wait for the page state.