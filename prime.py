pm = int(input("enter the numberr"))

flag =0

for i in range(2,pm):
    if pm%i==0:
        flag = 1
        break
if flag==1:
    print("prime ni hai")
      
else:
    print(" prime hai")


