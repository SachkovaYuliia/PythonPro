import os

class FileProcessor:
    
    @staticmethod

    def write_to_file(file_path: str, data: str):

        """
        Записує дані у файл.
        """

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)

    @staticmethod

    def read_from_file(file_path: str) -> str:

        """
        Читає дані з файлу. Якщо файл не існує, викидає виняток.
        """
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл за шляхом {file_path} не знайдено.")
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
