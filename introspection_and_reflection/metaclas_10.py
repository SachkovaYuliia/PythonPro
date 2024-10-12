# Реалізуйте метаклас SingletonMeta, який гарантує, що клас може мати лише один екземпляр (патерн Singleton). Якщо екземпляр класу вже створений, наступні виклики повинні повертати той самий об'єкт.

class SingletonMeta(type):
    """
    Метаклас, що забезпечує створення лише одного екземпляра класу.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Перевизначає виклик класу для контролю над створенням екземплярів.
        Якщо екземпляр вже існує, він повертається; якщо ні, створюється новий.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("Creating instance")


obj1 = Singleton()  
obj2 = Singleton()

print(obj1 is obj2)  
