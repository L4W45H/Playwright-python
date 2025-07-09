import pytest  # type: ignore
from playwright.sync_api import sync_playwright  # type: ignore
from pages.scrolling_dropdown_page import ScrollingDropdownPage  # type: ignore

def test_select_6th_option_in_scrolling_dropdown():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        dropdown_page = ScrollingDropdownPage(page)
        dropdown_page.goto()
        dropdown_page.open_dropdown()
        dropdown_page.select_option_by_index(5)
        print('6th option selected in Scrolling DropDown.')
        browser.close() 