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
          enter 4 for find the difference between sum of even and odd
          enter any key for exit😷""")
    choose = int(input("enter the option : "))

    def sum_odd_index():
           global odd_sum
           odd_sum = sum(listt[1::2])
           print(odd_sum)
    def sum_even_index():
           global even_sum 
           even_sum = sum(listt[::2])
           print(even_sum)
    def avg_listt():
           avg = sum(listt)/len(listt)
           print(f"average is {avg} of this list ")
    def difference_of_odd_and_sum():
             odd_sum = sum(listt[1::2])
             even_sum = sum(listt[::2])
             if odd_sum>even_sum:
                    print(odd_sum-even_sum)
             else:
                    print(even_sum-odd_sum)   
    if choose==1:
              sum_even_index()
    elif choose==2:
              sum_odd_index()
    elif choose==3:
              avg_listt()
    elif choose==4:
            difference_of_odd_and_sum()
    else:
              print("you entered wrong option (:  )")
              exit()
      
    
create_list()
