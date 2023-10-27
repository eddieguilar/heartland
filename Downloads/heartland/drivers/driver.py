from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


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
