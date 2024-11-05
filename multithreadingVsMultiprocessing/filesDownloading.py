# Задача 1: завантаження файлів із мережі
# Створіть програму, яка завантажує кілька файлів із мережі одночасно за допомогою потоків. Ваша програма повинна використовувати модуль threading для створення декількох потоків, кожен з яких відповідає за завантаження окремого файлу.

# Підказка: використайте бібліотеки requests або urllib для завантаження файлів.

import threading
import requests

def download_file(url, filename):

    """
    Функція для завантаження файлу
    """
    try:
        print(f"Завантаження {url} в файл {filename}")
        response = requests.get(url, stream=True)
        response.raise_for_status()  
        
        """
        Записуємо вміст файлу частинами
        """
        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"Завантаження {filename} завершено")
    
    except requests.RequestException as e:
        print(f"Помилка під час завантаження {url}: {e}")

urls = [
    ("https://picsum.photos/200/300", "file1.jpg"),
    ("https://picsum.photos/200/300", "file2.jpg"),
    ("https://picsum.photos/200", "file3.jpg"),
]

"""
Створюємо та запускаємо потоки для кожного файлу
"""
threads = []
for url, filename in urls:
    thread = threading.Thread(target=download_file, args=(url, filename))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Завантаження всіх файлів завершено")
