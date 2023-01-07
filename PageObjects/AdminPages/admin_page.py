# Site Administration Page Object

from selenium.webdriver.common.by import By

# Import locators
from Locators.locators import Locators


class AdminPage:

    def __init__(self, driver):

        self.driver = driver

    # Administration page action methods
    def click_course_admin_link(self):

        self.driver.find_element(By.LINK_TEXT, Locators.course_admin_link).click()

    def click_user_admin_link(self):

        self.driver.find_element(By.LINK_TEXT, Locators.user_admin_link).click()

    # Courses administration tab
    def click_manage_courses_categories_link(self):

        self.driver.find_element(By.LINK_TEXT, Locators.manage_courses_categories_link).click()

    def click_add_category_link(self):

        self.driver.find_element(By.LINK_TEXT, Locators.add_category_link).click()

    def click_add_course_link(self):

        self.driver.find_element(By.LINK_TEXT, Locators.add_course_link).click()

    # Users administration tab
    def click_browse_users_link(self):

        self.driver.find_element(By.LINK_TEXT, Locators.manage_users_link).click()

    def click_add_user_link(self):

        self.driver.find_element(By.LINK_TEXT, Locators.add_user_link).click()

    def click_cohorts_link(self):

        self.driver.find_element(By.LINK_TEXT, Locators.manage_cohorts_link).click()
