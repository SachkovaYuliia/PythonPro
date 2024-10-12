# Реалізуйте декоратор log_methods, який додається до класу і логуватиме виклики всіх його методів (назва методу та аргументи).

def log_methods(cls):
    """
    Декоратор, що логуватиме виклики всіх методів класу.

    """
    class WrappedClass(cls):
        def __getattribute__(self, name):
            """
            Перехоплює доступ до атрибутів класу і логує виклики методів.

            """
            attr = super().__getattribute__(name)


            if callable(attr):
                def wrapper(*args, **kwargs):
                    print(f"Logging: {name} called with {args}, {kwargs}")
                    return attr(*args, **kwargs)
                return wrapper
            return attr

    return WrappedClass


@log_methods
class MyClass:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


obj = MyClass()
print(obj.add(5, 3))      
print(obj.subtract(5, 3)) 
