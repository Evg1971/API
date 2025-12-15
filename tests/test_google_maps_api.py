# Импортируем класс Response из библиотеки requests для аннотации типов ответов от API.
from requests import Response
# Импортируем класс GoogleMapsApi из модуля utils.api для работы с API Google Maps.
from utils.api import GoogleMapsApi
# Импортируем класс Checking из модуля utils.checking для проверки статус-кодов ответов.
from utils.checking import Checking


class TestCreatePlace:
    @staticmethod
    def test_create_new_place():
        """ Тест для проверки создания нового места через API.
        Проверяет статус-коды POST, GET, PUT и DELETE запросов,
        а также корректность создания и обновления места. """
        # Начало тестирования метода POST: вывод сообщения о начале теста.
        print('Начало тестирования метода POST')

        # Вызов метода создания нового места через API.
        # Результат POST-запроса сохраняется в переменной result_post.
        result_post: Response = GoogleMapsApi.create_new_place()

        # Проверка, что статус-код ответа равен 200 (OK).
        Checking.check_status_code(result_post, 200)

        # Преобразование ответа POST-запроса в JSON-формат для извлечения данных.
        check_post = result_post.json()

        # Извлечение значения place_id из JSON-ответа.
        place_id = check_post.get('place_id')
        print(f"Создан place_id: {place_id}")  # Вывод place_id для отладки.

        # Проверка структуры JSON-ответа POST.
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])

        # Начало тестирования метода GET для проверки созданного места.
        print('Начало тестирования метода GET POST')

        # Вызов метода получения информации о месте по place_id.
        result_get: Response = GoogleMapsApi.get_new_place(place_id)

        # Проверка, что статус-код ответа равен 200 (OK).
        Checking.check_status_code(result_get, 200)

        # Проверка структуры JSON-ответа GET.
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])

        # Начало тестирования метода PUT для обновления информации о месте.
        print('Начало тестирования метода PUT')

        # Вызов метода обновления информации о месте по place_id.
        result_put: Response = GoogleMapsApi.put_new_place(place_id)

        # Проверка, что статус-код ответа равен 200 (OK).
        Checking.check_status_code(result_put, 200)

        # Проверка структуры JSON-ответа PUT.
        Checking.check_json_token(result_put, ['msg'])

        # Повторный вызов метода GET для проверки обновлённой информации о месте.
        print('Метод GET PUT')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)

        # Проверка, что статус-код ответа равен 200 (OK).
        Checking.check_status_code(result_get, 200)

        # Проверка структуры JSON-ответа GET.
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])

        # Вывод сообщения о начале тестирования метода DELETE.
        print('Начало тестирования метода DELETE')

        # Вызов метода удаления места по его идентификатору.
        result_delete: Response = GoogleMapsApi.delete_new_place(place_id)

        # Проверка, что статус-код ответа равен 200 (OK).
        Checking.check_status_code(result_delete, 200)

        # Проверка структуры JSON-ответа DELETE.
        Checking.check_json_token(result_delete, ['status'])

        # Преобразование ответа DELETE-запроса в JSON-формат для извлечения данных.
        check_delete = result_delete.json()

        # Извлечение значения поля 'status' из JSON-ответа.
        status = check_delete.get('status')

        # Проверка, что поле 'status' в ответе равно 'OK'.
        # Это подтверждает, что удаление прошло успешно.
        assert status == 'OK', f"Неожиданное значение поля status: {status}"

        # Вывод сообщения об успешной проверке статус-кода и статуса DELETE-запроса.
        print('Статус-код DELETE запроса корректен, место успешно удалено')

        # --- Тестирование метода GET после DELETE ---
        print('Тестирование метода GET (после DELETE)')

        # Вызов метода получения информации о месте по place_id после удаления.
        result_get: Response = GoogleMapsApi.get_new_place(place_id)

        # Проверка, что статус-код ответа равен 404.
        Checking.check_status_code(result_get, 404)

        # Проверка структуры JSON-ответа GET.
        Checking.check_json_token(result_get, ['msg'])

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
        print('Тестирование создания, изменения и удаления новой локации прошло'
              ' успешно')