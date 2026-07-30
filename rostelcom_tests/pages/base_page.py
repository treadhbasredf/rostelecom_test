"""Базовый класс Page Object."""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import config


class BasePage:
    """Базовые методы для всех страниц."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.EXPLICIT_WAIT)

    def find_element(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout or config.EXPLICIT_WAIT)
        return wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        try:
            self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            pass
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_displayed(self, locator, timeout=2):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def get_current_url(self):
        return self.driver.current_url