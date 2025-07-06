def searchInsert(arr,target ):

    low,high = 0,len(arr)-1
    while low <= high: 
        mid = (low+high)//2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
             low=mid+1
        else:
            high=mid+1  
    else:
        if arr[mid]>target:
            return mid
        else:
            return mid +1
size = int(input("Enter a size of an array:\n"))
arr = []
for i in range(size):
    elemt = int(input("Enter a required elements needed: \n"))
    arr.append(elemt)
arr.sort()
target = int(input("Enter a targetted value to Search :\n"))
result = searchInsert(arr,target)
print(result)