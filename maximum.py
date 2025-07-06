def maximum(nums):
    max_elmts = nums[0]
    intial_max = nums[0]
    for i in range(1,len(nums)):
        add = intial_max + nums[i]
        if add > nums[i]:
            intial_max = add
        else:
            intial_max = nums[i]
        if intial_max > max_elmts:
            max_elmts = intial_max
    return max_elmts
    
size = int(input("Enter Required Size for an array: \n"))
nums = []
for i in range(size):
    elmts = int(input("Enter elements required: \n"))
    nums.append(elmts)     
result = maximum(nums)
print(result)