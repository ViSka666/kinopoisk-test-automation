import sys
import os
import requests
import pytest
import allure

from api.Config import config

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.pop('CURL_CA_BUNDLE', None)


@allure.epic("API Тестирование")
@allure.feature("Поиск контента")
@allure.story("Фильтрация по различным критериям")
class TestKinopoiskAPI:

    @allure.id("API-1")
    @allure.title("Поиск фильмов по стране производства")
    @allure.description("Проверка поиска фильмов произведенных в указанной стране")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("search", "countries")
    @pytest.mark.api
    def test_search_by_countries(self):
        with allure.step("Подготовить запрос для поиска по стране 'Япония'"):
            url = config.url_search_by_countries('Япония')
            headers = config.headers()
            allure.attach(f"URL: {url}", "Request URL", allure.attachment_type.TEXT)

        with allure.step("Отправить GET запрос к API"):
            resp = requests.get(url, headers=headers)
            allure.attach(f"Status Code: {resp.status_code}", "Response", allure.attachment_type.TEXT)

        with allure.step("Проверить успешный ответ (200 OK)"):
            assert resp.status_code == 200

        with allure.step("Проверить структуру ответа"):
            data = resp.json()
            allure.attach(str(data), "Response Body", allure.attachment_type.JSON)

    @allure.id("API-2")
    @allure.title("Поиск фильма по ID")
    @allure.description("Проверка получения информации о фильме по его уникальному идентификатору")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("search", "id")
    @pytest.mark.api
    def test_search_by_id(self):
        with allure.step("Подготовить запрос для поиска фильма с ID 231243"):
            url = config.url_search_by_id('231243')
            headers = config.headers()
            allure.attach(f"URL: {url}", "Request URL", allure.attachment_type.TEXT)

        with allure.step("Отправить GET запрос к API"):
            resp = requests.get(url, headers=headers)
            allure.attach(f"Status Code: {resp.status_code}", "Response", allure.attachment_type.TEXT)

        with allure.step("Проверить успешный ответ (200 OK)"):
            assert resp.status_code == 200

    @allure.id("API-3")
    @allure.title("Поиск фильмов по рейтингу")
    @allure.description("Проверка фильтрации фильмов по рейтингу Кинопоиска")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("search", "rating")
    @pytest.mark.api
    def test_search_by_rating(self):
        with allure.step("Подготовить запрос для поиска фильмов с рейтингом 9"):
            url = config.url_search_by_rating('9')
            headers = config.headers()
            allure.attach(f"URL: {url}", "Request URL", allure.attachment_type.TEXT)

        with allure.step("Отправить GET запрос к API"):
            resp = requests.get(url, headers=headers)
            allure.attach(f"Status Code: {resp.status_code}", "Response", allure.attachment_type.TEXT)

        with allure.step("Проверить успешный ответ (200 OK)"):
            assert resp.status_code == 200

    @allure.id("API-4")
    @allure.title("Поиск фильмов по году выпуска")
    @allure.description("Проверка поиска фильмов выпущенных в указанном году")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("search", "year")
    @pytest.mark.api
    def test_search_by_year(self):
        with allure.step("Подготовить запрос для поиска фильмов 2026 года"):
            url = config.url_search_by_year('2026')
            headers = config.headers()
            allure.attach(f"URL: {url}", "Request URL", allure.attachment_type.TEXT)

        with allure.step("Отправить GET запрос к API"):
            resp = requests.get(url, headers=headers)
            allure.attach(f"Status Code: {resp.status_code}", "Response", allure.attachment_type.TEXT)

        with allure.step("Проверить успешный ответ (200 OK)"):
            assert resp.status_code == 200

    @allure.id("API-5")
    @allure.title("Поиск по типу контента")
    @allure.description("Проверка фильтрации контента по типу (мультфильм, сериал и т.д.)")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("search", "content_type")
    @pytest.mark.api
    def test_search_by_type_content(self):
        with allure.step("Подготовить запрос для поиска мультфильмов"):
            url = config.url_search_by_type_content('cartoon')
            headers = config.headers()
            allure.attach(f"URL: {url}", "Request URL", allure.attachment_type.TEXT)

        with allure.step("Отправить GET запрос к API"):
            resp = requests.get(url, headers=headers)
            allure.attach(f"Status Code: {resp.status_code}", "Response", allure.attachment_type.TEXT)

        with allure.step("Проверить успешный ответ (200 OK)"):
            assert resp.status_code == 200
