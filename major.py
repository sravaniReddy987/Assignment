import csv
def table(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            data.append(row)
    return data
def students_major(data):
    result = {}
    for student in data:
        major = student['major']
        if major not in result:
            result[major] = []
        result[major].append(student['name'])
    return result
file_path = "C:/Users/srava/OneDrive/Documents/Assignment/student_records.csv"
data =table(file_path)
result = students_major(data)
print("Classify Students by Major:",result)
 
