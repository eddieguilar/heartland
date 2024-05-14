import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaymentPage:
    """Payment page class"""

    def __init__(self, driver):
        self.driver = driver

    _place_order_button = (By.XPATH, "//button[@class='action primary checkout']//span")
    # _order_amount = (By.XPATH, "//td[@data-th='Order Total']//strong//span[contains(text(),'$256.00')]")
    _order_amount = "//td[@data-th='Order Total']//strong//span[contains(text(),'{}')]"
    _discount_button = (By.ID, "block-discount-heading")
    _discount_code_input_field_box = (By.ID, "discount-code")
    _apply_discount_button = (By.XPATH, "//button[@class='action action-apply']")
    _error_message = (By.XPATH, "//div[@class='message message-error error']")

    # def place_order(self, driver):
    #     time.sleep(2)
    #     element = driver.find_element(by=By.XPATH, value=("//button[@class='action primary checkout']//span"))
    #     driver.execute_script("arguments[0].click()", element)

    def click_place_order_button(self):
        self.driver.find_element(*self._place_order_button).click()
        return self

    # def get_order_total_amount(self):
    #     return self.driver.find_element(*self._order_amount).text

    def get_order_total_amount(self, amount):
        return self.driver.find_element(By.XPATH, self._order_amount.format(amount)).text

    def is_order_total_displayed(self, amount):
        try:
            return self.driver.find_element(By.XPATH, self._order_amount.format(amount)).is_displayed()
        except NoSuchElementException:
            return False

    def click_discount_button(self):
        self.driver.find_element(*self._discount_button).click()
        return self

    def input_discount_code(self):
        self.driver.find_element(*self._discount_code_input_field_box).send_keys("12345")
        return self

    def click_apply_discount_button(self):
        self.driver.find_element(*self._apply_discount_button).click()
        return self

    def is_error_displayed(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self._error_message))
            return self.driver.find_element(*self._error_message).is_displayed()
        except NoSuchElementException:
            print("No such element exception occurs")
        except TimeoutException:
            print("Timeout exception occurs")
            return False


