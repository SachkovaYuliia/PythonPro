# Реалізуйте клас Product, який представляє товар з наступними атрибутами:

# 1.	name – назва товару (рядок).

# 2.	price – ціна товару (число з плаваючою комою).

# Вам потрібно реалізувати три варіанти роботи з атрибутом price:

# 1.	Сеттери/геттери: реалізуйте методи get_price() і set_price(), які будуть дозволяти отримувати та встановлювати значення атрибута price. Додайте перевірку, що ціна не може бути від'ємною. Якщо ціна менше 0, викиньте виняток ValueError.

class ProductWithGetSet:
    def __init__(self, name, price):
        self.name = name
        self.set_price(price)

    def get_price(self):
        """Отримує ціну товару."""
        return self._price

    def set_price(self, price):
        """Встановлює ціну товару, якщо вона не менша за 0."""
        if price < 0:
            raise ValueError("Ціна не може бути від'ємною")
        self._price = price

    price = property(get_price, set_price)  


# 2.	Декоратор @property: використайте декоратор @property для створення властивості price. Також реалізуйте перевірку на від'ємне значення ціни.

class ProductWithProperty:
    def __init__(self, name, price):
        self.name = name
        self.price = price  

    @property
    def price(self):
        """Отримує ціну товару."""
        return self._price

    @price.setter
    def price(self, value):
        """Встановлює ціну товару, якщо вона не менша за 0."""
        if value < 0:
            raise ValueError("Ціна не може бути від'ємною")
        self._price = value



# 3.	Дескриптори: створіть окремий клас дескриптора PriceDescriptor, який буде контролювати встановлення та отримання ціни. Додайте до класу Product атрибут price, що використовує дескриптор для перевірки ціни.

# Завдання:

# 1.	Реалізуйте всі три класи: ProductWithGetSet, ProductWithProperty та ProductWithDescriptor.

class PriceDescriptor:
    """Дескриптор для контролю атрибута ціни."""

    def __init__(self):
        self._price = 0

    def __get__(self, instance, owner):
        """Отримує значення ціни."""
        return self._price

    def __set__(self, instance, value):
        """Встановлює ціну, якщо вона не менша за 0."""
        if value < 0:
            raise ValueError("Ціна не може бути від'ємною")
        self._price = value


class ProductWithDescriptor:
    price = PriceDescriptor()

    def __init__(self, name, price):
        self.name = name
        self.price = price  



# 2.	Напишіть тестову програму, яка створює об'єкти кожного з цих класів та намагається:

# o	Отримати та змінити ціну товару.

# o	Встановити від'ємне значення ціни та впевнитись, що воно правильно обробляється (викидання ValueError).

def test_product_classes():

    print("Тестування ProductWithGetSet:")
    product1 = ProductWithGetSet("Товар 1", 100)
    print(f"Назва: {product1.name}, Ціна: {product1.get_price()}")

    product1.set_price(150)
    print(f"Оновлена ціна: {product1.get_price()}")

    try:
        product1.set_price(-50)
    except ValueError as e:
        print(e)

    print("\n Тестування ProductWithProperty:")
    product2 = ProductWithProperty("Товар 2", 200)
    print(f"Назва: {product2.name}, Ціна: {product2.price}")

    product2.price = 250
    print(f"Оновлена ціна: {product2.price}")

    try:
        product2.price = -100
    except ValueError as e:
        print(e)

    print("\n Тестування ProductWithDescriptor:")
    product3 = ProductWithDescriptor("Товар 3", 300)
    print(f"Назва: {product3.name}, Ціна: {product3.price}")

    product3.price = 350
    print(f"Оновлена ціна: {product3.price}")

    try:
        product3.price = -200
    except ValueError as e:
        print(e)


test_product_classes()


# 3.	Порівняйте переваги та недоліки кожного з підходів (сеттери/геттери, @property, дескриптори). Напишіть висновок, який підхід більш зручний у вашому випадку та чому.

# Додаткове завдання (опціонально):

# 4.	Для класу з дескриптором додайте можливість встановлення значень ціни в євро або доларах (через додатковий атрибут валюти), використовуючи ще один дескриптор для конвертації валют.


class CurrencyDescriptor:
    """Дескриптор для обробки валюти та конвертації."""
    
    def __init__(self):
        self._currency = "USD" 
        self.conversion_rates = {
            "USD": 1.0,
            "EUR": 0.85,
        }

    def __get__(self, instance, owner):
        return self._currency

    def __set__(self, instance, value):
        if value not in self.conversion_rates:
            raise ValueError("Вказана валюта не підтримується")
        self._currency = value


class ProductWithCurrencyDescriptor:
    price = PriceDescriptor()
    currency = CurrencyDescriptor()

    def __init__(self, name, price, currency="USD"):
        self.name = name
        self.price = price 
        self.currency = currency  


def test_product_with_currency_descriptor():
    print("\n Тестування ProductWithCurrencyDescriptor:")
    product4 = ProductWithCurrencyDescriptor("Товар 4", 400, "USD")
    print(f"Назва: {product4.name}, Ціна: {product4.price}, Валюта: {product4.currency}")


    product4.currency = "EUR"
    print(f"Оновлена валюта: {product4.currency}")

    try:
        product4.currency = "GBP"
    except ValueError as e:
        print(e)


test_product_with_currency_descriptor()
