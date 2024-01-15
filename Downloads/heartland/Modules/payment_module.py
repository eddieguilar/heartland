"""
Payment Page Module
"""
from Downloads.heartland.pages.payment_page import PaymentPage


class PaymentModule(PaymentPage):
    """
    Payment Page Main Module Class
    """

    def __init__(self, driver):
        super().__init__(driver)

    def click_and_place_order(self):
        self.click_place_order_button()
        return self

