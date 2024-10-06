# 7. Парсинг великих лог-файлів для аналітики

# Уявіть, що у вас є великий лог-файл від веб-сервера. Створіть генератор, який зчитує файл порціями (по рядку) і повертає тільки рядки з помилками (код статусу 4XX або 5XX). Запишіть ці помилки в окремий файл для подальшого аналізу.

def error_log_generator(file_path):
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if ' 4' in line or ' 5' in line:  # Перевіряємо на коди статусу 4XX та 5XX
                yield line.strip()

def main():
    log_file = 'server.log'  
    error_file = 'error_log.txt'  # Файл для запису помилок

    # Використовуємо генератора для зчитування помилок
    with open(error_file, 'w', encoding='utf-8') as ef:
        for error_line in error_log_generator(log_file):
            ef.write(f"{error_line}\n")

    print(f"Помилки з файлу '{log_file}' збережено у '{error_file}'.")

if __name__ == "__main__":
    main()
