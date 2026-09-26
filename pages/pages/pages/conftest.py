import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Браузер: chrome или firefox",
    )
    parser.addoption(
        "--url",
        action="store",
        default="https://practice-automation.com/iframes/",
        help="URL для тестирования",
    )


@pytest.fixture(scope="function")
def driver(request):
    """Фикстура драйвера с мультибраузерностью и неявным ожиданием в ноль."""
    browser_name = request.config.getoption("--browser").lower()

    if browser_name == "chrome":
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Браузер '{browser_name}' не поддерживается")

    driver.maximize_window()
    driver.implicitly_wait(0)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def url(request):
    """Фикстура для получения URL."""
    return request.config.getoption("--url")
