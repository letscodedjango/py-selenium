from selenium import webdriver
import pytest


class TestWebsiteHome():

    def test_homepage_title(self):
        driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")
        driver.get("https://www.explorechoice.org")
        print('Successfully launched the chrome browser')

    def test_course_title(self):
        banner = driver.find_element_by_id("banner-conservancy")
        banner_text = banner.text
        print(banner_text)
