"""Все локаторы страниц."""
from selenium.webdriver.common.by import By


class AuthLocators:
    """Локаторы страницы авторизации."""
    FORM_TITLE = (By.CLASS_NAME, 'card-container__title')
    PRODUCT_TITLE = (By.CLASS_NAME, 'what-is__title')
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    BTN_LOGIN = (By.ID, 'kc-login')
    FORGOT_PASSWORD_LINK = (By.ID, 'forgot_password')
    REGISTRATION_LINK = (By.ID, 'kc-register')
    TAB_PHONE = (By.ID, 't-btn-tab-phone')
    TAB_EMAIL = (By.ID, 't-btn-tab-mail')
    TAB_LOGIN = (By.ID, 't-btn-tab-login')
    TAB_LS = (By.ID, 't-btn-tab-ls')
    ERROR_INVALID_DATA = (By.XPATH, '//*[@id="form-error-message"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.rt-input-container__meta--error')


class RecoveryLocators:
    """Локаторы страницы восстановления пароля."""
    USERNAME = (By.ID, 'username')
    BTN_NEXT = (By.ID, 'reset')
    BTN_BACK = (By.ID, 'reset-back')
    OPTION_SMS = (By.XPATH, '//*[contains(text(), "SMS") or contains(text(), "смс")]')


class RegistrationLocators:
    """Локаторы страницы регистрации."""
    INPUT_FIRST_NAME = (By.NAME, 'firstName')
    INPUT_LAST_NAME = (By.NAME, 'lastName')
    INPUT_EMAIL_PHONE = (By.ID, 'address')
    INPUT_PASSWORD = (By.ID, 'password')
    INPUT_PASSWORD_CONFIRM = (By.ID, 'password-confirm')
    BTN_CONTINUE = (By.XPATH, '//button[contains(text(), "Продолжить")] | //button[@type="submit"]')
    BTN_REGISTER_IN_MODAL = (By.XPATH, '//button[contains(text(), "Зарегистрироваться")]')
    ERROR_FIELD = (By.CSS_SELECTOR, '.rt-input-container__meta--error')
    MODAL = (By.XPATH, '//div[contains(@class, "modal")]')
    CODE_FIELDS = (By.XPATH, '//div[contains(@class, "code-input")]//input')