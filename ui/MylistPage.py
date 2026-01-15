import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage
import allure


class MylistPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._driver.implicitly_wait(4)

    @allure.step("Удалить контент из 'Избранного'")
    def remove_from_mylist(self) -> None:
        """
        Удаляет первый элемент из списка избранного
        """

        with allure.step("Обновить страницу для актуальных данных"):
            self._driver.refresh()
            time.sleep(15)
            self._driver.refresh()

        with allure.step("Выбрать первый контент в списке"):
            first_content = WebDriverWait(self._driver, 15).until(
                EC.element_to_be_clickable((
                    By.CSS_SELECTOR,
                    "ul[role='list'] li:first-child a"
                ))
            )
            self.human_click(first_content)

        with allure.step("Найти кнопку 'Избранное' для удаления"):
            bookmark_button = WebDriverWait(self._driver, 5).until(
                EC.element_to_be_clickable((
                    By.CSS_SELECTOR,
                    "button[data-test-id='ContentActions_bookmarkButton']"
                ))
            )

            allure.attach(self._driver.get_screenshot_as_png(),
                          name="before_remove_bookmark",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Нажать кнопку 'Избранное' для удаления"):
            self.human_click(bookmark_button, "Кнопка 'Избранное' (удаление)")

            allure.attach(self._driver.get_screenshot_as_png(),
                          name="after_remove_bookmark",
                          attachment_type=allure.attachment_type.PNG)
