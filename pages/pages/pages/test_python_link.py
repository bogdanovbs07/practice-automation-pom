from pages.main_page import MainPage


def test_python_download_link(driver, url):
    """Проверяем, что во втором iframe найдена правильная ссылка на Python."""
    main_page = MainPage(driver)
    main_page.open(url)

    second_frame = main_page.get_second_frame()
    second_frame.switch_to_frame()

    python_link = second_frame.get_python_download_link()

    second_frame.switch_to_default()

    assert python_link is not None, "Ссылка на Python не найдена"
    assert "python.org" in python_link, \
        f"Ожидалась ссылка на python.org, получено: {python_link}"
