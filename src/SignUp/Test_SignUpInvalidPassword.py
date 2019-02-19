from selenium.webdriver.common.by import By
from src.SignUp.SignUpFixture import SignUpFixture
from src.SignUp.SignUpFormFields import SignUpFormFields


class PasswordValidation(SignUpFixture):

    def test_SignUp_PasswordOnlyLetters(self):
        self.actions.click_element(By.XPATH, SignUpFormFields.join_as_individual_xpath)

        self.actions.enter_text(By.ID, SignUpFormFields.first_name, "test")
        self.actions.enter_text(By.ID, SignUpFormFields.last_name, "test")
        self.actions.enter_text(By.ID, SignUpFormFields.email, "tests@mail.com")
        self.actions.enter_text(By.ID, SignUpFormFields.password, "qwertyui")

        self.actions.click_element(By.XPATH, SignUpFormFields.checkbox_xpath)
        self.actions.click_element(By.XPATH, SignUpFormFields.register_button_xpath)

        paragraph_xpath = "//*[@id='landing-page-bucket']/div/div[2]/div[2]/div/p"
        paragraph_text = self.actions.get_element_text(By.XPATH, paragraph_xpath)
        self.assertEqual(paragraph_text, "Your password entered is not allowed because it is too simple")

    def test_SignUp_PasswordOnlyDigits(self):
        self.actions.click_element(By.XPATH, SignUpFormFields.join_as_individual_xpath)

        self.actions.enter_text(By.ID, SignUpFormFields.first_name, "test")
        self.actions.enter_text(By.ID, SignUpFormFields.last_name, "test")
        self.actions.enter_text(By.ID, SignUpFormFields.email, "tests@mail.com")
        self.actions.enter_text(By.ID, SignUpFormFields.password, "12345678")

        self.actions.click_element(By.XPATH, SignUpFormFields.checkbox_xpath)
        self.actions.click_element(By.XPATH, SignUpFormFields.register_button_xpath)

        paragraph_xpath = "//*[@id='landing-page-bucket']/div/div[2]/div[2]/div/p"
        paragraph_text = self.actions.get_element_text(By.XPATH, paragraph_xpath)
        self.assertEqual(paragraph_text, "Your password entered is not allowed because it is too simple")

