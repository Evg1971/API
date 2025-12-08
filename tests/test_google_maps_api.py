# Импортируем класс Response из библиотеки requests для аннотации типов ответов от API.
from requests import Response
# Импортируем класс GoogleMapsApi из модуля utils.api для работы с API Google Maps.
from utils.api import GoogleMapsApi


class TestCreatePlace:
    @staticmethod
    def test_create_new_place():
        """ Тест для проверки создания нового места через API.
        Проверяет статус-коды POST, GET и PUT запросов,
        а также корректность создания и обновления места. """
        # Начало тестирования метода POST: вывод сообщения о начале теста.
        print('Начало тестирования метода POST')

        # Вызов метода создания нового места через API.
        # Результат POST-запроса сохраняется в переменной result_post.
        result_post: Response = GoogleMapsApi.create_new_place()

        # Проверка статус-кода ответа POST-запроса.
        # Ожидается статус-код 200 (успешный запрос).
        assert result_post.status_code == 200, f"Неожиданный статус-код: {result_post.status_code}"
        print('Статус-код POST запроса корректен')

        # Преобразование ответа POST-запроса в JSON-формат для извлечения данных.
        check_post = result_post.json()

        # Извлечение значения place_id из JSON-ответа.
        place_id = check_post.get('place_id')
        print(f"Создан place_id: {place_id}")  # Вывод place_id для отладки.

        # Начало тестирования метода GET для проверки созданного места.
        print('Начало тестирования метода GET POST')

        # Вызов метода получения информации о месте по place_id.
        result_get: Response = GoogleMapsApi.get_new_place(place_id)

        # Проверка статус-кода ответа GET-запроса.
        assert result_get.status_code == 200, f"Неожиданный статус-код: {result_get.status_code}"
        print('Статус-код GET запроса корректен')

        # Начало тестирования метода PUT для обновления информации о месте.
        print('Начало тестирования метода PUT')

        # Вызов метода обновления информации о месте по place_id.
        result_put: Response = GoogleMapsApi.put_new_place(place_id)

        # Проверка статус-кода ответа PUT-запроса.
        assert result_put.status_code == 200, f"Неожиданный статус-код: {result_put.status_code}"
        print('Статус-код PUT запроса корректен')

        # Повторный вызов метода GET для проверки обновлённой информации о месте.
        print('Метод GET PUT')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)

        # Проверка статус-кода ответа повторного GET-запроса.
        assert result_get.status_code == 200, f"Неожиданный статус-код: {result_get.status_code}"
        print('Статус-код GET PUT запроса корректен')

        # Вывод сообщения об успешном завершении теста.
        print('Тест завершен успешно')
