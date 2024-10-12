# Реалізуйте метаклас AutoMethodMeta, який автоматично генерує методи геттера та сеттера для кожного атрибута класу. Метод повинен починатися з get_<attribute>() та set_<attribute>(value).

class AutoMethodMeta(type):
    """
    Метаклас, що автоматично створює методи get_<attribute> та set_<attribute>
    для кожного атрибута класу.
    """
    def __new__(cls, name, bases, class_dict):
        attributes = [attr_name for attr_name in class_dict if not attr_name.startswith('__')]

        for attr_name in attributes:
            class_dict[f'get_{attr_name}'] = cls._create_getter(attr_name)
            class_dict[f'set_{attr_name}'] = cls._create_setter(attr_name)

        return super().__new__(cls, name, bases, class_dict)

    @staticmethod
    def _create_getter(attr_name):
        """
        Створює метод геттера для атрибута.
        """
        def getter(self):
            return getattr(self, attr_name)
        return getter

    @staticmethod
    def _create_setter(attr_name):
        """
        Створює метод сеттера для атрибута.

        """
        def setter(self, value):
            setattr(self, attr_name, value)
        return setter


class Person(metaclass=AutoMethodMeta):
    name = "John"
    age = 30

p = Person()
print(p.get_name())  
p.set_age(31)
print(p.get_age())   
