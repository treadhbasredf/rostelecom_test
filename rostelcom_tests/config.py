"""Конфигурация для тестов."""
import os

BASE_URL = "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth"
AUTH_PARAMS = ("?client_id=account_b2c"
               "&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login"
               "&response_type=code&scope=openid")

IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 15

VALID_PHONE = "+7 999 123 45 67"
VALID_EMAIL = "test.user@example.com"
VALID_LOGIN = "test_user123"
VALID_LS = "123456789012"

INVALID_PHONE_SHORT = "12345"
INVALID_LOGIN = "nosuchuser"
INVALID_PASSWORD = "Test1234"

VALID_NAME = "Иван"
VALID_SURNAME = "Иванов"
SHORT_NAME = "И"
LATIN_NAME = "Ivan"

NEW_VALID_PASS = "NewPass1"
NEW_SHORT_PASS = "Pass1"
NEW_NO_UPPER_PASS = "password1"
NEW_CYRILLIC_PASS = "Пароль12"

INVALID_CODE = "111111"

REPORT_DIR = os.path.join(os.path.dirname(__file__), "reports")