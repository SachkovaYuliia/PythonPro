# 1.	Реалізуйте клас User з атрибутами first_name, last_name, email. Додайте методи для отримання та встановлення цих атрибутів через декоратор @property.

# 2.	Додайте методи для перевірки формату email-адреси.

import re

class User:
    """
    Клас, що представляє користувача з атрибутами first_name, last_name, email.
    """

    def __init__(self, first_name, last_name, email):
        """
        Ініціалізує об'єкт User.

        """
        self._first_name = first_name
        self._last_name = last_name
        self.email = email  

    @property
    def first_name(self):
        """
        Повертає ім'я користувача.

        """
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """
        Встановлює нове ім'я користувача.

        """
        self._first_name = value

    @property
    def last_name(self):
        """
        Повертає прізвище користувача.

        """
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """
        Встановлює нове прізвище користувача.

        """
        self._last_name = value

    @property
    def email(self):
        """
        Повертає email користувача.

        """
        return self._email

    @email.setter
    def email(self, value):
        """
        Встановлює новий email і перевіряє його коректність.

        """
        if not self.is_valid_email(value):
            raise ValueError(f"Invalid email format: {value}")
        self._email = value

    @staticmethod
    def is_valid_email(email):
        """
        Перевіряє формат email-адреси.

        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def __repr__(self):
        """
        Повертає строкове представлення об'єкта User.

        """
        return f"User('{self.first_name}', '{self.last_name}', '{self.email}')"



def test_user():
    user = User('Test', 'Test_0', 'test@gmail.com')
    print(user)  

    user.first_name = 'Test1'
    print(user.first_name)  

    user.last_name = 'Test1_1'
    print(user.last_name)  

    user.email = 'test1@gmail.com'
    print(user.email)  


    try:
        user.email = 'invalid-email'
    except ValueError as e:
        print(e)  

test_user()
