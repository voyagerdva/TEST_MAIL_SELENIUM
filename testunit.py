import unittest
from Pages.PageStart import Start
from Pages.PageAccount import Account

class testSendEmail(unittest.TestCase):

    def test_sendEmail(self):
        startPage = Start()
        startPage.goURL()
        startPage.logIn()

        accountPage = Account(startPage.getDriver())
        accountPage.sendEmail()
        accountPage.finish()

if __name__ == "__main__":
    unittest.main()