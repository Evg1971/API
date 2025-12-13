# Импортируем класс HttpMethods из модуля utils.http_methods для выполнения HTTP-запросов.
from utils.http_methods import HttpMethods


class GoogleMapsApi:
    # Базовый URL API, к которому будут отправляться все запросы.
    base_url = 'https://rahulshettyacademy.com'

    # Ключ API, который добавляется к каждому запросу в качестве параметра.
    key = '?key=qaclick123'

    @staticmethod
    def create_new_place():
        """
        Метод для создания нового места через API.
        Возвращает результат POST-запроса.
        """
        # JSON-объект с данными для создания нового места.
        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,  # Координата широты местоположения.
                "lng": 33.427362   # Координата долготы местоположения.
            },
            "accuracy": 50,  # Точность координат местоположения.
            "name": "Frontline house",  # Название создаваемого места.
            "phone_number": "(+91) 983 893 3937",  # Контактный телефон места.
            "address": "29, side layout, cohen 09",  # Адрес места.
            "types": [
                "shoe park",  # Тип места.
                "shop"        # Тип места.
            ],
            "website": "http://google.com",  # Веб-сайт места.
            "language": "French-IN"  # Язык информации о месте.
        }

        # Ресурсный путь для POST-запроса на создание нового места.
        post_resource = '/maps/api/place/add/json'

        # Формируем полный URL для POST-запроса.
        post_url = GoogleMapsApi.base_url + post_resource + GoogleMapsApi.key

        # Выводим сформированный URL для отладки.
        print(post_url)

        # Выполняем POST-запрос для создания нового места.
        result_post = HttpMethods.post(post_url, json_for_create_new_place)

        # Выводим текст ответа от сервера для отладки.
        print(result_post.text)

        # Возвращаем результат POST-запроса.
        return result_post

    @staticmethod
    def get_new_place(place_id):
        """ Метод для получения информации о месте по его идентификатору.
        Возвращает результат GET-запроса."""
        # Ресурсный путь для GET-запроса.
        get_resource = '/maps/api/place/get/json'

        # Формируем полный URL для GET-запроса, добавляя place_id в качестве параметра.
        get_url = GoogleMapsApi.base_url + get_resource + GoogleMapsApi.key + '&place_id=' + place_id

        # Выводим сформированный URL для отладки.
        print(get_url)

        # Выполняем GET-запрос для получения информации о месте.
        result_get = HttpMethods.get(get_url)

        # Выводим текст ответа от сервера для отладки.
        print(result_get.text)

        # Возвращаем результат GET-запроса.
        return result_get

    @staticmethod
    def put_new_place(place_id):
        """ Метод для обновления информации о месте по его идентификатору.
        Возвращает результат PUT-запроса. """
        # Ресурсный путь для PUT-запроса.
        put_resource = '/maps/api/place/update/json'

        # Формируем полный URL для PUT-запроса.
        put_url = GoogleMapsApi.base_url + put_resource + GoogleMapsApi.key

        # Выводим сформированный URL для отладки.
        print(put_url)

        # JSON-объект с данными для обновления информации о месте.
        json_for_update_new_location = {
            "place_id": place_id,  # Идентификатор места.
            "address": "100 Lenina street, RU",  # Новый адрес места.
            "key": "qaclick123"  # Ключ API.
        }

        # Выполняем PUT-запрос для обновления информации о месте.
        result_put = HttpMethods.put(put_url, json_for_update_new_location)

        # Выводим текст ответа от сервера для отладки.
        print(result_put.text)

        # Возвращаем результат PUT-запроса.
        return result_put

    @staticmethod
    def delete_new_place(place_id):
        """ Метод для удаления места по его идентификатору.
        Возвращает результат DELETE-запроса. """

        # Ресурсный путь для DELETE-запроса
        delete_resource = '/maps/api/place/delete/json'

        # Формируем полный URL для DELETE-запроса
        delete_url = GoogleMapsApi.base_url + delete_resource + GoogleMapsApi.key

        # Выводим сформированный URL для отладки.
        print(f"DELETE URL: {delete_url}")

        # JSON-объект с данными для удаления места.
        # Содержит идентификатор места, который нужно удалить.
        json_for_delete_new_location = {
            "place_id": place_id
        }

        # Выполняем DELETE-запрос для удаления места.
        # Передаем сформированный URL и JSON-объект с идентификатором места.
        result_delete = HttpMethods.delete(delete_url, json_for_delete_new_location)

        # Выводим текст ответа от сервера для отладки.
        print(f"DELETE Response: {result_delete.text}")

        # Возвращаем результат DELETE-запроса.
        return result_delete