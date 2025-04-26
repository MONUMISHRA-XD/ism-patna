name = "ABHINAV KUMAR"
roll = 174
sub1 = int(input("enter marks of python sub : "))
sub2 = int(input("enter marks of english sub : "))
avg = sub1+sub2
total = 200
print("--------------------------------")
print("student name : ",name)
print("Roll : ",roll)
print("python : ",sub1)
print("english : ",sub2)
print("--------------------------------")
print("total : ",total)
print("average : ",avg)
if avg>=180:
    print("rank : exellent")
elif avg>=130 and avg<180:
    print("rank : first")
elif avg>=90 and avg<130:
    print("rank : second")
elif avg>=50 and avg<90:
    print("rank : third")
else :
    print("fail")
