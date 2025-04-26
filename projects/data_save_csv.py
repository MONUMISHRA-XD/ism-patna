import csv 
def get_student_data():
    class_name = input("entr your class name:")
    roll_no = int(input("enter your roll number :"))
    reg_no = input("entr your registaion number")
    section = input("enter your section:")
    subject_marks = []
    for i in range(5):
        subject_name = input(f"enter name of subject {i+1}:")
        marks = int(input())
        subject_marks.append((subject_name,subject_marks))
    return [class_name,roll_no,reg_no,section] + subject_marks

def write_to_csv(data):
    with open('data.csv','a',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)
student_data = get_student_data()
write_to_csv(student_data)
print("student data saved to data.csv")
get_student_data()