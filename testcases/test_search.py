from playwright.sync_api import sync_playwright


def test_search_product():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Open website
        page.goto("https://www.saucedemo.com/")

        # Login
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Verify product list is displayed
        products = page.locator(".inventory_item")
        assert products.count() > 0

        # Verify first product is visible
        first_product = page.locator(".inventory_item_name").first
        assert first_product.is_visible()

        browser.close()
