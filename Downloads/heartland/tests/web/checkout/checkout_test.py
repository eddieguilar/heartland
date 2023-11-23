
from Downloads.heartland.drivers.driver import Driver
from Downloads.heartland.pages.checkout_page import CheckoutPage
from Downloads.heartland.pages.homepage import HomePage
from Downloads.heartland.pages.payment_page import PaymentPage
from Downloads.heartland.pages.product_page import ProductPage
from Downloads.heartland.pages.success_page import SuccessPage


def test_place_order():
    """Testing checkout"""
    driver_instance = Driver()
    driver = driver_instance.get_webdriver()
    driver.get("https://magento.softwaretestingboard.com/")

    hp = HomePage()
    product_page = ProductPage()
    checkout_page = CheckoutPage()
    payment = PaymentPage()
    success_page = SuccessPage()

    hp.search_jackets_for_women(driver)
    product_page.add_items_and_proceed_to_checkout(driver)
    checkout_page.fill_out_customer_information(driver)
    payment.place_order(driver)
    success_page.is_order_placed_successfully(driver)

    driver.quit()
