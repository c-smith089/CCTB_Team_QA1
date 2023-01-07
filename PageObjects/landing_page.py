# moodle root page

# Locators
from Locators.locators import Locators as L

from selenium.webdriver.common.by import By


class LandingPage:

    def __init__(self, driver):

        self.driver = driver

    def click_login_page_link(self):

        self.driver.find_element(By.LINK_TEXT, L.login_page_link_text).click()
