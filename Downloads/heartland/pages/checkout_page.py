import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Checkout page class"""

    def __init__(self, driver):
        self.driver = driver

    _email_field = (By.XPATH, "//div[@class='control _with-tooltip']//input[@type='email']")
    _first_name_field = (By.XPATH, "//input[@class='input-text'][@name='firstname']")
    _last_name_field = (By.XPATH, "//input[@class='input-text'][@name='lastname']")
    _company_name_field = (By.XPATH, "//input[@class='input-text'][@name='company']")
    _street_address_field = (By.XPATH, "//input[@class='input-text'][@name='street[0]']")
    _city_field = (By.XPATH, "//input[@class='input-text'][@name='city']")
    _region_field = (By.XPATH, "//select[@class='select'][@name='region_id']")
    _postcode_field = (By.XPATH, "//input[@class='input-text'][@name='postcode']")
    _telephone_number_field = (By.XPATH, "//input[@class='input-text'][@name='telephone']")
    _shipping_method = (By.XPATH, "//input[@value='tablerate_bestway']")
    _next_button = (By.XPATH, "//button[@data-role='opc-continue']")

    # def fill_out_customer_information(self, driver):
    #     time.sleep(2)
    #     driver.find_element(by=By.XPATH,
    #                         value=("//div[@class='control _with-tooltip']//input[@type='email']")).send_keys(
    #         'test123@gmail.com')
    #     driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='firstname']")).send_keys('Eddie')
    #     driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='lastname']")).send_keys('Aguilar')
    #     driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='company']")).send_keys('Heartland')
    #     driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='street[0]']")).send_keys('123 elm st')
    #     driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='city']")).send_keys('Carson')
    #     driver.find_element(by=By.XPATH, value=("//select[@class='select'][@name='region_id']")).click()
    #     driver.find_element(by=By.XPATH, value=("//option[@data-title='California']")).click()
    #     driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='postcode']")).send_keys('90746')
    #     driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='telephone']")).send_keys('123-123-1234')
    #     driver.find_element(by=By.XPATH, value=("//input[@value='tablerate_bestway']")).click()
    #     driver.find_element(by=By.XPATH, value=("//button[@data-role='opc-continue']")).click()

    def get_user_email(self, email):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self._email_field))
        self.driver.find_element(*self._email_field).send_keys(email)
        time.sleep(10)
        return self

    def get_user_first_name(self, first_name):
        # WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self._first_name_field))
        # self.driver.find_element(self._first_name_field).send_keys(first_name)
        element = self.driver.find_element(*self._first_name_field)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, first_name)
        element.send_keys(Keys.ENTER)
        return self

    def get_user_last_name(self, last_name):
        self.driver.find_element(*self._last_name_field).send_keys(last_name)
        return self

    def get_company_name(self, company_name):
        self.driver.find_element(*self._company_name_field).send_keys(company_name)
        return self

    def get_user_street_address(self, street_address):
        self.driver.find_element(*self._street_address_field).send_keys(street_address)
        return self

    def get_user_city_location(self, city_name):
        self.driver.find_element(*self._city_field).send_keys(city_name)
        return self

    def get_user_region_location(self, region):
        self.driver.find_element(*self._region_field).send_keys(region)
        return self

    def get_user_postal_code(self, postcode):
        self.driver.find_element(*self._postcode_field).send_keys(postcode)
        return self

    def get_user_telephone_information(self, telephone_number):
        self.driver.find_element(*self._telephone_number_field).send_keys(telephone_number)
        return self

    def select_shipping_method(self):
        self.driver.find_element(*self._shipping_method).click()
        return self

    def click_next_button(self):
        self.driver.find_element(*self._next_button).click()
        time.sleep(5)
        return self
