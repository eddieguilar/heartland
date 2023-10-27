from selenium.webdriver.common.by import By


class HomePage:
    """Homepage class"""

    def search_jackets_for_women(self, driver):
        driver.find_element(by=By.XPATH, value=("//a[@id='ui-id-4']//span[contains(text(),'Women')]")).click()
        driver.find_element(by=By.XPATH, value=("//a[contains(text(),'Jackets')]")).click()
        driver.find_element(by=By.XPATH, value=("//a[contains(text(), 'Jade Yoga Jacket')]")).click()
