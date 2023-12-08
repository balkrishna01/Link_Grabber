from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.keys import Keys


class StackOverflow:
    # Page components identifiers
    btn_login_link = "Log in"
    txtbox_email_id = "email"
    txtbox_password_id = "password"
    btn_login_id = "submit-button"
    searchbox_name = "q"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def clickLoginPage(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.btn_login_link)))
        self.driver.find_element(By.LINK_TEXT, self.btn_login_link).click()

    def setEmail(self, email):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.txtbox_email_id)))
        self.driver.find_element(By.ID, self.txtbox_email_id).click()
        self.driver.find_element(By.ID, self.txtbox_email_id).send_keys(email)

    def setPassword(self, password):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.txtbox_password_id)))
        self.driver.find_element(By.ID, self.txtbox_password_id).click()
        self.driver.find_element(By.ID, self.txtbox_password_id).send_keys(password)

    def clickLogin(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.btn_login_id)))
        self.driver.find_element(By.ID, self.btn_login_id).click()

    def searchQuery(self, question):
        self.wait.until(EC.element_to_be_clickable((By.NAME, self.searchbox_name)))
        self.driver.find_element(By.NAME, self.searchbox_name).click()
        self.driver.find_element(By.NAME, self.searchbox_name).send_keys(question)
        self.driver.find_element(By.NAME, self.searchbox_name).send_keys(Keys.ENTER)
