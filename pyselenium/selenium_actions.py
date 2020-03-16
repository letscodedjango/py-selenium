from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")

driver.get("https://aiims.edu/en.html")

driver.maximize_window()

sleep(4)

tenders = driver.find_element(By.XPATH, "//a[@title='Tenders']")

actions = ActionChains(driver)


actions.move_to_element(tenders).perform()

sleep(2)

award_letters = driver.find_element(By.ID,"menusys804")
actions.move_to_element(award_letters).click().perform()
#award_letters.click()

sleep(3)

# actions.context_click().perform()
actions.drag_and_drop()





