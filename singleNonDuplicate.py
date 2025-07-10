def singleNonDuplicate(nums):
    left,right = 0,len(nums)-1                  #
    while left<right:
        mid = (left + right)//2
        if mid % 2==1:
            mid -=1
        if nums[mid] != nums[mid+1]:
            right = mid
        else:
            left = mid+2
    return nums[left]
size = int(input("Enter a size of Array: \n"))
nums = []
for i in range(0,size):
    elmt = int(input("Enter elememt in an array: \n"))
    nums.append(elmt)
result = singleNonDuplicate(nums)
print(result)




# In a sorted array where every element appears twice except one, pairs start at even indexes.
# If nums[mid] == nums[mid + 1], it's a valid pair → skip both with mid + 2.
# If not, the unique element is at or before mid → shrink search space to the left.
# Always make mid even before comparing, to safely check the first of each pair.
