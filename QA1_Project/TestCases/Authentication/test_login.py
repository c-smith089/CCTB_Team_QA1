# Login Test Case

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


class TestLogin(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(Locators.home_page_url)

    def testLogin(self):

        # Log in credentials
        username = TestData.testuser1_username
        password = TestData.testuser1_password

        # Click login link
        homepage = HomePage(self.driver)
        homepage.click_login_link()

        # Enter credentials, log in
        loginpage = LoginPage(self.driver)
        loginpage.enter_username(username)
        loginpage.enter_password(password)
        loginpage.click_login()

    def tearDown(self):

        sleep(2)
        self.driver.close()
        self.driver.quit()
        print('Test completed.')
