# Playwright-Automation-Testing-Project
Developed a web automation testing framework using Playwright with Python for validating login, cart, and logout functionalities of a sample e-commerce application. Implemented automated UI test cases using Pytest and improved regression testing efficiency.
Playwright + Python Automation Testing Project

Project Title

E-Commerce Website Automation Testing using Playwright with Python

Project Description

This project automates core functionalities of a sample e-commerce web application using Playwright with Python. The automation framework validates key user workflows, including login, product search, adding to cart, checkout, and logout.

The objective of the project is to reduce repetitive manual testing effort and improve test execution efficiency.

Technologies Used

Python

Playwright

Pytest

HTML Reports

VS Code

Features Automated

Login functionality

Invalid login validation

Product search

Add to cart

Checkout

Logout functionality

UI element validations

Project Structure

playwright-python-project/
│
├── tests/
│   ├── test_login.py
│   ├── test_search.py
|   |__ test_checkout.py
|   |__ test_logout.py
│   └── test_cart.py
│
├── pages/
│   └── login_page.py
│
├── requirements.txt
├── pytest.ini
└── README.md

Installation Steps

pip install playwright
pip install pytest
playwright install

Sample Test Script

test_login.py

from playwright.sync_api import sync_playwright


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        assert "inventory" in page.url

        browser.close()

Sample Search Test

test_search.py

from playwright.sync_api import sync_playwright


def test_product_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        product = page.locator(".inventory_item_name").first
        assert product.is_visible()

        browser.close()

How to Run Tests

pytest

Resume Description

Developed an automation testing project using Playwright with Python to automate login, product validation, cart functionality, and UI workflows for a sample e-commerce application. Implemented automated test execution using Pytest and improved testing efficiency by reducing repetitive manual test execution.

GitHub Repository Name Suggestions

playwright-python-automation

qa-automation-playwright-python

ecommerce-testing-playwright

Additional Improvements You Can Add Later

Page Object Model (POM)

Data-driven testing

HTML reporting

Screenshot capture on failure

GitHub Actions CI/CD integration

API testing with requests/Postman

