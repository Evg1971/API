# Импортируем библиотеку requests для выполнения HTTP-запросов
import requests

# Импортируем класс Logger из модуля utils.logger для логирования запросов и ответов.
from utils.logger import Logger


# Класс HttpMethods предоставляет статические методы для выполнения различных HTTP-запросов
class HttpMethods:
    # Заголовки по умолчанию для всех запросов (указываем, что данные передаются в формате JSON)
    headers = {'Content-type': 'application/json'}
    # Куки, которые могут использоваться в запросах (изначально пустые)
    cookie = ''

    @staticmethod  # Статический метод для выполнения GET-запроса
    def get(url):
        # Логируем информацию о GET-запросе.
        Logger.add_request(url, method='GET')

        # Выполняем GET-запрос по указанному URL с заголовками и куками
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)

        # Логируем информацию об ответе на GET-запрос.
        Logger.add_response(result)

        # Возвращаем объект ответа.
        return result

    @staticmethod  # Статический метод для выполнения POST-запроса
    def post(url, body):
        # Логируем информацию о POST-запросе.
        Logger.add_request(url, method='POST')

        # Выполняем POST-запрос по указанному URL с телом запроса в формате JSON, заголовками и куками
        result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)

        # Логируем информацию об ответе на POST-запрос.
        Logger.add_response(result)

        # Возвращаем объект ответа.
        return result

    @staticmethod  # Статический метод для выполнения PUT-запроса
    def put(url, body):
        # Логируем информацию о PUT-запросе.
        Logger.add_request(url, method='PUT')

        # Выполняем PUT-запрос по указанному URL с телом запроса в формате JSON, заголовками и куками
        result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)

        # Логируем информацию об ответе на PUT-запрос.
        Logger.add_response(result)

        # Возвращаем объект ответа.
        return result

    @staticmethod  # Статический метод для выполнения DELETE-запроса
    def delete(url, body):
        # Логируем информацию о DELETE-запросе.
        Logger.add_request(url, method='DELETE')

        # Выполняем DELETE-запрос по указанному URL с телом запроса в формате JSON, заголовками и куками
        result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)

        # Логируем информацию об ответе на DELETE-запрос.
        Logger.add_response(result)

        # Возвращаем объект ответа.
        return result