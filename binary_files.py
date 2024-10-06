# 12. Зчитування великих бінарних файлів (опціонально)
# Напишіть програму, яка використовує менеджер контексту для зчитування бінарних файлів великими блоками даних (наприклад, по 1024 байти). Виведіть кількість прочитаних байт.

class BinaryFileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, 'rb')  # Відкриваємо файл у бінарному режимі
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()  # Закриваємо файл

    def read_blocks(self, block_size=1024):
        while True:
            block = self.file.read(block_size)  # Зчитуємо блоки
            if not block:  # Якщо нічого не залишилось, виходимо з циклу
                break
            yield block

def main():
    file_path = 'large_file.bin'  

    
    with open(file_path, 'wb') as f:
        f.write(b'\x00' * (5 * 1024 * 1024)) 

    total_bytes_read = 0

    with BinaryFileReader(file_path) as reader:
        for block in reader.read_blocks():
            bytes_read = len(block)
            total_bytes_read += bytes_read
            print(f"Прочитано {bytes_read} байт.")

    print(f"\n Загальна кількість прочитаних байт: {total_bytes_read} байт.")

if __name__ == "__main__":
    main()
