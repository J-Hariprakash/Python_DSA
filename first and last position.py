def First_and_Last(nums,target):
    low,high = 0,len(nums)-1
    def position():
        i = mid
        j = mid
        while i-1 >= 0 and nums[i-1]==nums[mid]:
            i-=1
        while j+1 < len(nums) and nums[j+1]==nums[mid]:
            j+=1
        return [i,j]
    while low <= high: 
        mid = (low+high)//2
        if target == nums[mid]:
            return position()
        elif target > nums[mid]:
             low=mid+1
        else:
            high=mid-1  
    return [-1,-1]
size = int(input("Enter a size of an array:\n"))
nums = []
for i in range(size):
    elemt = int(input("Enter a required elements needed: \n"))
    nums.append(elemt)
nums.sort()
target = int(input("Enter a targetted value to Search :\n"))
result = First_and_Last(nums,target)
print(result)