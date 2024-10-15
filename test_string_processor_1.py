# Завдання 1. Модульне тестування з використанням unittest

# Напишіть простий застосунок для обробки рядків та напишіть модульні тести з використанням бібліотеки unittest. Створіть клас StringProcessor з методами:

# reverse_string(s: str) -> str: повертає перевернутий рядок.
# capitalize_string(s: str) -> str: робить першу літеру рядка великої.
# count_vowels(s: str) -> int: повертає кількість голосних у рядку.
# Напишіть тести для кожного методу, перевіряючи кілька різних сценаріїв:

# порожні рядки,
# рядки з різними регістрами,
# рядки з цифрами та символами.
# Використовуйте декоратор @unittest.skip для пропуску тесту, який тестує метод reverse_string з порожнім рядком, оскільки це відома проблема, яку ви плануєте вирішити пізніше.

import unittest
from string_processor import StringProcessor

class TestStringProcessor(unittest.TestCase):
    """
    Клас для тестування методів StringProcessor.
    """

    def setUp(self):
        """
        Ініціалізація об'єкту перед кожним тестом.
        """

        self.processor = StringProcessor()

    @unittest.skip("Пропускаємо цей тест, поки проблема не буде вирішена.")
    def test_reverse_empty_string(self):
        """
        Тест для перевірки перевертання порожнього рядка (пропускається).
        """

        self.assertEqual(self.processor.reverse_string(''), '')

    def test_reverse_string(self):
        """
        Тест для перевірки перевертання рядка.
        """
        
        self.assertEqual(self.processor.reverse_string('hello'), 'olleh')
        self.assertEqual(self.processor.reverse_string('12345'), '54321')

    def test_capitalize_string(self):
        """
        Тест для перевірки капіталізації рядка.
        """

        self.assertEqual(self.processor.capitalize_string('hello'), 'Hello')
        self.assertEqual(self.processor.capitalize_string('Hello'), 'Hello')
        self.assertEqual(self.processor.capitalize_string('123hello'), '123hello')

    def test_count_vowels(self):
        """
        Тест для перевірки кількості голосних.
        """
        
        self.assertEqual(self.processor.count_vowels('hello'), 2)
        self.assertEqual(self.processor.count_vowels('HELLO'), 2)
        self.assertEqual(self.processor.count_vowels('12345'), 0)
        self.assertEqual(self.processor.count_vowels(''), 0)
        self.assertEqual(self.processor.count_vowels('AEIOUaeiou'), 10)

if __name__ == '__main__':
    unittest.main()
