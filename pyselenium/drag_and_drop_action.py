from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")

driver.get("https://jqueryui.com/droppable/")

driver.maximize_window()