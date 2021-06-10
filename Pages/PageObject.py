from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

class Page():

    def __init__(self):
        self.username = "test_abonent"
        self.password = "~!@#$%^&"
        self.emailAddress = "mariner-9@yandex.ru"
        self.emailTopic = "Topic - Hello from Selenium"
        self.USER_NAME_LOCATOR = ".email-container .email-input-container .email-input"
        self.PASSWORD_BUTTON_LOCATOR = "#mailbox > form.body.svelte-1eyrl7y > button.button.svelte-1eyrl7y"
        self.PASSWORD_LOCATOR = "#mailbox > form.body.svelte-1eyrl7y > div.password-input-container.svelte-1eyrl7y > input"
        self.PASSWORD_BUTTON_APPLY_LOCATOR = "#mailbox > form.body.svelte-1eyrl7y > button.second-button.svelte-1eyrl7y"
        self.BUTTON_COMPOSE_MESSAGE_LOCATOR = ".sidebar__compose-btn-box .compose-button"
        self.EMAIL_ADDRESS_LOCATOR = ".container--ItIg4 > div:nth-child(1) > input:nth-child(1)"
        self.EMAIL_TOPIC_LOCATOR = ".container--3QXHv > div:nth-child(1) > input:nth-child(1)"
        self.URL_LOCATOR = "https://mail.ru/?from=logout"
        self.BUTTON_SEND_CLICK_LOCATOR = ".button2.button2_base.button2_primary.button2_compact.button2_hover-support.js-shortcut"
        self.BUTTON_SEND_APPLY_CLICK_LOCATOR = "button.base-1-2-63:nth-child(4) > span:nth-child(1)"

    def runBrowser(self):
        self.setDriverFirefox()
        self.getURL()
        self.wait = WebDriverWait(self.driver, 15)


    def login(self):
        self.enterUserName()
        self.enterPassword()

    def sendEmail(self):
        self.buttonComposeMessage()
        self.inputEmailAddress()
        self.inputEmailTopic()
        self.buttonSendClick()
        self.buttonSendApplyClick()


    def setDriverFirefox(self):
        self.driver = webdriver.Firefox()

    def setDriverChrome(self):
        self.driver = webdriver.Chrome()

    def getURL(self):
        self.driver.get(self.URL_LOCATOR)

    def getDriver(self):
        return self.driver

    def enterUserName(self):
        enterUserName = self.driver.find_element_by_css_selector(self.USER_NAME_LOCATOR)
        enterUserName.send_keys(self.username)
        enterUserName.send_keys(Keys.ENTER)

    def enterPassword(self):
        enterPassword = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.PASSWORD_LOCATOR)))
        time.sleep(1)
        enterPassword.send_keys(self.password)
        enterPassword.send_keys(Keys.ENTER)


    def buttonComposeMessage(self):
        buttonComposeMessage = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.BUTTON_COMPOSE_MESSAGE_LOCATOR)))
        buttonComposeMessage.click()

    def inputEmailAddress(self):
        inputEmailAddress = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.EMAIL_ADDRESS_LOCATOR)))
        inputEmailAddress.send_keys(self.emailAddress)

    def inputEmailTopic(self):
        inputEmailTopic = self.driver.find_element_by_css_selector(self.EMAIL_TOPIC_LOCATOR)
        inputEmailTopic.send_keys(self.emailTopic)

    def buttonSendClick(self):
        buttonSendClick = self.driver.find_element_by_css_selector(self.BUTTON_SEND_CLICK_LOCATOR)
        buttonSendClick.click()


    def buttonSendApplyClick(self):
        buttonSendApplyClick = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.BUTTON_SEND_APPLY_CLICK_LOCATOR)))
        buttonSendApplyClick.click()


    def finish(self):
        self.driver.close()

