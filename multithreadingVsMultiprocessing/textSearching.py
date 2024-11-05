# Задача 5: паралельний пошук у файлах
# Реалізуйте програму, яка шукає певний текст у кількох великих файлах одночасно, використовуючи потоки або процеси. Для кожного файлу створіть окремий потік або процес.

from concurrent.futures import ThreadPoolExecutor
import os

files = ["file1.txt", "file2.txt", "file3.txt"]

search_text = "testtesttest"

def search_in_file(filename, search_text):
    results = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                if search_text in line:
                    results.append((line_number, line.strip()))
    except Exception as e:
        print(f"Помилка при обробці файлу {filename}: {e}")
    return filename, results


def parallel_search(files, search_text):
    """Основна функція для паралельного пошуку"""
    with ThreadPoolExecutor(max_workers=len(files)) as executor:
        futures = [executor.submit(search_in_file, file, search_text) for file in files]
        
        for future in futures:
            filename, results = future.result()
            print(f"\n Результати для файлу '{filename}':")
            if results:
                for line_number, line in results:
                    print(f"Рядок {line_number}: {line}")
            else:
                print("Текст не знайдено")

if __name__ == "__main__":
    parallel_search(files, search_text)
