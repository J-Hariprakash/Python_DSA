def rotation_left(nums,k):
    l = len(nums)
    k %=l
    k = l-k                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       2 
    nums.reverse() 
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k])           
    return nums
size = int(input("Enter Required Size for an array: \n"))
arr = []
for i in range(size):
    elmts = int(input("Enter elements required: \n"))
    arr.append(elmts)
nums = sorted(arr)
k = int(input("Enter number of rotaton required of an array: \n"))         
result = rotation_left(nums,k)
print(result)