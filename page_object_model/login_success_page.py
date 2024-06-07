from selenium.webdriver.remote.webdriver import WebDriver
from page_object_model.Locators.locators import Locators
from page_object_model.base_page import BasePage


class LoginSuccessPage(BasePage, Locators):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)


    @property
    def expected_url(self) -> str:
        return self._url2

    @property
    def header(self) -> str:
        return super()._get_text(self._header_locator)

    @property
    def is_logout_button_displayed(self) -> bool:
        return super()._is_displayed(self._logout_button_locator)






