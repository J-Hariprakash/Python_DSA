Num = int(input("enter a Number"))
Sum = 0
Temp = Num
Len = len(str(Num))
while Num > 0:
    Rem = Num%10 
    Sum += Rem**Len
    Num = Num//10
if Sum == Temp:
    print(Temp , "is an Amstrong Number")
else:
    print(Temp , "is not an Amstrong Number")   

    