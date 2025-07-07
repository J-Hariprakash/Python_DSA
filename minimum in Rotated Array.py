def min_Rotated(nums):
    left,right = 0,len(nums)-1
    while left<right:
        mid = (left + right)//2
        if nums[mid]>nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
size = int(input("Enter a size of Array: \n"))
nums = []
for i in range(0,size):
    elmt = int(input("Enter elememt in an array: \n"))
    nums.append(elmt)
result = min_Rotated(nums)
print(result)




