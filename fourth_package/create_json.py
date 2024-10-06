import json

def create_base_book_list(book_list):
    books = [
        {"назва": "Вечірка в Геловвін", "автор": "Агата Крісті", "рік": 2022, "наявність": True},
        {"назва": "Комісар Мегре", "автор": "Жорж Сіменон", "рік": 2018, "наявність": False},
        {"назва": "Паризькі години", "автор": "Алекс Джордж", "рік": 2020, "наявність": False}
    ]

    with open(book_list, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

    print(f"Файл {book_list} успішно створено з базовим списком книг.")
