from selenium import webdriver
import pytest


def test_url_open_chrome():
    driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")
    driver.get("https://www.goindigo.in/")
    driver.implicitly_wait(2)
    driver.maximize_window()


def test_url_open_firefox_test():
    driver = webdriver.Firefox()
    driver.get("https://www.goindigo.in/")
    driver.implicitly_wait(2)
    driver.maximize_window()


# url_open_chrome_test()
# url_open_firefox_test()
