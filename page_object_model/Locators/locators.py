from selenium.webdriver.common.by import By


class Locators:

    # Login Page Locators
    _url1 = "https://practicetestautomation.com/practice-test-login/"
    _user_name = (By.ID, "username")
    _password = (By.ID, "password")
    _submit_button = (By.XPATH, "//button[@class='btn']")
    _error_msg = (By.XPATH, "//div[@class='show']")

    # Login Success Page Locators

    _url2 = "https://practicetestautomation.com/logged-in-successfully/"
    _header_locator = (By.XPATH, "//h1[@class='post-title']")
    _logout_button_locator = (By.LINK_TEXT, "Log out")

