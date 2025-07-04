"""
This file contains all the different locators
"""

class OrangeHRMLocators:
    username_locator = 'username' #Name
    password_locator = 'password' #Name
    login_button_locator = '//div[@class="oxd-form-actions orangehrm-login-action"]/button' #XPATH
    drop_down_selector = '//i[@class="oxd-icon bi-caret-down-fill oxd-userdropdown-icon"]' #XPATH
    logout = '//a[contains(text(),"Logout")]' #XPATH
    # Validate Menu Preseent
    admin = '//a [@href = "/web/index.php/admin/viewAdminModule"]' #XPATH
    pim = '//a [@href = "/web/index.php/pim/viewPimModule"]' #XPATH
    leave = '//a [@href = "/web/index.php/leave/viewLeaveModule"]' #XPATH
    time = '//a [@href = "/web/index.php/time/viewTimeModule"]' #XPATH
    recruitment = '//a [@href = "/web/index.php/recruitment/viewRecruitmentModule"]' #XPATH
    my_info = '//a [@href = "/web/index.php/pim/viewMyDetails"]' #XPATH
    performance = '//a [@href = "/web/index.php/performance/viewPerformanceModule"]' #XPATH
    dashboard = '//a [@href = "/web/index.php/dashboard/index"]' #XPATH
    # Add New User
    add_admin = '//button[@class = "oxd-button oxd-button--medium oxd-button--secondary"]' #XPATH
    admin_user = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]' #XPATH
    admin_user_role = '//div[@role="listbox"]//span[text()="Admin"]'#XPATH'
    admin_employee = '//input[@placeholder="Type for hints..."]' #XPATH
    admin_status = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]' #XPATH
    admin_status_role = '//div[@role="listbox"]//span[contains(text(),"Enabled")]' #XPATH
    admin_username = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input' #XPATH
    admin_password = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input' #XPATH
    admin_cf_password = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input' #XPATH
    admin_save = '//button[@class = "oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]' #XPATH
    admin_present = '//div[contains(text(),"Admin123")]' #XPATH
    #FORGOT PASSWORD
    forgot_password = '//p[@class = "oxd-text oxd-text--p orangehrm-login-forgot-header"]' #XPATH
    reset_password = '//button[@class = "oxd-button oxd-button--large oxd-button--secondary orangehrm-forgot-password-button orangehrm-forgot-password-button--reset"]' #XPATH
    conf_message = '//h6[@class = "oxd-text oxd-text--h6 orangehrm-forgot-password-title"]' #XPATH
    # MENU MY_INFO
    personal_details = '//a[contains(text(),"Personal Details")]' #XPATH
    contact_details = '//a[contains(text(),"Contact Details")]' #XPATH
    emergency_contacts = '//a[contains(text(),"Emergency Contacts")]' #XPATH
    #ASSIGN LEAVE
    assign_leave = '//a[text() = "Assign Leave"]' #XPATH
    leave_type = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/div[1]' #XPATH
    person_leave = '//div[@role="listbox"]//span[text()="CAN - Personal"]' #XPATH
    from_date = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div/input' #XPATH
    to_date = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/input' #XPATH
    click_leave = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[6]/button' #CLASS
    ok_leave = '//button[@class = "oxd-button oxd-button--medium oxd-button--secondary orangehrm-button-margin"]' #XPATH
    my_leave = '//a[text() = "My Leave"]' #XPATH
    leave_select = '//div[contains(text(), "CAN - Personal")]' #XPATH
    #CLAIM
    claim = '//a [@href = "/web/index.php/claim/viewClaimModule"]' #XPATH
    assign_claim = '//button[@class ="oxd-button oxd-button--medium oxd-button--secondary"]' #XPATH
    name_select = '//div[@role="listbox"]//span[text()="Ranga  Akunuri"]'
    event_select = '(//div[@class= "oxd-select-text-input" and contains(text(),"-- Select --")])[1]' #XPATH
    event_select1 = '//div[@role="listbox"]//span[text()="Accommodation"]'#XPATH
    currency_select = '//div[contains(text(),"-- Select --")]'#XPATH
    currency_select1 = '//div[@role="listbox"]//span[text()="Aruban Florin"]'#XPATH
    create_claim = '//button[@class = "oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'#XPATH
    submit = '//button[@class = "oxd-button oxd-button--medium oxd-button--secondary orangehrm-sm-button"]' #XPATH
    claim_present = '//div[contains(text(),"Aruban Florin")]' #XPATH
    emp_claim = '//a[contains(text(),"Employee Claims")]' #XPATH










