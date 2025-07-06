Num = int(input("Enter a Size of Array :\n"))
list=[]
for i in range(Num):
    Elmts = int(input("enter elements:"))
    list.append(Elmts)
temp = 0
for j in range(Num):
    for k in range(j+1,Num):
        if list[j]>list[k]:
            temp = list[j]
            list[j] = list[k]
            list[k] = temp
print(list)            


    
