# 6. Ітерація через файли в каталозі
# Напишіть ітератор, який буде повертати всі файли в заданому каталозі по черзі. Для кожного файлу виведіть його назву та розмір.

import os

class DirectoryIterator:
    def __init__(self, directory):
        self.directory = directory
        self.files = os.listdir(directory)  # Отримуємо всі елементи в каталозі
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Перебираємо всі файли в каталозі
        while self.index < len(self.files):
            file_name = self.files[self.index]
            self.index += 1
            
            # Формуємо повний шлях до файлу
            file_path = os.path.join(self.directory, file_name)

            # Перевіряємо, чи є це файлом
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                return file_name, file_size

        # Якщо всі файли пройдені, StopIteration
        raise StopIteration

def main():
    # Запитуємо у користувача шлях до каталогу
    directory = input("Введіть шлях до каталогу: ")
    output_file = 'files_info.txt'  # Файл для збереження результатів

    # Перевіряємо, чи існує вказаний каталог
    if not os.path.isdir(directory):
        print("Вказаний шлях не є дійсним каталогом.")
        return

    iterator = DirectoryIterator(directory)

    # Відкриваємо файл для запису
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Назва файлу, Розмір (байт)\n")  # Записуємо заголовок

        # Ітеруємо через файли
        for file_name, file_size in iterator:
            print(f"Назва: {file_name}, Розмір: {file_size} байт")
            f.write(f"{file_name}, {file_size}\n")  # Записуємо дані у файл

    print(f"\n Дані про файли збережено у '{output_file}'.")

if __name__ == "__main__":
    main()
