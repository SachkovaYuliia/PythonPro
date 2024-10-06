from update_list import read_and_calculate_average, add_student
from format_converter import csv_to_json, json_to_csv
from students_list import create_csv_file

def main():
    csv_filename = 'students.csv'
    json_filename = 'students.json'

    create_csv_file(csv_filename)

    average_grade, students_list = read_and_calculate_average(csv_filename)
    print(f"Середня оцінка студентів: {average_grade:.2f}")

    name = input("Введіть ім'я нового студента: ")
    age = input("Введіть вік нового студента: ")
    grade = input("Введіть оцінку нового студента: ")

    add_student(csv_filename, name, age, grade)
    print(f"Студента {name} успішно додано!")

    average_grade, students_list = read_and_calculate_average(csv_filename)
    print(f"Нова середня оцінка студентів: {average_grade:.2f}")
    
    csv_to_json(csv_filename, json_filename)
    json_to_csv(json_filename, 'students_converted.csv')

if __name__ == "__main__":
    main()
