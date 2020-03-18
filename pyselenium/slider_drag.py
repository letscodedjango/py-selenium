from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")

driver.get("https://jqueryui.com/slider/")

sleep(3)
driver.maximize_window()

#driver.find_element_by_tag_name("iframe") # even if I have more than 1 iframe then also it will return only 1 which
# will be the very first iframe

iframe_list = driver.find_elements_by_tag_name("iframe")

print(len(iframe_list))
driver.switch_to.frame(0)
#driver.execute_script("window.scrollBy(x-pixels,y-pixels)");
sleep(3)
slider = driver.find_element_by_xpath("//div[@id='slider']//span")
actionsTwo = ActionChains(driver)
actionsTwo.drag_and_drop_by_offset(slider, 100, 0).perform()

sleep(5)

driver.close()
driver.quit()
