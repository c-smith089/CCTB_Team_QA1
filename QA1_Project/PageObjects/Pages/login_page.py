# Login Page Object

from selenium.webdriver.common.by import By

# Import locators
from QA1_Project.PageObjects.locators import Locators


class LoginPage:

    def __init__(self, driver):

        self.driver = driver

    # Login page action methods
    def enter_username(self, username):

        self.driver.find_element(By.ID, Locators.username_field).clear()
        self.driver.find_element(By.ID, Locators.username_field).click()
        self.driver.find_element(By.ID, Locators.username_field).send_keys(username)

    def enter_password(self, password):

        self.driver.find_element(By.ID, Locators.password_field).clear()
        self.driver.find_element(By.ID, Locators.password_field).click()
        self.driver.find_element(By.ID, Locators.password_field).send_keys(password)

    def click_login(self):

        self.driver.find_element(By.ID, Locators.login_button).click()
