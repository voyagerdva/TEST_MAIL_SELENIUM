from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from Pages.PageBase import Base

class Account(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.emailAddress = "mariner-9@yandex.ru"
        self.emailTopic = "Topic - Hello from Selenium"
        self.USER_NAME_LOCATOR = ".email-container .email-input-container .email-input"
        self.BUTTON_COMPOSE_MESSAGE_LOCATOR = ".sidebar__compose-btn-box .compose-button"
        self.EMAIL_ADDRESS_LOCATOR = ".container--ItIg4 > div:nth-child(1) > input:nth-child(1)"
        self.EMAIL_TOPIC_LOCATOR = ".container--3QXHv > div:nth-child(1) > input:nth-child(1)"
        self.BUTTON_SEND_CLICK_LOCATOR = ".button2.button2_base.button2_primary.button2_compact.button2_hover-support.js-shortcut"
        self.BUTTON_SEND_APPLY_CLICK_LOCATOR = "button.base-1-2-63:nth-child(4) > span:nth-child(1)"


    def sendEmail(self):
        self.buttonComposeMessage()
        self.inputEmailAddress()
        self.inputEmailTopic()
        self.buttonSendClick()
        self.buttonSendApplyClick()

    def buttonComposeMessage(self):
        buttonComposeMessage = WebDriverWait(self.getDriver(), 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.BUTTON_COMPOSE_MESSAGE_LOCATOR)))
        buttonComposeMessage.click()

    def inputEmailAddress(self):
        inputEmailAddress = WebDriverWait(self.getDriver(), 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.EMAIL_ADDRESS_LOCATOR)))
        inputEmailAddress.send_keys(self.emailAddress)

    def inputEmailTopic(self):
        inputEmailTopic = self.driver.find_element_by_css_selector(self.EMAIL_TOPIC_LOCATOR)
        inputEmailTopic.send_keys(self.emailTopic)

    def buttonSendClick(self):
        buttonSendClick = self.driver.find_element_by_css_selector(self.BUTTON_SEND_CLICK_LOCATOR)
        buttonSendClick.click()

    def buttonSendApplyClick(self):
        time.sleep(10)
        buttonSendApplyClick = WebDriverWait(self.getDriver(), 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.BUTTON_SEND_APPLY_CLICK_LOCATOR)))
        buttonSendApplyClick.click()