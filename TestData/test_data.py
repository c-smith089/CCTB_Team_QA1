# Test Data


class TestData:

    # LOGIN CREDENTIALS

    # Standard users
    testuser1_username = 'testuser1'
    testuser1_password = 'Testing2022!'

    # Admin users
    adminuser1_username = 'adminuser1'
    adminuser1_password = 'Testing2022!'

    # CREATE QUIZ FORM

    # General tab
    testquiz1_name = 'Test Quiz 1'
    testquiz1_description = 'This is Test Quiz 1 for Selenium testing purposes. This is Test Quiz 1 for Selenium testing purposes. This is Test Quiz 1 for Selenium testing purposes. This is Test Quiz 1 for Selenium testing purposes.'

    # Timing tab
    open_quiz_day = '01'
    open_quiz_month = 'January'
    open_quiz_year = '2023'
    open_quiz_hour = '00'
    open_quiz_minute = '00'

    close_quiz_day = '02'
    close_quiz_month = 'February'
    close_quiz_year = '2023'
    close_quiz_hour = '00'
    close_quiz_minute = '00'

    time_limit_number = '1'
    time_limit_unit = 'hours'

    when_time_expires = 'Attempts must be submitted before time expires, or they are not counted'

    # Grade tab
    grade_category = 'Uncategorised'  # only option, create grade category to further test
    grade_to_pass = '80'
    attempts_allowed = '2'
    grading_method = 'Average grade'

    # Layout tab
    new_page = 'Every 2 questions'
    navigation_method = 'Sequential'

    # Question behaviour tab
    shuffle_answers = 'No'
    question_behaviour = 'Immediate feedback'
    attempts_build = 'Yes'

    # Review options tab (only checkboxes requiring a single click)

    # Appearance tab
    show_user_picture = 'Small image'
    decimal_places_grades = '3'
    decimal_places_marks = '2'
    show_blocks = 'Yes'

    # Safe exam browser tab
    require_seb = 'Yes – Configure manually'
    seb_download = 'No'
    seb_exit_link = 'https://exit.testing.com/'
    seb_confirm_quit = 'No'
    seb_enable_quit = 'Yes'
    seb_quit_password = 'Qu!tS3bTest1'
    seb_enable_reload = 'No'
    seb_taskbar = 'Yes'
    seb_show_reload = 'No'
    seb_show_time = 'No'
    seb_show_keyboard = 'No'
    seb_show_wifi = 'Yes'
    seb_enable_audio = 'Yes'
    seb_mute_startup = 'Yes'
    seb_enable_spellcheck = 'Yes'
    seb_enable_url_filter = 'Yes'
    seb_filter_embedded = 'Yes'
    seb_expression_allow = 'Test expressions allowed'
    seb_regex_allow = 'Test regex allowed'
    seb_expression_block = 'Test expressions blocked'
    seb_regex_block = 'Test regex blocked'

    # Extra restrictions on attempts tab
    restriction_password = '3xtr@Restrictions'
    require_network_address = '0.0.0.0'
    first_delay_number = '2'
    first_delay_unit = 'hours'
    later_delay_number = '1'
    later_delay_unit = 'hours'
    browser_security = 'Full screen pop-up with some JavaScript security'
    allow_quiz_offline = 'Yes'

    # Overall feedback tab
    grade_boundary1_feedback = 'This is grade boundary 1 feedback for test 1. This is grade boundary 1 feedback for test 1.'
    grade_boundary2 = '90%'
    grade_boundary2_feedback = 'This is grade boundary 2 feedback for test 1. This is grade boundary 2 feedback for test 1.'
    grade_boundary3 = '80%'
    grade_boundary3_feedback = 'This is grade boundary 3 feedback for test 1. This is grade boundary 3 feedback for test 1.'
    grade_boundary4 = '65%'
    grade_boundary4_feedback = 'This is grade boundary 4 feedback for test 1. This is grade boundary 4 feedback for test 1.'
    grade_boundary5 = '50%'
    grade_boundary5_feedback = 'This is grade boundary 5 feedback for test 1. This is grade boundary 5 feedback for test 1.'

    # Common module settings tab
    availability = 'Hide from students'
    id_number = '00504861'
    force_language = 'English (en)'
    group_mode = 'Separate groups'

    # Restrict access tab
    student_match = 'must not'
    match_all_any = 'any'
    group = '(Any group)'
    choose_activity = 'Previous activity with completion'
    completion_requirement = 'must be complete with pass grade'

    restrict_from_until = 'until'
    restrict_day = '01'
    restrict_month = '05'
    restrict_year = '2024'
    restrict_hour = '12'
    restrict_minute = '00'

    restrict_grade = 'Course total'
    restrict_greater_than = '50'
    restrict_less_than = '90'

    restrict_profile_field = 'Country'
    restrict_profile_operator = 'contains'
    restrict_profile_value = 'Canada'

    # Big change