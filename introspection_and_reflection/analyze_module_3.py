# Напишіть програму, яка приймає на вхід назву модуля (рядок) та виводить список усіх класів, функцій та їхніх сигнатур у модулі. Використовуйте модуль inspect.

import inspect
import importlib

def analyze_module(module_name):
    """
    Аналізує модуль та виводить усі класи, функції та їх сигнатури.
    
    """
    
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        print(f"Модуль з назвою '{module_name}' не знайдено.")
        return

    functions = inspect.getmembers(module, inspect.isfunction)

    classes = inspect.getmembers(module, inspect.isclass)

    print("Функції:")
    if functions:
        for func_name, func in functions:
            signature = inspect.signature(func)
            print(f"- {func_name}{signature}")
    else:
        print("- <немає функцій у модулі>")

    print("\n Класи:")
    if classes:
        for class_name, cls in classes:
            print(f"- {class_name}")
      
            methods = inspect.getmembers(cls, inspect.isfunction)
            for method_name, method in methods:
                method_signature = inspect.signature(method)
                print(f"   - {method_name}{method_signature}")
    else:
        print("- <немає класів у модулі>")


analyze_module("math")
