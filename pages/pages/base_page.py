from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Низкоуровневое взаимодействие с элементами страницы."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, locator):
        """Найти элемент с явным ожиданием видимости."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        """Найти кликабельный элемент."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        """Кликнуть по элементу."""
        self.find_clickable(locator).click()

    def get_attribute(self, locator, attribute):
        """Получить атрибут элемента."""
        return self.find_element(locator).get_attribute(attribute)

    def get_text(self, locator):
        """Получить текст элемента."""
        return self.find_element(locator).text
