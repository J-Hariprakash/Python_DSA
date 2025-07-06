def modifiedBinarySearch(nums,target):    
    low,high = 0,len(nums)-1
    while low <= high: 
        mid = (low+high)//2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
             low=mid+1
        else:
            high=mid-1  
    return -1
def rotate(arr):
    l = len(arr)
    k = 1
    for i in range(1,l):
        if arr[i-1]<arr[i]:
           k+=1
        else:
            break
    res1 = modifiedBinarySearch(arr[:k],target)
    if res1!=-1:
        return res1
    res2 = modifiedBinarySearch(arr[k:],target)
    if res2!=-1:
        return res2+k
    return -1
size = int(input("Enter a size of an numsay:\n"))
arr = []
for i in range(size):
    elemt = int(input("Enter a required elements needed: \n"))
    arr.append(elemt)
target = int(input("Enter a targetted value to Search :\n"))
result = rotate(arr)
print(result)