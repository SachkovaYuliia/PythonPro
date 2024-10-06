import csv

def create_csv_file(students_list):
    with open(students_list, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Ім'я", 'Вік', 'Оцінка'])  
        writer.writerow(['Петро', 21, 90])
        writer.writerow(['Марина', 22, 85])
        writer.writerow(['Андрій', 20, 88])

if __name__ == "__main__":
    create_csv_file('students.csv')