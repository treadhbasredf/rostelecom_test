"""Page Object страницы авторизации."""
from pages.base_page import BasePage
from pages.locators import AuthLocators


class AuthPage(BasePage):
    """Методы для страницы авторизации."""

    def is_form_displayed(self):
        return self.is_displayed(AuthLocators.FORM_TITLE) and self.is_displayed(AuthLocators.USERNAME)

    def is_slogan_displayed(self):
        return self.is_displayed(AuthLocators.PRODUCT_TITLE)

    def is_tab_active(self, tab_locator):
        try:
            element = self.find_element(tab_locator, timeout=3)
            return "active" in (element.get_attribute("class") or "")
        except:
            return False

    def get_active_tab(self):
        tabs = [
            ("Телефон", AuthLocators.TAB_PHONE),
            ("Почта", AuthLocators.TAB_EMAIL),
            ("Логин", AuthLocators.TAB_LOGIN),
            ("Лицевой счёт", AuthLocators.TAB_LS),
        ]
        for name, locator in tabs:
            if self.is_tab_active(locator):
                return name
        return None

    def click_tab_phone(self):
        self.click(AuthLocators.TAB_PHONE)

    def click_tab_email(self):
        self.click(AuthLocators.TAB_EMAIL)

    def click_tab_login(self):
        self.click(AuthLocators.TAB_LOGIN)

    def click_tab_ls(self):
        self.click(AuthLocators.TAB_LS)

    def input_username(self, text):
        self.input_text(AuthLocators.USERNAME, text)

    def input_password(self, text):
        self.input_text(AuthLocators.PASSWORD, text)

    def click_login(self):
        self.click(AuthLocators.BTN_LOGIN)

    def click_forgot_password(self):
        self.click(AuthLocators.FORGOT_PASSWORD_LINK)

    def click_register(self):
        self.click(AuthLocators.REGISTRATION_LINK)

    def get_error_invalid_data(self):
        if self.is_displayed(AuthLocators.ERROR_INVALID_DATA, timeout=2):
            return self.get_text(AuthLocators.ERROR_INVALID_DATA)
        return ""

    def get_error_message(self):
        if self.is_displayed(AuthLocators.ERROR_MESSAGE, timeout=2):
            return self.get_text(AuthLocators.ERROR_MESSAGE)
        return ""

    def is_forgot_password_orange(self):
        try:
            element = self.find_element(AuthLocators.FORGOT_PASSWORD_LINK, timeout=2)
            return "orange" in (element.get_attribute("class") or "")
        except:
            return False