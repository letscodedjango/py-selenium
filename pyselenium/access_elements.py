from selenium import webdriver
import time

from time import sleep

driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")

driver.get("https://freecrm.co.in/")

sleep(4)

driver.maximize_window()


login_btn = driver.find_element_by_xpath("//ul[@class='rd-navbar-nav']/a")
login_btn.click()



username = driver.find_element_by_name("email")
username.send_keys("sharma.rajeshwar9@gmail.com")


password = driver.find_element_by_name("password")
password.send_keys("letscode")

sleep(3)

login_button = driver.find_element_by_xpath("//div[text()='Login']")
login_button.click()

sleep(3)

left_panel_contact = driver.find_element_by_xpath("//span[text()='Contacts']")
left_panel_contact.click()

sleep(3)

# contact_check_box = driver.find_element_by_xpath("(//input[@name='id'])[2]")
# contact_check_box.click()

contact_trash_icon_list = driver.find_elements_by_xpath("(//i[@class='trash icon'])")


for i in range(1, len(contact_trash_icon_list)):
    # contact_trash_icon = driver.find_element_by_xpath("(//i[@class='trash icon'])["+str(i)+"]")
    contact_trash_icon = driver.find_element_by_xpath("(//i[@class='trash icon'])[1]")
    contact_trash_icon.click()
    sleep(2);
    delete_btn = driver.find_element_by_xpath("(//i[@class='checkmark icon'])[2]")
    delete_btn.click()
    sleep(4);

sleep(3)

driver.close();
driver.quit();