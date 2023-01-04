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
    attempts_allowed = '1'
    grading_method = 'Average grade'

    # Layout tab
    new_page = 'Every 2 questions'
    navigation_method = 'Sequential'

    # Question behaviour tab
    shuffle_questions = 'No'
    question_behaviour = 'Immediate feedback'
    attempts_build = 'Yes'

    # Review options tab (only checkboxes requiring a single click)

    # Appearance tab
    show_user_picture = 'Small image'
    decimal_places_grades = '3'
    decimal_places_marks = '2'
    show_blocks = 'Yes'

    # Safe exam browser tab
    require_seb = 'Yes - Configure manually'
    seb_download = 'No'
    seb_exit_link = 'https://exit.testing.com/'
    seb_confirm_quit = 'No'
    seb_enable_quit = 'Yes'
    seb_quit_password = 'createquiztest1'
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

    # Extra restrictions on attempts tab

