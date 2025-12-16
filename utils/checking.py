import json

from requests import Response  # Импортируем класс Response из библиотеки requests


class Checking:
    @staticmethod
    def check_status_code(response: Response, status_code: int):
        """ Статический метод для проверки статус-кода HTTP-ответа."""

        # Проверяем, что статус-код ответа совпадает с ожидаемым
        assert response.status_code == status_code, (
            f"Провал. Ожидался статус-код {status_code}, "
            f"получен {response.status_code}"
        )
        # Если статус-коды совпадают, выводим сообщение об успехе
        print(f"Успешно. Статус-код = {response.status_code}")

    @staticmethod
    def check_json_token(response: Response, expected_value):
        """ Статический метод для проверки наличия ожидаемых полей в JSON-ответе."""

        # Преобразуем текст ответа в объект Python (JSON).
        token = json.loads(response.text)

        # Проверяем, что список ключей в JSON совпадает с ожидаемым списком.
        assert list(token) == expected_value, (
            f"Провал. Ожидались поля: {expected_value}, "
            f"получены поля: {list(token)}"
        )

        # Если проверка пройдена успешно, выводим сообщение.
        print("Все поля присутствуют")

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        """Статический метод для проверки значения конкретного поля в JSON-ответе."""

        # Преобразуем ответ в JSON-формат.
        check = response.json()

        # Получаем значение указанного поля.
        check_info = check.get(field_name)

        # Проверяем, что значение поля совпадает с ожидаемым.
        assert check_info == expected_value, (
            f"Провал. Ожидалось значение {expected_value}, "
            f"получено {check_info}"
        )
        # Если проверка пройдена успешно, выводим сообщение.
        print(f"Значение {field_name} верно")

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        """Статический метод для проверки наличия подстроки в значении поля JSON-ответа"""

        # Преобразуем ответ в JSON-формат.
        check = response.json()

        # Получаем значение указанного поля.
        check_info = check.get(field_name)

        # Проверяем, содержится ли искомая подстрока в значении поля.
        if search_word in check_info:
            print(f"Успешно. Слово {search_word} присутствует.")
        else:
            # Если подстрока не найдена, выводим сообщение о провале.
            print(f"Провал. Слово {search_word} отсутствует")