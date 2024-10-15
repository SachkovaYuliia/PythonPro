# Завдання 5. Тестування винятків у pytest (опціонально)

# Напишіть функцію divide(a: int, b: int) -> float, яка поділяє два числа. Якщо знаменник дорівнює нулю, функція повинна викидати виняток ZeroDivisionError. Напишіть тести з використанням pytest, які:

# перевіряють коректний поділ,
# перевіряють викидання виключення ZeroDivisionError, якщо знаменник дорівнює нулю.
# Додайте тест із параметризацією для перевірки поділу з різними значеннями.

import pytest
from divide_for_pytest import divide  

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
    Тест для перевірки поділу з різними значеннями
    """

    assert divide(a, b) == expected
