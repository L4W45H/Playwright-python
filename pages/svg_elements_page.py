from .base_page import BasePage
import os
from PIL import Image, ImageChops, ImageStat

class SVGElementsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def get_all_svg_elements(self):
        self.page.wait_for_selector('svg')
        return self.page.query_selector_all('svg')

    def screenshot_all_svgs(self, dir_path, prefix='screenshot_svg_element_'):
        svgs = self.get_all_svg_elements()
        screenshots = []
        for i, svg in enumerate(svgs):
            file_name = f"{prefix}{i + 1}.png"
            file_path = os.path.join(dir_path, file_name)
            svg.screenshot(path=file_path)
            screenshots.append(file_path)
        return screenshots

    @staticmethod
    def image_difference_percent(img1_path, img2_path, diff_path=None):
        img1 = Image.open(img1_path).convert('RGBA')
        img2 = Image.open(img2_path).convert('RGBA')
        if img1.size != img2.size:
            return 100.0
        diff = ImageChops.difference(img1, img2)
        stat = ImageStat.Stat(diff)
        mean_diff = sum(stat.mean[:3]) / 3
        percent_diff = (mean_diff / 255) * 100
        if diff_path:
            diff.save(diff_path)
        return percent_diff

    def compare_svgs_with_golden(self, dir_path, tolerance_percent=10.0, save_diff=False):
        screenshots = self.screenshot_all_svgs(dir_path)
        results = []
        for i, screenshot_path in enumerate(screenshots):
            golden_path = os.path.join(dir_path, f'golden_svg_element_{i+1}.png')
            diff_path = os.path.join(dir_path, f'diff_svg_element_{i+1}.png') if save_diff else None
            if not os.path.exists(golden_path):
                results.append((screenshot_path, golden_path, None, False, diff_path))
                continue
            percent_diff = self.image_difference_percent(screenshot_path, golden_path, diff_path=diff_path)
            is_within = percent_diff <= tolerance_percent
            results.append((screenshot_path, golden_path, percent_diff, is_within, diff_path))
        return results 