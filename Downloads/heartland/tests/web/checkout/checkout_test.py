import time

from Downloads.heartland.Modules.checkout_module import CheckoutModule
from Downloads.heartland.Modules.homepage_module import HomepageModule
from Downloads.heartland.Modules.payment_module import PaymentModule
from Downloads.heartland.Modules.product_module import ProductModule
from Downloads.heartland.Modules.success_module import SuccessModule
from Downloads.heartland.pages.homepage import HomePage
from Downloads.heartland.pages.success_page import SuccessPage


class TestOne:
    def test_place_order(self, setup):
        """Testing checkout"""

        # self.hp = HomePage(setup)
        # self.product_page = ProductPage()
        # self.checkout_page = CheckoutPage()
        # self.payment = PaymentPage()
        # self.success_page = SuccessPage()

        hp = HomepageModule(setup)
        product_page = ProductModule(setup)
        checkout_page = CheckoutModule(setup)
        payment = PaymentModule(setup)
        success_page = SuccessModule(setup)

        hp.add_item_to_cart()
        product_page.complete_adding_item_to_cart()
        checkout_page.get_user_info()
        payment.click_and_place_order()
        assert success_page.order_confirmation_displayed()
        # result = success_page.is_order_placed_successfully() # figure out how to print text.
        # print(result)

        # original code
        # self.hp.search_jackets_for_women(temp_driver_for_test)
        # self.product_page.add_items_and_proceed_to_checkout(temp_driver_for_test)
        # self.checkout_page.fill_out_customer_information(temp_driver_for_test)
        # self.payment.place_order(temp_driver_for_test)
        # self.success_page.is_order_placed_successfully(temp_driver_for_test)

    def test_verify_order_total_is_displayed(self, setup):
        hp = HomepageModule(setup)
        product_page = ProductModule(setup)
        checkout_page = CheckoutModule(setup)
        payment = PaymentModule(setup)
        expected_amount = ''

        hp.add_item_to_cart()
        product_page.complete_adding_item_to_cart()
        checkout_page.get_user_info()
        order_total = payment.verify_order_amount_is_displayed(expected_amount)
        print(order_total)
        assert payment.verify_order_amount_is_displayed(expected_amount) == "123"

        # assert order_total == '$256.00'

    def test_invalid_discount_code_message_displayed(self, setup):
        hp = HomepageModule(setup)
        product_page = ProductModule(setup)
        checkout_page = CheckoutModule(setup)
        payment = PaymentModule(setup)
        hp.add_item_to_cart()
        product_page.complete_adding_item_to_cart()
        checkout_page.get_user_info()
        payment.click_discount_button()
        payment.input_discount_code()
        payment.click_apply_discount_button()
        assert payment.is_error_displayed()

    def test_input_value_in_search_box(self, setup):
        hp = HomepageModule(setup)
        hp.search_for_item_in_search_field("tanks")
        hp.is_search_results_displayed()
        assert hp.is_search_results_displayed() == "Search results for: 'tanks for women'"

    # def test_select_item_from_category_dropdown(self, setup):
    #     hp = HomepageModule(setup)
    #     options = hp.select_item_from_category_dropdown('Pullover')
    #     assert options == 'Pullover'

    def test_select_item_from_category_dropdown(self, setup):
        hp = HomepageModule(setup)
        options = hp.select_item_from_category_dropdown()
        #assert options == 'Pullover'


