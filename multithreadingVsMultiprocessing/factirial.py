# Задача 7: обчислення факторіалу великих чисел
# Напишіть програму, яка обчислює факторіал великого числа за допомогою декількох потоків або процесів, розподіляючи обчислення між ними.

from concurrent.futures import ProcessPoolExecutor

# Функція для обчислення факторіала у визначеному діапазоні
def partial_factorial(start, end):
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result


def process_range(rng):
    """
    Функція, що обробляє пару значень (start, end)
    """
    return partial_factorial(rng[0], rng[1])


def parallel_factorial(n, num_workers=4):
    """
    Основна функція для обчислення факторіала великого числа паралельно
    """
    step = n // num_workers
    ranges = [(i * step + 1, (i + 1) * step) for i in range(num_workers)]
    
    if ranges[-1][1] < n:
        ranges[-1] = (ranges[-1][0], n)
    
  
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        """
        Виконуємо паралельне обчислення часткових факторіалів
        """
        partial_results = list(executor.map(process_range, ranges))
    
    final_result = 1
    for part in partial_results:
        final_result *= part
    
    return final_result

if __name__ == "__main__":
    n = 9
    result = parallel_factorial(n, num_workers=8)
    print(f"Факторіал числа {n} дорівнює: {result}")
