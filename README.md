# Playwright-Automation-Testing-Project

## Project Title

E-Commerce Website Automation Testing using Playwright with Python

## Project Description

This project automates core functionalities of a sample e-commerce web application using Playwright with Python. The automation framework validates key user workflows, including login, product search, adding to cart, checkout, and logout.

The objective of the project is to reduce repetitive manual testing effort and improve test execution efficiency.

## Technologies Used

* Python

* Playwright

* Pytest

* HTML Reports

* VS Code

## Features Automated

~ Login functionality

~ Invalid login validation

~ Product search

~ Add to cart

~ Checkout

~ Logout functionality

~ UI element validations

## Project Structure

- `playwright-python-project/testcases/`
   -  `test_login.py`
   -  `test_search.py`
   -  `test_checkout.py`
   -  `test_cart.py`
   -  `test_logout.py`
- `pages/login_page.py`
- `requirements.txt`
- `pytest.ini`

## Installation Steps

```bash
pip install playwright
pip install pytest
playwright install
```

## Sample Test Script

## test_login.py


```python
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
```


## Sample Search Test

## test_search.py

```python
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
```


## Run Tests

```bash
pytest
```

## Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

## Commands to Run

```bash
pip install -r requirements.txt
playwright install
pytest
```


