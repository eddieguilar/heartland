"""
Success Module
"""
from Downloads.heartland.pages.success_page import SuccessPage


class SuccessModule(SuccessPage):

    def __init__(self, driver):
        super().__init__(driver)

    def order_confirmation_displayed(self):
        return self.is_order_placed_successfully()
