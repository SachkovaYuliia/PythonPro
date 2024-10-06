# 1. Створення власного ітератора для зворотного читання файлу

# Напишіть власний ітератор, який буде зчитувати файл у зворотному порядку — рядок за рядком з кінця файлу до початку. Це може бути корисно для аналізу лог-файлів, коли останні записи найважливіші.

class ReverseFileIterator:
    def __init__(self, filename):
        self.file = open(filename, 'r', encoding='utf-8')
        self.lines = self.file.readlines()
        self.current_line = len(self.lines) - 1  # Індекс останнього рядка

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_line < 0:
            self.file.close()  
            raise StopIteration
        line = self.lines[self.current_line]
        self.current_line -= 1 # Переходимо до попереднього рядка
        return line.rstrip('\n')  

if __name__ == "__main__":
    filename = 'my.log'  
    reverse_iterator = ReverseFileIterator(filename)

    for line in reverse_iterator:
        print(line)
