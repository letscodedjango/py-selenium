from selenium import webdriver
import time

from time import sleep


def add_contacts_wo_parameter():
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

    new_btn = driver.find_element_by_xpath("//button[@class='ui linkedin button']/i[@class='edit icon']")
    new_btn.click()

    sleep(3)

    first_name = driver.find_element_by_name("first_name")
    first_name.send_keys("Jenny")

    last_name = driver.find_element_by_name("last_name")
    last_name.send_keys("Smith")

    email = driver.find_element_by_xpath("//input[@placeholder='Email address']")
    email.send_keys("jennysmith@gmale.com")

    sleep(3)

    save_btn = driver.find_element_by_xpath("//button[@class='ui linkedin button']/i[@class='save icon']")
    save_btn.click()


def add_contacts_with_parameter(firstname, lastname, email):
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

    new_btn = driver.find_element_by_xpath("//button[@class='ui linkedin button']/i[@class='edit icon']")
    new_btn.click()

    sleep(3)

    first_name = driver.find_element_by_name("first_name")
    first_name.send_keys(firstname)

    last_name = driver.find_element_by_name("last_name")
    last_name.send_keys(lastname)

    email_id = driver.find_element_by_xpath("//input[@placeholder='Email address']")
    email_id.send_keys(email)

    sleep(3)

    save_btn = driver.find_element_by_xpath("//button[@class='ui linkedin button']/i[@class='save icon']")
    save_btn.click()

    sleep(3)

    driver.close()
    driver.quit()


# add_contacts_wo_parameter()
#
# add_contacts_with_parameter('Mak', 'Jackson', 'mackjack@gmal.com')
# add_contacts_with_parameter('Mike', 'Tyson', 'mike@gmal.com')
# add_contacts_with_parameter('Kim', 'Choe', 'kimchoe@gmal.com')


def add_mulitple_contacts(firstname, lastname, email, driver):
    left_panel_contact = driver.find_element_by_xpath("//span[text()='Contacts']")
    left_panel_contact.click()

    sleep(3)

    new_btn = driver.find_element_by_xpath("//button[@class='ui linkedin button']/i[@class='edit icon']")
    new_btn.click()

    sleep(3)

    first_name = driver.find_element_by_name("first_name")
    first_name.send_keys(firstname)

    last_name = driver.find_element_by_name("last_name")
    last_name.send_keys(lastname)

    email_id = driver.find_element_by_xpath("//input[@placeholder='Email address']")
    email_id.send_keys(email)

    sleep(3)

    save_btn = driver.find_element_by_xpath("//button[@class='ui linkedin button']/i[@class='save icon']")
    save_btn.click()

    sleep(3)


def add_contacts_with_one_time_login():
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

    contacts_list = [{'firstname': 'Tom', 'lastname': 'Cruise', 'email': 'tomcruise@hollywood.com'},
                     {'firstname': 'Bruce', 'lastname': 'Wayne', 'email': 'brucewayne@hollywood.com'},
                     {'firstname': 'Sherlocks', 'lastname': 'Homes', 'email': 'tonystark@hollywood.com'}]

    for i in range(0, len(contacts_list)):
        print(contacts_list[i])
        value = list(contacts_list[i].values())

        add_mulitple_contacts(value[0], value[1], value[2], driver)


    # add_mulitple_contacts('Mak', 'Jackson', 'mackjack@gmal.com', driver)
    # add_mulitple_contacts('Mike', 'Tyson', 'mike@gmal.com', driver)
    # add_mulitple_contacts('Kim', 'Choe', 'kimchoe@gmal.com', driver)

    driver.close()
    driver.quit()


add_contacts_with_one_time_login()


def reading_dict_from_list():
    contacts_list = [{'firstname': 'Tom', 'lastname': 'Cruise', 'email': 'tomcruise@hollywood.com'},
                     {'firstname': 'Bruce', 'lastname': 'Wayne', 'email': 'brucewayne@hollywood.com'},
                     {'firstname': 'Sherlocks', 'lastname': 'Homes', 'email': 'tonystark@hollywood.com'}]

    for i in range(0, len(contacts_list)):
        print(contacts_list[i])

        value = contacts_list[i].values()
        print(list(value))


        # for value in contacts_list[i].values():
        #     print(value)

# reading_dict_from_list()
