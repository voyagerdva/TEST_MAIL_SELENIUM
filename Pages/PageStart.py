from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from Pages.PageBase import Base

class Start(Base):

    def __init__(self):
        super().__init__(None)
        self.username = "test_abonent"
        self.password = "~!@#$%^&"

        self.URL_LOCATOR = "https://mail.ru/?from=logout"

        self.USER_NAME_LOCATOR = ".email-container .email-input-container .email-input"
        self.PASSWORD_BUTTON_LOCATOR = "#mailbox > form.body.svelte-1eyrl7y > button.button.svelte-1eyrl7y"
        self.PASSWORD_LOCATOR = "#mailbox > form.body.svelte-1eyrl7y > div.password-input-container.svelte-1eyrl7y > input"
        self.PASSWORD_BUTTON_APPLY_LOCATOR = "#mailbox > form.body.svelte-1eyrl7y > button.second-button.svelte-1eyrl7y"


    def goURL(self):
        self.getDriver().get(self.URL_LOCATOR)

    def logIn(self):
        self.enterUserName()
        self.enterPassword()

    def enterUserName(self):
        enterUserName = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.USER_NAME_LOCATOR)))
        enterUserName.send_keys(self.username)
        enterUserName.send_keys(Keys.ENTER)

    def enterPassword(self):
        enterPassword = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.PASSWORD_LOCATOR)))
        time.sleep(1)
        enterPassword.send_keys(self.password)
        enterPassword.send_keys(Keys.ENTER)