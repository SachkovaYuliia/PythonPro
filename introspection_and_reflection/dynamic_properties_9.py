# Напишіть клас DynamicProperties, в якому можна динамічно додавати властивості через методи. Використовуйте вбудовані

# функції property() для створення геттера та сеттера під час виконання програми.


class DynamicProperties:
    def __init__(self):
        
        self._properties = {}

    def add_property(self, property_name, default_value=None):
        """
        Додає динамічну властивість з геттером та сеттером.

        """

        def getter(self):
            return self._properties.get(property_name, default_value)

        def setter(self, value):
            self._properties[property_name] = value

        prop = property(getter, setter)

        setattr(self.__class__, property_name, prop)


obj = DynamicProperties()

obj.add_property('name', 'default_name')

print(obj.name) 

obj.name = "Python"

print(obj.name)  
