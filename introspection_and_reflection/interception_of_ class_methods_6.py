# Напишіть клас Proxy, який приймає на вхід об'єкт і переадресовує виклики методів цього об'єкта, додатково логуючи виклики (наприклад, виводячи назву методу та аргументи).

class Proxy:


    def __init__(self, obj):
        """
        Ініціалізує проксі з переданим об'єктом.

        """
        self._obj = obj

    def __getattr__(self, name):
        """
        Переадресовує виклик методу об'єкта та логує його.

        """
        attr = getattr(self._obj, name)

        if callable(attr):
            def wrapper(*args, **kwargs):
                print(f"Calling method:\n{name} with args: {args}, kwargs: {kwargs}")
                return attr(*args, **kwargs)
            return wrapper
        else:
            return attr


class MyClass:
    def greet(self, name):
        return f"Hello, {name}!"


obj = MyClass()
proxy = Proxy(obj)


print(proxy.greet("Alice"))
