
```python
from playwright.sync_api import sync_playwright


def test_add_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        page.click("#add-to-cart-sauce-labs-backpack")
        page.click(".shopping_cart_link")

        cart_item = page.locator(".inventory_item_name")
        assert cart_item.is_visible()

        browser.close()
```
