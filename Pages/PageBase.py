from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class Base():

    def __init__(self, driver):
        if driver == None:
            options = Options()
            options.headless = True
            self.driver = webdriver.Firefox(options=options)
        else:
            self.driver = driver

    def getDriver(self):
        return self.driver

    def finish(self):
        self.driver.close()
