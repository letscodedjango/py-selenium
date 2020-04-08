import pytest
from selenium import webdriver
import time


@pytest.fixture(scope='class')
def setUp(request, browser, osType=None):
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    driver.get("https://www.explorechoice.org")
    print('Successfully launched the chrome browser')
    request.cls.driver = driver
    # request.self.driver = driver
    # AttributeError: 'SubRequest' object has no attribute 'self'
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture()
def take_screenshot(request):
    request.cls.driver.save_screenshot("../screenshots/" + str(round(time.time())) + ".png")
    yield
    request.cls.driver.save_screenshot("../screenshots/" + str(round(time.time())) + ".png")


# let define fixture to accept arguments from command line
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Accept the type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
