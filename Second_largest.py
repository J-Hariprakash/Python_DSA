def Reversed_array(arr):
    sortArr = list(reversed(sorted(arr)))
    print(sortArr)  
    for i in range(1,len(sortArr)):
        if sortArr[0] > sortArr[i]:
            return sortArr[i]
    else:
        return -1       

arr = list(map(int,input("Enter a elements required:\n").split(' ')))    
result = Reversed_array(arr)
print(result)
