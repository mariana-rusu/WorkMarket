from selenium.webdriver.common.by import By
from src.config.FindTalentSettings import FindTalentSettings
from src.FindTalent.FindTalentFixture import FindTalentFixture


class SearchQAPeople(FindTalentFixture):
    def test_CheckEveryResultContainSearchCriteria(self):
        self.driver.get(FindTalentSettings.search_url)

        self.actions.search_keyword(By.ID, "input-text", "qa")

        titles_xpath = "//div[@class='profile-card']/div[3]/ul[1]/li[1]/b/em"
        self.actions.wait_for_elements(By.XPATH, titles_xpath)

        titles = self.driver.find_elements_by_xpath(titles_xpath);

        for title in titles:
            self.assertTrue("qa" in title.text.lower())
