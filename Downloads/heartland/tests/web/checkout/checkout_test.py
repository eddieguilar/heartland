import time
from selenium.webdriver.common.by import By
from drivers.driver import Driver


def test_checkout():
    """Testing checkout"""
    driver_instance = Driver()
    driver = driver_instance.get_webdriver()
    driver.get("https://magento.softwaretestingboard.com/")

    driver.implicitly_wait(2)
    driver.find_element(by=By.XPATH, value=("//a[@id='ui-id-4']//span[contains(text(),'Women')]")).click()
    driver.find_element(by=By.XPATH, value=("//a[contains(text(),'Jackets')]")).click()
    driver.find_element(by=By.XPATH, value=("//a[contains(text(), 'Jade Yoga Jacket')]")).click()
    driver.find_element(by=By.XPATH, value=("//div[@option-label='XS']")).click()
    driver.find_element(by=By.XPATH, value=("//div[@option-label='Blue']")).click()
    driver.find_element(by=By.XPATH, value=("//input[@id='qty']")).clear()
    driver.find_element(by=By.XPATH, value=("//input[@id='qty']")).send_keys('10')
    time.sleep(5)
    driver.find_element(by=By.XPATH, value=("//span[normalize-space()='Add to Cart']")).click()
    time.sleep(5)
    driver.find_element(by=By.XPATH, value=("//a[normalize-space()='shopping cart']")).click()
    driver.find_element(by=By.XPATH, value=("//span[normalize-space()='Proceed to Checkout']")).click()

    driver.find_element(by=By.XPATH, value=("//div[@class='control _with-tooltip']//input[@type='email']")).send_keys('test123@gmail.com')
    driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='firstname']")).send_keys('Eddie')
    driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='lastname']")).send_keys('Aguilar')
    driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='company']")).send_keys('Heartland')
    driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='street[0]']")).send_keys('123 elm st')
    driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='city']")).send_keys('Carson')
    driver.find_element(by=By.XPATH, value=("//select[@class='select'][@name='region_id']")).click()
    driver.find_element(by=By.XPATH, value=("//option[@data-title='California']")).click()
    driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='postcode']")).send_keys('90746')
    driver.find_element(by=By.XPATH, value=("//input[@class='input-text'][@name='telephone']")).send_keys('123-123-1234')
    driver.find_element(by=By.XPATH, value=("//input[@value='tablerate_bestway']")).click()
    driver.find_element(by=By.XPATH, value=("//button[@data-role='opc-continue']")).click()
    time.sleep(5)
    element = driver.find_element(by=By.XPATH, value=("//button[@class='action primary checkout']//span"))
    driver.execute_script("arguments[0].click()", element)
    time.sleep(5)
    assert driver.find_element(By.XPATH, value=("//span[text()='Thank you for your purchase!']"))
