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
    add_course_link = 'Add a new course'  # By.LINK.TEXT

    # Users admin URL
    user_admin_url = 'https://smithtechlearning.ca/admin/search.php#linkusers'

    # Users admin Locators
    manage_users_link = 'Browse list of users'  # By.LINK_TEXT
    add_user_link = 'Add a new user'  # By.LINK_TEXT
    manage_cohorts_link = 'Cohorts'  # By.LINK_TEXT

    # v----------------------- LANDING PAGE ------------------------v

    # Landing page url and title
    landing_page_url = 'https://smithtechlearning.ca'
    landing_page_title = 'Smith Tech Learning'

    # Landing page objects

    # login_page_link_search = By.LINK_TEXT
    login_page_link_text = 'Log in'


    # v------------ Login credentials -------------v
    login_username = 'farnad'
    login_password = 'Welcome2022!?'

    # v------------ ADMIN PAGE: Users -------------v

    add_a_new_user = 'Add a new user'

    # v----------------------- CREATE USER PAGE ------------------------v

    # Create user page url and title
    create_user_page_url = 'https://smithtechlearning.ca/user/editadvanced.php?id=-1'
    create_user_page_title = 'STL: Administration: Users: Accounts: Add a new user'

    # Create user page objects

    create_user_username_tb = 'id_username'
    new_username = 'username1'

    create_user_password_link= 'Click to enter text'
    create_user_password_tb='id_newpassword'
    new_password = 'password1'

    first_name='Firstname'
    last_name="Lastname"
    email_address="email@test.com"
    email_display_option='Allow everyone to see my email address'
    moodle_net_profile = f'https://moodle.net/{new_username}'
    city="Vancouver"