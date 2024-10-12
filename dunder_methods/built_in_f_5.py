# 1.	Реалізуйте власну версію функцій len(), sum(), та min(). Використовуйте спеціальні методи __len__, __iter__, __getitem__, якщо необхідно.

# 2.	Напишіть тест для кожної з реалізованих функцій.

class MyCollection:
    """
    Клас MyCollection представляє колекцію даних та надає методи для взаємодії з ними.
    """

    def __init__(self, data):
        """
        Ініціалізує колекцію з переданими даними.

        """
        self.data = data

    def __len__(self):
        """
        Повертає кількість елементів у колекції.

        """
        return len(self.data)

    def __iter__(self):
        """
        Повертає ітератор для колекції.

        """
        return iter(self.data)
    
    def __getitem__(self, index):
        """
        Повертає елемент за індексом.

        """
        return self.data[index]


def my_len(collection):
    """
    Повертає кількість елементів у колекції.

    """
    return collection.__len__()

def my_sum(collection):
    """
    Обчислює суму елементів колекції.

    """
    total = 0
    for item in collection:
        total += item
    return total

def my_min(collection):
    """
    Знаходить мінімальний елемент колекції.

    """
    min_value = collection[0]
    for item in collection:
        if item < min_value:
            min_value = item
    return min_value


def test_my_len():
    """
    Тестує функцію my_len().

    """
    collection = MyCollection([1, 2, 3, 4, 5])
    assert my_len(collection) == 5, f"Очикувана length 5, але наявна {my_len(collection)}"
    print("my_len() is ok")

def test_my_sum():
    """
    Тестує функцію my_sum().

    """
    collection = MyCollection([1, 2, 3, 4, 5])
    assert my_sum(collection) == 15, f"Очикувана sum 15, але наявна {my_sum(collection)}"
    print("my_sum() is ok")

def test_my_min():
    """
    Тестує функцію my_min().

    """
    collection = MyCollection([5, 3, 8, 1, 4])
    assert my_min(collection) == 1, f"Очикуваний min 1, але наявний {my_min(collection)}"
    print("my_min() is ok")


test_my_len()
test_my_sum()
test_my_min()