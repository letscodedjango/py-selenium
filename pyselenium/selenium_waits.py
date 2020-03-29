from selenium import webdriver
from time import sleep

from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utility.explicit_wait import ExplicitWait
from utility.take_screenshot import TakeScreenshot

driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")

driver.get("https://jqueryui.com/accordion/")

driver.implicitly_wait(5);

## IMPLICIT wait
## EXPLICIT wait

driver.maximize_window()

take_ss = TakeScreenshot(driver)

# screenshot_folder_path = "/Users/gaurnitai/Desktop/PySelenium/screenshots/"

# driver.save_screenshot(screenshot_folder_path + "homepage.png")

take_ss.take_screenshot_with_random_filename()

driver.switch_to.frame(0);


section_one = driver.find_element_by_css_selector("div[aria-labelledby='ui-id-1']>p")
section_one_content = section_one.text
# print(section_one_content)

# driver.find_element_by_css_selector("h3[id=ui-id-3']")

#  hash(#) represents class in css selector
section_two_head = driver.find_element_by_css_selector("#ui-id-3")
section_two_head.click()

driver.save_screenshot(screenshot_folder_path + "section.png")
#  dot(.) represents class in css selector
# section_two_head = driver.find_element_by_css_selector("div[class='ui-id-3']")
# section_two_head = driver.find_element_by_css_selector(".ui-id-3")
# section_two_head.click()

explicit_Wait = WebDriverWait(driver, 10, 1, (ElementNotVisibleException))

# section_two_para = driver.find_element_by_css_selector("div[aria-labelledby='ui-id-3']>p")

content_text = """
		Sed non urna. Donec et ante. Phasellus eu ligula. Vestibulum sit amet
		purus. Vivamus hendrerit, dolor at aliquet laoreet, mauris turpis porttitor
		velit, faucibus interdum tellus libero ac justo. Vivamus non quam. In
		suscipit faucibus urna.
		"""

# explicit_Wait.until(
#     expected_conditions.text_to_be_present_in_element((By.XPATH, "//div[@aria-labelledby='ui-id-3']/p"),
#                                                       "Sed non urna. Donec et ante"))

# WebDriverWait(driver, 10).until(expected_conditions.invisibility_of_element_locate‌​d((By.XPATH, "//input[@id='message']")))

# sleep(5) # my element got loaded within 2 secs still the sleep will apply for 5 secs
# explicit_Wait.until(section_two_para.is_displayed())

explicit_Wait = ExplicitWait(driver)
explicit_Wait.wait_for_element(10,locator_value="//div[@aria-labelledby='ui-id-3']/p", text="Sed non urna. Donec et ante")

section_two_para = driver.find_element_by_css_selector("div[aria-labelledby='ui-id-3']>p")
section_two_content = section_two_para.text
print(section_two_content)

driver.close()
driver.quit()
