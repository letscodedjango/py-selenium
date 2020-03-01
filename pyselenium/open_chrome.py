from selenium import webdriver
import time

from time import sleep

driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")

driver.get("https://www.flipkart.com")

driver.maximize_window()

page_title = driver.title

print(page_title)

close_btn = driver.find_element_by_xpath("//html/body/div/div/div/button")
close_btn.click()

search_box = driver.find_element_by_xpath("//html/body/div/div/div/div/div/div/form/div/div/input")
search_box.send_keys("Redmi")


search_icon = driver.find_element_by_xpath("//html/body/div/div/div/div/div/div/form/div/button")
search_icon.click()
sleep(3)
redmi_counts = driver.find_element_by_xpath("(//html/body/div/div/div/div/div/div/div/div/div/span)[1]")
print(redmi_counts)
redmi_count_text = redmi_counts.text
print(str(redmi_count_text))

is_true = str(redmi_count_text).__contains__("1 – 40")
print(is_true)