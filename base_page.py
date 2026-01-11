import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Имитация человеческой задержки")
    def human_delay(self, min_seconds: float = 0.5, max_seconds: float = 2.0) -> None:
        """
        Создает случайную задержку для имитации человеческого поведения

        Args:
            min_seconds: Минимальное время задержки
            max_seconds: Максимальное время задержки
        """
        delay = random.uniform(min_seconds, max_seconds)
        allure.attach(f"Задержка: {delay:.1f} секунд",
                      name="delay_info",
                      attachment_type=allure.attachment_type.TEXT)
        time.sleep(delay)

    @allure.step("Имитировать человеческий клик")
    def human_click(self, element, description: str = "") -> None:
        """
        Выполняет клик по элементу с имитацией человеческого поведения

        Args:
            element: WebElement для клика
            description: Описание элемента для отладки
        """
        if description:
            allure.attach(f"Кликаем: {description}",
                          name="click_action",
                          attachment_type=allure.attachment_type.TEXT)

        self.human_delay(0.3, 0.8)
        element.click()
        self.human_delay(0.2, 0.5)

    @allure.step("Ожидание элемента")
    def wait_for_element(self, by, selector: str, timeout: int = 10):
        """
        Ожидает появление элемента на странице

        Args:
            by: Метод поиска (By.ID, By.CSS_SELECTOR и т.д.)
            selector: Селектор элемента
            timeout: Максимальное время ожидания в секундах

        Returns:
            Найденный WebElement
        """
        allure.attach(f"Селектор: {selector}, timeout: {timeout} сек",
                      name="wait_params",
                      attachment_type=allure.attachment_type.TEXT)

        self.human_delay(0.5, 1.0)
        return WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located((by, selector))
        )
