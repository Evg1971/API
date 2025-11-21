from utils.http_methods import HttpMethods  # Импортируем класс HttpMethods.


base_url = 'https://rahulshettyacademy.com'  # Базовый URL API.
key = '?qaclick123'  # Ключ для доступа к API.

class GoogleMapsApi:
    @staticmethod
    def create_new_place():
        # JSON-объект с данными для создания нового места.
        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        # Формируем полный URL для POST-запроса.
        post_resource = '/maps/api/place/add/json'
        post_url = base_url + post_resource + key
        print(post_url)  # Выводим URL для отладки.

        # Выполняем POST-запрос для создания нового места.
        result_post = HttpMethods.post(post_url, json_for_create_new_place)
        print(result_post.text)  # Выводим ответ от сервера.
        return result_post
