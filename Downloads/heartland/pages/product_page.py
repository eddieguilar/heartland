import time
from selenium.webdriver.common.by import By


class ProductPage:
    """Product page class"""
    def add_items_and_proceed_to_checkout(self, driver):
        time.sleep(2)
        driver.find_element(by=By.XPATH, value=("//div[@option-label='XS']")).click()
        driver.find_element(by=By.XPATH, value=("//div[@option-label='Blue']")).click()
        driver.find_element(by=By.XPATH, value=("//input[@id='qty']")).clear()
        driver.find_element(by=By.XPATH, value=("//input[@id='qty']")).send_keys('10')
        time.sleep(2)
        driver.find_element(by=By.XPATH, value=("//span[normalize-space()='Add to Cart']")).click()
        time.sleep(2)
        driver.find_element(by=By.XPATH, value=("//a[@class='action showcart']")).click()
        driver.find_element(by=By.XPATH, value=("//button[@id='top-cart-btn-checkout']")).click()
