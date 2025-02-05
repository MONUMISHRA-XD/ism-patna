
# Find the Sum of the Series 1 + 2 + 3 + 4 + ... + 50 in Python or C?
def one_line_fn():
    print(sum(range(1,51)))
def usingloop():
    sum = 0
    for i in range(1,51):
        sum =sum+i
    print(sum)

def using_math_formula():
    #formula  Sn = n/2(2*a+(n-1)*d)
    #formula Sn = n/2*(first+last)
    sum = 50/2*(1+50)
    print(sum)
#-----------------------------------------------------------------------------------------------------------------------------------------
#Find the Sum of the Series 1²  + 2²  + 3²  + 4²  + ... + 50²  in Python?
    

def usingloop_sq():
    total=0
    for i in range(1,51):
        total = total+i**2  
    print(total)
