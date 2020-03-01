from selenium import webdriver
import time

from time import sleep

driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")

driver.get("https://www.flipkart.com")

driver.maximize_window()

page_title = driver.title

print(page_title)

close_btn = driver.find_element_by_xpath("(//button)[2]")
close_btn.click()

search_box = driver.find_element_by_xpath("//div/input[@title='Search for products, brands and more']")
search_box.send_keys("Redmi")


search_icon = driver.find_element_by_xpath("//button[@type='submit']")
search_icon.click()
sleep(3)
redmi_counts = driver.find_element_by_xpath("//span[@class='_2yAnYN']")
print(redmi_counts)
redmi_count_text = redmi_counts.text
print(str(redmi_count_text))

is_true = str(redmi_count_text).__contains__("1 – 40")
print(is_true)