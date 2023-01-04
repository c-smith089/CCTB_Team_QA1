# Create Quiz Test Case

# Import packages, modules
from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Import Locators, test data
from Locators.locators import Locators
from TestData.test_data import TestData

# Import pages
from PageObjects.home_page import HomePage
from PageObjects.login_page import LoginPage
from PageObjects.dashboard_page import DashboardPage
from PageObjects.AdminPages.admin_page import AdminPage
from PageObjects.AdminPages.manage_courses_page import ManageCoursesPage
from PageObjects.AdminPages.test_course1_page import TestCourse1Page
from PageObjects.AdminPages.create_quiz_page import CreateQuizPage


class TestLogin(unittest.TestCase):

    s = Service(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    def setUp(self):

        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(Locators.home_page_url)

    def testLogin(self):

        # Click login link
        homepage = HomePage(self.driver)
        homepage.click_login_link()

        # Enter credentials, log in
        loginpage = LoginPage(self.driver)
        loginpage.enter_username(TestData.adminuser1_username)
        loginpage.enter_password(TestData.adminuser1_password)
        loginpage.click_login()

        # Navigate to admin
        dashboardpage = DashboardPage(self.driver)
        dashboardpage.click_admin_link()

        # Navigate to course admin, manage courses and categories
        adminpage = AdminPage(self.driver)
        adminpage.click_course_admin_link()
        adminpage.click_manage_courses_categories_link()

        # Navigate to test course view
        managecoursespage = ManageCoursesPage(self.driver)
        managecoursespage.click_test_course_1()
        managecoursespage.click_course_view()

        # Enable page edit, navigate to create quiz
        testcourse1page = TestCourse1Page(self.driver)
        testcourse1page.click_edit_mode_toggle()
        testcourse1page.click_add_activity_link()
        testcourse1page.click_add_quiz_button()

        # Enter quiz input, select options

        # General tab
        createquizpage = CreateQuizPage(self.driver)
        createquizpage.enter_quiz_name(TestData.testquiz1_name)
        createquizpage.enter_quiz_description(TestData.testquiz1_description)
        createquizpage.click_display_description_checkbox()  # test font editor buttons too?

        # Timing tab
        createquizpage.click_timing_tab()

        createquizpage.click_open_quiz_checkbox()
        createquizpage.enter_open_quiz_day(TestData.open_quiz_day)
        createquizpage.enter_open_quiz_month(TestData.open_quiz_month)
        createquizpage.enter_open_quiz_year(TestData.open_quiz_year)
        createquizpage.enter_open_quiz_hour(TestData.open_quiz_hour)
        createquizpage.enter_open_quiz_minute(TestData.open_quiz_minute)

        createquizpage.click_close_quiz_checkbox()
        createquizpage.enter_close_quiz_day(TestData.close_quiz_day)
        createquizpage.enter_close_quiz_month(TestData.close_quiz_month)
        createquizpage.enter_close_quiz_year(TestData.close_quiz_year)
        createquizpage.enter_close_quiz_hour(TestData.close_quiz_hour)
        createquizpage.enter_close_quiz_minute(TestData.close_quiz_minute)

        createquizpage.click_time_limit_checkbox()
        createquizpage.enter_time_limit_number(TestData.time_limit_number)
        createquizpage.enter_time_limit_unit(TestData.time_limit_unit)
        createquizpage.enter_when_time_expires(TestData.when_time_expires)

        # Grade tab
        createquizpage.click_grade_tab()
        breakpoint()

    def tearDown(self):

        sleep(2)
        self.driver.close()
        self.driver.quit()
        print('Test completed.')
