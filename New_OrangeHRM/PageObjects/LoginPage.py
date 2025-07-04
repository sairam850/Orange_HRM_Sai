"""
Login page contain methods related to the login action
"""


from selenium.webdriver.common.by import By
from PageObjects.HomePage import BasePage
from Locators.TestLocators import OrangeHRMLocators

class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME,OrangeHRMLocators.username_locator)
    PASSWORD_INPUT = (By.NAME,OrangeHRMLocators.password_locator)
    LOGIN_LOCATOR = (By.XPATH,OrangeHRMLocators.login_button_locator)
    DROP_DOWN = (By.XPATH,OrangeHRMLocators.drop_down_selector)
    LOGOUT = (By.XPATH,OrangeHRMLocators.logout)
    ADMIN_LOCATOR = (By.XPATH,OrangeHRMLocators.admin)
    PIM_LOCATOR = (By.XPATH,OrangeHRMLocators.pim)
    RECRUITMENT = (By.XPATH,OrangeHRMLocators.recruitment)
    MY_INFO = (By.XPATH,OrangeHRMLocators.my_info)
    PERFORMANCE = (By.XPATH,OrangeHRMLocators.performance)
    DASHBOARD = (By.XPATH,OrangeHRMLocators.dashboard)
    FORGOT_PASS = (By.XPATH,OrangeHRMLocators.forgot_password)
    RESET_PASS = (By.XPATH,OrangeHRMLocators.reset_password)
    CONF_MESSAGE = (By.XPATH,OrangeHRMLocators.conf_message)
    PERS_DETAIL = (By.XPATH,OrangeHRMLocators.personal_details)
    CONT_DETAIL = (By.XPATH,OrangeHRMLocators.contact_details)
    EME_CONTACTS = (By.XPATH,OrangeHRMLocators.emergency_contacts)

    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_LOCATOR)

    def click_dropdown(self):
        self.click(self.DROP_DOWN)

    def click_logout(self):
        self.click(self.LOGOUT)

    def check_username_password(self):
        self.is_visible(self.USERNAME_INPUT)
        self.is_visible(self.PASSWORD_INPUT)
        username_text_box = self.find_element(self.USERNAME_INPUT)
        password_text_box = self.find_element(self.PASSWORD_INPUT)
        if username_text_box.is_displayed() and password_text_box.is_displayed():
            return True
        else:
            return False

    def menu_item_validation(self):
        self.is_clickable(self.ADMIN_LOCATOR)
        self.is_clickable(self.PIM_LOCATOR)
        self.is_clickable(self.RECRUITMENT)
        self.is_clickable(self.MY_INFO)
        self.is_clickable(self.PERFORMANCE)
        self.is_clickable(self.DASHBOARD)
        self.is_visible(self.ADMIN_LOCATOR)
        self.is_visible(self.PIM_LOCATOR)
        self.is_visible(self.RECRUITMENT)
        self.is_visible(self.MY_INFO)
        self.is_visible(self.PERFORMANCE)
        self.is_visible(self.DASHBOARD)
        Admin_Locator = self.find_element(self.ADMIN_LOCATOR)
        Pim_Locator = self.find_element(self.PIM_LOCATOR)
        Recruitment_Locator = self.find_element(self.RECRUITMENT)
        My_Info_Locator = self.find_element(self.MY_INFO)
        Performance_Locator = self.find_element(self.PERFORMANCE)
        Dashboard_Locator = self.find_element(self.DASHBOARD)
        if Admin_Locator.is_enabled() and Pim_Locator.is_enabled()  and Recruitment_Locator.is_enabled() and My_Info_Locator.is_enabled() and Performance_Locator.is_enabled() and Dashboard_Locator.is_enabled():
            return True
        else:
            return False

    def forgot_password(self,user_input):
        self.click(self.FORGOT_PASS)
        self.enter_text(self.USERNAME_INPUT, user_input)
        self.click(self.RESET_PASS)
        confirmation_message = self.find_element(self.CONF_MESSAGE)
        if confirmation_message.is_displayed():
            return True
        else:
            return False

    def my_info_pers_detail(self):
        self.click(self.MY_INFO)
        self.is_clickable(self.PERS_DETAIL)
        self.is_visible(self.PERS_DETAIL)
        self.click(self.PERS_DETAIL)

    def my_info_contact_details(self):
        self.click(self.MY_INFO)
        self.is_clickable(self.CONT_DETAIL)
        self.is_visible(self.CONT_DETAIL)
        self.click(self.CONT_DETAIL)

    def my_info_emergency_con(self):
        self.click(self.MY_INFO)
        self.is_clickable(self.EME_CONTACTS)
        self.is_visible(self.EME_CONTACTS)
        self.click(self.EME_CONTACTS)
















