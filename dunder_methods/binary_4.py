# 1.	Реалізуйте клас BinaryNumber, який представляє двійкове число. Додайте методи для виконання двійкових операцій: AND (__and__), OR (__or__), XOR (__xor__) та NOT (__invert__).

# 2.	Напишіть тест для цих операцій.

class BinaryNumber:
    """
    Клас для представлення двійкового числа і виконання двійкових операцій.
    """

    def __init__(self, binary_str):
        """
        Ініціалізує об'єкт двійкового числа.

        """
        if not all(c in '01' for c in binary_str):
            raise ValueError("Invalid binary number")
        self.binary_str = binary_str

    def __and__(self, other):
        """
        Виконує двійкову операцію AND між двома двійковими числами.

        """
        return BinaryNumber(bin(int(self.binary_str, 2) & int(other.binary_str, 2))[2:])

    def __or__(self, other):
        """
        Виконує двійкову операцію OR між двома двійковими числами.

        """
        return BinaryNumber(bin(int(self.binary_str, 2) | int(other.binary_str, 2))[2:])

    def __xor__(self, other):
        """
        Виконує двійкову операцію XOR між двома двійковими числами.

        """
        return BinaryNumber(bin(int(self.binary_str, 2) ^ int(other.binary_str, 2))[2:])

    def __invert__(self):
        """
        Виконує двійкову операцію інверсії (~).

        """
        inverted_str = ''.join('1' if c == '0' else '0' for c in self.binary_str)
        return BinaryNumber(inverted_str)

    def __repr__(self):
        """
        Повертає рядкове представлення двійкового числа.

        """
        return f"BinaryNumber('{self.binary_str}')"


def test_binary_operations():
    """
    Тестує двійкові операції AND, OR, XOR та NOT (~).
    """
    bin1 = BinaryNumber("1010") 
    bin2 = BinaryNumber("1100")  

    # Операція AND
    result_and = bin1 & bin2
    print(f"{bin1} & {bin2} = {result_and}")

    # Операція OR
    result_or = bin1 | bin2
    print(f"{bin1} | {bin2} = {result_or}")

    # Операція XOR
    result_xor = bin1 ^ bin2
    print(f"{bin1} ^ {bin2} = {result_xor}")

    # Операція NOT (~)
    result_not = ~bin1
    print(f"~{bin1} = {result_not}")


test_binary_operations()