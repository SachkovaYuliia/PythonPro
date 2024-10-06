# 4. Генератор для обробки великих файлів

# Реалізуйте генератор, який читає великий текстовий файл рядок за рядком (наприклад, лог-файл) і повертає лише ті рядки, що містять певне ключове слово. Використайте цей генератор для фільтрації файлу та запису відповідних рядків у новий файл.

def line_filter_generator(filename, keyword):

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if keyword in line:
                    yield line
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

def save_filtered_lines(input_filename, output_filename, keyword): #Створюємо функцію для фільтру рядків на основі ключового слова та зберігаємо їх у новий файл.

    filtered_lines = line_filter_generator(input_filename, keyword)
    
    try:
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for line in filtered_lines:
                output_file.write(line)
        
        print(f"Відфільтровані рядки збережено у файл '{output_filename}'.")
    except Exception as e:
        print(f"Сталася помилка під час запису у файл: {e}")

def main():
    input_filename = 'large_log.txt'  
    output_filename = 'filtered_log.txt'  
    keyword = input("Введіть ключове слово для пошуку у файлі: ")

    save_filtered_lines(input_filename, output_filename, keyword)

if __name__ == "__main__":
    main()
