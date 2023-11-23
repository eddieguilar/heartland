import time
from selenium.webdriver.common.by import By


class SuccessPage:
    """Success page class"""

    def is_order_placed_successfully(self, driver):
        time.sleep(2)
        assert driver.find_element(By.XPATH, value=("//span[text()='Thank you for your purchase!']")).is_displayed()
