# Create Quiz Test Case
# More areas that could be tested: help question mark buttons, textbox entry font buttons

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
        createquizpage.click_display_description_checkbox()

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

        createquizpage.enter_grade_category(TestData.grade_category)
        createquizpage.enter_grade_to_pass(TestData.grade_to_pass)
        createquizpage.enter_attempts_allowed(TestData.attempts_allowed)
        createquizpage.enter_grading_method(TestData.grading_method)

        # Layout tab
        createquizpage.click_layout_tab()

        createquizpage.enter_new_page(TestData.new_page)
        createquizpage.click_layout_show_more_link()
        createquizpage.enter_navigation_method(TestData.navigation_method)

        # Question behaviour tab
        createquizpage.click_question_behaviour_tab()

        createquizpage.enter_shuffle_answers(TestData.shuffle_answers)
        createquizpage.enter_question_behaviour(TestData.question_behaviour)
        createquizpage.click_question_behaviour_show_more_link()
        createquizpage.enter_attempts_build(TestData.attempts_build)

        # Review options tab
        createquizpage.click_review_options_tab()

        createquizpage.click_open_overall_feedback_checkbox()
        createquizpage.click_open_right_answer_checkbox()
        createquizpage.click_open_general_feedback_checkbox()
        createquizpage.click_open_specific_feedback_checkbox()
        createquizpage.click_open_marks_checkbox()
        createquizpage.click_open_correct_checkbox()
        createquizpage.click_open_attempt_checkbox()

        createquizpage.click_immediately_overall_feedback_checkbox()
        createquizpage.click_immediately_right_answer_checkbox()
        createquizpage.click_immediately_general_feedback_checkbox()
        createquizpage.click_immediately_specific_feedback_checkbox()
        createquizpage.click_immediately_marks_checkbox()
        createquizpage.click_immediately_correct_checkbox()
        createquizpage.click_immediately_attempt_checkbox()

        createquizpage.click_during_right_answer_checkbox()
        createquizpage.click_during_general_feedback_checkbox()
        createquizpage.click_during_specific_feedback_checkbox()
        createquizpage.click_during_marks_checkbox()
        createquizpage.click_during_correct_checkbox()

        createquizpage.click_closed_overall_feedback_checkbox()
        createquizpage.click_closed_right_answer_checkbox()
        createquizpage.click_closed_general_feedback_checkbox()
        createquizpage.click_closed_specific_feedback_checkbox()
        createquizpage.click_closed_marks_checkbox()
        createquizpage.click_closed_correct_checkbox()
        createquizpage.click_closed_attempt_checkbox()

        # Appearance tab
        createquizpage.click_appearance_tab()

        createquizpage.enter_show_user_picture(TestData.show_user_picture)
        createquizpage.enter_decimal_places_grades(TestData.decimal_places_grades)
        createquizpage.enter_decimal_places_marks(TestData.decimal_places_marks)
        createquizpage.click_appearance_show_more()
        createquizpage.enter_show_blocks(TestData.show_blocks)

        # Safe exam browser tab
        createquizpage.click_safe_exam_browser_tab()

        createquizpage.enter_require_seb(TestData.require_seb)
        createquizpage.enter_seb_download(TestData.seb_download)
        createquizpage.enter_seb_exit_link(TestData.seb_exit_link)
        createquizpage.enter_seb_confirm_quit(TestData.seb_confirm_quit)
        createquizpage.enter_seb_quit_password(TestData.seb_quit_password)
        createquizpage.enter_seb_enable_reload(TestData.seb_enable_reload)
        createquizpage.enter_seb_taskbar(TestData.seb_taskbar)
        createquizpage.enter_seb_show_reload(TestData.seb_show_reload)
        createquizpage.enter_seb_show_time(TestData.seb_show_time)
        createquizpage.enter_seb_show_keyboard(TestData.seb_show_keyboard)
        createquizpage.enter_seb_show_wifi(TestData.seb_show_wifi)
        createquizpage.enter_seb_enable_audio(TestData.seb_enable_audio)
        createquizpage.enter_seb_enable_spellcheck(TestData.seb_enable_spellcheck)
        createquizpage.enter_seb_enable_url_filter(TestData.seb_enable_url_filter)
        createquizpage.enter_seb_filter_embedded(TestData.seb_filter_embedded)

        createquizpage.enter_seb_expression_allow(TestData.seb_expression_allow)
        createquizpage.enter_seb_regex_allow(TestData.seb_regex_allow)
        createquizpage.enter_seb_expression_block(TestData.seb_expression_block)
        createquizpage.enter_seb_regex_block(TestData.seb_regex_block)

        # Extra restrictions on attempts tab
        createquizpage.click_extra_restriction_tab()

        createquizpage.enter_restriction_password(TestData.restriction_password)
        createquizpage.click_restriction_show_more()

        createquizpage.click_first_delay_checkbox()
        createquizpage.enter_first_delay_number(TestData.first_delay_number)
        createquizpage.enter_first_delay_unit(TestData.first_delay_unit)

        createquizpage.enter_require_network_address(TestData.require_network_address)
        createquizpage.enter_browser_security(TestData.browser_security)

        # Overall feedback tab
        createquizpage.click_overall_feedback_tab()

        createquizpage.enter_grade_boundary1_feedback(TestData.grade_boundary1_feedback)

        createquizpage.enter_grade_boundary2(TestData.grade_boundary2)
        createquizpage.enter_grade_boundary2_feedback(TestData.grade_boundary2_feedback)

        createquizpage.click_add_more_feedback()

        createquizpage.enter_grade_boundary3(TestData.grade_boundary3)
        createquizpage.enter_grade_boundary3_feedback(TestData.grade_boundary3_feedback)

        createquizpage.enter_grade_boundary4(TestData.grade_boundary4)
        createquizpage.enter_grade_boundary4_feedback(TestData.grade_boundary4_feedback)

        createquizpage.enter_grade_boundary5(TestData.grade_boundary5)
        createquizpage.enter_grade_boundary5_feedback(TestData.grade_boundary5_feedback)

        # Common module settings tab
        createquizpage.click_common_module_tab()

        createquizpage.enter_availability(TestData.availability)
        createquizpage.enter_id_number(TestData.id_number)
        createquizpage.enter_force_language(TestData.force_language)
        createquizpage.enter_group_mode(TestData.group_mode)
        createquizpage.click_add_group_restriction()

        # Restrict access tab
        createquizpage.click_restrict_access_tab()

        createquizpage.enter_student_match(TestData.student_match)

        createquizpage.click_add_restriction()
        createquizpage.click_restrict_activity_completion()
        createquizpage.enter_match_all_any(TestData.match_all_any)
        createquizpage.enter_choose_activity(TestData.choose_activity)
        createquizpage.enter_completion_requirement(TestData.completion_requirement)

        createquizpage.click_add_restriction()
        createquizpage.click_restrict_date()
        createquizpage.enter_restrict_from_until(TestData.restrict_from_until)
        createquizpage.enter_restrict_day(TestData.restrict_day)
        createquizpage.enter_restrict_month(TestData.restrict_month)
        createquizpage.enter_restrict_year(TestData.restrict_year)
        createquizpage.enter_restrict_hour(TestData.restrict_hour)
        createquizpage.enter_restrict_minute(TestData.restrict_minute)

        createquizpage.click_add_restriction()
        createquizpage.click_restrict_grade()
        createquizpage.enter_restrict_grade(TestData.restrict_grade)
        createquizpage.click_restrict_greater_than_checkbox()
        createquizpage.enter_restrict_greater_than(TestData.restrict_greater_than)
        createquizpage.click_restrict_less_than_checkbox()
        createquizpage.enter_restrict_less_than(TestData.restrict_less_than)

        createquizpage.click_add_restriction()
        createquizpage.click_restrict_profile()
        createquizpage.enter_restrict_profile_field(TestData.restrict_profile_field)
        createquizpage.enter_restrict_profile_operator(TestData.restrict_profile_operator)
        createquizpage.enter_restrict_profile_value(TestData.restrict_profile_value)

        # Activity completion tab
        createquizpage.click_activity_completion_tab()
        breakpoint()

    def tearDown(self):

        sleep(2)
        self.driver.close()
        self.driver.quit()
        print('Test completed.')
