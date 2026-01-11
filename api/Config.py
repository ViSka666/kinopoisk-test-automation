import os
from dotenv import load_dotenv
import allure

load_dotenv()


class Config:
    def __init__(self):
        """
        Конфигурация для API Кинопоиска
        Загружает API ключ из переменных окружения
        """
        self.x_api_key = os.getenv("x_api_key")
        self.base_url = "https://api.kinopoisk.dev/v1.4/"

    @allure.step("Получить заголовки для API запросов")
    def headers(self):
        """
        Возвращает стандартные заголовки для API запросов

        Returns:
            dict: Заголовки с API ключом и типом контента
        """
        return {
            "X-API-KEY": f"{self.x_api_key}",
            "Content-Type": "application/json"
        }

    @allure.step("Сформировать URL для поиска по стране: {countries_name}")
    def url_search_by_countries(self, countries_name: str) -> str:
        """
        Формирует URL для поиска фильмов по стране производства

        Args:
            countries_name: Название страны

        Returns:
            str: Полный URL для запроса
        """
        return f"{self.base_url}movie?countries.name={countries_name}"

    @allure.step("Сформировать URL для поиска по ID: {id}")
    def url_search_by_id(self, id: str) -> str:
        """
        Формирует URL для поиска фильма по ID

        Args:
            id: Идентификатор фильма

        Returns:
            str: Полный URL для запроса
        """
        return f"{self.base_url}movie?id={id}"

    @allure.step("Сформировать URL для поиска по рейтингу: {rating}")
    def url_search_by_rating(self, rating: str) -> str:
        """
        Формирует URL для поиска фильмов по рейтингу

        Args:
            rating: Рейтинг фильма

        Returns:
            str: Полный URL для запроса
        """
        return f"{self.base_url}movie?rating.kp={rating}"

    @allure.step("Сформировать URL для поиска по году: {year}")
    def url_search_by_year(self, year: str) -> str:
        """
        Формирует URL для поиска фильмов по году выпуска

        Args:
            year: Год выпуска

        Returns:
            str: Полный URL для запроса
        """
        return f"{self.base_url}movie?year={year}"

    @allure.step("Сформировать URL для поиска по типу контента: {type_content}")
    def url_search_by_type_content(self, type_content: str) -> str:
        """
        Формирует URL для поиска по типу контента

        Args:
            type_content: Тип контента (cartoon, movie, tv-series и т.д.)

        Returns:
            str: Полный URL для запроса
        """
        return f"{self.base_url}movie?type={type_content}"


config = Config()
