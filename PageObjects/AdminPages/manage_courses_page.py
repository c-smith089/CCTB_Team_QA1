# Manage Courses and Categories Page Object

from selenium.webdriver.common.by import By

# Import locators
from Locators.locators import Locators


class ManageCoursesPage:

    def __init__(self, driver):

        self.driver = driver

    # Manage courses and categories page action methods
    def click_test_course_1(self):

        self.driver.find_element(By.LINK_TEXT, Locators.test_course_1_link).click()

    def click_course_view(self):

        self.driver.find_element(By.XPATH, Locators.course_view_button).click()
