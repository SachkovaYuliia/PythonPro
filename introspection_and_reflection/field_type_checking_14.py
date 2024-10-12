# Реалізуйте метаклас TypeCheckedMeta, який перевіряє типи атрибутів при їх встановленні. Якщо тип значення не відповідає типовому опису, має виникати помилка.

class TypeCheckedMeta(type):
    """
    Метаклас, який перевіряє типи атрибутів під час їх встановлення.
    """
    def __new__(cls, name, bases, class_dict):
        annotations = class_dict.get('__annotations__', {})

        for attr_name, attr_type in annotations.items():
            default_value = class_dict.get(attr_name, None)

            class_dict[attr_name] = cls._create_property(attr_name, attr_type, default_value)

        return super().__new__(cls, name, bases, class_dict)

    @staticmethod
    def _create_property(attr_name, attr_type, default_value):
        """
        Створює властивість (property) з логікою перевірки типу для атрибута.
        """
        private_name = f"_{attr_name}"

        def getter(self):
            return getattr(self, private_name, default_value)

        def setter(self, value):
            if not isinstance(value, attr_type):
                raise TypeError(f"Для атрибута '{attr_name}' очікується тип '{attr_type.__name__}', "
                                f"але отримано '{type(value).__name__}'")
            setattr(self, private_name, value)

        return property(getter, setter)

class Person(metaclass=TypeCheckedMeta):
    name: str = ""
    age: int = 0

p = Person()

p.name = "John"  
print(p.name)    

try:
    p.age = "30" 
except TypeError as e:
    print(e)  

