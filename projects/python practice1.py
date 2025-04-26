#write a python program which will keep adding a stream of numbers inputtedj by the user.the addin stops as soon as user presses q key on the keyboard
add = 0
while(True):
    no = input("Enter the price : \n")
    if no !='q':
          add= add + int(no)
          print(f"your current order :  {add}")
    else:
         print(f"your total bill is {add}.Thanks for sopping")
         print("thanks for using our calculator")
         break
