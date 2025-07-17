def multiply(num1,num2):
    l1,l2 = [],[]
    st=0
    for j in num1:
        st = st*10+int(j)
    l1.append(st)
    num2= num2[::-1]
    for i in num2:
        l2.append(int(i))
    sum,y = 0,len(l2)-1
    for k in range(y):
        sum += l1[0]*l2[k]*10**k
    return sum
    
num1 = input("Enter a string:\n")
num2 = input("Enter a string:\n")
res = multiply(num1,num2)
print(res)            
    
    