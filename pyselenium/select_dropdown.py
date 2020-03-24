from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")

driver.get("https://www.facebook.com/")

driver.implicitly_wait(5);

driver.maximize_window()

sleep(4)
# driver.switch_to.frame(0);


select_speed = driver.find_element_by_id("month")

select_class = Select(select_speed)

select_class.select_by_index(0)

sleep(5)

select_class.select_by_value("1")


sleep(5)

select_class.select_by_visible_text("Aug");


sleep(7)

driver.close()
driver.quit()