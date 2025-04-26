#fibonacci sereis
''''
num = int(input("entr number for fibonacci : "))
a = 0
b= 1
c = a+b
while (c<=num):
    print(c)
    a = b
    b = c
    c = a+b
'''

#harry

def fiborecursive(n):
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return fiborecursive(n-1) + fiborecursive(n-2)

if __name__ == "__main__":
    no = int(input("enter lenth of rebonacci "))
    print(f"using recusrive {no} is {fiborecursive(no)}")