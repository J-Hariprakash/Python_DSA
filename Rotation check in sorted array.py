def checkSort(nums):
    count = 0
    length = len(nums)
    for i in range(length-1):
        if nums[i] > nums[i+1]:
            count +=1
        if i == 0:
         if nums[length-1] > nums[i]:
            count+=1      
    if count > 1:
        return False
    else:
        return True        
size = int(input("Enter Required Size for an numsay: \n"))
nums = []
for i in range(size):
    elmts = int(input("Enter elements required: \n"))
    nums.append(elmts)
result = checkSort(nums)
print(result)