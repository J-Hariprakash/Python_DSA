Num= input("Enter a Number: \n")
Temp = int(Num)
Len = len(Num)
Sum = 0
x = 0
y = 1
for i in range(Len):
    rem = int(Num[x:y])
    cnvt = int(rem)
    Sum += rem**Len
    x +=1
    y +=1
if Sum == Temp:
    print(Temp , "is an Amstrong Number")
else:
    print(Temp , "is not an Amstrong Number")  
