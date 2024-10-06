# 3. Збір статистики про зображення

# У вас є каталог з великою кількістю зображень. Напишіть ітератор, який по черзі відкриває кожне зображення (наприклад, за допомогою модуля PIL), витягує з нього метадані (розмір, формат тощо) і зберігає ці дані у файл CSV.

import os
import csv
from PIL import Image

class ImageMetadataIterator:


    def __init__(self, directory, csv_filename):
     
        self.directory = directory #Шлях до каталогу із зображеннями.
        self.csv_filename = csv_filename #Назва CSV-файлу для запису метаданих.
        self.image_files = [f for f in os.listdir(directory) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff'))] #Можливі рожширення файлів.
        self.index = 0

    def __iter__(self):

        return self

    def __next__(self):

        if self.index >= len(self.image_files):
            raise StopIteration

        image_file = self.image_files[self.index]
        image_path = os.path.join(self.directory, image_file)

        try:
            with Image.open(image_path) as img:
                metadata = {
                    'filename': image_file,
                    'format': img.format,
                    'size': img.size,  
                    'mode': img.mode
                }
                self.index += 1
                return metadata #Знаходимо та повертаємо дані наступного зображеня в папці.
        except Exception as e:
            print(f"Помилка під час обробки файлу {image_file}: {e}")
            self.index += 1
            return self.__next__()  # Пропускаємо зображення з помилкою.

    def save_metadata_to_csv(self):

        with open(self.csv_filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['filename', 'format', 'size', 'mode']) #Записуємо всі метадані зображень у CSV-файл.
            writer.writeheader()
            for metadata in self:
                writer.writerow(metadata)


def main():
    
    image_directory = 'images' # Вказуємо шлях до каталогу з зображеннями.
    
    csv_filename = 'image_metadata.csv' # Присвоюємо ім'я CSV-файлу для збереження метаданих.
    
    image_iterator = ImageMetadataIterator(image_directory, csv_filename)    # Створюємо ітератор.
    image_iterator.save_metadata_to_csv()     # Зберігаємо метадані у CSV файлі.
    print(f"Метадані зображень збережено у {csv_filename}.")     # Виводимо повідомлення щодо збереження метаданих.


if __name__ == "__main__":
    main()
