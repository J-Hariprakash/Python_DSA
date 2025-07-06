Num = int(input("Enter a Size of Array :\n"))
list=[]
for i in range(Num):
    Elmts = int(input("enter elements:"))
    list.append(Elmts)
temp = 0
for j in range(Num):
    for k in range(Num-1):
        if list[k]>list[k+1]:
            temp = list[k]
            list[k] = list[k+1]
            list[k+1] = temp
print(list)            
