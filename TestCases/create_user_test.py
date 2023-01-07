# Moodle create user test on url: http://54.214.118.90

# libraries
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest

# locators
from Locators.locators import Locators as L
from PageObjects.AdminPages.add_a_new_user import AddANewUser
from PageObjects.AdminPages.admin_page import AdminPage
from PageObjects.AdminPages.admin_page_users import AdminPageUser
from PageObjects.dashboard_page import DashboardPage

# web pages
from PageObjects.landing_page import LandingPage
from PageObjects.login_page import LoginPage


class CreateUserTest(unittest.TestCase):
    s = Service(executable_path='chromedriver')
    driver = webdriver.Chrome(service=s)

    @classmethod
    def setUpClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_create_user(self):
        driver = self.driver
        login(driver,L.landing_page_url,L.login_username,L.login_password)
        sleep(1)
        dashboardPage = DashboardPage(driver)
        dashboardPage.click_admin_link()
        sleep(1)
        adminPage=AdminPage(driver)
        adminPage.click_user_admin_link()
        sleep(1)
        adminPageUser=AdminPageUser(driver)
        adminPageUser.click_add_a_new_user()
        sleep(1)
        addANewUser=AddANewUser(driver)
        addANewUser.enter_username(L.new_username)
        addANewUser.enter_password(L.new_password)
        addANewUser.enter_first_name(L.first_name)
        addANewUser.enter_last_name(L.last_name)
        addANewUser.enter_email_address(L.email_address)
        addANewUser.select_email_display_option(L.email_display_option)
        addANewUser.enter_moodle_net_profile(L.moodle_net_profile)
        addANewUser.enter_city(L.city)





    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

def login(driver,page,user, password):
    driver.get(page)

    landingPage = LandingPage(driver)
    landingPage.click_login_page_link()

    loginPage = LoginPage(driver)
    loginPage.enter_username(user)
    loginPage.enter_password(password)
    loginPage.click_login()