from utils.http_methods import HttpMethods  # Импортируем класс HttpMethods для выполнения HTTP-запросов.


# Базовый URL API, к которому будут отправляться запросы.
base_url = 'https://rahulshettyacademy.com'

# Ключ для доступа к API, добавляется к запросам в качестве параметра.
key = '?qaclick123'

class GoogleMapsApi:
    @staticmethod
    def create_new_place():
        # JSON-объект с данными, необходимыми для создания нового места.
        # Содержит информацию о местоположении, точности, названии, телефоне, адресе и других атрибутах.
        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,  # Широта местоположения.
                "lng": 33.427362    # Долгота местоположения.
            },
            "accuracy": 50,         # Точность координат.
            "name": "Frontline house",  # Название места.
            "phone_number": "(+91) 983 893 3937",  # Контактный телефон.
            "address": "29, side layout, cohen 09",  # Адрес места.
            "types": [
                "shoe park",  # Тип места.
                "shop"        # Тип места.
            ],
            "website": "http://google.com",  # Веб-сайт места.
            "language": "French-IN"  # Язык, на котором представлена информация.
        }

        # Формируем ресурсный путь для POST-запроса.
        post_resource = '/maps/api/place/add/json'

        # Формируем полный URL для POST-запроса, объединяя базовый URL, ресурсный путь и ключ.
        post_url = base_url + post_resource + key

        # Выводим сформированный URL для отладки.
        print(post_url)

        # Выполняем POST-запрос для создания нового места, передавая сформированный URL и JSON-данные.
        result_post = HttpMethods.post(post_url, json_for_create_new_place)

        # Выводим текст ответа от сервера для отладки.
        print(result_post.text)

        # Возвращаем результат POST-запроса.
        return result_post

    @staticmethod
    def get_new_place(place_id):
        # Формируем ресурсный путь для GET-запроса.
        get_resource = '/maps/api/place/get/json'

        # Формируем полный URL для GET-запроса, добавляя place_id в качестве параметра.
        get_url = base_url + get_resource + key + '&place_id=' + place_id

        # Выводим сформированный URL для отладки.
        print(get_url)

        # Выполняем GET-запрос для получения информации о месте по его place_id.
        result_get = HttpMethods.get(get_url)

        # Выводим текст ответа от сервера для отладки.
        print(result_get.text)

        # Возвращаем результат GET-запроса.
        return result_get
