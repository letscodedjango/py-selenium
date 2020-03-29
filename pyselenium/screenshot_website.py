from selenium import webdriver
from time import sleep

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utility.explicit_wait import ExplicitWait
from utility.take_screenshot import TakeScreenshot

driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")

driver.get("https://www.goindigo.in/")
driver.implicitly_wait(2)
driver.maximize_window()

take_ss = TakeScreenshot(driver)

# screenshot_folder_path = "/Users/gaurnitai/Desktop/PySelenium/screenshots/"

# driver.save_screenshot(screenshot_folder_path + "homepage.png")
take_ss.take_screenshot_with_dynamic_name()

actions = ActionChains(driver)
source = driver.find_element_by_xpath("(//input[@placeholder='From'])[1]")
source.clear()

actions.move_to_element(source).send_keys("Mumbai").send_keys(Keys.ENTER).perform()

# driver.save_screenshot(screenshot_folder_path + "cityenter.png")
take_ss.take_screenshot_with_dynamic_name()

destination = driver.find_element_by_xpath("(//input[@placeholder='To'])[1]")
destination.clear()
actions.move_to_element(destination).send_keys("Pune").send_keys(Keys.ENTER).perform()

#driver.save_screenshot("loading.png")
take_ss.take_screenshot_with_dynamic_name()

# To define folder path

# driver.save_screenshot(screenshot_folder_path + "loading.png")

sleep(5)
driver.close()
driver.quit()

# # To take screenshot
# driver.save_screenshot("loadingone.png") # This will save the screenshot in the same folder where your script is
# # To save at particular folder, we need to specify path
# sleep(3)
# screenshot_folder_path = "../screenshots"
# driver.save_screenshot(screenshot_folder_path + "anotherloading.png")