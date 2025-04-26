def cal():
    m = int(input("enter your first number "))
    n = int(input("enter your second number "))
    print("prss 1 forr addition\n press 2 forr multiplication")
    reult = int(input("what you want"))
    if reult ==1:
        print("addtion of this ",m+n)
    elif reult == 2:
        print("multiplication of thhis",m*n)
    else:
        print("this is worng")
okk = int(input("       press 1 for cal\n         press two for area of crcle\n"))
def circ():
    m = int(input("enter the radios of circle"))
    pai = 22/7

    formula = (pai*m**2)
    print("area of this circle is",formula)

def areatringle():  
    print("python script to calculate area of triangle length\n")
    b=int(input("enter the value of these base"))
    h=int(input("enter the value of these hight"))
    print("the value of these=",1/2*b*h)








    
if okk==1:
    cal()
elif okk == 2:
    circ()
if okk == 3:
    areatringle()
