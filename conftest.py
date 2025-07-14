import pytest
from playwright.sync_api import sync_playwright
import os

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page is not None:
            screenshots_dir = os.path.join(os.path.dirname(__file__), 'screenshots')
            os.makedirs(screenshots_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
            page.screenshot(path=screenshot_path)
            # Attach screenshot to HTML report
            try:
                from pytest_html import extras
                extra_image = extras.image(screenshot_path)
            except ImportError:
                extra_image = None
            if hasattr(rep, "extra"):
                rep.extra.append(extra_image)
            else:
                rep.extra = [extra_image] if extra_image else [] 