from selenium import webdriver
from time import time
import pytest


@pytest.fixture()
def SetUp():
    driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")
    screenshot_path = "/Users/gaurnitai/Desktop/PySelenium/screenshots/"
    yield
    driver.close()


def test_browser_launch(SetUp):
    # print("setting driver path ")
    # print("launching browser")
    driver.get("https://www.goindigo.in/")
    driver.save_screenshot(SetUp.screenshot_path + str(round(time())) + ".png")
    assert True


# print('driver close')
@pytest.mark.last
def test_homepage_title(SetUp):
    # print("getting homepage title ")
    # print('comparing title')
    title = SetUp.driver.title
    assert title == 'indigo'
