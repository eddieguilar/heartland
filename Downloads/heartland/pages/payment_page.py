import time
from selenium.webdriver.common.by import By


class PaymentPage:
    """Payment page class"""

    def __init__(self, driver):
        self.driver = driver

    _place_order_button = (By.XPATH, "//button[@class='action primary checkout']//span")

    # def place_order(self, driver):
    #     time.sleep(2)
    #     element = driver.find_element(by=By.XPATH, value=("//button[@class='action primary checkout']//span"))
    #     driver.execute_script("arguments[0].click()", element)

    def click_place_order_button(self):
        self.driver.find_element(*self._place_order_button).click()
        return self
