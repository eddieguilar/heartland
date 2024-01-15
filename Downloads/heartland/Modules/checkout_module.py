"""
CheckoutPage Module
"""
from Downloads.heartland.pages.checkout_page import CheckoutPage


class CheckoutModule(CheckoutPage):
    """
    Checkout Page Main Module Class
    """

    def __init__(self, driver):
        super().__init__(driver)

    def get_user_info(self, email='test@gmail.com', first_name='test_first_name', last_name='test_last_name', company_name='test',
                      street_address='123 test street', city_name='carson', region='California', postcode='90746',
                      telephone_number='123-123-1234'):
        """gets user information for checkout"""

        self.get_user_email(email)\
            .get_user_first_name(first_name)\
            .get_user_last_name(last_name)\
            .get_company_name(company_name)\
            .get_user_street_address(street_address)\
            .get_user_city_location(city_name)\
            .get_user_region_location(region)\
            .get_user_postal_code(postcode)\
            .get_user_telephone_information(telephone_number)\
            .select_shipping_method()\
            .click_next_button()
        return self
