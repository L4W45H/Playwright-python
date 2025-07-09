from .base_page import BasePage
import os

class SVGElementsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def get_all_svg_elements(self):
        self.page.wait_for_selector('svg')
        return self.page.query_selector_all('svg')

    def screenshot_all_svgs(self, dir_path):
        svgs = self.get_all_svg_elements()
        screenshots = []
        for i, svg in enumerate(svgs):
            file_name = f"svg_element_{i + 1}.png"
            file_path = os.path.join(dir_path, file_name)
            svg.screenshot(path=file_path)
            screenshots.append(file_path)
        return screenshots 