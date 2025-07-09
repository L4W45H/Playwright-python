import pytest  # type: ignore
from playwright.sync_api import sync_playwright  # type: ignore
from pages.shadow_dom_page import ShadowDomPage  # type: ignore

def test_fill_and_verify_shadow_dom():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        shadow_dom_page = ShadowDomPage(page)
        shadow_dom_page.goto()
        shadow_dom_page.fill_shadow_input('Hello Shadow DOM!')
        value = shadow_dom_page.get_shadow_input_value()
        assert value == 'Hello Shadow DOM!'
        browser.close() 