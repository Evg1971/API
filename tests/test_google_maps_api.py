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

        # Вывод сообщения о начале тестирования метода DELETE.
        print('Начало тестирования метода DELETE')

        # Вызов метода удаления места по его идентификатору.
        result_delete: Response = GoogleMapsApi.delete_new_place(place_id)

        # Проверка статус-кода ответа DELETE-запроса.
        # Ожидается статус-код 200, что означает успешное выполнение запроса.
        assert result_delete.status_code == 200, f"Неожиданный статус-код: {result_delete.status_code}"
        print("Статус-код DELETE корректен")

        # Преобразование ответа DELETE-запроса в JSON-формат для извлечения данных.
        check_delete = result_delete.json()

        # Извлечение значения поля 'status' из JSON-ответа.
        status = check_delete.get('status')

        # Проверка, что поле 'status' в ответе равно 'OK'.
        # Это подтверждает, что удаление прошло успешно.
        assert status == 'OK', f"Неожиданное значение поля status: {status}"

        # Вывод сообщения об успешной проверке статус-кода и статуса DELETE-запроса.
        print('Статус-код DELETE запроса корректен, место успешно удалено')

        # Вывод сообщения о начале проверки метода GET после удаления.
        print('Метод GET DELETE')

        # Вызов метода получения информации о месте по place_id после удаления.
        result_get: Response = GoogleMapsApi.get_new_place(place_id)

        # Проверка статус-кода ответа GET-запроса после удаления.
        # Ожидается статус-код 404, что означает, что место с данным place_id не найдено.
        assert result_get.status_code == 404, f"Неожиданный статус-код: {result_get.status_code}"
        print('Статус-код GET DELETE корректен')

        # Преобразование ответа GET-запроса в JSON-формат для извлечения данных.
        check_get = result_get.json()

        # Извлечение значения поля 'msg' из JSON-ответа.
        msg = check_get.get('msg')

        # Проверка, что поле 'msg' в ответе содержит сообщение об ошибке.
        # Это подтверждает, что место действительно удалено и недоступно для получения.
        assert msg == "Get operation failed, looks like place_id  doesn't exists", \
            f"Неожиданное сообщение в ответе: {msg}"
        print('Проверка удаления места прошла успешно')

        # Вывод сообщения об успешном завершении теста.
        print('Тест завершен успешно')