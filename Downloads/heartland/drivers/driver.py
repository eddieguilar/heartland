from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


class Driver:
    """Driver Class"""

    @staticmethod
    def get_webdriver():
        """
         Create the driver instance
         :return:
         """
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        return driver
