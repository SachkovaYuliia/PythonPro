# 5. Генератор для створення нескінченної послідовності

# Створіть генератор, який генерує нескінченну послідовність парних чисел. Використайте менеджер контексту для обмеження кількості генерованих чисел до 100 і збереження їх у файл.

class EvenNumberGenerator:
    def __init__(self):
        self.current = 0 #Наше перше парне число.

    def __iter__(self):
        return self

    def __next__(self):
        even_number = self.current
        self.current += 2 #Шаг 2 для отримання наступного парного числа.
        return even_number

def save_even_numbers_to_file(filename, limit):
    with open(filename, 'w') as file:
        generator = EvenNumberGenerator()
        count = 0
        for even_number in generator:
            if count >= limit:
                break
            file.write(f"{even_number}\n")
            count += 1 #Записуємо кожне парне число в лімітованому діапазоні.

def main():
    filename = 'even_numbers.txt'
    limit = 100
    save_even_numbers_to_file(filename, limit)
    print(f"{limit} парних чисел збережено в {filename}.")

if __name__ == "__main__":
    main()
