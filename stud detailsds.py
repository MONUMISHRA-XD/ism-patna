#write a python script and creATE A fuction and student name,roll no taken from user
#save in ms words
def ismpatna():
    roll = (input("enter your roll   "))
    name = input("enter your name   ")
    course = input("enter your course  ")
    list = [roll,",",name,",",course,"\\"]
    print(list)
    ism = open("ism.txt",'a')
    ism.writelines(list)
    ism.close()
    ismpatna()

ismpatna()

