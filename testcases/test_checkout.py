from playwright.sync_api import sync_playwright


def test_checkout():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Open website
        page.goto("https://www.saucedemo.com/")

        # Login
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Add product to cart
        page.click("#add-to-cart-sauce-labs-backpack")

        # Open cart
        page.click(".shopping_cart_link")

        # Proceed to checkout
        page.click("#checkout")

        # Fill checkout details
        page.fill("#first-name", "John")
        page.fill("#last-name", "Doe")
        page.fill("#postal-code", "500001")

        # Continue checkout
        page.click("#continue")

        # Verify checkout overview page
        assert "checkout-step-two" in page.url

        # Finish order
        page.click("#finish")

        # Verify order completion
        success_message = page.locator(".complete-header")
        assert success_message.is_visible()

        browser.close()
