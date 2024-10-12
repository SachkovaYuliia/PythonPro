# 1.	Створіть клас Vector, який представляє вектор у просторі з n вимірами. Додайте методи для додавання, віднімання векторів та обчислення скалярного добутку. Використовуйте dunder-методи (__add__, __sub__, __mul__).

# 2.	Додайте можливість порівняння двох векторів за їх довжиною.

import math

class Vector:
    """
    Клас для представлення вектора у просторі з n вимірами.

    """

    def __init__(self, *components):
        """
        Ініціалізує об'єкт класу Vector.

        """
        self.components = components

    def __add__(self, other):
        """
        Додає два вектори.

        """
        if len(self.components) != len(other.components):
            raise ValueError("Вектори повинні мати однакову кількість компонентів.")
        new_components = tuple(a + b for a, b in zip(self.components, other.components))
        return Vector(*new_components)

    def __sub__(self, other):
        """
        Віднімає два вектори.

        """
        if len(self.components) != len(other.components):
            raise ValueError("Вектори повинні мати однакову кількість компонентів.")
        new_components = tuple(a - b for a, b in zip(self.components, other.components))
        return Vector(*new_components)

    def __mul__(self, scalar):
        """
        Обчислює скалярний добуток вектора на скаляр.

        """
        if not isinstance(scalar, (int, float)):
            raise ValueError("Скаляр має бути числом.")
        new_components = tuple(a * scalar for a in self.components)
        return Vector(*new_components)

    def __eq__(self, other):
        """
        Перевіряє, чи є два вектори рівними.

        """
        return self.components == other.components

    def __lt__(self, other):
        """
        Порівнює довжини двох векторів.

        """
        return self.length() < other.length()

    def length(self):
        """
        Обчислює довжину вектора.

        """
        return math.sqrt(sum(a ** 2 for a in self.components))

    def __repr__(self):
        """
        Повертає вектор.

        """
        return f"Vector{self.components}"


vec1 = Vector(1, 2, 3)
vec2 = Vector(4, 5, 6)


result_add = vec1 + vec2
print(f"{vec1} + {vec2} = {result_add}")


result_sub = vec1 - vec2
print(f"{vec1} - {vec2} = {result_sub}")


result_mul = vec1 * 3
print(f"{vec1} * 3 = {result_mul}")


print(f"Довжина {vec1} = {vec1.length()}")


print(f"Чи довжина {vec1} менша за довжину {vec2}? {'Так' if vec1 < vec2 else 'Ні'}")
