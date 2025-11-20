from requests import Response  # Импортируем класс Response для аннотации типов.
from utils.api import GoogleMapsApi  # Импортируем класс GoogleMapsApi.

class TestCreatePlace:
    def test_create_new_place(self):
        print('Метод POSTT')  # Начало теста.
        result_post: Response = GoogleMapsApi.create_new_place()  # Вызов метода создания нового места.
