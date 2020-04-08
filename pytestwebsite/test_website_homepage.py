from time import sleep
import pytest
from selenium import webdriver


@pytest.mark.usefixtures("oneTimeSetUp")
class TestMyWebsite:

    @pytest.fixture()
    def setUp(self):
        self.driver.save_screenshot("../screenshots/homepage.png")

    def test_website_launch(self, setUp):
        is_displayed = self.driver.find_element_by_xpath("//img[@alt='logo']").is_displayed()
        assert True==is_displayed

    def test_homepage_title(self, setUp):
        print('Getting homepage title')
        page_title = self.driver.title
        print('Comparing title')
        assert page_title=='explorechoice.org'

    def test_homepage_links(self, setUp):
        print('Getting all links')
        links = self.driver.find_elements_by_tag_name('a')
        print('Validating links from homepage')
        assert 0 < len(links)
