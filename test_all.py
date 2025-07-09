import pytest  # type: ignore
from playwright.sync_api import sync_playwright  # type: ignore
from pages.drag_and_drop_page import DragAndDropPage  # type: ignore
from pages.scrolling_dropdown_page import ScrollingDropdownPage  # type: ignore
from pages.shadow_dom_page import ShadowDomPage  # type: ignore
from pages.slider_page import SliderPage  # type: ignore
from pages.upload_page import UploadPage  # type: ignore
from pages.pagination_web_table_page import PaginationWebTablePage  # type: ignore
from pages.svg_elements_page import SVGElementsPage  # type: ignore
import os

# Note: For image comparison, you would need to install Pillow and numpy, and optionally image comparison libraries.

def test_drag_and_drop():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        drag_and_drop_page = DragAndDropPage(page)
        drag_and_drop_page.goto()
        drag_and_drop_page.drag_and_drop()
        browser.close()

def test_select_6th_option_in_scrolling_dropdown():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        dropdown_page = ScrollingDropdownPage(page)
        dropdown_page.goto()
        dropdown_page.open_dropdown()
        dropdown_page.select_option_by_index(5)
        browser.close()

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

def test_upload_file():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        upload_page = UploadPage(page)
        upload_page.goto()
        upload_page.upload_file('/home/l4w45h-linux/Downloads/discord-0.0.98.deb')
        browser.close()

def test_pag_table_and_total_price():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        pagination_page = PaginationWebTablePage(page)
        pagination_page.goto()
        result = pagination_page.get_all_products_and_total_price()
        print('All products:', result['all_products'])
        rounded_price = round(result['total_price'])
        print('Total price:', rounded_price)
        browser.close()

def test_svg_elements_screenshot_comparison():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        svg_page = SVGElementsPage(page)
        svg_page.goto()
        svgs = svg_page.get_all_svg_elements()
        assert len(svgs) > 0
        # Screenshot comparison logic would go here, using Pillow/numpy or similar
        # For now, just take screenshots
        screenshots = svg_page.screenshot_all_svgs(os.path.join(os.path.dirname(__file__), 'files'))
        print('SVG screenshots:', screenshots)
        browser.close() 