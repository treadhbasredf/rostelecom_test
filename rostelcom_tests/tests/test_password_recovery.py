"""TC-13 – TC-18: Восстановление пароля."""
import pytest
import time
from pages.auth_page import AuthPage
from pages.locators import RecoveryLocators
import config


class TestRecovery:
    """Восстановление пароля."""

    @pytest.mark.recovery
    def test_recovery_form_displayed(self, driver):
        """TC-13: Отображение формы восстановления."""
        page = AuthPage(driver)
        page.click_forgot_password()
        assert page.is_displayed(RecoveryLocators.BTN_NEXT, timeout=5)
        assert page.is_displayed(RecoveryLocators.BTN_BACK, timeout=2)

    @pytest.mark.recovery
    def test_sms_option_available(self, driver):
        """TC-14: Опция восстановления по SMS."""
        page = AuthPage(driver)
        page.click_forgot_password()
        page.input_text(RecoveryLocators.USERNAME, config.VALID_PHONE)
        time.sleep(1)
        page.click(RecoveryLocators.BTN_NEXT)
        time.sleep(2)
        assert page.is_displayed(RecoveryLocators.OPTION_SMS, timeout=5) or \
               "reset" in driver.current_url.lower()

    @pytest.mark.recovery
    def test_password_mismatch(self, driver):
        """TC-15: Пароли не совпадают (требует капчу)."""
        pytest.skip("Валидация пароля требует капчу и код подтверждения")

    @pytest.mark.recovery
    def test_password_too_short(self, driver):
        """TC-16: Пароль короче 8 символов (требует капчу)."""
        pytest.skip("Валидация пароля требует капчу и код подтверждения")

    @pytest.mark.recovery
    def test_password_no_uppercase(self, driver):
        """TC-17: Пароль без заглавной буквы (требует капчу)."""
        pytest.skip("Валидация пароля требует капчу и код подтверждения")

    @pytest.mark.recovery
    def test_password_cyrillic(self, driver):
        """TC-18: Пароль с кириллицей (требует капчу)."""
        pytest.skip("Валидация пароля требует капчу и код подтверждения")