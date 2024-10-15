class UserManager:
    """
    Клас для керування користувачами.
    """

    def __init__(self):
        """
        Ініціалізує порожній словник користувачів.

        """
        self.users = {}

    def add_user(self, name: str, age: int):
        """
        Додає користувача з ім'ям та віком.

        """
        self.users[name] = age

    def remove_user(self, name: str):
        """
        Видаляє користувача за ім'ям.

        """
        if name in self.users:
            del self.users[name]

    def get_all_users(self) -> dict:
        """
        Повертає словник усіх користувачів.

        """
        return self.users.copy()
