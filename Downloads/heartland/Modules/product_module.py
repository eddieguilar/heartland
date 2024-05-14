"""
product page Module
"""
from Downloads.heartland.pages.product_page import ProductPage


class ProductModule(ProductPage):

    def __init__(self, driver):
        super().__init__(driver)

    def complete_adding_item_to_cart(self, qty='10', color='Blue'):
        self.select_size_option() \
            .select_a_color(color) \
            .clear_field() \
            .add_quantities(qty) \
            .click_add_to_cart_button() \
            .wait_for_shopping_cart_text_to_be_displayed()\
            .click_cart_icon() \
            .click_proceed_to_checkout_button()
        return self
