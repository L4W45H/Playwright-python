import pytest  # type: ignore
from playwright.sync_api import sync_playwright  # type: ignore
from pages.upload_page import UploadPage  # type: ignore

def test_upload_file():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        upload_page = UploadPage(page)
        upload_page.goto()
        upload_page.upload_file('/home/l4w45h-linux/Downloads/discord-0.0.98.deb')
        print('Upload test completed.')
        browser.close() 