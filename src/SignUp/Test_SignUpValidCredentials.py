from selenium.webdriver.common.by import By
from src.SignUp.SignUpFixture import SignUpFixture
from src.SignUp.SignUpFormFields import SignUpFormFields
import time


class ValidCredentials(SignUpFixture):

    def new_email_address(self):
        utc_time_now = str(round(time.time() * 1000))
        user_email = "testtestte{}@test.com".format(utc_time_now)
        return user_email

    def test_SignUp_positiveScenario(self):
        email_address = self.new_email_address()

        self.actions.click_element(By.XPATH, SignUpFormFields.join_as_individual_xpath)

        self.actions.enter_text(By.ID, SignUpFormFields.first_name, "test")
        self.actions.enter_text(By.ID, SignUpFormFields.last_name, "test")
        self.actions.enter_text(By.ID, SignUpFormFields.email, email_address)
        self.actions.enter_text(By.ID, SignUpFormFields.password, "test!234")

        self.actions.click_element(By.XPATH, SignUpFormFields.checkbox_xpath)
        self.actions.click_element(By.XPATH, SignUpFormFields.register_button_xpath)

        header_xpath = "//*[@id='campaign_landing']/div[1]/h2"
        header_text = self.actions.get_element_text(By.XPATH, header_xpath)

        self.assertEqual(header_text, "Thank You from CoName_6225")

        #call api to remove/delete generated email_address

