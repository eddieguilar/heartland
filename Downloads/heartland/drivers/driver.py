from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



class Driver:
    """Driver Class"""

    @staticmethod
    def get_webdriver():
        """
         Create the driver instance
         :return:
         """
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        return driver


