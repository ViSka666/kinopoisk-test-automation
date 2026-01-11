import sys
import os
import pytest
import allure

from ui.MainPage import MainPage
from ui.ContentPage import ContentPage
from ui.MylistPage import MylistPage
from ui.ChannelsPage import ChannelsPage

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@allure.epic("UI Тестирование")
@allure.feature("Функциональность Кинопоиск HD")
@allure.story("Основные пользовательские сценарии")
class TestKinopoiskUI:

    @allure.id("UI-1")
    @allure.title("Проверка успешной авторизации")
    @allure.description("""
    Авторизация выполняется через QR-код.
    Требуется ручное сканирование QR-кода в мобильном приложении Яндекс.
    """)
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("auth", "qr_code")
    @pytest.mark.ui
    def test_login(self, browser):
        """Авторизация уже выполнена в фикстуре browser"""
        with allure.step("Проверить, что авторизация прошла успешно"):
            try:
                allure.attach(
                    browser.current_url,
                    name="Current URL",
                    attachment_type=allure.attachment_type.TEXT
                )
                assert "hd.kinopoisk.ru" in browser.current_url
                allure.attach(
                    "Авторизация успешна",
                    name="Auth Status",
                    attachment_type=allure.attachment_type.TEXT
                )
            except Exception as e:
                allure.attach(
                    f"Ошибка проверки авторизации: {str(e)}",
                    name="auth_check_error",
                    attachment_type=allure.attachment_type.TEXT
                )
                raise

    @allure.id("UI-2")
    @allure.title("Поиск контента на платформе")
    @allure.description("Поиск и переход к контенту по ключевому слову")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("search", "navigation")
    @pytest.mark.ui
    def test_search_content(self, browser):
        with allure.step("Инициализировать главную страницу"):
            search = MainPage(browser)

        with allure.step("Выполнить поиск контента по запросу '12'"):
            search.click_search('12')

        with allure.step("Проверить, что произошел переход на страницу контента"):
            allure.attach(
                browser.current_url,
                name="URL после поиска",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.id("UI-3")
    @allure.title("Добавление контента в 'Избранное'")
    @allure.description("Добавление текущего контента в список избранного")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("favorites", "bookmark")
    @pytest.mark.ui
    def test_add_to_mylist_from_content(self, browser):
        with allure.step("Инициализировать страницу контента"):
            bookmark = ContentPage(browser)

        with allure.step("Добавить контент в избранное"):
            bookmark.click_bookmark()

    @allure.id("UI-4")
    @allure.title("Удаление контента из 'Избранного'")
    @allure.description("Удаление контента из списка избранного")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("favorites", "remove")
    @pytest.mark.ui
    def test_remove_from_mylist(self, browser):
        with allure.step("Перейти в раздел 'Моё'"):
            mylist = MainPage(browser)
            mylist.click_mylist()

        with allure.step("Удалить контент из избранного"):
            mylist_content = MylistPage(browser)
            mylist_content.remove_from_mylist()

    @allure.id("UI-5")
    @allure.title("Навигация по телеканалам")
    @allure.description("Переход в раздел каналов и выбор конкретного канала")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("channels", "navigation")
    @pytest.mark.ui
    def test_channels_navigation_and_selection(self, browser):
        with allure.step("Перейти в раздел 'Каналы'"):
            channels = MainPage(browser)
            channels.click_channels()

        with allure.step("Выбрать телеканал 'Мужское кино'"):
            channel_list = ChannelsPage(browser)
            channel_list.click_tv_channel('Мужское кино')
