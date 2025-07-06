Num = int(input("Enter a Size of Pattern: \n"))
for i in range(0,Num-1):
    print()
    for j in range(Num-1,i,-1):
        print(" ",end=" ")
    for j in range(0,2*i+1):
        print("*",end = " ")
for i in range(0,Num):
    print()
    for j in range(0,i):
        print(" ",end=" ")
    k = (2*(Num-i))-1    
    for j in range(0,k):
        print("*",end = " ")