from .base_page import BasePage

class ScrollingDropdownPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.dropdown = '#country'

    def open_dropdown(self):
        self.page.wait_for_selector(self.dropdown)
        self.page.click(self.dropdown)

    def select_option_by_index(self, index):
        self.page.wait_for_selector(self.dropdown)
        options = self.page.query_selector_all(self.dropdown + ' option')
        if index < 0 or index >= len(options):
            raise IndexError('Index out of range')
        value = options[index].get_attribute('value')
        self.page.select_option(self.dropdown, value) 