import csv
import json

def csv_to_json(csv_filename, json_filename):
    students = []
    with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            students.append(row)
    
    with open(json_filename, mode='w', encoding='utf-8') as json_file:
        json.dump(students, json_file, ensure_ascii=False, indent=4)
    print(f"Файл {csv_filename} успішно перетворено в {json_filename}.")

def json_to_csv(json_filename, csv_filename):
    with open(json_filename, mode='r', encoding='utf-8') as json_file:
        students = json.load(json_file)

    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['Ім\'я', 'Вік', 'Оцінка'])
        writer.writeheader()
        for student in students:
            writer.writerow(student)
    print(f"Файл {json_filename} успішно перетворено в {csv_filename}.")
