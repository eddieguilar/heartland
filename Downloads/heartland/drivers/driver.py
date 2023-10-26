from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Driver:
    "Driver Class"

    @staticmethod
    def get_webdriver():
        service_obj = Service("/Users/edwardaguilar/documents/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
        return driver
