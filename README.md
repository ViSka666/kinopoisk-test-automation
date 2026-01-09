Автоматизация тестирования Кинопоиск

Проект содержит 5 UI и 5 API автотестов для веб-приложения Кинопоиск.

Создайте файл .env в корне:

test_nomber=ваш_номер телефона

Запуск тестов

Все тесты:
pytest

Только UI-тесты:
pytest -m ui

Только API-тесты:
pytest -m api

Генерация отчета:
pytest --alluredir=allure-results
allure serve allure-results

Ссылки
Финальная работа по ручному тестированию: https://homework-skypro.yonote.ru/share/a4a3711e-9676-445d-841a-d797d2dd9114