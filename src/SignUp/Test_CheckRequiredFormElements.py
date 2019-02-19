from selenium.webdriver.common.by import By
from src.SignUp.SignUpFixture import SignUpFixture
from src.SignUp.SignUpFormFields import SignUpFormFields


class CheckRequiredFormElements(SignUpFixture):
    def test_VerifyLoadedElements(self):
        driver = self.driver
        self.actions.click_element(By.XPATH, SignUpFormFields.join_as_individual_xpath)

        header_xpath = "//*[@id='landing-page-bucket']/div/div[2]/div[1]/h3"
        header_text = self.actions.get_element_text(By.XPATH, header_xpath)
        self.assertEqual(header_text, "Sign Up for Work Market", "Header text is incorrect")

        self.assertTrue(driver.find_element_by_id(SignUpFormFields.first_name), "First Name textfield is missing")
        self.assertTrue(driver.find_element_by_id(SignUpFormFields.last_name), "Last Name textfield is missing")
        self.assertTrue(driver.find_element_by_id(SignUpFormFields.email), "Email textfield is missing")
        self.assertTrue(driver.find_element_by_id(SignUpFormFields.password), "Password textfield is missing")

        self.assertTrue(driver.find_element_by_xpath(SignUpFormFields.checkbox_xpath), "Checkbox is missing")
        self.assertTrue(driver.find_element_by_xpath(SignUpFormFields.disabled_register_button_xpath),
                        "REGISTER button is missing")
        disabled_register_button = driver.find_element_by_xpath(SignUpFormFields.disabled_register_button_xpath)
        self.assertFalse(disabled_register_button.is_enabled())


