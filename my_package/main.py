from math_utils import factorial
from string_utils import maximum_common_divisor

n = int(input("Введіть число для обчислення факторіала: "))
print(f"Факторіал числа {n} дорівнює {factorial(n)}")

a = int(input("Введіть перше число для обчислення найбільшого спільного дільника: "))
b = int(input("Введіть друге число для обчислення найбільшого спільного дільника: "))
print(f"Найбільший спільний дільник чисел {a} і {b} дорівнює {maximum_common_divisor(a, b)}")