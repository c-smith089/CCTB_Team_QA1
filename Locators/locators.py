# Locators


class Locators:

    # HOME PAGE

    # Home page URL and title
    home_page_url = 'https://smithtechlearning.ca'
    home_page_title = 'Smith Tech Learning'

    # Home page locators
    login_link = 'Log in'  # By.LINK_TEXT

    # LOGIN PAGE

    # Login page URL and title
    login_page_url = 'https://smithtechlearning.ca/login/index.php'
    login_page_title = 'Smith Tech Learning: Log in to the site'

    # Login page locators
    username_field = 'username'  # By.ID
    password_field = 'password'  # By.ID
    login_button = 'loginbtn'  # By.ID

    # DASHBOARD PAGE

    # Dashboard URL and title
    dashboard_page_url = 'https://smithtechlearning.ca/my/'
    dashboard_page_title = 'Dashboard'

    # Dashboard page locators
    user_menu_link = 'usermenu'  # By.CLASS_NAME
    logout_link = '//*[@id="carousel-item-main"]/a[7]'  # By.XPATH
    admin_link = 'Site administration'  # By.LINK_TEXT

    # SITE ADMIN PAGE

    # Admin page URL and title
    admin_url = 'https://smithtechlearning.ca/admin/search.php'
    admin_title = 'STL: Administration: Search'

    # Admin page locators
    course_admin_link = 'Courses'  # By.LINK_TEXT
    user_admin_link = 'Users'  # By.LINK_TEXT

    # Courses admin URL
    course_admin_url = 'https://smithtechlearning.ca/admin/search.php#linkcourses'

    # Courses admin locators
    manage_courses_categories_link = 'Manage courses and categories'  # By.LINK_TEXT
    add_category_link = 'Add a category'  # By.LINK_TEXT
    add_course_link = 'Add a new course'  # By.LINK_TEXT

    # Users admin URL
    user_admin_url = 'https://smithtechlearning.ca/admin/search.php#linkusers'

    # Users admin Locators
    manage_users_link = 'Browse list of users'  # By.LINK_TEXT
    add_user_link = 'Add a new user'  # By.LINK_TEXT
    manage_cohorts_link = 'Cohorts'  # By.LINK_TEXT

    # MANAGE COURSES AND CATEGORIES PAGE

    # Manage courses and categories URL and title
    manage_courses_url = 'https://smithtechlearning.ca/course/management.php'
    manage_courses_title = 'Course and category management'

    # Manage courses and categories locators
    create_category_button = '/html/body/div[5]/div[3]/div/div[3]/div/section/div/form/div[2]/div[1]/div/div/div[1]/a'  # By.XPATH
    create_course_button = '/html/body/div[5]/div[3]/div/div[3]/div/section/div/form/div[2]/div[2]/div/div/div[1]/a'  # By.XPATH
    test_course_1_link = 'Test Course 1 (CS)'  # By.LINK_TEXT
    course_view_button = '/html/body/div[5]/div[3]/div/div[3]/div/section/div/form/div[2]/div[3]/div/div[2]/div[1]/a[1]'  # By.XPATH

    # TEST COURSE 1 PAGE

    # Test course 1 page URL and title
    test_course_1_url = 'https://smithtechlearning.ca/course/view.php?id=3'
    test_course_1_title = 'Course: Test Course 1 (CS)'

    # Test course 1 page locators
    edit_mode_toggle = '/html/body/div[3]/nav/div[2]/form/div/div/input'  # By.XPATH
    body_element = '/html/body/div[5]/nav/div[2]/div[6]'  # By.XPATH
    add_activity_link = '/html/body/div[5]/div[5]/div/div[3]/div/section/div/div/div/ul/li[2]/div[2]/button/span[2]'  # By.XPATH
    add_quiz_button = '/html/body/div[7]/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[16]/div/a/div[2]'  # By.XPATH

    # CREATE QUIZ PAGE

    # Create quiz page URL and title (Test Course 1)
    create_quiz_page_url = 'https://smithtechlearning.ca/course/modedit.php?add=quiz&type=&course=3&section=1&return=0&sr=0'
    create_quiz_page_title = 'Editing Quiz'

    # Create quiz page locators
    content_change_checkbox = '//*[@id="id_coursecontentnotification"]'  # By.XPATH
    save_quiz_button = '//*[@id="id_submitbutton2"]'  # By.XPATH

    # General tab
    quiz_name_field = 'id_name'  # By.ID
    quiz_description_textbox = 'id_introeditoreditable'  # By.ID
    display_description_checkbox = 'id_showdescription'  # By.ID

    # Timing tab
    timing_tab = '//*[@id="collapseElement-1"]'  # By.XPATH
    open_quiz_checkbox = 'id_timeopen_enabled'  # By.ID
    open_quiz_day_menu = 'id_timeopen_day'  # By.ID
    open_quiz_month_menu = 'id_timeopen_month'  # By.ID
    open_quiz_year_menu = 'id_timeopen_year'  # By.ID
    open_quiz_hour_menu = 'id_timeopen_hour'  # By.ID
    open_quiz_minute_menu = 'id_timeopen_minute'  # By.ID
    close_quiz_checkbox = 'id_timeclose_enabled'  # By.ID
    close_quiz_day_menu = 'id_timeclose_day'  # By.ID
    close_quiz_month_menu = 'id_timeclose_month'  # By.ID
    close_quiz_year_menu = 'id_timeclose_year'  # By.ID
    close_quiz_hour_menu = 'id_timeclose_hour'  # By.ID
    close_quiz_minute_menu = 'id_timeclose_minute'  # By.ID
    time_limit_checkbox = 'id_timelimit_enabled'  # By.ID
    time_limit_number_field = 'id_timelimit_number'  # By.ID
    time_limit_unit_menu = 'id_timelimit_timeunit'  # By.ID
    when_time_expires_menu = 'id_overduehandling'  # By.ID

    # Grade tab
    grade_tab = '//*[@id="collapseElement-2"]'  # By.XPATH
    grade_category_menu = 'id_gradecat'  # By.ID
    grade_pass_field = 'id_gradepass'  # By.ID
    attempts_menu = 'id_attempts'  # By.ID
    grading_method_menu = 'id_grademethod'  # By.ID

    # Layout tab
    layout_tab = '//*[@id="collapseElement-3"]'  # By.XPATH
    new_page_menu = 'id_questionsperpage'  # By.ID
    layout_show_more_link = '/html/body/div[5]/div[5]/div/div[3]/div/section/div/form/fieldset[4]/div[2]/div[2]/div/a'  # By.XPATH
    nav_method_menu = 'id_navmethod'  # By.ID

    # Question behaviour tab
    question_behaviour_tab = '//*[@id="collapseElement-4"]'  # By.XPATH
    shuffle_answers_menu = 'id_shuffleanswers'  # By.ID
    question_behaviour_menu = 'id_preferredbehaviour'  # By.ID
    question_behaviour_show_more_link = '/html/body/div[5]/div[5]/div/div[3]/div/section/div/form/fieldset[5]/div[2]/div[3]/div/a'  # By.XPATH
    attempts_build_menu = 'id_attemptonlast'  # By.ID

    # Review options tab
    review_options_tab = '//*[@id="collapseElement-5"]'  # By.XPATH
    open_attempt_checkbox = 'id_attemptopen'  # By.ID
    open_correct_checkbox = 'id_correctnessopen'  # By.ID
    open_marks_checkbox = 'id_marksopen'  # By.ID
    open_specific_feedback_checkbox = 'id_specificfeedbackopen'  # By.ID
    open_general_feedback_checkbox = 'id_generalfeedbackopen'  # By.ID
    open_right_answer_checkbox = 'id_rightansweropen'  # By.ID
    open_overall_feedback_checkbox = 'id_overallfeedbackopen'  # By.ID
    immediately_attempt_checkbox = 'id_attemptimmediately'  # By.ID
    immediately_correct_checkbox = 'id_correctnessimmediately'  # By.ID
    immediately_marks_checkbox = 'id_marksimmediately'  # By.ID
    immediately_specific_feedback_checkbox = 'id_specificfeedbackimmediately'  # By.ID
    immediately_general_feedback_checkbox = 'id_generalfeedbackimmediately'  # By.ID
    immediately_right_answer_checkbox = 'id_rightanswerimmediately'  # By.ID
    immediately_overall_feedback_checkbox = 'id_overallfeedbackimmediately'  # By.ID
    closed_attempt_checkbox = 'id_attemptclosed'  # By.ID
    closed_correct_checkbox = 'id_correctnessclosed'  # By.ID
    closed_marks_checkbox = 'id_marksclosed'  # By.ID
    closed_specific_feedback_checkbox = 'id_specificfeedbackclosed'  # By.ID
    closed_general_feedback_checkbox = 'id_generalfeedbackclosed'  # By.ID
    closed_right_answer_checkbox = 'id_rightanswerclosed'  # By.ID
    closed_overall_feedback_checkbox = 'id_overallfeedbackclosed'  # By.ID

    # Appearance tab
    appearance_tab = '//*[@id="collapseElement-6"]'  # By.XPATH
    show_picture_menu = 'id_showuserpicture'  # By.ID
    decimal_places_grades_menu = 'id_decimalpoints'  # By.ID
    decimal_places_marks_menu = 'id_questiondecimalpoints'  # By.ID
    appearance_show_more_link = '/html/body/div[5]/div[5]/div/div[3]/div/section/div/form/fieldset[7]/div[2]/div[4]/div/a'  # By.XPATH
    show_blocks_menu = 'id_showblocks'  # By.ID

    # Safe exam browser tab
    safe_exam_browser_tab = '//*[@id="collapseElement-7"]'  # By.XPATH
    require_seb_menu = 'id_seb_requiresafeexambrowser'  # By.ID
    seb_download_menu = 'id_seb_showsebdownloadlink'  # By.ID
    seb_exit_link_field = 'id_seb_linkquitseb'  # By.ID
    seb_confirm_quit_menu = 'id_seb_userconfirmquit'  # By.ID
    seb_enable_quit_menu = 'id_seb_userconfirmquit'  # By.ID
    seb_quit_password_field = 'id_seb_quitpassword'  # By.ID
    seb_enable_reload_menu = 'id_seb_allowreloadinexam'  # By.ID
    seb_taskbar_menu = 'id_seb_showsebtaskbar'  # By.ID
    seb_show_reload_menu = 'id_seb_showreloadbutton'  # By.ID
    seb_show_time_menu = 'id_seb_showtime'  # By.ID
    seb_show_keyboard_menu = 'id_seb_showkeyboardlayout'  # By.ID
    seb_show_wifi_menu = 'id_seb_showwificontrol'  # By.ID
    seb_enable_audio_menu = 'id_seb_enableaudiocontrol'  # By.ID
    seb_mute_startup_menu = 'id_seb_muteonstartup'  # By.ID
    seb_enable_spellcheck_menu = 'id_seb_allowspellchecking'  # By.ID
    seb_enable_url_filter_menu = 'id_seb_activateurlfiltering'  # By.ID
    seb_filter_embeddeded_menu = 'id_seb_filterembeddedcontent'  # By.ID

    # Extra restrictions tab
    extra_restrictions_tab = '//*[@id="collapseElement-8"]'  # By.XPATH
    restrictions_password_field = '/html/body/div[5]/div[5]/div/div[3]/div/section/div/form/fieldset[9]/div[2]/div[1]/div[2]/span/a[1]/i'  # By.XPATH
    restrictions_show_more_link = '/html/body/div[5]/div[5]/div/div[3]/div/section/div/form/fieldset[9]/div[2]/div[2]/div/a'  # By.XPATH
    require_network_address_field = 'id_subnet'  # By.ID
    first_delay_checkbox = 'id_delay1_enabled'  # By.ID
    first_delay_number_field = 'id_delay1_number'  # By.ID
    first_delay_unit_menu = 'id_delay1_timeunit'  # By.ID
    later_delay_checkbox = 'id_delay2_enabled'  # By.ID
    later_delay_number_field = 'id_delay2_number'  # By.ID
    later_delay_unit_menu = 'id_delay2_timeunit'  # By.ID
    browser_security_menu = 'id_browsersecurity'  # By.ID
    quiz_reattempt_menu = 'id_allowofflineattempts'  # By.ID

    # Overall feedback tab
    overall_feedback_tab = '//*[@id="collapseElement-9"]'  # By.XPATH
    grade_boundary1_feedback_textbox = 'id_feedbacktext_0editable'  # By.ID
    grade_boundary2_field = 'id_feedbackboundaries_0'
    grade_boundary2_feedback_textbox = 'id_feedbacktext_1editable'  # By.ID
    add_more_feedback_button = 'id_boundary_add_fields'  # By.ID

    # Common module tab
    common_module_tab = '//*[@id="collapseElement-10"]'  # By.XPATH
    availability_menu = 'id_visible'  # By.ID
    id_number_field = 'id_cmidnumber'  # By.ID
    force_language_menu = 'id_lang'  # By.ID
    group_mode_menu = 'id_groupmode'  # By.ID
    grouping_menu = 'id_groupingid'  # By.ID
    add_group_restriction_button = '//*[@id="restrictbygroup"]'  # By.XPATH

    # Restrict access tab
    restrict_access_tab = '//*[@id="collapseElement-11"]'  # By.XPATH
    add_restriction_button = '/html/body/div[5]/div[5]/div/div[3]/div/section/div/form/fieldset[12]/div[2]/div/div[2]/div[1]/div/div[1]/div[5]/button'  # By.XPATH
    restriction_activity_completion_button = '//*[@id="availability_addrestriction_completion"]'  # By.XPATH
    student_match_menu = '/html/body/div[5]/div[5]/div/div[3]/div/section/div/form/fieldset[12]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/label/select'  # By.XPATH
    choose_activity_menu = '/html/body/div[5]/div[5]/div/div[3]/div/section/div/form/fieldset[12]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/span[1]/span[2]/label[1]/select'  # By.XPATH
    completion_status_menu = '/html/body/div[5]/div[5]/div/div[3]/div/section/div/form/fieldset[12]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/span[1]/span[2]/label[2]/select'  # By.XPATH

    # Activity completion tab
    activity_completion_tab = '//*[@id="collapseElement-12"]'  # By.XPATH
    completion_tracking_menu = 'id_completion'  # By.ID
    expect_completed_checkbox = 'id_completionexpected_enabled'  # By.ID
    expect_completed_day_menu = 'id_completionexpected_day'  # By.ID
    expect_completed_month_menu = 'id_completionexpected_month'  # By.ID
    expect_completed_year_menu = 'id_completionexpected_year'  # By.ID
    expect_completed_hour_menu = 'id_completionexpected_hour'  # By.ID
    expect_completed_minute_menu = 'id_completionexpected_minute'  # By.ID

    # Tags tab
    quiz_tags_tab = '//*[@id="collapseElement-13"]'  # By.XPATH
    quiz_tags_field = '/html/body/div[5]/div[5]/div/div[3]/div/section/div/form/fieldset[14]/div[2]/div/div[2]/div[3]/input'  # By.XPATH

    # Competencies tab
    competencies_tab = '//*[@id="collapseElement-14"]'  # By.XPATH
    course_competencies_field = '/html/body/div[5]/div[5]/div/div[3]/div/section/div/form/fieldset[15]/div[2]/div[1]/div[2]/div[3]/input'  # By.XPATH
    activity_completion_menu = 'id_competency_rule'  # By.ID
