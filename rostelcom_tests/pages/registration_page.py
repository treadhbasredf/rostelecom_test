"""Page Object страницы регистрации."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import RegistrationLocators


class RegistrationPage(BasePage):
    """Методы для страницы регистрации."""

    def input_first_name(self, name):
        self.input_text(RegistrationLocators.INPUT_FIRST_NAME, name)

    def input_last_name(self, surname):
        self.input_text(RegistrationLocators.INPUT_LAST_NAME, surname)

    def input_email_or_phone(self, value):
        self.input_text(RegistrationLocators.INPUT_EMAIL_PHONE, value)

    def input_password(self, password):
        self.input_text(RegistrationLocators.INPUT_PASSWORD, password)

    def input_password_confirm(self, password):
        self.input_text(RegistrationLocators.INPUT_PASSWORD_CONFIRM, password)

    def click_continue(self):
        self.click(RegistrationLocators.BTN_CONTINUE)

    def click_register_in_modal(self):
        if self.is_displayed(RegistrationLocators.BTN_REGISTER_IN_MODAL, timeout=2):
            self.click(RegistrationLocators.BTN_REGISTER_IN_MODAL)

    def is_code_form_displayed(self):
        return self.is_displayed(RegistrationLocators.CODE_FIELDS)

    def is_modal_displayed(self):
        return self.is_displayed(RegistrationLocators.MODAL)

    def get_field_error(self):
        if self.is_displayed(RegistrationLocators.ERROR_FIELD, timeout=1):
            return self.get_text(RegistrationLocators.ERROR_FIELD)
        return ""