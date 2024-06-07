from selenium.webdriver.remote.webdriver import WebDriver

from page_object_model.Locators.locators import Locators
from page_object_model.base_page import BasePage


class LoginPage(BasePage, Locators):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        """  
        This will allow us to use private and public variables of BaseClass
        """

    def open(self):
        super()._open_url(self._url1)

    def execute_login(self, username: str, password: str):
        super()._type(self._user_name, username)
        super()._type(self._password, password)
        super()._click(self._submit_button)

    def error_msg(self):
        return super()._get_text(self._error_msg, 3)

    @property
    def error_msg_is_displayed(self) -> bool:
        return super()._is_displayed(self._error_msg)


