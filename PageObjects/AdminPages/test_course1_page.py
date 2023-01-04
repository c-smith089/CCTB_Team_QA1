# Test Course 1 Page Object

from selenium.webdriver.common.by import By

# Import locators
from Locators.locators import Locators


class TestCourse1Page:

    def __init__(self, driver):

        self.driver = driver

    # Test course 1 page action methods
    def click_edit_mode_toggle(self):

        self.driver.find_element(By.XPATH, Locators.edit_mode_toggle).click()

    def click_body_element(self):

        self.driver.find_element(By.XPATH, Locators.body_element).click()

    def click_add_activity_link(self):

        self.driver.find_element(By.XPATH, Locators.add_activity_link).click()

    def click_add_quiz_button(self):

        self.driver.find_element(By.XPATH, Locators.add_quiz_button).click()
