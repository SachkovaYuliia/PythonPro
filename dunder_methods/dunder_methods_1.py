# 1.	Реалізуйте клас Fraction (дробові числа), який має методи для додавання, віднімання, множення та ділення двох об'єктів цього класу. Використайте спеціальні методи __add__, __sub__, __mul__, __truediv__.

# 2.	Реалізуйте метод __repr__, щоб можна було коректно виводити об'єкти цього класу у форматі "numerator/denominator".

import math

class Fraction:
    """
    Клас для представлення дробових чисел з можливістю виконання
    арифметичних операцій (додавання, віднімання, множення, ділення).
    """

    def __init__(self, numerator, denominator):
        """
        Ініціалізує дробове число.

        """
        if denominator == 0:
            raise ValueError("На ноль ділити не можна")
        self.numerator = numerator
        self.denominator = denominator
        self._reduce()

    def _reduce(self):
        """
        Зменшує дробове число до найменшого виразу.

        """
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __add__(self, other):
        """
        Додає два дроби.

        """
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """
        Віднімає два дроби.

        """
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """
        Множить два дроби.

        """
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        """
        Ділить два дроби.

        """
        if other.numerator == 0:
            raise ZeroDivisionError("На ноль ділити не можна")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __repr__(self):
        """
        Повертає рядкове представлення дробу.

        """
        return f"{self.numerator}/{self.denominator}"


frac1 = Fraction(1, 2)  
frac2 = Fraction(3, 4)  

print(f"{frac1} + {frac2} = {frac1 + frac2}")
print(f"{frac1} - {frac2} = {frac1 - frac2}")
print(f"{frac1} * {frac2} = {frac1 * frac2}")
print(f"{frac1} / {frac2} = {frac1 / frac2}")