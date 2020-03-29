import random
from time import time


class TakeScreenshot():
    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, filename):
        screenshot_folder_path = "/Users/gaurnitai/Desktop/PySelenium/screenshots/"
        self.driver.save_screenshot(screenshot_folder_path + filename + ".png")

    def take_screenshot_with_random_filename(self,):
        screenshot_folder_path = "/Users/gaurnitai/Desktop/PySelenium/screenshots/"
        filename = round(random.random() * 1000)
        self.driver.save_screenshot(screenshot_folder_path + str(filename) + ".png")

    def take_screenshot_with_dynamic_name(self):
        screenshot_folder_path = "/Users/gaurnitai/Desktop/PySelenium/screenshots/"
        self.driver.save_screenshot(screenshot_folder_path + str(round(time() * 1000)) + ".png")
