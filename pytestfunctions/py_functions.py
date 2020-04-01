from selenium import webdriver
import pytest

# A- Arrange (Setup/ Prerequisite)
# A - Action
# A - Assertion/Validation



def test_url_open_chrome():
    driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")
    driver.get("https://www.goindigo.in/")
    driver.implicitly_wait(2)
    driver.maximize_window()
    page_title = driver.title
    assert page_title == 'Indigo'
    # if(page_title == 'Indigo'):
    #     print('Its matching')
    # else:
    #     print('Its not matching')



def test_url_open_firefox():
    driver = webdriver.Firefox()
    driver.get("https://www.goindigo.in/")
    driver.implicitly_wait(2)
    driver.maximize_window()
    page_title = driver.title
    assert page_title == 'Indigo'
    # if (page_title == 'Indigo'):
    #     print('Its matching')
    # else:
    #     print('Its not matching')

#
# url_open_chrome_test()
# url_open_firefox_test()
