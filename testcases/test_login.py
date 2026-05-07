```python
from playwright.sync_api import sync_playwright


def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        assert "inventory" in page.url

        browser.close()


def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.fill("#user-name", "locked_out_user")
        page.fill("#password", "wrong_password")
        page.click("#login-button")

        error = page.locator("h3")
        assert error.is_visible()

        browser.close()
```
