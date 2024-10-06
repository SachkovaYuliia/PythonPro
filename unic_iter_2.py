# 2. Ітератор для генерації унікальних ідентифікаторів

# Створіть ітератор, який генерує унікальні ідентифікатори (наприклад, на основі UUID або хеш-функції). Ідентифікатори повинні генеруватися один за одним при кожній ітерації, і бути унікальними.

import hashlib
import itertools

class HashIDIterator:

    def __init__(self):

        # Ініціалізуємо ітератор з лічильником, починаючи з 1.

        self.counter = itertools.count(1)

    def __iter__(self):

        return self

    def __next__(self):

        # Генеруємо новий унікальний хеш на основі лічильника.

        current_value = str(next(self.counter)).encode('utf-8')
        return hashlib.sha256(current_value).hexdigest()

def generate_hash_ids(count):

    # Генеруємо та виводимо на екран певну кількість унікальних хеш-ідентифікаторів.
   
    hash_id_iterator = HashIDIterator()

    for _ in range(count):
        print(next(hash_id_iterator))

#    Наш мейн, точка входу в програму, запитуємо у користувача кількість ітеруємих ідентифікаторів

if __name__ == "__main__":
    try:
        count = int(input("Введіть кількість унікальних ідентифікаторів: "))
        if count > 0:
            generate_hash_ids(count)
        else:
            print("Кількість повинна бути більше 0.")
    except ValueError:
        print("Будь ласка, введіть ціле число.")
