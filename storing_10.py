# 10. Архівування та зберігання великих даних

# Реалізуйте менеджер контексту для архівування файлів (за допомогою модуля zipfile). Менеджер автоматично створює архів, додає файли, а після виходу з блоку with – завершує архівування та закриває архів.

import os
import zipfile

class ZipArchiver:
    def __init__(self, archive_name):
        self.archive_name = archive_name
        self.zipf = None

    def __enter__(self):
        # Створюємо ZIP-архів
        self.zipf = zipfile.ZipFile(self.archive_name, 'w', zipfile.ZIP_DEFLATED)
        print(f"Архів '{self.archive_name}' створено.")
        return self

    def add_file(self, file_path):
        # Додаємо файл до архіву
        if os.path.isfile(file_path):
            self.zipf.write(file_path, os.path.basename(file_path))
            print(f"Файл '{file_path}' додано до архіву.")
        else:
            print(f"Файл '{file_path}' не знайдено!")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.zipf:
            self.zipf.close()
            print(f"Архів '{self.archive_name}' закрито.")


def main():
    archive_name = 'my_archive.zip'
    files_to_archive = ['file1.txt', 'file2.txt', 'file3.txt']  # Список файлів для архівування

    # Створюємо тестові файли
    for file_name in files_to_archive:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(f"Це вміст файлу {file_name}.\n")

    # Використовуємо менеджер контексту для архівування файлів
    with ZipArchiver(archive_name) as archiver:
        for file_name in files_to_archive:
            archiver.add_file(file_name)

if __name__ == "__main__":
    main()
