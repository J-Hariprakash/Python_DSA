def Reversed_array(arr):
    sortArr = list(reversed(sorted(arr)))
    print(sortArr)  
    for i in range(1,len(sortArr)):
        if sortArr[0] > sortArr[i]:
            return sortArr[i]
    else:
        return -1       
size = int(input("Enter Required Size for an array: \n"))
arr = []
for i in range(size):
    elmts = int(input("Enter elements required: \n"))
    arr.append(elmts)     
result = Reversed_array(arr)
print(result)
