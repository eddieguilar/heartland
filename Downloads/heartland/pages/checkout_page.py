import time
from selenium.webdriver.common.by import By


class CheckoutPage:
    """Checkout page class"""
    def fill_out_customer_information(self, driver):
        time.sleep(2)
        driver.find_element(by=By.XPATH, value=("//div[@class='control _with-tooltip']//input[@type='email']")).send_keys('test123@gmail.com')
        driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='firstname']")).send_keys('Eddie')
        driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='lastname']")).send_keys('Aguilar')
        driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='company']")).send_keys('Heartland')
        driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='street[0]']")).send_keys('123 elm st')
        driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='city']")).send_keys('Carson')
        driver.find_element(by=By.XPATH, value=("//select[@class='select'][@name='region_id']")).click()
        driver.find_element(by=By.XPATH, value=("//option[@data-title='California']")).click()
        driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='postcode']")).send_keys('90746')
        driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='telephone']")).send_keys('123-123-1234')
        driver.find_element(by=By.XPATH, value=("//input[@value='tablerate_bestway']")).click()
        driver.find_element(by=By.XPATH, value=("//button[@data-role='opc-continue']")).click()
