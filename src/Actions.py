from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


class Actions:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator, value):
        wait = WebDriverWait(self.driver, 40)
        wait.until(ec.presence_of_element_located((locator, value)))
        element = self.driver.find_element(locator, value)
        element.click()

    def enter_text(self, locator, value, text):
        wait = WebDriverWait(self.driver, 40)
        wait.until(ec.presence_of_element_located((locator, value)))
        element = self.driver.find_element(locator, value)
        element.send_keys(text)

    def get_element_text(self, locator, value):
        wait = WebDriverWait(self.driver, 40)
        wait.until(ec.presence_of_element_located((locator, value)))
        element = self.driver.find_element(locator, value)

        return element.text

    def wait_for_element(self, locator, value):
        wait = WebDriverWait(self.driver, 40)
        wait.until(ec.presence_of_element_located((locator, value)))

    def wait_for_elements(self, locator, value):
        wait = WebDriverWait(self.driver, 40)
        wait.until(ec.presence_of_element_located((locator, value)))

    def search_keyword(self, locator, value, keyword):
        wait = WebDriverWait(self.driver, 40)
        wait.until(ec.presence_of_element_located((locator, value)))
        element = self.driver.find_element(locator, value)
        element.send_keys(keyword)
        element.send_keys(Keys.RETURN)
