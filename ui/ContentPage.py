from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage
import allure


class ContentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._driver.implicitly_wait(4)

    @allure.step("Добавить контент в 'Избранное'")
    def click_bookmark(self) -> None:
        """
        Добавляет текущий контент в список избранного
        """

        with allure.step("Найти кнопку 'Избранное' на странице контента"):
            bookmark_button = WebDriverWait(self._driver, 5).until(
                EC.element_to_be_clickable((
                    By.CSS_SELECTOR,
                    "button[data-test-id='ContentActions_bookmarkButton']"
                ))
            )

            allure.attach(self._driver.get_screenshot_as_png(),
                          name="before_bookmark",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Нажать кнопку 'Избранное'"):
            self.human_click(bookmark_button, "Кнопка 'Избранное'")

            allure.attach(self._driver.get_screenshot_as_png(),
                          name="after_bookmark",
                          attachment_type=allure.attachment_type.PNG)
