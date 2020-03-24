from time import sleep

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")

driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")

driver.implicitly_wait(5);

driver.maximize_window()

alert = Alert(driver)

click_me = driver.find_element_by_xpath("(//button[text()='Click me!'])[1]")
click_me.click()

sleep(3)

driver.switch_to.alert   # alert() --Java
alert_text = alert.text   # just getText() --Java
print(alert_text)
alert.accept()

sleep(4)

click_me = driver.find_element_by_xpath("(//button[text()='Click me!'])[2]")
click_me.click()

sleep(3)

driver.switch_to.alert   # alert() --Java
alert.dismiss()


sleep(4)

click_me = driver.find_element_by_xpath("(//button[text()='Click for Prompt Box'])")
click_me.click()

sleep(3)

driver.switch_to.alert   # alert() --Java
alert.send_keys("Hello")
alert.accept()


sleep(3)

driver.close()
driver.quit()

