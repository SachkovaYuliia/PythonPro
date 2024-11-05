# Задача 3: підрахунок суми чисел у великому масиві
# Створіть програму, яка ділить великий масив чисел на кілька частин і рахує суму кожної частини паралельно в різних процесах. Використовуйте модуль multiprocessing.

from multiprocessing import Pool
import numpy as np

"""
Генеруємо великий масив чисел
"""
large_array = np.random.randint(1, 100, size=10**6)  

def partial_sum(arr):
    """
    Функція для обчислення суми частини масиву
    """
    return sum(arr)


if __name__ == "__main__":
    num_processes = 4
    
    """
    Ділимо масив на частини
    """
    chunk_size = len(large_array) // num_processes
    chunks = [large_array[i:i + chunk_size] for i in range(0, len(large_array), chunk_size)]
    
    with Pool(processes=num_processes) as pool:
        partial_sums = pool.map(partial_sum, chunks)
    
    total_sum = sum(partial_sums)
    
    print(f"Загальна сума: {total_sum}")
