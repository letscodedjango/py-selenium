from selenium import webdriver


class BrowserLaunch():
    def test_chrome_browser(self):
        driver = webdriver.Chrome(executable_path="/Users/gaurnitai/Desktop/PySelenium/drivers/chromedriver")
        driver.get("https://www.explorechoice.org")
        print('Successfully launched the chrome browser')
        driver.quit()

    def test_firefox_browser(self):
        driver = webdriver.Firefox()
        driver.get("https://www.selenium.dev/")
        print("Successfully launched the firefox browser")
        driver.quit()


browser_launch = BrowserLaunch()
browser_launch.test_chrome_browser()
browser_launch.test_firefox_browser()