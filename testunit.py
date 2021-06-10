import time
import unittest
from Pages.InterfaceMail import Interface as IF

class testSendEmail(unittest.TestCase):

    def setUp(self):
        self.page = IF()

    def test_sendEmail(self):
        self.page.start()
        self.page.login()
        self.page.send()

        time.sleep(2)
        assert "Письмо отправлено" in self.page.getDriver().page_source

    def tearDown(self):
        self.page.close()

if __name__ == "__main__":
    unittest.main()

    ###