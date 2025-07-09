from .base_page import BasePage

class SliderPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.slider = '#slider-range'
        self.amount = '#amount'

    def move_slider(self, min_val, max_val):
        self.page.wait_for_selector(self.slider + ' span')
        slider = self.page.query_selector(self.slider)
        box = slider.bounding_box()
        min_x = box['x'] + box['width'] * min_val
        max_x = box['x'] + box['width'] * max_val
        center_y = box['y'] + box['height'] / 2
        handles = self.page.query_selector_all(self.slider + ' span')

        handles[0].hover()
        self.page.mouse.down()
        self.page.mouse.move(min_x, center_y, steps=10)
        self.page.mouse.up()

        handles[1].hover()
        self.page.mouse.down()
        self.page.mouse.move(max_x, center_y, steps=10)
        self.page.mouse.up()

    def get_slider_value(self):
        self.page.wait_for_selector(self.amount)
        return self.page.eval_on_selector(self.amount, 'el => el.value') 