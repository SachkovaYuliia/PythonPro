class StringProcessor:
    """Клас для обробки рядків."""

    def reverse_string(self, s: str) -> str:
        """Повертає перевернутий рядок."""
        return s[::-1]

    def capitalize_string(self, s: str) -> str:
        """Повертає рядок з першою великою літерою."""
        return s.capitalize()

    def count_vowels(self, s: str) -> int:
        """Повертає кількість голосних у рядку."""
        vowels = 'aeiouAEIOU'
        return sum(1 for char in s if char in vowels)
