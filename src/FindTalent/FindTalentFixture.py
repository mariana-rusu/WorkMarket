from selenium import webdriver
from selenium.webdriver.common.by import By
from src.config.FindTalentSettings import FindTalentSettings
from src.Actions import Actions
import unittest


class FindTalentFixture(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.actions = Actions(self.driver)
        self.driver.maximize_window()
        self.driver.get(FindTalentSettings.url)

        self.actions.enter_text(By.ID, "login-email", FindTalentSettings.email)
        self.actions.enter_text(By.ID, "login-password", FindTalentSettings.password)

        login_button_xpath = "//*[@id='login_page_button']/span"
        self.actions.click_element(By.XPATH, login_button_xpath)

        self.actions.wait_for_element(By.LINK_TEXT, "MANAGE PROFILE")

    def tearDown(self):
        user_xpath = "//header[@id='wm-main-nav']/div/div[2]/div[2]/div/div/div[4]/button"
        self.actions.click_element(By.XPATH, user_xpath)

        sign_out_text_link = "Sign Out"
        self.actions.click_element(By.LINK_TEXT,sign_out_text_link)

        self.driver.quit()
