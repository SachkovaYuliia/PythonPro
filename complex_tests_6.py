# Завдання 6. Приклад комплексного тестування

# Розробіть програму для роботи з банківськими транзакціями та протестуйте її за допомогою фікстур, моків, скіпів та параметризації. Напишіть клас BankAccount, який реалізує методи:

# deposit(amount: float): поповнення рахунку;
# withdraw(amount: float): зняття коштів (якщо достатньо коштів на рахунку).
# get_balance() -> float: повертає поточний баланс.
# Напишіть тести з використанням:

# фікстур для створення об'єкта банківського рахунку перед тестами,
# моків для тестування взаємодії із зовнішнім API (наприклад, для перевірки балансу),
# скіпів для пропуску тестів зняття коштів, якщо рахунок порожній.
# Використовуйте параметризацію для тестування різних сценаріїв поповнення та зняття коштів.

import pytest
from bankaccount_for_complex_test import divide  

def test_divide_correct():
    """
    Перевірка коректного поділу
    """

    assert divide(10, 2) == 5.0
    assert divide(9, 3) == 3.0
    assert divide(7, 1) == 7.0

def test_divide_zero_division():
    """
    Перевірка винятку ZeroDivisionError при діленні на нуль
    """

    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (9, 3, 3.0),
    (7, 7, 1.0),
    (100, 4, 25.0),
    (-10, 2, -5.0),
    (0, 5, 0.0),
])
def test_divide_parametrized(a, b, expected):
    """
    Параметризований тест для перевірки поділу з різними значеннями
    """

    assert divide(a, b) == expected
