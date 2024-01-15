"""WebDriver Helper Methods"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 60


class DriverUtil:
    """Driver Util class for webdriver helper methods"""

    def __init__(self, driver):
        self.driver = driver

    # def refresh_page(self):
    #     """Refresh the page
    #         """
    #     self.driver.refresh()
    #     return self
    #
    # def wait_for_element_visible(self, locator, timeout=TIMEOUT):
    #     """
    #     Wait for element to be visible
    #     :param locator: locator type and identifier tuple. Example (By.ID, 'login')
    #     :param timeout: Time to wait for element not to be visible
    #     :return: none
    #     """
    #
    #     WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
