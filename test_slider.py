import pytest  # type: ignore
from playwright.sync_api import sync_playwright  # type: ignore
from pages.slider_page import SliderPage  # type: ignore

def test_move_slider():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        slider_page = SliderPage(page)
        slider_page.goto()
        slider_page.move_slider(0.2, 0.9)
        value = slider_page.get_slider_value()
        print('Slider value:', value)
        browser.close() 