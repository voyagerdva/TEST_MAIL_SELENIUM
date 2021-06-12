from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import seleniumwrapper as selwrap

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
import time

class Base():

    def __init__(self):
        self.driver = self.setDriver()
        self.wait = WebDriverWait(self.driver, 15)

    def setDriver(self):
        self.driver = webdriver.Firefox()
        return self.driver

    def getDriver(self):
        return self.driver

    def finish(self):
        self.driver.close()

#
# bra = Base()
#
