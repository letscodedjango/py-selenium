from selenium import webdriver
import time

from time import sleep

driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")

driver.get("https://www.amazon.in")

driver.maximize_window()

page_title = driver.title

print(page_title)


search_box = driver.find_element_by_id("twotabsearchtextbox")
search_box.send_keys("Macbook Pro 15 inch")

search_icon = driver.find_element_by_xpath("//input[@type='submit']")
search_icon.click()
sleep(3)

expected_product_list = [
    'Apple MacBook Pro (15-inch, Latest Model, 16GB RAM, 256GB Storage, 2.6GHz Intel Core i7) - Space Grey',
    'New Apple MacBook Pro (13-inch, 8GB RAM, 128GB Storage, 1.4GHz Intel Core i5) - Space Grey']

products_list = driver.find_elements_by_xpath(
    "//div[@class='s-include-content-margin s-border-bottom']//a[@class='a-link-normal a-text-normal']")

