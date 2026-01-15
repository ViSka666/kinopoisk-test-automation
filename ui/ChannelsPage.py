from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base_page import BasePage
import allure


class ChannelsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._driver.implicitly_wait(4)

    @allure.step("Выбрать телеканал '{channel_name}'")
    def click_tv_channel(self, channel_name: str) -> None:
        """
        Выбирает телеканал по названию

        Args:
            channel_name: Название телеканала для выбора
        """

        with allure.step("Дождаться загрузки списка каналов"):
            wait = WebDriverWait(self._driver, 10)
            wait.until(EC.presence_of_element_located((
                By.CLASS_NAME, "styles_collection__72EdU"
            )))

        with allure.step(f"Найти и нажать на канал '{channel_name}'"):
            tv_channel_button = WebDriverWait(self._driver, 5).until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    f"//button[@title='{channel_name}']"
                ))
            )

            actions = ActionChains(self._driver)
            actions.move_to_element(tv_channel_button).pause(0.5).click().perform()

            allure.attach(self._driver.get_screenshot_as_png(),
                          name=f"channel_{channel_name.replace(' ', '_')}",
                          attachment_type=allure.attachment_type.PNG)
