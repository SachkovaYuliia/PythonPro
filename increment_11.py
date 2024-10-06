# 11. Інкрементне обчислення середніх значень (опціонально)

# Напишіть генератор, який по черзі зчитує великий файл даних (наприклад, числові показники продуктивності), обчислює середнє значення на кожній ітерації та оновлює результат. Це корисно для обробки великих даних, які не можна завантажити повністю в пам'ять.

def average_generator(file_path):
    total_sum = 0.0
    count = 0

    with open(file_path, 'r') as file:
        for line in file:
            try:
                # Перетворюємо рядок у число
                number = float(line.strip())
                total_sum += number
                count += 1
                current_average = total_sum / count
                yield current_average  # Повертаємо середнє значення на кожній ітерації
            except ValueError:
                print(f"Не вдалося перетворити рядок '{line.strip()}' у число. Пропускаємо.")

def main():
    file_path = 'even_numbers.txt'  

    with open(file_path, 'w') as f:
        for i in range(1, 101):  # Записуємо числа від 1 до 100
            f.write(f"{i}\n")

    # Використовуємо генератор для обчислення середніх значень
    avg_gen = average_generator(file_path)
    
    for avg in avg_gen:
        print(f"Поточне середнє значення: {avg:.2f}")

if __name__ == "__main__":
    main()
