""""WAP to find the sum and avg of odd and even index of a  list """
listt = []
def create_list():
    listt = []
    count = 0
    num_of_data = int(input("how many data you want to add in list :"))
    for i in range(num_of_data):
             data = int(input("enter the data for store in list :"))
             listt.append(data)
    
             count=count+1
    print("list is here: ",listt)

    

    print("""choose your option 😶
          enter 1 for find sum of even index
          enter 2 for find sum of odd index
           enter 3 for find avg of list 
          enter any key for exit😷""")
    choose = int(input("enter the option : "))

    def sum_odd_index():
           print(sum(listt[::2]))
    def sum_even_index():
           print(sum(listt[1::2]))
    def avg_listt():
           avg = sum(listt)/len(listt)
           print(f"average is {avg} of this list ")

    if choose==1:
           sum_even_index()
    elif choose==2:
           sum_odd_index()
    elif choose==3:
           avg_listt()
    else:
           print("you entered wrong option (:  )")
           exit()

    
create_list()
