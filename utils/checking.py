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
    def check_json_token(response: Response, expected_value: list):
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

