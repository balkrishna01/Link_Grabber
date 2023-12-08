from utilities.readProperties import ReadConfig
from pageObjects.stackoverflow import StackOverflow
from utilities.customLogger import LogGen
import time


class Test_stackoverflow:
    app_url = ReadConfig.getURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_grab10url(self, setup):
        self.driver = setup
        self.driver.get(self.app_url)
        self.driver.maximize_window()

        self.so = StackOverflow(self.driver)
        self.so.clickLoginPage()
        self.so.setEmail(self.email)
        self.so.setPassword(self.password)
        assert self.driver.title == "Log In - Stack Overflow"
        self.so.clickLogin()
        time.sleep(10)
        assert self.driver.title == "Stack Overflow - Where Developers Learn, Share, & Build Careers"
