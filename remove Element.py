def remove(arr,val):
    k = 0
    for i in range(len(arr)):
        if arr[i]!=val:
            arr[k]=arr[i]
            k+=1
    return arr[:k]
size = int(input("Enter Required Size for an array: \n"))
arr = []
for i in range(size):
    elmts = int(input("Enter elements required: \n"))
    arr.append(elmts)
val = int(input("enter a Targetted value:\n"))     
result = remove(arr,val)
print(result)
