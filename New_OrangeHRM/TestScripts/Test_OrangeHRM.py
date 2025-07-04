from PageObjects.HomePage import BasePage
from PageObjects.ClaimPage import ClaimPage
from PageObjects.LoginPage import LoginPage
from PageObjects.LeavePage import LeavePage
from PageObjects.UserPage import UserPage
from time import sleep
import pytest
from Configuration.conftest import driver
from Data.TestData import Data

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test case for Valid Url
def test_valid_url(driver):
    driver.get(Data.url)
    basepage = BasePage(driver)

    # asserting expected vs actual url
    assert basepage.fetch_url() == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    print("Success: Test Case Passed for Valid URL")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test case for Valid Username and Password
def test_check_uname_password(driver):
    driver.get(Data.url)
    loginpage = LoginPage(driver)

    # Asserting Username and Password Tab
    assert loginpage.check_username_password() == True
    print("Success: Test Case Passed for Check Username and Password")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test case for Forgot Password
def test_forgot_password(driver):
    driver.get(Data.url)
    loginpage = LoginPage(driver)

    # Validate Text for Forgot Password
    assert loginpage.forgot_password(Data.username) == True
    print("Success: Test Case Passed for Forgot Password")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test case for Menu Items
def test_menu_items(driver):
    driver.get(Data.url)
    loginpage = LoginPage(driver)
    loginpage.enter_username(Data.username)
    loginpage.enter_password(Data.password)
    loginpage.click_login()

    # Check Menu Items Displayed
    assert loginpage.menu_item_validation() == True
    print("Success: Test Case Passed for Menu Validation")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test case for My_Info_Personal
def test_my_info_pers_detail(driver):
    driver.get(Data.url)
    loginpage = LoginPage(driver)
    basepage = BasePage(driver)
    loginpage.enter_username(Data.username)
    loginpage.enter_password(Data.password)
    loginpage.click_login()
    loginpage.my_info_pers_detail()

    # asserting expected vs actual url
    assert basepage.fetch_url() == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7"
    print("Success: Test Case Passed for Personal Detail Validation")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test case for My_Info_Contact
def test_my_info_contact_details(driver):
    driver.get(Data.url)
    loginpage = LoginPage(driver)
    basepage = BasePage(driver)
    loginpage.enter_username(Data.username)
    loginpage.enter_password(Data.password)
    loginpage.click_login()
    loginpage.my_info_contact_details()

    # asserting expected vs actual url
    assert basepage.fetch_url() == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/contactDetails/empNumber/7"
    print("Success: Test Case Passed for Contact Detail Validation")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test case for My_Info_Contact
def test_my_info_emergency_con(driver):
    driver.get(Data.url)
    loginpage = LoginPage(driver)
    basepage = BasePage(driver)
    loginpage.enter_username(Data.username)
    loginpage.enter_password(Data.password)
    loginpage.click_login()
    loginpage.my_info_emergency_con()

    # asserting expected vs actual url
    assert basepage.fetch_url() == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmergencyContacts/empNumber/7"
    print("Success: Test Case Passed for Emergency Contact Validation")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test case for Claim
def test_claim_status(driver):
    driver.get(Data.url)
    loginpage = LoginPage(driver)
    claim_page = ClaimPage(driver)
    loginpage.enter_username(Data.username)
    loginpage.enter_password(Data.password)
    loginpage.click_login()
    sleep(5)
    claim_page.claim_click()
    claim_page.assign_claim()
    claim_page.add_employee(Data.employee)
    claim_page.name_select()
    claim_page.event_claim()
    claim_page.currency_select()
    claim_page.claim_button()
    sleep(5)
    claim_page.submit_claim()
    sleep(10)
    claim_page.my_claim()

    #Test Case for checking User Received Claim
    assert claim_page.claim_validation() == True
    print("Success: Test Case Passed for Submitting Claim")


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test case for Create User
def test_create_user(driver):
    driver.get(Data.url)
    loginpage = LoginPage(driver)
    userpage = UserPage(driver)
    claim_page = ClaimPage(driver)
    basepage = BasePage(driver)
    loginpage.enter_username(Data.username)
    loginpage.enter_password(Data.password)
    loginpage.click_login()
    sleep(5)
    userpage.click_admin()
    userpage.click_add()
    userpage.add_employee(Data.employee)
    claim_page.name_select()
    userpage.add_user_role()
    userpage.add_status()
    userpage.add_username(Data.Username)
    userpage.add_password(Data.Password)
    userpage.add_confirm_password(Data.C_Password)
    userpage.admin_save()
    sleep(3)
    loginpage.click_dropdown()
    loginpage.click_logout()
    sleep(3)
    loginpage.enter_username(Data.Username)
    loginpage.enter_password(Data.Password)
    loginpage.click_login()
    sleep(3)

    # asserting expected vs actual url
    assert basepage.fetch_url() == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    print("Success: Test Case Passed for Newly Create User")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test case for Checking User Present
def test_user_present(driver):
    driver.get(Data.url)
    loginpage = LoginPage(driver)
    userpage = UserPage(driver)
    loginpage.enter_username(Data.Username)
    loginpage.enter_password(Data.Password)
    loginpage.click_login()
    userpage.click_admin()

    # Check_User_Present
    assert userpage.admin_user_enabled() == True
    print("Success: Test Case Passed for User Present")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test case for Checking Leave
def test_leave(driver):
    driver.get(Data.url)
    loginpage = LoginPage(driver)
    leavepage = LeavePage(driver)
    claimpage = ClaimPage(driver)
    loginpage.enter_username(Data.username)
    loginpage.enter_password(Data.password)
    loginpage.click_login()
    sleep(5)
    leavepage.leave_click()
    sleep(5)
    leavepage.assign_leave()
    leavepage.add_employee(Data.employee)
    claimpage.name_select()
    leavepage.leave_type()
    leavepage.dates(Data.from_date)
    leavepage.click_leave()
    leavepage.ok_leave()
    leavepage.my_leave()

    # Asserting Leave
    assert leavepage.assert_leave() == True
    print("Success: Test Case Passed for Assigning Leave")





