import pytest  # type: ignore
from pages.shadow_dom_page import ShadowDomPage  # type: ignore

def test_fill_and_verify_shadow_dom(page):
    shadow_dom_page = ShadowDomPage(page)
    shadow_dom_page.goto()
    shadow_dom_page.fill_shadow_input('Hello Shadow DOM!')
    value = shadow_dom_page.get_shadow_input_value()
    assert value == 'Hello Shadow DOM!' 