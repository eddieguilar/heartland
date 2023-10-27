import time
from selenium.webdriver.common.by import By


class PaymentPage:
    """Payment page class"""

    def place_order(self, driver):
        time.sleep(2)
        element = driver.find_element(by=By.XPATH, value=("//button[@class='action primary checkout']//span"))
        driver.execute_script("arguments[0].click()", element)
