
from Downloads.heartland.Modules.checkout_module import CheckoutModule
from Downloads.heartland.Modules.homepage_module import HomepageModule
from Downloads.heartland.Modules.payment_module import PaymentModule
from Downloads.heartland.Modules.product_module import ProductModule
from Downloads.heartland.Modules.success_module import SuccessModule
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
