# Home Page Object

from selenium.webdriver.common.by import By

# Import locators
from Locators.locators import Locators


class HomePage:

    def __init__(self, driver):

        self.driver = driver

    # Home page action methods
    def click_login_link(self):

        self.driver.find_element(By.LINK_TEXT, Locators.login_link).click()
