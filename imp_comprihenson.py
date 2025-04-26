def comorihensionlist1():
        listi = []
        for i in range(10):
         listi.append(i)
        # print(listi)
       #trick 
        li = [i for i in range(6)]
        print(li)

#2nd comorihension
def comorihensionlist2():
      
        listtt =[]
        for i in range(50):
                is_even = i%2==0
                if is_even==True:
                      listtt.append(i)
        print(listtt)
        #trick
        evens = [num for num in range(50) if num%2==0]
        print(evens)
# comorihensionlist2()
        
def comorihension3():
      options = ["apple","anmy","moango","any","aam","aamdani","lol","alabany"]
      a_and_y = []

      for strings in options:
            if len(strings) <= 1:
                  continue
            
            if strings[0] != "a":
                  continue
            
            if strings[-1] != "y":
                  continue
            
            a_and_y.append(strings)
#       print(a_and_y)
      #trick
      a_and_y=[strings
                  for strings in options
                  if len(strings) >= 1
                  if strings[0]== "a"
                  if strings[-1]=="y"]  
      print(a_and_y)
# comorihension3()
            


#flatting a matrix (list of list)

def comorihension4():
      matrix = [[1,2,3],[4,5,6],[7,8,9]]
      flatted_list = []
      for row in matrix:
            for num in row:
                  flatted_list.append(num)

      #trick
      flatted_list = [num for row in matrix for num in row]
      print(flatted_list)
# comorihension4()



def comorihension5():
      