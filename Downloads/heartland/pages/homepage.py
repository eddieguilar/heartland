from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    """Homepage class"""

    def __init__(self, driver):
        self.driver = driver

    _move_to_women_tab = (By.XPATH, "//a[@id='ui-id-4']//span[contains(text(),'Women')]")
    _move_to_women_tops = (By.XPATH, "//a[@id='ui-id-9']//span[contains(text(),'Tops')]")
    _move_to_women_jackets = (By.XPATH, "//a[@id='ui-id-11']//span[contains(text(),'Jackets')]")
    _click_women_jackets = (By.XPATH, "//a[@id='ui-id-11']//span[contains(text(),'Jackets')]")
    _click_yoga_jacket = (By.XPATH, "//a[contains(text(), 'Jade Yoga Jacket')]")

    def move_to_womens_category(self):
        """hovers to women's category"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self._move_to_women_tab))
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*self._move_to_women_tab)).perform()
        return self

    def move_to_womens_tops(self):
        """hovers to women's tops"""
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*self._move_to_women_tops)).perform()
        return self

    def move_to_womens_jackets(self):
        """hovers to women's jackets"""
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*self._move_to_women_jackets)).perform()
        return self

    def click_womens_jackets_category(self):
        """click on women's jacket category"""
        self.driver.find_element(*self._click_women_jackets).click()
        return self

    def click_jade_yoga_jacket(self):
        """click on jade yoga jacket"""
        self.driver.find_element(*self._click_yoga_jacket).click()
        return self


    #original code
    # def move_to_womens_tops(self, driver):
    #     action = ActionChains(driver)
    #
    #     time.sleep(5)
    #
    #     ele = driver.find_element(by=By.XPATH, value="//a[@id='ui-id-4']//span[contains(text(),'Women')]")
    #     action.move_to_element(ele).perform()
    #     ele = driver.find_element(by=By.XPATH, value="//a[@id='ui-id-9']//span[contains(text(),'Tops')]")
    #     action.move_to_element(ele).perform()
    #     ele = driver.find_element(by=By.XPATH, value="//a[@id='ui-id-11']//span[contains(text(),'Jackets')]")
    #     action.move_to_element(ele).perform()
    #     driver.find_element(by=By.XPATH, value="//a[@id='ui-id-11']//span[contains(text(),'Jackets')]").click()

    #     driver.find_element(by=By.XPATH, value="//a[contains(text(), 'Jade Yoga Jacket')]").click()
    #     return self
