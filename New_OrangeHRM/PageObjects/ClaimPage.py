"""
Claim Page contains Creating Claim
"""

from selenium.webdriver.common.by import By
from PageObjects.HomePage import BasePage
from Locators.TestLocators import OrangeHRMLocators

class ClaimPage(BasePage):
    CLAIM = (By.XPATH,OrangeHRMLocators.claim)
    ADMIN_EMPLOYEE = (By.XPATH, OrangeHRMLocators.admin_employee)
    ASSIGN_CLAIM = (By.XPATH,OrangeHRMLocators.assign_claim)
    EVENT_SELECT = (By.XPATH,OrangeHRMLocators.event_select)
    EVENT_SELECT1 = (By.XPATH,OrangeHRMLocators.event_select1)
    CURRENCY_SELECT = (By.XPATH,OrangeHRMLocators.currency_select)
    CURRENCY_SELECT1 = (By.XPATH,OrangeHRMLocators.currency_select1)
    CLAIM_CREATE = (By.XPATH,OrangeHRMLocators.create_claim)
    SUBMIT_CLAIM = (By.XPATH,OrangeHRMLocators.submit)
    CLAIM_PRESENT = (By.XPATH,OrangeHRMLocators.claim_present)
    MY_CLAIM = (By.XPATH,OrangeHRMLocators.emp_claim)
    NAME_SELECT = (By.XPATH,OrangeHRMLocators.name_select)


    def claim_click(self):
        self.click(self.CLAIM)

    def assign_claim(self):
        self.click(self.ASSIGN_CLAIM)

    def add_employee(self, employee):
        self.enter_text(self.ADMIN_EMPLOYEE, employee)

    def event_claim(self):
        self.click(self.EVENT_SELECT)
        self.click(self.EVENT_SELECT1)

    def currency_select(self):
        self.click(self.CURRENCY_SELECT)
        self.click(self.CURRENCY_SELECT1)

    def claim_button(self):
        self.click(self.CLAIM_CREATE)

    def submit_claim(self):
        self.click(self.SUBMIT_CLAIM)

    def my_claim(self):
        self.click(self.MY_CLAIM)

    def name_select(self):
        self.click(self.NAME_SELECT)

    def claim_validation(self):
        claim_user = self.find_element(self.CLAIM_PRESENT)
        if claim_user.is_displayed() and claim_user.is_enabled():
            return True
        else:
            return False





