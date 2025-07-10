from .base_page import BasePage

class DragAndDropPage(BasePage):
    draggable = '#draggable'
    droppable = '#droppable'
    def __init__(self, page):
        super().__init__(page)


    def drag_and_drop(self):
        self.page.wait_for_selector(self.draggable)
        self.page.wait_for_selector(self.droppable)
        self.page.drag_and_drop(self.draggable, self.droppable) 