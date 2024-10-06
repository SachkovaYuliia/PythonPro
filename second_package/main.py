from downloader import download_page
from json_saver import save_json
from csv_saver import save_csv
from xml_saver import save_xml

def main():
    print("Оберіть дію:")
    print("1. Завантажити HTML-сторінку")
    print("2. Завантажити та зберегти JSON")
    print("3. Завантажити та зберегти CSV")
    print("4. Завантажити та зберегти XML")

    choice = input("Введіть номер дії: ")

    if choice == '1':
        url = input("Введіть URL сторінки для завантаження: ")
        filename = "page_content.txt"
        download_page(url, filename)

    elif choice == '2':
        url = input("Введіть URL з JSON-даними: ")
        filename = "data.json"
        save_json(url, filename)

    elif choice == '3':
        url = input("Введіть URL з CSV-даними: ")
        filename = "data.csv"
        save_csv(url, filename)

    elif choice == '4':
        url = input("Введіть URL з XML-даними: ")
        filename = "data.xml"
        save_xml(url, filename)

    else:
        print("Невірний вибір. Спробуйте знову.")

if __name__ == "__main__":
    main()
