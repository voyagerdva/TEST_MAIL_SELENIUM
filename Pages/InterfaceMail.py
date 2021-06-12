from Pages.PageBase import Base
from Pages.PageStart import Start
from Pages.PageAccount import Account


class Interface():
    def __init__(self):
        self.base = Base(None)
        self.start = Start()
        self.account = Account()



    def begin(self):
        self.account.checkURL(self.URL_LOCATOR)

    def logInAccount(self):
        self.account.logIn()

    # def login(self):
    #     self.logIn()

    def send(self):
        self.account.sendEmail()

    def close(self):
        self.account.finish()

    def getDriver(self):
        return self.account.getDriver()


interface = Interface()
interface.begin()
interface.logInAccount()
interface.send()
interface.close()