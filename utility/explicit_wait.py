from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ExplicitWait():
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_till_text_present(self, timeout=10, poll_frequency=1, locator_value=None, text=None):
        wait = WebDriverWait(self.driver, timeout, poll_frequency,
                             ignored_exceptions=[NoSuchElementException,
                                                 StaleElementReferenceException,
                                                 ElementNotInteractableException])
        wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, locator_value), text))

    def wait_for_element_till_its_presence(self, timeout=7, poll_frequency=0.5, locator_value=None, text=None):
        wait = WebDriverWait(self.driver, timeout, poll_frequency,
                             ignored_exceptions=[NoSuchElementException,
                                                 StaleElementReferenceException,
                                                 ElementNotInteractableException])
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, locator_value)))