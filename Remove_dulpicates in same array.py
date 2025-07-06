def Remove_Duplicate(nums):
    nums.sort()
    k = 2
    for i in range(2,len(nums)):
        if nums[i]!= nums[k-2]:
            nums[k] = nums[i]
            k+=1
    return  f'{k},nums = {nums[:k]}'
size = int(input("Enter Required Size for an array: \n"))
nums = []
for i in range(size):
    elmts = int(input("Enter elements required: \n"))
    nums.append(elmts)     
result = Remove_Duplicate(nums)
print(result)