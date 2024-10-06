import os
from create_json import create_base_book_list
from books_list import load_books, print_available_books, add_book

def main():
    filename = 'book_list.json' 

    if not os.path.exists(filename):
        create_base_book_list(filename)

    books = load_books(filename)

    print_available_books(books)

    title = input("Введіть назву нової книги: ")
    author = input("Введіть автора нової книги: ")
    year = int(input("Введіть рік видання нової книги: "))
    availability = input("Чи є книга доступною? (True/False): ").lower() == 'true'
    
    add_book(filename, title, author, year, availability)

    books = load_books(filename)
    print_available_books(books)
2024
if __name__ == "__main__":
    main()
