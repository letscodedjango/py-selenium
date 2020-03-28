from selenium import webdriver
from time import sleep

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utility.explicit_wait import ExplicitWait

driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")

driver.get("https://www.goindigo.in/")

driver.implicitly_wait(1);


driver.maximize_window()

explicit_wait = ExplicitWait(driver)

search_flight = driver.find_element_by_xpath("//span[text()='Search Flight']")
search_flight.click()

# wait = WebDriverWait(driver, 10, 1,
#                      ignored_exceptions=[ElementNotVisibleException, NoSuchElementException]
#                      )
# wait.until(expected_conditions.presence_of_element_located(By.XPATH,"//*[text()='Flights on these dates are not available.']" ))

explicit_wait.wait_for_element_till_its_presence(10, 1, locator_value="//*[text()='Flights on these dates are not available.']")


info_text = driver.find_element_by_xpath("//*[text()='Flights on these dates are not available.']")
isTrue = info_text.is_displayed()
print(isTrue)



explicit_Wait = ExplicitWait(driver)
explicit_Wait.wait_for_element(10,locator_value="//div[@aria-labelledby='ui-id-3']/p", text="Sed non urna. Donec et ante")

section_two_para = driver.find_element_by_css_selector("div[aria-labelledby='ui-id-3']>p")
section_two_content = section_two_para.text
print(section_two_content)


# wait = WebDriverWait(driver, 7, 0.5,
#                      ignored_exceptions=[ElementNotVisibleException, NoSuchElementException]
#                      )
# wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH,"//*[text()='Flights on these dates are not available.']"), "Flights on these dates"))
explicit_wait.wait_for_element_till_text_present(7, 0.5, locator_value="//*[text()='Flights on these dates are not available.']",text="Flights on these dates" )