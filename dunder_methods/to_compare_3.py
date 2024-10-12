# 1.	Реалізуйте клас Person із параметрами name та age. Додайте методи для порівняння за віком (__lt__, __eq__, __gt__).

# 2.	Напишіть програму для сортування списку об'єктів класу Person за віком.

class Person:
    """
    Клас для представлення особи із параментрами: ім'я та вік.

    """

    def __init__(self, name, age):
        """
        Ініціалізує об'єкт класу Person.

        """
        self.name = name
        self.age = age

    def __lt__(self, other):
        """
        Порівнює вік цієї особи з віком іншої.

        """
        return self.age < other.age

    def __eq__(self, other):
        """
        Перевіряє, чи є вік цієї особи рівним віку іншої особи.

        """
        return self.age == other.age

    def __gt__(self, other):
        """
        Порівнює вік цієї особи з віком іншої.

        """
        return self.age > other.age

    def __repr__(self):
        """
        Повертає інформацію.

        """
        return f"Person(name='{self.name}', age={self.age})"


people = [
    Person("Антон", 18),
    Person("Василь", 28),
    Person("Марина", 38),
    Person("Ольга", 48)
]


sorted_people = sorted(people)


print("Список людей, відсортований за віком:")
for person in sorted_people:
    print(person)
