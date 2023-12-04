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
def avg_grade(data):
    result={}
    for student in data:
        average=cal_avgGrade(student['grades'])
        result[student['name']]=average
    return result
file_path="C:/Users/srava/OneDrive/Documents/Assignment/student_records.csv"
data=table(file_path)
result=avg_grade(data)
print("Average Grade of student =",result)

 
