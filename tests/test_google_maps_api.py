from requests import Response  # Импортируем класс Response для аннотации типов ответов от API.
from utils.api import GoogleMapsApi  # Импортируем класс GoogleMapsApi, содержащий методы для работы с API Google Maps.


class TestCreatePlace:
    @staticmethod
    def test_create_new_place():
        # Начало выполнения теста: вывод сообщения о начале тестирования метода POST.
        print('Начало тестирования метода POST')

        # Вызов метода создания нового места через API. Результат сохраняется в переменной result_post.
        result_post: Response = GoogleMapsApi.create_new_place()

        # Проверка, что статус-код ответа равен 200 (успешный запрос).
        # Если статус-код другой, тест завершится с ошибкой и выведет неожиданный статус-код.
        assert result_post.status_code == 200, f"Неожиданный статус-код: {result_post.status_code}"

        # Вывод сообщения об успешной проверке статус-кода POST-запроса.
        print('Статус-код POST запроса корректен')

        # Преобразование ответа в JSON-формат для дальнейшей обработки.
        check_post = result_post.json()

        # Извлечение значения place_id из JSON-ответа.
        place_id = check_post.get('place_id')

        # Вывод созданного place_id для отладки и логирования.
        print(f"Создан place_id: {place_id}")

        # Начало тестирования метода GET: вывод сообщения о начале тестирования.
        print('Начало тестирования метода GET')

        # Вызов метода получения информации о созданном месте по place_id.
        result_get: Response = GoogleMapsApi.get_new_place(place_id)

        # Проверка, что статус-код ответа GET-запроса равен 200 (успешный запрос).
        assert result_get.status_code == 200, f"Неожиданный статус-код: {result_get.status_code}"

        # Вывод сообщения об успешной проверке статус-кода GET-запроса.
        print('Статус-код GET запроса корректен')

        # Вывод сообщения об успешном завершении теста.
        print('Тест завершен успешно')
