from selenium.webdriver.common.by import By

from utilities.readProperties import ReadConfig
from pageObjects.stackoverflow import StackOverflow
from utilities.customLogger import LogGen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


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
        time.sleep(5)
        assert self.driver.title == "Stack Overflow - Where Developers Learn, Share, & Build Careers"

        self.so.searchQuery("python automation")
        time.sleep(5)

        # Retrieve the URLs of the top 10 search results
        result_urls = []
        links = self.driver.find_elements(By.TAG_NAME, "a")
        for link in links[:10]:
            href = link.get_attribute("href")
            if href and "stackoverflow.com" in href:
                result_urls.append(href)
        print(result_urls)

        # Close the browser
        self.driver.quit()

        # Export URLs to an Excel file
        df = pd.DataFrame(result_urls, columns=["URLs"])
        df.to_excel(".\\Reports\\"+"stack_overflow_results.xlsx", index=False)
