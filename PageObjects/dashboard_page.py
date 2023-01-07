# Dashboard Page Object

from selenium.webdriver.common.by import By

# Import locators
from Locators.locators import Locators


class DashboardPage:

    def __init__(self, driver):

        self.driver = driver

    # Dashboard page action methods
    def click_user_menu_link(self):

        self.driver.find_element(By.CLASS_NAME, Locators.user_menu_link).click()

    def click_logout_link(self):

        self.driver.find_element(By.XPATH, Locators.logout_link).click()

    def click_admin_link(self):

        self.driver.find_element(By.LINK_TEXT, Locators.admin_link).click()
