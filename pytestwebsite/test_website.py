from selenium import webdriver
import pytest
import time


class TestWebsiteHome():
    # @pytest.fixture()
    # def take_screenshot(self):
    #     self.driver.save_screenshot("../screenshots/" +str(round(time.time()))+".png")
    #     yield
    #     self.driver.save_screenshot("../screenshots/" + str(round(time.time())) + ".png")

    # def setUp(self, request):
    #     driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")
    #     driver.get("https://www.explorechoice.org")
    #     print('Successfully launched the chrome browser')
    #     request.cls.driver = driver
    #     #request.self.driver = driver
    #     #AttributeError: 'SubRequest' object has no attribute 'self'
    #     yield driver
    #     driver.close()
    #     driver.quit()

    @pytest.fixture()
    def classSetUp(self):
        print('This is class level setup can be used to initialize objects used in this class')

    def test_homepage_title(self, setUp, take_screenshot, classSetUp):
        page_title = self.driver.title
        assert page_title == 'explorechoice.org'

    def test_course_title(self, setUp, take_screenshot, classSetUp):
        banner = self.driver.find_element_by_class_name("lead")
        banner_text = banner.text
        assert banner_text == "let's explore in & out of programming...."

    def test_testimonial_title(self, setUp, take_screenshot, classSetUp):
        banner = self.driver.find_element_by_class_name("lead")
        banner_text = banner.text
        print(banner_text)

## What if we have multiple test case and is it necessary to pass at once - please refer
# test_website_two.py
