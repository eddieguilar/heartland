import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Downloads.heartland.drivers.driver import Driver


@pytest.fixture(scope='function')
def setup(request):
    """Gets/quits webdriver"""
    web_driver = Driver()
    driver = web_driver.get_webdriver()
    driver.get('https://magento.softwaretestingboard.com/')
    request.cls.driver = driver  # Making the driver available to the test
    yield driver  # This is the "teardown" part
    driver.quit()  # Code after the "yield" will be executed after the test has completed
