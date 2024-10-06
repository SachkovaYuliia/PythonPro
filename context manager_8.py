# 8. Конфігурація через контекстні менеджери

# Напишіть власний контекстний менеджер для роботи з файлом конфігурацій (формат .ini або .json). Менеджер має автоматично зчитувати конфігурацію при вході в контекст і записувати зміни в файл після завершення роботи.

import json
import os

class ConfigManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = {}

    def __enter__(self):
        # Зчитуємо конфігурацію файлу при вході в контекст
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r', encoding='utf-8') as file:
                self.config_data = json.load(file)
        return self.config_data  # Повертаємо дані конфігурації

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Записуємо конфігурацію у файл при виході з контексту
        with open(self.config_file, 'w', encoding='utf-8') as file:
            json.dump(self.config_data, file, ensure_ascii=False, indent=4)

def main():
    config_file = 'config.json'  # Файл конфігурації

    with ConfigManager(config_file) as config:
        
        print("Поточні налаштування:", config)


        config['Нове налаштування'] = 'item 5'
        config['Інше налаштування'] = 5

    print(f"Зміни збережено у '{config_file}'.")

if __name__ == "__main__":
    main()
