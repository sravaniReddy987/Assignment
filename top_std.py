import csv
def table(file_path):
    data=[]
    with open(file_path, 'r') as file:
        csv_file=csv.DictReader(file)
        for row in csv_file:
            data.append(row)
    return data
def cal_avgGrade(student_grades):
    grades=[int(grade) for grade in student_grades.split(',')]
    return sum(grades)//len(grades)
def top_student(data):
    result={}
    for student in data:
        major=student['major']
        grade=cal_avgGrade(student['grades'])
        if major not in result or grade > result[major]['grades']:
            result[major]={'student':student['name'],'grades':grade}
    return result
file_path="C:/Users/srava/OneDrive/Documents/Assignment/student_records.csv"
data=table(file_path)
result=top_student(data)
print("Top Student in Major:",result)
 
