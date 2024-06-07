import allure
from page_object_model.login_page import LoginPage
from page_object_model.login_success_page import LoginSuccessPage


@allure.epic("User Authentication")
@allure.feature("Login Scenarios")
class TestPositiveScenarios:

    @allure.title("TC-01 - Positive Login Test")
    @allure.description("Test logging in with valid credentials and verifying successful login.")
    @allure.tag("smoke", "regression")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Sai Kiran")
    @allure.link("https://practicetestautomation.com/practice-test-login/", name="Login Page")
    @allure.story("As a user, I want to log in with valid credentials and see the success page.")
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "Password123")

        login_success_page = LoginSuccessPage(driver)
        try:
            assert login_success_page.current_url == login_success_page.expected_url, "Actual URL is not the same as expected"
            assert login_success_page.header == "Logged In Successfully", "Header is not expected"
            assert login_success_page.is_logout_button_displayed, "Logout button should be visible"
            allure.attach(driver.get_screenshot_as_png(), name="Login Success",
                          attachment_type=allure.attachment_type.PNG)
        except AssertionError as e:
            allure.attach(driver.get_screenshot_as_png(), name="Login Failure",
                          attachment_type=allure.attachment_type.PNG)
            raise e

    @allure.title("TC-02 - Negative Login Test with Incorrect Username")
    @allure.description("Test logging in with an incorrect username and verifying the error message.")
    @allure.tag("smoke", "regression")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Sai Kiran")
    @allure.link("https://practicetestautomation.com/practice-test-login/", name="Login Page")
    @allure.story("As a user, I want to see an error message when I log in with an incorrect username.")
    def test_negative_login_username(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("incorrectUser", "Password123")

        try:
            assert login_page.error_msg_is_displayed, "Error msg should be displayed"
            assert login_page.error_msg() == "Your username is invalid!", "Error msg not displayed"
            allure.attach(driver.get_screenshot_as_png(), name="Login Error Message Displayed",
                          attachment_type=allure.attachment_type.PNG)
        except AssertionError as e:
            allure.attach(driver.get_screenshot_as_png(), name="Login Error Message Not Displayed",
                          attachment_type=allure.attachment_type.PNG)
            raise e

    @allure.title("TC-03 - Negative Login Test with Incorrect Password")
    @allure.description("Test logging in with an incorrect password and verifying the error message.")
    @allure.tag("smoke", "regression")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Sai Kiran")
    @allure.link("https://practicetestautomation.com/practice-test-login/", name="Login Page")
    @allure.story("As a user, I want to see an error message when I log in with an incorrect password.")
    def test_negative_login_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "incorrectPassword")

        try:
            assert login_page.error_msg_is_displayed, "Error msg should be displayed"
            assert login_page.error_msg() == "Your password is invalid!", "Error msg not displayed"
            allure.attach(driver.get_screenshot_as_png(), name="Login Error Message Displayed",
                          attachment_type=allure.attachment_type.PNG)
        except AssertionError as e:
            allure.attach(driver.get_screenshot_as_png(), name="Login Error Message Not Displayed",
                          attachment_type=allure.attachment_type.PNG)
            raise e
