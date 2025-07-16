l = int(input("enter frist"))
r = int(input("enter second"))

for i in range(l,r+1):
    if i==1:
        continue
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

            
  