# Задача 2: паралельна обробка зображень
# Напишіть програму, яка обробляє кілька зображень одночасно (наприклад, змінює їх розмір або застосовує фільтр). Використовуйте модуль concurrent.futures і виконуйте обробку зображень у кількох процесах або потоках.

# Підказка: можна використовувати бібліотеку Pillow для обробки зображень.

from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import os

input_folder = "input_images"    
output_folder = "output_images" 

os.makedirs(output_folder, exist_ok=True)

"""Налаштовуємо нові розміри для кожного зображення
"""
image_sizes = {
    "file1.jpg": (200, 200),    
    "file2.jpg": (200, 200),   
    "file3.jpg": (200, 300),    
}


def process_image(filename):

    """
    Функція для обробки зображення
    """
    try:
        img_path = os.path.join(input_folder, filename)
        with Image.open(img_path) as img:
            new_size = image_sizes.get(filename, (800, 800))  
            
            img_resized = img.resize(new_size)
            
            output_path = os.path.join(output_folder, f"resized_{filename}")
            img_resized.save(output_path)
        
        print(f"{filename} оброблено та збережено як {output_path} з новим розміром {new_size}")
    
    except Exception as e:
        print(f"Помилка під час обробки {filename}: {e}")

image_files = ["file1.jpg", "file2.jpg", "file3.jpg"]

"""
Використання ThreadPoolExecutor для паралельної обробки зображень
"""
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(process_image, image_files)

print("Обробка всіх зображень завершена")
