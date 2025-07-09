from .base_page import BasePage

class UploadPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.file_input = '#singleFileInput'

    def upload_file(self, file_path):
        self.page.wait_for_selector(self.file_input)
        self.page.set_input_files(self.file_input, file_path) 