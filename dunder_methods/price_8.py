# 1.	Реалізуйте клас Price, що представляє ціну товару з можливістю заокруглення до двох десяткових знаків. Додайте методи для додавання, віднімання та порівняння цін.

# 2.	Поміркуйте, як клас Price може бути використаний в майбутньому класі PaymentGateway для обробки фінансових транзакцій.

class Price:
    """
    Клас для представлення ціни товару.

    """

    def __init__(self, amount):
        """
        Ініціалізує об'єкт класу Price.

        """
        self.amount = round(float(amount), 2)

    def __add__(self, other):
        """
        Додає дві ціни.

        """
        return Price(self.amount + other.amount)

    def __sub__(self, other):
        """
        Віднімає одну ціну від іншої.

        """
        return Price(self.amount - other.amount)

    def __eq__(self, other):
        """
        Порівнює дві ціни на рівність.

        """
        return self.amount == other.amount

    def __lt__(self, other):
        """
        Перевіряє, чи є ця ціна меншою за іншу.

        """
        return self.amount < other.amount

    def __repr__(self):
        """
        Повертає рядкове представлення ціни.

        """
        return f"${self.amount:.2f}"


price1 = Price(10.255)
price2 = Price(5.50)


result_add = price1 + price2
print(f"{price1} + {price2} = {result_add}")


result_sub = price1 - price2
print(f"{price1} - {price2} = {result_sub}")


print(f"Чи {price1} дорівнює {price2}? {'Так' if price1 == price2 else 'Ні'}")
print(f"Чи {price1} менше за {price2}? {'Так' if price1 < price2 else 'Ні'}")
