#problems = how to int values in .txt files,,,,how to make newline in easy way,,,how to open automaticly txt file after save
#               how to labels in txt file


name = input("entr your name")
classs= input("entr your class")
sec = input("entr your sec")
roll_no = (input("entr your roll"))

sci = int(input("entr your science marks"))
maths = int(input("enter your maths marks"))
eng = int(input("enter your english marks"))
social = int(input("enter your social science marks"))
hindi =int(input("enter your hindi marks"))

avg  = ((sci+maths+eng+social+hindi)/5)

if avg>=70:
    avg = "remarks: passed"
    print(avg)
else:
    avg = "remarks: fail"
    print(avg)

dict = {name:"name",classs:"class",sec:"section",roll_no:"roll no ",avg:"remarks"}

file= open("saved_data.txt","a")
file.writelines(dict)
#file.writelines(classs)
#file.writelines(sec)
#file.writelines(roll_no)
#file.writelines(avg)
#file.open("saved_data.txt","r")
file.close()

