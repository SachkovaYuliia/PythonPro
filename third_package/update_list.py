import csv

def read_and_calculate_average(filename):
    students = []
    total_grade = 0
    student_count = 0

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            students.append(row)
            total_grade += int(row['Оцінка'])
            student_count += 1

    average_grade = total_grade / student_count if student_count else 0
    return average_grade, students

def add_student(filename, name, age, grade):
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, age, grade])
