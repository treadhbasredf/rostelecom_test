"""TC-19 – TC-22: Регистрация."""
import pytest
from pages.auth_page import AuthPage
from pages.registration_page import RegistrationPage
import config


class TestRegistration:
    """Регистрация нового пользователя."""

    @pytest.mark.reg
    def test_valid_registration_to_code(self, driver):
        """TC-19: Успешная регистрация до подтверждения."""
        page = AuthPage(driver)
        page.click_register()
        reg = RegistrationPage(driver)
        reg.input_first_name(config.VALID_NAME)
        reg.input_last_name(config.VALID_SURNAME)
        reg.input_email_or_phone(config.VALID_EMAIL)
        reg.input_password(config.NEW_VALID_PASS)
        reg.input_password_confirm(config.NEW_VALID_PASS)
        reg.click_continue()
        if reg.is_modal_displayed():
            reg.click_register_in_modal()
        url_lower = driver.current_url.lower()
        assert reg.is_code_form_displayed() or \
               "registration" in url_lower or \
               "confirm" in url_lower, \
            f"Не перешли на форму подтверждения. URL: {driver.current_url}"

    @pytest.mark.reg
    def test_short_name(self, driver):
        """TC-20: Имя короче 2 символов."""
        page = AuthPage(driver)
        page.click_register()
        reg = RegistrationPage(driver)
        reg.input_first_name(config.SHORT_NAME)
        reg.input_last_name(config.VALID_SURNAME)
        reg.input_email_or_phone(config.VALID_EMAIL)
        reg.input_password(config.NEW_VALID_PASS)
        reg.input_password_confirm(config.NEW_VALID_PASS)
        reg.click_continue()
        error = reg.get_field_error()
        assert error, f"Нет ошибки валидации имени. Ошибка: {error}"

    @pytest.mark.reg
    def test_latin_name(self, driver):
        """TC-21: Латиница в имени."""
        page = AuthPage(driver)
        page.click_register()
        reg = RegistrationPage(driver)
        reg.input_first_name(config.LATIN_NAME)
        reg.input_last_name(config.VALID_SURNAME)
        reg.input_email_or_phone(config.VALID_EMAIL)
        reg.input_password(config.NEW_VALID_PASS)
        reg.input_password_confirm(config.NEW_VALID_PASS)
        reg.click_continue()
        error = reg.get_field_error()
        assert error, f"Нет ошибки валидации имени. Ошибка: {error}"

    @pytest.mark.reg
    def test_existing_email(self, driver):
        """TC-22: Существующий email."""
        page = AuthPage(driver)
        page.click_register()
        reg = RegistrationPage(driver)
        reg.input_first_name(config.VALID_NAME)
        reg.input_last_name(config.VALID_SURNAME)
        reg.input_email_or_phone("support@rt.ru")
        reg.input_password(config.NEW_VALID_PASS)
        reg.input_password_confirm(config.NEW_VALID_PASS)
        reg.click_continue()
        assert reg.is_modal_displayed(), "Модальное окно не появилось"