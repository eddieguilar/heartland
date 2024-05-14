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
        self.move_to_womens_category() \
            .move_to_womens_tops() \
            .move_to_womens_jackets() \
            .click_womens_jackets_category() \
            .click_jade_yoga_jacket()
        return self

    def search_for_item_in_search_field(self, text_input):
        """inputs text in search field """

        self.go_to_search_box_field(text_input) \
            .select_dropdown_option_from_search_box()
        return self

    def is_search_results_displayed(self):
        return self.search_results_text()

    def select_item_from_category_dropdown(self):
        self.move_to_womens_category()\
            .move_to_womens_tops()\
            .move_to_womens_jackets()\
            .click_womens_jackets_category()\
            .select_filter_options()
        return self

