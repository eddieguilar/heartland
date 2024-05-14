import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    """Product page class"""

    def __init__(self, driver):
        self.driver = driver

    _select_a_size = (By.XPATH, "//div[@option-label='XS']")
    _select_a_color = (By.XPATH, "//div[@option-label='Blue']")  # set up f string
    _clear_field = (By.XPATH, "//input[@id='qty']")
    _add_quantity = (By.XPATH, "//input[@id='qty']")
    _add_to_cart_button = (By.XPATH, "//span[normalize-space()='Add to Cart']")
    _shopping_cart_text = (By.XPATH, "//a[text()='shopping cart']")
    _cart_icon = (By.XPATH, "//a[@class='action showcart']")
    _proceed_to_checkout_button = (By.XPATH, "//button[@id='top-cart-btn-checkout']")

    def select_size_option(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self._select_a_size))
        self.driver.find_element(*self._select_a_size).click()
        return self

    def select_a_color(self, color):
        self.driver.find_element(*self._select_a_color).click()
        return self

    def clear_field(self):
        self.driver.find_element(*self._clear_field).clear()
        return self

    def add_quantities(self, qty):
        self.driver.find_element(*self._add_quantity).send_keys(qty)
        return self

    def click_add_to_cart_button(self):
        self.driver.find_element(*self._add_to_cart_button).click()
        # time.sleep(5)
        return self

    def wait_for_shopping_cart_text_to_be_displayed(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self._shopping_cart_text))
        # self.wait_for_element_visible(*self._cart_quantity)
        return self

    def click_cart_icon(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self._cart_icon))
        self.driver.find_element(*self._cart_icon).click()
        return self

    def click_proceed_to_checkout_button(self):
        # WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self._proceed_to_checkout_button))
        self.driver.find_element(*self._proceed_to_checkout_button).click()
        return self

    # def add_items_and_proceed_to_checkout(self, driver):
    #     time.sleep(2)
    #     # driver.find_element(by=By.XPATH, value=("//div[@option-label='XS']")).click()
    #     # driver.find_element(by=By.XPATH, value=("//div[@option-label='Blue']")).click()
    #     # driver.find_element(by=By.XPATH, value=("//input[@id='qty']")).clear()
    #     # driver.find_element(by=By.XPATH, value=("//input[@id='qty']")).send_keys('10')
    # time.sleep(2)
    # driver.find_element(by=By.XPATH, value=("//span[normalize-space()='Add to Cart']")).click()
    # time.sleep(10)
    # driver.find_element(by=By.XPATH, value=("//a[@class='action showcart']")).click()
    # time.sleep(2)
    # driver.find_element(by=By.XPATH, value=("//button[@id='top-cart-btn-checkout']")).click()
