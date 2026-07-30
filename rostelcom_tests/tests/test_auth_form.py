"""TC-01 – TC-07: Форма авторизации."""
import pytest
from pages.auth_page import AuthPage
import config


class TestAuthFormDisplay:
    """Отображение и навигация по табам."""

    @pytest.mark.auth
    def test_form_displayed_and_defaults(self, driver):
        """TC-01: Форма, слоган, таб по умолчанию."""
        page = AuthPage(driver)
        assert page.is_form_displayed()
        assert page.is_slogan_displayed()
        assert page.get_active_tab() == "Телефон"

    @pytest.mark.auth
    def test_switch_to_email_tab(self, driver):
        """TC-02: Переключение на «Почта»."""
        page = AuthPage(driver)
        page.click_tab_email()
        assert page.get_active_tab() == "Почта"

    @pytest.mark.auth
    def test_switch_to_login_tab(self, driver):
        """TC-03: Переключение на «Логин»."""
        page = AuthPage(driver)
        page.click_tab_login()
        assert page.get_active_tab() == "Логин"

    @pytest.mark.auth
    def test_switch_to_ls_tab(self, driver):
        """TC-04: Переключение на «Лицевой счёт»."""
        page = AuthPage(driver)
        page.click_tab_ls()
        assert page.get_active_tab() == "Лицевой счёт"


class TestAuthNegative:
    """Негативные сценарии авторизации."""

    @pytest.mark.auth
    def test_empty_fields(self, driver):
        """TC-05: Пустые поля."""
        page = AuthPage(driver)
        page.click_login()
        error = page.get_error_invalid_data() or page.get_error_message()
        assert error, "Нет сообщения об ошибке"

    @pytest.mark.auth
    def test_invalid_credentials(self, driver):
        """TC-06: Неверная связка логин+пароль."""
        page = AuthPage(driver)
        page.click_tab_login()
        page.input_username(config.INVALID_LOGIN)
        page.input_password(config.INVALID_PASSWORD)
        page.click_login()
        error = page.get_error_invalid_data()
        assert error, "Нет сообщения об ошибке"
        assert any(text in error for text in [
            "Неверный логин или пароль",
            "Неверно введен текст с картинки",
        ]), f"Неожиданное сообщение: {error}"
        if "Неверный логин или пароль" in error:
            assert page.is_forgot_password_orange(), "Ссылка не стала оранжевой"

    @pytest.mark.auth
    def test_short_phone(self, driver):
        """TC-07: Короткий номер телефона."""
        page = AuthPage(driver)
        page.input_username(config.INVALID_PHONE_SHORT)
        page.input_password(config.INVALID_PASSWORD)
        page.click_login()
        error = page.get_error_invalid_data() or page.get_error_message()
        assert error, "Нет сообщения об ошибке"