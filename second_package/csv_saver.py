import requests
import csv

def save_csv(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()

        lines = response.text.splitlines()
        reader = csv.reader(lines)

        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(reader)

        print(f"CSV-дані успішно збережено у {filename}")

    except requests.exceptions.RequestException as err:
        print(f"Помилка запиту: {err}")
