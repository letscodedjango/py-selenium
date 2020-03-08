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

left_pane_items_list = driver.find_elements_by_xpath("//div[@id='main-nav']//span")

expected_items_list = ['Home', 'Calendars', 'Contact', 'Companies', 'Deals', 'Tasks', 'Cases', 'Calls', 'Documents', 'Email', 'Campaigns', 'Forms']


for i in range(0, len(left_pane_items_list)):
    print(left_pane_items_list[i].text)
    item_actual_text = left_pane_items_list[i].text
    if(item_actual_text == expected_items_list[i]):
        print(item_actual_text + "is matching with " + expected_items_list[i])
    else:
        print(item_actual_text + "is not matching with " + expected_items_list[i])


driver.close();
driver.quit();