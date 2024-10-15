# Завдання 3. Використання фікстур у pytest

# Напишіть програму для керування користувачами та напишіть тести з використанням фікстур у pytest. Напишіть клас UserManager, який реалізує такі методи:

# add_user(name: str, age: int): додає користувача.
# remove_user(name: str): видаляє користувача на ім'я.
# get_all_users() -> list: повертає список усіх користувачів.

import pytest
from user_manager import UserManager

@pytest.fixture
def user_manager():
    """
    Створює екземпляр UserManager та додає попередніх користувачів.
    """
    
    um = UserManager()
    um.add_user("Alice", 30)
    um.add_user("Bob", 25)
    return um

def test_add_user(user_manager):
    """
    Тест перевіряє, чи додається новий користувач.
    """

    user_manager.add_user("Charlie", 20)
    assert "Charlie" in user_manager.get_all_users()
    assert user_manager.get_all_users()["Charlie"] == 20

def test_remove_user(user_manager):
    """
    Тест перевіряє, чи видаляється існуючий користувач.
    """

    user_manager.remove_user("Alice")
    assert "Alice" not in user_manager.get_all_users()

def test_get_all_users(user_manager):
    """
    Тест перевіряє, чи повертається правильний список користувачів.
    """

    users = user_manager.get_all_users()
    assert len(users) == 2
    assert users == {"Alice": 30, "Bob": 25}

@pytest.mark.skipif(
    len({"Alice": 30, "Bob": 25}) < 3,
    reason="Менше трьох користувачів"
)
def test_skip_if_few_users(user_manager):
    """
    Тест пропускається, якщо кількість користувачів менше трьох.
    """

    assert len(user_manager.get_all_users()) >= 3