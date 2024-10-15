# Завдання 2. Мокування за допомогою unittest.mock

# Напишіть програму для отримання даних з веб-сайту та протестуйте його за допомогою моків. Напишіть клас WebService, який має метод get_data(url: str) -> dict. Цей метод повинен використовувати бібліотеку requests, щоб робити GET-запит та повертати JSON-відповідь. Використовуйте unittest.mock для макування HTTP-запитів. Замокуйте метод requests.get таким чином, щоб він повертав фейкову відповідь (наприклад, {"data": "test"}), та протестуйте метод get_data.

# Напишіть кілька тестів:

# перевірка успішного запиту (200),
# перевірка обробки помилки (404 чи інші коди).

import unittest
from unittest.mock import patch, Mock
import requests
from web_service import WebService


class TestWebService(unittest.TestCase):
    """
    Клас для тестування WebService з використанням unittest.mock.

    Тести включають перевірку успішного запиту та обробку різних помилок HTTP-запитів.
    """

    @patch('web_service.requests.get')
    def test_get_data_success(self, mock_get):
        """
        Тест для перевірки успішного отримання даних (статус 200).

        Імітує успішну відповідь від сервера та перевіряє, що метод
        повертає коректну JSON-відповідь.
        """
        
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_get.return_value = mock_response

        service = WebService()
        result = service.get_data('http://example.com')

        # Перевірка, що результат відповідає очікуваній відповіді
        self.assertEqual(result, {"data": "test"})
        # Перевірка, що GET-запит був виконаний
        mock_get.assert_called_once_with('http://example.com')

    @patch('web_service.requests.get')
    def test_get_data_404_error(self, mock_get):
        """
        Тест для перевірки обробки помилки 404 (Not Found).

        Імітує відповідь від сервера зі статусом 404 та перевіряє, що
        піднімається виключення HTTPError.
        """
        
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_get.return_value = mock_response

        service = WebService()

        with self.assertRaises(requests.exceptions.HTTPError):
            service.get_data('http://example.com/notfound')

        mock_get.assert_called_once_with('http://example.com/notfound')

    @patch('web_service.requests.get')
    def test_get_data_server_error(self, mock_get):
        """
        Тест для перевірки обробки помилки 500 (Internal Server Error).

        Імітує відповідь від сервера зі статусом 500 та перевіряє, що
        піднімається виключення HTTPError.
        """

        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_get.return_value = mock_response

        service = WebService()

        with self.assertRaises(requests.exceptions.HTTPError):
            service.get_data('http://example.com/servererror')

        mock_get.assert_called_once_with('http://example.com/servererror')


if __name__ == '__main__':
    unittest.main()

