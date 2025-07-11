import pytest  # type: ignore
from pages.drag_and_drop_page import DragAndDropPage  # type: ignore
from pages.scrolling_dropdown_page import ScrollingDropdownPage  # type: ignore
from pages.shadow_dom_page import ShadowDomPage  # type: ignore
from pages.slider_page import SliderPage  # type: ignore
from pages.upload_page import UploadPage  # type: ignore
from pages.pagination_web_table_page import PaginationWebTablePage  # type: ignore
from pages.svg_elements_page import SVGElementsPage  # type: ignore
import os
from PIL import Image, ImageChops



def test_drag_and_drop(page):
    drag_and_drop_page = DragAndDropPage(page)
    drag_and_drop_page.goto()
    drag_and_drop_page.drag_and_drop()

def test_select_6th_option_in_scrolling_dropdown(page):
    dropdown_page = ScrollingDropdownPage(page)
    dropdown_page.goto()
    dropdown_page.open_dropdown()
    dropdown_page.select_option_by_index(5)

def test_fill_and_verify_shadow_dom(page):
    shadow_dom_page = ShadowDomPage(page)
    shadow_dom_page.goto()
    shadow_dom_page.fill_shadow_input('Hello Shadow DOM!')
    value = shadow_dom_page.get_shadow_input_value()
    assert value == 'Hello Shadow DOM!'

def test_move_slider(page):
    slider_page = SliderPage(page)
    slider_page.goto()
    slider_page.move_slider(0.2, 0.9)
    value = slider_page.get_slider_value()
    print('Slider value:', value)

def test_upload_file(page):
    upload_page = UploadPage(page)
    upload_page.goto()
    upload_page.upload_file('/home/l4w45h-linux/Downloads/discord-0.0.98.deb')

def test_pag_table_and_total_price(page):
    pagination_page = PaginationWebTablePage(page)
    pagination_page.goto()
    result = pagination_page.get_all_products_and_total_price()
    print('All products:', result['all_products'])
    rounded_price = round(result['total_price'])
    print('Total price:', rounded_price)

def images_are_equal(img1_path, img2_path):
    img1 = Image.open(img1_path).convert('RGB')
    img2 = Image.open(img2_path).convert('RGB')
    if img1.size != img2.size:
        return False
    diff = ImageChops.difference(img1, img2)
    return not diff.getbbox()

def test_svg_elements_screenshot_comparison(page):
    svg_page = SVGElementsPage(page)
    files_dir = os.path.join(os.path.dirname(__file__), 'files')
    svg_page.goto()
    results = svg_page.compare_svgs_with_golden(files_dir, tolerance_percent=10.0, save_diff=True)
    for screenshot, golden, percent_diff, is_within, diff_path in results:
        if percent_diff is None:
            print(f"Golden image not found: {golden}")
        elif not is_within:
            print(f"Difference {percent_diff:.2f}% exceeds tolerance for {screenshot} vs {golden}")
            if diff_path:
                print(f"Diff image saved at: {diff_path}")
    assert all(is_within for _, _, _, is_within, _ in results), "Some SVG screenshots differ from golden images beyond tolerance!" 