from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._driver.implicitly_wait(4)

    @allure.step("Перейти в раздел 'Моё'")
    def click_mylist(self) -> None:
        """
        Открывает раздел с избранным контентом пользователя
        """

        with allure.step("Найти и нажать кнопку 'Моё'"):
            mylist = self._driver.find_element(By.ID, "personal")
            self.human_click(mylist, "Кнопка 'Моё'")

            allure.attach(self._driver.get_screenshot_as_png(),
                          name="mylist_page",
                          attachment_type=allure.attachment_type.PNG)

    @allure.step("Поиск контента по запросу '{word}'")
    def click_search(self, word: str) -> None:
        """
        Выполняет поиск контента по ключевому слову

        Args:
            word: Ключевое слово для поиска
        """

        with allure.step("Открыть поле поиска"):
            search = self._driver.find_element(
                By.CSS_SELECTOR,
                "button[data-tid='SearchButton']"
            )
            search.click()

        with allure.step(f"Ввести поисковый запрос '{word}'"):
            input_word = self._driver.find_element(
                By.CSS_SELECTOR, "input[type='search']"
            )
            input_word.send_keys(word)

        with allure.step("Дождаться результатов поиска"):
            self.wait.until(EC.presence_of_element_located((
                By.CLASS_NAME, "styles_content__TwwjO"
            )))

        with allure.step("Выбрать первый результат из списка"):
            first_content_link = self._driver.find_element(
                By.CSS_SELECTOR,
                "ul[role='list'] li:first-child a"
            )
            self.human_click(first_content_link)

            allure.attach(self._driver.get_screenshot_as_png(),
                          name=f"search_results_{word}",
                          attachment_type=allure.attachment_type.PNG)

    @allure.step("Перейти в раздел 'Каналы'")
    def click_channels(self) -> None:
        """
        Открывает раздел телеканалов
        """

        with allure.step("Прокрутить страницу в начало"):
            self._driver.execute_script("window.scrollTo(0, 0);")

        with allure.step("Найти ссылку на раздел 'Каналы'"):
            channels = self.wait.until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//a[contains(@class, 'NavLink_link') and text()='Каналы']"
                ))
            )

        with allure.step("Прокрутить к элементу и нажать"):
            self._driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
                channels
            )
            channels.click()

            allure.attach(self._driver.get_screenshot_as_png(),
                          name="channels_page",
                          attachment_type=allure.attachment_type.PNG)
