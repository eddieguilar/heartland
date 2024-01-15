import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SuccessPage:
    """Success page class"""

    def __init__(self, driver):
        self.driver = driver

    _order_confirmation_text = (By.XPATH, "//span[text()='Thank you for your purchase!'] ")

    def is_order_placed_successfully(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self._order_confirmation_text))
        return self.driver.find_element(By.XPATH, value="//span[text()='Thank you for your purchase!']").is_displayed()
