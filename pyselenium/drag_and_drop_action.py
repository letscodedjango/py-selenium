from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")

driver.get("https://jqueryui.com/droppable/")

sleep(3)
driver.maximize_window()

#driver.find_element_by_tag_name("iframe") # even if I have more than 1 iframe then also it will return only 1 which
# will be the very first iframe

iframe_list = driver.find_elements_by_tag_name("iframe")

print(len(iframe_list))

driver.switch_to.frame(0)

draggable_element = driver.find_element_by_id("draggable")

droppable_element = driver.find_element_by_id("droppable")

actions = ActionChains(driver)

actions.drag_and_drop(draggable_element, droppable_element).perform()

# actions.drag_and_drop_by_offset(draggable_element, 100, 0).perform();
# actions.drag_and_drop_by_offset(draggable_element, -100, 0).perform();

sleep(5)


# driver.switch_to_default_content()
driver.switch_to.default_content()

slider_link = driver.find_element_by_xpath("//a[text()='Slider']")

driver.execute_script("arguments[0].scrollIntoView();", slider_link)

slider_link.click()


driver.switch_to.frame(0)

driver.execute_script("arguments[0].scrollIntoView();", slider_link)


slider = driver.find_element_by_xpath("//div[@id='slider']//span")


actions.drag_and_drop_by_offset(slider, 100, 0).perform()



sleep(5)
driver.close()
driver.quit()
