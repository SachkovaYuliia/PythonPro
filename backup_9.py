# 9. Автоматичне резервне копіювання

# Напишіть менеджер контексту, який буде створювати резервну копію важливого файлу перед його обробкою. Якщо обробка пройде успішно, оригінальний файл замінюється новим. У разі помилки резервна копія автоматично відновлюється.

import os
import shutil

class BackupManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.backup_path = file_path + '.bak'

    def __enter__(self):
        # Створюємо резервну копію файлу
        shutil.copy2(self.file_path, self.backup_path)
        print(f"Резервна копія '{self.backup_path}' створена.")
        return self.file_path

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # Відновлюємо оригінальний файл, якщо сталася помилка
            shutil.copy2(self.backup_path, self.file_path)
            print(f"Помилка при обробці файлу. Відновлено '{self.file_path}' з резервної копії.")
        else:
            # Якщо все пройшло успішно, видаляємо резервну копію
            os.remove(self.backup_path)
            print(f"Обробка пройшла успішно. Резервна копія '{self.backup_path}' видалена.")


def process_file(file_path):

    print(f"Обробка файлу: {file_path}")
    
    # Додаємо новий рядок до файлу
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write("\nДодано новий рядок.")

def main():
    file_path = 'important_file.txt'

    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("Це важливий файл.\n")

    try:
        with BackupManager(file_path) as managed_file:
            process_file(managed_file)
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    main()
