from selenium.webdriver.common.by import By
from src.SignUp.SignUpFixture import SignUpFixture
from src.SignUp.SignUpFormFields import SignUpFormFields


class EmailValidation(SignUpFixture):
    def test_SignUpWithUsedEmail(self):
        self.actions.click_element(By.XPATH, SignUpFormFields.join_as_individual_xpath)

        self.actions.enter_text(By.ID, SignUpFormFields.first_name, "test")
        self.actions.enter_text(By.ID, SignUpFormFields.last_name, "test")
        self.actions.enter_text(By.ID, SignUpFormFields.email, "test@test.com")
        self.actions.enter_text(By.ID, SignUpFormFields.password, "test!234")

        self.actions.click_element(By.XPATH, SignUpFormFields.checkbox_xpath)
        self.actions.click_element(By.XPATH, SignUpFormFields.register_button_xpath)

        paragraph_xpath = "//*[@id='landing-page-bucket']/div/div[2]/div[2]/div/p"
        paragraph_text = self.actions.get_element_text(By.XPATH, paragraph_xpath)
        self.assertEqual(paragraph_text, "The email address test@test.com is already being used.")


