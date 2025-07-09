# Requires: pip install playwright
from playwright.sync_api import Page  # type: ignore

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://testautomationpractice.blogspot.com/'

    def goto(self):
        self.page.goto(self.url) 