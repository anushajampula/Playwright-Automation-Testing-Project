```python
from playwright.sync_api import sync_playwright


def test_logout():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        page.click("#react-burger-menu-btn")
        page.click("#logout_sidebar_link")

        assert "saucedemo" in page.url

        browser.close()
```
