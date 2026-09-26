from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SecondFrame:
    """Второй iframe, инкапсулированный в MainPage."""

    def __init__(self, driver):
        self.driver = driver

    def switch_to_frame(self):
        """Переключиться во второй iframe (индекс 1)."""
        self.driver.switch_to.frame(1)

    def get_python_download_link(self):
        """Получить href ссылки на скачивание Python."""
        link = self.driver.find_element(
            By.XPATH, "//a[contains(text(), 'Python') or contains(@href, 'python.org')]"
        )
        return link.get_attribute("href")

    def switch_to_default(self):
        """Вернуться в основной документ."""
        self.driver.switch_to.default_content()


class MainPage(BasePage):
    """Главная страница с iframes."""

    def __init__(self, driver):
        super().__init__(driver)
        self.second_frame = SecondFrame(driver)

    def open(self, url):
        self.driver.get(url)

    def get_second_frame(self):
        return self.second_frame
