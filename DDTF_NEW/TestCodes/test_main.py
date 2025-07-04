import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators.Test_Locators import test_locators
from Test_Excel_Functions.Excel_Functions import all_excel_functions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


class Test_orange:
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        excel_file = 'D:\\Project_Copy\\New_OrangeHRM\\DDTF_NEW\\TestDatas\\Excel.xlsx'
        sheet_name = 'Sheet1'
        self.s = all_excel_functions(excel_file, sheet_name)
        self.rows = self.s.row_count()
        yield
        self.driver.close()

    def test_login(self, boot):
        self.driver.get(test_locators.url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 8)
        start_row = 2
        end_row = 4

        for row_no in range(start_row, end_row + 1):
            username = self.s.read_data(row_no, 6)
            password = self.s.read_data(row_no, 7)

            username_element = wait.until(EC.visibility_of_element_located((By.NAME, test_locators().Email)))
            username_element.send_keys(username)

            password_element = wait.until(EC.visibility_of_element_located((By.NAME, test_locators().Password)))
            password_element.send_keys(password)

            login_button = wait.until(EC.element_to_be_clickable((By.XPATH, test_locators().Login_button)))
            login_button.click()

            try:
                wait.until(EC.url_matches('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'))
                self.s.write_data(row_no, 8, "TEST PASS")
                print("SUCCESS : Logged in with Username {a} & {b}".format(a=username, b=password))

                profile_image = wait.until(EC.presence_of_element_located((By.XPATH, test_locators().Profile_image)))
                profile_image.click()
                logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, test_locators().Logout_button)))
                logout_button.click()

                wait.until(EC.url_matches("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"))

            except TimeoutException:
                self.s.write_data(row_no, 8, "TEST FAIL")

                assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
                print("FAIL : Login failed with Username {a} & {b}".format(a=username, b=password))

                self.driver.refresh()
