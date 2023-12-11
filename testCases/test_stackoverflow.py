from selenium.webdriver.common.by import By

from utilities.readProperties import ReadConfig
from pageObjects.stackoverflow import StackOverflow
from utilities.customLogger import LogGen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from bs4 import BeautifulSoup


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
        html_source = self.driver.page_source
        result_urls = []

        soup = BeautifulSoup(html_source, 'html.parser')
        outer_div = soup.find('div', class_='flush-left js-search-results')

        if outer_div:
            print("div found!")
            # Find all anchor tags within the outer div
            links = outer_div.find_all('a', href=True)

            # Iterate through each anchor tag and extract URLs
            for link in links[:10]:
                url = link['href']
                r_url = "{}{}".format(self.app_url, url)
                result_urls.append(r_url)

        else:
            print("Results div not found!")

        # Close the browser
        self.driver.quit()

        # Export URLs to an Excel file
        df = pd.DataFrame(result_urls, columns=["URLs"])
        df.to_excel(".\\Reports\\"+"stack_overflow_results.xlsx", index=False)
