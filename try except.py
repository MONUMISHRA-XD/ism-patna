try:
   m =  (input("enter your first number"))
   n = (input("enrter second number "))
   div = m/n
   print(div)
except TypeError as er:
    print(int(m)/int(n))

     
