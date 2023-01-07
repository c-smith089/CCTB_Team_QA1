# moodle admin page

# Locators
from Locators.locators import Locators as L

from selenium.webdriver.common.by import By


class AdminPageUser:

    def __init__(self, driver):

        self.driver = driver

    def click_add_a_new_user(self):

        self.driver.find_element(By.LINK_TEXT, L.add_a_new_user).click()
