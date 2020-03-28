from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")
driver.get("https://www.google.com")

driver.implicitly_wait(5)
serach_box = driver.find_element_by_name("q")
# serach_box.send_keys("PYTHON")

action = ActionChains(driver)
action.key_down(Keys.SHIFT).send_keys("Python").key_up(Keys.SHIFT).perform()
serach_box.clear()
action.key_down(Keys.SHIFT, serach_box).send_keys("selenium").key_up(Keys.SHIFT, serach_box).perform()
serach_box.clear()
action.key_down("\ue008", serach_box).send_keys("webdriver").key_up("\ue008", serach_box).perform()

#serach_box.send_keys(Keys.ENTER)

#action.send_keys("\ue007").perform()

action.key_down("\ue007").key_up("\ue007").perform()



sleep(6)

driver.close()
driver.quit()