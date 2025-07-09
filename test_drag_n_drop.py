import pytest  # type: ignore
from playwright.sync_api import sync_playwright  # type: ignore
from pages.drag_and_drop_page import DragAndDropPage  # type: ignore

def test_drag_and_drop():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        drag_and_drop_page = DragAndDropPage(page)
        drag_and_drop_page.goto()
        drag_and_drop_page.drag_and_drop()
        print('Drag and drop test completed.')
        browser.close() 