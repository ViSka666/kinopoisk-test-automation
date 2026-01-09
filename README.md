# Автоматизация тестирования Кинопоиск

Проект содержит 5 UI и 5 API автотестов для веб-приложения Кинопоиск.

## Установка

```bash
git clone https://github.com/VISKa666/kinopoisk-test-automation.git
cd kinopoisk-test-automation
pip install -r requirements.txt
```

## Настройка
Создайте файл .env в корне:
test_number=ваш_номер телефона

## Запуск тестов

### Все тесты:
```bash
pytest
```

### Только UI-тесты:
```bash
pytest -m ui
```

### Только API-тесты:
```bash
pytest -m api
```

### Генерация отчета:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Ссылки
Финальная работа по ручному тестированию: https://homework-skypro.yonote.ru/share/a4a3711e-9676-445d-841a-d797d2dd9114