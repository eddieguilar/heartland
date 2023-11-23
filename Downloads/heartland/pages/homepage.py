import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Downloads.heartland.drivers.driver import driver



class HomePage:
    """Homepage class"""

    def search_jackets_for_women(self, driver):
        action = ActionChains(driver)

        time.sleep(2)
        ele = driver.find_element(by=By.XPATH, value="//a[@id='ui-id-4']//span[contains(text(),'Women')]")
        action.move_to_element(ele).perform()
        ele = driver.find_element(by=By.XPATH, value="//a[@id='ui-id-9']//span[contains(text(),'Tops')]")
        action.move_to_element(ele).perform()
        ele = driver.find_element(by=By.XPATH, value="//a[@id='ui-id-11']//span[contains(text(),'Jackets')]")
        action.move_to_element(ele).perform()
        driver.find_element(by=By.XPATH, value="//a[@id='ui-id-11']//span[contains(text(),'Jackets')]").click()
        driver.find_element(by=By.XPATH, value="//a[contains(text(), 'Jade Yoga Jacket')]").click()





        # time.sleep(2)
        # driver.find_element(by=By.XPATH, value=("//a[@id='ui-id-4']//span[contains(text(),'Women')]")).click()
        # driver.find_element(by=By.XPATH, value=("//a[contains(text(),'Jackets')]")).click()
        #


