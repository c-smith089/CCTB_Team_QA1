# Create Quiz Page Object

from selenium.webdriver.common.by import By

# Import locators
from Locators.locators import Locators


class CreateQuizPage:

    def __init__(self, driver):

        self.driver = driver

    # Create quiz page action methods

    # General tab
    def enter_quiz_name(self, quiz_name):

        self.driver.find_element(By.ID, Locators.quiz_name_field).clear()
        self.driver.find_element(By.ID, Locators.quiz_name_field).click()
        self.driver.find_element(By.ID, Locators.quiz_name_field).send_keys(quiz_name)

    def enter_quiz_description(self, quiz_description):

        self.driver.find_element(By.ID, Locators.quiz_description_textbox).clear()
        self.driver.find_element(By.ID, Locators.quiz_description_textbox).click()
        self.driver.find_element(By.ID, Locators.quiz_description_textbox).send_keys(quiz_description)

    def click_display_description_checkbox(self):

        self.driver.find_element(By.ID, Locators.display_description_checkbox).click()

    # Timing tab
    def click_timing_tab(self):

        self.driver.find_element(By.XPATH, Locators.timing_tab).click()

    def click_open_quiz_checkbox(self):

        self.driver.find_element(By.ID, Locators.open_quiz_checkbox).click()

    def enter_open_quiz_day(self, open_quiz_day):

        self.driver.find_element(By.ID, Locators.open_quiz_day_menu).click()
        self.driver.find_element(By.ID, Locators.open_quiz_day_menu).send_keys(open_quiz_day)

    def enter_open_quiz_month(self, open_quiz_month):

        self.driver.find_element(By.ID, Locators.open_quiz_month_menu).click()
        self.driver.find_element(By.ID, Locators.open_quiz_month_menu).send_keys(open_quiz_month)

    def enter_open_quiz_year(self, open_quiz_year):

        self.driver.find_element(By.ID, Locators.open_quiz_year_menu).click()
        self.driver.find_element(By.ID, Locators.open_quiz_year_menu).send_keys(open_quiz_year)

    def enter_open_quiz_hour(self, open_quiz_hour):

        self.driver.find_element(By.ID, Locators.open_quiz_hour_menu).click()
        self.driver.find_element(By.ID, Locators.open_quiz_hour_menu).send_keys(open_quiz_hour)

    def enter_open_quiz_minute(self, open_quiz_minute):

        self.driver.find_element(By.ID, Locators.open_quiz_minute_menu).click()
        self.driver.find_element(By.ID, Locators.open_quiz_minute_menu).send_keys(open_quiz_minute)

    def click_close_quiz_checkbox(self):

        self.driver.find_element(By.ID, Locators.close_quiz_checkbox).click()

    def enter_close_quiz_day(self, close_quiz_day):

        self.driver.find_element(By.ID, Locators.close_quiz_day_menu).click()
        self.driver.find_element(By.ID, Locators.close_quiz_day_menu).send_keys(close_quiz_day)

    def enter_close_quiz_month(self, close_quiz_month):

        self.driver.find_element(By.ID, Locators.close_quiz_month_menu).click()
        self.driver.find_element(By.ID, Locators.close_quiz_month_menu).send_keys(close_quiz_month)

    def enter_close_quiz_year(self, close_quiz_year):

        self.driver.find_element(By.ID, Locators.close_quiz_year_menu).click()
        self.driver.find_element(By.ID, Locators.close_quiz_year_menu).send_keys(close_quiz_year)

    def enter_close_quiz_hour(self, open_quiz_hour):

        self.driver.find_element(By.ID, Locators.open_quiz_hour_menu).click()
        self.driver.find_element(By.ID, Locators.open_quiz_hour_menu).send_keys(
            open_quiz_hour)

    def enter_close_quiz_minute(self, open_quiz_minute):

        self.driver.find_element(By.ID, Locators.open_quiz_minute_menu).click()
        self.driver.find_element(By.ID, Locators.open_quiz_minute_menu).send_keys(open_quiz_minute)

    def click_time_limit_checkbox(self):

        self.driver.find_element(By.ID, Locators.time_limit_checkbox).click()

    def enter_time_limit_number(self, time_limit_number):

        self.driver.find_element(By.ID, Locators.time_limit_number_field).clear()
        self.driver.find_element(By.ID, Locators.time_limit_number_field).click()
        self.driver.find_element(By.ID, Locators.time_limit_number_field).send_keys(time_limit_number)

    def enter_time_limit_unit(self, time_limit_unit):

        self.driver.find_element(By.ID, Locators.time_limit_unit_menu).click()
        self.driver.find_element(By.ID, Locators.time_limit_unit_menu).send_keys(time_limit_unit)

    def enter_when_time_expires(self, when_time_expires):

        self.driver.find_element(By.ID, Locators.when_time_expires_menu).click()
        self.driver.find_element(By.ID, Locators.when_time_expires_menu).send_keys(when_time_expires)

    # Grade tab
    def click_grade_tab(self):

        self.driver.find_element(By.XPATH, Locators.grade_tab).click()

    def enter_grade_category(self, grade_category):

        self.driver.find_element(By.ID, Locators.grade_category_menu).click()
        self.driver.find_element(By.ID, Locators.grade_category_menu).send_keys(grade_category)

    def enter_grade_to_pass(self, grade_to_pass):

        self.driver.find_element(By.ID, Locators.grade_pass_field).clear()
        self.driver.find_element(By.ID, Locators.grade_pass_field).click()
        self.driver.find_element(By.ID, Locators.grade_pass_field).send_keys(grade_to_pass)

    def enter_attempts_allowed(self, attempts_allowed):

        self.driver.find_element(By.ID, Locators.attempts_menu).click()
        self.driver.find_element(By.ID, Locators.attempts_menu).send_keys(attempts_allowed)

    def enter_grading_method(self, grading_method):

        self.driver.find_element(By.ID, Locators.grading_method_menu).click()
        self.driver.find_element(By.ID, Locators.grading_method_menu).send_keys(grading_method)

    # Layout tab
    def click_layout_tab(self):

        self.driver.find_element(By.XPATH, Locators.layout_tab).click()

    def enter_new_page(self, new_page):

        self.driver.find_element(By.ID, Locators.new_page_menu).click()
        self.driver.find_element(By.ID, Locators.new_page_menu).send_keys(new_page)

    def click_layout_show_more_link(self):

        self.driver.find_element(By.XPATH, Locators.layout_show_more_link).click()

    def enter_navigation_method(self, navigation_method):

        self.driver.find_element(By.ID, Locators.nav_method_menu).click()
        self.driver.find_element(By.ID, Locators.nav_method_menu).send_keys(navigation_method)

    # Question behaviour tab
    def click_question_behaviour_tab(self):

        self.driver.find_element(By.XPATH, Locators.question_behaviour_tab).click()

    def enter_shuffle_answers(self, shuffle_answers):

        self.driver.find_element(By.ID, Locators.shuffle_answers_menu).click()
        self.driver.find_element(By.ID, Locators.shuffle_answers_menu).send_keys(shuffle_answers)

    def enter_question_behaviour(self, question_behaviour):

        self.driver.find_element(By.ID, Locators.question_behaviour_menu).click()
        self.driver.find_element(By.ID, Locators.question_behaviour_menu).send_keys(question_behaviour)

    def click_question_behaviour_show_more_link(self):

        self.driver.find_element(By.XPATH, Locators.question_behaviour_show_more_link).click()

    def enter_attempts_build(self, attempts_build):

        self.driver.find_element(By.ID, Locators.attempts_build_menu).click()
        self.driver.find_element(By.ID, Locators.attempts_build_menu).send_keys(attempts_build)

    # Review options tab
    def click_review_options_tab(self):

        self.driver.find_element(By.XPATH, Locators.review_options_tab)

    def click_open_attempt_checkbox(self):

        self.driver.find_element(By.ID, Locators.open_attempt_checkbox).click()

    def click_open_correct_checkbox(self):

        self.driver.find_element(By.ID, Locators.open_correct_checkbox).click()

    def click_open_marks_checkbox(self):

        self.driver.find_element(By.ID, Locators.open_marks_checkbox).click()

    def click_open_specific_feedback_checkbox(self):

        self.driver.find_element(By.ID, Locators.open_specific_feedback_checkbox).click()

    def click_open_general_feedback_checkbox(self):

        self.driver.find_element(By.ID, Locators.open_general_feedback_checkbox).click()

    def click_open_right_answer_checkbox(self):

        self.driver.find_element(By.ID, Locators.open_right_answer_checkbox).click()

    def click_open_overall_feedback_checkbox(self):
        self.driver.find_element(By.ID, Locators.open_overall_feedback_checkbox).click()

    def click_immediately_attempt_checkbox(self):

        self.driver.find_element(By.ID, Locators.immediately_attempt_checkbox).click()

    def click_immediately_correct_checkbox(self):

        self.driver.find_element(By.ID, Locators.immediately_correct_checkbox).click()

    def click_immediately_marks_checkbox(self):

        self.driver.find_element(By.ID, Locators.immediately_marks_checkbox).click()

    def click_immediately_specific_feedback_checkbox(self):

        self.driver.find_element(By.ID, Locators.immediately_specific_feedback_checkbox).click()

    def click_immediately_general_feedback_checkbox(self):

        self.driver.find_element(By.ID, Locators.immediately_general_feedback_checkbox).click()

    def click_immediately_right_answer_checkbox(self):

        self.driver.find_element(By.ID, Locators.immediately_right_answer_checkbox).click()

    def click_immediately_overall_feedback_checkbox(self):
        self.driver.find_element(By.ID, Locators.immediately_overall_feedback_checkbox).click()

    # Appearance tab
    def click_appearance_tab(self):

        self.driver.find_element(By.XPATH, Locators.appearance_tab)

    def enter_show_user_picture(self, show_user_picture):

        self.driver.find_element(By.ID, Locators.show_picture_menu).click()
        self.driver.find_element(By.ID, Locators.show_picture_menu).send_keys(show_user_picture)

    def enter_decimal_places_grades(self, decimal_places_grades):

        self.driver.find_element(By.ID, Locators.decimal_places_grades_menu).click()
        self.driver.find_element(By.ID, Locators.decimal_places_grades_menu).send_keys(decimal_places_grades)

    def enter_decimal_places_marks(self, decimal_places_marks):

        self.driver.find_element(By.ID, Locators.decimal_places_marks_menu).click()
        self.driver.find_element(By.ID, Locators.decimal_places_marks_menu).send_keys(decimal_places_marks)

    def click_appearance_show_more_link(self):

        self.driver.find_element(By.XPATH, Locators.appearance_show_more_link).click()

    def enter_show_blocks(self, show_blocks):

        self.driver.find_element(By.ID, Locators.show_blocks_menu).click()
        self.driver.find_element(By.ID, Locators.show_blocks_menu).send_keys(show_blocks)

    # Safe Exam Browser tab
    def click_safe_exam_browser_tab(self):

        self.driver.find_element(By.XPATH, Locators.safe_exam_browser_tab).click()

    def enter_require_seb(self, require_seb):

        self.driver.find_element(By.ID, Locators.require_seb_menu).click()
        self.driver.find_element(By.ID, Locators.require_seb_menu).send_keys(require_seb)

    def enter_seb_download(self, seb_download):

        self.driver.find_element(By.ID, Locators.seb_download_menu).click()
        self.driver.find_element(By.ID, Locators.seb_download_menu).send_keys(seb_download)

    def enter_seb_exit_link(self, seb_exit_link):

        self.driver.find_element(By.ID, Locators.seb_exit_link_field).click()
        self.driver.find_element(By.ID, Locators.seb_exit_link_field).send_keys(seb_exit_link)

    def enter_seb_confirm_quit(self, seb_confirm_quit):

        self.driver.find_element(By.ID, Locators.seb_confirm_quit_menu).click()
        self.driver.find_element(By.ID, Locators.seb_confirm_quit_menu).send_keys(seb_confirm_quit)

    def enter_seb_enable_quit(self, seb_enable_quit):

        self.driver.find_element(By.ID, Locators.seb_enable_quit_menu).click()
        self.driver.find_element(By.ID, Locators.seb_enable_quit_menu).send_keys(seb_enable_quit)

    def enter_seb_quit_password(self, seb_quit_password):

        self.driver.find_element(By.ID, Locators.seb_quit_password_field).clear()
        self.driver.find_element(By.ID, Locators.seb_quit_password_field).click()
        self.driver.find_element(By.ID, Locators.seb_quit_password_field).send_keys(seb_quit_password)

    def enter_seb_enable_reload(self, seb_enable_reload):

        self.driver.find_element(By.ID, Locators.seb_enable_reload_menu).click()
        self.driver.find_element(By.ID, Locators.seb_enable_reload_menu).send_keys(seb_enable_reload)

    def enter_seb_taskbar(self, seb_taskbar):

        self.driver.find_element(By.ID, Locators.seb_taskbar_menu).click()
        self.driver.find_element(By.ID, Locators.seb_taskbar_menu).send_keys(seb_taskbar)

    def enter_seb_show_reload(self, seb_show_reload):

        self.driver.find_element(By.ID, Locators.seb_show_reload_menu).click()
        self.driver.find_element(By.ID, Locators.seb_show_reload_menu).send_keys(seb_show_reload)

    def enter_seb_show_time(self, seb_show_time):

        self.driver.find_element(By.ID, Locators.seb_show_time_menu).click()
        self.driver.find_element(By.ID, Locators.seb_show_time_menu).send_keys(seb_show_time)

    def enter_seb_show_keyboard(self, seb_show_keyboard):

        self.driver.find_element(By.ID, Locators.seb_show_keyboard_menu).click()
        self.driver.find_element(By.ID, Locators.seb_show_keyboard_menu).send_keys(seb_show_keyboard)

    def enter_seb_show_wifi(self, seb_show_wifi):

        self.driver.find_element(By.ID, Locators.seb_show_wifi_menu).click()
        self.driver.find_element(By.ID, Locators.seb_show_wifi_menu).send_keys(seb_show_wifi)

    def enter_seb_enable_audio(self, seb_enable_audio):

        self.driver.find_element(By.ID, Locators.seb_enable_audio_menu).click()
        self.driver.find_element(By.ID, Locators.seb_enable_audio_menu).send_keys(seb_enable_audio)

    def enter_seb_mute_startup(self, seb_mute_startup):

        self.driver.find_element(By.ID, Locators.seb_mute_startup_menu).click()
        self.driver.find_element(By.ID, Locators.seb_mute_startup_menu).send_keys(seb_mute_startup)

    def enter_seb_enable_spellcheck(self, seb_enable_spellcheck):

        self.driver.find_element(By.ID, Locators.seb_enable_spellcheck_menu).click()
        self.driver.find_element(By.ID, Locators.seb_enable_spellcheck_menu).send_keys(seb_enable_spellcheck)

    def enter_seb_enable_url_filter(self, seb_enable_url_filter):

        self.driver.find_element(By.ID, Locators.seb_enable_url_filter_menu).click()
        self.driver.find_element(By.ID, Locators.seb_enable_url_filter_menu).send_keys(seb_enable_url_filter)

    def enter_seb_filter_embedded(self, seb_filter_embedded):

        self.driver.find_element(By.ID, Locators.seb_enable_audio_menu).click()
        self.driver.find_element(By.ID, Locators.seb_enable_audio_menu).send_keys(seb_filter_embedded)

    # Extra restrictions on attempts tab
    def click_extra_restrictions_tab(self):

        self.driver.find_element(By.XPATH, Locators.extra_restrictions_tab).click()

    def enter_restrictions_password(self, restrictions_password):

        self.driver.find_element(By.XPATH, Locators.restrictions_password_field).clear()
        self.driver.find_element(By.XPATH, Locators.restrictions_password_field).click()
        self.driver.find_element(By.XPATH, Locators.restrictions_password_field).send_keys(restrictions_password)

    def click_restrictions_show_more(self):

        self.driver.find_element(By.XPATH, Locators.restrictions_show_more_link).click()

    def enter_require_network_address(self, require_network_address):

        self.driver.find_element(By.ID, Locators.require_network_address_field).clear()
        self.driver.find_element(By.ID, Locators.require_network_address_field).click()
        self.driver.find_element(By.ID, Locators.require_network_address_field).send_keys(require_network_address)

    def click_first_delay_checkbox(self):

        self.driver.find_element(By.ID, Locators.first_delay_checkbox).click()

    def enter_first_delay_number(self, first_delay_number):

        self.driver.find_element(By.ID, Locators.first_delay_number_field).clear()
        self.driver.find_element(By.ID, Locators.first_delay_number_field).click()
        self.driver.find_element(By.ID, Locators.first_delay_number_field).send_keys(first_delay_number)

    def enter_first_delay_unit(self, first_delay_unit):

        self.driver.find_element(By.ID, Locators.first_delay_unit_menu).click()
        self.driver.find_element(By.ID, Locators.first_delay_unit_menu).send_keys(first_delay_unit)

    def click_later_delay_checkbox(self):

        self.driver.find_element(By.ID, Locators.later_delay_checkbox).click()

    def enter_later_delay_number(self, later_delay_number):

        self.driver.find_element(By.ID, Locators.later_delay_number_field).clear()
        self.driver.find_element(By.ID, Locators.later_delay_number_field).click()
        self.driver.find_element(By.ID, Locators.later_delay_number_field).send_keys(later_delay_number)

    def enter_later_delay_unit(self, later_delay_unit):

        self.driver.find_element(By.ID, Locators.later_delay_unit_menu).click()
        self.driver.find_element(By.ID, Locators.later_delay_unit_menu).send_keys(later_delay_unit)

    def enter_browser_security(self, browser_security):

        self.driver.find_element(By.ID, Locators.browser_security_menu).click()
        self.driver.find_element(By.ID, Locators.browser_security_menu).send_keys(browser_security)

    def enter_quiz_reattempt(self, quiz_reattempt):

        self.driver.find_element(By.ID, Locators.quiz_reattempt_menu).click()
        self.driver.find_element(By.ID, Locators.quiz_reattempt_menu).send_keys(quiz_reattempt)

    # Overall feedback tab
    def click_overall_feedback_tab(self):

        self.driver.find_element(By.XPATH, Locators.overall_feedback_tab).click()

    def enter_grade_boundary1_feedback(self, grade_boundary1_feedback):

        self.driver.find_element(By.ID, Locators.grade_boundary1_feedback_textbox).clear()
        self.driver.find_element(By.ID, Locators.grade_boundary1_feedback_textbox).click()
        self.driver.find_element(By.ID, Locators.grade_boundary1_feedback_textbox).send_keys(grade_boundary1_feedback)

    def enter_grade_boundary2(self, grade_boundary2):

        self.driver.find_element(By.ID, Locators.grade_boundary2_field).clear()
        self.driver.find_element(By.ID, Locators.grade_boundary2_field).click()
        self.driver.find_element(By.ID, Locators.grade_boundary2_field).send_keys(grade_boundary2)

    def enter_grade_boundary2_feedback(self, grade_boundary2_feedback):

        self.driver.find_element(By.ID, Locators.grade_boundary2_feedback_textbox).clear()
        self.driver.find_element(By.ID, Locators.grade_boundary2_feedback_textbox).click()
        self.driver.find_element(By.ID, Locators.grade_boundary2_feedback_textbox).send_keys(grade_boundary2_feedback)

    def click_add_more_feedback(self):

        self.driver.find_element(By.ID, Locators.add_more_feedback_button).click()

    # Common module tab
    def click_common_module_tab(self):

        self.driver.find_element(By.XPATH, Locators.common_module_tab).click()

    def enter_availability(self, availability):

        self.driver.find_element(By.ID, Locators.availability_menu).click()
        self.driver.find_element(By.ID, Locators.availability_menu).send_keys(availability)

    def enter_id_number(self, id_number):

        self.driver.find_element(By.ID, Locators.id_number_field).click()
        self.driver.find_element(By.ID, Locators.id_number_field).send_keys(id_number)

    def enter_force_language(self, force_language):

        self.driver.find_element(By.ID, Locators.force_language_menu).click()
        self.driver.find_element(By.ID, Locators.force_language_menu).send_keys(force_language)

    def enter_group_mode(self, group_mode):

        self.driver.find_element(By.ID, Locators.group_mode_menu).click()
        self.driver.find_element(By.ID, Locators.group_mode_menu).send_keys(group_mode)

    def enter_grouping(self, grouping):

        self.driver.find_element(By.ID, Locators.grouping_menu).click()
        self.driver.find_element(By.ID, Locators.grouping_menu).send_keys(grouping)

    def click_add_group_restriction(self):

        self.driver.find_element(By.XPATH, Locators.add_group_restriction_button).click()

    # Restrict access tab
    def click_restrict_access_tab(self):

        self.driver.find_element(By.XPATH, Locators.restrict_access_tab).click()

    def click_add_restriction(self):

        self.driver.find_element(By.XPATH, Locators.add_restriction_button).click()

    def click_restriction_activity_completion(self):

        self.driver.find_element(By.XPATH, Locators.restriction_activity_completion_button).click()

    def enter_student_match(self, student_match):

        self.driver.find_element(By.XPATH, Locators.student_match_menu).click()
        self.driver.find_element(By.XPATH, Locators.student_match_menu).send_keys(student_match)

    def enter_choose_activity(self, choose_activity):

        self.driver.find_element(By.XPATH, Locators.choose_activity_menu).click()
        self.driver.find_element(By.XPATH, Locators.choose_activity_menu).send_keys(choose_activity)

    def enter_completion_status(self, completion_status):

        self.driver.find_element(By.XPATH, Locators.completion_status_menu).click()
        self.driver.find_element(By.XPATH, Locators.completion_status_menu).send_keys(completion_status)

    # Activity completion tab
    def click_activity_completion_tab(self):

        self.driver.find_element(By.XPATH, Locators.activity_completion_tab).click()

    def enter_completion_tracking(self, completion_tracking):

        self.driver.find_element(By.ID, Locators.completion_tracking_menu).click()
        self.driver.find_element(By.ID, Locators.completion_tracking_menu).send_keys(completion_tracking)

    def click_expect_completed_checkbox(self):

        self.driver.find_element(By.ID, Locators.expect_completed_checkbox).click()

    def enter_expect_completed_day(self, expect_completed_day):

        self.driver.find_element(By.ID, Locators.expect_completed_day_menu).click()
        self.driver.find_element(By.ID, Locators.expect_completed_day_menu).send_keys(expect_completed_day)

    def enter_expect_completed_month(self, expect_completed_month):

        self.driver.find_element(By.ID, Locators.expect_completed_month_menu).click()
        self.driver.find_element(By.ID, Locators.expect_completed_month_menu).send_keys(expect_completed_month)

    def enter_expect_completed_year(self, expect_completed_year):

        self.driver.find_element(By.ID, Locators.expect_completed_year_menu).click()
        self.driver.find_element(By.ID, Locators.expect_completed_year_menu).send_keys(expect_completed_year)

    def enter_expect_completed_hour(self, expect_completed_hour):

        self.driver.find_element(By.ID, Locators.expect_completed_hour_menu).click()
        self.driver.find_element(By.ID, Locators.expect_completed_hour_menu).send_keys(expect_completed_hour)

    def enter_expect_completed_minute(self, expect_completed_minute):

        self.driver.find_element(By.ID, Locators.expect_completed_minute_menu).click()
        self.driver.find_element(By.ID, Locators.expect_completed_minute_menu).send_keys(expect_completed_minute)

    # Tags tab
    def click_tags_tab(self):

        self.driver.find_element(By.XPATH, Locators.quiz_tags_tab).click()

    def enter_tags(self, quiz_tags):

        self.driver.find_element(By.XPATH, Locators.quiz_tags_field).clear()
        self.driver.find_element(By.XPATH, Locators.quiz_tags_field).click()
        self.driver.find_element(By.XPATH, Locators.quiz_tags_field).send_keys(quiz_tags)

    # Competencies tab
    def click_competencies_tab(self):

        self.driver.find_element(By.XPATH, Locators.competencies_tab).click()

    def enter_course_competencies(self, course_competencies):

        self.driver.find_element(By.XPATH, Locators.course_competencies_field).clear()
        self.driver.find_element(By.XPATH, Locators.course_competencies_field).click()
        self.driver.find_element(By.XPATH, Locators.course_competencies_field).send_keys(course_competencies)

    def enter_activity_completion(self, activity_completion):

        self.driver.find_element(By.ID, Locators.activity_completion_menu).click()
        self.driver.find_element(By.ID, Locators.activity_completion_menu).send_keys(activity_completion)
