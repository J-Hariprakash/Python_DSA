def removeDuplicates(self,arr):
        newArr =[]
        sortArr = sorted(arr)
        previous = sortArr[0]
        count = 1
        newArr.append(sortArr[0])
        for i in range(1,len(sortArr)):
            if previous != sortArr[i]:
                previous = sortArr[i]
                newArr.append(sortArr[i])
                count+=1
            else:
                continue
        return newArr
size = int(input("Enter Required Size for an array: \n"))
arr = []
for i in range(size):
    elmts = int(input("Enter elements required: \n"))
    arr.append(elmts)     
result = removeDuplicates(arr)
print(result)