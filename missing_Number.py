def missing(arr):
    sortArr = sorted(arr)
    for i in range(len(sortArr)):
        if i != sortArr[i]:
            return i
    else:
        return len(sortArr)  
size = int(input("Enter Required Size for an array: \n"))
arr = []
for i in range(size):
    elmts = int(input("Enter elements required: \n"))
    arr.append(elmts)     
result = missing(arr)
print(result)