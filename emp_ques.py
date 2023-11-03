emp_name = "Abhinav Kumar"
emp_id = 174
basic_salary = int(input("enter the basic salary : "))
print("--------------------------")
TA = (5*basic_salary/100)
DA = (7*basic_salary/100)
HRA = (10*basic_salary/100)
PF = (12*basic_salary/100)
gross_salary = (basic_salary+TA+DA+HRA)
if gross_salary>80000:
    post = "manager"
elif gross_salary<80000 and gross_salary>50000:
    post = "TL"
elif gross_salary<50000 and gross_salary>35000:
    post = "Staff"
elif gross_salary<35000 and gross_salary>10000:
    post = "Peon"

print("emp name : ",emp_name)
print("emp id : ",emp_id)
print("Basic Salary :" ,basic_salary)
print("5% TA : ",TA)
print("7% DA : ",DA)
print("10% HRA : ",HRA)
print("Gross salary : ",gross_salary)

if basic_salary>21800:
    print("12% PF : ",PF)
else:
    print("PF : employee not eligible for PF")
print("post : ",post)


