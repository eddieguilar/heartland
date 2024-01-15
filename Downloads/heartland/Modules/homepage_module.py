"""
homepage Module
"""
from Downloads.heartland.pages.homepage import HomePage


class HomepageModule(HomePage):
    """
    Homepage Main Module Class
    """

    def __init__(self, driver):
        super().__init__(driver)

    def add_item_to_cart(self):
        """
        adds jade yoga jacket item to cart
        """
        self.move_to_womens_category()\
            .move_to_womens_tops()\
            .move_to_womens_jackets()\
            .click_womens_jackets_category()\
            .click_jade_yoga_jacket()
        return self

