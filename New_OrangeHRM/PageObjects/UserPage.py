"""
User Page Contains Creating User
"""

from selenium.webdriver.common.by import By
from PageObjects.HomePage import BasePage
from Locators.TestLocators import OrangeHRMLocators

class UserPage(BasePage):
    ADMIN_LOCATOR = (By.XPATH, OrangeHRMLocators.admin)
    ADD_ADMIN = (By.XPATH,OrangeHRMLocators.add_admin)
    ADMIN_USER = (By.XPATH,OrangeHRMLocators.admin_user)
    ADMIN_USER_ROLE = (By.XPATH,OrangeHRMLocators.admin_user_role)
    ADMIN_EMPLOYEE = (By.XPATH,OrangeHRMLocators.admin_employee)
    ADMIN_STATUS = (By.XPATH,OrangeHRMLocators.admin_status)
    ADMIN_STATUS_ROLE = (By.XPATH,OrangeHRMLocators.admin_status_role)
    ADMIN_USERNAME  = (By.XPATH,OrangeHRMLocators.admin_username)
    ADMIN_PASSWORD = (By.XPATH,OrangeHRMLocators.admin_password)
    ADMIN_CF_PASSWORD = (By.XPATH,OrangeHRMLocators.admin_cf_password)
    ADMIN_SAVE = (By.XPATH,OrangeHRMLocators.admin_save)
    ADMIN_PRESENT = (By.XPATH,OrangeHRMLocators.admin_present)

    def click_admin(self):
        self.click(self.ADMIN_LOCATOR)

    def click_add(self):
        self.click(self.ADD_ADMIN)

    def add_user_role(self):
        self.click(self.ADMIN_USER)
        self.click(self.ADMIN_USER_ROLE)

    def add_employee(self,employee):
        self.enter_text(self.ADMIN_EMPLOYEE,employee)

    def add_status(self):
        self.click(self.ADMIN_STATUS)
        self.click(self.ADMIN_STATUS_ROLE)

    def add_username(self,username):
        self.enter_text(self.ADMIN_USERNAME,username)

    def add_password(self,password):
        self.enter_text(self.ADMIN_PASSWORD,password)

    def add_confirm_password(self,confirm_password):
        self.enter_text(self.ADMIN_CF_PASSWORD,confirm_password)

    def admin_save(self):
        self.click(self.ADMIN_SAVE)

    def admin_user_enabled(self):
        admin_user = self.find_element(self.ADMIN_PRESENT)
        if admin_user.is_displayed() and admin_user.is_enabled():
            return True
        else:
            return False


