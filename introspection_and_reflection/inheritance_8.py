# Напишіть функцію analyze_inheritance(cls), яка приймає клас, аналізує його спадкування та виводить усі методи, які він наслідує від базових класів.

import inspect

def analyze_inheritance(cls):
    """
    Аналізує клас на предмет успадкованих методів від базових класів.

    """
    base_classes = cls.__bases__
    
    if not base_classes:
        print(f"Клас {cls.__name__} не має базових класів.")
        return
    
    print(f"Клас {cls.__name__} наслідує:")
    
    for base_class in base_classes:
        base_methods = inspect.getmembers(base_class, predicate=inspect.isfunction)
        
        for method_name, method in base_methods:
            if method_name not in cls.__dict__:
                print(f"- {method_name} з {base_class.__name__}")

class Parent:
    def parent_method(self):
        pass

class Child(Parent):
    def child_method(self):
        pass

analyze_inheritance(Child)
