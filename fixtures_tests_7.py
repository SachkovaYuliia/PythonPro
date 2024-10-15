# Завдання 7. Тестування з використанням фікстур та тимчасових файлів

# Напишіть програму для роботи з файлами та протестуйте її, використовуючи тимчасові файли та фікстури в pytest. Реалізуйте клас FileProcessor, який має такі методи:

# write_to_file(file_path: str, data: str): записує дані у файл.
# read_from_file(file_path: str) -> str: читає дані з файлу.

import pytest
from fileProcessor_for_fixtures import FileProcessor


def test_file_write_read(tmpdir):
    """
    Тестує запис і читання простого рядка у файл.
    Створюється тимчасовий файл 'testfile.txt', в який записується рядок
    "Hello, World!", після чого він зчитується і перевіряється.
    """
    file = tmpdir.join("testfile.txt")

    FileProcessor.write_to_file(file, "Hello, World!")

    content = FileProcessor.read_from_file(file)

    assert content == "Hello, World!"


def test_large_data_write_read(tmpdir):
    """
    Тестує запис і читання великого обсягу даних.
    Створюється тимчасовий файл 'largefile.txt', в який записується 10,000
    символів 'A', після чого ці дані зчитуються і перевіряються.
    """
    file = tmpdir.join("largefile.txt")
    large_data = "A" * 10000 

    FileProcessor.write_to_file(file, large_data)

    content = FileProcessor.read_from_file(file)

    assert content == large_data


def test_empty_data_write_read(tmpdir):
    """
    Тестує запис і читання порожнього рядка.
    Створюється тимчасовий файл 'emptyfile.txt', в який записується порожній
    рядок, після чого він зчитується і перевіряється.
    """
    file = tmpdir.join("emptyfile.txt")

    FileProcessor.write_to_file(file, "")


    content = FileProcessor.read_from_file(file)

    assert content == ""


def test_read_nonexistent_file(tmpdir):
    """
    Тестує виклик винятку при спробі читати неіснуючий файл.
    Перевіряється, що при спробі читання неіснуючого файлу виникає
    FileNotFoundError з відповідним повідомленням.
    """
    nonexistent_file = tmpdir.join("nonexistentfile.txt")

    with pytest.raises(FileNotFoundError, match="Файл за шляхом .* не знайдено."):
        FileProcessor.read_from_file(nonexistent_file)
