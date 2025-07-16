num = int(input("enter:\n"))
l =[]
while True:
    sum = 0
    while num>0:
        rem = num%10
        sum += rem**2
        num//=10
    if sum == 1:
        print(" happy")
        break
    if sum in l:
        print("sad")
        break
    l.append(sum)
    num = sum