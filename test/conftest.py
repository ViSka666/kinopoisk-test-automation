import pytest
from selenium import webdriver
import allure


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для создания скриншотов при падении тестов"""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            if "browser" in item.fixturenames:
                driver = item.funcargs["browser"]
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception as e:
            allure.attach(
                f"Не удалось сделать скриншот: {str(e)}",
                name="screenshot_error",
                attachment_type=allure.attachment_type.TEXT
            )


@pytest.fixture(scope="session")
def browser():
    """
    Фикстура для браузера - создается автоматически для UI тестов
    Выполняет авторизацию через QR-код
    """

    with allure.step("Инициализировать Chrome драйвер"):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        allure.attach(
            "Chrome драйвер инициализирован",
            name="browser_init",
            attachment_type=allure.attachment_type.TEXT
        )

    try:
        with allure.step("Выполнить авторизацию через QR-код"):
            from ui.AuthorizationPage import AuthorizationPage
            login_page = AuthorizationPage(driver)
            login_page.login_account()
    except Exception as e:
        allure.attach(
            f"Ошибка авторизации: {str(e)}",
            name="auth_error",
            attachment_type=allure.attachment_type.TEXT
        )
        driver.quit()
        raise

    yield driver

    with allure.step("Закрыть браузер"):
        driver.quit()
        allure.attach(
            "Браузер закрыт",
            name="browser_quit",
            attachment_type=allure.attachment_type.TEXT
        )
