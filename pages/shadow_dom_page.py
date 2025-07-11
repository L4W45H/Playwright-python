from .base_page import BasePage

class ShadowDomPage(BasePage):
    shadow_host = '#shadow_host'
    input_selector = 'input[type="text"]'
    def __init__(self, page):
        super().__init__(page)


    def fill_shadow_input(self, value):
        self.page.wait_for_selector(self.shadow_host)
        self.page.evaluate(
            '''([shadow_host, input_selector, value]) => {
                const shadowRoot = document.querySelector(shadow_host).shadowRoot;
                const input = shadowRoot.querySelector(input_selector);
                input.value = value;
                input.dispatchEvent(new Event('input', { bubbles: true }));
            }''',
            [self.shadow_host, self.input_selector, value]
        )

    def get_shadow_input_value(self):
        self.page.wait_for_selector(self.shadow_host)
        return self.page.evaluate(
            '''([shadow_host, input_selector]) => {
                const shadowRoot = document.querySelector(shadow_host).shadowRoot;
                return shadowRoot.querySelector(input_selector).value;
            }''',
            [self.shadow_host, self.input_selector]
        ) 