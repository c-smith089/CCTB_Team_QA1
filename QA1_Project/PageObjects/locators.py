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

