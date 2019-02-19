from selenium import webdriver
from src.Actions import Actions
from src.config.SignUpSettings import SignUpSettings
import unittest


class SignUpFixture(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.actions = Actions(self.driver)
        self.driver.maximize_window()
        self.driver.get(SignUpSettings.url)

    def tearDown(self):
        # close the browser window
        self.driver.quit()