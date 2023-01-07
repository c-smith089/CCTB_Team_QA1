# Logout Test Case

# Import packages, modules
from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Import locators, test data
from Locators.locators import Locators
from TestData.test_data import TestData

# Import pages
from PageObjects.home_page import HomePage
from PageObjects.login_page import LoginPage
from PageObjects.dashboard_page import DashboardPage


class TestLogout(unittest.TestCase):

    s = Service(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    def setUp(self):

        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(Locators.home_page_url)

    def testLogout(self):

        # Click login link
        homepage = HomePage(self.driver)
        homepage.click_login_link()

        # On login page, enter credentials, log in
        loginpage = LoginPage(self.driver)
        loginpage.enter_username(TestData.testuser1_username)
        loginpage.enter_password(TestData.testuser1_password)
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
