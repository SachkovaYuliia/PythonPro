class AgeVerifier:
    
    @staticmethod
    def is_adult(age: int) -> bool:
        """
        Перевіряє, чи є користувач дорослим.
        Повертає True, якщо вік більше або дорівнює 18, інакше False.

        :param age: Вік користувача
        :return: True або False
        """
        if age < 0:
            raise ValueError("Вік не може бути меншим за 0.")
        return age >= 18