# Реалізуйте метаклас LimitedAttributesMeta, який дозволяє класам мати лише фіксовану кількість атрибутів (наприклад, максимум 3). Якщо додати більше атрибутів, має виникати помилка.

class LimitedAttributesMeta(type):
    """
    Метаклас, що обмежує кількість атрибутів класу до заданої кількості.
    Якщо кількість атрибутів перевищує ліміт, викликається помилка TypeError.
    """
    MAX_ATTRIBUTES = 3 

    def __new__(cls, name, bases, class_dict):
        actual_attributes = [key for key in class_dict if not key.startswith('__')]
        
        if len(actual_attributes) > cls.MAX_ATTRIBUTES:
            raise TypeError(f"Клас {name} не може мати більше {cls.MAX_ATTRIBUTES} атрибутів.")

        return super().__new__(cls, name, bases, class_dict)


class LimitedClass(metaclass=LimitedAttributesMeta):
    attr1 = 1
    attr2 = 2
    attr3 = 3
    attr4 = 4 


obj = LimitedClass()  
