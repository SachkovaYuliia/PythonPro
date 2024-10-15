import requests


class WebService:
    """
    Клас для отримання даних з веб-сайту за допомогою HTTP-запиту.

    Метод get_data робить GET-запит до вказаного URL та повертає JSON-відповідь,
    піднімаючи виключення у разі помилки HTTP-запиту.
    """

    def get_data(self, url: str) -> dict:
        """
        Виконує GET-запит до веб-сайту та повертає JSON-відповідь.

        Args:
            url (str): URL, за яким робиться запит.

        Returns:
            dict: JSON-відповідь від сервера.

        Raises:
            HTTPError: Якщо сервер повертає код помилки (404, 500 тощо).
        """
        response = requests.get(url)
        response.raise_for_status()  
        return response.json()
