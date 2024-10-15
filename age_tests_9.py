# Завдання 9. Тестування різних сценаріїв скіпів та умов (опціонально)

# Завдання: Напишіть програму для перевірки віку користувачів та додайте різні скіпи та умови у тестах. Реалізуйте клас AgeVerifier, який перевіряє вік:

# is_adult(age: int) -> bool: повертає True, якщо вік більше або дорівнює 18.

# Напишіть тести, які:

# перевіряють коректну роботу функції для різного віку,
# пропускають тест, якщо вік менший за 0 (некоректне значення), з використанням pytest.mark.skip.

import pytest
from ageVerifier_for_age_tests import AgeVerifier  

# Тести для різних значень віку
@pytest.mark.parametrize("age, expected", [
    (17, False),  # Неповнолітній
    (18, True),   # Дорослий
    (20, True),   # Дорослий
    (120, True),  # Дорослий
    (121, False), # Малоймовірний сценарій
])
def test_is_adult(age, expected):
    """
    Перевіряє коректну роботу функції is_adult для різних вікових груп.
    """
    assert AgeVerifier.is_adult(age) == expected


# Тест з пропуском, якщо вік менший за 0
@pytest.mark.skip(reason="Некоректне значення віку (менше за 0)")
def test_is_adult_negative_age():
    """
    Пропускає тест, якщо вік некоректний (менше 0).
    """
    assert AgeVerifier.is_adult(-1) == False


# Умовний скіп, якщо вік більше 120
@pytest.mark.skipif(121 > 120, reason="Неправильне значення віку (більше 120)")
def test_is_adult_age_above_120():
    """
    Пропускає тест, якщо вік більше 120 (малоймовірний сценарій).
    """
    assert AgeVerifier.is_adult(121) == False


# Тест з очікуваним винятком для негативного віку
def test_is_adult_raises_for_negative_age():
    """
    Перевіряє, що викликається ValueError, якщо вік менший за 0.
    """
    with pytest.raises(ValueError, match="Вік не може бути меншим за 0."):
        AgeVerifier.is_adult(-5)
