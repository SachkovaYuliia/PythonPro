# Напишіть клас MutableClass, який має методи для динамічного додавання та видалення атрибутів об'єкта. Реалізуйте методи add_attribute(name, value) та remove_attribute(name).

class MutableClass:
    """
    Клас, що дозволяє динамічно додавати та видаляти атрибути об'єкта.
    """
    
    def add_attribute(self, name, value):
        """
        Додає атрибут до об'єкта.

        """
        setattr(self, name, value)
    
    def remove_attribute(self, name):
        """
        Видаляє атрибут з об'єкта, якщо він існує.
        """
        if hasattr(self, name):
            delattr(self, name)
        else:
            raise AttributeError(f"Attribute '{name}' does not exist.")



obj = MutableClass()


obj.add_attribute("name", "Python")
print(obj.name)  


obj.remove_attribute("name")
