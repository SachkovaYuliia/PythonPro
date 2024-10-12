# Створіть метаклас LoggingMeta, який автоматично додає логування при доступі до будь-якого атрибута класу. Кожен раз, коли атрибут змінюється або читається, повинно з'являтися повідомлення в консолі.

class LoggingMeta(type):
    """
    Метаклас, що додає логування при доступі та зміні атрибутів класу.
    Логує доступ (читання) і модифікацію атрибутів.
    
    """
    def __new__(cls, name, bases, class_dict):
        for key, value in class_dict.items():
            if not key.startswith('__') and not callable(value):
                class_dict[key] = cls._create_property(key)
        
        return super().__new__(cls, name, bases, class_dict)

    @staticmethod
    def _create_property(attr_name):
        """
        Створює властивість (property) з логуванням для читання і запису атрибута.

        """
        def getter(self):
            print(f"Logging: accessed '{attr_name}'")
            return self.__dict__.get(attr_name, None)
        
        def setter(self, value):
            print(f"Logging: modified '{attr_name}'")
            self.__dict__[attr_name] = value
        
        return property(getter, setter)

class MyClass(metaclass=LoggingMeta):
    def __init__(self, name):
        self.name = name

    def __setattr__(self, name, value):
        print(f"Logging: modified '{name}'")
        super().__setattr__(name, value)

    def __getattribute__(self, name):
        print(f"Logging: accessed '{name}'")
        return super().__getattribute__(name)


obj = MyClass("Python")
print(obj.name)  
obj.name = "New Python" 
