def Find_lcm(a,b):
    Number = max(a,b)
    while True:
        if Number%a==0 and Number%b==0:
            return Number
        else:    
            Number+=1

def Find_gcd(a,b):
    Number = min(a,b)
    while Number>0:
        if a%Number==0 and b%Number==0:
            return Number
        else:
            Number-=1

Size = int(input("Enter a Size of list needed : \n"))
list=[]
for Element in range(Size):
    #Elmts = int(input("Enter Elements Required\n"))
    list.append(int(input("Enter Elements Required\n")))
     
while True:
    Option = int(input("Enter an Option : \n 1.LCM \n 2.GCD \n 3.Exit \n"))
    if Option ==1:
      first = list[0]
      for i in range(1,Size):
        first = Find_lcm(first,list[i])
      print("LCM of Given numbers :",first)    
    elif Option==2:
      first = list[0]
      for i in range(1,Size):
        first = Find_gcd(first,list[i])
      print("GCD of Given Numbers :",first)
    elif Option==3:
      print("exited from Program Successfully")
      break
    else:
       print("enter a Vaild Number again")



     
           





            



