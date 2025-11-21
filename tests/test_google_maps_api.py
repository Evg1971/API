from requests import Response  # Импортируем класс Response для аннотации типов.
from utils.api import GoogleMapsApi  # Импортируем класс GoogleMapsApi.


class TestCreatePlace:
    @staticmethod
    def test_create_new_place():
        print('Метод POST')  # Начало теста.
        result_post: Response = GoogleMapsApi.create_new_place()  # Вызов метода создания нового места.
        # Проверка статус-кода ответа
        assert result_post.status_code == 200, f"Неожиданный статус-код: {result_post.status_code}"
        print('Статус-код корректен')  # Вывод информации о статус-коде
        print('Тест завершился успешно')  # Информация о завершении теста
