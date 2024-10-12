# Напишіть функцію analyze_object(obj), яка приймає будь-який об'єкт та виводить: 

# Тип об'єкта.
# Список всіх методів та атрибутів об'єкта.
# Тип кожного атрибута.

def analyze_object(obj):
    """
    Аналізує будь-який об'єкт та виводить: 

    # Тип об'єкта.
    # Список всіх методів та атрибутів об'єкта.
    # Тип кожного атрибута.

    """
    
  
    print(f"Тип об'єкта: {type(obj)}\n")
    

    attributes_and_methods = dir(obj)
    
    print("Методи та атрибути:")
    

    for attr in attributes_and_methods:

        if not attr.startswith('__'):

            attribute = getattr(obj, attr)

            print(f"- {attr}: {type(attribute)}")


class MyClass:
    def __init__(self, value):
        self.value = value

    def say_hello(self):
        return f"Hello, {self.value}"


obj = MyClass("World")
analyze_object(obj)
