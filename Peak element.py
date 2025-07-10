def peakElement(nums):
    left,right = 0,len(nums)-1                  #
    while left<right:
        mid = (left + right)//2
        if nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid
    return left
size = int(input("Enter a size of Array: \n"))
nums = []
for i in range(0,size):
    elmt = int(input("Enter elememt in an array: \n"))
    nums.append(elmt)
result = peakElement(nums)
print(result)










# Finds any one peak element in O(log n) time using binary search.
# If nums[mid] < nums[mid+1], move right (left = mid + 1) because the slope is increasing.
# Else, move left (right = mid) because a peak must exist on the left side or at mid.
# Loop stops when left == right, which will be a peak index.
# Works because at least one peak always exists in any array.
