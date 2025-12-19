# Импортируем модуль datetime для работы с датой и временем.
import datetime
# Импортируем модуль os для работы с переменными окружения и файловой системой.
import os
# Импортируем класс Response из библиотеки requests для аннотации типов ответов от API.
from requests import Response

class Logger:
    # Имя файла лога формируется с использованием текущей даты и времени.
    # Файлы логов сохраняются в папке Logs.
    file_name = f"Logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + '.log'

    @classmethod
    def write_log_to_file(cls, data: str):
        """Классовый метод для записи данных в файл лога.
        Args: data (str): Строка, которую необходимо записать в файл лога.
        """
        # Открываем файл лога в режиме добавления ('a') с кодировкой utf-8.
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            # Записываем переданные данные в файл.
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, method: str):
        """Классовый метод для логирования информации о запросе.
        Args: url (str): URL, по которому был отправлен запрос.
            method (str): Метод HTTP-запроса (например, GET, POST, PUT, DELETE).
        """
        # Получаем имя текущего теста из переменной окружения.
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        # Формируем строку с информацией о запросе.
        data_to_add = f'\n-----\n'  # Разделитель для удобства чтения лога.
        data_to_add += f'Test: {test_name}\n'  # Имя теста.
        data_to_add += f'Time: {str(datetime.datetime.now())}\n'  # Текущее время.
        data_to_add += f'Request method: {method}\n'  # Метод запроса.
        data_to_add += f'Request URL: {url}\n'  # URL запроса.
        data_to_add += '\n'  # Пустая строка для разделения.

        # Записываем сформированную строку в файл лога.
        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, result: Response):
        """Классовый метод для логирования информации об ответе на запрос.
        Args: result (Response): Объект ответа от сервера.
        """
        # Преобразуем заголовки и куки ответа в словари для удобства логирования.
        headers_as_dict = dict(result.headers)
        cookies_as_dict = dict(result.cookies)

        # Формируем строку с информацией об ответе.
        data_to_add = f'Response code: {result.status_code}\n'  # Статус-код ответа.
        data_to_add += f'Response text: {result.text}\n'  # Текст ответа.
        data_to_add += f'Response headers: {headers_as_dict}\n'  # Заголовки ответа.
        data_to_add += f'Response cookies: {cookies_as_dict}\n'  # Куки ответа.
        data_to_add += f'\n-----\n'  # Разделитель для удобства чтения лога.

        # Записываем сформированную строку в файл лога.
        cls.write_log_to_file(data_to_add)
