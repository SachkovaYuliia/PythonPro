import json

def load_books(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return []
    except json.JSONDecodeError:
        print("Помилка при розборі JSON.")
        return []

def print_available_books(books):
    available_books = [book for book in books if book["наявність"]]
    if available_books:
        print("Доступні книги:")
        for book in available_books:
            print(f"- {book['назва']} автор: {book['автор']} (Рік: {book['рік']})")
    else:
        print("Немає доступних книг.")

def add_book(filename, title, author, year, availability):
    new_book = {
        "назва": title,
        "автор": author,
        "рік": year,
        "наявність": availability
    }

    try:
        with open(filename, 'r+', encoding='utf-8') as file:
            books = json.load(file) 
            
            for book in books:
                if book['назва'] == title and book['автор'] == author:
                    print("Ця книга вже існує.")
                    return
            
            books.append(new_book)    
            
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(books, file, ensure_ascii=False, indent=4)

    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
    except json.JSONDecodeError:
        print("Помилка при розборі JSON.")
