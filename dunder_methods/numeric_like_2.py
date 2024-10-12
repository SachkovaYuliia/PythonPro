# 1.	Реалізуйте клас Vector, що підтримує операції додавання, віднімання, множення на число та порівняння за довжиною. Використовуйте відповідні dunder-методи (__add__, __sub__, __mul__, __lt__, __eq__).

# 2.	Додайте до класу метод для отримання довжини вектора.

import math

class Vector:
    """
    Клас для представлення векторів.
    Підтримує операції додавання, віднімання, множення на число та порівняння за довжиною.

    """

    def __init__(self, *components):
        """
        Ініціалізує вектор.

        """
        self.components = components

    def __add__(self, other):
        """
        Додає два вектори.

        """
        if len(self.components) != len(other.components):
            raise ValueError("Вектори мають мати однакову кількість компонентів.")
        new_components = tuple(a + b for a, b in zip(self.components, other.components))
        return Vector(*new_components)

    def __sub__(self, other):
        """
        Віднімає два вектори.

        """
        if len(self.components) != len(other.components):
            raise ValueError("Вектори мають мати однакову кількість компонентів.")
        new_components = tuple(a - b for a, b in zip(self.components, other.components))
        return Vector(*new_components)

    def __mul__(self, scalar):
        """
        Множить вектор на скалярне число.

        """
        if not isinstance(scalar, (int, float)):
            raise ValueError("Скалярна величина має бути числом")
        new_components = tuple(a * scalar for a in self.components)
        return Vector(*new_components)

    def __eq__(self, other):
        """
        Перевіряє, чи рівні два вектори.

        """
        return self.components == other.components

    def __lt__(self, other):
        """
        Порівнює довжини двох векторів.

        """
        return self.length() < other.length()

    def length(self):
        """
        Обчислює модуль довжини вектора.

        """
        return math.sqrt(sum(a ** 2 for a in self.components))

    def __repr__(self):
        """
        Повертає вектор.

        """
        return f"Vector{self.components}"



vec1 = Vector(1, 2, 3)
vec2 = Vector(4, 5, 6)


print(f"{vec1} + {vec2} = {vec1 + vec2}")
print(f"{vec1} - {vec2} = {vec1 - vec2}")
print(f"{vec1} * 3 = {vec1 * 3}")
print(f"Length of {vec1} = {vec1.length()}")
print(f"Is {vec1} shorter than {vec2}? {'Yes' if vec1 < vec2 else 'No'}")


vec3 = Vector(1, 2, 3)
print(f"Is {vec1} equal to {vec3}? {'Yes' if vec1 == vec3 else 'No'}")
