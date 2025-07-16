def prime(a):
    for j in range(2,a):
        if a%j == 0:
            return False
    else:
        return True
num = int(input("Enter a Number:\n"))
for i in range(2,num+1):
    if num%i ==0:
        if prime(i):
            if i==2 or i==3 or i==5:
                continue
            else:
                print("not ugly")
                break
else:
    print("ugly")

