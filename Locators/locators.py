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
