# Logout Test Case
# *Note: Set login credentials on lines 26, 27 (refer to TestData class in test_data.py)

# Import packages, modules
from time import sleep
import unittest
from selenium import webdriver

# Import locators, test data
from QA1_Project.PageObjects.locators import Locators
from QA1_Project.TestCases.test_data import TestData

# Import pages
from QA1_Project.PageObjects.Pages.home_page import HomePage
from QA1_Project.PageObjects.Pages.login_page import LoginPage
from QA1_Project.PageObjects.Pages.dashboard_page import DashboardPage


class TestLogout(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(Locators.home_page_url)

    def testLogout(self):

        # Login credentials
        username = TestData.testuser1_username
        password = TestData.testuser1_password

        # Click login link
        homepage = HomePage(self.driver)
        homepage.click_login_link()

        # On login page, enter credentials, log in
        loginpage = LoginPage(self.driver)
        loginpage.enter_username(username)
        loginpage.enter_password(password)
        loginpage.click_login()

        # On dashboard page, click user menu, logout
        dashboardpage = DashboardPage(self.driver)
        dashboardpage.click_user_menu_link()
        dashboardpage.click_logout_link()

    def tearDown(self):

        sleep(2)
        self.driver.close()
        self.driver.quit()
        print('Test completed.')
