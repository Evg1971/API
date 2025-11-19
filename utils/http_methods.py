# Импортируем библиотеку requests для выполнения HTTP-запросов
import requests

# Класс HttpMethods предоставляет статические методы для выполнения различных HTTP-запросов
class HttpMethods:
    # Заголовки по умолчанию для всех запросов (указываем, что данные передаются в формате JSON)
    headers = {'Content-type': 'application/json'}
    # Куки, которые могут использоваться в запросах (изначально пустые)
    cookie = ''

    # Статический метод для выполнения GET-запроса
    @staticmethod
    def get(url):
        # Выполняем GET-запрос по указанному URL с заголовками и куками
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result


    # Статический метод для выполнения POST-запроса
    @staticmethod
    def post(url, body):
        # Выполняем POST-запрос по указанному URL с телом запроса в формате JSON, заголовками и куками
        result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result


    # Статический метод для выполнения PUT-запроса
    @staticmethod
    def put(url, body):
        # Выполняем PUT-запрос по указанному URL с телом запроса в формате JSON, заголовками и куками
        result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result


    # Статический метод для выполнения DELETE-запроса
    @staticmethod
    def delete(url, body):
        # Выполняем DELETE-запрос по указанному URL с телом запроса в формате JSON, заголовками и куками
        result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result
