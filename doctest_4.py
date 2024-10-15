# Завдання 4. Тестування з використанням doctest

# Додайте документацію з прикладами використання та напишіть тести з використанням doctest. Напишіть функції для роботи з числами:

# is_even(n: int) -> bool: перевіряє, чи є число парним.
# factorial(n: int) -> int: повертає факторіал числа.

def is_even(n: int) -> bool:
    """
    Перевіряє, чи є число парним.

    >>> is_even(2)
    True
    >>> is_even(3)
    False
    >>> is_even(0)
    True
    >>> is_even(-4)
    True
    >>> is_even(-5)
    False
    """
    return n % 2 == 0

def factorial(n: int) -> int:
    """
    Повертає факторіал числа. Якщо число менше 0, викликає ValueError.

    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(3)
    6
    >>> factorial(-1)
    Traceback (most recent call last):
    ...
    ValueError: Факторіал визначений лише для невід'ємних чисел.
    """
    if n < 0:
        raise ValueError("Факторіал визначений лише для невід'ємних чисел.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
