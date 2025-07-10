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






# In a rotated sorted array with no duplicates, the minimum element is the only point where order breaks.
# Use binary search: if nums[mid] > nums[right], min must be in right half → left = mid + 1.
# Else, the min is in left half (including mid) → right = mid.
# When left == right, that index holds the minimum element.



