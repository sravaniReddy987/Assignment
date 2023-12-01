import csv
def table(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            data.append(row)
    return data
def failing_students(data):
    fail_students = []
    for student in data:
        grades = [int(grade) for grade in student['grades']]
        if any(grade < 70 for grade in grades):
            fail_students.append(student['name'])
    return fail_students
file_path = "C:/Users/srava/OneDrive/Documents/Assignment/student_records.csv"
data=table(file_path)
fail_students = failing_students(data)
print("Failed Students are:",fail_students)
