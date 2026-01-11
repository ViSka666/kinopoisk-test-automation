from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage
import allure
import time


class AuthorizationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver

        with allure.step("Открыть главную страницу Кинопоиска"):
            self._driver.get("https://hd.kinopoisk.ru/")
            self._driver.implicitly_wait(4)
            self._driver.maximize_window()

    @allure.step("Авторизация через QR-код")
    def login_account(self) -> None:
        """
        Выполняет процесс авторизации через QR-код
        Требует ручного сканирования QR-кода в мобильном приложении Яндекс
        """

        try:
            with allure.step("Закрыть начальный попап"):
                try:
                    close_button = WebDriverWait(self._driver, 60).until(
                        EC.element_to_be_clickable((
                            By.CSS_SELECTOR,
                            "button[data-tid='CloseButton']"
                        ))
                    )
                    self.human_click(close_button, "Закрыть начальный попап")
                except Exception as e:
                    allure.attach(f"Не удалось найти попап: {str(e)}",
                                  name="popup_warning",
                                  attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            allure.attach(f"Ошибка в шаге закрытия попапа: {str(e)}",
                          name="step_error",
                          attachment_type=allure.attachment_type.TEXT)

        with allure.step("Нажать кнопку 'Войти'"):
            login_link = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR,
                    "a.LoginLink_root__bvmul[data-test-id='link_a']"
                ))
            )
            self.human_click(login_link, "Кнопка 'Войти'")

        with allure.step("Выбрать авторизацию через QR-код"):
            qr_button = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR,
                    "button[data-testid='magic-btn']"
                ))
            )
            self.human_click(qr_button, "Кнопка 'QR-код'")

        try:
            with allure.step("Нажать 'Напомнить позже' для пропуска дополнительной защиты"):
                later_button = WebDriverWait(self._driver, 30).until(
                    EC.element_to_be_clickable((
                        By.CSS_SELECTOR,
                        "button[data-testid='webauthn-reg-later-button']"
                    ))
                )
                self.human_click(later_button, "Кнопка 'Напомнить позже'")
        except Exception as e:
            allure.attach(f"Ошибка при поиске кнопки 'Напомнить позже': {str(e)}",
                          name="later_button_error",
                          attachment_type=allure.attachment_type.TEXT)

        with allure.step("Выбрать профиль пользователя"):
            time.sleep(5)
            allure.attach("ТРЕБУЕТСЯ РУЧНОЕ ДЕЙСТВИЕ: Отсканируйте QR-код в приложении Яндекс",
                          name="manual_action_required",
                          attachment_type=allure.attachment_type.TEXT)

            account = WebDriverWait(self._driver, 60).until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR,
                    "ul[data-tid='ProfilesFamilyVerticalList'] li:first-child a"
                ))
            )
            self.human_click(account)
