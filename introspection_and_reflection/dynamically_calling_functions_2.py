# Реалізуйте функцію call_function(obj, method_name, *args), яка приймає об'єкт, назву методу в вигляді рядка та довільні аргументи для цього методу. Функція повинна викликати відповідний метод об'єкта і повернути результат.

def call_function(obj, method_name, *args):
    """
    Викликає метод об'єкта  за назвою та передає йому довільні аргументи.

    """
    
    method = getattr(obj, method_name, None)
    

    if method is None or not callable(method):
        raise AttributeError(f"Об'єкт не має методу з назвою '{method_name}'")
    

    return method(*args)


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


calc = Calculator()
print(call_function(calc, "add", 10, 5))       
print(call_function(calc, "subtract", 10, 5))  
