from Pages.PageObject import Page

class Interface():
    def __init__(self):
        self.page = Page()

    def start(self):
        self.page.runBrowser()

    def login(self):
        self.page.login()

    def send(self):
        self.page.sendEmail()

    def close(self):
        self.page.finish()

    def getDriver(self):
        return self.page.getDriver()

