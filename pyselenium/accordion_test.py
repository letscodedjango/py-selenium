from selenium import webdriver
from time import sleep


driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")

driver.get("https://jqueryui.com/accordion/")

sleep(3)
driver.maximize_window()

driver.switch_to.frame(0);

section_one = driver.find_element_by_css_selector("div[aria-labelledby='ui-id-1']>p")
section_one_content = section_one.text
# print(section_one_content)

#driver.find_element_by_css_selector("h3[id=ui-id-3']")

#  hash(#) represents class in css selector
section_two_head = driver.find_element_by_css_selector("#ui-id-3")
section_two_head.click()

#  dot(.) represents class in css selector
#section_two_head = driver.find_element_by_css_selector("div[class='ui-id-3']")
# section_two_head = driver.find_element_by_css_selector(".ui-id-3")
# section_two_head.click()

section_two_para = driver.find_element_by_css_selector("div[aria-labelledby='ui-id-3']>p")
sleep(5) # my element got loaded within 2 secs still the sleep will apply for 5 secs
section_two_content = section_two_para.text
print(section_two_content)





driver.close()
driver.quit()
