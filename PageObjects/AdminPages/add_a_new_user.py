# add a new user
from selenium.webdriver.support.select import Select

# Locators
from Locators.locators import Locators as L

from selenium.webdriver.common.by import By


class AddANewUser:

    def __init__(self, driver):

        self.driver = driver

    def enter_username(self,  username):
        self.driver.find_element(By.ID, L.create_user_username_tb).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.LINK_TEXT, L.create_user_password_link).click()
        self.driver.find_element(By.ID, L.create_user_password_tb).send_keys(password)

    def enter_first_name(self,firstname):
        self.driver.find_element(By.ID, 'id_firstname').send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element(By.ID, 'id_lastname').send_keys(lastname)

    def enter_email_address(self, emailaddress):
        self.driver.find_element(By.ID, 'id_email').send_keys(emailaddress)

    def select_email_display_option(self,email_display_option):
        Select(self.driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text(email_display_option)

    def enter_moodle_net_profile(self,moodle_net_profile):
        self.driver.find_element(By.ID, 'id_moodlenetprofile').send_keys(moodle_net_profile)

    def enter_city(self,city):
        self.driver.find_element(By.ID, 'id_city').send_keys(city)

    def select_country(self,country):
        Select(self.driver.find_element(By.ID, 'id_country')).select_by_visible_text(country)