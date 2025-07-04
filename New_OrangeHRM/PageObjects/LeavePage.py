"""
Leave Page Contains Leaves
"""

from selenium.webdriver.common.by import By
from PageObjects.HomePage import BasePage
from Locators.TestLocators import OrangeHRMLocators

class LeavePage(BasePage):
    LEAVE = (By.XPATH,OrangeHRMLocators.leave)
    ASSIGN_LEAVE = (By.XPATH,OrangeHRMLocators.assign_leave)
    ADMIN_EMPLOYEE = (By.XPATH, OrangeHRMLocators.admin_employee)
    LEAVE_TYPE = (By.XPATH,OrangeHRMLocators.leave_type)
    PERSON_LEAVE = (By.XPATH,OrangeHRMLocators.person_leave)
    FROM_DATE = (By.XPATH,OrangeHRMLocators.from_date)
    TO_DATE = (By.XPATH,OrangeHRMLocators.to_date)
    CLICK_LEAVE = (By.XPATH,OrangeHRMLocators.click_leave)
    OK_LEAVE = (By.XPATH,OrangeHRMLocators.ok_leave)
    MY_LEAVE = (By.XPATH,OrangeHRMLocators.my_leave)
    LEAVE_ASSERT = (By.XPATH,OrangeHRMLocators.leave_select)

    def leave_click(self):
        self.click(self.LEAVE)

    def assign_leave(self):
        self.click(self.ASSIGN_LEAVE)

    def add_employee(self, employee):
        self.enter_text(self.ADMIN_EMPLOYEE, employee)

    def leave_type(self):
        self.click(self.LEAVE_TYPE)
        self.click(self.PERSON_LEAVE)

    def dates(self,from_date):
        self.enter_text(self.FROM_DATE,from_date)
        self.click(self.TO_DATE)


    def click_leave(self):
        self.click(self.CLICK_LEAVE)

    def ok_leave(self):
        self.click(self.OK_LEAVE)

    def my_leave(self):
        self.click(self.MY_LEAVE)

    def assert_leave(self):
        my_leave = self.find_element(self.LEAVE_ASSERT)
        if my_leave.is_displayed():
            return True
        else:
            return False











